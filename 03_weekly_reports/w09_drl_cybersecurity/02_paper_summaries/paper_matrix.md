# W09 논문 5편 비교표

| 논문 | 연구문제 | 핵심 방법 | 데이터/실험 | 보안 위협 | 평가 지표 | 한계 | 내 논문 활용 |
|---|---|---|---|---|---|---|---|
| P01 | DRL 알고리즘 계열과 학습 원리 정리 | DRL survey, value/policy/actor-critic 분류 | 문헌조사 중심 | 보상·상태 관측이 정책을 왜곡할 가능성 | return, value, policy 성능 | 사이버보안 직접 사례는 제한적 | MDP, Q-learning, DQN 이론 배경 |
| P02 | 안전중요 자율 시스템에서 DRL 적용 가능성 | 자율주행 DRL survey | simulator, validation, safe RL 논의 | 잘못된 자동 행동과 sim-to-real gap | safety, validation, deployment risk | 자율주행 도메인 중심 | 자동 사이버 대응의 안전성 유추 |
| P03 | DRL을 cyber defense에 적용하는 방식 | cyber security DRL survey | CPS, IDS, game-theoretic defense 문헌 | 상태 조작, 보상 왜곡, 적응형 공격 | detection, defense utility, robustness | 표준 benchmark 비교 어려움 | W09 핵심 관련연구 |
| P04 | RL 기반 IDS/IPS, IoT, IAM 연구 현황 | systematic/brief survey | NSL-KDD, CICIDS, AWID 등 문헌상 데이터셋 | IDS 오탐·미탐, IoT/IAM 보안 | detection rate, precision, accuracy | IAM 연구와 표준 지표 부족 | Detection F1와 평가표 근거 |
| P05 | DRL 정책을 어떻게 검증할 것인가 | verification survey, taxonomy | verification tasks/environments | 안전 명세 위반, stochastic policy 실패 | safety, robustness, reachability | 실제 cyber-defense 실험은 별도 필요 | safety violation과 robustness 지표 근거 |

## 종합 비교

### 1. 공통적으로 다루는 문제

다섯 편은 모두 DRL을 순차 의사결정 시스템으로 보고, 상태·행동·보상·정책의 정의가 성능과 안전성을 좌우한다고 본다. W09에서는 이를 cyber-defense agent의 alert state, response action, reward signal로 변환했다.

### 2. 논문 간 차이점

P01은 이론, P02는 안전중요 자동화, P03/P04는 사이버보안 적용, P05는 검증을 담당한다. 따라서 한 논문만으로 W09를 완성하기보다 `원리 -> 적용 -> 평가 -> 검증`의 사슬로 묶는 것이 적절하다.

### 3. 아직 해결되지 않은 문제

DRL cyber-defense 연구는 실제 운영 로그와 안전한 공개 benchmark 사이의 간극이 크다. 또한 보상함수 설계가 공격자에게 조작되거나 현실 목표를 잘못 대변할 때, 높은 reward가 높은 보안성을 뜻하지 않을 수 있다.

### 4. 기말 논문 주제로 발전 가능한 연결부

가장 직접적인 연결부는 “DRL 기반 사이버 방어 에이전트의 보상조작 위협과 안전성 평가 프레임워크”이다. W09 toy 실험은 이 주제를 위한 최소 재현 예시로 사용할 수 있다.
