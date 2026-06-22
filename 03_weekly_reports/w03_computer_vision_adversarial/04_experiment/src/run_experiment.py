#!/usr/bin/env python3
"""Run the W03 safe computer-vision adversarial toy experiment.

The experiment uses synthetic 8x8 bar images and a nearest-centroid classifier.
It evaluates clean accuracy, a white-box L-infinity perturbation that moves an
input toward the opposite class centroid, and a simple 2-level feature squeezing
check. It does not use personal data, real services, or operational attack
targets.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import random
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    import yaml  # type: ignore[import-not-found]
except ModuleNotFoundError:  # pragma: no cover - local fallback
    yaml = None


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = ROOT / "configs" / "config.yaml"


def parse_scalar(value: str) -> Any:
    value = value.strip()
    if not value:
        return ""
    if value[0] in {"'", '"'} and value[-1:] == value[0]:
        return value[1:-1]
    if value.lower() == "true":
        return True
    if value.lower() == "false":
        return False
    if value.lower() in {"null", "none"}:
        return None
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        return [parse_scalar(part.strip()) for part in inner.split(",")]
    try:
        return int(value)
    except ValueError:
        pass
    try:
        return float(value)
    except ValueError:
        return value


def load_simple_yaml(path: Path) -> dict[str, Any]:
    root: dict[str, Any] = {}
    stack: list[tuple[int, dict[str, Any]]] = [(-1, root)]

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.split("#", 1)[0].rstrip()
        if not line.strip():
            continue
        indent = len(line) - len(line.lstrip(" "))
        key, separator, raw_value = line.strip().partition(":")
        if not separator:
            raise ValueError(f"Unsupported config line: {raw_line}")
        while indent <= stack[-1][0]:
            stack.pop()
        parent = stack[-1][1]
        if raw_value.strip() == "":
            child: dict[str, Any] = {}
            parent[key] = child
            stack.append((indent, child))
        else:
            parent[key] = parse_scalar(raw_value)
    return root


def load_config(path: Path) -> dict[str, Any]:
    if yaml is not None:
        with path.open("r", encoding="utf-8") as file:
            return yaml.safe_load(file)
    return load_simple_yaml(path)


def clip(value: float) -> float:
    return max(0.0, min(1.0, value))


def make_base_image(label: int, size: int, stroke: float, background: float) -> list[float]:
    image = [background for _ in range(size * size)]
    center_a = size // 2 - 1
    center_b = size // 2
    if label == 0:
        for row in range(size):
            image[row * size + center_a] = stroke
            image[row * size + center_b] = stroke
    else:
        for col in range(size):
            image[center_a * size + col] = stroke
            image[center_b * size + col] = stroke
    return image


def add_noise(image: list[float], noise_std: float, rng: random.Random) -> list[float]:
    return [clip(pixel + rng.gauss(0.0, noise_std)) for pixel in image]


def make_dataset(config: dict[str, Any], split: str) -> tuple[list[list[float]], list[int]]:
    data_config = config["data"]
    size = int(data_config["image_size"])
    n_per_class = int(data_config[f"n_{split}_per_class"])
    noise_std = float(data_config["noise_std"])
    stroke = float(data_config["stroke_value"])
    background = float(data_config["background_value"])
    seed_offset = 0 if split == "train" else 10_000
    rng = random.Random(int(config["seed"]) + seed_offset)

    samples: list[tuple[list[float], int]] = []
    for label in [0, 1]:
        for _ in range(n_per_class):
            image = make_base_image(label, size, stroke, background)
            samples.append((add_noise(image, noise_std, rng), label))
    rng.shuffle(samples)
    x_values = [sample[0] for sample in samples]
    y_values = [sample[1] for sample in samples]
    return x_values, y_values


class NearestCentroidModel:
    def __init__(self, centroids: dict[int, list[float]]) -> None:
        self.centroids = centroids
        self.labels = sorted(centroids)

    def predict_one(self, x_value: list[float]) -> int:
        return min(self.labels, key=lambda label: squared_distance(x_value, self.centroids[label]))

    def predict(self, x_values: list[list[float]]) -> list[int]:
        return [self.predict_one(x_value) for x_value in x_values]


def squared_distance(left: list[float], right: list[float]) -> float:
    return sum((a - b) ** 2 for a, b in zip(left, right))


def fit_nearest_centroid(x_values: list[list[float]], y_values: list[int]) -> NearestCentroidModel:
    labels = sorted(set(y_values))
    width = len(x_values[0])
    sums = {label: [0.0 for _ in range(width)] for label in labels}
    counts = {label: 0 for label in labels}
    for x_value, label in zip(x_values, y_values):
        counts[label] += 1
        for index, pixel in enumerate(x_value):
            sums[label][index] += pixel
    centroids = {
        label: [total / counts[label] for total in sums[label]]
        for label in labels
    }
    return NearestCentroidModel(centroids)


def confusion_matrix(y_true: list[int], y_pred: list[int], labels: list[int]) -> list[list[int]]:
    index = {label: position for position, label in enumerate(labels)}
    matrix = [[0 for _ in labels] for _ in labels]
    for actual, predicted in zip(y_true, y_pred):
        matrix[index[actual]][index[predicted]] += 1
    return matrix


def evaluate(y_true: list[int], y_pred: list[int], labels: list[int]) -> dict[str, Any]:
    matrix = confusion_matrix(y_true, y_pred, labels)
    total = len(y_true)
    correct = sum(matrix[index][index] for index in range(len(labels)))
    precisions: list[float] = []
    recalls: list[float] = []
    f1_scores: list[float] = []
    for index in range(len(labels)):
        true_positive = matrix[index][index]
        false_positive = sum(matrix[row][index] for row in range(len(labels)) if row != index)
        false_negative = sum(matrix[index][col] for col in range(len(labels)) if col != index)
        precision = true_positive / (true_positive + false_positive) if true_positive + false_positive else 0.0
        recall = true_positive / (true_positive + false_negative) if true_positive + false_negative else 0.0
        f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
        precisions.append(precision)
        recalls.append(recall)
        f1_scores.append(f1)
    return {
        "accuracy": correct / total,
        "precision_macro": sum(precisions) / len(precisions),
        "recall_macro": sum(recalls) / len(recalls),
        "f1_macro": sum(f1_scores) / len(f1_scores),
        "confusion_matrix": matrix,
    }


def sign(value: float) -> float:
    if value > 0:
        return 1.0
    if value < 0:
        return -1.0
    return 0.0


def perturb_toward_opposite_centroid(
    model: NearestCentroidModel,
    x_value: list[float],
    true_label: int,
    epsilon: float,
) -> list[float]:
    target_label = next(label for label in model.labels if label != true_label)
    source = model.centroids[true_label]
    target = model.centroids[target_label]
    return [
        clip(pixel + epsilon * sign(target_pixel - source_pixel))
        for pixel, source_pixel, target_pixel in zip(x_value, source, target)
    ]


def feature_squeeze(x_value: list[float], levels: int) -> list[float]:
    if levels < 2:
        raise ValueError("feature_squeeze levels must be >= 2")
    return [round(pixel * (levels - 1)) / (levels - 1) for pixel in x_value]


def attack_success_rate(y_true: list[int], clean_pred: list[int], attacked_pred: list[int]) -> float:
    initially_correct = [index for index, (actual, predicted) in enumerate(zip(y_true, clean_pred)) if actual == predicted]
    if not initially_correct:
        return math.nan
    changed_to_wrong = sum(1 for index in initially_correct if attacked_pred[index] != y_true[index])
    return changed_to_wrong / len(initially_correct)


def make_row(
    condition: str,
    epsilon: float,
    defense: str,
    metrics: dict[str, Any],
    clean_accuracy: float,
    asr: float | None,
    n_samples: int,
) -> dict[str, Any]:
    return {
        "condition": condition,
        "epsilon": epsilon,
        "defense": defense,
        "n_samples": n_samples,
        "accuracy": metrics["accuracy"],
        "precision_macro": metrics["precision_macro"],
        "recall_macro": metrics["recall_macro"],
        "f1_macro": metrics["f1_macro"],
        "attack_success_rate": asr,
        "robust_drop": clean_accuracy - metrics["accuracy"],
        "confusion_matrix": metrics["confusion_matrix"],
    }


def write_pgm(path: Path, image: list[float], size: int) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    values = [str(int(round(clip(pixel) * 255))) for pixel in image]
    with path.open("w", encoding="utf-8") as file:
        file.write("P2\n")
        file.write(f"{size} {size}\n")
        file.write("255\n")
        for row in range(size):
            start = row * size
            file.write(" ".join(values[start:start + size]) + "\n")


def run(config: dict[str, Any]) -> dict[str, Any]:
    x_train, y_train = make_dataset(config, "train")
    x_test, y_test = make_dataset(config, "test")
    model = fit_nearest_centroid(x_train, y_train)
    labels = model.labels

    clean_pred = model.predict(x_test)
    clean_metrics = evaluate(y_test, clean_pred, labels)
    clean_accuracy = float(clean_metrics["accuracy"])
    rows = [
        make_row(
            condition="clean_baseline",
            epsilon=0.0,
            defense="none",
            metrics=clean_metrics,
            clean_accuracy=clean_accuracy,
            asr=None,
            n_samples=len(y_test),
        )
    ]

    attack_config = config["attack"]
    for epsilon in [float(value) for value in attack_config["epsilons"]]:
        adversarial = [
            perturb_toward_opposite_centroid(model, x_value, true_label, epsilon)
            for x_value, true_label in zip(x_test, y_test)
        ]
        attacked_pred = model.predict(adversarial)
        metrics = evaluate(y_test, attacked_pred, labels)
        rows.append(
            make_row(
                condition=attack_config["type"],
                epsilon=epsilon,
                defense="none",
                metrics=metrics,
                clean_accuracy=clean_accuracy,
                asr=attack_success_rate(y_test, clean_pred, attacked_pred),
                n_samples=len(y_test),
            )
        )

    defense_config = config["defense"]
    defense_epsilon = float(defense_config["epsilon"])
    adversarial = [
        perturb_toward_opposite_centroid(model, x_value, true_label, defense_epsilon)
        for x_value, true_label in zip(x_test, y_test)
    ]
    squeezed = [
        feature_squeeze(x_value, int(defense_config["levels"]))
        for x_value in adversarial
    ]
    defense_pred = model.predict(squeezed)
    defense_metrics = evaluate(y_test, defense_pred, labels)
    rows.append(
        make_row(
            condition="adversarial_with_feature_squeeze",
            epsilon=defense_epsilon,
            defense=f"{defense_config['type']}_{defense_config['levels']}_levels",
            metrics=defense_metrics,
            clean_accuracy=clean_accuracy,
            asr=attack_success_rate(y_test, clean_pred, defense_pred),
            n_samples=len(y_test),
        )
    )

    example_index = next(index for index, label in enumerate(y_test) if label == 0)
    example_clean = x_test[example_index]
    example_adversarial = perturb_toward_opposite_centroid(
        model,
        example_clean,
        y_test[example_index],
        defense_epsilon,
    )
    example_squeezed = feature_squeeze(example_adversarial, int(defense_config["levels"]))

    return {
        "metadata": {
            "week": config["week"],
            "topic": config["topic"],
            "dataset": config["data"]["type"],
            "seed": int(config["seed"]),
            "model": config["model"]["type"],
            "run_at_utc": datetime.now(timezone.utc).isoformat(),
            "safety_scope": config["security_scope"],
        },
        "rows": rows,
        "examples": {
            "label": y_test[example_index],
            "epsilon": defense_epsilon,
            "clean": example_clean,
            "adversarial": example_adversarial,
            "feature_squeezed": example_squeezed,
        },
    }


def format_optional(value: float | None) -> str:
    if value is None:
        return ""
    if isinstance(value, float) and math.isnan(value):
        return "nan"
    return f"{value:.6f}"


def write_outputs(results: dict[str, Any], output_dir: Path, config: dict[str, Any]) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    csv_path = output_dir / config["outputs"]["metrics_csv"]
    json_path = output_dir / config["outputs"]["results_json"]
    log_path = output_dir / config["outputs"]["run_log"]
    rows = results["rows"]
    fieldnames = [
        "condition",
        "epsilon",
        "defense",
        "n_samples",
        "accuracy",
        "precision_macro",
        "recall_macro",
        "f1_macro",
        "attack_success_rate",
        "robust_drop",
        "confusion_matrix",
    ]

    with csv_path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    with json_path.open("w", encoding="utf-8") as file:
        json.dump(results, file, ensure_ascii=False, indent=2)

    with log_path.open("w", encoding="utf-8") as file:
        file.write("# W03 Experiment Run Log\n\n")
        for key, value in results["metadata"].items():
            file.write(f"- {key}: {value}\n")
        file.write("\n## Metrics\n\n")
        file.write("| Condition | Epsilon | Defense | N | Accuracy | Macro F1 | ASR | Robust Drop |\n")
        file.write("|---|---:|---|---:|---:|---:|---:|---:|\n")
        for row in rows:
            file.write(
                f"| {row['condition']} | {row['epsilon']:.2f} | {row['defense']} | "
                f"{row['n_samples']} | {row['accuracy']:.6f} | {row['f1_macro']:.6f} | "
                f"{format_optional(row['attack_success_rate'])} | {row['robust_drop']:.6f} |\n"
            )
        file.write("\n## Confusion Matrices\n\n")
        file.write("Rows are true labels and columns are predicted labels.\n\n")
        for row in rows:
            file.write(f"### {row['condition']} eps={row['epsilon']:.2f} defense={row['defense']}\n\n")
            file.write(json.dumps(row["confusion_matrix"], ensure_ascii=False) + "\n\n")

    size = int(config["data"]["image_size"])
    examples = results["examples"]
    write_pgm(output_dir / config["outputs"]["clean_example"], examples["clean"], size)
    write_pgm(output_dir / config["outputs"]["adversarial_example"], examples["adversarial"], size)
    write_pgm(output_dir / config["outputs"]["defense_example"], examples["feature_squeezed"], size)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    args = parser.parse_args()

    config = load_config(args.config)
    output_dir = ROOT / config["outputs"]["directory"]
    results = run(config)
    write_outputs(results, output_dir, config)
    print(f"Wrote W03 experiment outputs to {output_dir}")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:  # pragma: no cover - command-line guard
        sys.exit(f"W03 experiment failed: {exc}")
