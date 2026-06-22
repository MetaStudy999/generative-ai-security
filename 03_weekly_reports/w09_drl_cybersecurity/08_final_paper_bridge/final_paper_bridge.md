# W09 기말논문 연결표

## 1. 추천 연구 주제

| 번호 | 주제 후보 | 대상 시스템 | 보안 위협 | 방법론 | 기여 가능성 |
|---:|---|---|---|---|---|
| 1 | DRL 기반 사이버 방어 에이전트의 보상조작 위협과 안전성 평가 프레임워크 연구 | DRL cyber-defense agent | Reward manipulation, unsafe response | 문헌분석 + synthetic Q-learning toy protocol | 높음 |
| 2 | 강화학습 기반 자동 보안 대응에서 보상함수 설계와 안전 위반율의 관계 분석 | automated cyber response | reward misspecification, over-isolation | synthetic simulation + safety metric | 높음 |
| 3 | 사이버보안 DRL 정책의 다중지표 평가 연구 | IDS/IPS DRL policy | state poisoning, reward manipulation | Detection F1/Safety/Robustness 통합 평가 | 보통 |

## 2. 추천 최종 제목

- 국문: DRL 기반 사이버 방어 에이전트의 보상조작 위협과 안전성 평가 프레임워크 연구
- 영문: A Safety Evaluation Framework for Reward Manipulation Threats in DRL-Based Cyber Defense Agents

## 3. 기말 논문에 반영할 내용

| 논문 장 | 반영 가능 내용 |
|---|---|
| 서론 | AI 기반 자동 방어 시스템의 필요성과 reward integrity 위험 |
| 관련연구 | DRL fundamentals, safety-critical automation, cyber-defense DRL, RL for cybersecurity, DRL verification |
| 연구문제 | reward manipulation과 safe cyber-defense policy |
| 연구방법 | synthetic state/action/reward 기반 위협모형 및 평가설계 |
| 분석/실험 | true reward, observed reward, Detection F1, Safety Violation Rate, Policy Robustness 비교 |
| 보안적 함의 | 무결성, 가용성, 안전성, 책임성, 재현성 관점 |
| 결론 | 안전한 DRL 보안 에이전트 평가체계 제안 |

## 4. W09 실험에서 가져갈 기여 후보

| 기여 후보 | 설명 |
|---|---|
| Reward integrity 관점 | observed reward와 true reward를 분리해 보상조작을 탐지한다. |
| Safety-aware metric | Detection F1만이 아니라 Safety Violation Rate를 함께 본다. |
| Robustness check | alert perturbation 조건에서 같은 정책을 평가한다. |
| Reproducible package | seed, config, script, CSV, JSON, run log를 함께 보존한다. |
| Literature audit | P03/P04/P05 저자명 차이처럼 강의계획서와 DOI/PDF 메타데이터 충돌을 검증표에 남긴다. |

## 5. KCI/SCI 전환 메모

KCI형 논문은 국문 문제의식과 평가 프레임워크를 중심으로 구성한다. 국내 참고문헌 3편 이상은 아직 확인 필요다.

SCI형 논문은 multi-metric safety evaluation framework를 중심으로 Background, Problem, Method, Results, Contribution, Implications 구조를 사용할 수 있다. 단, 현재 W09 실험은 tabular Q-learning과 synthetic state 기반이므로 실제 IDS/IPS 또는 neural DRL policy 성능으로 주장하지 않는다.
