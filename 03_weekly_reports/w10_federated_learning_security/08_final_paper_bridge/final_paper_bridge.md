# W10 기말논문 연결표

## 1. 이번 주차에서 얻은 연구 주제 후보

| 번호 | 주제 후보 | 대상 시스템 | 보안 위협 | 방법론 | 기여 가능성 |
|---:|---|---|---|---|---|
| 1 | 연합학습 환경에서 malicious client 비율에 따른 poisoning/backdoor 위험 분석 | FL 시스템 | Model poisoning, backdoor | synthetic FL 모의실험, 지표 비교 | 높음 |
| 2 | FL 보안 평가를 위한 utility-privacy-robustness 통합 지표 연구 | FL 시스템 | Gradient leakage, privacy attack, poisoned update | 평가 프레임워크 설계 | 높음 |
| 3 | Robust aggregation이 ASR과 clean accuracy에 미치는 영향 비교 | FL 모델 | Backdoor, malicious client | FedAvg와 coordinate median 비교 | 높음 |

## 2. 기말 논문에 반영할 내용

| 논문 장 | 반영 가능 내용 |
|---|---|
| 서론 | 분산 AI 학습과 데이터 프라이버시 요구 증가, FL의 양면성 |
| 관련연구 | FL aggregation taxonomy, FL security/privacy survey, FL backdoor survey |
| 연구문제 | clean accuracy만으로 보안성을 판단할 수 없는 문제 |
| 연구방법 | synthetic/toy 실험 또는 문헌 기반 평가표 설계 |
| 분석/실험 | malicious client rate, global accuracy, ASR, privacy leakage proxy 비교 |
| 보안적 함의 | confidentiality, integrity, privacy, accountability 관점 |
| 결론 | 재현 가능한 FL 보안 평가 프레임워크 제안 |

## 3. W10 결과의 연결 문장

W10 toy 실험에서 20% poisoned FedAvg는 global accuracy 0.950000을 유지했지만 ASR 0.496835를 보였다. 같은 악성 client 비율에서 coordinate median은 ASR을 0.237342로 낮췄다. 이 결과는 AI 보안 평가에서 일반 성능과 공격 성공률을 함께 기록해야 한다는 기말 논문의 핵심 논지로 연결된다.

## 4. 사용 시 주의

본 결과는 synthetic toy logistic regression에 한정된다. 기말논문에 직접 실험 결과로 사용하려면 복수 seed, 다양한 non-IID split, 다른 aggregation rule, privacy attack 지표를 추가해야 한다.
