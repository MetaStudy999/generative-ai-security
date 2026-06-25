# P05 Summary

## Deep Reinforcement Learning Verification: A Survey — Matthew Landers, Afsaneh Doryab, ACM Computing Surveys, 2023

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W09 심층강화학습(DRL) & 사이버보안 적용·보상조작 |
| 논문명 | Deep Reinforcement Learning Verification: A Survey |
| 저자 | Matthew Landers, Afsaneh Doryab |
| 공식 출판 정보 | ACM Computing Surveys, Vol. 55, No. 14s, Article 330, pp. 1–31, online 2023-07-17 |
| DOI | https://doi.org/10.1145/3596444 |
| 로컬 PDF | `01_papers/pdf/05_Landers_Doryab_2023_DRL_Verification_Survey.pdf` |
| 검증 상태 | W09 `paper_list.md` 기준 공식 DOI 확인. 강의계획서 지정 `H. Yan et al.`과 동일 논문인지 확인되지 않아 동일성 확인 메모 유지 |
| PDF 확인 메모 | repo의 PDF 폴더에 해당 PDF blob이 존재함을 확인했다. 요약은 로컬 PDF 경로와 W09 `paper_list.md`의 공식 DOI 메타데이터 기준으로 보완했다. |
| 핵심 근거 사용 가능 여부 | 가능. W09에서 DRL policy의 안전성 검증, testing, formal verification, runtime monitoring, counterexample trace를 설명하는 검증 핵심 문헌으로 사용 |

---

## 1. 한 문장 요약

이 논문은 deep reinforcement learning verification을 **policy verification, safety property, reachability analysis, formal methods, simulation-based testing, adversarial state testing, runtime monitoring, counterexample generation, coverage, scalability** 관점에서 정리하며, W09에서 DRL 기반 사이버 방어 agent를 실제 운영 전에 안전 명세와 violation rate로 검증해야 함을 뒷받침하는 핵심 문헌이다.

---

## 2. 핵심 연구문제

> DRL policy는 높은 reward를 달성하더라도 특정 상태에서 위험한 action을 선택할 수 있으므로, 이를 운영 전에 어떤 safety specification, formal verification, testing, runtime monitoring으로 검증할 수 있는가?

| 번호 | 연구질문 |
|---|---|
| RQ1 | DRL policy는 어떤 safety property와 behavioral specification으로 검증할 수 있는가? |
| RQ2 | Formal verification, reachability analysis, model checking, abstraction은 DRL policy의 어떤 안전성을 보증할 수 있는가? |
| RQ3 | Testing과 adversarial state generation은 DRL policy의 failure case와 counterexample을 어떻게 찾는가? |
| RQ4 | Runtime monitoring은 배포 후 unsafe action을 어떻게 탐지하고 차단할 수 있는가? |
| RQ5 | 사이버 방어 DRL agent에서 차단·격리·계정잠금·정책변경 같은 고위험 action은 어떤 검증과 승인 절차가 필요한가? |

---

## 3. 논문의 핵심 기여

| 기여 | 설명 | W09 연결 |
|---|---|---|
| DRL verification taxonomy | DRL policy 검증 기법을 formal verification, testing, runtime monitoring 등으로 분류 | W09 검증 핵심 문헌 |
| Safety property 중심 관점 | reward와 별개로 policy가 지켜야 할 안전 명세를 강조 | cyber defense unsafe action 제약 |
| Formal methods 적용 정리 | reachability, abstraction, model checking, SMT/MILP 계열 접근의 장단점 정리 | W12 신경망 검증과 연결 |
| Testing과 counterexample | simulation-based testing, adversarial test, falsification으로 failure case 탐색 | W09 toy/cyber range 평가 연결 |
| Runtime assurance 필요성 | 정적 검증만으로 부족한 경우 runtime monitor와 fallback 필요 | W14 MLOps·W15 evidence chain 연결 |

---

## 4. 목차별 핵심 개괄

| 목차 | 핵심 내용 | 비전공자용 이해 |
|---|---|---|
| 1. Introduction | DRL은 복잡한 환경에서 강력하지만, 예측 불가능한 action과 안전성 문제가 있다. 따라서 policy 검증이 필요하다. | AI가 점수는 잘 받아도 위험한 선택을 할 수 있으므로, 실제 투입 전 안전검사가 필요하다. |
| 2. Background | RL/DRL, MDP, policy, neural network, safety property, verification 기본 개념을 설명한다. | 정책은 “상황을 보고 행동을 고르는 규칙”이고, 검증은 이 규칙이 위험한 행동을 하지 않는지 확인하는 일이다. |
| 3. Verification Problems | 정책 안전성, 입력 교란, 도달가능 상태, action constraint, reward와 safety의 불일치 문제를 다룬다. | 평균 점수가 높아도 특정 상황에서 위험한 행동을 하면 안전하지 않다. |
| 4. Formal Verification | 수학적 방법으로 특정 상태 범위에서 policy가 안전 명세를 만족하는지 증명하려는 접근을 정리한다. | 가능한 상황을 수학적으로 따져 “이 범위 안에서는 위험 행동을 안 한다”고 확인하는 방식이다. |
| 5. Testing and Falsification | simulation과 adversarial test로 policy가 실패하는 상태를 찾는다. | AI가 언제 실수하는지 일부러 어려운 상황을 만들어 시험한다. |
| 6. Runtime Monitoring | 배포 중 policy 행동을 감시하고, 위험 action이 감지되면 차단·경고·fallback을 수행한다. | 자동차에 긴급브레이크가 있듯이, 보안 agent에도 위험 action을 막는 감시 장치가 필요하다. |
| 7. Challenges | DRL policy의 고차원 상태공간, 연속 action, 복잡한 environment, scalability, specification 설계가 어렵다. | 모든 가능한 상황을 완전히 검증하기 어렵기 때문에 제한된 범위와 증거를 명확히 해야 한다. |
| 8. Future Directions | scalable verification, compositional verification, safe RL, robust testing, certified runtime assurance가 필요하다. | 앞으로는 더 큰 모델과 실제 운영 환경에서도 쓸 수 있는 검증법이 필요하다. |
| 9. Conclusion | DRL 검증은 안전 중요 시스템에 필수이며, formal verification, testing, monitoring을 결합해야 한다. | 자동화 AI를 믿으려면 성능표뿐 아니라 안전검사표와 실패사례 기록이 필요하다. |

---

## 5. 핵심 이론 및 수식

> 아래 수식은 DRL verification과 W09 사이버보안 자동대응 검증을 설명하기 위한 표준화된 표현이다. 실제 시스템 공격 절차가 아니라 safety specification과 평가 지표를 설명하기 위한 것이다.

### 5.1 Safety Property

DRL policy가 안전 상태에서 위험 action을 선택하지 않아야 한다는 명세다.

$$
\forall s\in \mathcal{S}_{safe},\quad \pi(s)\notin \mathcal{A}_{unsafe}
$$

| 기호 | 의미 |
|---|---|
| $\mathcal{S}_{safe}$ | 정상 운영 또는 안전 상태 집합 |
| $\pi(s)$ | 상태 $s$에서 policy가 선택한 action |
| $\mathcal{A}_{unsafe}$ | 자동 실행하면 안 되는 위험 action 집합 |

### 비전공자용 설명

정상 상황에서는 서버 격리, 계정 잠금, 전체 차단 같은 위험한 행동을 자동으로 하면 안 된다는 규칙이다.

---

### 5.2 Violation Rate

검증 또는 테스트 중 unsafe action이 발생한 비율이다.

$$
ViolationRate=\frac{N_{unsafe\ actions}}{N_{episodes}}
$$

| 기호 | 의미 |
|---|---|
| $N_{unsafe\ actions}$ | unsafe action이 발생한 횟수 또는 episode 수 |
| $N_{episodes}$ | 전체 평가 episode 수 |

### 보안적 의미

평균 reward가 높아도 violation rate가 높으면 실제 보안 자동대응에 배포하면 안 된다. 안전성은 성능과 별도 지표로 관리해야 한다.

---

### 5.3 Reachability of Unsafe States

Policy를 따를 때 unsafe state에 도달 가능한지 확인한다.

$$
Reach_{\pi}(\mathcal{S}_0)=\{s_t\mid s_0\in\mathcal{S}_0,\; a_t=\pi(s_t),\; s_{t+1}\sim P(\cdot\mid s_t,a_t)\}
$$

$$
Reach_{\pi}(\mathcal{S}_0)\cap \mathcal{S}_{unsafe}=\varnothing
$$

| 기호 | 의미 |
|---|---|
| $\mathcal{S}_0$ | 초기 상태 집합 |
| $Reach_{\pi}$ | policy를 따를 때 도달 가능한 상태 집합 |
| $\mathcal{S}_{unsafe}$ | 장애·위험·정책 위반 상태 집합 |

### 비전공자용 설명

AI가 어떤 행동을 계속 선택해도 금지된 위험 상태로 가지 않는지 확인하는 것이다.

---

### 5.4 Counterexample Trace

검증 실패 시, 어떤 상태-행동 경로가 unsafe result로 이어졌는지 기록해야 한다.

$$
\tau_{cex}=(s_0,a_0,r_0,s_1,a_1,r_1,\ldots,s_T),\qquad s_T\in\mathcal{S}_{unsafe}
$$

### 보안적 의미

Counterexample trace는 “왜 실패했는지”를 설명하는 증거다. W09에서는 unsafe action case를 보고서에 남기되, 실제 공격 절차가 아니라 synthetic/toy trace로 제한해야 한다.

---

### 5.5 Runtime Monitor

Runtime monitor는 실행 중 policy action이 safety specification을 위반하는지 검사한다.

$$
Monitor(s_t,a_t)=
\begin{cases}
allow, & (s_t,a_t)\models \varphi_{safe}\\
block, & (s_t,a_t)\not\models \varphi_{safe}
\end{cases}
$$

| 기호 | 의미 |
|---|---|
| $\varphi_{safe}$ | 안전 명세 |
| allow | action 실행 허용 |
| block | action 차단 또는 human approval 요청 |

### 보안적 의미

DRL policy가 잘못된 action을 선택해도 runtime monitor가 실행 전에 막을 수 있어야 한다. 고위험 보안 action은 monitor와 human approval을 통과해야 한다.

---

### 5.6 False Safe Rate

검증기 또는 monitor가 unsafe action을 안전하다고 잘못 판단한 비율이다.

$$
FalseSafeRate=\frac{N_{unsafe\ accepted}}{N_{unsafe\ actions}}
$$

### 보안적 의미

검증 도구도 완벽하지 않다. unsafe action을 safe로 잘못 허용하는 false safe가 낮아야 한다.

---

### 5.7 Verification Coverage

검증이 전체 상태·행동 공간 중 어느 범위를 다뤘는지 기록한다.

$$
Coverage=\frac{|\mathcal{S}_{verified}\times\mathcal{A}_{verified}|}{|\mathcal{S}_{target}\times\mathcal{A}_{target}|}
$$

### 보안적 의미

“검증했다”는 말은 범위가 중요하다. 어떤 상태와 action을 검증했는지 coverage를 기록하지 않으면 과장된 안전성 주장이 된다.

---

## 6. AI 원리 70% 관점 분석

| 원리 항목 | 설명 | W09/P05에서의 의미 |
|---|---|---|
| Policy verification | DRL policy가 명세를 만족하는지 확인 | 자동 방어 action 안전성 검증 |
| Safety property | reward와 별도로 지켜야 할 안전 조건 | 차단·격리·삭제 action 제약 |
| Reachability | policy가 어떤 상태로 갈 수 있는지 분석 | unsafe state 도달 가능성 확인 |
| Formal methods | 수학적 검증·추상화·제약해결 | W12 신경망 검증과 연결 |
| Testing/falsification | failure case와 counterexample 탐색 | simulation 기반 보안 평가 |
| Runtime monitoring | 실행 중 unsafe action 감시 | 실제 운영 안전장치 |
| Coverage | 검증 범위 명시 | 과장된 안전성 주장 방지 |
| Counterexample | 실패 경로 기록 | 재현성·감사 증거 |

---

## 7. 보안 이슈 30% 관점 분석

| 보안 항목 | DRL Verification 관점 해석 | 대표 평가 지표 |
|---|---|---|
| 기밀성 | 검증 로그와 state trace가 내부 보안 상태를 포함할 수 있음 | trace access control, log minimization |
| 무결성 | safety specification, monitor, policy checkpoint가 조작되면 검증 결과가 왜곡됨 | spec integrity, checkpoint hash |
| 가용성 | monitor가 정상 action을 과도하게 차단하면 방어 지연 또는 서비스 문제 발생 | false block rate, latency |
| 프라이버시 | state/action trace에 사용자·세션 정보가 포함될 수 있음 | privacy filtering, anonymization |
| 안전성 | unsafe action과 unsafe state 도달을 방지해야 함 | violation rate, unsafe reachability |
| 책임성 | counterexample trace와 monitor decision을 남겨야 사고 재현 가능 | trace completeness, audit completeness |

---

## 8. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | DRL policy, safety specification, action space, monitor, verification result, counterexample trace, policy checkpoint, runtime log |
| 공격자 목표 | state 교란으로 unsafe action 유도, monitor 우회, safety spec 약화, policy checkpoint 오염, false safe 유도 |
| 공격자 능력 | state observation 조작, environment assumption 악용, adversarial state 생성, log/trace 누락 유도, 검증 범위 밖 상태 유도 |
| 공격 경로 | environment state → policy inference → proposed action → monitor/verification layer → action execution/logging |
| 방어자 능력 | formal specification, testing, adversarial state evaluation, runtime monitor, action permission, rollback, human approval |
| 제외 범위 | 실제 네트워크 공격, 실제 자동 차단 실험, 무단 시스템 조작, 검증 우회 절차 제공 |

---

## 9. 평가방법 및 지표

| 평가축 | 지표 | 의미 | W09/P05 활용 |
|---|---|---|---|
| 안전성 | violation rate, unsafe action count | 위험 action 발생 여부 | 자동대응 배포 전 핵심 지표 |
| 도달가능성 | unsafe reachability, reachable unsafe states | policy가 위험 상태로 갈 수 있는지 | formal verification 연결 |
| 강건성 | policy robustness, adversarial state failure rate | 상태 교란에 대한 안전성 | 공격자 적응 평가 |
| 검증 범위 | coverage, verified state-action ratio | 검증한 범위 | 안전 주장 범위 명시 |
| Runtime assurance | monitor alarm rate, blocked unsafe action | 실행 중 위험 action 차단 | MLOps 운영 연결 |
| 오탐/과잉차단 | false block rate, false safe rate | monitor 판단 오류 | 실사용성 평가 |
| 재현성 | counterexample trace completeness | 실패 사례 재현 가능성 | W15 evidence chain |
| 비용 | verification time, runtime latency | 검증·운영 비용 | 배포 가능성 평가 |

---

## 10. 재현성 체크리스트

| 항목 | 기록해야 할 내용 |
|---|---|
| Safety specification | 안전 명세, 금지 action, 금지 state, threshold, 근거 |
| Environment | simulator/cyber range version, topology, transition assumption, scenario |
| Policy | DRL algorithm, policy checkpoint, model hash, training seed |
| Action space | safe action, approval-required action, forbidden action 구분 |
| Verification method | formal verification, testing, falsification, runtime monitoring 중 사용 방식 |
| Coverage | 검증한 state/action 범위와 제외 범위 |
| Counterexample | unsafe trace, state-action-reward sequence, failure condition |
| Runtime monitor | monitor rule, alarm threshold, block/approval/fallback policy |
| Evaluation | violation rate, false safe, false block, robustness, latency |
| 한계 | 검증 범위 밖 상태에 대해 안전을 보증하지 않음 |

---

## 11. 논문의 고유 기여

1. DRL policy 검증 연구를 formal verification, testing, runtime monitoring 관점으로 체계화한다.
2. DRL의 성능 평가와 안전성 검증을 분리해야 함을 명확히 보여준다.
3. Safety property, violation rate, counterexample trace, runtime monitor를 DRL 운영의 핵심 증거로 제시한다.
4. W09 P03/P04의 DRL 사이버보안 자동대응 연구에 검증 계층을 추가하는 근거가 된다.
5. W12 신경망 검증, W14 MLOps, W15 reproducibility와 직접 연결되는 bridge 문헌으로 활용 가능하다.

---

## 12. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 확장성 문제 | 고차원 state/action space에서 formal verification은 계산 비용이 크다. | toy/small policy와 runtime monitor 중심으로 제한 |
| 명세 설계 어려움 | 무엇이 안전한 action인지 도메인별로 다르다. | cyber action safety table 작성 |
| 검증 범위 한계 | 모든 가능한 공격 상태를 완전히 검증하기 어렵다. | coverage와 excluded scope 명시 |
| False safe 위험 | 검증기 또는 monitor가 unsafe action을 놓칠 수 있다. | false safe rate와 human approval 병기 |
| Runtime overhead | monitor가 latency를 증가시킬 수 있다. | runtime latency와 blocked action 기록 |
| 실제 운영 전이 | simulation 검증이 실제 SOC 환경 안전을 완전히 보장하지 않는다. | limitation statement와 rollback plan 포함 |

---

## 13. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | DRL 기반 보안 자동대응은 성능보다 safety property와 violation rate 관리가 우선이라는 문제의식 |
| 2장 관련연구 | DRL verification survey를 자동대응 안전 검증 문헌으로 정리 |
| 3장 위협모형 | policy, action space, safety specification, monitor, counterexample trace 보호 자산 정의 |
| 4장 연구방법 | violation rate, unsafe reachability, coverage, false safe, runtime alarm 지표 설계 |
| 5장 분석 | cyber defense action safety table과 runtime monitor workflow 제시 |
| 6장 보안적 함의 | human approval, rollback, monitor, audit log, 검증 범위 한계 해석 |

---

## 14. 기말논문 연결 3문장

1. W09에서 기말논문에 반영할 개념: DRL 기반 보안 자동대응은 cumulative reward가 높더라도 unsafe action을 선택하면 배포할 수 없으므로, safety property와 violation rate를 별도로 검증해야 한다.
2. W09에서 기말논문에 반영할 표·그림·실험: safety property 표, action safety classification, violation rate·false safe rate·coverage 평가표, runtime monitor workflow를 반영한다.
3. W09가 LLM/RAG 보안 감사 프레임워크와 연결되는 지점: LLM agent가 차단·삭제·신고·도구 실행 같은 action을 수행할 때도 DRL verification과 동일하게 action permission, monitor, human approval, counterexample trace를 W14/W15 evidence chain에 포함해야 한다.

---

## 15. 최종 판단

P05는 W09의 검증 핵심 문헌이다. P01이 DRL 기본 이론을 제공하고 P03/P04가 사이버보안 적용을 설명한다면, P05는 자동대응 정책을 실제 운영 전에 어떻게 안전하게 검증할지 설명한다. 따라서 W09 기말논문 연결에서는 P05를 **safety property, violation rate, runtime monitor, counterexample trace, human approval 기반 자동대응 검증의 중심 근거 문헌**으로 사용하는 것이 적절하다.

---

## 16. 변환 호환성 메모

```bash
pandoc P05_summary.md -o P05_summary.docx
pandoc P05_summary.md -o P05_summary.pdf --pdf-engine=xelatex
```
