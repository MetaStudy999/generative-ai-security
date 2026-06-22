# AI 원리 70% 정리

## 1. 핵심 이론

W10의 AI 원리는 연합학습(Federated Learning, FL)의 학습 구조를 이해하는 것이다. FL은 각 client가 local data를 보유한 상태에서 local model update를 계산하고, server가 update를 aggregation하여 global model을 갱신하는 학습 방식이다. 핵심은 raw data를 중앙으로 모으지 않는다는 점이지만, model update 자체가 무결성·프라이버시 위험의 대상이 될 수 있다.

AI 원리 70%는 다음 질문을 중심으로 정리한다.

- client는 어떤 local objective를 최적화하는가?
- server는 어떤 aggregation rule로 update를 합치는가?
- FedAvg와 robust aggregation은 어떤 실패 조건이 다른가?
- Non-IID data와 client heterogeneity는 성능과 보안 평가를 어떻게 흔드는가?
- privacy, utility, communication cost는 어떤 trade-off를 만드는가?

## 2. 핵심 개념표

| 개념 | 정의 | 직관적 설명 | 관련 논문 |
|---|---|---|---|
| Federated Learning | 여러 client가 데이터를 직접 공유하지 않고 모델 update를 공유해 global model을 학습하는 구조 | 데이터는 각자 갖고, 모델만 협업해 만든다 | P01, P02 |
| Client | local data와 계산자원을 가진 참여자 | 각 기관·기기·사용자에 해당한다 | P01 |
| Server | client update를 수집하고 global model을 갱신하는 조정자 | 중앙 데이터 저장소가 아니라 조율자다 | P01, P04 |
| Aggregation | 여러 local update를 하나의 global update로 결합하는 절차 | 투표나 평균처럼 여러 의견을 합치는 단계 | P01 |
| FedAvg | client model parameter 또는 update를 평균해 global model을 만드는 대표 알고리즘 | 가장 기본적인 평균 집계 | P01 |
| Personalized FL | client별 데이터 분포 차이를 반영해 개인화 모델을 학습하는 접근 | 모두에게 같은 모델이 항상 최선은 아니다 | P01 |
| Non-IID Data | client마다 label 분포와 feature 분포가 다른 상황 | 병원·기기·지역마다 데이터 성격이 다르다 | P01, P03 |
| Robust Aggregation | 악성 또는 이상 update 영향을 줄이는 집계 방식 | 평균 대신 median처럼 이상값에 덜 흔들리는 규칙을 쓴다 | P03, P05 |
| Secure Aggregation | server가 개별 update를 직접 보지 않고 합산값만 얻도록 하는 보호 기법 | privacy에는 도움이 되지만 이상 update 탐지는 어려워질 수 있다 | P02, P04 |
| Communication Cost | round 수, 전송 parameter 수, client 수로 생기는 비용 | 좋은 모델도 너무 자주 많이 보내면 운영이 어렵다 | P01 |

## 3. 수식 또는 알고리즘

FedAvg의 기본 흐름은 다음과 같이 요약할 수 있다.

```text
1. server가 global parameter w_t를 client에 보낸다.
2. 각 client k는 local data D_k로 w_t를 여러 step 학습해 w_t^k를 만든다.
3. server는 client sample 수 또는 동일 가중치로 w_t^k를 평균해 w_{t+1}을 만든다.
4. 이 과정을 round 단위로 반복한다.
```

W10 toy 실험에서는 logistic regression parameter 3개를 10개 client가 25 round 동안 갱신했다. FedAvg 조건과 coordinate median 조건을 비교해 aggregation rule이 ASR에 어떤 차이를 만드는지 확인했다.

## 4. 초보자용 설명

연합학습은 "데이터를 모으지 않고 모델을 함께 학습한다"는 아이디어다. 하지만 server가 받는 model update가 모두 선의라고 가정하면 위험하다. 한 client가 나쁜 update를 보내면 global model이 특정 입력에서만 오동작할 수 있고, update 자체가 local data의 단서를 담을 수도 있다. 따라서 FL의 핵심 원리는 학습 구조와 aggregation 구조를 이해하는 데서 출발한다.

## 5. 보안 연구와의 연결

W10 실험에서 Clean FL은 global accuracy 0.960000, ASR 0.136076이었다. 20% poisoned FedAvg는 global accuracy가 0.950000으로 크게 무너지지 않았지만 ASR은 0.496835로 상승했다. 같은 20% 악성 client 조건에서 coordinate median은 ASR을 0.237342로 낮췄다. 이 결과는 FL 보안 평가에서 clean accuracy만 보면 위험을 놓칠 수 있음을 보여준다.
