# 보안 이슈 30% 정리

## 1. 주요 보안 이슈

W11의 보안 이슈는 membership inference, privacy leakage, utility-privacy trade-off이다. 핵심 보호 자산은 학습 데이터 원문뿐 아니라 “특정 레코드가 학습에 포함되었는지”라는 membership information이다.

| 이슈 | 설명 | 방어/평가 연결 |
|---|---|---|
| Membership inference attack | 모델 출력, confidence, loss 등으로 학습 포함 여부를 추론 | MI attack accuracy |
| Training data leakage | 모델이 학습 데이터의 민감 패턴을 과도하게 반영 | privacy leakage score |
| Model memorization | 과적합 또는 반복 학습으로 특정 sample 신호가 커짐 | train/test confidence gap |
| Shadow/evaluation data | 공격 평가를 위해 member/non-member 역할을 나누는 데이터 | synthetic/public data로만 사용 |
| DP defense | clipping/noise/accounting으로 개별 sample 영향 제한 | epsilon/delta, utility drop |
| Output restriction | confidence/logit 노출 제한 | MI 신호 감소, usability 저하 가능 |

## 2. CIA 관점 분석

| 관점 | 관련 위협 | 설명 |
|---|---|---|
| Confidentiality | membership inference / training data leakage | 특정 개인 또는 레코드의 학습 포함 여부가 민감정보가 될 수 있다. |
| Integrity | privacy mechanism misuse | DP를 적용했다고 주장하지만 accountant나 설정이 부정확하면 연구 결론이 왜곡된다. |
| Availability | utility degradation from excessive noise | 과도한 noise는 모델 성능을 떨어뜨려 정상 사용성을 낮춘다. |
| Privacy | individual record exposure | 레코드 단위 포함 여부, 민감 속성, confidence 신호가 privacy risk가 된다. |
| Safety | incorrect privacy guarantee interpretation | `epsilon_proxy`나 toy 결과를 실제 DP 보장처럼 해석하면 위험하다. |
| Accountability | unverified DP claim / missing privacy accounting | DOI, 원문, 설정, seed, output log 없이 privacy claim을 확정하면 재현성이 떨어진다. |

## 3. 안전 범위

본 주차의 MI 평가는 synthetic/public 데이터 기반의 개념 검증으로만 다룬다. 실제 개인 데이터, 실제 운영 모델/API, 무단 대량 질의, 특정 개인의 학습 포함 여부 추론은 제외한다.
