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
    "week": "W13",
    "topic": "model IP, model stealing, and model extraction defense",
    "seed": 42,
    "run_date": "2026-06-22",
    "status": "executed",
    "data": {
        "type": "synthetic_binary_classification",
        "personal_data": False,
        "train_samples": 1400,
        "test_samples": 500,
        "query_pool_samples": 1800,
        "features": 4,
        "noise": 0.75,
    },
    "experiment": {
        "victim_model": "toy_logistic_classifier_with_watermark_trigger_set",
        "substitute_model": "query_response_1nn_classifier",
        "epochs": 70,
        "learning_rate": 0.055,
        "regularization": 0.002,
        "query_budgets": [100, 500, 1000],
        "watermark_triggers": 20,
        "watermark_fraction": 0.05,
        "trigger_radius": 0.03,
    },
    "security_scope": {
        "allowed": "local synthetic toy evaluation only",
        "disallowed": "actual API probing, commercial model extraction, personal data use",
    },
}


Vector = list[float]
Sample = tuple[list[float], int]


def parse_scalar(raw: str) -> Any:
    value = raw.strip()
    if not value:
        return ""
    if (value.startswith('"') and value.endswith('"')) or (
        value.startswith("'") and value.endswith("'")
    ):
        return value[1:-1]
    if value.lower() == "true":
        return True
    if value.lower() == "false":
        return False
    if value.lower() == "null":
        return None
    if value.startswith("[") and value.endswith("]"):
        items = [item.strip() for item in value[1:-1].split(",") if item.strip()]
        return [parse_scalar(item) for item in items]
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


def deep_update(base: dict[str, Any], incoming: dict[str, Any]) -> dict[str, Any]:
    for key, value in incoming.items():
        if isinstance(value, dict) and isinstance(base.get(key), dict):
            deep_update(base[key], value)
        else:
            base[key] = value
    return base


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


def distance(left: list[float], right: list[float]) -> float:
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(left, right)))


def generate_dataset(count: int, feature_count: int, noise: float, rng: random.Random) -> list[Sample]:
    base_weights = [1.05, -0.90, 0.70, -0.45][:feature_count]
    samples: list[Sample] = []
    for _ in range(count):
        features = [rng.gauss(0.0, 1.0) for _ in range(feature_count)]
        latent = dot(base_weights, features) + 0.20 * math.sin(features[0]) + rng.gauss(0.0, noise)
        label = 1 if latent >= 0 else 0
        samples.append((features, label))
    return samples


def train_logistic(
    samples: list[Sample],
    feature_count: int,
    epochs: int,
    learning_rate: float,
    regularization: float,
    rng: random.Random,
) -> Vector:
    weights = [0.0] * (feature_count + 1)
    working = list(samples)
    for _ in range(epochs):
        rng.shuffle(working)
        for features, label in working:
            x = add_bias(features)
            probability = sigmoid(dot(weights, x))
            error = probability - label
            gradient = [error * value + regularization * weight for value, weight in zip(x, weights)]
            weights = [weight - learning_rate * grad for weight, grad in zip(weights, gradient)]
    return weights


def predict_logistic(weights: Vector, features: list[float]) -> int:
    return 1 if sigmoid(dot(weights, add_bias(features))) >= 0.5 else 0


def make_trigger_set(count: int, feature_count: int, rng: random.Random) -> list[Sample]:
    triggers: list[Sample] = []
    for index in range(count):
        features = [0.0] * feature_count
        primary = index % feature_count
        secondary = (index * 2 + 1) % feature_count
        features[primary] = 2.65 + 0.04 * index
        features[secondary] = -2.35 - 0.03 * index
        for cursor in range(feature_count):
            features[cursor] += rng.uniform(-0.015, 0.015)
        signature = 1 if index % 3 in (0, 2) else 0
        triggers.append((features, signature))
    return triggers


def make_victim_predictor(weights: Vector, triggers: list[Sample], radius: float):
    def victim_predict(features: list[float]) -> int:
        for trigger_features, signature in triggers:
            if distance(features, trigger_features) <= radius:
                return signature
        return predict_logistic(weights, features)

    return victim_predict


def clean_accuracy(predictor, samples: list[Sample]) -> float:
    correct = sum(1 for features, label in samples if predictor(features) == label)
    return safe_div(correct, len(samples))


class NearestNeighborSubstitute:
    def __init__(self, samples: list[Sample]):
        self.samples = samples

    def predict(self, features: list[float]) -> int:
        nearest_features, nearest_label = min(
            self.samples,
            key=lambda sample: distance(features, sample[0]),
        )
        _ = nearest_features
        return nearest_label


def query_training_set(
    budget: int,
    query_pool: list[Sample],
    triggers: list[Sample],
    victim_predict,
    watermark_fraction: float,
    rng: random.Random,
) -> tuple[list[Sample], int]:
    trigger_count = min(len(triggers), max(1, round(budget * watermark_fraction)))
    normal_count = max(0, budget - trigger_count)
    selected_normals = rng.sample(query_pool, min(normal_count, len(query_pool)))
    selected_triggers = rng.sample(triggers, trigger_count)
    queried: list[Sample] = []
    for features, _label in selected_normals + selected_triggers:
        queried.append((features, victim_predict(features)))
    rng.shuffle(queried)
    return queried, trigger_count


def agreement(left_predictor, right_predictor, samples: list[Sample]) -> float:
    same = sum(1 for features, _label in samples if left_predictor(features) == right_predictor(features))
    return safe_div(same, len(samples))


def trigger_detection(predictor, triggers: list[Sample]) -> float:
    matches = sum(1 for features, signature in triggers if predictor(features) == signature)
    return safe_div(matches, len(triggers))


def run(config: dict[str, Any]) -> dict[str, Any]:
    seed = int(config["seed"])
    rng = random.Random(seed)
    feature_count = int(config["data"]["features"])
    train_samples = int(config["data"]["train_samples"])
    test_samples = int(config["data"]["test_samples"])
    query_pool_samples = int(config["data"]["query_pool_samples"])
    noise = float(config["data"]["noise"])
    epochs = int(config["experiment"]["epochs"])
    learning_rate = float(config["experiment"]["learning_rate"])
    regularization = float(config["experiment"]["regularization"])
    budgets = [int(item) for item in config["experiment"]["query_budgets"]]
    trigger_count = int(config["experiment"]["watermark_triggers"])
    watermark_fraction = float(config["experiment"]["watermark_fraction"])
    trigger_radius = float(config["experiment"]["trigger_radius"])

    train = generate_dataset(train_samples, feature_count, noise, rng)
    test = generate_dataset(test_samples, feature_count, noise, rng)
    query_pool = generate_dataset(query_pool_samples, feature_count, noise, rng)
    victim_weights = train_logistic(
        train,
        feature_count,
        epochs,
        learning_rate,
        regularization,
        rng,
    )
    clean_control_weights = train_logistic(
        generate_dataset(train_samples, feature_count, noise, rng),
        feature_count,
        epochs,
        learning_rate,
        regularization,
        rng,
    )
    triggers = make_trigger_set(trigger_count, feature_count, rng)
    victim_predict = make_victim_predictor(victim_weights, triggers, trigger_radius)

    clean_control_predict = lambda features: predict_logistic(clean_control_weights, features)
    false_positive_rate = trigger_detection(clean_control_predict, triggers)
    victim_accuracy = clean_accuracy(victim_predict, test)

    rows: list[dict[str, Any]] = [
        {
            "condition": "Baseline victim model",
            "query_budget": 0,
            "watermark_queries_seen": 0,
            "extraction_fidelity": 1.0,
            "substitute_accuracy": victim_accuracy,
            "watermark_detection": trigger_detection(victim_predict, triggers),
            "false_positive_rate": false_positive_rate,
            "utility_accuracy": victim_accuracy,
            "interpretation": "Owner model keeps clean utility while preserving trigger-set ownership signal.",
        }
    ]

    for budget in budgets:
        queried, seen = query_training_set(
            budget,
            query_pool,
            triggers,
            victim_predict,
            watermark_fraction,
            rng,
        )
        substitute = NearestNeighborSubstitute(queried)
        substitute_predict = substitute.predict
        rows.append(
            {
                "condition": f"Substitute query {budget}",
                "query_budget": budget,
                "watermark_queries_seen": seen,
                "extraction_fidelity": agreement(substitute_predict, victim_predict, test),
                "substitute_accuracy": clean_accuracy(substitute_predict, test),
                "watermark_detection": trigger_detection(substitute_predict, triggers),
                "false_positive_rate": false_positive_rate,
                "utility_accuracy": "",
                "interpretation": "Higher query budget improves behavior mimicry and may inherit the watermark signal.",
            }
        )

    rows.append(
        {
            "condition": "Watermarked ownership check",
            "query_budget": 0,
            "watermark_queries_seen": len(triggers),
            "extraction_fidelity": 1.0,
            "substitute_accuracy": victim_accuracy,
            "watermark_detection": trigger_detection(victim_predict, triggers),
            "false_positive_rate": false_positive_rate,
            "utility_accuracy": victim_accuracy,
            "interpretation": "Trigger-set check is a toy ownership signal check, not ownership evidence.",
        }
    )

    return {
        "metadata": {
            "week": config["week"],
            "topic": config["topic"],
            "seed": seed,
            "run_date": config.get("run_date", "2026-06-22"),
            "status": "executed",
            "security_scope": config["security_scope"],
        },
        "config": config,
        "victim_weights": victim_weights,
        "trigger_count": len(triggers),
        "rows": rows,
    }


def write_outputs(result: dict[str, Any], output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    rows = result["rows"]
    fieldnames = [
        "condition",
        "query_budget",
        "watermark_queries_seen",
        "extraction_fidelity",
        "substitute_accuracy",
        "watermark_detection",
        "false_positive_rate",
        "utility_accuracy",
        "interpretation",
    ]

    with (output_dir / "metrics_summary.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({key: fmt(row[key]) for key in fieldnames})

    (output_dir / "results.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    table_header = (
        "| Condition | Query Budget | Extraction Fidelity | Substitute Accuracy | "
        "Watermark Detection | False Positive Rate | Utility Accuracy |\n"
        "|---|---:|---:|---:|---:|---:|---:|\n"
    )
    table_rows = []
    for row in rows:
        table_rows.append(
            "| {condition} | {query_budget} | {extraction_fidelity} | {substitute_accuracy} | "
            "{watermark_detection} | {false_positive_rate} | {utility_accuracy} |".format(
                **{key: fmt(value) for key, value in row.items()}
            )
        )

    run_log = "\n".join(
        [
            "# W13 Experiment Run Log",
            "",
            f"- Week: {result['metadata']['week']}",
            f"- Run date: {result['metadata']['run_date']}",
            f"- Seed: {result['metadata']['seed']}",
            "- Data: synthetic binary classification, no personal data",
            "- Scope: local toy model extraction and watermark detection evaluation only",
            "",
            "## Results",
            "",
            table_header + "\n".join(table_rows),
            "",
            "## Interpretation",
            "",
            "The substitute model is trained only from local synthetic query-response pairs.",
            "The watermark signal is a deterministic trigger-set ownership check in a toy setting.",
            "These numbers must not be interpreted as results on a real API or commercial model.",
            "",
        ]
    )
    (output_dir / "run_log.md").write_text(run_log, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default=str(BASE_DIR / "configs" / "config.yaml"))
    parser.add_argument("--output-dir", default=str(BASE_DIR / "outputs"))
    args = parser.parse_args()

    started = time.time()
    config = load_config(Path(args.config))
    result = run(config)
    result["metadata"]["elapsed_seconds"] = round(time.time() - started, 6)
    write_outputs(result, Path(args.output_dir))


if __name__ == "__main__":
    main()
