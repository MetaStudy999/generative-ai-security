import argparse
import csv
import json
import math
import random
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]
REAL_LABEL = 0
FAKE_LABEL = 1
LABEL_NAMES = {
    REAL_LABEL: "real",
    FAKE_LABEL: "synthetic_or_deepfake",
}


def load_config(path: Path) -> dict:
    config = {
        "week": "W06",
        "topic": "확률생성모형(Diffusion/GAN) & 딥페이크 검출",
        "seed": 42,
        "run_date": "2026-06-22",
        "data": {
            "n_per_label": 60,
            "domains": {
                "in_domain": {
                    "name": "lab_reference",
                    "real_mean": 0.22,
                    "fake_mean": 0.78,
                    "std": 0.08,
                },
                "cross_domain": {
                    "name": "compressed_unseen",
                    "real_mean": 0.34,
                    "fake_mean": 0.61,
                    "std": 0.16,
                },
            },
        },
        "experiment": {
            "detector_threshold": 0.50,
            "review_band": [0.40, 0.60],
        },
        "security_scope": {
            "allowed": "synthetic detector score reliability analysis",
            "disallowed": "actual deepfake generation, personal data use, unauthorized service testing",
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


def clamp(value: float, lower: float = 0.001, upper: float = 0.999) -> float:
    return max(lower, min(upper, value))


def fmt(value: float | int | str | None) -> str:
    if value is None:
        return ""
    if isinstance(value, float):
        return f"{value:.6f}"
    return str(value)


def build_domain_samples(domain_key: str, domain: dict, n_per_label: int, rng: random.Random) -> list[dict]:
    rows = []
    for label, mean_key in [(REAL_LABEL, "real_mean"), (FAKE_LABEL, "fake_mean")]:
        for index in range(n_per_label):
            score = clamp(rng.gauss(float(domain[mean_key]), float(domain["std"])))
            rows.append(
                {
                    "id": f"{domain_key}_{LABEL_NAMES[label]}_{index:03d}",
                    "domain_key": domain_key,
                    "domain": domain["name"],
                    "label": label,
                    "score": score,
                }
            )
    rng.shuffle(rows)
    return rows


def predict(score: float, threshold: float) -> int:
    return FAKE_LABEL if score >= threshold else REAL_LABEL


def confusion_counts(rows: list[dict], threshold: float) -> dict[str, int]:
    counts = {"tp": 0, "tn": 0, "fp": 0, "fn": 0}
    for row in rows:
        prediction = predict(row["score"], threshold)
        label = int(row["label"])
        if prediction == FAKE_LABEL and label == FAKE_LABEL:
            counts["tp"] += 1
        elif prediction == REAL_LABEL and label == REAL_LABEL:
            counts["tn"] += 1
        elif prediction == FAKE_LABEL and label == REAL_LABEL:
            counts["fp"] += 1
        elif prediction == REAL_LABEL and label == FAKE_LABEL:
            counts["fn"] += 1
    return counts


def safe_div(numerator: float, denominator: float) -> float:
    return numerator / denominator if denominator else 0.0


def mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def auroc(rows: list[dict]) -> float:
    real_scores = [row["score"] for row in rows if row["label"] == REAL_LABEL]
    fake_scores = [row["score"] for row in rows if row["label"] == FAKE_LABEL]
    wins = 0.0
    total = len(real_scores) * len(fake_scores)
    for fake_score in fake_scores:
        for real_score in real_scores:
            if fake_score > real_score:
                wins += 1.0
            elif fake_score == real_score:
                wins += 0.5
    return safe_div(wins, total)


def expected_calibration_error(rows: list[dict], threshold: float, bins: int = 5) -> float:
    buckets = [[] for _ in range(bins)]
    for row in rows:
        score = row["score"]
        prediction = predict(score, threshold)
        confidence = score if prediction == FAKE_LABEL else 1.0 - score
        correct = 1.0 if prediction == row["label"] else 0.0
        bucket_index = min(bins - 1, int(confidence * bins))
        buckets[bucket_index].append((confidence, correct))

    ece = 0.0
    total = len(rows)
    for bucket in buckets:
        if not bucket:
            continue
        avg_confidence = mean([item[0] for item in bucket])
        avg_accuracy = mean([item[1] for item in bucket])
        ece += (len(bucket) / total) * abs(avg_accuracy - avg_confidence)
    return ece


def summarize_condition(condition: str, rows: list[dict], threshold: float, notes: str) -> dict:
    counts = confusion_counts(rows, threshold)
    tp = counts["tp"]
    tn = counts["tn"]
    fp = counts["fp"]
    fn = counts["fn"]
    precision = safe_div(tp, tp + fp)
    recall = safe_div(tp, tp + fn)
    f1 = safe_div(2 * precision * recall, precision + recall)
    real_scores = [row["score"] for row in rows if row["label"] == REAL_LABEL]
    fake_scores = [row["score"] for row in rows if row["label"] == FAKE_LABEL]
    return {
        "condition": condition,
        "sample_count": len(rows),
        "accuracy": safe_div(tp + tn, len(rows)),
        "precision": precision,
        "recall": recall,
        "f1": f1,
        "false_positive_rate": safe_div(fp, fp + tn),
        "false_negative_rate": safe_div(fn, fn + tp),
        "auroc": auroc(rows),
        "expected_calibration_error": expected_calibration_error(rows, threshold),
        "auto_coverage": None,
        "review_rate": None,
        "score_gap": mean(fake_scores) - mean(real_scores),
        "notes": notes,
        "confusion": counts,
    }


def summarize_review_band(rows: list[dict], threshold: float, review_band: list[float]) -> dict:
    lower, upper = float(review_band[0]), float(review_band[1])
    auto_rows = [row for row in rows if row["score"] < lower or row["score"] > upper]
    review_rows = [row for row in rows if lower <= row["score"] <= upper]
    summary = summarize_condition(
        "Review-band triage on shifted domain",
        auto_rows,
        threshold,
        "scores inside the uncertainty band are routed to human review instead of auto decision",
    )
    summary["sample_count"] = len(rows)
    summary["auto_decision_count"] = len(auto_rows)
    summary["review_count"] = len(review_rows)
    summary["auto_coverage"] = safe_div(len(auto_rows), len(rows))
    summary["review_rate"] = safe_div(len(review_rows), len(rows))
    summary["review_band"] = review_band
    return summary


def evaluate(config: dict) -> tuple[list[dict], dict]:
    seed = int(config.get("seed", 42))
    rng = random.Random(seed)
    data_config = config["data"]
    exp_config = config["experiment"]
    n_per_label = int(data_config.get("n_per_label", 60))
    threshold = float(exp_config.get("detector_threshold", 0.50))
    review_band = exp_config.get("review_band", [0.40, 0.60])

    in_domain = build_domain_samples("in_domain", data_config["domains"]["in_domain"], n_per_label, rng)
    cross_domain = build_domain_samples("cross_domain", data_config["domains"]["cross_domain"], n_per_label, rng)

    metrics = [
        summarize_condition(
            "In-domain detector baseline",
            in_domain,
            threshold,
            "synthetic reference-domain detector scores have clear real/fake separation",
        ),
        summarize_condition(
            "Cross-domain reliability stress",
            cross_domain,
            threshold,
            "compressed/unseen-domain scores reduce the real/fake margin and expose FPR/FNR trade-off",
        ),
        summarize_review_band(cross_domain, threshold, review_band),
    ]

    details = {
        "config": config,
        "threshold": threshold,
        "review_band": review_band,
        "label_names": LABEL_NAMES,
        "sample_predictions": [
            {
                "id": row["id"],
                "domain": row["domain"],
                "true_label": LABEL_NAMES[row["label"]],
                "score": row["score"],
                "prediction": LABEL_NAMES[predict(row["score"], threshold)],
                "routed_to_review": bool(review_band[0] <= row["score"] <= review_band[1]),
            }
            for row in cross_domain[:10]
        ],
    }
    return metrics, details


def write_metrics_csv(path: Path, metrics: list[dict]) -> None:
    fieldnames = [
        "condition",
        "sample_count",
        "accuracy",
        "precision",
        "recall",
        "f1",
        "false_positive_rate",
        "false_negative_rate",
        "auroc",
        "expected_calibration_error",
        "auto_coverage",
        "review_rate",
        "score_gap",
        "notes",
    ]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in metrics:
            writer.writerow({key: fmt(row.get(key)) for key in fieldnames})


def write_run_log(path: Path, config: dict, metrics: list[dict], details: dict) -> None:
    metric_rows = "\n".join(
        "| {condition} | {sample_count} | {accuracy} | {f1} | {false_positive_rate} | {false_negative_rate} | {auroc} | {expected_calibration_error} | {auto_coverage} | {review_rate} | {score_gap} | {notes} |".format(
            condition=row["condition"],
            sample_count=fmt(row.get("sample_count")),
            accuracy=fmt(row.get("accuracy")),
            f1=fmt(row.get("f1")),
            false_positive_rate=fmt(row.get("false_positive_rate")),
            false_negative_rate=fmt(row.get("false_negative_rate")),
            auroc=fmt(row.get("auroc")),
            expected_calibration_error=fmt(row.get("expected_calibration_error")),
            auto_coverage=fmt(row.get("auto_coverage")),
            review_rate=fmt(row.get("review_rate")),
            score_gap=fmt(row.get("score_gap")),
            notes=row["notes"],
        )
        for row in metrics
    )
    prediction_rows = "\n".join(
        f"| {row['id']} | {row['domain']} | {row['true_label']} | {fmt(row['score'])} | {row['prediction']} | {row['routed_to_review']} |"
        for row in details["sample_predictions"]
    )
    path.write_text(
        f"""# W06 실험 실행 로그

| 항목 | 내용 |
|---|---|
| 실행일 | {config.get("run_date", "2026-06-22")} |
| Seed | {config.get("seed", 42)} |
| 데이터 | synthetic real/fake detector score distributions |
| 모델 | threshold-based toy deepfake detector |
| 기준 threshold | {details["threshold"]} |
| review band | {details["review_band"]} |
| 보안 시나리오 | in-domain 성능과 compressed/unseen domain 신뢰성 저하 비교 |
| 안전 범위 | 실제 딥페이크 생성, 실제 개인정보, 무단 서비스 질의 없음 |

## 실행 명령

```bash
python3 src/run_experiment.py --config configs/config.yaml
```

## 주요 지표

| 조건 | Samples | Accuracy | F1 | FPR | FNR | AUROC | ECE | Auto coverage | Review rate | Score gap | 해석 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
{metric_rows}

## Cross-domain 예측 샘플

| ID | Domain | 정답 | Score | 예측 | Review routing |
|---|---|---|---:|---|---|
{prediction_rows}

## 산출물

- `outputs/metrics_summary.csv`
- `outputs/results.json`
- `outputs/run_log.md`

## 한계

이 결과는 딥페이크 탐지 신뢰성 평가 지표를 설명하기 위한 synthetic toy 실험이다. 실제 딥페이크 데이터셋, 실제 탐지 모델, 사법 포렌식 증거능력, 운영 서비스의 보안 성능으로 일반화하지 않는다.
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
