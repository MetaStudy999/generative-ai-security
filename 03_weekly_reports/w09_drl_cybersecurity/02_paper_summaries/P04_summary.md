# P04 Summary

## Cyber-security and reinforcement learning — A brief survey — Amrin Maria Khan Adawadkar, Nilima Kulkarni, Engineering Applications of Artificial Intelligence, 2022

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W09 심층강화학습(DRL) & 사이버보안 적용·보상조작 |
| 논문명 | Cyber-security and reinforcement learning — A brief survey |
| 저자 | Amrin Maria Khan Adawadkar, Nilima Kulkarni |
| 공식 출판 정보 | Engineering Applications of Artificial Intelligence, Vol. 114, Article 105116, Sep. 2022 |
| DOI | https://doi.org/10.1016/j.engappai.2022.105116 |
| 로컬 PDF | `01_papers/pdf/04_Adawadkar_Kulkarni_2022_Cybersecurity_RL_Survey.pdf` |
| 검증 상태 | W09 `paper_list.md` 기준 공식 DOI 확인. 강의계획서의 `Aditya Adawadkar et al.` 표기와 공식 DOI 기준 저자명 차이 메모 유지 |
| PDF 확인 메모 | repo의 PDF 폴더에 해당 PDF blob이 존재함을 확인했다. 요약은 로컬 PDF 경로와 W09 `paper_list.md`의 공식 DOI 메타데이터 기준으로 보완했다. |
| 핵심 근거 사용 가능 여부 | 가능. W09에서 RL/DRL 기반 사이버보안 응용의 폭과 attacker-defender 순차 의사결정 구조를 보조 설명하는 문헌으로 사용 |

---

## 1. 한 문장 요약

이 논문은 reinforcement learning을 사이버보안 문제에 적용하는 연구 흐름을 **intrusion detection, intrusion response, adaptive defense, access control, cyber-physical security, network protection, game-like attacker-defender interaction, reward design** 관점에서 개괄하며, W09에서 보안 자동대응이 단순 분류가 아니라 **상태 관찰–방어 행동–보상–정책 개선**으로 이어지는 순차 의사결정 문제임을 설명하는 보조 핵심 문헌이다.

---

## 2. 핵심 연구문제

> 사이버보안 환경에서 공격자와 방어자는 지속적으로 상호작용하므로, RL 기반 방어자는 어떤 상태를 관찰하고 어떤 대응 action을 선택하며 어떤 reward를 기준으로 정책을 개선해야 안전하고 비용 효율적인 방어를 수행할 수 있는가?

| 번호 | 연구질문 |
|---|---|
| RQ1 | RL은 사이버 공격-방어 상호작용을 Markov decision process 또는 game-like sequential decision problem으로 어떻게 모델링할 수 있는가? |
| RQ2 | Intrusion detection, intrusion response, access control, malware 대응, resource allocation, CPS 보안에서 RL을 적용할 때 어떤 장점과 위험이 있는가? |
| RQ3 | 방어 에이전트의 state, action, reward 설계가 실제 탐지율, 오탐률, 대응 비용, 서비스 가용성에 어떤 영향을 주는가? |
| RQ4 | 공격자가 alert stream, state observation, reward feedback을 교란하면 RL 방어 정책은 어떤 취약성을 갖는가? |
| RQ5 | 실제 네트워크 자동방어에 RL을 적용하기 전에 simulation, human approval, rollback, audit log를 어떻게 설계해야 하는가? |

---

## 3. 논문의 핵심 기여

| 기여 | 설명 | W09 연결 |
|---|---|---|
| RL-cybersecurity 연결 정리 | RL이 cyber defense에 적용될 수 있는 주요 영역을 개괄 | W09 P03의 직접 사이버보안 DRL 문헌을 보조 |
| Attacker-defender 상호작용 관점 | 보안을 정적 분류가 아니라 동적 대응 문제로 해석 | 순차 의사결정 기반 보안 자동화 설명 |
| 응용 범위 확장 | intrusion detection/response, access control, network security, CPS security 등 응용을 정리 | 기말논문 관련연구 범위 확장 |
| Reward 설계 위험 강조 | reward가 실제 보안 목표를 반영하지 않으면 과잉 대응이나 취약 정책이 발생 가능 | reward hacking·false blocking 분석 연결 |
| 운영 안전성 함의 제공 | 실제 자동방어는 simulation 검증, 승인, rollback, 감사가 필요 | W14 MLOps·W15 evidence chain 연결 |

---

## 4. 목차별 핵심 개괄

| 목차 | 핵심 내용 | 비전공자용 이해 |
|---|---|---|
| 1. Introduction | 사이버공격은 계속 변하고 공격자는 방어자 대응을 관찰해 전략을 바꾼다. RL은 이런 반복 상호작용을 학습하는 방법으로 사용될 수 있다. | 보안은 시험문제처럼 한 번 맞히는 것이 아니라, 공격자와 방어자가 번갈아 움직이는 게임에 가깝다. |
| 2. Reinforcement Learning Background | Agent, environment, state, action, reward, policy, value, Q-learning 등 RL 기본 개념을 설명한다. | AI가 현재 상황을 보고 행동을 고른 뒤 결과 점수를 받아 다음 행동을 개선하는 방식이다. |
| 3. Cyber-security Applications | 침입탐지, 침입대응, access control, malware 대응, 네트워크 방어, CPS 보안 등 RL 적용 사례를 정리한다. | RL은 공격을 탐지하는 것뿐 아니라 어떤 방어 조치를 할지 결정하는 데도 쓰일 수 있다. |
| 4. Attacker-Defender Interaction | 공격자와 방어자의 상호작용을 sequential decision/game 관점으로 해석한다. | 공격자는 방어를 피하려 하고, 방어자는 공격 패턴에 맞춰 대응을 바꾸는 구조다. |
| 5. Reward and Policy Issues | 방어 목표를 reward로 어떻게 정의하느냐가 정책 품질을 좌우한다. 탐지율만 높이면 오탐과 과잉 차단이 생길 수 있다. | 점수를 잘못 주면 AI가 실제 보안이 아니라 점수 따기용 행동을 배운다. |
| 6. Challenges | 실제 네트워크 환경의 복잡성, 학습 데이터 부족, reward 설계, 안전성, 실시간성, 재현성, 공격자 적응성이 한계로 남는다. | 보안 자동화는 실험실에서 잘 되어도 실제 시스템에 넣기 전에 매우 조심해야 한다. |
| 7. Conclusion | RL은 사이버보안에 유망하지만, 실제 배포에는 검증 가능한 환경, 안전 제약, 운영 로그, 사람 승인 절차가 필요하다. | 자동방어는 편리하지만, 잘못 작동하면 서비스 장애를 만들 수 있어 통제가 필요하다. |

---

## 5. 핵심 이론 및 수식

> 아래 수식은 RL 기반 사이버보안 응용을 W09 보고서에서 설명하기 위한 표준화된 표현이다. 실제 공격 절차가 아니라 안전한 simulation/toy evaluation과 문헌 기반 분석을 전제로 한다.

### 5.1 Optimal Policy

RL agent는 상태 $s$에서 장기 보상이 가장 큰 행동을 선택하는 정책을 학습한다.

$$
\pi^*(s)=\arg\max_a Q^*(s,a)
$$

| 기호 | 의미 |
|---|---|
| $\pi^*(s)$ | 상태 $s$에서의 최적 정책 |
| $Q^*(s,a)$ | 상태 $s$에서 행동 $a$를 선택했을 때의 최적 행동가치 |

### 비전공자용 설명

보안 agent가 현재 상황을 보고 “차단할지, 관찰할지, 사람에게 넘길지” 중 장기적으로 가장 좋은 행동을 고르는 것이다.

### 보안적 의미

최적 정책은 reward 정의에 의존한다. reward가 실제 보안 목표를 제대로 반영하지 않으면 최적 정책도 안전하지 않을 수 있다.

---

### 5.2 Bellman Optimality Equation

최적 Q-value는 현재 reward와 다음 상태에서 얻을 수 있는 최적 가치로 정의된다.

$$
Q^*(s,a)=\mathbb{E}\left[r+\gamma\max_{a'}Q^*(s',a')\mid s,a\right]
$$

| 기호 | 의미 |
|---|---|
| $r$ | 현재 행동 이후 받은 reward |
| $s'$ | 다음 상태 |
| $a'$ | 다음 상태에서 가능한 행동 |
| $\gamma$ | 미래 reward 할인율 |

### 비전공자용 설명

좋은 행동은 지금 점수만 높은 행동이 아니라 다음 상황까지 고려했을 때 장기적으로 좋은 행동이다.

### 보안적 의미

당장 의심 트래픽을 차단하면 좋아 보일 수 있지만, 정상 서비스를 중단시키면 장기 비용이 커진다. 따라서 reward는 탐지와 비용을 같이 반영해야 한다.

---

### 5.3 Cybersecurity RL MDP

사이버보안 RL 환경은 다음과 같이 표현할 수 있다.

$$
\mathcal{M}_{sec}=(\mathcal{S},\mathcal{A},P,R,\gamma)
$$

| 기호 | 의미 |
|---|---|
| $\mathcal{S}$ | alert, traffic, host status, vulnerability, user/session state |
| $\mathcal{A}$ | monitor, scan, block, isolate, patch, escalate, rollback |
| $P$ | 방어 action 이후 환경 전이 |
| $R$ | 탐지 보상, 오탐 penalty, 대응 비용, 서비스 영향 |
| $\gamma$ | 미래 효과 반영 정도 |

### 보안적 의미

사이버보안 RL은 state와 action 정의가 부정확하면 잘못된 정책을 학습한다. 특히 자동 차단·격리 action은 반드시 권한과 승인 조건이 필요하다.

---

### 5.4 Response Utility Score

방어 action의 효용은 성공 보상과 비용 penalty를 함께 고려해야 한다.

$$
ResponseUtility=w_1\cdot ResponseSuccess-w_2\cdot FalsePositive-w_3\cdot ResponseCost-w_4\cdot AvailabilityImpact
$$

| 항목 | 의미 |
|---|---|
| ResponseSuccess | 공격 탐지·차단·완화 성공 |
| FalsePositive | 정상 행위를 공격으로 오탐한 비용 |
| ResponseCost | 조치 수행 비용과 운영 부담 |
| AvailabilityImpact | 서비스 중단, 지연, 정상 사용자 영향 |

### 비전공자용 설명

공격을 막는 것이 중요하지만 정상 사용자까지 막으면 좋은 대응이 아니다.

---

### 5.5 Missed Attack Rate와 False Blocking Rate

자동대응은 놓친 공격과 잘못 차단한 정상 행위를 모두 평가해야 한다.

$$
MissedAttackRate=\frac{FN_{attack}}{TP_{attack}+FN_{attack}}
$$

$$
FalseBlockingRate=\frac{FP_{normal}}{FP_{normal}+TN_{normal}}
$$

### 보안적 의미

MissedAttackRate가 높으면 공격을 놓치고, FalseBlockingRate가 높으면 정상 사용자를 막는다. 두 지표를 동시에 줄이는 것이 목표다.

---

### 5.6 Policy Stability

학습된 정책이 episode나 환경 변화에 따라 과도하게 흔들리지 않는지 평가한다.

$$
PolicyStability=1-\frac{1}{N}\sum_{i=1}^{N}d(\pi_i,\pi_{i-1})
$$

| 기호 | 의미 |
|---|---|
| $\pi_i$ | $i$번째 학습 또는 평가 시점의 정책 |
| $d(\cdot)$ | 정책 차이를 측정하는 거리 함수 |

### 보안적 의미

정책이 조금의 로그 변화나 트래픽 변화에 과도하게 바뀌면 운영 신뢰성이 낮다. 보안 자동화에는 policy stability가 중요하다.

---

### 5.7 Human Approval and Rollback Constraint

고위험 대응은 자동 실행보다 승인과 rollback이 필요하다.

$$
a_t\in\mathcal{A}_{high\text{-}risk}\Rightarrow Approval(a_t)=1 \land RollbackPlan(a_t)=1
$$

### 보안적 의미

서버 격리, 계정 잠금, 네트워크 차단, 정책 변경은 자동 실행하지 않고 승인·복구 계획과 함께 수행해야 한다.

---

## 6. AI 원리 70% 관점 분석

| 원리 항목 | 설명 | W09/P04에서의 의미 |
|---|---|---|
| Reinforcement Learning | agent가 action을 선택하고 reward로 정책을 개선 | 보안 자동대응의 기본 원리 |
| Bellman Equation | 현재 reward와 미래 가치를 함께 고려 | 단기 탐지와 장기 운영 비용 균형 |
| Q-value | state-action의 장기 가치 추정 | 방어 action 선택 기준 |
| Exploration | 새로운 방어 전략 시도 | 미지 공격 대응 가능성과 위험 병존 |
| Attacker-defender dynamics | 공격자와 방어자가 서로 적응 | 고정 규칙 방어의 한계 설명 |
| Reward shaping | 탐지·오탐·비용·가용성을 reward로 결합 | reward hacking 방지 |
| Policy stability | 정책의 일관성 유지 | 운영 신뢰성 확보 |
| Human oversight | 고위험 action 승인 | 실제 배포 안전장치 |

---

## 7. 보안 이슈 30% 관점 분석

| 보안 항목 | RL-Cybersecurity 관점 해석 | 대표 평가 지표 |
|---|---|---|
| 기밀성 | alert stream, network state, user/session log가 민감정보가 될 수 있음 | state exposure risk, log access control |
| 무결성 | state, reward, policy, action log가 조작되면 방어 정책이 왜곡됨 | reward manipulation rate, state poisoning rate |
| 가용성 | 과잉 차단·격리로 정상 서비스가 중단될 수 있음 | false blocking rate, availability impact |
| 프라이버시 | 사용자 행동 로그 기반 state가 개인정보를 포함할 수 있음 | log minimization, privacy filtering |
| 안전성 | 잘못된 action이 방어 실패 또는 운영 장애를 만들 수 있음 | unsafe action count, rollback success |
| 책임성 | 자동 action의 근거와 결과를 추적해야 함 | policy auditability, action trace completeness |

---

## 8. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | defense policy, alert stream, network service, user availability, state representation, reward function, action log, rollback plan |
| 공격자 목표 | 방어 정책 예측, state observation 교란, false alert 유발, 대응 비용 증가, 과잉 차단 유도, reward hacking |
| 공격자 능력 | traffic pattern 변경, 로그 누락·오염 유발, alert flooding, 정상/악성 경계 혼동 유도, policy probing |
| 공격 경로 | network event → alert/state stream → RL policy → response action → service impact/reward feedback → policy update |
| 방어자 능력 | state validation, reward audit, action permission, human approval, rollback, runtime monitoring, policy evaluation |
| 제외 범위 | 실제 네트워크 공격, 실제 자동 차단 실험, 무단 시스템 조작, 공격 절차 제공 |

---

## 9. 평가방법 및 지표

| 평가축 | 지표 | 의미 | W09/P04 활용 |
|---|---|---|---|
| 탐지·대응 성공 | response success, detection rate | 공격을 탐지·완화했는지 | 자동대응 성능 |
| 미탐 | missed attack rate | 공격을 놓친 비율 | 보안 실패 비용 |
| 오탐·과잉차단 | FPR, false blocking rate | 정상 행위를 잘못 차단 | 가용성·사용성 평가 |
| 비용 | response cost, availability impact | 조치 비용과 서비스 영향 | 운영 가능성 |
| 장기 보상 | cumulative reward, average return | 장기 방어 성능 | RL 성능 지표 |
| 안정성 | policy stability, reward variance | 정책이 일관적인지 | 재현성·운영 신뢰성 |
| 안전성 | unsafe action count, rollback success | 위험 action과 복구 가능성 | 배포 전 검증 |
| 감사 가능성 | action trace completeness | 자동 action 설명·재현 가능성 | W15 evidence chain |

---

## 10. 재현성 체크리스트

| 항목 | 기록해야 할 내용 |
|---|---|
| Environment | simulator/cyber range, topology, traffic model, attacker model, scenario |
| State stream | alert source, feature definition, observation interval, missing value 처리 |
| Action space | monitor, block, isolate, patch, escalate, rollback 등 action과 권한 수준 |
| Reward function | 탐지 보상, 오탐 penalty, 비용, 가용성 영향, reward weight |
| RL algorithm | Q-learning/DQN/policy gradient/actor-critic 등 사용 알고리즘 |
| Training | seed, episode 수, exploration schedule, replay buffer, hyperparameter |
| Evaluation | response success, missed attack, FPR, cost, stability, unsafe action |
| Safety control | human approval rule, rollback plan, forbidden action list |
| Security log | state-action-reward trace, policy checkpoint, failure case, reviewer decision |
| 한계 | toy/simulation 결과를 실제 SOC 자동대응 성능으로 과장하지 않음 |

---

## 11. 논문의 고유 기여

1. RL과 사이버보안의 접점을 짧지만 폭넓게 개괄한다.
2. 공격-방어 상호작용을 순차 의사결정 문제로 해석할 수 있음을 보여준다.
3. Intrusion detection/response, access control, cyber-physical security 등 응용 범위를 넓힌다.
4. Reward 설계와 정책 선택이 보안 효과뿐 아니라 오탐·비용·가용성에 영향을 준다는 점을 설명한다.
5. W09 P03의 DRL for cyber security 문헌과 함께 자동대응 평가축을 구성하는 보조 핵심 문헌으로 활용 가능하다.

---

## 12. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 짧은 survey | 폭넓은 개괄이지만 각 응용의 실험 세부사항은 제한적이다. | P03/P05와 결합해 깊이 보완 |
| 실제 배포 위험 | RL 자동방어는 과잉 대응과 서비스 중단 위험이 있다. | action approval, rollback, safety constraint 포함 |
| Reward misspecification | reward가 실제 보안 목표와 다르면 잘못된 정책이 학습된다. | reward audit와 cost 항목 명시 |
| 공격자 적응성 | 공격자는 방어 정책을 관찰하고 우회할 수 있다. | policy probing과 perturbed-state 평가 포함 |
| 재현성 부족 | 환경·트래픽·시드·reward 설정이 달라지면 결과가 달라진다. | config와 episode trace를 필수화 |
| 개인정보·로그 위험 | 보안 로그와 사용자 행위 데이터가 민감정보를 포함할 수 있다. | synthetic/toy data와 log minimization 적용 |

---

## 13. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | RL은 사이버 공격-방어 상호작용을 자동대응 정책 문제로 해석할 수 있다는 문제의식 |
| 2장 관련연구 | RL-cybersecurity brief survey를 보조 선행연구로 정리 |
| 3장 위협모형 | alert stream, state, reward, policy, action log, rollback plan 보호 자산 정의 |
| 4장 연구방법 | response success, missed attack rate, false blocking rate, policy stability, rollback success 지표 설계 |
| 5장 분석 | 자동대응 action approval과 rollback 기반 안전 제약표 제시 |
| 6장 보안적 함의 | reward hacking, 과잉차단, 정책 예측, audit log, human approval 필요성 해석 |

---

## 14. 기말논문 연결 3문장

1. W09에서 기말논문에 반영할 개념: RL은 사이버 공격-방어 상호작용을 상태, 행동, 보상, 정책으로 구성된 동적 문제로 모델링할 수 있게 한다.
2. W09에서 기말논문에 반영할 표·그림·실험: RL cyber defense pipeline, response utility score, false blocking/missed attack 평가표, human approval·rollback action 분류표를 반영한다.
3. W09가 LLM/RAG 보안 감사 프레임워크와 연결되는 지점: LLM agent가 보안 action을 자동 수행할 경우 RL 기반 정책 선택은 반드시 action permission, rollback, policy audit, state-action-reward log를 W14/W15 evidence chain에 포함해야 한다.

---

## 15. 최종 판단

P04는 W09의 보안 응용 보조 핵심 문헌이다. P03이 DRL 기반 사이버보안을 더 직접적이고 체계적으로 다룬다면, P04는 RL과 사이버보안의 접점을 짧게 개괄하면서 공격-방어 상호작용, response cost, false blocking, policy stability, rollback 필요성을 설명하는 데 유용하다. 따라서 W09 기말논문 연결에서는 P04를 **RL 기반 자동대응의 운영 위험과 승인·복구·감사 설계의 근거 문헌**으로 사용하는 것이 적절하다.

---

## 16. 변환 호환성 메모

```bash
pandoc P04_summary.md -o P04_summary.docx
pandoc P04_summary.md -o P04_summary.pdf --pdf-engine=xelatex
```
