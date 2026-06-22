# 00_folder_structure_integration_mapping.md
# 전체 폴더 구조 소문자 적용표

이 문서는 `00_전체폴더_생성.md`의 목표 구조를 현재 저장소에 소문자 폴더명으로 반영한 결과를 기록한다.

## 적용 원칙

- 기존 파일은 삭제하지 않는다.
- 폴더명은 소문자, 숫자, 언더바를 사용한다.
- 현재 `/home/ubuntu/genai`를 프로젝트 루트로 사용한다.
- 기존 강의자료, 논문 PDF, Codex 지시문은 새 소문자 경로 안에서 보존한다.
- 주차 폴더는 `w01_...`부터 `w15_...`까지 주제명을 포함한다.

## 최상위 폴더 매핑

| 지시서 기준 | 현재 저장소 적용 위치 | 처리 방식 |
|---|---|---|
| `AISEC_WEEKLY_REPORTS/` | `./` | 현재 `/home/ubuntu/genai`를 프로젝트 루트로 사용 |
| `00_class_materials` | `00_class_materials` | 강의자료와 README/요약 파일 보관 |
| `01_codex_prompts` | `01_codex_prompts` | Codex 지시문과 주차별 프롬프트 보관 |
| `02_report_templates` | `02_report_templates` | 보고서 템플릿 보관 |
| `03_weekly_reports` | `03_weekly_reports` | 주차별 PDF 구조와 관리/보고 템플릿 보관 |
| `04_final_paper` | `04_final_paper` | 기말논문 하위 구조 생성 |
| `05_references` | `05_references` | 참고문헌 하위 구조 생성 |
| `06_submission` | `06_submission` | 최종 제출물 하위 구조 생성 |
| `99_backup` | `99_backup` | 백업 하위 구조 생성 |

## 주차 폴더 매핑

| 지시서 기준 | 현재 저장소 적용 위치 | 주제 |
|---|---|---|
| `w01_deep_learning_ml_security` | `03_weekly_reports/w01_deep_learning_ml_security` | 딥러닝 패러다임 & ML 보안 분류학 |
| `w02_optimization_data_poisoning` | `03_weekly_reports/w02_optimization_data_poisoning` | 대규모 최적화 & 데이터 오염 위협 |
| `w03_computer_vision_adversarial` | `03_weekly_reports/w03_computer_vision_adversarial` | 컴퓨터비전 표현학습 & 비전 대적공격 |
| `w04_transformer_nlp_security` | `03_weekly_reports/w04_transformer_nlp_security` | Transformer 변형 & NLP 대적공격·프라이버시 |
| `w05_ssl_backdoor` | `03_weekly_reports/w05_ssl_backdoor` | 자기지도학습·파운데이션 모델 & Poisoning/Backdoor |
| `w06_diffusion_gan_deepfake` | `03_weekly_reports/w06_diffusion_gan_deepfake` | 확률생성모형(Diffusion/GAN) & 딥페이크 검출 |
| `w07_llm_security_privacy` | `03_weekly_reports/w07_llm_security_privacy` | LLM 학습·정렬·평가 & LLM 보안·프라이버시 |
| `w08_rag_prompt_injection` | `03_weekly_reports/w08_rag_prompt_injection` | RAG·프롬프팅 프레임워크 & 프롬프트 인젝션 |
| `w09_drl_cybersecurity` | `03_weekly_reports/w09_drl_cybersecurity` | 심층강화학습(DRL) & 사이버보안 적용·보상조작 |
| `w10_federated_learning_security` | `03_weekly_reports/w10_federated_learning_security` | 연합학습(FL) & FL 위협·방어·정책 |
| `w11_differential_privacy_mi` | `03_weekly_reports/w11_differential_privacy_mi` | 차등프라이버시(DP) & 멤버십 추론 공격·방어 |
| `w12_nn_verification_xai` | `03_weekly_reports/w12_nn_verification_xai` | 신경망 검증·정형방법 & 대적방어·XAI·강건성 트레이드오프 |
| `w13_model_stealing_watermarking` | `03_weekly_reports/w13_model_stealing_watermarking` | 모델 지식재산(IP)·모델 도난·모델 추출 위협 |
| `w14_mlops_supply_chain` | `03_weekly_reports/w14_mlops_supply_chain` | MLOps/DevOps·데이터/모델 파이프라인·공급망 보안 |
| `w15_reproducibility_xai_paper` | `03_weekly_reports/w15_reproducibility_xai_paper` | 연구평가·재현성·설명가능성(XAI)·논문 구성 |

## 주차 내부 폴더 매핑

| 지시서 기준 | 현재 저장소 적용 위치 | 비고 |
|---|---|---|
| `00_management` | `00_management` | 주차 관리 문서 보관 |
| `01_papers` | `01_papers` | PDF, BibTeX, 논문 목록 보관 |
| `02_paper_summaries` | `02_paper_summaries` | 논문 요약과 비교표 보관 |
| `03_theory_notes` | `03_theory_notes` | AI 원리와 보안 이슈 노트 보관 |
| `04_experiment` | `04_experiment` | Docker 기반 실습 기록 보관 |
| `05_ai_worklog` | `05_ai_worklog` | AI 활용 기록 보관 |
| `06_report` | `06_report` | 보고서 초안, 최종본, 리뷰 보관 |
| `07_week_submission` | `07_week_submission` | 주차별 제출 점검 자료 보관 |
| `08_final_paper_bridge` | `08_final_paper_bridge` | 기말논문 연결 자료 보관 |
