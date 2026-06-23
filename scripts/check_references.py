#!/usr/bin/env python3
"""Check reference verification status for the final paper."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "04_final_paper" / "06_appendices" / "reference_verification.md"
DOI_RE = re.compile(r"\b10\.\d{4,9}/[-._;()/:A-Z0-9]+\b", re.IGNORECASE)


def emit(status: str, message: str) -> None:
    print(f"[{status}] {message}")


def parse_reference_rows(text: str) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    header: list[str] = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|") or "---" in stripped:
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if not cells:
            continue
        if cells[0] in {"번호", "No", "No."}:
            header = cells
            continue
        if header and cells[0].isdigit():
            rows.append({header[idx]: cells[idx] for idx in range(min(len(header), len(cells)))})
    return rows


def is_confirmed(status: str) -> bool:
    normalized = status.replace("`", "").strip().upper()
    return normalized in {"확인", "확인 완료", "VERIFIED"}


def main() -> int:
    if not TARGET.exists():
        emit("FAIL", f"참고문헌 검증 파일이 없습니다: {TARGET.relative_to(ROOT)}")
        return 1

    text = TARGET.read_text(encoding="utf-8")
    rows = parse_reference_rows(text)
    domestic_rows = [row for row in rows if row.get("구분") == "국내"]
    international_rows = [row for row in rows if row.get("구분") == "해외"]
    domestic_confirmed = [row for row in domestic_rows if is_confirmed(row.get("상태", ""))]
    international_confirmed = [row for row in international_rows if is_confirmed(row.get("상태", ""))]
    has_needs_check = "확인 필요" in text
    has_partial_check = "부분 확인" in text
    doi_matches = DOI_RE.findall(text)

    emit("PASS", f"국내 문헌 행 개수: {len(domestic_rows)}")
    emit("PASS", f"해외 문헌 행 개수: {len(international_rows)}")

    if has_needs_check:
        emit("WARN", "`확인 필요` 항목이 남아 있습니다.")
    else:
        emit("PASS", "`확인 필요` 항목이 없습니다.")

    if has_partial_check:
        emit("WARN", "`부분 확인` 항목이 남아 있습니다.")
    else:
        emit("PASS", "`부분 확인` 항목이 없습니다.")

    if doi_matches:
        emit("PASS", f"DOI 문자열 {len(doi_matches)}건을 찾았습니다.")
    else:
        emit("WARN", "DOI 문자열을 찾지 못했습니다.")

    failed = False
    if len(domestic_confirmed) < 3:
        emit(
            "FAIL",
            f"국내 문헌 확인 완료가 {len(domestic_confirmed)}편입니다. 최소 3편이 필요합니다.",
        )
        failed = True
    else:
        emit("PASS", f"국내 문헌 확인 완료: {len(domestic_confirmed)}편")

    if len(international_confirmed) < 5:
        emit(
            "FAIL",
            f"해외 문헌 확인 완료가 {len(international_confirmed)}편입니다. 최소 5편이 필요합니다.",
        )
        failed = True
    else:
        emit("PASS", f"해외 문헌 확인 완료: {len(international_confirmed)}편")

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
