# W09 기말논문 연결표

## 1. 이번 주차에서 얻은 연구 주제 후보

| 번호 | 주제 후보 | 대상 시스템 | 보안 위협 | 방법론 | 기여 가능성 |
|---:|---|---|---|---|---|
| 1 | DRL 기반 사이버 방어 에이전트의 보상조작 위협모형 연구 | DRL cyber defense | Reward manipulation | 위협모형/평가체계 | 높음 |
| 2 | 사이버보안 DRL 에이전트의 상태·행동·보상 설계 기준 연구 | DRL agent | 상태 조작·보상 왜곡 | 프레임워크 설계 | 높음 |
| 3 | 자동화된 AI 보안 대응 시스템의 안전성 평가 체크리스트 연구 | Autonomous defense | Unsafe action | 체크리스트/사례분석 | 보통 |

## 2. 기말 논문에 반영할 내용

| 논문 장 | 반영 가능 내용 |
|---|---|
| 서론 | AI 기반 자동 방어 시스템의 필요성과 위험 |
| 관련연구 | DRL survey, cyber security RL survey, DRL verification |
| 연구문제 | reward manipulation과 safe cyber-defense policy |
| 연구방법 | toy environment 기반 위협모형 및 평가설계 |
| 분석/실험 | reward stability, safety violation, detection score 비교 |
| 보안적 함의 | 무결성, 가용성, 안전성, 책임성 관점 |
| 결론 | 안전한 DRL 보안 에이전트 평가체계 제안 |

## 3. W09 실험에서 가져갈 기여 후보

| 기여 후보 | 설명 |
|---|---|
| Reward integrity 관점 | observed reward와 true reward를 분리해 보상조작을 탐지한다. |
| Safety-aware metric | Detection F1만이 아니라 Safety Violation Rate를 함께 본다. |
| Robustness check | alert perturbation 조건에서 같은 정책을 평가한다. |
| Reproducible package | seed, config, script, CSV, JSON, run log를 함께 보존한다. |
