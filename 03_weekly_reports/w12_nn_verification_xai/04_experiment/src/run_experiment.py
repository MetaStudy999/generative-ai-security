import argparse
import csv
import json
import math
import random
import time
from pathlib import Path
from typing import Any


BASE_DIR = Path(__file__).resolve().parents[1]


DEFAULT_CONFIG: dict[str, Any] = {
    "week": "W12",
    "topic": "신경망 검증·정형방법 & 대적방어·XAI·강건성 트레이드오프",
    "seed": 42,
    "run_date": "2026-06-22",
    "status": "executed",
    "data": {
        "type": "synthetic_binary_classification",
        "personal_data": False,
        "train_samples": 420,
        "test_samples": 320,
        "features": 4,
        "noise": 0.95,
        "fairness_group_feature": 2,
    },
    "experiment": {
        "model": "toy_logistic_classifier",
        "epochs": 90,
        "learning_rate": 0.06,
        "regularization": 0.002,
        "robust_regularization": 0.010,
        "epsilon": 0.35,
        "robust_augmentation_copies": 1,
    },
    "security_scope": {
        "allowed": "synthetic toy robustness/XAI evaluation and formal-bound proxy",
        "disallowed": "actual safety-critical system attack, production model probing, personal data use",
    },
}


Vector = list[float]
Sample = tuple[list[float], int, int]


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

    for raw_line in text.splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue
        indent = len(raw_line) - len(raw_line.lstrip(" "))
        stripped = raw_line.strip()
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
        else:
            parent[clean_key] = parse_scalar(raw)
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


def safe_div(numerator: float, denominator: float) -> float:
    return numerator / denominator if denominator else 0.0


def fmt(value: Any) -> str:
    if isinstance(value, float):
        return f"{value:.6f}"
    return str(value)


def generate_dataset(count: int, feature_count: int, noise: float, rng: random.Random) -> list[Sample]:
    true_weights = [1.15, -0.80, 0.55, -0.35][:feature_count]
    samples: list[Sample] = []
    for _ in range(count):
        features = [rng.gauss(0.0, 1.0) for _ in range(feature_count)]
        group = 1 if features[2 if feature_count > 2 else 0] >= 0 else 0
        latent = dot(true_weights, features) + 0.25 * group + rng.gauss(0.0, noise)
        label = 1 if latent >= 0 else 0
        samples.append((features, label, group))
    return samples


def predict_proba(weights: Vector, features: list[float]) -> float:
    return sigmoid(dot(weights, add_bias(features)))


def predict(weights: Vector, features: list[float]) -> int:
    return 1 if predict_proba(weights, features) >= 0.5 else 0


def adversarial_features(weights: Vector, features: list[float], label: int, epsilon: float) -> list[float]:
    direction = -1.0 if label == 1 else 1.0
    return [
        value + direction * epsilon * (1.0 if weight >= 0 else -1.0)
        for value, weight in zip(features, weights[1:])
    ]


def augment_for_robustness(samples: list[Sample], weights: Vector, epsilon: float, copies: int) -> list[Sample]:
    augmented = list(samples)
    for _ in range(copies):
        for features, label, group in samples:
            augmented.append((adversarial_features(weights, features, label, epsilon), label, group))
    return augmented


def train_model(
    train: list[Sample],
    config: dict[str, Any],
    rng: random.Random,
    regularization: float,
) -> Vector:
    feature_count = int(config["data"]["features"])
    weights = [0.0] * (feature_count + 1)
    epochs = int(config["experiment"]["epochs"])
    learning_rate = float(config["experiment"]["learning_rate"])

    working = list(train)
    for _ in range(epochs):
        rng.shuffle(working)
        for features, label, _group in working:
            x = add_bias(features)
            probability = sigmoid(dot(weights, x))
            error = probability - label
            gradient = [error * value + regularization * weight for value, weight in zip(x, weights)]
            weights = [weight - learning_rate * grad for weight, grad in zip(weights, gradient)]
    return weights


def accuracy(weights: Vector, samples: list[Sample]) -> float:
    correct = sum(1 for features, label, _group in samples if predict(weights, features) == label)
    return safe_div(correct, len(samples))


def robust_accuracy(weights: Vector, samples: list[Sample], epsilon: float) -> float:
    correct = 0
    for features, label, _group in samples:
        perturbed = adversarial_features(weights, features, label, epsilon)
        correct += int(predict(weights, perturbed) == label)
    return safe_div(correct, len(samples))


def attribution(weights: Vector, features: list[float]) -> list[float]:
    return [weight * value for weight, value in zip(weights[1:], features)]


def cosine_similarity(left: list[float], right: list[float]) -> float:
    numerator = dot(left, right)
    left_norm = math.sqrt(dot(left, left))
    right_norm = math.sqrt(dot(right, right))
    return safe_div(numerator, left_norm * right_norm)


def explanation_stability(weights: Vector, samples: list[Sample], epsilon: float) -> float:
    values: list[float] = []
    for features, label, _group in samples:
        perturbed = adversarial_features(weights, features, label, epsilon)
        clean_attr = [abs(value) for value in attribution(weights, features)]
        perturbed_attr = [abs(value) for value in attribution(weights, perturbed)]
        values.append(cosine_similarity(clean_attr, perturbed_attr))
    return safe_div(sum(values), len(values))


def certified_rate(weights: Vector, samples: list[Sample], epsilon: float) -> tuple[float, float]:
    radius_penalty = epsilon * sum(abs(value) for value in weights[1:])
    certified = 0
    margins: list[float] = []
    for features, label, _group in samples:
        logit = dot(weights, add_bias(features))
        signed_margin = logit if label == 1 else -logit
        bound = signed_margin - radius_penalty
        margins.append(bound)
        certified += int(bound > 0)
    return safe_div(certified, len(samples)), safe_div(sum(margins), len(margins))


def fairness_gap(weights: Vector, samples: list[Sample]) -> float:
    group_accuracy: dict[int, list[int]] = {0: [], 1: []}
    for features, label, group in samples:
        group_accuracy[group].append(int(predict(weights, features) == label))
    group_0 = safe_div(sum(group_accuracy[0]), len(group_accuracy[0]))
    group_1 = safe_div(sum(group_accuracy[1]), len(group_accuracy[1]))
    return abs(group_0 - group_1)


def evaluate_condition(label: str, weights: Vector, test: list[Sample], epsilon: float) -> dict[str, Any]:
    started = time.perf_counter()
    certified, mean_bound_margin = certified_rate(weights, test, epsilon)
    verification_cost_ms = (time.perf_counter() - started) * 1000
    clean = accuracy(weights, test)
    robust = robust_accuracy(weights, test, epsilon)
    return {
        "condition": label,
        "clean_accuracy": clean,
        "robust_accuracy": robust,
        "explanation_stability": explanation_stability(weights, test, epsilon),
        "certified_rate": certified,
        "mean_bound_margin": mean_bound_margin,
        "fairness_gap": fairness_gap(weights, test),
        "verification_cost_ms": verification_cost_ms,
    }


def write_outputs(config: dict[str, Any], rows: list[dict[str, Any]], output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    csv_path = output_dir / "metrics_summary.csv"
    fields = [
        "condition",
        "clean_accuracy",
        "robust_accuracy",
        "explanation_stability",
        "certified_rate",
        "mean_bound_margin",
        "fairness_gap",
        "verification_cost_ms",
    ]
    with csv_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

    results = {
        "metadata": {
            "week": config["week"],
            "topic": config["topic"],
            "run_date": config["run_date"],
            "seed": config["seed"],
            "status": "executed",
            "data": config["data"],
            "experiment": config["experiment"],
            "security_scope": config["security_scope"],
        },
        "metrics": rows,
    }
    (output_dir / "results.json").write_text(
        json.dumps(results, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    lines = [
        "# W12 실험 실행 로그",
        "",
        "| 항목 | 내용 |",
        "|---|---|",
        f"| 실행일 | {config['run_date']} |",
        f"| Seed | {config['seed']} |",
        f"| 데이터 | {config['data']['type']} |",
        f"| 개인정보 사용 | {config['data']['personal_data']} |",
        f"| 모델 | {config['experiment']['model']} |",
        f"| epsilon | {config['experiment']['epsilon']} |",
        f"| 보안 범위 | {config['security_scope']['allowed']} |",
        f"| 제외 범위 | {config['security_scope']['disallowed']} |",
        "",
        "## 결과 요약",
        "",
        "| 조건 | Clean Accuracy | Robust Accuracy | Explanation Stability | Certified Rate | Fairness Gap | Verification Cost ms |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            "| {condition} | {clean_accuracy} | {robust_accuracy} | {explanation_stability} | "
            "{certified_rate} | {fairness_gap} | {verification_cost_ms} |".format(
                **{key: fmt(value) for key, value in row.items()}
            )
        )
    lines.extend(
        [
            "",
            "## 해석 주의",
            "",
            "- 이 결과는 synthetic toy classification에서 얻은 교육용 수치다.",
            "- certified rate는 선형 로지스틱 모델의 L-infinity bound proxy이며, 대규모 DNN의 완전한 formal verification 결과가 아니다.",
            "- 실제 안전중요 시스템 공격, 운영 모델 침해, 개인정보 기반 평가는 수행하지 않았다.",
        ]
    )
    (output_dir / "run_log.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def run(config: dict[str, Any]) -> list[dict[str, Any]]:
    seed = int(config["seed"])
    train_rng = random.Random(seed)
    model_rng = random.Random(seed + 1)
    robust_rng = random.Random(seed + 2)
    feature_count = int(config["data"]["features"])
    train = generate_dataset(
        int(config["data"]["train_samples"]),
        feature_count,
        float(config["data"]["noise"]),
        train_rng,
    )
    test = generate_dataset(
        int(config["data"]["test_samples"]),
        feature_count,
        float(config["data"]["noise"]),
        random.Random(seed + 99),
    )
    epsilon = float(config["experiment"]["epsilon"])

    clean_weights = train_model(
        train,
        config,
        model_rng,
        float(config["experiment"]["regularization"]),
    )
    augmented = augment_for_robustness(
        train,
        clean_weights,
        epsilon,
        int(config["experiment"]["robust_augmentation_copies"]),
    )
    robust_weights = train_model(
        augmented,
        config,
        robust_rng,
        float(config["experiment"]["robust_regularization"]),
    )

    rows = [
        evaluate_condition("Clean model", clean_weights, test, epsilon),
        evaluate_condition("Adversarial input", clean_weights, test, epsilon),
        evaluate_condition("Robust defense", robust_weights, test, epsilon),
        evaluate_condition("XAI stability check", robust_weights, test, epsilon / 2),
    ]
    rows[1]["clean_accuracy"] = rows[0]["clean_accuracy"]
    rows[1]["explanation_stability"] = explanation_stability(clean_weights, test, epsilon * 1.5)
    rows[1]["certified_rate"] = certified_rate(clean_weights, test, epsilon * 1.5)[0]
    rows[1]["mean_bound_margin"] = certified_rate(clean_weights, test, epsilon * 1.5)[1]
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="configs/config.yaml")
    parser.add_argument("--output-dir", default="outputs")
    args = parser.parse_args()

    config_path = Path(args.config)
    if not config_path.is_absolute():
        config_path = BASE_DIR / config_path
    output_dir = Path(args.output_dir)
    if not output_dir.is_absolute():
        output_dir = BASE_DIR / output_dir

    config = load_config(config_path)
    rows = run(config)
    write_outputs(config, rows, output_dir)

    print(f"Wrote {output_dir / 'metrics_summary.csv'}")
    print(f"Wrote {output_dir / 'results.json'}")
    print(f"Wrote {output_dir / 'run_log.md'}")


if __name__ == "__main__":
    main()
