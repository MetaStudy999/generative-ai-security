# 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 논문 제목 | Deep Reinforcement Learning: A Brief Survey |
| 로컬 PDF 제목 | A Brief Survey of Deep Reinforcement Learning |
| 저자 | Kai Arulkumaran; Marc Peter Deisenroth; Miles Brundage; Anil Anthony Bharath |
| 학술지/학회 | IEEE Signal Processing Magazine, Vol. 34, No. 6, pp. 26-38 |
| 연도 | 2017 |
| DOI/URL | https://doi.org/10.1109/MSP.2017.2743240 |
| PDF 파일명 | 01_Arulkumaran_et_al_2017_Deep_Reinforcement_Learning_Survey.pdf |
| 검증 상태 | 부분 검증: DOI/Crossref 기준 공식 제목은 `Deep Reinforcement Learning: A Brief Survey`, 로컬 PDF는 arXiv extended version |

## 2. 한 문장 요약

> 이 논문은 DRL이 고차원 관측에서 순차 의사결정을 학습하는 문제를 value-based, policy-based, actor-critic 계열로 정리하며, 보상 기반 자율 에이전트를 보안 평가 대상으로 모델링할 이론적 기반을 제공한다.

## 3. 연구문제

이 문헌의 핵심 질문은 딥러닝의 표현학습 능력이 강화학습의 상태-행동 가치 추정과 정책 학습을 어떻게 확장하는가이다. W09에서는 이 질문을 사이버 방어 에이전트의 상태, 행동, 보상 설계 문제로 옮겨 읽는다.

## 4. 핵심 개념

| 개념 | 설명 | W09 연결 |
|---|---|---|
| MDP | 상태, 행동, 전이, 보상, 할인율로 순차 의사결정을 표현한다. | toy cyber-defense 환경 정의 |
| Q-function | 특정 상태에서 특정 행동을 택했을 때의 기대 누적 보상이다. | tabular Q-learning 실험 |
| DQN | Q-function을 신경망으로 근사해 고차원 입력을 다룬다. | DRL 사이버 방어 확장 가능성 |
| Policy Gradient | 정책 자체를 직접 최적화한다. | 연속 행동/확률 정책 방어 모델 |
| Actor-Critic | 정책을 고르는 actor와 가치를 평가하는 critic을 결합한다. | 자동 대응 정책의 안정성 논의 |

## 5. 방법론

Survey 형식으로 DRL 알고리즘을 value function, policy search, actor-critic 흐름으로 분류한다. 또한 exploration/exploitation, sample complexity, function approximation의 어려움을 설명해 DRL 실험 설계에서 왜 seed, 환경, 보상 함수를 고정해야 하는지 보여준다.

### 5.1 핵심 수식 또는 알고리즘 설명

| 항목 | 내용 |
|---|---|
| 수식/알고리즘 이름 | MDP와 Bellman Expectation Equation |
| 원문 위치 | 논문 세부 절/쪽/그림/알고리즘 번호 확인 필요. 로컬 DOI/URL 점검표로 문헌 대응만 확인. |
| 작성 형식 | Markdown + LaTeX math |
| 검산 도구 | 사용 안 함 |
| 수식 또는 절차 | 표준 정의식 / 원문 직접 인용 아님.<br>$$V^\pi(s)=\mathbb{E}_\pi\left[r_t+\gamma V^\pi(s_{t+1})\mid s_t=s\right]$$ |
| 기호·입력·출력 | \(s\): state, \(a\): action, \(r_t\): reward, \(\gamma\): discount factor, \(\pi\): policy |
| 직관적 의미 | MDP와 Bellman Expectation Equation는 DRL 사이버보안 평가에서 핵심 원리나 평가 지표를 정량적으로 해석하기 위한 표준식이다. |
| 보안 관점 해석 | DRL 사이버보안 평가에서는 정상 성능과 보안 실패 조건을 분리해 보아야 한다. 이 항목은 공격·방어 원리 또는 운영 통제의 평가 기준을 명시하되, 실제 공격 절차나 무단 적용 단계는 포함하지 않는다. |
| 평가 지표와 연결 | return, success rate, safety violation rate |
| 한계와 가정 | 표준 정의식 / 원문 직접 인용 아님. 논문별 변형, 정확한 수식 번호, 실험 설정은 원문 PDF에서 확인 필요다. |
| 기말 논문 반영 여부 | 반영 |

## 6. 주요 결과

논문은 DRL의 강점이 raw sensory input, 게임, 로봇, 제어 문제처럼 상태공간이 큰 영역에서 드러난다고 정리한다. 동시에 trial-and-error 학습, 장기 보상, 함수근사 안정성 문제가 남아 있어 안전성·검증이 필요하다는 연결고리를 만든다.

## 7. 보안 관점 분석

DRL 보안에서는 보상과 상태 관측이 공격면이 된다. 공격자가 관측값이나 보상 신호를 왜곡하면 에이전트는 높은 보상을 받는다고 믿지만 실제 방어 목표와 어긋난 정책을 배울 수 있다.

## 8. 한계와 오픈문제

일반 DRL survey이므로 사이버보안 데이터셋이나 공격자 모형은 직접 다루지 않는다. W09에서는 P03/P04의 cyber-defense 문헌과 결합해 보안 평가 항목을 보완해야 한다. 또한 로컬 PDF는 arXiv extended version이므로, 제출 참고문헌에는 IEEE 출판판 제목, 권호, 페이지, DOI를 우선 사용한다.

## 9. 기말 논문에 반영할 부분

기말 논문의 배경 이론 장에서 MDP, Q-learning, DQN, policy gradient, actor-critic을 정의하는 근거로 활용한다. 실험 장에서는 보상조작이 Q-learning 정책에 미치는 영향을 설명하는 이론적 연결로 반영한다.
