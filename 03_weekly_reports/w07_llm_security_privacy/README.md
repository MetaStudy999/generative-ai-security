<!-- AUTO-GENERATED-WEEKLY-AUDIT-README -->
# [W07] LLM 학습·정렬·평가 & LLM 보안·프라이버시

자동 생성 파일: `scripts/weekly_audit.py`

## 1. 주차 핵심 주제

- 강의계획서상 주제: LLM 학습·정렬·평가 & LLM 보안·프라이버시
- AI 원리: `03_theory_notes/ai_principle_70.md` 중심으로 정리
- 보안 이슈: `03_theory_notes/security_issue_30.md`, `threat_model.md` 중심으로 정리

## 2. 주요 논문

| ID | 제목 | 저자 | 연도 | 학술지/학회명 | DOI 또는 URL | 확인 경로 | 확인일 | 상태 |
|---|---|---|---:|---|---|---|---|---|
| P01 | J. Chang et al., *A Survey on Evaluation of Large Language Models*, ACM Computing Surveys, 2024 | 확인 필요 | 확인 필요 | 확인 필요 | https://doi.org/10.1145/3641289 | `01_papers/paper_list.md`, `01_papers/doi_check.md` | 현 세션 인터넷 미확인 | 부분 검증 |
| P02 | Ankur Das et al., *Security and Privacy Challenges of Large Language Models: A Survey*, ACM Computing Surveys, 2025 | 확인 필요 | 확인 필요 | 확인 필요 | https://doi.org/10.1145/3712001; arXiv https://arxiv.org/abs/2402.00888 | `01_papers/paper_list.md`, `01_papers/doi_check.md` | 현 세션 인터넷 미확인 | DOI/제목 불일치 의심 |
| P03 | Mingzhe Yao et al., *A survey on large language model security and privacy: problems, methods, and opportunities*, AI Open, 2024 | 확인 필요 | 확인 필요 | 확인 필요 | https://doi.org/10.1016/j.hcc.2024.100211; arXiv https://arxiv.org/abs/2312.02003 | `01_papers/paper_list.md`, `01_papers/doi_check.md` | 현 세션 인터넷 미확인 | 대체 문헌 후보 |
| P04 | Yongtao Yin et al., *A survey on multimodal large language models*, National Science Review, 2024 | 확인 필요 | 확인 필요 | 확인 필요 | https://doi.org/10.1093/nsr/nwae403; arXiv https://arxiv.org/abs/2306.13549 | `01_papers/paper_list.md`, `01_papers/doi_check.md` | 현 세션 인터넷 미확인 | DOI/제목 불일치 의심 |
| P05 | Shujun Li et al., *When Software Security Meets Large Language Models: A Survey*, IEEE/CAA Journal of Automatica Sinica, 2025 | 확인 필요 | 확인 필요 | 확인 필요 | https://doi.org/10.1109/JAS.2024.124971 | `01_papers/paper_list.md`, `01_papers/doi_check.md` | 현 세션 인터넷 미확인 | DOI/제목 불일치 의심 |

주의: 현 세션에서는 인터넷으로 DOI/URL 실제 존재 여부를 재검증하지 않았으므로, 로컬 검증 기록이 있더라도 최종 제출 전 사람이 확인한다.

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
- [w07_submission_report.html](07_week_submission/w07_submission_report.html)
- [w07_submission_report.md](07_week_submission/w07_submission_report.md)

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

- config.yaml 상태: `safe_synthetic_run` (executed 상태와 outputs 일치)
- outputs 폴더 존재 여부: O
- metrics_summary.csv 존재 여부: O
- results.json 존재 여부: O
- run_log.md 존재 여부: O
- 그래프 파일 존재 여부: O
- 수치 대조 상태: 기준 원천 존재
- 수치 기준 원천: `03_weekly_reports/w07_llm_security_privacy/04_experiment/outputs/metrics_summary.csv`

## 5. 기말논문 연결

1. 이 주차에서 기말논문에 반영할 개념: LLM 학습·정렬·평가 과정의 보안·프라이버시 위협면을 기말논문 위협모형의 핵심 축으로 반영한다.
2. 이 주차에서 기말논문에 반영할 표·그림·실험: 주차별 실험표, metrics_summary.csv 기반 그래프, config/seed/run_log 재현성 증거를 표·그림 후보로 반영한다.
3. 이 주차가 RAG 문서 오염/LLM 보안 감사 프레임워크와 연결되는 지점: 프롬프트, 파라미터, 학습데이터, 출력 로그에서 발생하는 개인정보·정렬 우회 위험을 RAG/LLM 감사 프레임워크의 상위 위협면으로 연결한다.

## 6. 확인 필요 항목

- 참고문헌 검증 필요 항목: 확인 필요 0건, 부분 검증 키워드 1건, 대체 문헌 키워드 1건
- 수치 대조 필요 항목: 기준 원천 존재
- PDF/HTML 수동 확인 필요 항목: PDF 시각적 깨짐과 HTML 렌더링은 자동 정상 처리하지 않음
- 참고문헌 실제 존재 여부, 강의계획서 지정 문헌과 로컬 PDF 일치 여부, 최종 제출본 서식은 사람이 직접 확인해야 한다.

이 README는 파일 존재와 구조를 자동으로 정리한 문서이며, 참고문헌 진위·논문 품질·PDF 시각 검수는 사람이 별도로 확인해야 한다.
