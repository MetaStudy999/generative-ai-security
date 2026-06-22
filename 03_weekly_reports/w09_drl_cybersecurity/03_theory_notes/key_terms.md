# 핵심 용어

| 용어 | 작업 정의 | W09에서의 쓰임 |
|---|---|---|
| Reinforcement Learning | agent가 environment와 상호작용하며 reward를 최대화하는 policy를 학습하는 방법 | DRL cyber-defense의 기본 틀 |
| Agent | state를 관측하고 action을 선택하는 주체 | 사이버 방어 에이전트 |
| Environment | action의 결과와 reward를 돌려주는 외부 세계 | synthetic cyber-defense simulator |
| State | 의사결정에 필요한 현재 관측 정보 | alert level, asset criticality, vulnerability |
| Action | agent가 선택할 수 있는 대응 | monitor, isolate, patch, escalate |
| Reward | 행동의 좋고 나쁨을 수치화한 학습 신호 | true reward, manipulated reward, robust reward |
| MDP | state, action, transition, reward, discount로 구성된 순차 의사결정 모델 | toy 실험의 모델링 기반 |
| Q-function | state-action pair의 기대 누적 보상 | tabular Q-learning 업데이트 |
| DQN | Q-function을 deep neural network로 근사하는 DRL 알고리즘 | 실제 DRL 확장 논의 |
| Policy Gradient | policy parameter를 직접 최적화하는 방법 | 확률적 자동 대응 정책 논의 |
| Actor-Critic | actor가 action을 고르고 critic이 value를 평가하는 구조 | DRL cyber-defense 확장 후보 |
| Exploration/Exploitation | 새로운 행동 탐색과 알려진 좋은 행동 활용의 균형 | 학습 안정성 |
| Reward Manipulation | reward signal이 공격자나 잘못된 계측에 의해 왜곡되는 위협 | W09 핵심 보안 이슈 |
| Reward Hacking | agent가 숫자 reward는 높이지만 실제 목표를 어기는 현상 | observed reward와 true reward 분리 |
| Safety Violation | 공격 방치 또는 정상 이벤트 과잉 대응처럼 안전 명세를 어긴 사건 | 주요 평가 지표 |
| Policy Robustness | 관측 교란 조건에서도 policy가 성능과 안전성을 유지하는 정도 | perturbed alert 평가 |
| DRL Verification | DRL policy가 safety/robustness specification을 만족하는지 검토하는 절차 | P05와 기말논문 연결 |
