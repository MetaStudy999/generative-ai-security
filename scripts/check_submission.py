#!/usr/bin/env python3
"""Check final submission package readiness."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHECKLIST = ROOT / "04_final_paper" / "07_final_submission" / "submit_checklist.md"
FINAL_DIR = ROOT / "06_submission" / "final_paper_submission"
AI_DISCLOSURE = ROOT / "04_final_paper" / "06_appendices" / "ai_disclosure.md"
REFERENCE_VERIFICATION = (
    ROOT / "04_final_paper" / "06_appendices" / "reference_verification.md"
)
JOURNAL_SOURCE = (
    ROOT / "04_final_paper" / "00_journal_format" / "journal_format_source.md"
)


def emit(status: str, message: str) -> None:
    print(f"[{status}] {message}")


def check_file(path: Path, label: str) -> bool:
    if path.exists():
        emit("PASS", f"{label} 존재: {path.relative_to(ROOT)}")
        return True
    emit("FAIL", f"{label} 없음: {path.relative_to(ROOT)}")
    return False


def main() -> int:
    failed = False

    if FINAL_DIR.exists():
        emit("PASS", f"최종 제출 폴더 존재: {FINAL_DIR.relative_to(ROOT)}")
    else:
        emit("FAIL", f"최종 제출 폴더 없음: {FINAL_DIR.relative_to(ROOT)}")
        failed = True

    docx_files = sorted(FINAL_DIR.glob("*.docx")) if FINAL_DIR.exists() else []
    pdf_files = sorted(FINAL_DIR.glob("*.pdf")) if FINAL_DIR.exists() else []

    if docx_files:
        emit("PASS", f"DOCX 제출본 {len(docx_files)}개 발견")
    else:
        emit("WARN", "DOCX 제출본이 아직 없습니다.")

    if pdf_files:
        emit("PASS", f"PDF 제출본 {len(pdf_files)}개 발견")
    else:
        emit("WARN", "PDF 제출본이 아직 없습니다.")

    for path, label in [
        (CHECKLIST, "제출 체크리스트"),
        (AI_DISCLOSURE, "AI 활용 고지서"),
        (REFERENCE_VERIFICATION, "참고문헌 검증표"),
        (JOURNAL_SOURCE, "학회지 양식 출처표"),
    ]:
        if not check_file(path, label):
            failed = True

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
