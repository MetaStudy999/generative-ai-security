#!/usr/bin/env python3
"""Run a local static audit over synthetic toy documents."""

from __future__ import annotations

import csv
import json
from datetime import datetime
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = BASE_DIR / "data" / "synthetic_documents.csv"
OUTPUT_DIR = BASE_DIR / "outputs"
RESULTS_FILE = OUTPUT_DIR / "results.json"
METRICS_FILE = OUTPUT_DIR / "metrics_summary.csv"
RUN_LOG_FILE = OUTPUT_DIR / "run_log.md"


def ratio(numerator: int, denominator: int) -> float:
    if denominator == 0:
        return 0.0
    return round(numerator / denominator, 4)


def load_documents() -> list[dict[str, str]]:
    with DATA_FILE.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def write_json(results: dict[str, object]) -> None:
    with RESULTS_FILE.open("w", encoding="utf-8") as handle:
        json.dump(results, handle, ensure_ascii=False, indent=2)
        handle.write("\n")


def write_metrics(metrics: dict[str, float], definitions: dict[str, str]) -> None:
    with METRICS_FILE.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["metric", "value", "definition"])
        writer.writeheader()
        for metric, value in metrics.items():
            writer.writerow(
                {
                    "metric": metric,
                    "value": value,
                    "definition": definitions[metric],
                }
            )


def write_run_log(results: dict[str, object]) -> None:
    metrics = results["metrics"]
    counts = results["counts"]
    generated_at = results["generated_at"]
    content = f"""# Run Log

## 1. 실행 개요

| 항목 | 내용 |
|---|---|
| 실행 일시 | {generated_at} |
| 입력 파일 | `{DATA_FILE.relative_to(BASE_DIR)}` |
| 결과 파일 | `{RESULTS_FILE.relative_to(BASE_DIR)}`, `{METRICS_FILE.relative_to(BASE_DIR)}` |
| 분석 유형 | synthetic toy document static audit |
| 실제 LLM 호출 | 수행하지 않음 |
| 외부 API 호출 | 수행하지 않음 |
| 실제 공격 자동화 | 수행하지 않음 |
| 실제 개인정보 사용 | 수행하지 않음 |

## 2. 집계 결과

| 항목 | 값 |
|---|---:|
| 전체 문서 수 | {counts["total_documents"]} |
| high risk 문서 수 | {counts["high_risk_documents"]} |
| 차단 기대 사례 수 | {counts["expected_block_cases"]} |
| 차단 성공으로 계산한 high risk 사례 수 | {counts["blocked_high_risk_cases"]} |
| privacy 유형 문서 수 | {counts["privacy_documents"]} |

## 3. 정적 감사 지표

| 지표 | 값 | 해석 |
|---|---:|---|
| ASR | {metrics["ASR"]} | high risk 문서 중 차단 기대가 아닌 사례 비율 |
| DPR | {metrics["DPR"]} | high risk 문서 중 차단 기대로 분류된 비율 |
| Leakage | {metrics["Leakage"]} | synthetic privacy 문서 중 차단 기대가 아닌 사례 비율 |
| RC | {metrics["RC"]} | risk label과 expected control이 모두 채워진 문서 비율 |

## 4. 주의

이 로그는 실제 모델, 실제 RAG 시스템, 실제 서비스, 실제 공격 절차를 평가한 결과가 아니다. `synthetic_documents.csv`에 기록된 toy case의 정적 기대 통제값을 집계한 재현성 점검용 산출물이다.
"""
    RUN_LOG_FILE.write_text(content, encoding="utf-8")


def main() -> int:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    documents = load_documents()

    total_documents = len(documents)
    high_risk = [row for row in documents if row.get("risk_label") == "high"]
    expected_block = [row for row in documents if row.get("expected_control") == "block"]
    blocked_high_risk = [
        row
        for row in high_risk
        if row.get("expected_control") == "block"
    ]
    attack_success = [
        row
        for row in high_risk
        if row.get("expected_control") != "block"
    ]
    privacy_documents = [row for row in documents if row.get("doc_type") == "privacy"]
    privacy_leakage = [
        row
        for row in privacy_documents
        if row.get("expected_control") != "block"
    ]
    review_complete = [
        row
        for row in documents
        if row.get("risk_label") and row.get("expected_control")
    ]

    metrics = {
        "ASR": ratio(len(attack_success), len(high_risk)),
        "DPR": ratio(len(blocked_high_risk), len(high_risk)),
        "Leakage": ratio(len(privacy_leakage), len(privacy_documents)),
        "RC": ratio(len(review_complete), total_documents),
    }
    definitions = {
        "ASR": "Attack Success Rate proxy: high risk 문서 중 expected_control이 block이 아닌 비율",
        "DPR": "Dangerous Prompt Rejection proxy: high risk 문서 중 expected_control이 block인 비율",
        "Leakage": "Synthetic privacy 문서 중 expected_control이 block이 아닌 비율",
        "RC": "Review Coverage: risk_label과 expected_control이 모두 채워진 비율",
    }
    counts = {
        "total_documents": total_documents,
        "high_risk_documents": len(high_risk),
        "expected_block_cases": len(expected_block),
        "blocked_high_risk_cases": len(blocked_high_risk),
        "privacy_documents": len(privacy_documents),
    }
    results = {
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "input_file": str(DATA_FILE.relative_to(BASE_DIR)),
        "analysis_type": "literature_and_synthetic_case_analysis",
        "safety_scope": {
            "real_personal_data_used": False,
            "real_service_attack_used": False,
            "unauthorized_api_call_used": False,
            "external_api_call_used": False,
            "llm_call_used": False,
        },
        "counts": counts,
        "metrics": metrics,
        "metric_definitions": definitions,
    }

    write_json(results)
    write_metrics(metrics, definitions)
    write_run_log(results)

    print(f"[PASS] Wrote {RESULTS_FILE.relative_to(BASE_DIR)}")
    print(f"[PASS] Wrote {METRICS_FILE.relative_to(BASE_DIR)}")
    print(f"[PASS] Wrote {RUN_LOG_FILE.relative_to(BASE_DIR)}")
    print("[PASS] Static synthetic audit completed without external calls.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
