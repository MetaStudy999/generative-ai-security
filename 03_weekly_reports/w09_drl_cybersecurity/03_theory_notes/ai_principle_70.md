# AI 원리 70% 정리

## 1. 핵심 이론

강화학습은 agent가 environment의 state를 관측하고 action을 선택한 뒤 reward를 받아 policy를 개선하는 순차 의사결정 틀이다. DRL은 value function 또는 policy를 deep neural network로 근사해 큰 상태공간을 다룬다. W09의 보안 논의는 이 구조 위에서 출발한다. 공격자는 모델 자체보다 state observation, reward signal, environment feedback을 조작해 정책을 우회할 수 있다.

## 2. 핵심 개념표

| 개념 | 정의 | 직관적 설명 | 관련 논문 |
|---|---|---|---|
| Reinforcement Learning | 보상을 통해 순차 행동 정책을 학습하는 방법 | 시행착오로 좋은 행동을 찾는다 | P01 |
| Agent | 상태를 보고 행동을 선택하는 학습 주체 | 방어 에이전트 | P01, P03 |
| Environment | 행동의 결과와 보상을 돌려주는 세계 | 네트워크/호스트/로그 시뮬레이터 | P01, P03 |
| State | 의사결정에 쓰이는 현재 관측 정보 | alert level, 자산 중요도, 취약 여부 | P01, P03 |
| Action | agent가 선택하는 대응 | monitor, isolate, patch, escalate | P03, P04 |
| Reward | 행동의 좋고 나쁨을 수치화한 신호 | 탐지 성공 보상, 오탐 비용, 안전 위반 패널티 | P01, P03 |
| MDP | state, action, transition, reward, discount로 구성된 의사결정 모델 | 다음 상태가 현재 상태와 행동에 의존한다 | P01, P05 |
| Q-function | state-action pair의 기대 누적 보상 | 이 상태에서 이 행동이 얼마나 좋은가 | P01 |
| DQN | Q-function을 neural network로 근사하는 DRL 방법 | 큰 상태공간의 Q-table 대체 | P01, P03 |
| Policy Gradient | policy parameter를 직접 업데이트하는 방법 | 행동 확률 자체를 학습한다 | P01 |
| Actor-Critic | actor가 행동을 고르고 critic이 가치를 평가하는 구조 | 정책 학습과 가치 평가를 결합한다 | P01, P03 |
| DRL Verification | DRL policy가 safety/robustness specification을 만족하는지 확인 | 높은 reward와 안전성을 분리해 본다 | P05 |

## 3. 수식 또는 알고리즘

MDP는 보통 `(S, A, P, R, gamma)`로 표현한다. agent는 return을 최대화하는 policy를 찾는다.

```text
G_t = r_{t+1} + gamma r_{t+2} + gamma^2 r_{t+3} + ...
Q(s, a) <- Q(s, a) + alpha [r + gamma max_a' Q(s', a') - Q(s, a)]
```

W09 toy 실험은 deep neural network 대신 tabular Q-learning을 사용했다. 목적은 고성능 DRL 구현이 아니라, reward manipulation이 정책 선택과 안전 지표에 미치는 방향을 재현 가능하게 보여주는 것이다.

## 4. 초보자용 설명

DRL 에이전트는 “어떤 상황에서 어떤 행동을 하면 장기적으로 점수가 높아지는가”를 배운다. 문제는 점수판이 틀릴 수 있다는 점이다. 보안 환경에서 reward가 잘못 설계되거나 조작되면 agent는 실제로는 위험한 행동을 하면서도 학습상으로는 좋은 행동이라고 믿게 된다.

## 5. 보안 연구와의 연결

W09의 핵심 연결은 다음 세 가지다.

| AI 원리 | 보안 질문 | W09 실험 연결 |
|---|---|---|
| State | 공격자가 alert를 낮추거나 높이면 정책이 흔들리는가 | perturbed alert 평가 |
| Action | 자동 대응이 오탐/미탐 상황에서 안전한가 | safety violation rate |
| Reward | 보상 신호가 조작되면 방어 성능이 낮아지는가 | manipulated reward 조건 |
