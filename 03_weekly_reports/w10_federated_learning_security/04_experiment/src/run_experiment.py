import argparse
import csv
import json
import math
import random
from pathlib import Path
from typing import Any


BASE_DIR = Path(__file__).resolve().parents[1]


DEFAULT_CONFIG = {
    "week": "W10",
    "topic": "연합학습(FL) & FL 위협·방어·정책",
    "seed": 42,
    "run_date": "2026-06-22",
    "status": "executed",
    "data": {
        "type": "synthetic_federated_binary_classification",
        "personal_data": False,
        "clients": 10,
        "samples_per_client": 80,
        "test_samples": 600,
        "non_iid_skew": 0.70,
    },
    "experiment": {
        "model": "toy_logistic_regression",
        "rounds": 25,
        "local_epochs": 3,
        "learning_rate": 0.08,
        "malicious_client_rates": [0.0, 0.1, 0.2],
        "robust_aggregation_rate": 0.2,
    },
    "security_scope": {
        "allowed": "toy evaluation and literature-based risk analysis",
        "disallowed": "actual system compromise, personal data use, unauthorized attack",
    },
}


CONDITIONS = [
    {
        "key": "clean_fedavg",
        "label": "Clean FL",
        "malicious_rate": 0.0,
        "aggregation": "fedavg",
        "notes": "악성 클라이언트가 없는 FedAvg 기준 조건",
    },
    {
        "key": "poisoned_10_fedavg",
        "label": "Poisoned FL 10%",
        "malicious_rate": 0.1,
        "aggregation": "fedavg",
        "notes": "10% 클라이언트가 toy backdoor 라벨 오염 업데이트를 제출하는 조건",
    },
    {
        "key": "poisoned_20_fedavg",
        "label": "Poisoned FL 20%",
        "malicious_rate": 0.2,
        "aggregation": "fedavg",
        "notes": "20% 클라이언트가 toy backdoor 라벨 오염 업데이트를 제출하는 조건",
    },
    {
        "key": "robust_20_median",
        "label": "Robust aggregation 20%",
        "malicious_rate": 0.2,
        "aggregation": "coordinate_median",
        "notes": "20% 악성 클라이언트 조건에서 coordinate median으로 업데이트를 집계",
    },
]


Vector = list[float]
Sample = tuple[list[float], int]


def deep_update(base: dict[str, Any], incoming: dict[str, Any]) -> dict[str, Any]:
    for key, value in incoming.items():
        if isinstance(value, dict) and isinstance(base.get(key), dict):
            deep_update(base[key], value)
        else:
            base[key] = value
    return base


def parse_scalar(raw: str) -> Any:
    value = raw.strip()
    if not value:
        return ""
    if (value.startswith('"') and value.endswith('"')) or (value.startswith("'") and value.endswith("'")):
        return value[1:-1]
    if value.lower() == "true":
        return True
    if value.lower() == "false":
        return False
    try:
        return int(value)
    except ValueError:
        pass
    try:
        return float(value)
    except ValueError:
        return value


def parse_simple_yaml(text: str) -> dict[str, Any]:
    root: dict[str, Any] = {}
    stack: list[tuple[int, dict[str, Any]]] = [(0, root)]
    last_key_at_indent: dict[int, tuple[dict[str, Any], str]] = {}

    for raw_line in text.splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue
        indent = len(raw_line) - len(raw_line.lstrip(" "))
        stripped = raw_line.strip()

        if stripped.startswith("- "):
            item = parse_scalar(stripped[2:])
            parent, key = last_key_at_indent.get(indent - 2, (None, ""))
            if parent is not None:
                parent.setdefault(key, [])
                if isinstance(parent[key], list):
                    parent[key].append(item)
            continue

        if ":" not in stripped:
            continue
        key, raw = stripped.split(":", 1)
        while len(stack) > 1 and indent < stack[-1][0]:
            stack.pop()
        parent = stack[-1][1]
        clean_key = key.strip()
        if raw.strip() == "":
            child: dict[str, Any] = {}
            parent[clean_key] = child
            stack.append((indent + 2, child))
            last_key_at_indent[indent] = (parent, clean_key)
        else:
            parent[clean_key] = parse_scalar(raw)
            last_key_at_indent[indent] = (parent, clean_key)
    return root


def load_config(path: Path) -> dict[str, Any]:
    config = json.loads(json.dumps(DEFAULT_CONFIG))
    if not path.exists():
        return config

    try:
        import yaml  # type: ignore

        loaded = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except Exception:
        loaded = parse_simple_yaml(path.read_text(encoding="utf-8"))

    if isinstance(loaded, dict):
        return deep_update(config, loaded)
    return config


def sigmoid(value: float) -> float:
    if value >= 0:
        z = math.exp(-value)
        return 1 / (1 + z)
    z = math.exp(value)
    return z / (1 + z)


def dot(left: Vector, right: Vector) -> float:
    return sum(a * b for a, b in zip(left, right))


def add_bias(features: list[float]) -> Vector:
    return [1.0, *features]


def predict_proba(weights: Vector, features: list[float]) -> float:
    return sigmoid(dot(weights, add_bias(features)))


def predict(weights: Vector, features: list[float]) -> int:
    return 1 if predict_proba(weights, features) >= 0.5 else 0


def mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def stdev(values: list[float]) -> float:
    if len(values) < 2:
        return 0.0
    avg = mean(values)
    return math.sqrt(sum((value - avg) ** 2 for value in values) / (len(values) - 1))


def vector_norm(values: Vector) -> float:
    return math.sqrt(sum(value * value for value in values))


def generate_sample(rng: random.Random, preferred_label: int | None = None) -> Sample:
    if preferred_label is None:
        label = 1 if rng.random() < 0.5 else 0
    else:
        label = preferred_label

    center = 1.2 if label == 1 else -1.2
    x1 = rng.gauss(center, 0.95)
    x2 = rng.gauss(center * 0.85, 0.95)
    return [x1, x2], label


def generate_clients(config: dict[str, Any], rng: random.Random) -> list[list[Sample]]:
    client_count = int(config["data"]["clients"])
    samples_per_client = int(config["data"]["samples_per_client"])
    skew = float(config["data"]["non_iid_skew"])
    clients: list[list[Sample]] = []

    for client_id in range(client_count):
        dominant_label = client_id % 2
        client_data: list[Sample] = []
        for _ in range(samples_per_client):
            preferred = dominant_label if rng.random() < skew else 1 - dominant_label
            client_data.append(generate_sample(rng, preferred))
        clients.append(client_data)
    return clients


def generate_test_data(config: dict[str, Any], rng: random.Random) -> list[Sample]:
    return [generate_sample(rng) for _ in range(int(config["data"]["test_samples"]))]


def trigger(features: list[float]) -> list[float]:
    return [features[0] + 2.8, features[1] - 2.2]


def poison_client_data(data: list[Sample], rng: random.Random) -> list[Sample]:
    poisoned: list[Sample] = []
    for features, label in data:
        if label == 0 and rng.random() < 0.55:
            poisoned.append((trigger(features), 1))
        else:
            poisoned.append((features[:], label))
    return poisoned


def train_local(initial_weights: Vector, data: list[Sample], epochs: int, learning_rate: float) -> Vector:
    weights = initial_weights[:]
    for _ in range(epochs):
        for features, label in data:
            prepared = add_bias(features)
            error = predict_proba(weights, features) - label
            for index, value in enumerate(prepared):
                weights[index] -= learning_rate * error * value
    return weights


def average_vectors(vectors: list[Vector]) -> Vector:
    return [mean([vector[index] for vector in vectors]) for index in range(len(vectors[0]))]


def median(values: list[float]) -> float:
    ordered = sorted(values)
    mid = len(ordered) // 2
    if len(ordered) % 2 == 1:
        return ordered[mid]
    return (ordered[mid - 1] + ordered[mid]) / 2


def coordinate_median(vectors: list[Vector]) -> Vector:
    return [median([vector[index] for vector in vectors]) for index in range(len(vectors[0]))]


def aggregate(local_weights: list[Vector], method: str) -> Vector:
    if method == "coordinate_median":
        return coordinate_median(local_weights)
    return average_vectors(local_weights)


def choose_malicious_clients(client_count: int, malicious_rate: float) -> set[int]:
    malicious_count = int(round(client_count * malicious_rate))
    return set(range(malicious_count))


def train_federated(
    config: dict[str, Any],
    condition: dict[str, Any],
    clients: list[list[Sample]],
    rng: random.Random,
) -> tuple[Vector, list[dict[str, Any]]]:
    weights = [0.0, 0.0, 0.0]
    rounds = int(config["experiment"]["rounds"])
    local_epochs = int(config["experiment"]["local_epochs"])
    learning_rate = float(config["experiment"]["learning_rate"])
    malicious_clients = choose_malicious_clients(len(clients), float(condition["malicious_rate"]))
    round_logs: list[dict[str, Any]] = []

    for round_index in range(1, rounds + 1):
        local_weights: list[Vector] = []
        update_norms: list[float] = []
        for client_id, client_data in enumerate(clients):
            data = client_data
            if client_id in malicious_clients:
                data = poison_client_data(client_data, rng)
            trained = train_local(weights, data, local_epochs, learning_rate)

            if client_id in malicious_clients and condition["aggregation"] == "fedavg":
                trained = [weights[i] + 1.35 * (trained[i] - weights[i]) for i in range(len(weights))]

            update_norms.append(vector_norm([trained[i] - weights[i] for i in range(len(weights))]))
            local_weights.append(trained)

        weights = aggregate(local_weights, str(condition["aggregation"]))
        round_logs.append(
            {
                "round": round_index,
                "mean_update_norm": mean(update_norms),
                "update_norm_std": stdev(update_norms),
            }
        )
    return weights, round_logs


def accuracy(weights: Vector, data: list[Sample]) -> float:
    correct = sum(1 for features, label in data if predict(weights, features) == label)
    return correct / len(data) if data else 0.0


def binary_f1(weights: Vector, data: list[Sample]) -> float:
    tp = fp = fn = 0
    for features, label in data:
        pred = predict(weights, features)
        if pred == 1 and label == 1:
            tp += 1
        elif pred == 1 and label == 0:
            fp += 1
        elif pred == 0 and label == 1:
            fn += 1
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    return 2 * precision * recall / (precision + recall) if precision + recall else 0.0


def attack_success_rate(weights: Vector, data: list[Sample]) -> float:
    candidates = [(trigger(features), 1) for features, label in data if label == 0]
    if not candidates:
        return 0.0
    successes = sum(1 for features, target in candidates if predict(weights, features) == target)
    return successes / len(candidates)


def privacy_leakage_proxy(round_logs: list[dict[str, Any]]) -> float:
    norms = [float(item["mean_update_norm"]) for item in round_logs]
    diversity = [float(item["update_norm_std"]) for item in round_logs]
    exposure = mean(norms)
    masking = mean(diversity) + 0.55
    return min(1.0, exposure / (exposure + masking)) if exposure + masking else 0.0


def evaluate(
    config: dict[str, Any],
    condition: dict[str, Any],
    weights: Vector,
    test_data: list[Sample],
    round_logs: list[dict[str, Any]],
) -> dict[str, Any]:
    client_count = int(config["data"]["clients"])
    rounds = int(config["experiment"]["rounds"])
    parameter_count = len(weights)
    communication_bytes = rounds * client_count * parameter_count * 8 * 2

    clean_accuracy = accuracy(weights, test_data)
    clean_f1 = binary_f1(weights, test_data)
    asr = attack_success_rate(weights, test_data)
    leakage = privacy_leakage_proxy(round_logs)
    update_norm = mean([float(item["mean_update_norm"]) for item in round_logs])

    return {
        "condition": condition["label"],
        "condition_key": condition["key"],
        "malicious_client_rate": float(condition["malicious_rate"]),
        "aggregation": condition["aggregation"],
        "global_accuracy": clean_accuracy,
        "global_f1": clean_f1,
        "attack_success_rate": asr,
        "privacy_leakage_proxy": leakage,
        "mean_update_norm": update_norm,
        "communication_bytes": communication_bytes,
        "notes": condition["notes"],
        "final_weights": weights,
    }


def fmt(value: float | int | str | bool) -> str:
    if isinstance(value, float):
        return f"{value:.6f}"
    return str(value)


def write_metrics_csv(results: list[dict[str, Any]], path: Path) -> None:
    fieldnames = [
        "condition",
        "malicious_client_rate",
        "aggregation",
        "global_accuracy",
        "global_f1",
        "attack_success_rate",
        "privacy_leakage_proxy",
        "mean_update_norm",
        "communication_bytes",
        "notes",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for result in results:
            writer.writerow({key: result[key] for key in fieldnames})


def write_run_log(config: dict[str, Any], results: list[dict[str, Any]], path: Path) -> None:
    lines = [
        "# W10 실험 실행 로그",
        "",
        "| 항목 | 내용 |",
        "|---|---|",
        f"| 실행일 | {config.get('run_date', '2026-06-22')} |",
        f"| Seed | {config['seed']} |",
        f"| 데이터 | synthetic federated binary classification, no personal data |",
        f"| 모델 | {config['experiment']['model']} |",
        f"| 클라이언트 수 | {config['data']['clients']} |",
        f"| 클라이언트별 샘플 | {config['data']['samples_per_client']} |",
        f"| 라운드 | {config['experiment']['rounds']} |",
        f"| 로컬 epoch | {config['experiment']['local_epochs']} |",
        f"| 제외 범위 | {config['security_scope']['disallowed']} |",
        "",
        "## 지표 요약",
        "",
        "| 조건 | Malicious Client Rate | Aggregation | Global Accuracy | Global F1 | ASR | Privacy Leakage Proxy | Mean Update Norm | Communication Bytes | 해석 |",
        "|---|---:|---|---:|---:|---:|---:|---:|---:|---|",
    ]
    for result in results:
        lines.append(
            "| {condition} | {rate:.0%} | {aggregation} | {acc:.6f} | {f1:.6f} | {asr:.6f} | {leak:.6f} | {norm:.6f} | {bytes} | {notes} |".format(
                condition=result["condition"],
                rate=result["malicious_client_rate"],
                aggregation=result["aggregation"],
                acc=result["global_accuracy"],
                f1=result["global_f1"],
                asr=result["attack_success_rate"],
                leak=result["privacy_leakage_proxy"],
                norm=result["mean_update_norm"],
                bytes=result["communication_bytes"],
                notes=result["notes"],
            )
        )
    lines.extend(
        [
            "",
            "## 해석 메모",
            "",
            "- Clean FL은 악성 클라이언트가 없는 FedAvg 기준 조건이다.",
            "- Poisoned FL 조건은 synthetic label/backdoor update만 사용하며 실제 공격 payload나 실제 FL 서비스 접속을 포함하지 않는다.",
            "- ASR은 원래 class 0인 synthetic test sample에 toy trigger를 더했을 때 target class 1로 예측되는 비율이다.",
            "- Privacy Leakage Proxy는 라운드별 update norm과 클라이언트 간 update 다양성으로 계산한 노출 위험 대용 지표이며 실제 gradient inversion 성공률이 아니다.",
            "- Robust aggregation 조건은 동일한 20% 악성 클라이언트 조건에서 coordinate median 집계를 적용한 비교 기준이다.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def run(config_path: Path, output_dir: Path) -> None:
    config = load_config(config_path)
    output_dir.mkdir(parents=True, exist_ok=True)

    base_rng = random.Random(int(config["seed"]))
    clients = generate_clients(config, base_rng)
    test_data = generate_test_data(config, base_rng)
    results: list[dict[str, Any]] = []
    all_round_logs: dict[str, list[dict[str, Any]]] = {}

    for offset, condition in enumerate(CONDITIONS):
        rng = random.Random(int(config["seed"]) + offset + 100)
        weights, round_logs = train_federated(config, condition, clients, rng)
        all_round_logs[condition["key"]] = round_logs
        results.append(evaluate(config, condition, weights, test_data, round_logs))

    write_metrics_csv(results, output_dir / "metrics_summary.csv")
    write_run_log(config, results, output_dir / "run_log.md")

    serializable = {
        "config": config,
        "results": results,
        "round_logs": all_round_logs,
        "safety_note": "All data are synthetic. No personal data, live service, or unauthorized system access is used.",
    }
    (output_dir / "results.json").write_text(
        json.dumps(serializable, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Run W10 synthetic FL security toy experiment.")
    parser.add_argument("--config", default=str(BASE_DIR / "configs" / "config.yaml"))
    parser.add_argument("--output-dir", default=str(BASE_DIR / "outputs"))
    args = parser.parse_args()
    run(Path(args.config), Path(args.output_dir))


if __name__ == "__main__":
    main()
