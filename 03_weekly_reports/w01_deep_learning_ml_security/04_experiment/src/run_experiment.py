#!/usr/bin/env python3
"""Run the W01 safe toy ML-security experiment.

The script is intentionally self-contained and uses only Python's standard
library. It creates synthetic binary-classification data, trains a small
logistic-regression model, and evaluates:

1. clean baseline performance
2. label-noise training impact
3. toy feature perturbation impact
4. privacy-safe overfitting/confidence signals

It does not use personal data, query real services, or implement an attack
against a real system.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import random
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = ROOT / "configs" / "config.yaml"
DEFAULT_OUTPUT_DIR = ROOT / "outputs"


DEFAULTS: dict[str, Any] = {
    "week": "W01",
    "topic": "딥러닝 패러다임 & ML 보안 분류학",
    "seed": 42,
    "data": {
        "synthetic": {
            "n_samples": 1200,
            "n_features": 20,
            "n_informative": 8,
            "class_sep": 1.2,
            "test_size": 0.3,
        }
    },
    "experiment": {
        "model": {"max_iter": 1000, "learning_rate": 0.15, "l2": 0.001},
        "label_noise": {"flip_fraction": 0.15},
        "toy_perturbation": {"gaussian_noise_std": 0.35},
        "privacy_audit": {
            "train_test_gap_medium": 0.05,
            "train_test_gap_high": 0.1,
        },
    },
}


@dataclass(frozen=True)
class DatasetBundle:
    x_train: list[list[float]]
    x_test: list[list[float]]
    y_train: list[int]
    y_test: list[int]


@dataclass
class Standardizer:
    means: list[float]
    stds: list[float]

    @classmethod
    def fit(cls, x: list[list[float]]) -> "Standardizer":
        n_features = len(x[0])
        means = []
        stds = []
        for j in range(n_features):
            column = [row[j] for row in x]
            mean = sum(column) / len(column)
            variance = sum((value - mean) ** 2 for value in column) / len(column)
            std = math.sqrt(variance) or 1.0
            means.append(mean)
            stds.append(std)
        return cls(means=means, stds=stds)

    def transform(self, x: list[list[float]]) -> list[list[float]]:
        return [
            [(value - self.means[j]) / self.stds[j] for j, value in enumerate(row)]
            for row in x
        ]


class LogisticRegressionGD:
    def __init__(self, max_iter: int, learning_rate: float, l2: float) -> None:
        self.max_iter = max_iter
        self.learning_rate = learning_rate
        self.l2 = l2
        self.weights: list[float] = []
        self.bias = 0.0
        self.scaler: Standardizer | None = None

    def fit(self, x_raw: list[list[float]], y: list[int]) -> None:
        self.scaler = Standardizer.fit(x_raw)
        x = self.scaler.transform(x_raw)
        n_samples = len(x)
        n_features = len(x[0])
        self.weights = [0.0] * n_features
        self.bias = 0.0

        for _ in range(self.max_iter):
            grad_w = [0.0] * n_features
            grad_b = 0.0
            for row, target in zip(x, y):
                probability = sigmoid(dot(self.weights, row) + self.bias)
                error = probability - target
                for j, value in enumerate(row):
                    grad_w[j] += error * value
                grad_b += error

            for j in range(n_features):
                grad = (grad_w[j] / n_samples) + self.l2 * self.weights[j]
                self.weights[j] -= self.learning_rate * grad
            self.bias -= self.learning_rate * (grad_b / n_samples)

    def predict_proba(self, x_raw: list[list[float]]) -> list[float]:
        if self.scaler is None:
            raise RuntimeError("Model must be fitted before prediction.")
        x = self.scaler.transform(x_raw)
        return [sigmoid(dot(self.weights, row) + self.bias) for row in x]

    def predict(self, x_raw: list[list[float]]) -> list[int]:
        return [1 if probability >= 0.5 else 0 for probability in self.predict_proba(x_raw)]


def parse_scalar(value: str) -> Any:
    value = value.strip()
    if value.startswith('"') and value.endswith('"'):
        return value[1:-1]
    if value.startswith("'") and value.endswith("'"):
        return value[1:-1]
    lowered = value.lower()
    if lowered == "true":
        return True
    if lowered == "false":
        return False
    try:
        if "." in value:
            return float(value)
        return int(value)
    except ValueError:
        return value


def load_simple_yaml(path: Path) -> dict[str, Any]:
    """Parse the limited YAML subset used by this config file."""
    root: dict[str, Any] = {}
    stack: list[tuple[int, dict[str, Any]]] = [(-1, root)]

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue
        if raw_line.lstrip().startswith("- "):
            continue
        indent = len(raw_line) - len(raw_line.lstrip(" "))
        line = raw_line.strip()
        if ":" not in line:
            continue
        key, raw_value = line.split(":", 1)
        key = key.strip()
        raw_value = raw_value.strip()

        while indent <= stack[-1][0]:
            stack.pop()
        parent = stack[-1][1]
        if raw_value == "":
            child: dict[str, Any] = {}
            parent[key] = child
            stack.append((indent, child))
        else:
            parent[key] = parse_scalar(raw_value)
    return root


def deep_merge(defaults: dict[str, Any], override: dict[str, Any]) -> dict[str, Any]:
    merged: dict[str, Any] = dict(defaults)
    for key, value in override.items():
        if isinstance(value, dict) and isinstance(merged.get(key), dict):
            merged[key] = deep_merge(merged[key], value)
        else:
            merged[key] = value
    return merged


def load_config(path: Path) -> dict[str, Any]:
    if not path.exists():
        return DEFAULTS
    parsed = load_simple_yaml(path)
    return deep_merge(DEFAULTS, parsed)


def dot(left: list[float], right: list[float]) -> float:
    return sum(a * b for a, b in zip(left, right))


def sigmoid(value: float) -> float:
    if value >= 0:
        z = math.exp(-value)
        return 1.0 / (1.0 + z)
    z = math.exp(value)
    return z / (1.0 + z)


def make_synthetic_dataset(config: dict[str, Any], seed: int) -> tuple[list[list[float]], list[int]]:
    synthetic = config["data"]["synthetic"]
    rng = random.Random(seed)
    n_samples = int(synthetic["n_samples"])
    n_features = int(synthetic["n_features"])
    n_informative = int(synthetic["n_informative"])
    class_sep = float(synthetic["class_sep"])

    weights = [rng.uniform(-1.0, 1.0) for _ in range(n_informative)]
    x: list[list[float]] = []
    scores: list[float] = []

    for _ in range(n_samples):
        row = [rng.gauss(0.0, 1.0) for _ in range(n_features)]
        signal = sum(row[j] * weights[j] for j in range(n_informative))
        score = signal + rng.gauss(0.0, 1.0 / max(class_sep, 0.1))
        x.append(row)
        scores.append(score)

    threshold = sorted(scores)[len(scores) // 2]
    y = [1 if score >= threshold else 0 for score in scores]
    return x, y


def train_test_split_stratified(
    x: list[list[float]], y: list[int], test_size: float, seed: int
) -> DatasetBundle:
    rng = random.Random(seed)
    by_class = {0: [], 1: []}
    for index, label in enumerate(y):
        by_class[label].append(index)

    train_indices: list[int] = []
    test_indices: list[int] = []
    for indices in by_class.values():
        rng.shuffle(indices)
        n_test = int(round(len(indices) * test_size))
        test_indices.extend(indices[:n_test])
        train_indices.extend(indices[n_test:])

    rng.shuffle(train_indices)
    rng.shuffle(test_indices)
    return DatasetBundle(
        x_train=[x[index] for index in train_indices],
        x_test=[x[index] for index in test_indices],
        y_train=[y[index] for index in train_indices],
        y_test=[y[index] for index in test_indices],
    )


def build_dataset(config: dict[str, Any], seed: int) -> DatasetBundle:
    x, y = make_synthetic_dataset(config, seed)
    test_size = float(config["data"]["synthetic"]["test_size"])
    return train_test_split_stratified(x, y, test_size, seed)


def make_model(config: dict[str, Any]) -> LogisticRegressionGD:
    model_cfg = config["experiment"]["model"]
    return LogisticRegressionGD(
        max_iter=int(model_cfg["max_iter"]),
        learning_rate=float(model_cfg["learning_rate"]),
        l2=float(model_cfg["l2"]),
    )


def compute_metrics(y_true: list[int], y_pred: list[int]) -> dict[str, float]:
    tp = sum(1 for actual, pred in zip(y_true, y_pred) if actual == 1 and pred == 1)
    tn = sum(1 for actual, pred in zip(y_true, y_pred) if actual == 0 and pred == 0)
    fp = sum(1 for actual, pred in zip(y_true, y_pred) if actual == 0 and pred == 1)
    fn = sum(1 for actual, pred in zip(y_true, y_pred) if actual == 1 and pred == 0)
    total = len(y_true)

    accuracy = (tp + tn) / total
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0

    return {
        "accuracy": round(accuracy, 6),
        "precision": round(precision, 6),
        "recall": round(recall, 6),
        "f1": round(f1, 6),
    }


def metric_row(name: str, y_true: list[int], y_pred: list[int], note: str) -> dict[str, Any]:
    row: dict[str, Any] = {"condition": name}
    row.update(compute_metrics(y_true, y_pred))
    row["security_note"] = note
    return row


def flip_labels(y: list[int], fraction: float, seed: int) -> tuple[list[int], int]:
    rng = random.Random(seed)
    y_noisy = list(y)
    n_flip = int(round(len(y_noisy) * fraction))
    for index in rng.sample(range(len(y_noisy)), n_flip):
        y_noisy[index] = 1 - y_noisy[index]
    return y_noisy, n_flip


def perturb_features(x: list[list[float]], std: float, seed: int) -> list[list[float]]:
    rng = random.Random(seed)
    return [[value + rng.gauss(0.0, std) for value in row] for row in x]


def accuracy(y_true: list[int], y_pred: list[int]) -> float:
    return sum(1 for actual, pred in zip(y_true, y_pred) if actual == pred) / len(y_true)


def confidence_stats(probabilities: list[float]) -> dict[str, float]:
    max_confidence = [max(probability, 1.0 - probability) for probability in probabilities]
    sorted_conf = sorted(max_confidence)
    p95_index = min(len(sorted_conf) - 1, int(round(0.95 * (len(sorted_conf) - 1))))
    return {
        "mean_max_confidence": round(sum(max_confidence) / len(max_confidence), 6),
        "p95_max_confidence": round(sorted_conf[p95_index], 6),
    }


def privacy_risk_label(train_acc: float, test_acc: float, config: dict[str, Any]) -> str:
    audit_cfg = config["experiment"]["privacy_audit"]
    gap = train_acc - test_acc
    if gap >= float(audit_cfg["train_test_gap_high"]):
        return "high_overfitting_signal"
    if gap >= float(audit_cfg["train_test_gap_medium"]):
        return "medium_overfitting_signal"
    return "low_overfitting_signal"


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    fieldnames = list(rows[0].keys())
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_run_log(path: Path, results: dict[str, Any]) -> None:
    lines = [
        "# W01 Experiment Run Log",
        "",
        f"- Run timestamp: {results['run_timestamp_utc']}",
        f"- Seed: {results['seed']}",
        "- Data: synthetic binary classification data only",
        "- Safety scope: no personal data, no real service, no unauthorized query",
        "",
        "## Metrics",
        "",
        "| Condition | Accuracy | Precision | Recall | F1 | Security note |",
        "|---|---:|---:|---:|---:|---|",
    ]
    for row in results["metrics"]:
        lines.append(
            "| {condition} | {accuracy:.6f} | {precision:.6f} | {recall:.6f} | {f1:.6f} | {security_note} |".format(
                **row
            )
        )
    audit = results["privacy_safe_audit"]
    lines.extend(
        [
            "",
            "## Privacy-Safe Audit",
            "",
            f"- Train accuracy: {audit['train_accuracy']:.6f}",
            f"- Test accuracy: {audit['test_accuracy']:.6f}",
            f"- Train-test gap: {audit['train_test_gap']:.6f}",
            f"- Risk label: {audit['risk_label']}",
            "",
            "This audit is an overfitting/confidence check on synthetic data. It is not a membership inference attack against real data.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def run(config_path: Path, output_dir: Path) -> dict[str, Any]:
    config = load_config(config_path)
    seed = int(config["seed"])
    bundle = build_dataset(config, seed)

    clean_model = make_model(config)
    clean_model.fit(bundle.x_train, bundle.y_train)
    clean_predictions = clean_model.predict(bundle.x_test)
    clean_metrics = metric_row(
        "clean_baseline",
        bundle.y_test,
        clean_predictions,
        "normal synthetic test split",
    )

    label_cfg = config["experiment"]["label_noise"]
    y_noisy, n_flipped = flip_labels(bundle.y_train, float(label_cfg["flip_fraction"]), seed + 1)
    noisy_model = make_model(config)
    noisy_model.fit(bundle.x_train, y_noisy)
    noisy_predictions = noisy_model.predict(bundle.x_test)
    noisy_metrics = metric_row(
        "label_noise_training",
        bundle.y_test,
        noisy_predictions,
        f"{n_flipped} training labels flipped in toy data",
    )

    perturb_cfg = config["experiment"]["toy_perturbation"]
    x_perturbed = perturb_features(
        bundle.x_test,
        float(perturb_cfg["gaussian_noise_std"]),
        seed + 2,
    )
    perturb_predictions = clean_model.predict(x_perturbed)
    perturb_metrics = metric_row(
        "toy_feature_perturbation",
        bundle.y_test,
        perturb_predictions,
        "gaussian feature noise on synthetic test split",
    )

    train_predictions = clean_model.predict(bundle.x_train)
    train_acc = accuracy(bundle.y_train, train_predictions)
    test_acc = float(clean_metrics["accuracy"])
    privacy_audit = {
        "train_accuracy": round(train_acc, 6),
        "test_accuracy": round(test_acc, 6),
        "train_test_gap": round(train_acc - test_acc, 6),
        "train_confidence": confidence_stats(clean_model.predict_proba(bundle.x_train)),
        "test_confidence": confidence_stats(clean_model.predict_proba(bundle.x_test)),
        "risk_label": privacy_risk_label(train_acc, test_acc, config),
        "note": "Synthetic-data overfitting/confidence audit only.",
    }

    metrics = [clean_metrics, noisy_metrics, perturb_metrics]
    results = {
        "week": config["week"],
        "topic": config["topic"],
        "seed": seed,
        "run_timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "data": {
            "type": "synthetic",
            "n_train": len(bundle.y_train),
            "n_test": len(bundle.y_test),
            "personal_data": False,
        },
        "metrics": metrics,
        "privacy_safe_audit": privacy_audit,
        "reproducibility": {
            "config_path": str(config_path),
            "source": "src/run_experiment.py",
            "outputs": ["metrics_summary.csv", "results.json", "run_log.md"],
        },
    }

    output_dir.mkdir(parents=True, exist_ok=True)
    write_csv(output_dir / "metrics_summary.csv", metrics)
    (output_dir / "results.json").write_text(
        json.dumps(results, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_run_log(output_dir / "run_log.md", results)
    return results


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    results = run(args.config, args.output_dir)
    print(json.dumps(results["metrics"], ensure_ascii=False, indent=2))
    print(f"Saved outputs to: {args.output_dir}")


if __name__ == "__main__":
    main()
