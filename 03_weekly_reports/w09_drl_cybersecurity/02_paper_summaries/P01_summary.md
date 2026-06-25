# P01 Summary

## Deep Reinforcement Learning: A Brief Survey — Kai Arulkumaran et al., IEEE Signal Processing Magazine, 2017

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W09 심층강화학습(DRL) & 사이버보안 적용·보상조작 |
| 논문명 | Deep Reinforcement Learning: A Brief Survey |
| 저자 | Kai Arulkumaran, Marc Peter Deisenroth, Miles Brundage, Anil Anthony Bharath |
| 공식 출판 정보 | IEEE Signal Processing Magazine, Vol. 34, No. 6, pp. 26–38, Nov. 2017 |
| DOI | https://doi.org/10.1109/MSP.2017.2743240 |
| 로컬 PDF | `01_papers/pdf/01_Arulkumaran_et_al_2017_Deep_Reinforcement_Learning_Survey.pdf` |
| 검증 상태 | W09 `paper_list.md` 기준 공식 DOI 확인. 로컬 PDF는 arXiv extended version이므로 출판판과 세부 차이 메모 유지 |
| PDF 확인 메모 | repo의 PDF 폴더에 해당 PDF blob이 존재함을 확인했다. 요약은 로컬 PDF 경로와 W09 `paper_list.md`의 공식 DOI 메타데이터 기준으로 보완했다. |
| 핵심 근거 사용 가능 여부 | 가능. W09에서 DRL의 state-action-reward-policy-value-function 기본 원리와 사이버 방어 자동화 모델링의 이론 배경으로 사용 |

---

## 1. 한 문장 요약

이 논문은 deep reinforcement learning을 **Markov Decision Process, state, action, reward, return, value function, Q-learning, DQN, policy gradient, actor-critic, exploration, memory, attention, unsupervised auxiliary learning** 관점에서 정리하며, W09에서 사이버 방어 자동화와 보상조작 위험을 순차 의사결정 문제로 모델링하기 위한 핵심 AI 원리 기반을 제공한다.

---

## 2. 핵심 연구문제

> 강화학습의 순차 의사결정 구조를 심층신경망과 결합하면 복잡한 상태공간에서 어떤 방식으로 정책을 학습할 수 있으며, 이 구조를 사이버보안에 적용할 때 reward 설계·상태 관찰·정책 안정성·검증 가능성은 어떤 문제가 되는가?

| 번호 | 연구질문 |
|---|---|
| RQ1 | DRL은 MDP 기반 순차 의사결정을 deep neural network function approximation으로 어떻게 확장하는가? |
| RQ2 | Value-based, policy-based, actor-critic 방법은 어떤 수학적 차이와 학습 특성을 갖는가? |
| RQ3 | Exploration과 exploitation trade-off는 자동 방어 agent가 새로운 공격을 탐색하는 과정에서 어떤 의미를 갖는가? |
| RQ4 | Experience replay, target network, policy gradient, actor-critic은 학습 안정성과 sample efficiency를 어떻게 개선하는가? |
| RQ5 | 사이버보안 환경에서 reward function이 잘못 설계되면 agent가 실제 안전이 아니라 점수만 최대화하는 reward hacking 정책을 학습할 수 있는가? |

---

## 3. 논문의 핵심 기여

| 기여 | 설명 | W09 연결 |
|---|---|---|
| DRL 기본 틀 정리 | RL의 state, action, reward, policy, value function을 deep learning과 연결 | W09 AI 원리 70% 핵심 |
| 주요 알고리즘 분류 | DQN, policy gradient, actor-critic, model-based/model-free RL 계열 정리 | cyber defense agent 설계 기준 |
| Function approximation 설명 | 고차원 상태공간에서 deep neural network가 value/policy를 근사하는 방식 설명 | 보안 로그·alert 상태 표현 연결 |
| Exploration 문제 제시 | 탐색과 활용의 균형, sparse reward, sample efficiency 문제 정리 | cyber range 실험 설계 연결 |
| 응용·한계 정리 | control, robotics, perception, planning 등 응용과 안정성 문제 제시 | W09 P03~P05 사이버보안·검증 문헌 연결 |

---

## 4. 목차별 핵심 개괄

| 목차 | 핵심 내용 | 비전공자용 이해 |
|---|---|---|
| 1. Introduction | Deep learning과 reinforcement learning의 결합이 복잡한 의사결정 문제에서 성과를 내기 시작했으며, DRL은 perception과 control을 end-to-end로 연결한다. | AI가 정답표를 보고 배우는 것이 아니라, 직접 행동해보고 점수를 받으며 더 나은 선택법을 배운다. |
| 2. Background: Reinforcement Learning | Agent, environment, state, action, reward, policy, return, value function, MDP의 기본 구조를 설명한다. | 게임처럼 현재 상태를 보고 행동을 고르고, 그 결과로 점수를 받아 다음 행동을 개선하는 방식이다. |
| 3. Value-Based Methods | Q-learning과 DQN 계열을 정리한다. DQN은 deep neural network로 Q-value를 근사하고 experience replay와 target network로 안정화한다. | 각 행동이 얼마나 좋은지 점수를 예측하고, 가장 점수가 높은 행동을 고르는 방식이다. |
| 4. Policy Gradient Methods | Policy 자체를 직접 parameterized function으로 두고 expected return을 최대화한다. 연속 행동공간이나 확률적 정책에 유리하다. | 행동별 점수를 따로 계산하기보다 “이 상황에서는 이런 행동을 할 확률” 자체를 학습한다. |
| 5. Actor-Critic Methods | Actor는 행동을 고르고 critic은 그 행동이 얼마나 좋은지 평가한다. value-based와 policy-based의 장점을 결합한다. | 한 명은 실행하고, 한 명은 코치처럼 평가하면서 같이 배우는 구조다. |
| 6. Model-Based RL | 환경의 dynamics를 모델링해 planning과 simulation을 활용한다. sample efficiency를 높일 수 있지만 model error가 누적될 수 있다. | 실제로 다 해보기 어렵기 때문에 가상 환경을 만들어 미리 연습하는 방식이다. |
| 7. Memory, Attention, Unsupervised Learning | POMDP, long-term dependency, representation learning을 위해 memory, attention, auxiliary task가 사용된다. | 현재 화면만 보고 판단하기 어렵다면 과거 기록과 중요한 단서에 집중해야 한다. |
| 8. Applications and Challenges | Atari, robotics, control 등에서 성과가 있었지만 안정성, sample efficiency, generalization, safety 문제가 남아 있다. | DRL은 강력하지만 훈련이 느리고, 예상 밖 행동을 할 수 있어 실제 보안 시스템에 바로 넣기 어렵다. |
| 9. Conclusion | DRL은 고차원 의사결정 문제의 유망한 방법이지만 안정성·검증·안전성·재현성 문제가 중요하다. | 보안 자동대응에 쓰려면 “잘 배운다”보다 “안전하게 검증 가능하다”가 더 중요하다. |

---

## 5. 핵심 이론 및 수식

> 아래 수식은 DRL의 기본 원리와 W09 사이버보안 적용을 설명하기 위한 표준화된 표현이다. 수식은 GitHub, MS Word, PDF 변환 호환성을 위해 Markdown 표 밖의 LaTeX block math로 작성한다.

### 5.1 Markov Decision Process

강화학습 문제는 보통 MDP로 표현한다.

$$
\mathcal{M}=(\mathcal{S},\mathcal{A},P,R,\gamma)
$$

| 기호 | 의미 |
|---|---|
| $\mathcal{S}$ | state 집합 |
| $\mathcal{A}$ | action 집합 |
| $P(s'\mid s,a)$ | 상태 전이 확률 |
| $R(s,a)$ | reward 함수 |
| $\gamma$ | 미래 보상의 할인율 |

### 비전공자용 설명

게임판의 현재 위치가 state, 내가 누를 수 있는 버튼이 action, 점수가 reward다. agent는 어떤 상황에서 어떤 버튼을 눌러야 장기적으로 점수가 높은지 배운다.

### 보안적 의미

사이버 방어에서는 state가 alert, host 상태, 네트워크 흐름이고 action은 차단, 격리, 탐지 강화, 로그 수집 등이 될 수 있다. reward는 공격 차단, 오탐 비용, 서비스 영향까지 반영해야 한다.

---

### 5.2 Return

Agent는 한 번의 보상만 보지 않고 미래 보상을 할인해 합산한 return을 최대화한다.

$$
G_t=\sum_{k=0}^{\infty}\gamma^k r_{t+k+1}
$$

| 기호 | 의미 |
|---|---|
| $G_t$ | 시점 $t$ 이후 누적 return |
| $r_{t+k+1}$ | 미래 시점의 reward |
| $\gamma$ | 미래 reward를 얼마나 중요하게 볼지 정하는 할인율 |

### 비전공자용 설명

눈앞의 점수만 보는 것이 아니라, 지금 행동이 나중에 가져올 결과까지 계산한다.

### 보안적 의미

당장 의심 트래픽을 모두 차단하면 reward가 높아 보일 수 있지만, 정상 서비스까지 막으면 장기적으로 비용이 커진다. 따라서 reward 설계가 중요하다.

---

### 5.3 State-Value Function과 Action-Value Function

상태 또는 상태-행동의 장기적 가치를 계산한다.

$$
V^{\pi}(s)=\mathbb{E}_{\pi}[G_t\mid S_t=s]
$$

$$
Q^{\pi}(s,a)=\mathbb{E}_{\pi}[G_t\mid S_t=s,A_t=a]
$$

| 기호 | 의미 |
|---|---|
| $V^{\pi}(s)$ | 정책 $\pi$를 따를 때 상태 $s$의 가치 |
| $Q^{\pi}(s,a)$ | 상태 $s$에서 action $a$를 했을 때의 가치 |

### 비전공자용 설명

“지금 이 상황이 얼마나 좋은가?”가 $V$, “지금 이 상황에서 이 행동을 하면 얼마나 좋은가?”가 $Q$다.

### 보안적 의미

보안 자동대응에서는 “현재 경보 상태가 얼마나 위험한가?”와 “격리 조치를 하면 장기적으로 이득인가?”를 구분해 평가할 수 있다.

---

### 5.4 Q-learning Update

Q-learning은 다음 상태의 최대 Q-value를 이용해 현재 Q-value를 갱신한다.

$$
Q(s_t,a_t)\leftarrow Q(s_t,a_t)+\alpha\left[r_{t+1}+\gamma\max_{a'}Q(s_{t+1},a')-Q(s_t,a_t)\right]
$$

| 기호 | 의미 |
|---|---|
| $\alpha$ | 학습률 |
| $r_{t+1}$ | action 이후 받은 reward |
| $\max_{a'}Q(s_{t+1},a')$ | 다음 상태에서 가능한 최고 action value |

### 비전공자용 설명

예상한 점수와 실제로 받은 점수가 다르면, 다음에는 더 정확하게 예측하도록 점수표를 고친다.

### 보안적 의미

방어 action의 효과가 환경에 따라 달라지므로, 보안 agent는 episode log와 reward feedback으로 정책을 갱신한다. 단, 공격자가 reward signal을 왜곡하면 잘못된 정책을 배울 수 있다.

---

### 5.5 Deep Q-Network Objective

DQN은 신경망 $Q_\theta$로 Q-value를 근사한다.

$$
\mathcal{L}(\theta)=\mathbb{E}_{(s,a,r,s')\sim D}\left[\left(r+\gamma\max_{a'}Q_{\theta^-}(s',a')-Q_\theta(s,a)\right)^2\right]
$$

| 기호 | 의미 |
|---|---|
| $D$ | experience replay buffer |
| $Q_\theta$ | 현재 Q-network |
| $Q_{\theta^-}$ | target network |

### 비전공자용 설명

과거 경험을 저장해 두었다가 다시 꺼내 학습하고, 목표 점수표를 따로 두어 학습이 흔들리지 않게 하는 방식이다.

### 보안적 의미

보안 로그와 대응 결과를 replay buffer처럼 사용할 수 있지만, 로그가 오염되면 잘못된 경험을 반복 학습할 수 있다.

---

### 5.6 Policy Objective

Policy gradient는 정책이 만드는 expected return을 직접 최대화한다.

$$
J(\theta)=\mathbb{E}_{\pi_\theta}\left[\sum_t\gamma^t r_t\right]
$$

정책 gradient는 다음처럼 표현할 수 있다.

$$
\nabla_\theta J(\theta)=\mathbb{E}_{\pi_\theta}\left[\nabla_\theta \log \pi_\theta(a_t\mid s_t)G_t\right]
$$

| 기호 | 의미 |
|---|---|
| $\pi_\theta(a\mid s)$ | 상태 $s$에서 행동 $a$를 선택할 확률 |
| $J(\theta)$ | 정책의 기대 return |

### 비전공자용 설명

어떤 행동이 장기적으로 좋은 결과를 냈다면 그 행동을 선택할 확률을 높이고, 나쁜 결과를 냈다면 낮춘다.

---

### 5.7 Actor-Critic 구조

Actor는 action을 선택하고 critic은 value를 추정한다.

$$
\delta_t=r_{t+1}+\gamma V_w(s_{t+1})-V_w(s_t)
$$

$$
\theta\leftarrow\theta+\alpha\delta_t\nabla_\theta\log\pi_\theta(a_t\mid s_t)
$$

| 기호 | 의미 |
|---|---|
| $\delta_t$ | TD error. critic이 계산한 예측 오차 |
| $V_w$ | critic의 value function |
| $\pi_\theta$ | actor의 policy |

### 비전공자용 설명

Actor는 실제로 행동하고, critic은 “그 행동이 기대보다 좋았는지 나빴는지” 평가한다. 평가가 좋으면 그런 행동을 더 자주 하게 된다.

---

### 5.8 사이버보안 적용형 Reward

보안 자동대응에서는 탐지 성공, 차단 성공, 오탐 비용, 대응 비용을 함께 고려해야 한다.

$$
R_{cyber}=w_1\cdot DetectionBenefit-w_2\cdot FalsePositiveCost-w_3\cdot ResponseCost-w_4\cdot ServiceImpact
$$

### 보안적 의미

보안 agent가 무조건 차단만 선택하면 공격은 줄어도 정상 서비스가 망가진다. 따라서 reward는 탐지 성능과 운영 비용을 함께 반영해야 한다.

---

## 6. AI 원리 70% 관점 분석

| 원리 항목 | 설명 | W09/P01에서의 의미 |
|---|---|---|
| MDP | 상태, 행동, 보상, 전이, 할인율로 의사결정 문제 표현 | 사이버 방어 환경 모델링 |
| Return | 장기 보상 합산 | 즉시 차단과 장기 비용 균형 |
| Value Function | 상태 또는 행동의 장기 가치 평가 | 방어 action의 기대효과 계산 |
| Q-learning | 행동가치 함수를 경험으로 갱신 | discrete response action 학습 |
| DQN | Q-value를 deep neural network로 근사 | 고차원 보안 상태 처리 |
| Policy Gradient | 정책을 직접 최적화 | 연속/복합 action 방어 정책 가능 |
| Actor-Critic | 행동 선택과 가치 평가를 결합 | 안정적 학습과 정책 개선 |
| Exploration | 새로운 action을 시도 | 미지 공격 탐색과 운영 위험 균형 |

---

## 7. 보안 이슈 30% 관점 분석

| 보안 항목 | DRL 관점 해석 | 대표 평가 지표 |
|---|---|---|
| 기밀성 | state에 내부 network topology, host status, alert log가 포함될 수 있음 | state exposure risk, log access control |
| 무결성 | state observation, reward, transition log가 조작되면 policy가 오염됨 | reward manipulation rate, poisoned episode rate |
| 가용성 | agent가 과도한 차단·격리를 선택하면 서비스 영향 발생 | service impact, false blocking rate |
| 프라이버시 | user/session 로그 기반 state가 개인정보를 포함할 수 있음 | privacy filtering rate, log minimization |
| 안전성 | 잘못된 자동 대응이 실제 서비스 장애나 방어 실패를 유발 | safety violation rate, false action rate |
| 책임성 | 어떤 state에서 어떤 action을 왜 선택했는지 기록해야 함 | episode trace completeness, policy auditability |

---

## 8. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | cyber environment state, alert, reward function, policy, action log, replay buffer, simulator, episode trace |
| 공격자 목표 | state observation 교란, reward 조작, replay buffer 오염, policy 유도, 방어 action 회피 |
| 공격자 능력 | 관측값 조작, 공격 traffic 패턴 변경, reward signal 간접 조작, false alert 유발, simulator gap 악용 |
| 공격 경로 | environment observation → state encoder → DRL policy → action selection → cyber response → reward/log update |
| 방어자 능력 | state validation, reward audit, safe action constraint, simulator 검증, human approval, runtime monitor |
| 제외 범위 | 실제 네트워크 공격, 실제 자동 차단 실험, 무단 시스템 조작, 공격 절차 제공 |

---

## 9. 평가방법 및 지표

| 평가축 | 지표 | 의미 | W09/P01 활용 |
|---|---|---|---|
| 학습 성능 | cumulative reward, average return | 정책이 장기 보상을 개선하는지 | DRL 기본 성능 |
| 탐지·방어 성능 | detection rate, mitigation success | 공격 탐지와 대응 성공 | P03 사이버보안 연결 |
| 비용 | response cost, service impact, false blocking rate | 자동 대응의 운영 비용 | 실사용성 평가 |
| 안정성 | reward variance, policy stability | episode별 정책 변동성 | 재현성 평가 |
| 안전성 | safety violation rate, unsafe action count | 위험 action 발생 여부 | P05 verification 연결 |
| 강건성 | performance under perturbed states | 관측 교란·환경 변화 대응 | 보안 위협 평가 |
| 설명가능성 | action rationale, state-action trace | 왜 해당 action을 선택했는지 | audit 연결 |
| 재현성 | seed, environment version, reward definition | 실험 재현 가능성 | W15 evidence chain |

---

## 10. 재현성 체크리스트

| 항목 | 기록해야 할 내용 |
|---|---|
| Environment | simulator/cyber range version, state definition, transition rule |
| Action space | 가능한 방어 action, 금지 action, human approval 필요 action |
| Reward function | reward 항목, 가중치, penalty, 변경 이력 |
| Model | DQN/policy gradient/actor-critic variant, network architecture, optimizer |
| Training | seed, episode 수, batch size, replay buffer, exploration schedule |
| Evaluation | cumulative reward, detection rate, cost, safety violation, false action rate |
| Security log | state-action-reward trace, unsafe action case, reward anomaly, policy checkpoint |
| 한계 | toy simulator 결과를 실제 SOC 자동대응 성능으로 과장하지 않음 |

---

## 11. 논문의 고유 기여

1. Deep reinforcement learning의 핵심 알고리즘 계열을 간결하게 정리한다.
2. MDP, return, value function, Q-learning, policy gradient, actor-critic을 하나의 흐름으로 설명한다.
3. Deep neural network가 고차원 state/action 문제에서 value 또는 policy를 근사하는 방식을 보여준다.
4. 사이버보안 자동대응을 state-action-reward 기반 의사결정 문제로 모델링하는 데 필요한 이론 기반을 제공한다.
5. W09 P03~P05의 사이버보안 적용·검증 문헌을 이해하기 위한 공통 수학 언어를 제공한다.

---

## 12. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 직접 사이버보안 문헌은 아님 | DRL 기본 survey이며 cyber-specific threat는 다루지 않는다. | W09 P03/P04와 결합 |
| Sample efficiency 문제 | DRL은 많은 episode와 상호작용이 필요하다. | toy simulator와 문헌 기반 분석으로 제한 |
| Reward 설계 취약성 | 잘못된 reward는 reward hacking과 위험 action을 유도한다. | reward audit과 safety constraint 포함 |
| 재현성 어려움 | seed, 환경, reward, exploration schedule 차이가 결과에 큰 영향을 준다. | config와 episode trace 기록 |
| 안전성 검증 부족 | DRL policy는 예상 밖 행동을 할 수 있다. | W09 P05 verification과 runtime monitor 연결 |
| 실제 운영 전이 문제 | 시뮬레이터에서 잘한 정책이 실제 SOC 환경에서 실패할 수 있다. | simulation-to-real gap 한계 명시 |

---

## 13. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | AI 보안 자동대응은 단발성 분류가 아니라 상태-행동-보상 기반 순차 의사결정 문제라는 문제의식 |
| 2장 관련연구 | DRL 기본 survey, MDP, Q-learning, policy gradient, actor-critic 정리 |
| 3장 위협모형 | state, reward, policy, action log, replay buffer 보호 자산 정의 |
| 4장 연구방법 | cumulative reward, detection rate, response cost, safety violation, policy stability 지표 설계 |
| 5장 분석 | cyber defense MDP와 reward 설계 실패 사례를 toy/synthetic 방식으로 제시 |
| 6장 보안적 함의 | reward hacking, unsafe action, human approval, runtime monitoring 필요성 해석 |

---

## 14. 기말논문 연결 3문장

1. W09에서 기말논문에 반영할 개념: DRL은 보안 자동대응을 state, action, reward, policy로 구성된 순차 의사결정 문제로 모델링할 수 있게 한다.
2. W09에서 기말논문에 반영할 표·그림·실험: MDP 구조도, Q-learning/policy gradient 수식, cyber reward 설계표, state-action-reward trace 예시를 반영한다.
3. W09가 LLM/RAG 보안 감사 프레임워크와 연결되는 지점: RAG/agent 보안 대응도 반복적 action selection 문제로 볼 수 있으므로, reward function, action permission, human approval, episode log를 W14/W15 evidence chain에 포함해야 한다.

---

## 15. 최종 판단

P01은 직접 사이버보안 문헌은 아니지만 W09의 DRL 원리 핵심 문헌이다. P03~P05가 DRL의 사이버보안 적용과 검증을 담당한다면, P01은 MDP, Q-learning, policy gradient, actor-critic이라는 기본 수학 언어를 제공한다. 따라서 W09 기말논문 연결에서는 P01을 **cyber defense MDP와 reward 설계, 자동대응 policy 평가의 이론 배경 문헌**으로 사용하는 것이 적절하다.

---

## 16. 변환 호환성 메모

```bash
pandoc P01_summary.md -o P01_summary.docx
pandoc P01_summary.md -o P01_summary.pdf --pdf-engine=xelatex
```
