import argparse
import csv
import json
import math
import random
from pathlib import Path
from typing import Any


BASE_DIR = Path(__file__).resolve().parents[1]


DEFAULT_CONFIG: dict[str, Any] = {
    "week": "W11",
    "topic": "차등프라이버시(DP) & 멤버십 추론 공격·방어",
    "seed": 42,
    "run_date": "2026-06-22",
    "status": "executed",
    "data": {
        "type": "synthetic_binary_classification",
        "personal_data": False,
        "train_samples": 320,
        "test_samples": 320,
        "features": 3,
        "train_noise": 0.85,
        "test_noise": 0.90,
    },
    "experiment": {
        "model": "toy_logistic_regression",
        "epochs": 60,
        "learning_rate": 0.08,
        "regularization": 0.001,
        "membership_threshold": 0.94,
        "conditions": [
            {"key": "non_dp_baseline", "label": "Non-DP baseline", "noise_multiplier": 0.00, "epsilon_proxy": "not_applicable"},
            {"key": "dp_like_low", "label": "DP-like noise low", "noise_multiplier": 0.10, "epsilon_proxy": 8.0},
            {"key": "dp_like_medium", "label": "DP-like noise medium", "noise_multiplier": 0.45, "epsilon_proxy": 3.0},
            {"key": "dp_like_high", "label": "DP-like noise high", "noise_multiplier": 1.20, "epsilon_proxy": 1.0},
        ],
    },
    "security_scope": {
        "allowed": "synthetic toy evaluation and literature-based privacy-risk analysis",
        "disallowed": "actual personal data, production model probing, unauthorized API queries, real-person membership inference",
    },
}


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
    if value.lower() == "null":
        return None
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


def safe_div(numerator: float, denominator: float) -> float:
    return numerator / denominator if denominator else 0.0


def fmt(value: Any) -> str:
    if value is None:
        return "해당 없음"
    if isinstance(value, float):
        return f"{value:.6f}"
    return str(value)


def generate_dataset(count: int, feature_count: int, noise: float, rng: random.Random) -> list[Sample]:
    samples: list[Sample] = []
    for _ in range(count):
        label = 1 if rng.random() < 0.5 else 0
        center = 1.0 if label == 1 else -1.0
        features = [rng.gauss(center * (1.0 - index * 0.12), noise) for index in range(feature_count)]
        samples.append((features, label))
    return samples


def train_model(train: list[Sample], config: dict[str, Any], condition: dict[str, Any], rng: random.Random) -> Vector:
    feature_count = int(config["data"]["features"])
    weights = [0.0] * (feature_count + 1)
    epochs = int(config["experiment"]["epochs"])
    learning_rate = float(config["experiment"]["learning_rate"])
    regularization = float(config["experiment"]["regularization"])
    noise_multiplier = float(condition["noise_multiplier"])
    clipped_norm = 1.0

    for _ in range(epochs):
        rng.shuffle(train)
        for features, label in train:
            x = add_bias(features)
            probability = sigmoid(dot(weights, x))
            error = probability - label
            gradient = [error * value + regularization * weight for value, weight in zip(x, weights)]
            norm = math.sqrt(sum(value * value for value in gradient))
            if norm > clipped_norm:
                gradient = [value * clipped_norm / norm for value in gradient]
            if noise_multiplier > 0:
                gradient = [value + rng.gauss(0.0, noise_multiplier * 0.25) for value in gradient]
            weights = [weight - learning_rate * grad for weight, grad in zip(weights, gradient)]
    return weights


def accuracy(weights: Vector, samples: list[Sample]) -> float:
    correct = sum(1 for features, label in samples if predict(weights, features) == label)
    return safe_div(correct, len(samples))


def member_scores(weights: Vector, samples: list[Sample]) -> list[float]:
    scores = []
    for features, label in samples:
        probability = predict_proba(weights, features)
        scores.append(probability if label == 1 else 1.0 - probability)
    return scores


def summarize_condition(
    condition: dict[str, Any],
    weights: Vector,
    train: list[Sample],
    test: list[Sample],
    baseline_accuracy: float | None,
    threshold: float,
) -> dict[str, Any]:
    train_accuracy = accuracy(weights, train)
    test_accuracy = accuracy(weights, test)
    train_scores = member_scores(weights, train)
    test_scores = member_scores(weights, test)
    member_positive = sum(1 for value in train_scores if value >= threshold)
    nonmember_positive = sum(1 for value in test_scores if value >= threshold)
    mi_attack_accuracy = safe_div(member_positive + (len(test_scores) - nonmember_positive), len(train_scores) + len(test_scores))
    privacy_leakage_score = max(0.0, mean(train_scores) - mean(test_scores))
    utility_drop = 0.0 if baseline_accuracy is None else max(0.0, baseline_accuracy - test_accuracy)

    return {
        "condition_key": condition["key"],
        "condition": condition["label"],
        "accuracy": test_accuracy,
        "train_accuracy": train_accuracy,
        "mi_attack_accuracy": mi_attack_accuracy,
        "epsilon_proxy": condition["epsilon_proxy"],
        "utility_drop": utility_drop,
        "privacy_leakage_score": privacy_leakage_score,
        "mean_member_confidence": mean(train_scores),
        "mean_nonmember_confidence": mean(test_scores),
        "noise_multiplier": float(condition["noise_multiplier"]),
        "notes": "표준 라이브러리 기반 synthetic toy 결과이며 정식 DP 보증이 아니다.",
    }


def evaluate(config: dict[str, Any]) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    rng = random.Random(int(config["seed"]))
    train = generate_dataset(
        int(config["data"]["train_samples"]),
        int(config["data"]["features"]),
        float(config["data"]["train_noise"]),
        rng,
    )
    test = generate_dataset(
        int(config["data"]["test_samples"]),
        int(config["data"]["features"]),
        float(config["data"]["test_noise"]),
        rng,
    )
    threshold = float(config["experiment"]["membership_threshold"])

    metrics: list[dict[str, Any]] = []
    baseline_accuracy: float | None = None
    sample_predictions: list[dict[str, Any]] = []

    for condition in config["experiment"]["conditions"]:
        condition_rng = random.Random(int(config["seed"]) + len(metrics) * 101)
        weights = train_model(list(train), config, condition, condition_rng)
        row = summarize_condition(condition, weights, train, test, baseline_accuracy, threshold)
        if baseline_accuracy is None:
            baseline_accuracy = row["accuracy"]
        metrics.append(row)
        for index, (features, label) in enumerate(test[:3]):
            probability = predict_proba(weights, features)
            sample_predictions.append(
                {
                    "condition": condition["label"],
                    "sample_id": f"test_{index:03d}",
                    "label": label,
                    "probability": probability,
                    "prediction": 1 if probability >= 0.5 else 0,
                }
            )

    details = {
        "config": config,
        "membership_threshold": threshold,
        "data_statement": "synthetic binary classification data; no personal data; no external service query",
        "sample_predictions": sample_predictions,
    }
    return metrics, details


def write_metrics_csv(path: Path, metrics: list[dict[str, Any]]) -> None:
    fieldnames = [
        "condition",
        "accuracy",
        "train_accuracy",
        "mi_attack_accuracy",
        "epsilon_proxy",
        "utility_drop",
        "privacy_leakage_score",
        "mean_member_confidence",
        "mean_nonmember_confidence",
        "noise_multiplier",
        "notes",
    ]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in metrics:
            writer.writerow({key: fmt(row.get(key)) for key in fieldnames})


def write_run_log(path: Path, config: dict[str, Any], metrics: list[dict[str, Any]], details: dict[str, Any]) -> None:
    metric_rows = "\n".join(
        "| {condition} | {accuracy} | {train_accuracy} | {mi_attack_accuracy} | {epsilon_proxy} | {utility_drop} | {privacy_leakage_score} | {noise_multiplier} | {notes} |".format(
            condition=row["condition"],
            accuracy=fmt(row["accuracy"]),
            train_accuracy=fmt(row["train_accuracy"]),
            mi_attack_accuracy=fmt(row["mi_attack_accuracy"]),
            epsilon_proxy=fmt(row["epsilon_proxy"]),
            utility_drop=fmt(row["utility_drop"]),
            privacy_leakage_score=fmt(row["privacy_leakage_score"]),
            noise_multiplier=fmt(row["noise_multiplier"]),
            notes=row["notes"],
        )
        for row in metrics
    )
    sample_rows = "\n".join(
        "| {condition} | {sample_id} | {label} | {probability} | {prediction} |".format(
            condition=row["condition"],
            sample_id=row["sample_id"],
            label=row["label"],
            probability=fmt(row["probability"]),
            prediction=row["prediction"],
        )
        for row in details["sample_predictions"]
    )
    path.write_text(
        f"""# W11 실험 실행 로그

| 항목 | 내용 |
|---|---|
| 실행일 | {config.get("run_date", "2026-06-22")} |
| Seed | {config.get("seed", 42)} |
| 데이터 | synthetic binary classification, no personal data |
| 모델 | toy logistic regression with clipped gradients and DP-like gradient noise |
| Membership threshold | {details["membership_threshold"]} |
| 보안 시나리오 | non-DP baseline, DP-like noise low/medium/high |
| 안전 범위 | 실제 개인정보, 실제 개인 대상 membership inference, 운영 모델/API 질의, 무단 서비스 테스트 없음 |

## 실행 명령

```bash
python3 src/run_experiment.py --config configs/config.yaml
```

## 주요 지표

| 조건 | Accuracy | Train Accuracy | MI Attack Accuracy | Epsilon Proxy | Utility Drop | Privacy Leakage Score | Noise Multiplier | 해석 |
|---|---:|---:|---:|---:|---:|---:|---:|---|
{metric_rows}

## Synthetic 샘플 예측 기록

| 조건 | Sample ID | Label | Probability | Prediction |
|---|---|---:|---:|---:|
{sample_rows}

## 산출물

- `outputs/metrics_summary.csv`
- `outputs/results.json`
- `outputs/run_log.md`

## 한계

이 결과는 DP와 membership inference 평가표를 설명하기 위한 synthetic toy 실험이다. `epsilon_proxy`는 정식 privacy accountant로 계산한 보장이 아니며, noise 강도에 따른 해석용 proxy이다. 실제 개인정보 보호 수준, 실제 서비스 모델의 membership inference 위험, 실제 DP-SGD 보증으로 일반화하지 않는다.
""",
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="configs/config.yaml")
    args = parser.parse_args()

    config_path = BASE_DIR / args.config
    config = load_config(config_path)
    metrics, details = evaluate(config)

    output_dir = BASE_DIR / "outputs"
    output_dir.mkdir(parents=True, exist_ok=True)
    write_metrics_csv(output_dir / "metrics_summary.csv", metrics)
    (output_dir / "results.json").write_text(
        json.dumps({"metrics": metrics, "details": details}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    write_run_log(output_dir / "run_log.md", config, metrics, details)
    print(json.dumps({"status": "ok", "outputs": str(output_dir)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
