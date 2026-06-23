# AI 활용 기록

| 일자 | 도구 | 사용 목적 | 주요 입력 | 산출물 | 본인 검토 | 검증 방법 |
|---|---|---|---|---|---|---|
| 2026-06-22 | Codex | W03 보고서 구조 보완 및 초안 작성 | `W03` 프롬프트와 로컬 파일 상태 | 논문 요약, 이론노트, 보안노트, 실험 설계, 통합보고서 초안 | 원문/DOI/수치 검증 항목은 별도 표시 | PDF 파일명, 프롬프트 논문 목록, 최종 원문 대조 |
| 2026-06-22 | Codex | W03 실험 결과 완성 및 문서 갱신 | 로컬 W03 실험 폴더와 사용자 요청 | `src/run_experiment.py`, `outputs/` 결과, 관련 Markdown 업데이트 | synthetic toy 범위와 실행 로그 기준 수치 확인 | `python3 src/run_experiment.py --config configs/config.yaml`, `outputs/run_log.md` |
| 2026-06-22 | Codex | W03 발표용 보고서 작성 | W03 최종 통합보고서와 실험 로그 | `09_presentation/presentation_report.md` | 발표 수치와 한계 표현 확인 | `04_experiment/outputs/run_log.md`, `06_report/final/integrated_report_final.md` |
| 2026-06-22 | Codex | W03 제출용 보고서와 HTML 작성 | W03 통합보고서, 발표보고서, 실험 로그 | `w03_submission_report.md/html`, `presentation_report.html` | 제출 수치, DOI/URL 확인 상태, toy 한계 확인 | `04_experiment/outputs/run_log.md`, `01_papers/doi_check.md` |
| 2026-06-22 | Codex | W03 발표용 슬라이드 작성 | W03 발표용 보고서와 실험 로그 | `presentation_slides.md`, `presentation_slides.html` | 슬라이드 수치와 한계 표현 확인 | `04_experiment/outputs/run_log.md` |
| 2026-06-22 | Codex | W03 발표 보조자료 작성 | W03 발표 슬라이드와 실험 로그 | `speaker_notes.md`, `qna.md`, `one_page_handout.md` | 발화 대본, 예상 질문, 배포 요약의 수치와 한계 표현 확인 | `presentation_slides.md`, `04_experiment/outputs/run_log.md` |
| 2026-06-22 | Codex | W03 최종 보완 | 공통 README, 템플릿 원칙, W03 최종 보완 지시, 로컬 산출물 | DOI/URL 재검증, 16장 목차, KCI/SCI 섹션, PDF 위험 표시 | DOI/URL은 Crossref/DOI 기준 확인, 수치는 `outputs/` 로그와 대조, PDF 삭제는 미실행 | `python3 src/run_experiment.py --config configs/config.yaml`, `outputs/run_log.md`, `git ls-files`, GitHub API |

## 사용 원칙

- AI 산출물은 초안이며 최종 책임은 작성자에게 있다.
- DOI, URL, 정량 결과는 임의 생성하지 않는다.
- 확인된 DOI/URL도 최종 제출 전 사람이 인용 형식과 PDF 보관 정책을 재검토한다.

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
| 입력 근거 | `w03_computer_vision_adversarial/04_experiment/outputs/metrics_summary.csv`, 기존 통합보고서, 발표 슬라이드, 이론노트 |
| 생성 산출물 | `09_presentation/assets/charts/w03_metrics_chart.svg`, `09_presentation/assets/diagrams/w03_pipeline_diagram.svg`, `09_presentation/assets/figure_manifest.md` |
| 검증 방식 | CSV에서 읽은 기존 수치만 차트화하고, 수식은 표준 정의식으로 한정했으며, formal guarantee가 불명확한 항목은 확인 필요로 표시 |
| 안전 범위 | 공개 데이터, synthetic/toy 데이터, 로컬 모의실험 설명으로 제한하고 실제 시스템 악용 절차는 작성하지 않음 |
<!-- formula-visual-ai-worklog:end -->
