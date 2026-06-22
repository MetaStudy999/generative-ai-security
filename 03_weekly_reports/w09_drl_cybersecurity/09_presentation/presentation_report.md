# W09 발표용 보고서

## 1. 발표 메타정보

| 항목 | 내용 |
|---|---|
| 주차 | W09 |
| 주제 | 심층강화학습(DRL) & 사이버보안 적용·보상조작 |
| 발표 시간 | 8-10분 |
| 핵심 메시지 | DRL cyber-defense에서 reward가 흔들리면 높은 점수 뒤에 안전하지 않은 정책이 숨어 있을 수 있다. |
| 실험 근거 | `04_experiment/outputs/run_log.md` |

## 2. 한 문장 요약과 발표 흐름

DRL 기반 사이버 방어 에이전트는 상태·행동·보상 설계에 따라 성능과 안전성이 크게 달라지며, reward manipulation은 실제 보안 목표를 훼손할 수 있다.

발표 흐름:

1. DRL 원리: state-action-reward-policy
2. 사이버보안 적용: cyber-defense agent
3. 보상조작 위협: reward hacking과 unsafe response
4. toy 실험: normal/manipulated/robust reward 비교
5. 기말논문 연결: 안전성 평가 프레임워크

## 3. 논문 5편의 발표 역할

| ID | 발표 역할 |
|---|---|
| P01 | DRL 알고리즘 원리와 MDP 배경 |
| P02 | 안전중요 자동화와 validation 필요성 |
| P03 | DRL cyber defense 적용 영역 |
| P04 | IDS/IPS, IoT, IAM 평가 지표 |
| P05 | DRL verification과 safety specification |

## 4. AI 원리 70%와 보안 이슈 30%

AI 원리는 MDP, Q-function, DQN, policy gradient, actor-critic, verification을 중심으로 설명한다. 보안 이슈는 reward manipulation, state observation manipulation, false positive/false negative automated response를 중심으로 설명한다.

## 5. 실습/실험 실행 상태와 결과 근거

| 조건 | Average Reward | Detection F1 | Safety Violation Rate | Policy Robustness |
|---|---:|---:|---:|---:|
| Normal reward | 1.085250 | 0.840206 | 0.011667 | 0.838417 |
| Manipulated reward | 0.521167 | 0.617512 | 0.195000 | 0.325000 |
| Robust reward design | 0.910833 | 0.780952 | 0.000000 | 0.709583 |

해석: manipulated reward는 observed reward를 높게 보이게 만들 수 있지만 true security objective 기준 성능과 안전성을 악화시켰다.

## 6. 기말논문 연결 지점

기말논문 후보는 “DRL 기반 사이버 방어 에이전트의 보상조작 위협과 안전성 평가 프레임워크”이다. W09의 실험과 표는 reward integrity, safety-aware metric, reproducible evaluation package로 이어진다.

## 7. 예상 질문과 답변

| 질문 | 답변 요지 |
|---|---|
| 왜 deep RL이 아니라 tabular Q-learning인가? | 목적은 고성능 DRL 구현이 아니라 reward manipulation 효과를 안전하고 재현 가능하게 설명하는 것이다. |
| Robust reward가 Average Reward는 기준보다 낮은데 더 좋은가? | 안전 위반을 0으로 낮추는 대신 false positive 비용을 감수한다. 운영 목표에 따라 trade-off를 선택해야 한다. |
| 실제 네트워크에 적용할 수 있는가? | 직접 일반화할 수 없다. 실제 적용 전 공개 benchmark, 로그 익명화, formal/simulation validation이 필요하다. |
