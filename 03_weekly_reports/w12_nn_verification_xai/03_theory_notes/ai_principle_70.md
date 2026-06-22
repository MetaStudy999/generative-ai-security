# AI 원리 70% 정리

## 1. 핵심 관점

W12의 AI 원리는 신경망 검증, abstraction, formal methods, robustness proof, XAI explanation stability, robustness-accuracy-fairness trade-off를 하나의 평가 구조로 이해하는 것이다. 핵심은 모델이 clean test에서 맞았는지뿐 아니라, 작은 입력 변화 범위에서 명세를 만족하는지, 설명 결과가 안정적인지, 검증 비용이 감당 가능한지를 함께 보는 데 있다.

## 2. 핵심 개념표

| 개념 | 정의 | 직관적 설명 | W12 연결 |
|---|---|---|---|
| Neural network verification | 특정 입력 영역에서 모델 출력이 명세를 만족하는지 확인하는 절차 | 테스트셋 평균 성능보다 강한 질문을 던진다 | P01 |
| Abstraction | 복잡한 네트워크 계산을 검증 가능한 근사 표현으로 바꾸는 방법 | 세부 계산을 줄여 검증 가능성을 높인다 | P01 |
| Reachability | 가능한 입력 집합이 출력 공간에서 어디까지 도달하는지 분석 | 작은 입력 변화가 위험 출력으로 이어지는지 본다 | P01 |
| Empirical robustness | 제한된 공격/테스트 조건에서 관측한 강건성 | 공격을 해봤더니 버텼는가 | P02 |
| Certified robustness | 명세와 bound에 근거해 보증 가능한 강건성 | 정해진 범위 안에서 안전하다고 말할 수 있는가 | P01, P04 |
| Lipschitz bound | 입력 변화 대비 출력 변화의 상한을 제한하는 관점 | 작은 입력 변화가 큰 출력 변화로 증폭되는지 제한한다 | P04 |
| XAI stability | 입력 변화 전후 설명 결과의 일관성 | 예측뿐 아니라 설명도 흔들리지 않는지 본다 | P03 |
| Multi-objective evaluation | accuracy, robustness, fairness를 함께 보는 평가 | 하나의 점수로 안전성을 과장하지 않는다 | P05 |

## 3. 대표 수식과 지표

아래 식은 원문 직접 인용이 아니라 W12 보고서의 설명용 정리다.

| 지표 | 설명 |
|---|---|
| `Clean Accuracy` | 정상 synthetic test data에서 예측이 맞은 비율 |
| `Robust Accuracy` | toy perturbation proxy 후에도 예측이 맞은 비율 |
| `Certified Rate` | 선형 모델 margin bound proxy가 양수인 샘플 비율 |
| `Explanation Stability` | clean/perturbed feature attribution의 cosine similarity |
| `Fairness Gap` | synthetic group 간 accuracy 차이 |
| `Verification Cost` | bound proxy 계산 시간(ms) |

## 4. 초보자용 설명

일반 평가가 "시험지를 풀어봤더니 몇 점인가"라면, 신경망 검증은 "시험지가 조금 바뀌어도 답이 안전하게 유지되는가"를 묻는다. XAI 안정성은 "답의 이유도 비슷하게 유지되는가"를 묻는다. Robustness-accuracy-fairness trade-off는 "한쪽을 높였을 때 다른 중요한 기준이 나빠지지 않았는가"를 묻는다.

## 5. 실험 해석 한계

W12의 `certified_rate`는 toy logistic classifier의 선형 margin bound proxy일 뿐 formal verifier가 발급한 DNN certificate가 아니다. `adversarial_features()`도 실제 PGD/FGSM 구현이 아니라 선형 가중치 부호 기반 toy perturbation proxy다.
