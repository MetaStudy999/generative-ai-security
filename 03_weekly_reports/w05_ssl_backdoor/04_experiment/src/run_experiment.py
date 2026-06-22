import argparse
import csv
import json
import math
import random
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]
SOURCE_LABEL = 0
TARGET_LABEL = 1
LABEL_NAMES = {
    SOURCE_LABEL: "source_semantic_class",
    TARGET_LABEL: "target_semantic_class",
}


def load_config(path: Path) -> dict:
    config = {
        "seed": 42,
        "run_date": "2026-06-22",
        "data": {
            "train_per_class": 24,
            "test_per_class": 16,
            "cluster_std": 0.18,
        },
        "experiment": {
            "poison_rate": 0.20,
            "trigger_vector": [2.4, 0.3],
            "defense_threshold": 0.95,
        },
    }
    try:
        import yaml  # type: ignore

        loaded = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        return deep_update(config, loaded)
    except Exception:
        return config


def deep_update(base: dict, incoming: dict) -> dict:
    for key, value in incoming.items():
        if isinstance(value, dict) and isinstance(base.get(key), dict):
            deep_update(base[key], value)
        else:
            base[key] = value
    return base


def make_point(rng: random.Random, center: tuple[float, float], std: float) -> list[float]:
    return [rng.gauss(center[0], std), rng.gauss(center[1], std)]


def build_split(split: str, n_per_class: int, std: float, rng: random.Random) -> list[dict]:
    centers = {
        SOURCE_LABEL: (-1.0, 0.0),
        TARGET_LABEL: (1.0, 0.0),
    }
    rows = []
    for label, center in centers.items():
        for index in range(n_per_class):
            rows.append(
                {
                    "id": f"{split}_{LABEL_NAMES[label]}_{index:02d}",
                    "split": split,
                    "label": label,
                    "embedding": make_point(rng, center, std),
                    "poisoned": False,
                }
            )
    return rows


def apply_trigger(embedding: list[float], trigger_vector: list[float]) -> list[float]:
    return [embedding[0] + trigger_vector[0], embedding[1] + trigger_vector[1]]


def build_poisoned_training(train_rows: list[dict], poison_rate: float, trigger_vector: list[float]) -> list[dict]:
    poisoned_rows = [dict(row) for row in train_rows]
    source_rows = [row for row in train_rows if row["label"] == SOURCE_LABEL]
    poison_count = max(1, round(len(source_rows) * poison_rate))
    for row in source_rows[:poison_count]:
        poisoned_rows.append(
            {
                "id": f"{row['id']}_trigger",
                "split": "train",
                "label": TARGET_LABEL,
                "source_label": SOURCE_LABEL,
                "embedding": apply_trigger(row["embedding"], trigger_vector),
                "poisoned": True,
            }
        )
    return poisoned_rows


def centroid_classifier(rows: list[dict]) -> dict[int, list[float]]:
    sums: dict[int, list[float]] = {}
    counts: dict[int, int] = {}
    for row in rows:
        label = int(row["label"])
        sums.setdefault(label, [0.0, 0.0])
        counts[label] = counts.get(label, 0) + 1
        sums[label][0] += row["embedding"][0]
        sums[label][1] += row["embedding"][1]
    return {label: [value[0] / counts[label], value[1] / counts[label]] for label, value in sums.items()}


def distance(left: list[float], right: list[float]) -> float:
    return math.sqrt((left[0] - right[0]) ** 2 + (left[1] - right[1]) ** 2)


def predict(embedding: list[float], centroids: dict[int, list[float]]) -> int:
    return min(centroids, key=lambda label: distance(embedding, centroids[label]))


def accuracy(rows: list[dict], centroids: dict[int, list[float]]) -> float:
    correct = sum(1 for row in rows if predict(row["embedding"], centroids) == row["label"])
    return correct / len(rows)


def mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def fmt(value: float | int | str | None) -> str:
    if value is None:
        return ""
    if isinstance(value, float):
        return f"{value:.6f}"
    return str(value)


def evaluate(config: dict) -> tuple[list[dict], dict]:
    seed = int(config.get("seed", 42))
    rng = random.Random(seed)
    data_config = config["data"]
    exp_config = config["experiment"]
    train_rows = build_split(
        "train",
        int(data_config.get("train_per_class", 24)),
        float(data_config.get("cluster_std", 0.18)),
        rng,
    )
    test_rows = build_split(
        "test",
        int(data_config.get("test_per_class", 16)),
        float(data_config.get("cluster_std", 0.18)),
        rng,
    )
    trigger_vector = [float(value) for value in exp_config.get("trigger_vector", [2.4, 0.3])]
    poison_rate = float(exp_config.get("poison_rate", 0.20))
    defense_threshold = float(exp_config.get("defense_threshold", 0.95))

    clean_centroids = centroid_classifier(train_rows)
    poisoned_train = build_poisoned_training(train_rows, poison_rate, trigger_vector)
    poisoned_centroids = centroid_classifier(poisoned_train)

    source_test_rows = [row for row in test_rows if row["label"] == SOURCE_LABEL]
    triggered_predictions = [
        predict(apply_trigger(row["embedding"], trigger_vector), poisoned_centroids)
        for row in source_test_rows
    ]
    attack_success_rate = sum(1 for prediction in triggered_predictions if prediction == TARGET_LABEL) / len(
        triggered_predictions
    )
    representation_shifts = [
        distance(row["embedding"], apply_trigger(row["embedding"], trigger_vector)) for row in source_test_rows
    ]

    clean_view_rng = random.Random(seed + 7)
    clean_consistency_shifts = [
        distance(
            row["embedding"],
            [
                row["embedding"][0] + clean_view_rng.gauss(0.0, 0.07),
                row["embedding"][1] + clean_view_rng.gauss(0.0, 0.07),
            ],
        )
        for row in source_test_rows
    ]
    trigger_flags = [shift > defense_threshold for shift in representation_shifts]
    clean_flags = [shift > defense_threshold for shift in clean_consistency_shifts]
    trigger_detection_rate = sum(trigger_flags) / len(trigger_flags)
    clean_false_positive_rate = sum(clean_flags) / len(clean_flags)
    attack_after_defense = attack_success_rate * (1.0 - trigger_detection_rate)

    metrics = [
        {
            "condition": "Clean representation baseline",
            "clean_accuracy": accuracy(test_rows, clean_centroids),
            "poisoned_clean_accuracy": None,
            "attack_success_rate": None,
            "attack_after_defense": None,
            "representation_shift": None,
            "trigger_detection_rate": None,
            "clean_false_positive_rate": None,
            "notes": "clean synthetic embeddings classified by nearest centroid",
        },
        {
            "condition": "Poisoned/backdoor representation",
            "clean_accuracy": None,
            "poisoned_clean_accuracy": accuracy(test_rows, poisoned_centroids),
            "attack_success_rate": attack_success_rate,
            "attack_after_defense": None,
            "representation_shift": mean(representation_shifts),
            "trigger_detection_rate": None,
            "clean_false_positive_rate": None,
            "notes": "triggered source embeddings move toward the target centroid",
        },
        {
            "condition": "Consistency defense check",
            "clean_accuracy": None,
            "poisoned_clean_accuracy": None,
            "attack_success_rate": None,
            "attack_after_defense": attack_after_defense,
            "representation_shift": mean(clean_consistency_shifts),
            "trigger_detection_rate": trigger_detection_rate,
            "clean_false_positive_rate": clean_false_positive_rate,
            "notes": "paired-view distance flags large trigger-induced representation shifts",
        },
    ]

    details = {
        "config": config,
        "label_names": LABEL_NAMES,
        "clean_centroids": clean_centroids,
        "poisoned_centroids": poisoned_centroids,
        "poisoned_sample_count": sum(1 for row in poisoned_train if row.get("poisoned")),
        "source_test_count": len(source_test_rows),
        "sample_predictions": [
            {
                "id": row["id"],
                "true_label": LABEL_NAMES[row["label"]],
                "clean_prediction": LABEL_NAMES[predict(row["embedding"], poisoned_centroids)],
                "triggered_prediction": LABEL_NAMES[
                    predict(apply_trigger(row["embedding"], trigger_vector), poisoned_centroids)
                ],
                "trigger_flagged_by_defense": distance(row["embedding"], apply_trigger(row["embedding"], trigger_vector))
                > defense_threshold,
            }
            for row in source_test_rows[:8]
        ],
    }
    return metrics, details


def write_metrics_csv(path: Path, metrics: list[dict]) -> None:
    fieldnames = [
        "condition",
        "clean_accuracy",
        "poisoned_clean_accuracy",
        "attack_success_rate",
        "attack_after_defense",
        "representation_shift",
        "trigger_detection_rate",
        "clean_false_positive_rate",
        "notes",
    ]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in metrics:
            writer.writerow({key: fmt(row.get(key)) for key in fieldnames})


def write_run_log(path: Path, config: dict, metrics: list[dict], details: dict) -> None:
    metric_rows = "\n".join(
        "| {condition} | {clean_accuracy} | {poisoned_clean_accuracy} | {attack_success_rate} | {attack_after_defense} | {representation_shift} | {trigger_detection_rate} | {clean_false_positive_rate} | {notes} |".format(
            condition=row["condition"],
            clean_accuracy=fmt(row.get("clean_accuracy")),
            poisoned_clean_accuracy=fmt(row.get("poisoned_clean_accuracy")),
            attack_success_rate=fmt(row.get("attack_success_rate")),
            attack_after_defense=fmt(row.get("attack_after_defense")),
            representation_shift=fmt(row.get("representation_shift")),
            trigger_detection_rate=fmt(row.get("trigger_detection_rate")),
            clean_false_positive_rate=fmt(row.get("clean_false_positive_rate")),
            notes=row["notes"],
        )
        for row in metrics
    )
    prediction_rows = "\n".join(
        f"| {row['id']} | {row['true_label']} | {row['clean_prediction']} | {row['triggered_prediction']} | {row['trigger_flagged_by_defense']} |"
        for row in details["sample_predictions"]
    )
    path.write_text(
        f"""# W05 실험 실행 로그

| 항목 | 내용 |
|---|---|
| 실행일 | {config.get("run_date", "2026-06-22")} |
| Seed | {config.get("seed", 42)} |
| 데이터 | synthetic 2D representation clusters |
| 모델 | nearest-centroid representation classifier |
| 보안 시나리오 | source class embedding에 trigger vector를 더해 target class로 이동 |
| 방어 점검 | paired-view consistency distance threshold |
| 안전 범위 | 실제 개인정보, 실제 서비스, 무단 공격 없음 |

## 실행 명령

```bash
python3 src/run_experiment.py --config configs/config.yaml
```

## 주요 지표

| 조건 | Clean Acc. | Poisoned Clean Acc. | ASR | ASR after defense | Mean Shift | Detection Rate | Clean FPR | 해석 |
|---|---:|---:|---:|---:|---:|---:|---:|---|
{metric_rows}

## 예측 샘플

| ID | 정답 | Clean 예측 | Trigger 예측 | 방어 플래그 |
|---|---|---|---|---|
{prediction_rows}

## 산출물

- `outputs/metrics_summary.csv`
- `outputs/results.json`
- `outputs/run_log.md`

## 한계

이 결과는 synthetic 2D representation toy 실험의 평가 형식 검증용 수치이며, 실제 SSL 모델, foundation model, 상용 시스템의 poisoning/backdoor 보안 성능으로 일반화하지 않는다.
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
        json.dumps(
            {
                "metrics": metrics,
                "details": details,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    write_run_log(output_dir / "run_log.md", config, metrics, details)
    print(json.dumps({"status": "ok", "outputs": str(output_dir)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
