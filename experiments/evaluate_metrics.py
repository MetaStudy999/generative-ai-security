import csv
from collections import Counter

from common import (
    DATASET_PATH,
    METHODS,
    OUTPUT_DIR,
    ROOT,
    environment_summary,
    evaluate_method,
    load_dataset,
    write_predictions,
)


METRIC_COLUMNS = [
    "method",
    "documents",
    "precision",
    "recall",
    "f1_score",
    "false_positive_rate",
    "dangerous_document_prevention_rate",
    "leakage_rate",
    "human_review_rate",
]

MATRIX_COLUMNS = ["method", "tp", "fp", "tn", "fn"]


def write_metrics(metrics_rows: list[dict[str, str]], matrix_rows: list[dict[str, str]]) -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    with (OUTPUT_DIR / "metrics_summary.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=METRIC_COLUMNS)
        writer.writeheader()
        writer.writerows(metrics_rows)

    with (OUTPUT_DIR / "confusion_matrix.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=MATRIX_COLUMNS)
        writer.writeheader()
        writer.writerows(matrix_rows)


def write_failures(failures: list[dict[str, str]]) -> None:
    lines = ["# Failure Cases", ""]
    if not failures:
        lines.append("No false positives or false negatives were observed.")
    else:
        for item in failures:
            lines.extend(
                [
                    f"## {item['method']} / {item['doc_id']} / {item['failure_type']}",
                    "",
                    f"- doc_type: {item['doc_type']}",
                    f"- expected_decision: {item['expected_decision']}",
                    f"- predicted_decision: {item['predicted_decision']}",
                    f"- source_type: {item['source_type']}",
                    f"- notes: {item['notes']}",
                    "",
                ]
            )
    (OUTPUT_DIR / "failure_cases.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_run_log(metrics_rows: list[dict[str, str]]) -> None:
    rows = load_dataset()
    counts = Counter(row["doc_type"] for row in rows)
    lines = [
        "# Run Log",
        "",
        "## Environment",
        "",
        *[f"- {line}" for line in environment_summary()],
        "",
        "## Commands",
        "",
        "```bash",
        "python3 experiments/run_baseline_no_filter.py",
        "python3 experiments/run_baseline_keyword.py",
        "python3 experiments/run_baseline_regex.py",
        "python3 experiments/run_proposed_framework.py",
        "python3 experiments/evaluate_metrics.py",
        "```",
        "",
        "## Dataset",
        "",
        f"- path: {DATASET_PATH.relative_to(ROOT)}",
        f"- rows: {len(rows)}",
        *[f"- {key}: {value}" for key, value in sorted(counts.items())],
        "",
        "## Metrics Summary",
        "",
        "| method | precision | recall | f1_score | fpr | prevention | leakage | review |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for metric in metrics_rows:
        lines.append(
            "| {method} | {precision} | {recall} | {f1_score} | {false_positive_rate} | "
            "{dangerous_document_prevention_rate} | {leakage_rate} | {human_review_rate} |".format(**metric)
        )
    lines.extend(
        [
            "",
            "## Interpretation Boundary",
            "",
            "이 결과는 synthetic 문서와 규칙 기반 판정기로 생성한 재현성 검증용 수치이다. 실제 기업 RAG 시스템, 실제 LLM, 실제 개인정보, 실제 공격 성공률로 일반화하지 않는다.",
        ]
    )
    (OUTPUT_DIR / "run_log.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    load_dataset()
    metrics_rows: list[dict[str, str]] = []
    matrix_rows: list[dict[str, str]] = []
    failures: list[dict[str, str]] = []

    for method, predictor in METHODS.items():
        write_predictions(method, predictor)
        metrics, matrix, method_failures = evaluate_method(method, predictor)
        metrics_rows.append(metrics)
        matrix_rows.append(matrix)
        failures.extend(method_failures)

    write_metrics(metrics_rows, matrix_rows)
    write_failures(failures)
    write_run_log(metrics_rows)
    print(f"wrote {OUTPUT_DIR / 'metrics_summary.csv'}")


if __name__ == "__main__":
    main()
