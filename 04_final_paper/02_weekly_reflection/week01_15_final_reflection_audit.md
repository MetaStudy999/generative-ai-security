# 1주차-15주차 final 반영 점검표

## 점검 요약

`03_weekly_reports/` 아래 1주차부터 15주차까지 모든 주차에 `06_report/final/integrated_report_final.md`가 존재한다. 다만 기말 논문 초안과 기존 반영표는 W07, W08, W11, W14, W15를 중심으로 작성되어 있어, 전체 주차의 공통 내용과 수식 설명이 명시적으로 연결되지는 않았다. 본 점검에서는 15개 final 보고서를 모두 기말 논문의 배경·관련연구·위협모형·평가지표·재현성 근거로 다시 매핑하고, 논문별 핵심 수식/알고리즘 보충표를 별도 파일로 추가했다.

## 반영 원칙

| 구분 | 반영 방식 |
|---|---|
| W01-W06 | 딥러닝, 최적화, 컴퓨터비전, Transformer, SSL, 생성모형의 AI 원리와 poisoning/backdoor/deepfake 위협을 공통 이론 배경으로 반영 |
| W07-W08 | LLM/RAG 보안, prompt injection, benchmark contamination, source verification을 핵심 사례로 반영 |
| W09-W13 | DRL, FL, DP/MI, 검증/XAI, 모델 도난/워터마킹을 다중 보안 평가축으로 반영 |
| W14-W15 | MLOps, 공급망, 재현성, 참고문헌 검증, AI 활용 고지를 제출 가능성·연구윤리 통제로 반영 |

## 주차별 반영 상태

| 주차 | final 보고서 | 기말 논문 반영 위치 | 반영 상태 | 추가 보완 |
|---|---|---|---|---|
| W01 | `w01_deep_learning_ml_security/06_report/final/integrated_report_final.md` | 1장 배경, 4장 생명주기 위협모형 | 반영 보완 | 역전파, F1, 대적위험, privacy attack advantage 설명 추가 |
| W02 | `w02_optimization_data_poisoning/06_report/final/integrated_report_final.md` | 2장 관련연구, 4장 평가방법 | 반영 보완 | ERM/SGD, poisoning bilevel objective, ASR 설명 추가 |
| W03 | `w03_computer_vision_adversarial/06_report/final/integrated_report_final.md` | 2장 관련연구, 6장 무결성 | 반영 보완 | convolution, attention, robust accuracy 설명 추가 |
| W04 | `w04_transformer_nlp_security/06_report/final/integrated_report_final.md` | 2장 관련연구, 6장 privacy | 반영 보완 | attention complexity, adversarial text objective, prompt leakage 설명 추가 |
| W05 | `w05_ssl_backdoor/06_report/final/integrated_report_final.md` | 2장 관련연구, 4장 평가방법 | 반영 보완 | contrastive loss, poisoning, backdoor ASR 설명 추가 |
| W06 | `w06_diffusion_gan_deepfake/06_report/final/integrated_report_final.md` | 2장 관련연구, 6장 safety | 반영 보완 | diffusion loss, GAN min-max, deepfake detection 지표 설명 추가 |
| W07 | `w07_llm_security_privacy/06_report/final/integrated_report_final.md` | 1장, 2장, 4장 핵심 축 | 반영 완료 | LLM 평가 평균, unsafe rate, code vulnerability rate 설명 추가 |
| W08 | `w08_rag_prompt_injection/06_report/final/integrated_report_final.md` | 2장, 3장, 4장 핵심 축 | 반영 완료 | retrieval top-k, GraphRAG score, injection ASR 설명 추가 |
| W09 | `w09_drl_cybersecurity/06_report/final/integrated_report_final.md` | 4장 평가방법, 6장 safety | 반영 보완 | Bellman update, policy return, safety violation 설명 추가 |
| W10 | `w10_federated_learning_security/06_report/final/integrated_report_final.md` | 4장 평가방법, 6장 privacy/integrity | 반영 보완 | FedAvg, robust aggregation, FL backdoor ASR 설명 추가 |
| W11 | `w11_differential_privacy_mi/06_report/final/integrated_report_final.md` | 4장 핵심 평가축, 6장 privacy | 반영 완료 | DP 정의, DP-SGD, MI advantage 설명 추가 |
| W12 | `w12_nn_verification_xai/06_report/final/integrated_report_final.md` | 4장 평가방법, 6장 accountability | 반영 보완 | verification property, Lipschitz bound, explanation stability 설명 추가 |
| W13 | `w13_model_stealing_watermarking/06_report/final/integrated_report_final.md` | 2장 관련연구, 6장 confidentiality/accountability | 반영 보완 | extraction fidelity, watermark z-score, FPR/TPR 설명 추가 |
| W14 | `w14_mlops_supply_chain/06_report/final/integrated_report_final.md` | 4장 재현성, 5장 감사 결과 | 반영 완료 | evidence coverage, deployment risk, anomaly score 설명 추가 |
| W15 | `w15_reproducibility_xai_paper/06_report/final/integrated_report_final.md` | 5장 분석, 6장 책임성, 부록 | 반영 완료 | contamination rate, assurance coverage, TCAV 설명 추가 |

## 보완 결과

| 보완 항목 | 결과 |
|---|---|
| 15주차 final 존재 여부 | 15/15 확인 |
| 기말 논문 반영표 | W01-W15 전체 기준으로 확장 |
| 수식/알고리즘 보충 | `04_final_paper/04_methodology_experiment/formula_metric_supplement.md` 추가 |
| 주차별 final 보고서 직접 반영 | 15/15 보고서에 `2.1 핵심 수식 또는 알고리즘 쉬운 설명` 섹션 추가 |
| 초안 반영 방식 | 핵심 연구축은 W07/W08/W11/W14/W15, 전체 배경과 평가축은 W01-W15로 명시 |
| 주의사항 | 수식 보충표는 보고서 이해용 대표 수식이다. 원문에서 직접 인용한 수식이 필요한 경우 최종 제출 전 논문 원문 쪽/절 번호를 대조해야 한다. |
