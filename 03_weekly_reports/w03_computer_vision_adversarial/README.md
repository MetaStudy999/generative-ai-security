<!-- AUTO-GENERATED-WEEKLY-AUDIT-README -->
# [W03] 컴퓨터비전 표현학습 & 비전 대적공격

자동 생성 파일: `scripts/weekly_audit.py`

## 1. 주차 핵심 주제

- 강의계획서상 주제: 컴퓨터비전 표현학습 & 비전 대적공격
- AI 원리: `03_theory_notes/ai_principle_70.md` 중심으로 정리
- 보안 이슈: `03_theory_notes/security_issue_30.md`, `threat_model.md` 중심으로 정리

## 2. 주요 논문

| ID | 제목 | 저자 | 연도 | 학술지/학회명 | DOI 또는 URL | 확인 경로 | 확인일 | 상태 |
|---|---|---|---:|---|---|---|---|---|
| P01 | Gradient-Based Learning Applied to Document Recognition | Yann LeCun, Leon Bottou, Yoshua Bengio, Patrick Haffner | 1998 | 확인 필요 | 확인 필요 | `01_papers/paper_list.md`, `01_papers/doi_check.md` | 검증 기록 기반 | 확인 완료(로컬/공식 검증 기록 기준) |
| P02 | Deep Learning for Computer Vision: A Brief Review | Athanasios Voulodimos, Nikolaos Doulamis, Anastasios Doulamis, Eftychios Protopapadakis | 2018 | 확인 필요 | 확인 필요 | `01_papers/paper_list.md`, `01_papers/doi_check.md` | 검증 기록 기반 | 확인 완료(로컬/공식 검증 기록 기준) |
| P03 | Multimodal Learning With Transformers: A Survey | Peng Xu, Xiatian Zhu, David A. Clifton | 2023 | 확인 필요 | 확인 필요 | `01_papers/paper_list.md`, `01_papers/doi_check.md` | 검증 기록 기반 | 확인 완료(로컬/공식 검증 기록 기준) |
| P04 | Transformers in Vision: A Survey | Salman Khan, Muzammal Naseer, Munawar Hayat, Syed Waqas Zamir, Fahad Shahbaz Khan, Mubarak Shah | 2022 | 확인 필요 | 확인 필요 | `01_papers/paper_list.md`, `01_papers/doi_check.md` | 검증 기록 기반 | 확인 완료(로컬/공식 검증 기록 기준) |
| P05 | A Survey of Robustness and Safety of 2D and 3D Deep Learning Models against Adversarial Attacks | Yanjie Li, Bin Xie, Songtao Guo, Yuanyuan Yang, Bin Xiao | 2024 | 확인 필요 | 확인 필요 | `01_papers/paper_list.md`, `01_papers/doi_check.md` | 검증 기록 기반 | 확인 완료(로컬/공식 검증 기록 기준) |

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
- [README.md](04_experiment/outputs/README.md)
- [metrics_summary.csv](04_experiment/outputs/metrics_summary.csv)
- [results.json](04_experiment/outputs/results.json)
- [run_log.md](04_experiment/outputs/run_log.md)
- [README.md](04_experiment/results/README.md)

- 주차별 제출 보고서:
- [integrated_report_draft.md](06_report/draft/integrated_report_draft.md)
- [integrated_report_final.md](06_report/final/integrated_report_final.md)
- [w03_submission_report.html](07_week_submission/w03_submission_report.html)
- [w03_submission_report.md](07_week_submission/w03_submission_report.md)

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
- 수치 대조 상태: 기준 원천 존재
- 수치 기준 원천: `03_weekly_reports/w03_computer_vision_adversarial/04_experiment/outputs/metrics_summary.csv`

## 5. 기말논문 연결

1. 이 주차에서 기말논문에 반영할 개념: 컴퓨터비전 표현학습 & 비전 대적공격의 핵심 개념을 LLM/RAG 시스템 생명주기별 위협·통제 항목으로 반영한다.
2. 이 주차에서 기말논문에 반영할 표·그림·실험: 주차별 실험표, metrics_summary.csv 기반 그래프, config/seed/run_log 재현성 증거를 표·그림 후보로 반영한다.
3. 이 주차가 RAG 문서 오염/LLM 보안 감사 프레임워크와 연결되는 지점: 문서 오염, 프롬프트/컨텍스트 변조, 모델·운영 로그 감사 항목을 분리하는 LLM 보안 감사 체크포인트와 연결된다.

## 6. 확인 필요 항목

- 참고문헌 검증 필요 항목: 확인 필요 0건, 부분 검증 키워드 0건, 관련 보조 문헌 키워드 0건
- 수치 대조 필요 항목: 기준 원천 존재
- PDF/HTML 수동 확인 필요 항목: PDF 시각적 깨짐과 HTML 렌더링은 자동 정상 처리하지 않음
- 참고문헌 실제 존재 여부, 강의계획서 지정 문헌과 로컬 PDF 일치 여부, 최종 제출본 서식은 사람이 직접 확인해야 한다.

이 README는 파일 존재와 구조를 자동으로 정리한 문서이며, 참고문헌 진위·논문 품질·PDF 시각 검수는 사람이 별도로 확인해야 한다.
