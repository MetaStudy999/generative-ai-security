# W10 발표용 보고서

## 1. 발표 메타정보

| 항목 | 내용 |
|---|---|
| 주차 | W10 |
| 주제 | 연합학습(FL) & FL 위협·방어·정책 |
| 발표 시간 | 8-10분 |
| 핵심 메시지 | FL 보안 평가는 clean accuracy만으로 충분하지 않고, ASR·privacy leakage·aggregation rule을 함께 봐야 한다. |
| 실험 근거 | `04_experiment/outputs/run_log.md` |

## 2. 한 문장 요약과 발표 흐름

연합학습은 데이터를 중앙으로 모으지 않는 장점이 있지만, local update와 aggregation 단계가 새로운 보안 평가 지점이 된다.

발표 흐름은 FL 원리, 위협모형, 논문 5편의 역할, synthetic toy 실험, 기말논문 연결 순서로 진행한다.

## 3. 논문 5편의 발표 역할

| 논문 | 발표 역할 |
|---|---|
| P01 | FedAvg와 aggregation taxonomy를 설명하는 원리 배경 |
| P02 | FL security/privacy threat taxonomy 소개 |
| P03 | attack-defense taxonomy와 평가 프로토콜 연결 |
| P04 | privacy attack, defense, policy landscape 연결 |
| P05 | backdoor threat와 ASR 지표 설명 |

## 4. AI 원리 70% 발표 설명

FL은 client가 local data로 update를 만들고 server가 aggregation으로 global model을 갱신하는 구조다. FedAvg는 평균 집계이고, coordinate median 같은 robust aggregation은 이상 update에 덜 민감한 방어 후보가 된다. Non-IID data, personalization, communication cost는 FL 성능과 보안 평가를 함께 흔든다.

## 5. 보안 이슈 30% 발표 설명

FL의 보안 이슈는 gradient leakage, membership inference, poisoning, model poisoning, backdoor, malicious client로 정리된다. 특히 backdoor는 clean accuracy가 유지되어도 특정 trigger 조건에서만 오동작할 수 있으므로 ASR을 별도로 측정해야 한다.

## 6. 실습/실험 실행 상태와 결과 근거

| 조건 | Malicious Client Rate | Aggregation | Global Accuracy | ASR | 해석 |
|---|---:|---|---:|---:|---|
| Clean FL | 0% | fedavg | 0.960000 | 0.136076 | 기준 조건 |
| Poisoned FL 10% | 10% | fedavg | 0.953333 | 0.297468 | ASR 상승 시작 |
| Poisoned FL 20% | 20% | fedavg | 0.950000 | 0.496835 | clean 성능은 유지되나 ASR 크게 상승 |
| Robust aggregation 20% | 20% | coordinate_median | 0.955000 | 0.237342 | ASR 완화, 완전 제거는 아님 |

모든 실험은 synthetic toy data만 사용했다. Privacy Leakage Proxy는 실제 gradient inversion 성공률이 아니라 update norm 기반 대용 지표다.

## 7. 기말논문 연결 지점

W10는 기말논문의 "AI 보안 평가는 utility, attack success, privacy exposure, reproducibility를 동시에 기록해야 한다"는 논지를 뒷받침한다. W11의 DP/MI, W14의 MLOps supply chain과 연결하면 분산 AI 시스템의 평가 프레임워크로 확장할 수 있다.

## 8. 예상 질문과 답변

| 질문 | 답변 |
|---|---|
| 왜 실제 FL framework를 쓰지 않았나? | 주차 목적은 공격 성능 경쟁이 아니라 평가표와 로그 구조를 안전하게 검증하는 것이다. |
| ASR이 높아도 accuracy가 높은 이유는? | backdoor는 전체 test set이 아니라 trigger 조건에서만 오동작을 유도하므로 clean accuracy만으로 드러나지 않을 수 있다. |
| Privacy Leakage Proxy는 실제 privacy attack인가? | 아니다. 실제 gradient inversion이나 membership inference가 아니라 update 노출 위험을 설명하는 대용 지표다. |
| Robust aggregation이면 충분한가? | coordinate median은 ASR을 낮췄지만 0.237342로 남아 있었다. 추가 방어와 로그 검증이 필요하다. |
