#!/usr/bin/env python3
"""Check required AI disclosure fields."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "04_final_paper" / "06_appendices" / "ai_disclosure.md"
REQUIRED_ITEMS = [
    "사용한 AI 도구명",
    "사용 일자",
    "사용 목적",
    "주요 프롬프트",
    "AI 산출물 반영 위치",
    "본인 수정 내용",
    "사실관계 검증 방법",
    "참고문헌 검증 방법",
    "최종 책임 확인",
]


def emit(status: str, message: str) -> None:
    print(f"[{status}] {message}")


def main() -> int:
    if not TARGET.exists():
        emit("FAIL", f"AI 활용 고지서가 없습니다: {TARGET.relative_to(ROOT)}")
        return 1

    text = TARGET.read_text(encoding="utf-8")
    missing = []
    for item in REQUIRED_ITEMS:
        if item in text:
            emit("PASS", f"필수 항목 확인: {item}")
        else:
            emit("FAIL", f"필수 항목 누락: {item}")
            missing.append(item)

    if missing:
        emit("FAIL", f"누락 항목 수: {len(missing)}")
        return 1

    emit("PASS", "AI 활용 고지 필수 항목이 모두 존재합니다.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
