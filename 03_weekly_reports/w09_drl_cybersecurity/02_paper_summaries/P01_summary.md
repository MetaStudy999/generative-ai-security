# P01 Summary

## Deep Reinforcement Learning: A Brief Survey — Kai Arulkumaran et al., IEEE Signal Processing Magazine, 2017

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W09 DRL & Cybersecurity |
| 논문명 | Deep Reinforcement Learning: A Brief Survey |
| 저자 | Kai Arulkumaran et al. |
| 출판 정보 | IEEE Signal Processing Magazine, 34(6), pp. 26–38, 2017 |
| DOI | https://doi.org/10.1109/MSP.2017.2743240 |
| 검증 상태 | W09 `paper_list.md` 기준 공식 DOI 확인. 로컬 PDF는 arXiv extended version이므로 판본 차이 메모 유지 |

---

## 1. 한 문장 요약

이 논문은 deep reinforcement learning을 **state, action, reward, policy, value function, Q-learning, policy gradient, actor-critic, exploration** 관점에서 정리하며, W09에서 사이버 방어 자동화를 순차 의사결정 문제로 모델링하는 핵심 AI 원리 배경을 제공한다.

---

## 2. 핵심 연구질문

| 번호 | 연구질문 |
|---|---|
| RQ1 | DRL은 MDP 기반 순차 의사결정을 어떻게 신경망으로 확장하는가? |
| RQ2 | Value-based, policy-based, actor-critic 방법은 어떤 차이가 있는가? |
| RQ3 | Exploration과 exploitation trade-off는 사이버 방어 정책 학습에 어떤 의미를 갖는가? |
| RQ4 | 보안 환경에서 reward 설계 오류는 어떤 위험을 만드는가? |

---

## 3. 핵심 수식

### 3.1 MDP와 Return

$$
G_t=\sum_{k=0}^{\infty}\gamma^k r_{t+k+1}
$$

### 3.2 Q-learning Update

$$
Q(s_t,a_t)\leftarrow Q(s_t,a_t)+\alpha\left[r_{t+1}+\gamma\max_{a'}Q(s_{t+1},a')-Q(s_t,a_t)\right]
$$

### 3.3 Policy Objective

$$
J(\theta)=\mathbb{E}_{\pi_\theta}\left[\sum_t \gamma^t r_t\right]
$$

**보안 해석:** 사이버 방어 reward를 잘못 설계하면 에이전트가 실제 안전이 아니라 점수만 최대화하는 정책을 학습할 수 있다.

---

## 4. 위협모형·평가지표

| 항목 | 내용 |
|---|---|
| 보호 자산 | 네트워크 상태, alert, 방어 정책, 대응 action, reward log |
| 공격자 목표 | 상태 관찰 교란, reward 조작, 방어 정책 우회 |
| 대표 지표 | cumulative reward, detection rate, response cost, false action rate, policy stability |
| 재현성 | environment seed, reward function, state/action definition, episode log 기록 |

---

## 5. 기말논문 연결

P01은 W09의 DRL 이론 배경이다. 기말논문에서는 RAG/LLM 보안 자동대응을 상태-행동-보상 기반 의사결정 문제로 모델링할 때 기본 수식과 한계로 사용한다.

---

## 6. 최종 판단

P01은 직접 사이버보안 문헌은 아니지만 W09의 DRL 원리 핵심 문헌이다. 보안 적용과 검증은 P03~P05와 결합한다.
