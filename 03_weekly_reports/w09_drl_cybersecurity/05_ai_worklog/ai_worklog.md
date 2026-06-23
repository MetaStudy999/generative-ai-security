# W09 AI 활용 기록

| 일자 | 도구 | 사용 목적 | 입력/근거 | 산출물 | 검증 방식 | 남은 확인 |
|---|---|---|---|---|---|---|
| 2026-06-22 | Codex | 공통 지침 확인과 W09 산출물 완성 | README, W09 프롬프트, 기존 주차 구조 | 보고서 구조 보완 | 로컬 파일 대조 | P03/P04/P05 저자명 차이 확인 |
| 2026-06-22 | Codex | 로컬 PDF 기반 서지 대조 | `01_papers/pdf/` 첫 페이지 | DOI 표, 강의계획서 저자명 차이 메모 | `pdftotext`, DOI/Crossref 대조 | P03/P04/P05 원 강의자료 확인 |
| 2026-06-22 | Codex | synthetic toy 실험 코드 작성/실행 | W09 실험 지시, 공통 결과 원칙 | `src/run_experiment.py`, `outputs/` | `python3` 실행, CSV/JSON/run log 대조 | 실제 환경 일반화 금지 |
| 2026-06-23 | Codex | 제출본과 발표자료 최종 보완 | 통합보고서, 실험 로그 | submission, presentation 패키지 | 수치 일치 여부 점검 | 사람 최종 검토 |

## 윤리 메모

- AI 산출물은 초안 작성과 구조화에 사용했다.
- 논문 DOI와 저자명은 DOI/Crossref와 로컬 PDF를 대조했으며, 강의계획서와 충돌하는 항목은 `확인 필요`로 남겼다.
- 실험 수치는 실제 실행 로그가 있는 값만 사용했다.
- 실제 공격 자동화, 무단 스캔, exploit 절차는 작성하지 않았다.

# AI 활용 기록: 수식·알고리즘 보강

| 항목 | 기록 내용 |
|---|---|
| 사용 목적 | 수식 설명 / LaTeX 변환 / 기호 정의 / 검산 보조 |
| 반영 위치 | `02_paper_summaries/P01_summary.md`-`P05_summary.md`의 `### 5.1 핵심 수식 또는 알고리즘 설명`, `02_paper_summaries/formula_audit.md`, `00_class_materials/formula_audit_index.md` |
| 검증 방식 | 로컬 `README.md`, `math_formula_toolchain.md`, `paper_summary_template.md`, 각 주차 `paper_list.md`와 `doi_check.md`를 확인했다. 대표 표준식은 공식 arXiv/DOI landing page로 문헌 존재를 일부 대조했으나, 개별 원문 절/쪽/그림/알고리즘 번호는 `확인 필요`로 유지했다. |
| 주의사항 | 검증 전 수식·정량값은 확정값으로 쓰지 않고, 표준식은 `표준 정의식 / 원문 직접 인용 아님`으로 표시했다. 실제 공격 절차나 무단 침투 단계는 작성하지 않았다. |
