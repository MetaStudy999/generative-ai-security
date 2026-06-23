# W09 DRL 기반 사이버보안

Research Question: DRL 기반 사이버보안에서 성능 지표와 보안 지표를 어떻게 분리해 평가할 수 있는가?

---

## Core Formula

### MDP Tuple, Return, Bellman Equation

$$
\mathcal{M}=(\mathcal{S},\mathcal{A},P,R,\gamma),
\qquad
G_t=\sum_{k=0}^{\infty}\gamma^k r_{t+k},
\qquad
V^\pi(s)=\mathbb{E}_{a\sim\pi}\left[R(s,a)+\gamma\sum_{s'}P(s'|s,a)V^\pi(s')\right]
$$

| 기호 | 의미 |
|---|---|
| `\mathcal{S},\mathcal{A}` | 상태 공간과 행동 공간 |
| `P,R` | 전이확률과 보상 함수 |
| `\gamma` | 할인율 |
| `V^\pi` | 정책 pi의 상태 가치 |

- 직관적 의미: DRL은 상태, 행동, 전이, 보상으로 정책을 학습한다. Bellman 식은 현재 가치가 즉시 보상과 미래 가치로 구성됨을 보여준다.
- 보안적 의미: 보상이 잘못 설계되면 정책이 보안 목표와 다른 방향으로 최적화될 수 있다.
- 평가 지표 연결: average_reward, observed_reward, detection_f1, policy_robustness와 연결한다.
- 한계: toy environment 기준이며 실제 사이버 작전 자동화를 다루지 않는다.

---

## Threat Model

- Diagram: MDP security evaluation flow
- Stages: State, Policy, Action, Reward, Safety Eval
- 안전 범위: public, synthetic, toy, local evaluation

![W09 pipeline diagram](assets/diagrams/w09_pipeline_diagram.svg)

---

## Evaluation Protocol

- Metrics: average_reward, observed_reward, detection_f1, safety_violation_rate, policy_robustness
- 데이터 출처: `04_experiment/outputs/metrics_summary.csv`

| condition | average_reward | observed_reward | detection_f1 | safety_violation_rate | policy_robustness |
| --- | --- | --- | --- | --- | --- |
| Normal reward | 1.085 | 1.085 | 0.84 | 0.012 | 0.838 |
| Manipulated reward | 0.521 | 0.842 | 0.618 | 0.195 | 0.325 |
| Robust reward design | 0.911 | 0.967 | 0.781 | 0 | 0.71 |

---

## Figure-first Result

![W09 metrics chart](assets/charts/w09_metrics_chart.svg)

그래프는 reward, detection_f1, safety_violation_rate, policy_robustness를 조건별로 함께 보여준다. 보상 점수가 좋아 보여도 safety violation이 높으면 보안 정책으로는 실패할 수 있다. 수치는 `metrics_summary.csv`에서 읽었다.

---

## Paper Map

| ID | 논문 역할 | 발표에서 쓰는 위치 | 기말논문 연결 |
|---|---|---|---|
| P01 | 핵심 이론 | Background / Core Formula | DRL 기반 사이버보안의 관련연구 뼈대 |
| P02 | 위협 분류 | Threat Model | 공격자·방어자·보호자산 정의 |
| P03 | 평가 지표 | Evaluation Protocol | 정량 지표와 로그 근거 연결 |
| P04 | 공격·방어 사례 | Security Implication | 보안적 함의와 방어 한계 |
| P05 | 재현성·정책 근거 | Limitation | 확인 필요 항목과 제출 전 검증 |

---

## Limitation

- DRL 환경은 toy simulation이며 실제 네트워크 공격 자동화 절차를 제공하지 않는다.
- 원문 DOI/URL과 formal guarantee는 최종 제출 전 확인 필요.
- 실제 운영 시스템 악용 절차나 무단 API 질의 절차는 포함하지 않음.

---

## Final Takeaway

W09의 핵심은 `average_reward, observed_reward, detection_f1, safety_violation_rate, policy_robustness`를 성능·보안·재현성 근거로 분리해 기말논문의 평가방법에 연결하는 것이다.
