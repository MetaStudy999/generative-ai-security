# P02 Summary

## Deep Reinforcement Learning for Autonomous Driving: A Survey — B. Ravi Kiran et al., IEEE TITS, 2022

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W09 심층강화학습(DRL) & 사이버보안 적용·보상조작 |
| 논문명 | Deep Reinforcement Learning for Autonomous Driving: A Survey |
| 저자 | B. Ravi Kiran, Ibrahim Sobh, Victor Talpaert, Patrick Mannion, Ahmad A. Al Sallab, Senthil Yogamani, Patrick Perez |
| 공식 출판 정보 | IEEE Transactions on Intelligent Transportation Systems, Vol. 23, No. 6, pp. 4909–4926, Jun. 2022 |
| DOI | https://doi.org/10.1109/TITS.2021.3054625 |
| 로컬 PDF | `01_papers/pdf/02_Kiran_et_al_2022_DRL_Autonomous_Driving_Survey.pdf` |
| 검증 상태 | W09 `paper_list.md` 기준 공식 DOI 확인. 로컬 PDF는 arXiv v2 기반이며, DOI 등록/early access 시점과 최종 출판연도 차이 및 arXiv v2와 출판판 세부 차이는 최종 제출 전 대조 필요 |
| PDF 확인 메모 | repo의 PDF 폴더에 해당 PDF blob이 존재함을 확인했다. 요약은 로컬 PDF 경로와 W09 `paper_list.md`의 공식 DOI 메타데이터 기준으로 보완했다. |
| 핵심 근거 사용 가능 여부 | 가능. W09에서 DRL의 안전 제약, 시뮬레이션 기반 검증, reward shaping, 실제 환경 전이 문제를 이해하기 위한 응용 배경 문헌으로 사용 |

---

## 1. 한 문장 요약

이 논문은 자율주행 분야에서 deep reinforcement learning을 **perception, decision making, planning, control, reward design, imitation/offline learning, simulation, safety constraint, sample efficiency, sim-to-real transfer** 관점으로 정리하며, W09에서 사이버 방어 DRL agent도 자동 action을 수행하기 전에 안전 제약·검증·운영 비용·human approval을 고려해야 함을 설명하는 응용 기반 문헌이다.

---

## 2. 핵심 연구문제

> 자율주행과 같은 안전 중요 시스템에서 DRL 정책은 상태를 어떻게 관찰하고, 어떤 행동을 선택하며, 어떤 보상과 제약 아래 학습되어야 실제 환경에서 안전하게 동작할 수 있는가?

| 번호 | 연구질문 |
|---|---|
| RQ1 | 자율주행 DRL에서 state, action, reward, policy는 perception, planning, control 단계와 어떻게 연결되는가? |
| RQ2 | Lane keeping, lane change, intersection handling, car following, navigation 같은 task는 어떤 DRL 문제로 모델링되는가? |
| RQ3 | Reward shaping과 safety constraint는 왜 필수이며, 잘못 설계되면 어떤 unsafe behavior를 유도하는가? |
| RQ4 | Simulation 기반 학습과 실제 도로 환경 사이의 sim-to-real gap은 어떻게 줄일 수 있는가? |
| RQ5 | 자율주행 DRL의 안전 제약·scenario evaluation·failure case analysis를 사이버 방어 자동화에 어떻게 전이할 수 있는가? |

---

## 3. 논문의 핵심 기여

| 기여 | 설명 | W09 연결 |
|---|---|---|
| 자율주행 DRL taxonomy | perception, planning, decision making, control, end-to-end driving 등 자율주행 task별 DRL 적용을 정리 | DRL 응용 설계 사례 제공 |
| State/action/reward 설계 논의 | 센서 입력, 주행 상태, 조향·가속·제동 action, 안전·효율 reward를 정리 | cyber defense state/action/reward 설계 참고 |
| 안전 제약 강조 | collision, lane departure, comfort, traffic rule violation 등 safety constraint를 고려 | 보안 자동대응의 unsafe action 제약과 연결 |
| Simulation 기반 평가 정리 | CARLA, TORCS, SUMO, Gazebo 등 simulation 환경과 scenario evaluation 필요성 제시 | cyber range/simulator 기반 보안 평가 연결 |
| 한계와 미래 과제 제시 | sample efficiency, explainability, generalization, sim-to-real, safety assurance 문제를 제시 | W09 P05 DRL verification과 직접 연결 |

---

## 4. 목차별 핵심 개괄

| 목차 | 핵심 내용 | 비전공자용 이해 |
|---|---|---|
| 1. Introduction | DRL은 자율주행처럼 복잡하고 순차적인 의사결정 문제에 적용 가능하지만, 안전성과 실제 환경 전이가 큰 과제다. | 자율주행차가 운전 게임처럼 연습하면서 배우지만, 실제 도로에서는 실수 비용이 매우 크다. |
| 2. Background on Autonomous Driving | 자율주행 시스템은 perception, localization, prediction, planning, control 등 여러 모듈로 구성된다. | 차가 주변을 보고, 자기 위치를 알고, 다른 차 움직임을 예측하고, 어떻게 움직일지 결정한다. |
| 3. Reinforcement Learning Basics | MDP, state, action, reward, policy, value function 등 RL 기본 개념을 자율주행 task에 연결한다. | 현재 도로 상황을 보고 조향·가속·제동을 선택하고, 그 결과로 점수를 받으며 배운다. |
| 4. DRL Algorithms for Driving | DQN, DDPG, A3C, PPO, actor-critic, policy gradient 등 value-based/policy-based 방법을 자율주행에 적용한 연구를 정리한다. | 상황이 복잡하므로 단순 규칙 대신 신경망이 행동 정책을 학습한다. |
| 5. DRL for Decision Making | 차선 변경, 교차로 통과, 추월, 합류, 경로 선택 등 decision-level task를 DRL로 모델링한다. | “지금 차선을 바꿀지, 기다릴지, 속도를 줄일지”를 학습하는 부분이다. |
| 6. DRL for Control | 조향각, 가속, 브레이크 등 low-level continuous control 문제를 다룬다. | 결정이 끝난 뒤 실제로 핸들과 페달을 어떻게 조작할지 배우는 단계다. |
| 7. End-to-End Driving | 카메라·라이다 등 raw sensor input에서 바로 action을 출력하는 end-to-end policy를 다룬다. | 사람처럼 화면을 보고 바로 운전 행동을 내는 AI에 가깝다. |
| 8. Simulation and Training Environments | 실제 도로 실험의 위험과 비용 때문에 simulation, scenario, domain randomization이 중요하다. | 실제 차로 위험하게 실험하지 않고 가상 도로에서 다양한 상황을 반복 연습한다. |
| 9. Challenges and Future Directions | sample efficiency, safety, explainability, robustness, sim-to-real transfer, verification 문제가 남아 있다. | 자율주행 AI가 잘 운전해도 왜 그렇게 했는지, 예외 상황에서도 안전한지 검증해야 한다. |
| 10. Conclusion | DRL은 자율주행에 유망하지만 실제 배포에는 안전 제약, 시뮬레이션 검증, 설명가능성, 재현성이 필수다. | DRL은 강력하지만 안전 중요한 분야에서는 자동 실행 전에 검증과 제한이 필요하다. |

---

## 5. 핵심 이론 및 수식

> 아래 수식은 자율주행 DRL과 W09 사이버보안 적용을 설명하기 위한 표준화된 표현이다. 수식은 GitHub, MS Word, PDF 변환 호환성을 위해 Markdown 표 밖의 LaTeX block math로 작성한다.

### 5.1 Autonomous Driving MDP

자율주행 DRL은 차량과 도로 환경의 순차 의사결정 문제로 표현할 수 있다.

$$
\mathcal{M}_{drive}=(\mathcal{S},\mathcal{A},P,R,\gamma)
$$

| 기호 | 의미 |
|---|---|
| $\mathcal{S}$ | 차량 위치, 속도, 주변 차량, 차선, 신호, 센서 정보 등 상태 공간 |
| $\mathcal{A}$ | 조향, 가속, 감속, 차선 변경, 정지 등 행동 공간 |
| $P$ | 행동 후 다음 주행 상태로 전이될 확률 |
| $R$ | 안전·효율·안락함·규칙 준수를 반영하는 보상 |
| $\gamma$ | 미래 보상의 할인율 |

### 비전공자용 설명

자동차 게임에서 현재 화면이 state, 핸들·가속·브레이크가 action, 사고 없이 목적지에 가까워지면 reward를 받는다고 보면 된다.

### 보안적 의미

사이버 방어에서도 현재 alert와 네트워크 상태가 state, 차단·격리·탐지 강화가 action, 공격 차단과 서비스 영향이 reward가 될 수 있다.

---

### 5.2 Constrained Return

안전 중요 시스템에서는 reward만 최대화하면 안 되고, 위험 비용이 허용 범위를 넘지 않아야 한다.

$$
J(\pi)=\mathbb{E}_{\pi}\left[\sum_{t=0}^{T}\gamma^t r_t\right], \qquad C(\pi)\leq c_{max}
$$

| 기호 | 의미 |
|---|---|
| $J(\pi)$ | 정책 $\pi$의 기대 누적 보상 |
| $C(\pi)$ | collision, rule violation, service impact 같은 누적 위험 비용 |
| $c_{max}$ | 허용 가능한 최대 위험 |

### 비전공자용 설명

목적지에 빨리 도착하는 것만 목표로 하면 위험하다. “빨리 가되 사고를 내면 안 된다”는 제약이 필요하다.

### 보안적 의미

보안 agent도 공격을 빨리 막는 것만 보면 정상 사용자를 차단할 수 있다. false blocking, service outage, excessive quarantine을 제약으로 둬야 한다.

---

### 5.3 Reward Shaping

자율주행 reward는 여러 목표를 합친 형태가 될 수 있다.

$$
R_{drive}=w_1 Progress-w_2 Collision-w_3 LaneViolation-w_4 Discomfort-w_5 RuleViolation
$$

| 항목 | 의미 |
|---|---|
| Progress | 목적지 또는 목표 경로로의 진행 |
| Collision | 충돌 penalty |
| LaneViolation | 차선 이탈 penalty |
| Discomfort | 급가속·급감속·급조향 penalty |
| RuleViolation | 신호·속도·교통규칙 위반 penalty |

### 비전공자용 설명

좋은 운전은 빠르기만 해서는 안 된다. 안전하고, 차선을 지키고, 승차감도 좋아야 한다.

### 보안적 의미

사이버 방어 reward도 공격 차단만이 아니라 정상 서비스 영향, 오탐, 대응 비용, 사용자 피해를 포함해야 한다.

---

### 5.4 Safety Violation Rate

안전 위반 발생 비율을 별도 지표로 기록한다.

$$
SafetyViolationRate=\frac{N_{unsafe\ episodes}}{N_{total\ episodes}}
$$

| 기호 | 의미 |
|---|---|
| $N_{unsafe\ episodes}$ | 충돌, 차선 이탈, 위험 action이 발생한 episode 수 |
| $N_{total\ episodes}$ | 전체 평가 episode 수 |

### 보안적 의미

평균 reward가 높아도 일부 episode에서 치명적 사고가 발생하면 배포하기 어렵다. 보안 자동화도 unsafe action rate를 별도로 봐야 한다.

---

### 5.5 Simulation-to-Real Gap

시뮬레이터와 실제 환경의 성능 차이를 측정한다.

$$
Sim2RealGap=Metric_{simulation}-Metric_{real}
$$

| 기호 | 의미 |
|---|---|
| $Metric_{simulation}$ | 시뮬레이션 환경 성능 |
| $Metric_{real}$ | 실제 또는 더 현실적인 검증 환경 성능 |

### 비전공자용 설명

운전 게임에서 잘한다고 실제 도로에서 바로 잘 운전한다는 뜻은 아니다. 게임과 현실은 다르기 때문이다.

### 보안적 의미

cyber range에서 잘 작동한 자동 방어 정책이 실제 SOC 환경에서 실패할 수 있다. simulator version, scenario diversity, real log validation이 필요하다.

---

### 5.6 Policy Robustness under Perturbation

센서 노이즈나 공격성 교란에 대해 정책 성능이 얼마나 유지되는지 측정한다.

$$
RobustnessDrop=J_{clean}(\pi)-J_{perturbed}(\pi)
$$

| 기호 | 의미 |
|---|---|
| $J_{clean}$ | 정상 관측 상태에서의 return |
| $J_{perturbed}$ | 교란된 관측 상태에서의 return |

### 보안적 의미

자율주행에서는 센서 노이즈나 adversarial sign이 문제이고, 사이버보안에서는 false alert, missing log, observation poisoning이 같은 역할을 한다.

---

### 5.7 Human Approval Constraint

안전 중요한 action은 자동 실행보다 승인 기반으로 제한할 수 있다.

$$
a_t \in \mathcal{A}_{auto} \cup \mathcal{A}_{approval}, \qquad a_t\in\mathcal{A}_{approval}\Rightarrow HumanReview(a_t)=1
$$

### 보안적 의미

자율주행에서 위험한 조작은 safety layer가 제한하듯, 보안 자동대응에서도 서버 격리·계정 잠금·대규모 차단은 human approval이 필요하다.

---

## 6. AI 원리 70% 관점 분석

| 원리 항목 | 설명 | W09/P02에서의 의미 |
|---|---|---|
| DRL for control | 복잡한 연속 action을 학습 | 조향·가속·제동과 보안 대응 action 비교 |
| DRL for decision making | 고수준 운전 결정을 학습 | 차선 변경과 차단/격리 결정의 유사성 |
| Reward shaping | 여러 목표와 penalty를 reward로 결합 | 탐지 성공·오탐·서비스 영향 균형 |
| Safety constraint | 위험 action을 제한 | 보안 자동대응의 금지 action 정의 |
| Simulation training | 실제 위험을 줄이기 위해 가상환경에서 학습 | cyber range 기반 실험과 연결 |
| Sim-to-real transfer | simulation 정책을 실제 환경으로 전이 | toy 실험의 일반화 한계 설명 |
| Robustness | 센서 노이즈·환경 변화에 대응 | 관측 교란·로그 누락에 대한 방어 정책 평가 |
| Human-in-the-loop | 고위험 상황에서 사람 승인 필요 | 자동 대응 배포 전 승인 정책 연결 |

---

## 7. 보안 이슈 30% 관점 분석

| 보안 항목 | 자율주행 DRL 관점 해석 | W09 사이버보안 전이 |
|---|---|---|
| 기밀성 | 센서·위치·주행 로그가 민감정보가 될 수 있음 | 네트워크 상태·사용자 로그 접근통제 필요 |
| 무결성 | 센서 관측이 교란되면 정책이 잘못된 action을 선택 | alert/log/state poisoning 위험 |
| 가용성 | 잘못된 자동 action이 차량 운행 또는 서비스 운영을 방해 | 과잉 차단·서비스 중단 위험 |
| 안전성 | 충돌·차선 이탈·교통법규 위반은 치명적 피해 | 위험 대응 action과 false blocking 제한 |
| 책임성 | 어떤 state에서 왜 action을 선택했는지 추적 필요 | state-action-reward trace와 audit log 필요 |
| 강건성 | 날씨·조명·센서 노이즈에 정책이 흔들릴 수 있음 | 공격 패턴 변화·로그 누락·노이즈 상황 평가 필요 |

---

## 8. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | safety policy, sensor/state observation, learned policy, reward function, simulator, scenario seed, action log, failure case |
| 공격자 목표 | state observation 교란, 위험 action 유도, reward hacking, simulation gap 악용, 안전 제약 우회 |
| 공격자 능력 | 센서/상태 노이즈 유발, scenario 편향, false signal 삽입, reward proxy 악용, environment assumption 공격 |
| 공격 경로 | sensor/environment observation → state encoder → DRL policy → action selection → safety layer/human approval → environment response |
| 방어자 능력 | state validation, safety constraint, simulation scenario diversity, robustness test, human approval, runtime monitoring |
| 제외 범위 | 실제 자율주행 차량 조작, 실제 도로 실험, 실제 사이버 시스템 자동 차단, 공격 절차 제공 |

---

## 9. 평가방법 및 지표

| 평가축 | 지표 | 의미 | W09/P02 활용 |
|---|---|---|---|
| 기본 성능 | cumulative reward, task success rate | 목표 수행 능력 | DRL 응용 성능 |
| 안전성 | safety violation rate, collision/unsafe action count | 위험 action 발생 여부 | 안전 제약 평가 |
| 비용 | response cost, discomfort/service impact | action의 부작용 | 보안 대응 비용 전이 |
| 강건성 | RobustnessDrop, perturbed-state return | 교란 상황 성능 유지 | observation poisoning 평가 |
| 전이성 | Sim2RealGap, scenario generalization | 시뮬레이션과 실제 차이 | cyber range 일반화 한계 |
| 지연 | response latency, decision time | 실시간 의사결정 가능성 | SOC/agent 운영 연결 |
| 설명가능성 | action rationale, failure case explanation | action 이유 추적 | 책임성·감사 연결 |
| 재현성 | simulator version, seed, reward function | 실험 반복 가능성 | W15 evidence chain |

---

## 10. 재현성 체크리스트

| 항목 | 기록해야 할 내용 |
|---|---|
| Simulator | CARLA/TORCS/SUMO/Gazebo 등 환경명, version, scenario, map |
| State definition | sensor input, processed state, observation noise, normalization |
| Action space | discrete/continuous action, safety-filtered action, approval-required action |
| Reward/cost | reward 항목, penalty, safety constraint, 가중치 |
| DRL model | DQN/DDPG/PPO/A3C/actor-critic 등 알고리즘, network architecture |
| Training | seed, episode 수, replay buffer, exploration schedule, hyperparameter |
| Evaluation | task success, violation rate, robustness, latency, failure case |
| Transfer | simulation-only 결과인지, real-world 또는 realistic scenario 검증인지 명시 |
| Security log | state-action-reward trace, unsafe action, approval decision, rollback event |
| 한계 | 자율주행 simulation 결과를 실제 도로 또는 실제 사이버 방어 성능으로 과장하지 않음 |

---

## 11. 논문의 고유 기여

1. 자율주행이라는 안전 중요 응용에서 DRL 연구를 체계적으로 분류한다.
2. DRL의 state, action, reward 설계가 실제 시스템 안전성과 직결됨을 보여준다.
3. Safety constraint, reward shaping, simulation, sample efficiency, sim-to-real gap 문제를 강조한다.
4. W09에서 사이버 방어 agent도 자동 action 실행 전 safety layer와 human approval이 필요하다는 논리적 근거를 제공한다.
5. W09 P03~P05의 사이버보안 DRL 적용·검증 문헌과 연결되는 안전 제약형 DRL 응용 사례로 활용 가능하다.

---

## 12. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 직접 사이버보안 문헌은 아님 | 자율주행 DRL survey이며 cyber defense 자체가 주제는 아니다. | P03/P04와 결합해 cyber defense로 전이 |
| 실세계 검증 어려움 | 실제 도로 환경 검증은 비용과 위험이 크다. | cyber range/synthetic simulator 한계를 명시 |
| Reward misspecification | 잘못된 reward는 위험하거나 비윤리적인 정책을 만들 수 있다. | reward audit, safety constraint, human approval 포함 |
| Sim-to-real gap | simulation에서 좋은 정책이 실제 환경에서 실패할 수 있다. | scenario diversity와 robustness test 포함 |
| 설명가능성 부족 | DRL action의 이유를 해석하기 어렵다. | state-action trace와 failure case 분석 포함 |
| 안전성 보증 부족 | 평균 성능만으로 안전한 정책을 보장할 수 없다. | safety violation rate와 worst-case analysis 병기 |

---

## 13. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | 보안 자동대응도 자율주행처럼 안전 중요한 순차 의사결정 문제라는 문제의식 |
| 2장 관련연구 | 자율주행 DRL survey를 안전 제약 DRL 응용 문헌으로 정리 |
| 3장 위협모형 | state observation, reward, policy, action, safety layer 보호 자산 정의 |
| 4장 연구방법 | constrained return, safety violation rate, Sim2RealGap, RobustnessDrop 지표 설계 |
| 5장 분석 | cyber defense action에 대한 safety constraint와 human approval 적용표 제시 |
| 6장 보안적 함의 | reward hacking, unsafe action, 과잉차단, runtime monitoring, human-in-the-loop 필요성 해석 |

---

## 14. 기말논문 연결 3문장

1. W09에서 기말논문에 반영할 개념: 자율주행 DRL은 안전 중요한 환경에서 state-action-reward 설계와 safety constraint가 얼마나 중요한지 보여주며, 이 원칙은 사이버 방어 자동대응에도 그대로 적용된다.
2. W09에서 기말논문에 반영할 표·그림·실험: constrained return 수식, reward shaping 표, safety violation rate, Sim2RealGap, human approval action 분류표를 반영한다.
3. W09가 LLM/RAG 보안 감사 프레임워크와 연결되는 지점: RAG/agent 보안 대응을 DRL로 자동화하려면 action permission, response cost, false blocking, human approval, state-action-reward trace를 W14/W15 evidence chain에 포함해야 한다.

---

## 15. 최종 판단

P02는 직접 사이버보안 문헌은 아니지만 W09의 안전 제약형 DRL 응용 사례로 중요하다. 자율주행에서 요구되는 safety constraint, reward shaping, simulation-based evaluation, sim-to-real gap, human oversight는 사이버 방어 자동화에도 그대로 전이된다. 따라서 W09 기말논문 연결에서는 P02를 **안전 중요 DRL 시스템의 reward·constraint·simulation 검증 원칙을 제공하는 보조 핵심 문헌**으로 사용하는 것이 적절하다.

---

## 16. 변환 호환성 메모

```bash
pandoc P02_summary.md -o P02_summary.docx
pandoc P02_summary.md -o P02_summary.pdf --pdf-engine=xelatex
```
