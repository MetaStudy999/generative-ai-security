# W02 논문 5편 비교표

| 논문 | 연구문제 | 핵심 방법 | 데이터/실험 | 보안 위협 | 평가 지표 | 한계 | 내 논문 활용 |
|---|---|---|---|---|---|---|---|
| P01 | 대규모 ML에서 어떤 최적화 방법이 확장성과 수렴성을 보장하는가 | SGD, noise reduction, second-order method review | 이론/사례 중심 | 직접 보안 공격은 아님 | 수렴성, 계산 비용, 일반화 | poisoning 지표 직접 제공 없음 | 학습 데이터 조작이 목적함수와 gradient에 미치는 영향 설명 |
| P02 | 딥러닝 모델을 더 작고 빠르고 효율적으로 만들려면 무엇을 고려해야 하는가 | 효율적 모델링, 압축, 학습/시스템/하드웨어 survey | 문헌조사, 실무 가이드 | 효율화가 방어 비용과 검증 범위에 영향 | 정확도, latency, memory, FLOPs, cost | poisoning/backdoor 전용 문헌은 아님 | 방어 평가에 비용·속도·배포 가능성 추가 |
| P03 | poisoning 공격과 대응책을 어떻게 분류할 수 있는가 | 공격/방어 taxonomy | survey | poisoning, backdoor, federated poisoning | accuracy drop, ASR, detection, robustness | 개별 실험 재현은 별도 필요 | W02 위협모형과 평가방법의 중심 근거 |
| P04 | 훈련 데이터 poisoning 공격과 방어를 threat model 중심으로 어떻게 체계화할 수 있는가 | systematic survey, threat model 분석 | 100편 이상 문헌 검토 | targeted/untargeted poisoning, clean-label, backdoor | clean accuracy, attack success, stealthiness, detection | 도메인별 일반화 한계 | 데이터 생명주기 기반 방어 체크리스트 |
| P05 | DNN부터 LLM까지 backdoor 공격과 방어는 어떻게 발전했는가 | backdoor attack/detection/removal/LLM survey | survey | trigger 기반 조건부 오분류 | clean accuracy, ASR, trigger stealthiness, removal effect | LLM 환경 최신성 지속 갱신 필요 | clean accuracy-ASR 동시 평가 프레임 |

## 종합 비교

### 1. 공통적으로 다루는 문제

다섯 편은 모두 모델 성능을 단일 accuracy로만 설명하면 부족하다는 결론으로 연결된다. P01과 P02는 성능이 만들어지는 학습·효율화 원리를 제공하고, P03-P05는 학습 과정에 악의적 데이터가 들어올 때 모델 무결성과 안전성이 어떻게 손상되는지 보여준다.

### 2. 논문 간 차이점

P01은 최적화 이론, P02는 효율적 딥러닝, P03은 poisoning 전반 taxonomy, P04는 training data poisoning의 threat model, P05는 backdoor와 LLM 확장에 초점을 둔다. 따라서 W02 보고서는 “AI 원리 70%”에서 P01-P02를, “보안 이슈 30%”에서 P03-P05를 중심 문헌으로 배치한다.

### 3. 아직 해결되지 않은 문제

- Clean accuracy를 유지하면서 ASR이 높은 backdoor를 어떻게 안정적으로 탐지할 것인가.
- 모델 압축과 pruning이 backdoor 제거에 도움이 되는지, 혹은 trigger를 더 은닉시키는지 어떻게 평가할 것인가.
- Survey taxonomy를 실제 제출 가능한 toy experiment와 어떻게 윤리적으로 연결할 것인가.
- DOI, 판본, 로컬 PDF 제목이 다른 경우 참고문헌 검증 책임을 어떻게 문서화할 것인가.

### 4. 기말 논문 주제로 발전 가능한 연결부

가장 자연스러운 기말 주제는 “학습 데이터 오염과 backdoor 평가를 위한 다중지표 프레임워크”이다. 핵심 기여는 오염률, clean accuracy, ASR, stealthiness, detection rate, 재현성 증거, 방어 비용을 한 표에서 관리하는 평가 프로토콜을 제안하는 것이다.
