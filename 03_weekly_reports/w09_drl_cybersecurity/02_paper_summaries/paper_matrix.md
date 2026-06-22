# W09 논문 5편 비교표

| 논문 | 연구문제 | 핵심 방법 | 데이터/실험 | AI 원리 기여 | 보안 위협 연결 | 평가 지표 | 한계 | 내 논문 활용 |
|---|---|---|---|---|---|---|---|---|
| P01 | DRL 알고리즘 계열과 학습 원리는 어떻게 정리되는가 | value-based, policy-based, actor-critic, model-based/model-free DRL survey | 문헌조사 중심 | MDP, Q-learning, DQN, policy gradient, actor-critic 기본 원리 | 보상·상태 관측이 정책을 왜곡할 가능성 | return, value, policy performance | 사이버보안 직접 사례는 제한적, 로컬 PDF는 arXiv extended version | DRL 이론 배경과 수식 설명 |
| P02 | 안전중요 자율 시스템에서 DRL을 어떻게 검증·배포할 수 있는가 | autonomous driving DRL survey, simulation, validation, safe RL 논의 | simulator, autonomous driving task 문헌 | 안전중요 자동화와 sim-to-real gap | 잘못된 자동 action, unsafe policy, validation gap | safety, collision rate, validation score, deployment risk | 자율주행 도메인 중심, 로컬 PDF는 arXiv v2 | 자동 사이버 대응의 안전성 유추 |
| P03 | DRL은 cyber security 문제에 어떻게 적용되는가 | cyber-defense DRL survey, IDS, CPS, game-theoretic defense | 사이버보안 DRL 문헌조사 | DRL을 alert state, response action, defense policy로 연결 | state manipulation, reward manipulation, adaptive attacker | detection performance, defense utility, robustness | 표준 benchmark와 실제 운영로그 간 간극, 강의계획서 저자명 차이 확인 필요 | W09 핵심 관련연구 |
| P04 | RL 기반 cybersecurity 연구는 어떤 task와 지표를 사용하는가 | IDS/IPS, IoT, IAM 등 RL 적용 survey | NSL-KDD, CICIDS, AWID 등 문헌상 데이터셋 | RL 기반 탐지·대응 시스템 평가 | 오탐, 미탐, IoT/IAM 정책 실패 | detection rate, precision, recall, accuracy, F1 | IAM 연구와 표준 지표 부족, 강의계획서 저자명 차이 확인 필요 | Detection F1와 실험 평가표 근거 |
| P05 | DRL policy의 안전성과 강건성은 어떻게 검증할 수 있는가 | DRL verification taxonomy, safety specification, reachability/robustness analysis | verification tasks/environments 문헌 | 높은 reward와 안전성의 분리 | safety specification violation, stochastic policy failure | safety, robustness, reachability, policy verification | 실제 cyber-defense 실험은 별도 필요, 강의계획서 저자명 차이 확인 필요 | safety violation과 policy robustness 지표 근거 |

## 종합 비교

P01은 DRL 기본 원리 문헌이다. MDP, Q-learning, DQN, policy gradient, actor-critic을 정의해 W09의 state/action/reward 구조를 세우는 역할을 한다[1].

P02는 안전중요 자동화와 sim-to-real gap 문헌이다. 자율주행 문헌이지만, 자동 사이버 대응에서도 시뮬레이션에서 좋은 정책이 실제 운영망에서 안전하다고 단정할 수 없다는 근거로 사용한다[2].

P03/P04는 cyber defense와 IDS/IPS 적용 문헌이다. P03은 DRL을 cyber-defense policy로 연결하고, P04는 RL 기반 IDS/IPS, IoT, IAM 연구에서 detection rate, precision, recall, F1 같은 표준 지표가 필요함을 보여준다[3][4].

P05는 DRL verification과 safety specification 문헌이다. W09에서는 높은 reward가 safety specification 만족을 뜻하지 않는다는 점을 강조하는 근거로 사용한다[5].

W09의 핵심 연결부는 "높은 observed reward가 높은 실제 보안성을 의미하지 않는다"는 점이다. 따라서 보고서와 실험은 true reward, observed reward, detection F1, safety violation rate, policy robustness를 분리해 기록한다.

## Reward Manipulation과 Reward Misspecification 구분

| 개념 | 정의 | W09 예시 | 평가 연결 |
|---|---|---|---|
| Reward manipulation | 공격자 또는 환경 조작자가 보상 신호를 의도적으로 왜곡하는 경우 | 공격 이벤트 미대응 패널티를 약화하고 자동 격리 비용을 과장한 manipulated reward 조건 | observed reward와 true reward 차이, safety violation rate 증가 |
| Reward misspecification | 설계자가 실제 보안 목표를 잘못 반영한 보상함수 설계 오류 | 탐지 성공만 보상하고 정상 이벤트 과잉 격리 비용을 충분히 반영하지 않는 설계 | F1은 높아도 availability/safety 비용 증가 |

## Toy 실험의 위치

W09 toy 실험은 실제 IDS/IPS나 실제 neural DRL policy가 아니라 tabular Q-learning 기반 평가 구조 설명용이다. 실험 환경은 synthetic cyber-defense state/action/reward로 제한되며, 실제 네트워크 공격, 실제 트래픽 수집, 개인정보, exploit 실행, 공격 자동화 절차를 포함하지 않는다.
