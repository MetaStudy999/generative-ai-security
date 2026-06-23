<!-- AUTO-GENERATED-WEEKLY-AUDIT-README -->
# [W15] 연구평가·재현성·설명가능성(XAI)·논문 구성

자동 생성 파일: `scripts/weekly_audit.py`

## 1. 주차 핵심 주제

- 강의계획서상 주제: 연구평가·재현성·설명가능성(XAI)·논문 구성
- AI 원리: `03_theory_notes/ai_principle_70.md` 중심으로 정리
- 보안 이슈: `03_theory_notes/security_issue_30.md`, `threat_model.md` 중심으로 정리

## 2. 주요 논문

| ID | 제목 | 저자 | 연도 | 학술지/학회명 | DOI 또는 URL | 확인 경로 | 확인일 | 상태 |
|---|---|---|---:|---|---|---|---|---|
| P01 | A Survey on Evaluation of Large Language Models | Yupeng Chang et al. | 2024 | ACM Transactions on Intelligent Systems and Technology | https://doi.org/10.1145/3641289 | `01_papers/paper_list.md`, `01_papers/doi_check.md` | 검증 기록 기반 | 확인 완료(로컬/공식 검증 기록 기준) |
| P02 | Assuring the Machine Learning Lifecycle: Desiderata, Methods, and Challenges | Rob Ashmore, Radu Calinescu, Colin Paterson | 2021 | ACM Computing Surveys | https://doi.org/10.1145/3453444 | `01_papers/paper_list.md`, `01_papers/doi_check.md` | 검증 기록 기반 | 확인 완료(로컬/공식 검증 기록 기준) |
| P03 | Explainable AI (XAI): Core Ideas, Techniques, and Solutions | Rudresh Dwivedi et al. | 2023 | ACM Computing Surveys | https://doi.org/10.1145/3561048 | `01_papers/paper_list.md`, `01_papers/doi_check.md` | 검증 기록 기반 | 확인 완료(로컬/공식 검증 기록 기준) |
| P04 | Explainable Artificial Intelligence (XAI): Concepts, taxonomies, opportunities and challenges toward responsible AI | Alejandro Barredo Arrieta et al. | 2020 | Information Fusion | https://doi.org/10.1016/j.inffus.2019.12.012 | `01_papers/paper_list.md`, `01_papers/doi_check.md` | 검증 기록 기반 | 확인 완료(로컬/공식 검증 기록 기준) |
| P05 | Concept-based Explainable Artificial Intelligence: A Survey | Eleonora Poeta et al. | 2025 | ACM Computing Surveys | https://doi.org/10.1145/3774643 | `01_papers/paper_list.md`, `01_papers/doi_check.md` | 검증 기록 기반 | 확인 완료(로컬/공식 검증 기록 기준) |

주의: 자동 감사는 로컬/공식 검증 기록을 대조하는 보조 점검이므로, 최종 제출 전 사람이 DOI landing page와 출판사/RISS 상세 페이지를 다시 확인한다.

## 3. 주요 산출물

- 논문 요약:
- [P01_summary.md](02_paper_summaries/P01_summary.md)
- [P02_summary.md](02_paper_summaries/P02_summary.md)
- [P03_summary.md](02_paper_summaries/P03_summary.md)
- [P04_summary.md](02_paper_summaries/P04_summary.md)
- [P05_summary.md](02_paper_summaries/P05_summary.md)

- 이론 정리:
- [ai_principle_70.md](03_theory_notes/ai_principle_70.md)
- [security_issue_30.md](03_theory_notes/security_issue_30.md)
- [threat_model.md](03_theory_notes/threat_model.md)

- 실험 보고서:
- [experiment_report.md](04_experiment/experiment_report.md)
- [metrics_summary.csv](04_experiment/outputs/metrics_summary.csv)
- [results.json](04_experiment/outputs/results.json)
- [run_log.md](04_experiment/outputs/run_log.md)

- 주차별 제출 보고서:
- [integrated_report_draft.md](06_report/draft/integrated_report_draft.md)
- [integrated_report_final.md](06_report/final/integrated_report_final.md)
- [w15_submission_report.html](07_week_submission/w15_submission_report.html)
- [w15_submission_report.md](07_week_submission/w15_submission_report.md)

- 발표자료:
- [README.md](09_presentation/README.md)
- [figure_manifest.md](09_presentation/assets/figure_manifest.md)
- [README.md](09_presentation/assets/figures/README.md)
- [one_page_handout.md](09_presentation/one_page_handout.md)
- [presentation_report.html](09_presentation/presentation_report.html)
- [presentation_report.md](09_presentation/presentation_report.md)
- [presentation_slides.html](09_presentation/presentation_slides.html)
- [presentation_slides.md](09_presentation/presentation_slides.md)
- 외 2개

- AI 활용 고지:
- [ai_disclosure_draft.md](05_ai_worklog/ai_disclosure_draft.md)
- [ai_outputs.md](05_ai_worklog/ai_outputs.md)
- [ai_worklog.md](05_ai_worklog/ai_worklog.md)
- [human_review.md](05_ai_worklog/human_review.md)
- [prompts.md](05_ai_worklog/prompts.md)

- 기말논문 연결 자료:
- [contribution_candidates.md](08_final_paper_bridge/contribution_candidates.md)
- [final_paper_bridge.md](08_final_paper_bridge/final_paper_bridge.md)
- [topic_candidates.md](08_final_paper_bridge/topic_candidates.md)
- [weekly_reflection_table.md](08_final_paper_bridge/weekly_reflection_table.md)


## 4. 실험 및 결과

- config.yaml 상태: `executed` (executed 상태와 outputs 일치)
- outputs 폴더 존재 여부: O
- metrics_summary.csv 존재 여부: O
- results.json 존재 여부: O
- run_log.md 존재 여부: O
- 그래프 파일 존재 여부: O
- 수치 대조 상태: 자동 대조 완료
- 수치 기준 원천: `03_weekly_reports/w15_reproducibility_xai_paper/04_experiment/outputs/metrics_summary.csv`

## 5. 기말논문 연결

1. 이 주차에서 기말논문에 반영할 개념: 재현성, 평가 프로토콜, 참고문헌 검증, AI 활용 고지를 기말논문 제출 품질관리 체계로 반영한다.
2. 이 주차에서 기말논문에 반영할 표·그림·실험: 주차별 실험표, metrics_summary.csv 기반 그래프, config/seed/run_log 재현성 증거를 표·그림 후보로 반영한다.
3. 이 주차가 RAG 문서 오염/LLM 보안 감사 프레임워크와 연결되는 지점: metrics/config/run_log/reference verification을 묶어 LLM 보안 감사 프레임워크의 증거 체인과 한계 고지 원칙으로 연결한다.

## 6. 확인 필요 항목

- 참고문헌 검증 필요 항목: 확인 필요 0건, 부분 검증 키워드 0건, 관련 보조 문헌 키워드 0건
- 수치 대조 필요 항목: 자동 대조 완료
- PDF/HTML 수동 확인 필요 항목: PDF 시각적 깨짐과 HTML 렌더링은 자동 정상 처리하지 않음
- 참고문헌 실제 존재 여부, 강의계획서 지정 문헌과 로컬 PDF 일치 여부, 최종 제출본 서식은 사람이 직접 확인해야 한다.

이 README는 파일 존재와 구조를 자동으로 정리한 문서이며, 참고문헌 진위·논문 품질·PDF 시각 검수는 사람이 별도로 확인해야 한다.
