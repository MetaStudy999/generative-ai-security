# AI 활용 기록

| 일자 | 도구 | 사용 목적 | 주요 입력 | 산출물 | 본인 검토 | 검증 방법 |
|---|---|---|---|---|---|---|
| 2026-06-22 | Codex | W08 공통 지침 확인 및 산출물 완성 | W08 프롬프트, 주차 README, 로컬 W08 파일 | 작업 범위와 누락 파일 파악 | 공통 실험/발표/제출 규칙 대조 | `03_weekly_reports/README.md` 확인 |
| 2026-06-22 | Codex | 서지정보 보정 | 로컬 PDF, `pdfinfo`, `pdftotext` 출력 | 논문 목록, DOI/URL 표 보정 | DOI 임의 생성 금지 확인 | PDF 첫 페이지와 DOI/arXiv 식별자 대조 |
| 2026-06-22 | Codex | synthetic 실험 코드 작성 | W08 실습 지시, 안전 범위 | `src/run_experiment.py`, config 갱신 | 실제 공격 payload·개인정보·외부 API 제외 확인 | 코드 리뷰 및 실행 로그 확인 |
| 2026-06-22 | Codex | 보고서·제출본·발표자료 작성 | 실험 outputs, 논문 요약, 평가방법 | 통합보고서, 제출본, 발표자료 | 수치 일치성 확인 | `metrics_summary.csv`, `results.json`, `run_log.md` 대조 |

## 사용 원칙

- AI 산출물은 초안 작성, 구조화, 코드 생성, 일관성 점검에 사용했다.
- DOI, URL, 원문 수치, 실험 수치는 추측하지 않고 PDF 또는 실행 산출물 기준으로만 반영했다.
- 최종 책임은 작성자에게 있으며, P01 DOI는 미확정으로 유지한다.
- 실제 공격 payload, 실제 개인정보, live API/tool 호출은 사용하지 않았다.

# AI 활용 기록: 수식·알고리즘 보강

| 항목 | 기록 내용 |
|---|---|
| 사용 목적 | 수식 설명 / LaTeX 변환 / 기호 정의 / 검산 보조 |
| 반영 위치 | `02_paper_summaries/P01_summary.md`-`P05_summary.md`의 `### 5.1 핵심 수식 또는 알고리즘 설명`, `02_paper_summaries/formula_audit.md`, `00_class_materials/formula_audit_index.md` |
| 검증 방식 | 로컬 `README.md`, `math_formula_toolchain.md`, `paper_summary_template.md`, 각 주차 `paper_list.md`와 `doi_check.md`를 확인했다. 대표 표준식은 공식 arXiv/DOI landing page로 문헌 존재를 일부 대조했으나, 개별 원문 절/쪽/그림/알고리즘 번호는 `확인 필요`로 유지했다. |
| 주의사항 | 검증 전 수식·정량값은 확정값으로 쓰지 않고, 표준식은 `표준 정의식 / 원문 직접 인용 아님`으로 표시했다. 실제 공격 절차나 무단 침투 단계는 작성하지 않았다. |
