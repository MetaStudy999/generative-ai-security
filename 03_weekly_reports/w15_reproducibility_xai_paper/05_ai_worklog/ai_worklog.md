# AI 활용 기록

| 일자 | 도구 | 사용 목적 | 주요 입력 | 산출물 | 본인 검토 | 검증 방법 |
|---|---|---|---|---|---|---|
| 2026-06-22 | Codex | W15 보고서 구조 보완 및 초안 작성 | `W15` 프롬프트, 공통 README, 로컬 W15 파일 상태 | 논문 요약, 이론노트, 보안노트, 통합보고서 보완 | 대체 PDF와 부분 확인 DOI를 별도 표시 | 로컬 PDF 첫 페이지, DOI 표, 출판사/아카이브 페이지 대조 |
| 2026-06-23 | Codex | W15 최종 보완 및 기말논문 연결 정리 | P03/P05 DOI 재검증, local audit outputs, 기말논문 초안 | 최신 16장 목차, KCI/SCI 섹션, 표/그림, AI 고지, 체크리스트 | P03은 DOI 부분 확인과 로컬 PDF 불일치로 표시, P05 DOI 확인 | DOI/Crossref/arXiv metadata, PDF metadata, run_log 대조 |
| 2026-06-22 | Codex | 로컬 재현성·제출 준비 감사 스크립트 작성 | W15 필수 산출물 목록, `04_final_paper` 연결 파일 목록 | `04_experiment/src/run_experiment.py`, `outputs/metrics_summary.csv`, `results.json`, `run_log.md` | 실제 공격·개인정보·모델 성능 주장 없음 확인 | 실행 로그와 CSV/JSON 값 대조 |
| 2026-06-22 | Codex | 제출본·발표자료 작성 | 통합보고서, 실험보고서, DOI 검증표, 감사 결과 | `07_week_submission/w15_submission_report.*`, `09_presentation/` | Markdown/HTML 상태값 일치 확인 | `outputs/run_log.md` 기준 수치 확인 |

## 사용 원칙

- AI 산출물은 초안이며 최종 책임은 작성자에게 있다.
- DOI, URL, 정량 결과는 임의 생성하지 않는다.
- 실행 로그가 없는 모델 성능 수치는 작성하지 않는다.
- P03 지정 논문 원문 PDF, P05 권호/issue, 국내 문헌은 최종 제출 전 사람이 재검증한다.

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
| 입력 근거 | `w15_reproducibility_xai_paper/04_experiment/outputs/metrics_summary.csv`, 기존 통합보고서, 발표 슬라이드, 이론노트 |
| 생성 산출물 | `09_presentation/assets/charts/w15_metrics_chart.svg`, `09_presentation/assets/diagrams/w15_pipeline_diagram.svg`, `09_presentation/assets/figure_manifest.md` |
| 검증 방식 | CSV에서 읽은 기존 수치만 차트화하고, 수식은 표준 정의식으로 한정했으며, formal guarantee가 불명확한 항목은 확인 필요로 표시 |
| 안전 범위 | 공개 데이터, synthetic/toy 데이터, 로컬 모의실험 설명으로 제한하고 실제 시스템 악용 절차는 작성하지 않음 |
<!-- formula-visual-ai-worklog:end -->
