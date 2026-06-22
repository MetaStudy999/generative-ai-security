# W09 심층강화학습(DRL) & 사이버보안 적용·보상조작 통합보고서

## 0. 메타정보

| 항목 | 내용 |
|---|---|
| 주차 | W09 |
| 주제 | 심층강화학습(DRL) & 사이버보안 적용·보상조작 |
| 작성일 | 2026-06-22 |
| 문서 상태 | 최종본 |
| 사용 AI 도구 | Codex |
| 실습 환경 | Ubuntu 24.04 기준, Python 3, Docker 설정 포함 |
| 실험 근거 | `04_experiment/outputs/run_log.md`, `metrics_summary.csv`, `results.json` |

## 1. 한 문장 요약

DRL 기반 사이버 방어 에이전트는 상태·행동·보상 설계에 따라 방어 성능과 안전성이 크게 달라지며, 보상조작은 높은 관측 보상 뒤에서 실제 보안 목표를 훼손할 수 있다.

## 2. AI 원리 70% 정리

강화학습은 agent가 state를 관측하고 action을 선택한 뒤 reward를 받아 policy를 개선하는 순차 의사결정 구조다. DRL은 value function 또는 policy를 deep neural network로 근사해 큰 상태공간을 다루며, DQN, policy gradient, actor-critic이 대표적이다.

| 개념 | W09에서의 의미 | 관련 문헌 |
|---|---|---|
| MDP | 사이버 방어 환경을 state, action, transition, reward로 모델링 | P01, P05 |
| Q-function | 상태-행동 쌍의 기대 누적 보상 | P01 |
| DQN | 큰 상태공간에서 Q-function을 신경망으로 근사 | P01, P03 |
| Policy Gradient | 정책 자체를 직접 최적화 | P01 |
| Actor-Critic | 정책 선택과 가치 평가를 결합 | P01, P03 |
| DRL Verification | 안전성·강건성 명세를 만족하는지 검토 | P05 |

### 2.1 핵심 수식 또는 알고리즘 쉬운 설명

아래 수식은 원문 수식의 직접 인용이 아니라, 각 논문의 핵심 개념을 보고서에서 설명하기 위한 대표 수식과 지표다. 최종 제출본에서 원문 수식으로 인용할 경우 논문 원문 쪽/절 번호를 추가 확인한다.

| ID | 핵심 수식/알고리즘 | 쉬운 설명 | 보안 평가 연결 |
|---|---|---|---|
| P01 | $Q(s,a)\leftarrow Q(s,a)+\alpha[r+\gamma\max_{a'}Q(s',a')-Q(s,a)]$ | 강화학습 에이전트는 행동 뒤 받은 보상으로 다음 선택 가치를 고친다. | DRL 기본 원리 |
| P02 | $J(\pi)=E[\sum_t \gamma^t r_t]$ | 자율주행/제어 DRL은 장기 보상 합이 커지는 정책을 찾는다. | safe policy evaluation |
| P03 | $R=TP-\lambda FP-\mu FN-\rho Cost$ | 사이버 방어 보상은 탐지 성공만 아니라 오탐, 미탐, 비용을 함께 반영해야 한다. | cyber defense reward design |
| P04 | $F1=2PR/(P+R)$ | IDS/IPS는 공격 탐지율과 오탐 관리가 동시에 중요하다. | RL-based IDS 평가 |
| P05 | $P_\pi(\varphi)\ge p$ | DRL 검증은 정책이 안전 속성 $\varphi$를 충분히 높은 확률로 만족하는지 확인한다. | policy verification |

## 3. 보안 이슈 30% 정리

DRL cyber defense의 핵심 공격면은 상태 관측, 보상 신호, 정책 업데이트, 자동 대응 action이다. 특히 reward manipulation은 agent가 학습 중 받는 점수를 왜곡해 실제 보안 목표와 다른 행동을 유도할 수 있다.

| 관점 | 관련 위협 | 평가 연결 |
|---|---|---|
| Confidentiality | 보안 로그와 state observation 노출 | 개인정보 미사용, synthetic state |
| Integrity | reward manipulation, state poisoning | observed reward와 true reward 비교 |
| Availability | 정상 이벤트 과잉 격리 | safety violation rate |
| Safety | 공격 이벤트 미대응 | Detection F1, violation rate |
| Accountability | 설명 불가능한 자동 대응 | seed/config/run log 보존 |

## 4. 논문 5편 요약

| 번호 | 논문 제목 | 핵심 기여 | W09 활용 |
|---:|---|---|---|
| P01 | A Brief Survey of Deep Reinforcement Learning | DRL 알고리즘 계열과 학습 원리 정리 | MDP, Q-learning, DQN 배경 |
| P02 | Deep Reinforcement Learning for Autonomous Driving: A Survey | 안전중요 자율 시스템에서 DRL 적용 난점 정리 | 자동 대응 안전성, sim-to-real gap |
| P03 | Deep Reinforcement Learning for Cyber Security | DRL 기반 사이버 방어 연구 분류 | cyber-defense 위협모형 |
| P04 | Cyber-security and reinforcement learning - A brief survey | IDS/IPS, IoT, IAM RL 연구와 평가 지표 정리 | Detection F1와 표준 지표 필요성 |
| P05 | Deep Reinforcement Learning Verification: A Survey | DRL verification taxonomy와 safety specification 정리 | safety violation, robustness 평가 |

## 5. 논문 5편 비교

P01은 원리, P02는 안전중요 자동화, P03/P04는 사이버보안 적용, P05는 검증을 담당한다. 다섯 편을 연결하면 “DRL policy를 어떻게 학습하는가”에서 “그 policy가 사이버보안 환경에서 안전한가”로 연구 질문이 확장된다.

## 6. Research Track

### 6.1 연구문제

RQ1. 사이버보안 환경에서 DRL 에이전트의 상태·행동·보상 설계는 방어 성능과 안전성에 어떤 영향을 미치는가?

RQ2. Reward manipulation은 DRL 기반 사이버 방어 에이전트의 정책을 어떻게 왜곡할 수 있는가?

RQ3. DRL 기반 자동 대응 시스템을 평가할 때 Detection F1, Safety Violation Rate, Policy Robustness를 어떻게 결합해야 하는가?

### 6.2 위협모형

| 항목 | 내용 |
|---|---|
| 대상 시스템 | DRL 기반 사이버 방어 에이전트 |
| 보호 자산 | 상태 관측값, 보상함수, 정책, 보안 로그, 대응 action |
| 공격자 | 외부 공격자, 내부자, 환경 조작자 |
| 공격자의 지식 | White-box / Gray-box / Black-box |
| 공격자의 능력 | alert 조작, reward 신호 왜곡, 로그 오염 |
| 공격 성공 조건 | 공격 미대응 또는 정상 이벤트 과잉 대응 정책 유도 |
| 제외 범위 | 실제 시스템 침해, 실제 네트워크 공격, 개인정보, 무단 스캔 |

### 6.3 평가방법

| 평가 항목 | 지표 | 측정 방법 |
|---|---|---|
| Defense Utility | Average Reward | true reward 기준 평균 보상 |
| Detection Performance | Detection F1 | 공격 이벤트에 대응 action을 선택했는지 계산 |
| Safety | Safety Violation Rate | 공격 방치 또는 정상 이벤트 과잉 격리 비율 |
| Reward Integrity | Observed Reward vs Average Reward | 학습 reward와 실제 목표 reward 비교 |
| Robustness | Policy Robustness, Perturbed F1 | alert 관측 교란 조건에서 평가 |
| Reproducibility | Seed/config/output completeness | CSV/JSON/run log 보존 |

### 6.4 재현성

| 항목 | 내용 |
|---|---|
| Seed | 42 |
| Script | `04_experiment/src/run_experiment.py` |
| Config | `04_experiment/configs/config.yaml` |
| Run log | `04_experiment/outputs/run_log.md` |
| Metrics | `04_experiment/outputs/metrics_summary.csv` |
| JSON | `04_experiment/outputs/results.json` |
| 실행 명령 | `python3 src/run_experiment.py --config configs/config.yaml` |

### 6.5 한계와 오픈문제

toy 실험은 실제 IDS/IPS 성능을 주장하지 않는다. 또한 tabular Q-learning으로 보상조작 효과를 설명했으므로, neural DRL policy의 검증이나 실제 운영망 배포 안전성은 후속 연구로 남긴다.

## 7. 실습 요약

| 조건 | Average Reward | Detection F1 | Safety Violation Rate | Policy Robustness | 해석 |
|---|---:|---:|---:|---:|---|
| Normal reward | 1.085250 | 0.840206 | 0.011667 | 0.838417 | 기준 보상은 탐지 성능과 안전성 균형이 좋았다. |
| Manipulated reward | 0.521167 | 0.617512 | 0.195000 | 0.325000 | 보상조작으로 실제 방어 utility와 안전성이 악화되었다. |
| Robust reward design | 0.910833 | 0.780952 | 0.000000 | 0.709583 | 안전 위반은 제거했지만 오탐 비용이 증가했다. |

## 8. AI 활용 기록 요약

| 도구 | 사용 목적 | 반영 위치 | 검증 방식 |
|---|---|---|---|
| Codex | 공통 지침 확인, 문서 보완, toy 실험 코드 작성, 실행 로그 반영 | W09 전체 산출물 | 로컬 PDF, config, run log, CSV/JSON 대조 |

## 9. 토론 질문

1. 보안 자동 대응에서 Detection F1과 Safety Violation Rate 중 어느 지표를 우선해야 하는가?
2. reward manipulation과 단순 reward misspecification을 어떻게 구분할 수 있는가?
3. toy simulation 결과를 실제 운영 환경 평가로 확장하려면 어떤 공개 benchmark가 필요한가?

## 10. 기말 논문 연결

| 논문 장 | 반영 가능 내용 |
|---|---|
| 서론 | AI 기반 자동 방어 시스템의 필요성과 위험 |
| 관련연구 | DRL survey, cyber-security RL survey, DRL verification |
| 연구문제 | reward manipulation과 safe cyber-defense policy |
| 연구방법 | toy environment 기반 위협모형 및 평가설계 |
| 분석/실험 | reward stability, safety violation, detection score 비교 |
| 보안적 함의 | 무결성, 가용성, 안전성, 책임성 관점 |
| 결론 | 안전한 DRL 보안 에이전트 평가체계 제안 |

## 11. 참고문헌 검증표

| 번호 | 문헌 | DOI/URL | 상태 |
|---:|---|---|---|
| 1 | Arulkumaran et al., 2017 | https://doi.org/10.1109/MSP.2017.2743240 | 확인 |
| 2 | Kiran et al., 2022 | https://doi.org/10.1109/TITS.2021.3054625 | 확인 |
| 3 | Nguyen and Reddi, 2023 | https://doi.org/10.1109/TNNLS.2021.3121870 | 확인 |
| 4 | Adawadkar and Kulkarni, 2022 | https://doi.org/10.1016/j.engappai.2022.105116 | 확인 |
| 5 | Landers and Doryab, 2023 | https://doi.org/10.1145/3596444 | 확인 |

## 12. 자기 점검

| 항목 | 상태 |
|---|---|
| 논문 5편 요약 | 완료 |
| 논문 비교표 | 완료 |
| AI 원리 70% | 완료 |
| 보안 이슈 30% | 완료 |
| Research Track | 완료 |
| 실험 코드와 결과 | 완료 |
| 제출용 Markdown/HTML | 완료 |
| 발표자료 패키지 | 완료 |
| AI 활용 고지 | 완료 |
| 실제 공격 자동화 제외 | 준수 |
