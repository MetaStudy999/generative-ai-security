# W11 기말논문 연결표

## 1. 이번 주차에서 얻은 연구 주제 후보

| 번호 | 주제 후보 | 대상 시스템 | 보안 위협 | 방법론 | 기여 가능성 |
|---:|---|---|---|---|---|
| 1 | AI 보안 연구에서 privacy claim을 검증하기 위한 다중지표 평가 프레임워크 | ML/DL 학습 시스템 | Membership inference, privacy leakage, DP misuse | 문헌분석 + toy 실험 + 체크리스트 | 높음 |
| 2 | DP-SGD/DP-like 방어의 utility-privacy trade-off 보고 기준 연구 | DP 적용 모델 | 과도한 epsilon, accountant 누락, utility degradation | accuracy/MI/leakage/accounting 표준 보고 | 높음 |
| 3 | 멤버십 추론 관점의 AI privacy risk threat model | 모델 API와 평가 로그 | membership information 노출 | 위협모형 + synthetic evaluation protocol | 높음 |

## 2. 기말 논문에 반영할 내용

| 논문 장 | 반영 가능 내용 |
|---|---|
| 서론 | AI 모델 학습에서 privacy protection과 utility trade-off를 동시에 평가해야 하는 문제의식 |
| 관련연구 | DP misuse, centralized DP-DL, MI attack/defense survey, FL 확장 대체 문헌 |
| 연구문제 | privacy claim 검증을 위한 utility, MI risk, leakage, accounting, reproducibility의 결합 |
| 연구방법 | synthetic toy 실험, threat model, DOI/PDF 검증표, seed/config/output log |
| 분석/실험 | Accuracy 0.956250 baseline, DP-like high utility drop 0.006250, leakage score 비교 |
| 보안적 함의 | DP claim accountability, 실제 개인정보/운영 API 제외 원칙 |
| 결론 | 재현 가능한 privacy evaluation reporting checklist 제안 |

## 3. W11에서 바로 가져갈 표

| 평가 항목 | W11 지표 | 기말논문 활용 |
|---|---|---|
| Utility | Accuracy, Utility Drop | 모델 효용 손실 분석 |
| Membership Risk | MI Attack Accuracy | privacy risk proxy |
| Leakage | Privacy Leakage Score | confidence gap 기반 leakage 해석 |
| Privacy Claim | Epsilon Proxy / formal epsilon 구분 | DP 주장 검증 책임 |
| Reproducibility | seed, config, CSV/JSON/log | 실험 재현성 장 |
