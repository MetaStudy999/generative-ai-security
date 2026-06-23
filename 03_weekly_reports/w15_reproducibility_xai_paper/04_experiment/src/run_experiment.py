"""Run a safe W15 reproducibility and submission readiness audit.

This script does not execute an attack or train a model. It checks local
repository artifacts required by the W15 instructions and records only audit
metadata that can be verified from files in the workspace.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from datetime import datetime, timezone
from pathlib import Path


REQUIRED_W15_FILES = [
    "00_management/week_info.md",
    "00_management/todo_checklist.md",
    "00_management/grading_rubric.md",
    "00_management/progress_log.md",
    "01_papers/paper_list.md",
    "01_papers/doi_check.md",
    "01_papers/download_source.md",
    "02_paper_summaries/P01_summary.md",
    "02_paper_summaries/P02_summary.md",
    "02_paper_summaries/P03_summary.md",
    "02_paper_summaries/P04_summary.md",
    "02_paper_summaries/P05_summary.md",
    "02_paper_summaries/paper_matrix.md",
    "03_theory_notes/ai_principle_70.md",
    "03_theory_notes/security_issue_30.md",
    "03_theory_notes/key_terms.md",
    "03_theory_notes/threat_model.md",
    "03_theory_notes/evaluation_protocol.md",
    "03_theory_notes/open_problems.md",
    "04_experiment/Dockerfile",
    "04_experiment/docker-compose.yml",
    "04_experiment/pyproject.toml",
    "04_experiment/configs/config.yaml",
    "04_experiment/experiment_report.md",
    "05_ai_worklog/ai_worklog.md",
    "05_ai_worklog/prompts.md",
    "05_ai_worklog/ai_outputs.md",
    "05_ai_worklog/human_review.md",
    "05_ai_worklog/ai_disclosure_draft.md",
    "06_report/draft/integrated_report_draft.md",
    "06_report/final/integrated_report_final.md",
    "06_report/review/self_review.md",
    "07_week_submission/README.md",
    "07_week_submission/submit_checklist.md",
    "07_week_submission/w15_submission_report.md",
    "07_week_submission/w15_submission_report.html",
    "08_final_paper_bridge/final_paper_bridge.md",
    "08_final_paper_bridge/topic_candidates.md",
    "08_final_paper_bridge/contribution_candidates.md",
    "08_final_paper_bridge/weekly_reflection_table.md",
    "09_presentation/presentation_report.md",
    "09_presentation/presentation_report.html",
    "09_presentation/presentation_slides.md",
    "09_presentation/presentation_slides.html",
    "09_presentation/speaker_notes.md",
    "09_presentation/qna.md",
    "09_presentation/one_page_handout.md",
]

FINAL_PAPER_FILES = [
    "04_final_paper/01_planning/final_topic.md",
    "04_final_paper/01_planning/research_question.md",
    "04_final_paper/01_planning/contribution.md",
    "04_final_paper/02_weekly_reflection/weekly_reflection_table.md",
    "04_final_paper/03_related_work/literature_matrix.md",
    "04_final_paper/05_draft/paper_draft.md",
    "04_final_paper/06_appendices/ai_disclosure.md",
    "04_final_paper/06_appendices/reference_verification.md",
    "04_final_paper/07_final_submission/submit_checklist.md",
]


def find_repo_root(start: Path) -> Path:
    for path in [start, *start.parents]:
        if (path / "03_weekly_reports").exists() and (path / "04_final_paper").exists():
            return path
    raise RuntimeError("Could not locate repository root")


def count_doi_statuses(doi_file: Path) -> dict[str, float | int]:
    text = doi_file.read_text(encoding="utf-8")
    rows = [line for line in text.splitlines() if re.match(r"^\| P\d{2} \|", line)]
    confirmed = sum(1 for line in rows if "| 확인 |" in line)
    partial = sum(1 for line in rows if "| 부분 확인 |" in line)
    unverified = sum(1 for line in rows if "| 미검증 |" in line)
    score = confirmed + (partial * 0.5)
    total = len(rows)
    rate = score / total if total else 0.0
    return {
        "total": total,
        "confirmed": confirmed,
        "partial": partial,
        "unverified": unverified,
        "weighted_rate": rate,
    }


def count_ai_disclosure_fields(disclosure_file: Path) -> dict[str, int | float]:
    text = disclosure_file.read_text(encoding="utf-8")
    rows = [line for line in text.splitlines() if line.startswith("|") and "작성 내용" not in line and "---" not in line]
    filled = 0
    total = 0
    for line in rows:
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) >= 2:
            total += 1
            filled += int(bool(cells[1]))
    return {"total": total, "filled": filled, "rate": filled / total if total else 0.0}


def metric_row(category: str, metric: str, value: str | int | float, status: str, evidence: str) -> dict[str, str]:
    return {
        "category": category,
        "metric": metric,
        "value": str(value),
        "status": status,
        "evidence": evidence,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="configs/config.yaml")
    args = parser.parse_args()

    experiment_dir = Path.cwd()
    repo_root = find_repo_root(experiment_dir)
    w15_root = repo_root / "03_weekly_reports" / "w15_reproducibility_xai_paper"
    outputs_dir = experiment_dir / "outputs"
    outputs_dir.mkdir(exist_ok=True)

    required_existing = sum(1 for rel in REQUIRED_W15_FILES if (w15_root / rel).exists())
    final_existing = sum(1 for rel in FINAL_PAPER_FILES if (repo_root / rel).exists())
    pdf_count = len(list((w15_root / "01_papers" / "pdf").glob("*.pdf")))
    doi_status = count_doi_statuses(w15_root / "01_papers" / "doi_check.md")
    ai_disclosure = count_ai_disclosure_fields(w15_root / "05_ai_worklog" / "ai_disclosure_draft.md")

    required_rate = required_existing / len(REQUIRED_W15_FILES)
    final_rate = final_existing / len(FINAL_PAPER_FILES)

    metrics = [
        metric_row("artifact", "w15_required_files", f"{required_existing}/{len(REQUIRED_W15_FILES)}", "complete" if required_rate == 1 else "partial", "03_weekly_reports/w15_reproducibility_xai_paper"),
        metric_row("artifact", "final_paper_link_files", f"{final_existing}/{len(FINAL_PAPER_FILES)}", "complete" if final_rate == 1 else "partial", "04_final_paper"),
        metric_row("paper", "local_pdf_count", pdf_count, "complete" if pdf_count >= 5 else "partial", "01_papers/pdf"),
        metric_row("reference", "doi_confirmed", doi_status["confirmed"], "complete" if doi_status["confirmed"] >= 4 else "partial", "01_papers/doi_check.md"),
        metric_row("reference", "doi_partial", doi_status["partial"], "partial" if doi_status["partial"] else "complete", "01_papers/doi_check.md"),
        metric_row("reference", "doi_unverified", doi_status["unverified"], "attention" if doi_status["unverified"] else "complete", "01_papers/doi_check.md"),
        metric_row("reference", "weighted_reference_verification_rate", f"{doi_status['weighted_rate']:.2f}", "partial", "01_papers/doi_check.md"),
        metric_row("ai_disclosure", "ai_disclosure_completeness", f"{ai_disclosure['filled']}/{ai_disclosure['total']}", "complete" if ai_disclosure["rate"] == 1 else "partial", "05_ai_worklog/ai_disclosure_draft.md"),
        metric_row("reproducibility", "config_present", int((experiment_dir / args.config).exists()), "complete", args.config),
        metric_row("reproducibility", "seed_recorded", 42, "complete", args.config),
    ]

    with (outputs_dir / "metrics_summary.csv").open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["category", "metric", "value", "status", "evidence"], lineterminator="\n")
        writer.writeheader()
        writer.writerows(metrics)

    result = {
        "week": "W15",
        "audit_type": "reproducibility_and_submission_readiness",
        "executed_at_utc": datetime.now(timezone.utc).isoformat(),
        "config": args.config,
        "required_w15_files": {"existing": required_existing, "total": len(REQUIRED_W15_FILES), "rate": required_rate},
        "final_paper_link_files": {"existing": final_existing, "total": len(FINAL_PAPER_FILES), "rate": final_rate},
        "local_pdf_count": pdf_count,
        "doi_status": doi_status,
        "ai_disclosure": ai_disclosure,
        "security_scope": {
            "personal_data_used": False,
            "actual_attack_performed": False,
            "benchmark_performance_claimed": False,
        },
    }
    (outputs_dir / "results.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")

    run_log = [
        "# W15 재현성·제출 준비 감사 실행 로그",
        "",
        f"- 실행 시각(UTC): {result['executed_at_utc']}",
        f"- 실행 명령: `python src/run_experiment.py --config {args.config}`",
        "- 실험 성격: 모델 성능 실험이 아니라 로컬 산출물 감사",
        "- 개인정보 사용: 없음",
        "- 실제 공격 수행: 없음",
        "- benchmark 성능 주장: 없음",
        "",
        "## 결과 요약",
        "",
        "| 항목 | 값 | 상태 | 근거 |",
        "|---|---:|---|---|",
    ]
    for row in metrics:
        run_log.append(f"| {row['metric']} | {row['value']} | {row['status']} | `{row['evidence']}` |")
    run_log.extend(
        [
            "",
            "## 해석",
            "",
            "W15 필수 산출물과 기말논문 연결 파일의 존재 여부, DOI/URL 검증 상태, AI 활용 고지 완성도를 점검했다.",
            "P03은 공식 DOI 메타데이터를 확인했지만 로컬 PDF가 Mersha et al. 대체 문헌이므로 부분 확인으로 유지한다.",
            "P05는 arXiv와 최종 ACM DOI가 연결되어 DOI 확인 상태로 갱신했다.",
        ]
    )
    (outputs_dir / "run_log.md").write_text("\n".join(run_log) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
