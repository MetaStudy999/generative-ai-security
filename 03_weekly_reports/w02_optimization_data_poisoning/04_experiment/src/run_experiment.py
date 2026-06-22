#!/usr/bin/env python3
"""Run the W02 safe data-poisoning toy experiment.

The experiment uses scikit-learn's public digits dataset and evaluates:

1. clean baseline classification
2. label-flipping poisoning at several rates
3. a simple toy backdoor trigger on a small fraction of training samples

It is intentionally limited to a local/public educational dataset. It does not
touch personal data, real services, or unauthorized systems.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    import numpy as np
    import yaml
    from sklearn.datasets import load_digits
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import accuracy_score, precision_recall_fscore_support
    from sklearn.model_selection import train_test_split
    from sklearn.pipeline import make_pipeline
    from sklearn.preprocessing import StandardScaler
except ModuleNotFoundError as exc:  # pragma: no cover - environment guard
    message = (
        f"Missing dependency: {exc.name}\n"
        "Run inside the Docker environment or install requirements first:\n"
        "  docker build -t w02-aisec .\n"
        "  docker run --rm -it -v $(pwd):/workspace w02-aisec bash\n"
        "  python src/run_experiment.py --config configs/config.yaml\n"
    )
    sys.exit(message)


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = ROOT / "configs" / "config.yaml"


def load_config(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def make_model(config: dict[str, Any]) -> Any:
    max_iter = int(config["model"]["max_iter"])
    return make_pipeline(
        StandardScaler(),
        LogisticRegression(max_iter=max_iter, solver="lbfgs", random_state=int(config["seed"])),
    )


def evaluate_model(model: Any, x_test: np.ndarray, y_test: np.ndarray) -> dict[str, float]:
    prediction = model.predict(x_test)
    precision, recall, f1, _ = precision_recall_fscore_support(
        y_test,
        prediction,
        average="macro",
        zero_division=0,
    )
    return {
        "accuracy": float(accuracy_score(y_test, prediction)),
        "precision_macro": float(precision),
        "recall_macro": float(recall),
        "f1_macro": float(f1),
    }


def label_flip(y_train: np.ndarray, rate: float, offset: int, seed: int) -> tuple[np.ndarray, int]:
    poisoned = y_train.copy()
    rng = np.random.default_rng(seed)
    n_flip = int(round(len(poisoned) * rate))
    if n_flip == 0:
        return poisoned, 0
    indices = rng.choice(len(poisoned), size=n_flip, replace=False)
    poisoned[indices] = (poisoned[indices] + offset) % 10
    return poisoned, n_flip


def add_trigger(x: np.ndarray, pixels: list[int], value: float) -> np.ndarray:
    triggered = x.copy()
    triggered[:, pixels] = value
    return triggered


def make_backdoor_train_data(
    x_train: np.ndarray,
    y_train: np.ndarray,
    poison_rate: float,
    target_label: int,
    pixels: list[int],
    trigger_value: float,
    seed: int,
) -> tuple[np.ndarray, np.ndarray, int]:
    rng = np.random.default_rng(seed)
    candidate_indices = np.where(y_train != target_label)[0]
    n_poison = int(round(len(y_train) * poison_rate))
    n_poison = min(n_poison, len(candidate_indices))
    poison_indices = rng.choice(candidate_indices, size=n_poison, replace=False)

    x_poisoned = x_train.copy()
    y_poisoned = y_train.copy()
    x_poisoned[poison_indices] = add_trigger(x_poisoned[poison_indices], pixels, trigger_value)
    y_poisoned[poison_indices] = target_label
    return x_poisoned, y_poisoned, n_poison


def run(config: dict[str, Any]) -> dict[str, Any]:
    seed = int(config["seed"])
    digits = load_digits()
    x = digits.data.astype(float)
    y = digits.target.astype(int)

    x_train, x_test, y_train, y_test = train_test_split(
        x,
        y,
        test_size=float(config["data"]["test_size"]),
        random_state=seed,
        stratify=y,
    )

    rows: list[dict[str, Any]] = []

    clean_model = make_model(config)
    clean_model.fit(x_train, y_train)
    clean_metrics = evaluate_model(clean_model, x_test, y_test)
    rows.append(
        {
            "condition": "clean_baseline",
            "poisoning_rate": 0.0,
            "n_poisoned": 0,
            "asr": None,
            **clean_metrics,
        }
    )

    offset = int(config["poisoning"]["label_flip_offset"])
    for index, rate in enumerate(config["poisoning"]["label_flip_rates"]):
        y_poisoned, n_flip = label_flip(y_train, float(rate), offset, seed + index + 1)
        model = make_model(config)
        model.fit(x_train, y_poisoned)
        metrics = evaluate_model(model, x_test, y_test)
        rows.append(
            {
                "condition": "label_flip",
                "poisoning_rate": float(rate),
                "n_poisoned": n_flip,
                "asr": None,
                **metrics,
            }
        )

    target_label = int(config["backdoor"]["target_label"])
    pixels = [int(pixel) for pixel in config["backdoor"]["trigger_pixels"]]
    trigger_value = float(config["backdoor"]["trigger_value"])
    poison_rate = float(config["backdoor"]["poison_rate"])
    x_backdoor, y_backdoor, n_backdoor = make_backdoor_train_data(
        x_train,
        y_train,
        poison_rate,
        target_label,
        pixels,
        trigger_value,
        seed + 99,
    )
    backdoor_model = make_model(config)
    backdoor_model.fit(x_backdoor, y_backdoor)
    backdoor_clean_metrics = evaluate_model(backdoor_model, x_test, y_test)

    attack_mask = y_test != target_label
    x_triggered = add_trigger(x_test[attack_mask], pixels, trigger_value)
    triggered_prediction = backdoor_model.predict(x_triggered)
    asr = float(np.mean(triggered_prediction == target_label))
    rows.append(
        {
            "condition": "toy_backdoor",
            "poisoning_rate": poison_rate,
            "n_poisoned": n_backdoor,
            "asr": asr,
            **backdoor_clean_metrics,
        }
    )

    return {
        "metadata": {
            "week": config["week"],
            "topic": config["topic"],
            "dataset": "sklearn.datasets.load_digits",
            "seed": seed,
            "run_at_utc": datetime.now(timezone.utc).isoformat(),
            "safety_scope": config["security_scope"],
        },
        "rows": rows,
    }


def write_outputs(results: dict[str, Any], output_dir: Path, config: dict[str, Any]) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    rows = results["rows"]
    csv_path = output_dir / config["outputs"]["metrics_csv"]
    json_path = output_dir / config["outputs"]["results_json"]
    log_path = output_dir / config["outputs"]["run_log"]

    fieldnames = [
        "condition",
        "poisoning_rate",
        "n_poisoned",
        "accuracy",
        "precision_macro",
        "recall_macro",
        "f1_macro",
        "asr",
    ]
    with csv_path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    with json_path.open("w", encoding="utf-8") as file:
        json.dump(results, file, ensure_ascii=False, indent=2)

    with log_path.open("w", encoding="utf-8") as file:
        file.write("# W02 Experiment Run Log\n\n")
        for key, value in results["metadata"].items():
            file.write(f"- {key}: {value}\n")
        file.write("\n## Metrics\n\n")
        file.write("| Condition | Poisoning Rate | N Poisoned | Accuracy | Macro F1 | ASR |\n")
        file.write("|---|---:|---:|---:|---:|---:|\n")
        for row in rows:
            asr = "" if row["asr"] is None else f"{row['asr']:.6f}"
            file.write(
                f"| {row['condition']} | {row['poisoning_rate']:.2f} | {row['n_poisoned']} | "
                f"{row['accuracy']:.6f} | {row['f1_macro']:.6f} | {asr} |\n"
            )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    args = parser.parse_args()

    config = load_config(args.config)
    output_dir = ROOT / config["outputs"]["directory"]
    results = run(config)
    write_outputs(results, output_dir, config)
    print(f"Wrote W02 experiment outputs to {output_dir}")


if __name__ == "__main__":
    main()
