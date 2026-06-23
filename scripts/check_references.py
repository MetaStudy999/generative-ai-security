#!/usr/bin/env python3
"""Check final-paper and weekly reference verification status.

The check is deliberately conservative. A DOI string alone is not treated as
proof; unresolved weekly-paper mismatches are reported as WARN so make check can
surface them without pretending that manual scholarly verification is complete.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FINAL_TARGET = ROOT / "04_final_paper" / "06_appendices" / "reference_verification.md"
WEEKLY_ROOT = ROOT / "03_weekly_reports"
DOI_RE = re.compile(r"\b10\.\d{4,9}/[-._;()/:A-Z0-9]+\b", re.IGNORECASE)
PAPER_ID_RE = re.compile(r"^P(\d{2})$", re.IGNORECASE)

MISMATCH_KEYWORDS = (
    "동일 여부 확인",
    "동일 여부",
    "표기와 다름",
    "다르므로",
    "차이 확인",
    "지정 원문",
)
ALTERNATE_KEYWORDS = ("RELATED", "관련 보조 문헌", "관련 논문 PDF")
LOCAL_PDF_MISSING_KEYWORDS = ("로컬 PDF 없음", "PDF 없음", "원문 PDF 미보유")
NEEDS_CHECK_KEYWORDS = ("확인 필요", "미확인", "확정하지 않음")
PARTIAL_KEYWORDS = ("부분 검증", "부분 확인", "부분 완료", "부분 동일")
CONFIRMED_KEYWORDS = ("VERIFIED", "확인 완료", "DOI 확인", "DOI/URL 확인", "검증", "확인")


@dataclass
class BucketCounts:
    total: int = 0
    confirmed: int = 0
    needs_check: int = 0
    partial: int = 0
    mismatch: int = 0
    local_pdf_missing: int = 0
    alternate: int = 0

    @property
    def unresolved(self) -> int:
        return self.needs_check + self.partial + self.mismatch + self.local_pdf_missing + self.alternate


def emit(status: str, message: str) -> None:
    print(f"[{status}] {message}")


def clean_cell(value: str) -> str:
    return re.sub(r"<[^>]+>", "", value).replace("`", "").strip()


def is_separator(cells: list[str]) -> bool:
    return bool(cells) and all(set(cell.replace(":", "").strip()) <= {"-"} for cell in cells)


def parse_markdown_table_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    rows: list[dict[str, str]] = []
    header: list[str] = []
    for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        stripped = line.strip()
        if not stripped.startswith("|"):
            header = []
            continue
        cells = [clean_cell(cell) for cell in stripped.strip("|").split("|")]
        if is_separator(cells):
            continue
        if not header:
            header = cells
            continue
        rows.append({header[idx]: cells[idx] for idx in range(min(len(header), len(cells)))})
    return rows


def row_identifier(row: dict[str, str]) -> str:
    for key in ("ID", "번호", "인용번호"):
        value = clean_cell(row.get(key, ""))
        if value:
            return value
    first_value = next(iter(row.values()), "")
    return clean_cell(first_value)


def status_text(row: dict[str, str], extra: str = "") -> str:
    return " ".join(clean_cell(value) for value in row.values()) + " " + extra


def classify_reference(row: dict[str, str], extra: str = "", local_pdf_exists: bool | None = None) -> str:
    raw = status_text(row, extra)
    upper = raw.upper()
    if any(keyword in upper or keyword in raw for keyword in ALTERNATE_KEYWORDS):
        return "alternate"
    if any(keyword in raw for keyword in LOCAL_PDF_MISSING_KEYWORDS):
        return "local_pdf_missing"
    if local_pdf_exists is False:
        return "local_pdf_missing"
    if any(keyword in raw for keyword in MISMATCH_KEYWORDS):
        return "mismatch"
    if any(keyword in raw for keyword in NEEDS_CHECK_KEYWORDS):
        return "needs_check"
    if any(keyword in raw for keyword in PARTIAL_KEYWORDS):
        return "partial"
    if any(keyword in raw for keyword in CONFIRMED_KEYWORDS):
        return "confirmed"
    return "needs_check"


def add_bucket(counts: BucketCounts, bucket: str) -> None:
    counts.total += 1
    if bucket == "confirmed":
        counts.confirmed += 1
    elif bucket == "partial":
        counts.partial += 1
    elif bucket == "mismatch":
        counts.mismatch += 1
    elif bucket == "local_pdf_missing":
        counts.local_pdf_missing += 1
    elif bucket == "alternate":
        counts.alternate += 1
    else:
        counts.needs_check += 1


def final_rows() -> list[dict[str, str]]:
    return [
        row
        for row in parse_markdown_table_rows(FINAL_TARGET)
        if row_identifier(row).isdigit()
    ]


def final_counts(rows: list[dict[str, str]], kind: str) -> BucketCounts:
    counts = BucketCounts()
    for row in rows:
        if row.get("구분") != kind:
            continue
        add_bucket(counts, classify_reference(row))
    return counts


def weekly_dirs() -> list[Path]:
    if not WEEKLY_ROOT.exists():
        return []
    return sorted(
        path
        for path in WEEKLY_ROOT.iterdir()
        if path.is_dir() and re.match(r"w\d{2}_", path.name)
    )


def rows_by_paper_id(path: Path) -> dict[str, dict[str, str]]:
    rows: dict[str, dict[str, str]] = {}
    for row in parse_markdown_table_rows(path):
        paper_id = row_identifier(row)
        if PAPER_ID_RE.match(paper_id):
            rows[paper_id.upper()] = row
    return rows


def local_pdf_exists(week_dir: Path, paper_id: str) -> bool | None:
    match = PAPER_ID_RE.match(paper_id)
    if not match:
        return None
    pdf_dir = week_dir / "01_papers" / "pdf"
    if not pdf_dir.exists():
        return False
    prefix = f"{int(match.group(1)):02d}_"
    return any(path.name.startswith(prefix) and path.suffix.lower() == ".pdf" for path in pdf_dir.iterdir())


def weekly_counts() -> tuple[BucketCounts, list[str], int, int]:
    counts = BucketCounts()
    unresolved_weeks: list[str] = []
    explicit_body_reference_difference = 0
    doi_matches = 0
    for week_dir in weekly_dirs():
        paper_rows = rows_by_paper_id(week_dir / "01_papers" / "paper_list.md")
        doi_rows = rows_by_paper_id(week_dir / "01_papers" / "doi_check.md")
        week_unresolved = False
        week_text = ""
        for rel_path in ("01_papers/paper_list.md", "01_papers/doi_check.md"):
            path = week_dir / rel_path
            if path.exists():
                week_text += "\n" + path.read_text(encoding="utf-8", errors="ignore")
        doi_matches += len(DOI_RE.findall(week_text))
        explicit_body_reference_difference += week_text.count("본문-참고문헌 차이")
        for paper_id, row in sorted(paper_rows.items()):
            extra_row = doi_rows.get(paper_id, {})
            extra = status_text(extra_row)
            bucket = classify_reference(row, extra, local_pdf_exists(week_dir, paper_id))
            add_bucket(counts, bucket)
            if bucket != "confirmed":
                week_unresolved = True
        if week_unresolved:
            unresolved_weeks.append(week_dir.name[:3].upper())
    return counts, unresolved_weeks, explicit_body_reference_difference, doi_matches


def emit_bucket(prefix: str, counts: BucketCounts) -> None:
    status = "PASS" if counts.unresolved == 0 else "WARN"
    emit(
        status,
        (
            f"{prefix} 총 {counts.total}개, 확인 완료 {counts.confirmed}개, "
            f"확인 필요 {counts.needs_check}개, 부분 검증 {counts.partial}개, "
            f"관련 논문 재분류 항목 {counts.mismatch}개, 관련 보조 문헌 항목 {counts.alternate}개, "
            f"로컬 PDF 없음 {counts.local_pdf_missing}개"
        ),
    )


def main() -> int:
    if not FINAL_TARGET.exists():
        emit("FAIL", f"참고문헌 검증 파일이 없습니다: {FINAL_TARGET.relative_to(ROOT)}")
        return 1

    final_text = FINAL_TARGET.read_text(encoding="utf-8", errors="ignore")
    rows = final_rows()
    domestic = final_counts(rows, "국내")
    international = final_counts(rows, "해외")
    weekly, unresolved_weeks, body_ref_difference, weekly_doi_matches = weekly_counts()
    final_doi_matches = DOI_RE.findall(final_text)

    emit_bucket("국내 문헌", domestic)
    emit_bucket("해외 문헌", international)
    emit("PASS" if final_doi_matches else "WARN", f"최종논문 참고문헌 DOI 문자열 {len(final_doi_matches)}건")
    emit_bucket("주차별 P01-P05 문헌(로컬 기록 기준)", weekly)
    emit("PASS" if weekly_doi_matches else "WARN", f"주차별 DOI 문자열 {weekly_doi_matches}건")
    emit(
        "WARN" if body_ref_difference else "PASS",
        f"본문-참고문헌 차이 명시 표기 {body_ref_difference}건",
    )
    if unresolved_weeks:
        emit("WARN", "수동 참고문헌 확인 필요 주차: " + ", ".join(unresolved_weeks))

    failed = False
    if domestic.confirmed < 3:
        emit("FAIL", f"국내 문헌 확인 완료가 {domestic.confirmed}편입니다. 최소 3편이 필요합니다.")
        failed = True
    if international.confirmed < 5:
        emit("FAIL", f"해외 문헌 확인 완료가 {international.confirmed}편입니다. 최소 5편이 필요합니다.")
        failed = True

    if failed:
        emit("FAIL", "최종 판정: 참고문헌 최소 요건 미충족")
        return 1
    if weekly.unresolved:
        emit("WARN", "최종 판정: 최종논문 최소 요건은 충족하지만 주차별 수동 검증 항목이 남아 있습니다.")
    else:
        emit("PASS", "최종 판정: 자동 점검 기준 참고문헌 상태 양호")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
