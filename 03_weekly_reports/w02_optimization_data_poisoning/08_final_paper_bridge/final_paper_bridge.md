# W02 기말논문 연결표

## 1. 이번 주차에서 얻은 연구 주제 후보

| 번호 | 주제 후보 | 대상 시스템 | 보안 위협 | 방법론 | 기여 가능성 |
|---:|---|---|---|---|---|
| 1 | 학습 데이터 오염 공격이 ML 모델 성능과 신뢰성에 미치는 영향 분석 | 분류 모델 | Label-flipping / poisoning | 오염률별 toy 실험과 문헌 분석 | 높음 |
| 2 | Backdoor 공격의 clean accuracy와 ASR 간 괴리 분석 | 이미지 분류 모델 | Backdoor | trigger toy 실험과 지표 비교 | 높음 |
| 3 | Poisoning/backdoor 방어평가를 위한 다중지표 프레임워크 | ML 시스템 | 데이터 오염, trigger 공격 | 평가 프로토콜 설계 | 높음 |
| 4 | 모델 효율화가 backdoor 방어 비용과 탐지 가능성에 미치는 영향 | 경량 모델 | Backdoor 잔존/탐지 실패 | 문헌 분석과 압축 조건 실험 | 중간 |

## 2. 기말 논문에 반영할 내용

| 논문 장 | 반영 가능 내용 |
|---|---|
| 서론 | 학습 데이터 오염은 모델 학습 목적함수와 신뢰성을 흔드는 훈련 단계 위협 |
| 관련연구 | 대규모 최적화, 효율적 딥러닝, poisoning survey, backdoor survey |
| 연구문제 | 오염률, 공격 유형, ASR, clean accuracy의 관계 |
| 연구방법 | label-flipping 및 toy backdoor 평가 프로토콜 |
| 분석/실험 | clean accuracy, macro F1, ASR, stealthiness 비교 |
| 보안적 함의 | 무결성, 안전성, 책임성, 재현성 관점 |
| 결론 | 재현 가능한 데이터 오염 평가체계 제안 |

## 3. 추천 기말 주제

가장 적합한 주제는 “학습 데이터 오염과 backdoor 평가를 위한 다중지표 프레임워크”이다. 이 주제는 W02의 최적화 원리, poisoning taxonomy, backdoor 지표, Docker 실험 설계를 모두 활용할 수 있고, 이후 주차의 adversarial example, LLM security, RAG prompt injection, MLOps supply chain과도 연결하기 쉽다.
