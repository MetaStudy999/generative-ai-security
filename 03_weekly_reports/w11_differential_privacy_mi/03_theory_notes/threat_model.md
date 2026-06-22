# 위협모형

| 항목 | 내용 |
|---|---|
| 대상 시스템 | 개인정보가 포함될 수 있는 ML/DL 학습 시스템과 DP 적용 모델 |
| 보호 자산 | 학습 데이터 포함 여부, 개인 레코드, confidence score, loss 신호, 모델 출력, 평가 로그 |
| 공격자 | 외부 질의자, 모델 사용자, API 접근자, 내부 평가자 |
| 공격자의 지식 | Black-box 출력 관찰부터 gray-box 평가 로그 접근까지 구분 |
| 공격자의 능력 | 모델 질의, confidence score 관찰, synthetic member/non-member 평가, 출력 비교 |
| 공격 경로 | 모델 API, 예측 확률, 학습 결과, 평가 로그, FL update |
| 공격 성공 조건 | 특정 데이터가 학습에 사용되었는지 통계적으로 우연 이상으로 구분 |
| 방어자 가정 | DP-SGD 또는 DP-like noise, output restriction, calibration, regularization, privacy accounting 가능 |
| 제외 범위 | 실제 개인정보 데이터 사용, 실제 개인 대상 추론, 무단 API 대량 질의, 운영 시스템 공격 |

## 연구문제 후보

RQ1. DP-SGD 또는 DP-like noise의 강도 변화는 모델 accuracy와 membership inference risk 사이에 어떤 trade-off를 만드는가?

RQ2. Membership inference 위험은 overfitting, confidence score, 학습/평가 데이터 분포 차이에 따라 어떻게 달라지는가?

RQ3. AI 보안 연구에서 DP를 주장할 때 privacy accounting, utility, attack evaluation, reproducibility log를 어떤 최소 항목으로 함께 보고해야 하는가?
