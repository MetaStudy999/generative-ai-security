# W02 AI 활용 기록

| 일자 | AI 도구 | 사용 목적 | 입력 자료 | 산출물 | 본인 검토/수정 필요 | 검증 방법 |
|---|---|---|---|---|---|---|
| 2026-06-22 | Codex | W02 폴더 구조 점검 | 로컬 파일 목록, W02 지시서 | 누락 산출물 목록 파악 | 제출 범위 확인 | `rg --files`, W02 prompt 대조 |
| 2026-06-22 | Codex | 논문 요약 보강 | 로컬 PDF 파일명, PDF 메타데이터, arXiv/DOI 검색 결과 | P01-P05 요약, 비교표 | 출판 판본 최종 대조 | PDF metadata, DOI/URL 표 |
| 2026-06-22 | Codex | 이론/보안 노트 작성 | W02 주제, 논문 요약 | AI 원리, 보안 이슈, 위협모형, 평가방법 | 수업 표현과 맞춤 | 최종보고서와 상호 대조 |
| 2026-06-22 | Codex | 실험 코드 작성 | 지시서의 scikit-learn digits 실습 요구 | `src/run_experiment.py`, config, README | Docker 실행 검증 | py_compile, 의존성 안내 확인 |
| 2026-06-22 | Codex | Docker 실습 실행 및 결과 반영 | W02 실험 코드와 config | `outputs/metrics_summary.csv`, `results.json`, `run_log.md`, 보고서 결과표 | 결과 해석 범위 확인 | Docker build/run, 출력 파일 확인 |
| 2026-06-22 | Codex | 최종보고서/발표자료 작성 | 보강된 주차 산출물 | 통합보고서, 제출용 보고서, 발표자료 | 발표 시간에 맞춘 축약 | 체크리스트 검토 |
| 2026-06-22 | Codex | 공통 지침 재점검 및 발표 파일명 보강 | 루트 README, W02 지시서, 기존 W02 발표자료 | `presentation_report.*`, `presentation_slides.*`, 체크리스트 갱신 | 기존 W02 별칭 파일과 중복 제공 범위 확인 | 공통 발표 패키지 파일명 대조 |

## 사용 원칙

- AI 산출물은 초안 작성과 구조화에 사용했다.
- 논문 DOI/URL은 확인 가능한 근거가 있는 경우에만 기록했다.
- 실험 결과는 Docker 실행 로그가 생성된 뒤 반영했다.
- 최종 제출자는 인용, 실험 결과, 문장 표현, 연구윤리 책임을 직접 확인해야 한다.

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
| 입력 근거 | `w02_optimization_data_poisoning/04_experiment/outputs/metrics_summary.csv`, 기존 통합보고서, 발표 슬라이드, 이론노트 |
| 생성 산출물 | `09_presentation/assets/charts/w02_metrics_chart.png`, `09_presentation/assets/charts/w02_metrics_chart.svg`, `09_presentation/assets/diagrams/w02_pipeline_diagram.svg`, `09_presentation/assets/figure_manifest.md` |
| 검증 방식 | CSV에서 읽은 기존 수치만 차트화하고, 수식은 표준 정의식으로 한정했으며, formal guarantee가 불명확한 항목은 확인 필요로 표시 |
| 안전 범위 | 공개 데이터, synthetic/toy 데이터, 로컬 모의실험 설명으로 제한하고 실제 시스템 악용 절차는 작성하지 않음 |
<!-- formula-visual-ai-worklog:end -->
