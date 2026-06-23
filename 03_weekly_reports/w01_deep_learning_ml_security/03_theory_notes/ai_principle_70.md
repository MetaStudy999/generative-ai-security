# W01 AI 원리 70% 정리

## 0. 문서 목적

이 문서는 W01의 AI 원리 70%를 정리한다. 목표는 딥러닝을 단순히 “정확도를 내는 모델”로 보지 않고, **데이터 → 표현학습 → 최적화 → 일반화 → 생명주기 보증 → 보안 취약성**으로 이어지는 시스템으로 이해하는 것이다.

---

## 1. W01 AI 원리의 핵심 주장

W01에서 AI 원리는 다음 세 가지로 요약된다.

1. 딥러닝은 원시 입력을 여러 층의 표현으로 변환하는 함수 근사 시스템이다.
2. 학습은 손실함수를 줄이는 파라미터를 찾는 최적화 과정이고, 일반화는 보지 못한 데이터에서도 성능이 유지되는지를 뜻한다.
3. 보안 취약성은 모델이 학습한 표현, gradient, 데이터 분포, 출력 인터페이스, 평가 가정이 공격자에게 어떻게 노출되는지와 연결된다.

---

## 2. 핵심 개념표

| 개념 | 정의 | 직관적 설명 | 관련 논문 | 보안 연결 |
|---|---|---|---|---|
| Deep Learning | 여러 처리 계층을 통해 데이터의 추상 표현을 학습하는 ML 방법 | 픽셀, 로그, 패킷 같은 원시 입력을 점점 의미 있는 특징으로 바꾼다. | P01 | 표현공간 공격, 모델 취약성 |
| Representation Learning | 사람이 직접 설계한 특징 대신 모델이 유용한 특징 공간을 학습하는 것 | 좋은 표현을 배우면 분류·탐지·생성 과제가 쉬워진다. | P01 | adversarial example, leakage |
| Backpropagation | 손실의 기울기를 뒤로 전파해 파라미터를 갱신하는 학습 절차 | 모델이 어디서 틀렸는지 계산하고 각 층을 조금씩 고친다. | P01 | gradient 기반 공격의 원리 배경 |
| Generalization | 학습 데이터가 아닌 새 데이터에서도 성능이 유지되는 성질 | 시험 문제만 외우지 않고 새로운 문제도 푸는 능력이다. | P01, P02 | overfitting, MIA |
| ML Lifecycle | 데이터 수집, 전처리, 학습, 검증, 배포, 모니터링의 반복 과정 | 모델 하나가 아니라 운영 파이프라인 전체를 봐야 한다. | P02 | MLOps, evidence chain |
| Intrusion Detection | 정상/공격 행위를 탐지하거나 이상행위를 식별하는 보안 응용 | 모델의 오류가 오탐과 미탐 비용으로 이어진다. | P03 | IDS 평가 지표 |
| Robustness | 입력 교란이나 분포 변화에서도 성능이 크게 무너지지 않는 성질 | 공격자가 입력을 살짝 바꿔도 모델이 버티는지 보는 기준이다. | P04 | ASR, robust accuracy |
| Privacy Leakage | 모델이나 출력이 학습 데이터 정보를 노출하는 위험 | 모델이 정답을 맞히면서도 학습 데이터 비밀을 흘릴 수 있다. | P05 | MIA, inversion |

---

## 3. 핵심 수식

> 아래 수식은 W01 이론 설명을 위한 표준 정의식이다. 원문 수식의 직접 인용이 아니라, 보고서에서 AI 원리와 보안 평가를 연결하기 위한 정형화 표현이다.

### 3.1 경험위험 최소화

$$
R(\theta)=\mathbb{E}_{(x,y)\sim D}\left[\ell(f_\theta(x),y)\right]
$$

실제 학습에서는 전체 분포를 알 수 없으므로 학습 데이터 평균 손실을 최소화한다.

$$
\hat{R}(\theta)=\frac{1}{n}\sum_{i=1}^{n}\ell(f_\theta(x_i),y_i)
$$

**보안 연결:** 이 목적함수는 정상 학습 데이터 기준의 성능을 최적화한다. 공격 입력, 데이터 오염, 프라이버시 누출은 별도의 평가가 필요하다.

---

### 3.2 Gradient Descent

$$
\theta_{t+1}=\theta_t-\eta\nabla_\theta L(\theta_t)
$$

| 기호 | 의미 |
|---|---|
| $\theta$ | 모델 파라미터 |
| $\eta$ | learning rate |
| $L$ | 손실함수 |
| $\nabla_\theta L$ | 파라미터에 대한 손실의 기울기 |

**보안 연결:** gradient는 학습을 가능하게 하지만, gradient 정보는 adversarial example 생성이나 privacy inference의 단서가 될 수 있다.

---

### 3.3 일반화 격차

성능 기준으로 표현하면 다음과 같다.

$$
GeneralizationGap_{acc}=Acc_{train}-Acc_{test}
$$

손실 기준으로 표현하면 다음과 같다.

$$
GeneralizationGap_{loss}=Loss_{test}-Loss_{train}
$$

**보안 연결:** 일반화 격차가 크면 과적합 가능성이 높고, 이는 membership inference 위험 신호가 될 수 있다.

---

### 3.4 대적 위험

$$
R_{adv}(\theta)=\mathbb{E}_{(x,y)\sim D}\left[\max_{\delta\in\Delta}\ell(f_\theta(x+\delta),y)\right]
$$

| 기호 | 의미 |
|---|---|
| $\delta$ | 입력 교란 |
| $\Delta$ | 허용된 교란 집합 |
| $R_{adv}$ | 공격 조건에서의 위험 |

**보안 연결:** 모델 평가는 정상 입력뿐 아니라 최악의 허용 교란 입력에서도 수행되어야 한다.

---

### 3.5 Privacy Leakage와 Membership Inference

$$
Adv_{MI}=\Pr[A(z)=1\mid z\in D_{train}]-\Pr[A(z)=1\mid z\notin D_{train}]
$$

**보안 연결:** 모델이 특정 데이터의 학습 포함 여부를 드러내면 기밀성이 훼손된다. 이는 모델이 정확할 때도 발생할 수 있다.

---

## 4. 알고리즘 흐름

### 4.1 일반 ML 학습 흐름

```text
1. 데이터 수집
2. 전처리 및 라벨 검수
3. 학습/검증/테스트 split
4. 모델 학습
5. clean 성능 평가
6. robust/privacy/reproducibility 평가
7. 배포 전 보증 증거 확인
8. 운영 중 모니터링과 로그 보존
```

### 4.2 보안 평가가 추가되는 지점

| ML 단계 | 일반 ML 질문 | 보안 평가 질문 |
|---|---|---|
| 데이터 수집 | 데이터가 충분한가 | 데이터 출처와 개인정보 포함 여부는 확인했는가 |
| 학습 | 손실이 줄었는가 | poisoning, overfitting, leakage 위험은 없는가 |
| 검증 | test accuracy가 높은가 | robust accuracy, ASR, MI advantage는 어떤가 |
| 배포 | 서비스가 동작하는가 | model extraction, logging, access control은 준비됐는가 |
| 모니터링 | 성능이 유지되는가 | drift, 오탐/미탐, 사고 추적 로그가 남는가 |

---

## 5. 초보자용 설명

딥러닝은 입력을 받아 정답을 외우는 기계가 아니다. 입력을 여러 단계의 특징으로 바꿔 가며 규칙을 찾는 시스템이다. 문제는 그 규칙이 항상 사람의 직관과 같지 않다는 데 있다.

모델은 정상 데이터에서는 잘 맞지만, 사람이 보기에는 거의 같은 입력을 다르게 판단할 수 있다. 또한 출력 확률, confidence, embedding만으로도 학습 데이터의 흔적이 드러날 수 있다. 그래서 AI 보안에서는 accuracy 하나만 보지 않고, robust accuracy, ASR, leakage risk, evidence coverage를 함께 본다.

---

## 6. 보안 연구와의 연결

| AI 원리 | 연결되는 보안 문제 | 관련 주차 |
|---|---|---|
| Gradient | adversarial example, saliency manipulation | W03, W12 |
| Representation | feature leakage, embedding inversion | W05, W11 |
| Generalization | overfitting, membership inference | W11 |
| Lifecycle | data/model/deployment risk | W14, W15 |
| Evaluation | benchmark contamination, metric gaming | W15 |
| Output Interface | model extraction, privacy leakage | W13 |

---

## 7. W01 결론

W01에서 딥러닝은 “정확도를 내는 모델”이 아니라 **데이터, 학습, 평가, 배포가 연결된 시스템**으로 정의한다. 이후 주차의 공격과 방어는 이 시스템의 어느 단계와 자산을 겨냥하는지에 따라 정리한다.
