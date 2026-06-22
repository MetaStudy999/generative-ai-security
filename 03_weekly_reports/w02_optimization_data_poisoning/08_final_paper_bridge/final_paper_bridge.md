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

## 4. KCI/SCI 전환 메모

| 구분 | 내용 |
|---|---|
| KCI형 추천 제목 | 학습 데이터 오염과 백도어 공격 평가를 위한 다중지표 프레임워크 연구 |
| SCI형 추천 제목 | A Multi-Metric Evaluation Framework for Training Data Poisoning and Backdoor Attacks: Separating Clean Performance, Attack Success Rate, and Reproducibility Evidence |
| 핵심 연구문제 | 오염률 증가에 따른 clean accuracy/macro F1 변화, toy backdoor 조건의 ASR 분리, 재현성 증거 기록 |
| 실험 기반 | scikit-learn digits + logistic regression 기반 안전한 toy protocol |
| 확장 방향 | 딥러닝 모델, self-supervised backdoor, federated poisoning, LLM/RAG 데이터 오염, MLOps 공급망 |
| 제출 전 보강 | 국내 참고문헌 3편 이상, P04 판본 확인, ACM Article 번호 확인, PDF 저작권 위험 처리 |

## 5. 참고문헌 검증 반영

- P02는 ACM Computing Surveys 최종판 DOI `10.1145/3578938`을 우선 인용한다.
- P04는 DOI `10.1145/3585385`의 ACM Computing Surveys 논문으로 확인했으나, 강의계획서 지정 제목 "Training Data Poisoning Attacks and Defenses: A Systematic Review"와 현재 로컬 PDF "Wild Patterns Reloaded"의 동일 여부는 최종 확인 필요하다.
- 실험 수치는 `04_experiment/outputs/metrics_summary.csv`, `results.json`, `run_log.md` 기준으로만 사용한다.
