# AI 활용 기록

| 주차 일정 | 도구 | 사용 목적 | 주요 입력 | 산출물 | 본인 검토 | 검증 방법 |
|---|---|---|---|---|---|---|
| 2026-06-22 또는 확인 필요 | Codex | W01 보고서 구조 보완 및 내용 완성 | W01 작업 지시서, 로컬 Markdown/PDF 파일 목록 | 논문 요약, 비교표, 이론노트, 보안노트, 실험 설계, 통합보고서 | 논문별 주장 분리, DOI/URL 검증 상태 표시 | 로컬 PDF 메타데이터, DOI/arXiv 페이지, 파일 간 교차 확인 |
| 2026-06-22 또는 확인 필요 | Codex | W01 실습 소스 작성 및 실행 | `04_experiment/configs/config.yaml` | `src/run_experiment.py`, `outputs/metrics_summary.csv`, `outputs/results.json`, `outputs/run_log.md` | synthetic data와 안전 범위 확인 | 로컬 실행 결과와 출력 파일 확인 |

## 사용 원칙

- AI는 초안 구성, 문장 정리, 비교표 작성, 검증표 정리에 사용했다.
- DOI/URL은 확인 가능한 근거가 있는 경우에만 입력했다.
- 정량 실험값은 `src/run_experiment.py` 실행 로그를 근거로 기록했다.
- 최종 제출 전 원문 세부 수치와 인용 형식은 작성자가 다시 검토한다.

# AI 활용 기록: 수식·알고리즘 보강

| 항목 | 기록 내용 |
|---|---|
| 사용 목적 | 수식 설명 / LaTeX 변환 / 기호 정의 / 검산 보조 |
| 반영 위치 | `02_paper_summaries/P01_summary.md`-`P05_summary.md`의 `### 5.1 핵심 수식 또는 알고리즘 설명`, `02_paper_summaries/formula_audit.md`, `00_class_materials/formula_audit_index.md` |
| 검증 방식 | 로컬 `README.md`, `math_formula_toolchain.md`, `paper_summary_template.md`, 각 주차 `paper_list.md`와 `doi_check.md`를 확인했다. 대표 표준식은 공식 arXiv/DOI landing page로 문헌 존재를 일부 대조했으나, 개별 원문 절/쪽/그림/알고리즘 번호는 `확인 필요`로 유지했다. |
| 주의사항 | 검증 전 수식·정량값은 확정값으로 쓰지 않고, 표준식은 `표준 정의식 / 원문 직접 인용 아님`으로 표시했다. 실제 공격 절차나 무단 침투 단계는 작성하지 않았다. |

<!-- formula-visual-ai-worklog:start -->
## 2026-06-23 수식·그래프·그림 보강 작업

| 항목 | 기록 내용 |
|---|---|
| 사용 도구 | Codex, Python, matplotlib |
| 사용 목적 | 주차별 통합보고서와 발표자료에 핵심 수식, 기호 정의표, 그래프, 다이어그램, 발표자 노트 설명을 추가 |
| 입력 근거 | `w01_deep_learning_ml_security/04_experiment/outputs/metrics_summary.csv`, 기존 통합보고서, 발표 슬라이드, 이론노트 |
| 생성 산출물 | `09_presentation/assets/charts/w01_metrics_chart.png`, `09_presentation/assets/charts/w01_metrics_chart.svg`, `09_presentation/assets/diagrams/w01_pipeline_diagram.svg`, `09_presentation/assets/figure_manifest.md` |
| 검증 방식 | CSV에서 읽은 기존 수치만 차트화하고, 수식은 표준 정의식으로 한정했으며, formal guarantee가 불명확한 항목은 확인 필요로 표시 |
| 안전 범위 | 공개 데이터, synthetic/toy 데이터, 로컬 모의실험 설명으로 제한하고 실제 시스템 악용 절차는 작성하지 않음 |
<!-- formula-visual-ai-worklog:end -->
