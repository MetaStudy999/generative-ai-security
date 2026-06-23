# W10 기말논문 연결표

## 1. 이번 주차에서 얻은 연구 주제 후보

| 번호 | 주제 후보 | 대상 시스템 | 보안 위협 | 방법론 | 기여 가능성 |
|---:|---|---|---|---|---|
| 1 | 연합학습 환경에서 malicious client 비율에 따른 poisoning/backdoor 위험 분석 | FL 시스템 | Model poisoning, backdoor | synthetic FL 모의실험, 지표 비교 | 높음 |
| 2 | FL 보안 평가를 위한 utility-privacy-robustness 통합 지표 연구 | FL 시스템 | Gradient leakage, privacy attack, poisoned update | 평가 프레임워크 설계 | 높음 |
| 3 | Robust aggregation이 ASR과 clean accuracy에 미치는 영향 비교 | FL 모델 | Backdoor, malicious client | FedAvg와 coordinate median 비교 | 높음 |

## 1.1 KCI/SCI 확장 후보

| 구분 | 제목 후보 | 확장 방향 |
|---|---|---|
| KCI | 연합학습 환경에서 악성 클라이언트 비율과 집계 방식이 Backdoor ASR에 미치는 영향 분석 | 국내 연구 배경, 국문 초록, 국내 참고문헌 보완 |
| SCI | A Multi-Metric Evaluation Framework for Backdoor Robustness and Privacy Exposure in Federated Learning Under Malicious Client Participation | 복수 seed, 실제 FL framework, DP/secure aggregation, non-IID benchmark 확장 |

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

Privacy Leakage Proxy는 실제 gradient inversion 또는 membership inference 성공률이 아니라 update norm 기반 대용 지표다. 따라서 기말논문에는 실제 privacy attack 결과가 아니라 privacy exposure proxy로만 표기한다.

## 4. 사용 시 주의

본 결과는 synthetic toy logistic regression에 한정된다. 기말논문에 직접 실험 결과로 사용하려면 복수 seed, 다양한 non-IID split, 다른 aggregation rule, privacy attack 지표를 추가해야 한다. 실제 FL 서비스, 실제 개인정보, 실제 공격 payload는 연구윤리와 안전 심사 없이 포함하지 않는다.

<!-- AUTO-WEEKLY-BRIDGE-CHECK:start -->
## 자동 보완: 기말논문 연결 3문장

1. 이 주차에서 기말논문에 반영할 개념: 연합학습(FL) & FL 위협·방어·정책의 핵심 개념을 LLM/RAG 시스템 생명주기별 위협·통제 항목으로 반영한다.
2. 이 주차에서 기말논문에 반영할 표·그림·실험: 주차별 실험표, metrics_summary.csv 기반 그래프, config/seed/run_log 재현성 증거를 표·그림 후보로 반영한다.
3. 이 주차가 RAG 문서 오염/LLM 보안 감사 프레임워크와 연결되는 지점: 문서 오염, 프롬프트/컨텍스트 변조, 모델·운영 로그 감사 항목을 분리하는 LLM 보안 감사 체크포인트와 연결된다.
<!-- AUTO-WEEKLY-BRIDGE-CHECK:end -->
