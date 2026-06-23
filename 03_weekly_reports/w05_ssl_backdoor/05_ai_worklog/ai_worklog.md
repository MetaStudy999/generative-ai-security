# AI 활용 기록

| 일자 | 도구 | 사용 목적 | 주요 입력 | 산출물 | 본인 검토 | 검증 방법 |
|---|---|---|---|---|---|---|
| 2026-06-22 | Codex | W05 보고서 구조 보완 및 초안 작성 | `W05` 프롬프트와 로컬 파일 상태 | 논문 요약, 이론노트, 보안노트, 실험 설계, 통합보고서 초안 | 원문/DOI/수치 검증 항목은 별도 표시 | PDF 파일명, 프롬프트 논문 목록, 최종 원문 대조 |
| 2026-06-22 | Codex | synthetic toy 실험 코드 작성 및 실행 | W05 실험 폴더, config, 안전 범위 원칙 | `src/run_experiment.py`, `outputs/metrics_summary.csv`, `outputs/results.json`, `outputs/run_log.md` | 실제 시스템 공격이 아닌 synthetic 표현공간 실험인지 확인 | 실행 로그와 CSV/JSON 대조 |
| 2026-06-22 | Codex | 제출본과 발표자료 작성 | 최종 보고서, 실험 결과, DOI/URL 검증표 | `07_week_submission/`, `09_presentation/` 산출물 | toy 결과의 일반화 금지 문구 확인 | `run_log.md` 수치와 문서 수치 비교 |

## 사용 원칙

- AI 산출물은 초안이며 최종 책임은 작성자에게 있다.
- DOI, URL, 정량 결과는 확인 근거가 있을 때만 기록한다.
- 원문 세부 내용은 최종 제출 전 사람이 대조한다.

# AI 활용 기록: 수식·알고리즘 보강

| 항목 | 기록 내용 |
|---|---|
| 사용 목적 | 수식 설명 / LaTeX 변환 / 기호 정의 / 검산 보조 |
| 반영 위치 | `02_paper_summaries/P01_summary.md`-`P05_summary.md`의 `### 5.1 핵심 수식 또는 알고리즘 설명`, `02_paper_summaries/formula_audit.md`, `00_class_materials/formula_audit_index.md` |
| 검증 방식 | 로컬 `README.md`, `math_formula_toolchain.md`, `paper_summary_template.md`, 각 주차 `paper_list.md`와 `doi_check.md`를 확인했다. 대표 표준식은 공식 arXiv/DOI landing page로 문헌 존재를 일부 대조했으나, 개별 원문 절/쪽/그림/알고리즘 번호는 `확인 필요`로 유지했다. |
| 주의사항 | 검증 전 수식·정량값은 확정값으로 쓰지 않고, 표준식은 `표준 정의식 / 원문 직접 인용 아님`으로 표시했다. 실제 공격 절차나 무단 침투 단계는 작성하지 않았다. |
