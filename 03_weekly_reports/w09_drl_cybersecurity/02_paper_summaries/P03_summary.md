# P03 Summary

## Deep Reinforcement Learning for Cyber Security — Thanh Thi Nguyen, Vijay Janapa Reddi, IEEE TNNLS, 2023

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W09 심층강화학습(DRL) & 사이버보안 적용·보상조작 |
| 논문명 | Deep Reinforcement Learning for Cyber Security |
| 저자 | Thanh Thi Nguyen, Vijay Janapa Reddi |
| 공식 출판 정보 | IEEE Transactions on Neural Networks and Learning Systems, Vol. 34, No. 8, pp. 3779–3795, Aug. 2023 |
| DOI | https://doi.org/10.1109/TNNLS.2021.3121870 |
| 로컬 PDF | `01_papers/pdf/03_Nguyen_Reddi_2023_DRL_for_Cyber_Security.pdf` |
| 검증 상태 | W09 `paper_list.md` 기준 공식 DOI 확인. 강의계획서의 `Ngoc-Tinh Nguyen et al.` 표기와 공식 DOI 기준 저자명 차이 메모 유지 |
| PDF 확인 메모 | repo의 PDF 폴더에 해당 PDF blob이 존재함을 확인했다. 요약은 로컬 PDF 경로와 W09 `paper_list.md`의 공식 DOI 메타데이터 기준으로 보완했다. |
| 핵심 근거 사용 가능 여부 | 가능. W09에서 DRL을 사이버보안 문제에 직접 적용하는 중심 문헌으로 사용 |

---

## 1. 한 문장 요약

이 논문은 deep reinforcement learning을 **intrusion detection, malware analysis, cyber-physical system security, network defense, moving target defense, autonomous response, resource allocation, adversarial environment** 관점에서 사이버보안 문제에 적용하는 연구를 정리하며, W09에서 보안 대응을 단발성 분류가 아니라 **state-action-reward 기반 순차 의사결정과 감사 가능한 자동대응 정책 평가 문제**로 확장하는 핵심 문헌이다.

---

## 2. 핵심 연구문제

> 사이버보안 문제를 DRL의 state, action, reward, policy, environment로 어떻게 모델링할 수 있으며, 자동 방어 정책은 탐지율·오탐·대응비용·서비스 영향·안전성을 함께 고려해 어떻게 평가되어야 하는가?

| 번호 | 연구질문 |
|---|---|
| RQ1 | 침입탐지, 악성코드 분석, 네트워크 방어, CPS 보안, 자원 할당 문제는 어떤 state/action/reward 구조로 DRL에 매핑되는가? |
| RQ2 | DRL 기반 자동 방어 정책은 탐지율, 오탐률, 대응 비용, 서비스 영향, 지연시간을 어떻게 함께 고려해야 하는가? |
| RQ3 | 공격자가 상태 관측, reward signal, traffic pattern, 환경 전이를 조작할 때 DRL policy는 어떤 취약성을 갖는가? |
| RQ4 | 사이버보안 DRL 연구에서 simulation, cyber range, synthetic toy environment, benchmark는 어떤 한계와 재현성 문제를 갖는가? |
| RQ5 | 실제 운영 환경에 DRL 방어 정책을 적용하기 전에 human-in-the-loop, runtime monitoring, safe action constraint를 어떻게 설계해야 하는가? |

---

## 3. 논문의 핵심 기여

| 기여 | 설명 | W09 연결 |
|---|---|---|
| Cybersecurity DRL taxonomy | DRL의 사이버보안 적용 영역을 침입탐지, 방어, CPS, 네트워크 관리, 자동대응 등으로 정리 | W09의 직접 보안 핵심 |
| State/action/reward 모델링 관점 | 보안 문제를 MDP와 sequential decision-making으로 표현하는 틀 제공 | cyber defense MDP 설계 |
| DRL 알고리즘 적용 비교 | DQN, policy gradient, actor-critic 등 DRL 계열의 보안 적용 사례 정리 | P01 기본 이론과 연결 |
| 보안 평가 지표 확장 | 탐지율만이 아니라 오탐, 대응 비용, latency, policy robustness를 고려해야 함을 제시 | W09 평가방법 설계 |
| 한계와 미래 과제 제시 | 실제 환경 전이, 안전성, explainability, scalability, adversarial robustness, reproducibility 문제 제시 | W09 P05 verification 및 W14/W15 연결 |

---

## 4. 목차별 핵심 개괄

| 목차 | 핵심 내용 | 비전공자용 이해 |
|---|---|---|
| 1. Introduction | 사이버공격은 동적이고 적응적으로 변하기 때문에, 고정 규칙이나 단발성 분류만으로는 한계가 있다. DRL은 보안 방어를 순차 의사결정 문제로 모델링할 수 있다. | 보안은 한 번 맞히고 끝나는 문제가 아니라, 공격자의 움직임을 보며 계속 대응하는 게임에 가깝다. |
| 2. DRL Background | MDP, agent, environment, state, action, reward, policy, value function, DQN, policy gradient, actor-critic 기본 개념을 설명한다. | AI 보안 agent가 현재 상황을 보고 행동을 고른 뒤, 결과 점수를 받아 다음에는 더 나은 행동을 배운다. |
| 3. DRL for Cyber Security Applications | 침입탐지, malware detection, network security, cyber-physical system defense, access/resource management 등 적용 사례를 정리한다. | 보안 분야에서 DRL은 탐지뿐 아니라 차단, 격리, 자원 배분, 방어 정책 선택에도 쓰일 수 있다. |
| 4. DRL-based Intrusion Detection and Response | 네트워크 상태, alert, traffic feature를 state로 보고 탐지·대응 action을 선택하는 구조를 설명한다. | 보안관제 시스템이 경보를 보고 어떤 대응을 할지 학습하는 방식이다. |
| 5. DRL for Cyber-Physical and IoT Security | 센서, 제어기, IoT 장치처럼 물리 시스템과 연결된 환경에서 DRL 보안 적용을 다룬다. | 스마트팩토리나 드론·로봇처럼 실제 장비가 연결된 환경에서는 잘못된 대응이 물리적 피해로 이어질 수 있다. |
| 6. Challenges | reward 설계, sample efficiency, environment realism, adversarial manipulation, 안전성, 설명가능성, 재현성 문제가 남아 있다. | 보안 agent가 높은 점수만 좇으면 과잉 차단, 정상 사용자 피해, 잘못된 자동 대응이 생길 수 있다. |
| 7. Future Directions | 안전한 DRL, robust policy, interpretable policy, realistic simulator, human-in-the-loop, benchmark 정립이 필요하다. | 실제 보안 현장에 넣으려면 사람이 검토하고, 위험 action을 제한하고, 로그를 남겨야 한다. |
| 8. Conclusion | DRL은 사이버보안 자동화에 유망하지만 실제 시스템에는 제한적·검증된 방식으로 적용해야 한다. | 보안 자동화의 핵심은 “자동으로 잘 막기”보다 “안전하게, 설명 가능하게, 재현 가능하게 막기”다. |

---

## 5. 핵심 이론 및 수식

> 아래 수식은 DRL 기반 사이버보안 모델링과 W09 보안 평가를 설명하기 위한 표준화된 표현이다. 실제 공격 절차가 아니라 안전한 simulation/toy evaluation과 문헌 기반 분석을 전제로 한다.

### 5.1 Cyber Defense MDP

사이버 방어 문제는 MDP로 표현할 수 있다.

$$
\mathcal{M}_{cyber}=(\mathcal{S},\mathcal{A},P,R,\gamma)
$$

| 기호 | 의미 |
|---|---|
| $\mathcal{S}$ | 네트워크 상태, host 상태, alert, traffic feature, 취약점 상태 |
| $\mathcal{A}$ | monitor, alert, block, isolate, patch, scan, escalate 등 방어 행동 |
| $P$ | action 이후 보안 환경이 변화하는 전이 확률 |
| $R$ | 공격 차단, 오탐 비용, 대응 비용, 서비스 영향 등을 반영한 reward |
| $\gamma$ | 미래 보상 할인율 |

### 비전공자용 설명

보안 agent가 현재 네트워크 상황을 보고 “감시할지, 차단할지, 격리할지, 사람에게 넘길지”를 선택하고, 그 결과가 좋았는지 점수를 받아 학습하는 구조다.

### 보안적 의미

상태와 행동을 어떻게 정의하느냐가 성능보다 중요하다. 위험 action을 자동 실행하게 만들면 실제 서비스 장애나 정상 사용자 차단으로 이어질 수 있다.

---

### 5.2 Cyber Defense Reward

보안 reward는 탐지 성공뿐 아니라 오탐, 대응 비용, 서비스 영향을 함께 반영해야 한다.

$$
r_t=\alpha\cdot Detection_t-\beta\cdot FalseAlarm_t-\lambda\cdot ResponseCost_t-\mu\cdot ServiceImpact_t
$$

| 항목 | 의미 |
|---|---|
| $Detection_t$ | 공격 탐지 또는 완화 성공 보상 |
| $FalseAlarm_t$ | 정상 행위를 공격으로 오탐한 비용 |
| $ResponseCost_t$ | 차단·격리·스캔·패치 같은 대응 비용 |
| $ServiceImpact_t$ | 정상 서비스 중단 또는 사용자 피해 비용 |

### 비전공자용 설명

공격을 막는 것만 점수로 주면 agent는 모든 것을 차단하려 할 수 있다. 따라서 정상 사용자를 막은 비용과 서비스 중단 비용을 penalty로 넣어야 한다.

---

### 5.3 Defense Policy Objective

DRL agent는 장기 기대 reward를 최대화하는 정책을 학습한다.

$$
\pi^*=\arg\max_{\pi}\mathbb{E}_{\pi}\left[\sum_{t=0}^{T}\gamma^t r_t\right]
$$

### 보안적 의미

정책이 장기 보상을 최대화한다는 것은 장기적으로 안전하고 비용 효율적인 방어를 목표로 한다는 뜻이다. 하지만 reward가 부정확하면 정책도 잘못된다.

---

### 5.4 Detection and False Positive Trade-off

탐지율과 오탐률은 함께 봐야 한다.

$$
DefenseScore=w_1\cdot TPR-w_2\cdot FPR-w_3\cdot Cost
$$

| 기호 | 의미 |
|---|---|
| $TPR$ | 실제 공격을 탐지한 비율 |
| $FPR$ | 정상 행위를 공격으로 오탐한 비율 |
| $Cost$ | 대응 비용 또는 운영 비용 |

### 비전공자용 설명

공격을 많이 잡아도 정상 사용자를 많이 막으면 좋은 보안 시스템이라고 보기 어렵다.

---

### 5.5 Policy Robustness under Perturbed State

관측 상태가 오염되거나 누락될 때 정책 성능이 얼마나 유지되는지 평가한다.

$$
RobustnessDrop=J_{clean}(\pi)-J_{perturbed}(\pi)
$$

| 기호 | 의미 |
|---|---|
| $J_{clean}$ | 정상 상태 관측에서의 기대 return |
| $J_{perturbed}$ | 교란·누락·오염된 상태 관측에서의 기대 return |

### 보안적 의미

공격자가 로그 일부를 숨기거나 false alert를 만들면 agent가 잘못된 action을 선택할 수 있다. 따라서 관측 교란 조건에서 policy robustness를 측정해야 한다.

---

### 5.6 Reward Manipulation Risk

Reward signal이 공격자나 환경 오류에 의해 왜곡되면 정책이 잘못 학습된다.

$$
RewardError=|R_{true}(s,a)-R_{observed}(s,a)|
$$

$$
RewardManipulationRate=\frac{N_{manipulated\ reward\ episodes}}{N_{total\ episodes}}
$$

### 보안적 의미

보상 로그가 잘못되면 agent는 실제 안전과 다른 방향으로 학습한다. W09에서는 reward function과 reward log를 감사 대상으로 둔다.

---

### 5.7 Human-in-the-loop Safe Action Constraint

고위험 방어 action은 자동 실행하지 않고 사람 승인 또는 safety layer를 요구할 수 있다.

$$
a_t\in\mathcal{A}_{safe}\cup\mathcal{A}_{approval},\qquad a_t\in\mathcal{A}_{approval}\Rightarrow Review(a_t)=1
$$

| 기호 | 의미 |
|---|---|
| $\mathcal{A}_{safe}$ | 자동 실행 가능한 저위험 action |
| $\mathcal{A}_{approval}$ | 사람 승인 또는 추가 검증이 필요한 고위험 action |

### 보안적 의미

계정 잠금, 서버 격리, 대규모 차단, 정책 변경 같은 action은 자동으로 실행하지 않고 승인 기반으로 제한해야 한다.

---

## 6. AI 원리 70% 관점 분석

| 원리 항목 | 설명 | W09/P03에서의 의미 |
|---|---|---|
| MDP | 사이버 방어를 state-action-reward로 모델링 | 자동대응 구조의 기본 틀 |
| DRL policy | 복잡한 상태에서 방어 action 선택 | alert와 네트워크 상태 기반 대응 |
| Value learning | action의 장기 효과 평가 | 즉시 차단과 장기 서비스 비용 균형 |
| Exploration | 새로운 방어 action이나 탐지 전략 시도 | 미지 공격 대응 가능성과 운영 위험 |
| Reward shaping | 탐지·오탐·비용·서비스 영향을 reward로 결합 | reward hacking 방지 |
| Simulation | 실제 네트워크 대신 안전한 환경에서 학습·평가 | cyber range와 toy evaluation 필요 |
| Robustness | 관측 교란과 환경 변화에서 정책 유지 | adversarial cyber environment 평가 |
| Human-in-the-loop | 고위험 action에 사람 승인 결합 | 실제 배포 안전성 확보 |

---

## 7. 보안 이슈 30% 관점 분석

| 보안 항목 | DRL Cybersecurity 관점 해석 | 대표 평가 지표 |
|---|---|---|
| 기밀성 | 네트워크 상태, 로그, alert, 사용자 행위 데이터가 민감정보가 될 수 있음 | state exposure risk, log access control |
| 무결성 | 상태 관측, reward, replay buffer, policy checkpoint가 오염될 수 있음 | poisoned episode rate, reward manipulation rate |
| 가용성 | 과도한 자동 차단·격리 action이 정상 서비스를 중단시킬 수 있음 | service impact, false blocking rate |
| 프라이버시 | 사용자·세션·네트워크 로그 기반 state가 개인정보를 포함할 수 있음 | log minimization, privacy filtering rate |
| 안전성 | 잘못된 자동 대응이 방어 실패 또는 운영 장애를 유발할 수 있음 | safety violation rate, unsafe action count |
| 책임성 | state-action-reward trace가 없으면 자동 action을 설명·감사할 수 없음 | episode trace completeness, policy auditability |

---

## 8. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | network state, IDS alert, host status, reward function, policy, action permission, replay buffer, simulator, episode log |
| 공격자 목표 | 탐지 회피, state observation 교란, false alert 유발, reward 조작, policy 유도, 방어 action 회피 |
| 공격자 능력 | traffic pattern 변경, 관측값 누락·오염, false positive 유도, reward proxy 악용, simulator assumption 공격 |
| 공격 경로 | environment observation → state encoder → DRL policy → action selection → cyber response → reward/log update |
| 방어자 능력 | state validation, reward audit, safe action constraint, simulator 검증, runtime monitor, human approval |
| 제외 범위 | 실제 네트워크 공격, 실제 자동 차단 실험, 무단 시스템 조작, 공격 절차 제공 |

---

## 9. 평가방법 및 지표

| 평가축 | 지표 | 의미 | W09/P03 활용 |
|---|---|---|---|
| 탐지 성능 | detection rate, TPR, FPR | 공격 탐지와 오탐 균형 | IDS/alert 기반 DRL 평가 |
| 자동대응 효과 | mitigation success, response success | 방어 action이 피해를 줄였는지 | autonomous response 평가 |
| 비용 | response cost, service impact, false blocking rate | 대응의 운영 비용 | 안전 제약 평가 |
| 장기 성능 | cumulative reward, average return | 장기 방어 성능 | DRL 기본 성능 |
| 안정성 | policy stability, reward variance | episode별 변동성 | 재현성 평가 |
| 강건성 | RobustnessDrop under perturbed state | 상태 교란에 대한 내성 | 공격자 적응 평가 |
| 안전성 | unsafe action count, safety violation rate | 위험 action 발생 여부 | 배포 전 검증 |
| 감사 가능성 | state-action-reward trace completeness | 사후 재현·책임 추적 | W15 evidence chain |

---

## 10. 재현성 체크리스트

| 항목 | 기록해야 할 내용 |
|---|---|
| Environment | simulator/cyber range version, topology, traffic generator, scenario |
| State definition | state feature, alert source, normalization, missing data 처리 |
| Action space | monitor, block, isolate, patch, scan, escalate 등 action과 권한 수준 |
| Reward function | 탐지 보상, 오탐 penalty, 대응 비용, 서비스 영향 penalty, 가중치 |
| DRL model | DQN/policy gradient/actor-critic 등 알고리즘, network architecture, optimizer |
| Training | seed, episode 수, replay buffer, exploration schedule, hyperparameter |
| Evaluation | detection rate, FPR, cost, cumulative reward, safety violation, robustness |
| Security log | state-action-reward trace, unsafe action case, reward anomaly, policy checkpoint |
| 한계 | toy simulator 결과를 실제 SOC 자동대응 성능으로 과장하지 않음 |

---

## 11. 논문의 고유 기여

1. DRL을 사이버보안 분야에 직접 적용한 연구 흐름을 체계적으로 정리한다.
2. 사이버보안 문제가 단발성 classification을 넘어 sequential decision-making 문제로 확장될 수 있음을 보여준다.
3. 탐지율과 보상뿐 아니라 오탐, 대응 비용, 서비스 영향, 정책 강건성을 함께 평가해야 함을 설명한다.
4. W09에서 P01의 DRL 기본 이론과 P05의 DRL verification을 연결하는 중심 응용 문헌 역할을 한다.
5. 기말논문에서 cyber defense MDP, reward function, human approval, episode trace 기반 평가를 설계하는 근거가 된다.

---

## 12. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 실제 환경 전이 어려움 | simulation에서 학습한 정책이 실제 SOC·네트워크에서 실패할 수 있다. | simulation-to-real 한계 명시 |
| Reward 설계 취약성 | reward가 실제 보안 목표를 잘 반영하지 않으면 reward hacking 발생 | reward audit과 cost 항목 추가 |
| 공격자 적응성 | 공격자는 정책을 관찰하고 우회할 수 있다. | perturbed-state robustness 평가 |
| 재현성 부족 | 환경, seed, traffic, reward 설정 차이가 결과를 크게 바꾼다. | config와 episode trace 필수화 |
| 안전성 검증 부족 | 평균 reward가 높아도 위험 action이 발생할 수 있다. | safety violation rate와 human approval 병기 |
| 데이터·로그 프라이버시 | state와 reward log가 민감정보를 포함할 수 있다. | synthetic data와 log minimization 적용 |

---

## 13. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | AI 보안 대응은 탐지 모델 하나가 아니라 순차적 자동대응 policy 문제라는 문제의식 |
| 2장 관련연구 | DRL for cybersecurity survey를 직접 핵심 선행연구로 정리 |
| 3장 위협모형 | state observation, reward function, policy, action permission, episode log 보호 자산 정의 |
| 4장 연구방법 | cyber defense MDP, reward 설계, detection/FPR/cost/safety violation 지표 설계 |
| 5장 분석 | synthetic cyber-defense scenario에서 state-action-reward trace 표 제시 |
| 6장 보안적 함의 | reward hacking, unsafe action, human-in-the-loop, runtime monitoring 필요성 해석 |

---

## 14. 기말논문 연결 3문장

1. W09에서 기말논문에 반영할 개념: DRL for cybersecurity는 보안 대응을 state, action, reward, policy로 구성된 순차 의사결정 문제로 정의하며, 이는 RAG/agent 보안 자동대응 설계에도 적용 가능하다.
2. W09에서 기말논문에 반영할 표·그림·실험: cyber defense MDP 구조도, reward 설계표, detection/FPR/response cost/safety violation 평가표, state-action-reward trace 예시를 반영한다.
3. W09가 LLM/RAG 보안 감사 프레임워크와 연결되는 지점: LLM agent가 보안 action을 자동 수행할 경우 reward function, action permission, human approval, episode log를 W14/W15 evidence chain에 포함해야 한다.

---

## 15. 최종 판단

P03은 W09의 중심 문헌이다. P01이 DRL 기본 이론을 제공하고 P02가 안전 중요 시스템에서의 DRL 제약을 보여준다면, P03은 DRL을 사이버보안에 직접 적용하는 taxonomy와 평가축을 제공한다. 따라서 W09 기말논문 연결에서는 P03을 **cyber defense MDP, reward 설계, 자동대응 평가, human-in-the-loop 안전 제약의 중심 근거 문헌**으로 사용하는 것이 적절하다.

---

## 16. 변환 호환성 메모

```bash
pandoc P03_summary.md -o P03_summary.docx
pandoc P03_summary.md -o P03_summary.pdf --pdf-engine=xelatex
```
