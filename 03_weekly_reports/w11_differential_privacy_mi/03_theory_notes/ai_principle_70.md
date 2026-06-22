# AI 원리 70% 정리

## 1. 핵심 이론

W11의 중심 원리는 차등프라이버시(DP), privacy budget, DP-SGD, privacy accounting이다. DP는 한 개인 레코드가 데이터셋에 포함되었는지 여부가 모델 출력 또는 통계 결과에 과도하게 드러나지 않도록 확률적 경계를 두는 방식이다.

딥러닝에서는 DP-SGD가 대표 구현이다. 각 sample 또는 mini-batch gradient를 clipping하고 noise를 더한 뒤, 여러 학습 step에 걸친 privacy loss를 accountant로 추적한다. 이때 noise를 많이 넣으면 privacy risk가 낮아질 수 있지만 accuracy와 convergence가 나빠질 수 있다. 반대로 utility를 우선하면 DP 보장이 느슨해질 수 있다.

## 2. 핵심 개념표

| 개념 | 정의 | 직관적 설명 | 관련 논문 |
|---|---|---|---|
| Differential Privacy | 인접 데이터셋의 출력 분포 차이를 제한하는 privacy 정의 | 한 사람의 데이터가 들어갔는지 출력만 보고 알아차리기 어렵게 함 | P01, P02, P03 |
| Privacy Budget | 허용되는 privacy loss의 총량 | 예산이 작을수록 보호는 강하지만 utility 비용이 커질 수 있음 | P01, P02 |
| Epsilon | DP 보장에서 출력 분포 차이를 조절하는 핵심 매개변수 | 작은 epsilon은 강한 보호, 큰 epsilon은 약한 보호로 해석 | P01, P03 |
| Delta | 순수 DP가 아닌 approximate DP에서 허용하는 작은 실패확률 | 아주 드문 privacy guarantee 실패 여지 | P02, P03 |
| DP-SGD | gradient clipping과 noise injection을 결합한 SGD 변형 | 학습 업데이트가 개별 sample을 과도하게 반영하지 않게 함 | P02, P03 |
| Privacy Accounting | 여러 학습 step의 privacy loss를 누적 계산 | “총 privacy budget을 얼마나 썼는가”를 추적 | P02 |
| Utility-Privacy Trade-off | privacy 보호와 모델 성능 사이의 상충관계 | noise가 커지면 leakage는 줄 수 있지만 accuracy도 흔들릴 수 있음 | P01, P05 |

## 3. 수식 또는 알고리즘

```text
데이터 준비
-> sample/gradient별 clipping
-> noise injection
-> model update
-> privacy accounting
-> accuracy, MI risk, leakage, utility drop 동시 평가
```

DP claim은 다음 네 가지를 함께 적어야 해석 가능하다.

| 항목 | 보고 이유 |
|---|---|
| epsilon/delta | privacy guarantee의 수치적 조건 |
| accountant | 여러 step의 privacy loss 계산 방식 |
| clipping/noise 설정 | DP-SGD 구현의 핵심 조절값 |
| utility/leakage 지표 | 실제 모델 효용과 privacy risk 확인 |

## 4. 초보자용 설명

DP는 “데이터 하나가 들어가도 모델이 너무 달라지지 않게 만드는 약속”이다. 하지만 약속이 있으려면 수학적 조건, 구현 설정, 누적 계산이 모두 맞아야 한다. 단순히 noise를 넣었다고 DP가 되는 것은 아니다.

## 5. 보안 연구와의 연결

Membership inference는 DP가 막고자 하는 대표 privacy risk 중 하나다. 공격자가 confidence나 loss를 보고 “이 sample이 학습에 있었나”를 맞히려 할 때, DP와 regularization은 train/test 신호 차이를 줄이는 방어로 해석할 수 있다. 따라서 W11의 실험도 accuracy만 보지 않고 `MI Attack Accuracy`, `Privacy Leakage Score`, `Utility Drop`을 함께 기록한다.
