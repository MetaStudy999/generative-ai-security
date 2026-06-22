# 주차별 보고서 반영표

| 번호 | 주차 | 기말 논문 반영 위치 | 반영할 핵심 내용 | 활용 방식 |
|---:|---|---|---|---|
| 1 | W01 딥러닝 패러다임 & ML 보안 분류학 | 1장 서론, 4장 연구방법 | ML 생명주기, 표현학습, privacy/robustness 공통 평가축 | 공통 배경 |
| 2 | W02 대규모 최적화 & 데이터 오염 위협 | 2장 관련연구, 4장 평가방법 | ERM/SGD, poisoning, backdoor ASR | 훈련 단계 위협 |
| 3 | W03 컴퓨터비전 & 대적 공격 | 2장 관련연구, 6장 보안적 함의 | CNN/ViT, robust accuracy, adversarial perturbation | 무결성 위협 |
| 4 | W04 Transformer/NLP 보안 | 2장 관련연구, 6장 프라이버시 | attention, NLP adversarial attack, prompt privacy | LLM 배경 |
| 5 | W05 SSL & backdoor | 2장 관련연구, 4장 평가방법 | contrastive learning, SSL 추천/영상, backdoor stealthiness | 표현학습 위협 |
| 6 | W06 Diffusion/GAN & deepfake | 2장 관련연구, 6장 안전성 | diffusion loss, GAN min-max, deepfake reliability | 생성모형 안전성 |
| 7 | W07 LLM 보안·프라이버시 | 1장 서론, 2장 관련연구 | LLM 평가, benchmark contamination, 데이터 추출 위험 | 핵심 배경 |
| 8 | W08 RAG·프롬프트 인젝션 | 2장 관련연구, 3장 연구문제 | RAG 문서 오염, indirect prompt injection, human approval gate | 핵심 위협모형 |
| 9 | W09 DRL 사이버보안 | 4장 평가방법, 6장 안전성 | MDP, reward design, safety violation | 보조 평가축 |
| 10 | W10 연합학습 보안 | 4장 평가방법, 6장 프라이버시/무결성 | FedAvg, robust aggregation, FL backdoor | 분산학습 위협 |
| 11 | W11 차등프라이버시 & MI | 4장 연구방법, 6장 프라이버시 | DP, DP-SGD, MI risk, utility-privacy trade-off | 핵심 평가축 |
| 12 | W12 NN 검증 & XAI | 4장 평가방법, 6장 책임성 | certified robustness, explanation stability, trade-off | 검증·설명 신뢰성 |
| 13 | W13 모델 도난 & 워터마킹 | 2장 관련연구, 6장 책임성 | extraction fidelity, watermark detection, FPR | 모델 IP 보호 |
| 14 | W14 MLOps/공급망 보안 | 4장 연구방법, 5장 분석 | Docker, config, seed, artifact inventory, supply-chain risk | 재현성 체크리스트 |
| 15 | W15 연구평가·재현성·XAI·논문 구성 | 5장 분석, 6장 책임성, 부록 | 참고문헌 검증, AI 활용 고지, benchmark contamination | 연구윤리·제출 검증 |

## 반영 구조

W01-W06은 AI 보안 평가의 공통 이론 배경과 대표 위협을 제공한다. W07-W08은 본 논문의 직접 사례인 LLM/RAG 보안 위협을 구성한다. W09-W13은 강화학습, 연합학습, 프라이버시, 검증, 모델 IP 보호를 통해 평가 지표의 확장성을 보완한다. W14-W15는 재현성·참고문헌 검증·AI 활용 고지를 포함한 제출 가능성 통제로 연결한다.
