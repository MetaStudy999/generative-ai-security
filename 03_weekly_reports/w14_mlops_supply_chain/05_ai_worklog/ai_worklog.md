# AI 활용 기록

| 일자 | 도구 | 사용 목적 | 주요 입력 | 산출물 | 본인 검토 | 검증 방법 |
|---|---|---|---|---|---|---|
| 2026-06-22 | Codex | 공통 지침과 W14 프롬프트 확인 | `README.md`, `03_weekly_reports/README.md`, `01_codex_prompts/W14_mlops_supply_chain.md` | 작업 범위 정리 | 실험 수치는 outputs 기준으로만 반영 | 로컬 파일 대조 |
| 2026-06-22 | Codex | 로컬 PDF 메타데이터 대조 | W14 PDF 첫 페이지, 수업 검수보고서 | P01 제목 보정, P03/P04/P05 대체 PDF 상태 기록 | DOI와 원문 불일치 항목 분리 | PDF first page, 수업자료 대조 |
| 2026-06-22 | Codex | Synthetic toy MLOps pipeline 작성 및 실행 | config.yaml, 공통 실험 산출물 규칙 | run_experiment.py, outputs 6개 파일 | 실제 개인정보/운영 서비스 사용 없음 확인 | run_log, CSV, JSON 대조 |
| 2026-06-22 | Codex | 보고서·제출본·발표자료 작성 | 실행 결과와 W14 문헌요약 | 통합보고서, 제출본, 발표 패키지 | 수치 일관성 확인 | `rg`와 파일별 표 대조 |

## 사용 원칙

- AI 산출물은 초안이며 최종 책임은 작성자에게 있다.
- DOI, URL, 정량 결과는 근거 파일이 있을 때만 적는다.
- P03/P04/P05의 공식 원문 PDF는 최종 제출 전 사람이 재확인한다.

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
| 입력 근거 | `w14_mlops_supply_chain/04_experiment/outputs/metrics_summary.csv`, 기존 통합보고서, 발표 슬라이드, 이론노트 |
| 생성 산출물 | `09_presentation/assets/charts/w14_metrics_chart.svg`, `09_presentation/assets/diagrams/w14_pipeline_diagram.svg`, `09_presentation/assets/figure_manifest.md` |
| 검증 방식 | CSV에서 읽은 기존 수치만 차트화하고, 수식은 표준 정의식으로 한정했으며, formal guarantee가 불명확한 항목은 확인 필요로 표시 |
| 안전 범위 | 공개 데이터, synthetic/toy 데이터, 로컬 모의실험 설명으로 제한하고 실제 시스템 악용 절차는 작성하지 않음 |
<!-- formula-visual-ai-worklog:end -->
