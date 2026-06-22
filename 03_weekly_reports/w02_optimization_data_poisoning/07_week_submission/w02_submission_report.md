# W02 제출용 보고서

## 표지

| 항목 | 내용 |
|---|---|
| 주차 | W02 |
| 보고서 제목 | 대규모 최적화 & 데이터 오염 위협 |
| 과목 범위 | AI 보안 |
| 작성일 | 2026-06-22 |
| 문서 상태 | 제출용 통합본 |
| 관련 산출물 위치 | `03_weekly_reports/w02_optimization_data_poisoning/` |

## 초록

본 보고서는 대규모 최적화와 데이터 오염 위협을 연결하여, 학습 데이터가 모델의 최적화 경로와 최종 보안성에 미치는 영향을 분석한다. AI 원리 측면에서는 stochastic gradient descent, 일반화, 효율적 학습, 모델 압축과 경량화를 정리하고, 보안 측면에서는 label-flipping poisoning, training data manipulation, backdoor attack, clean accuracy와 ASR의 차이를 설명한다. 다섯 편의 문헌을 비교하여 최적화 원리 문헌과 poisoning/backdoor 보안 문헌의 역할을 분리했고, scikit-learn digits 기반 Docker toy experiment 설계를 통해 clean baseline, label-flip, toy backdoor 조건을 재현 가능하게 기록했다. 결론적으로 W02는 기말 논문의 “학습 데이터 오염과 backdoor 평가를 위한 다중지표 프레임워크”로 발전 가능하다.

**키워드:** 대규모 최적화, SGD, 데이터 오염, poisoning, backdoor, ASR, 재현성

## 1. 서론

머신러닝 모델은 데이터와 라벨을 이용해 손실함수를 최소화한다. 따라서 데이터가 오염되면 단순히 입력 하나가 잘못되는 것이 아니라 학습 목적함수와 gradient 방향이 달라진다. W02의 핵심 질문은 “학습 데이터 오염이 모델의 정상 성능과 공격 조건 성능을 어떻게 다르게 만드는가”이다.

## 2. AI 원리

대규모 최적화에서는 전체 데이터의 gradient를 매번 계산하기 어렵기 때문에 stochastic gradient와 mini-batch 학습이 중요하다. 이 방식은 확장성은 높지만 데이터 품질에 민감하다. 또한 효율적 딥러닝은 모델을 작고 빠르게 만들지만, 보안 평가에서는 정확도뿐 아니라 탐지 비용, 재학습 비용, backdoor 잔존 가능성까지 함께 봐야 한다.

## 3. 보안 이슈

Data poisoning은 학습 데이터를 조작해 모델 학습 결과를 바꾸는 공격이다. Label-flipping은 라벨을 변경하는 단순한 오염이고, backdoor는 trigger가 있는 입력에서만 공격자 목표 행동을 유발하는 은닉 공격이다. W02 평가에서는 clean accuracy와 ASR을 반드시 분리한다.

## 4. 문헌 요약

| ID | 문헌 | 활용 |
|---|---|---|
| P01 | Optimization Methods for Large-Scale Machine Learning | 최적화와 SGD 배경 |
| P02 | Efficient Deep Learning | 효율성, 압축, 비용 지표 |
| P03 | A Comprehensive Survey on Poisoning Attacks and Countermeasures in Machine Learning | poisoning taxonomy |
| P04 | Wild Patterns Reloaded | training data poisoning threat model |
| P05 | A survey of backdoor attacks and defences | backdoor, ASR, detection/removal |

## 5. Research Track

| 항목 | 내용 |
|---|---|
| 연구문제 | 오염률과 공격 유형에 따라 clean accuracy, macro F1, ASR이 어떻게 변하는가 |
| 대상 시스템 | 지도학습 기반 분류 모델 |
| 위협 | label-flipping poisoning, toy backdoor trigger |
| 평가 지표 | clean accuracy, macro F1, ASR, stealthiness, reproducibility |
| 재현성 | Docker, pyproject.toml/uv sync, config, seed, outputs 로그 |
| 제외 범위 | 실제 개인정보, 실제 서비스, 무단 API, 운영 시스템 공격 |

## 6. 실습 설계

실습 코드는 `04_experiment/src/run_experiment.py`에 작성했다. Docker 환경에서 `python src/run_experiment.py --config configs/config.yaml`로 실행했고, 결과는 `04_experiment/outputs/`에 저장했다.

| 조건 | 오염률 | Clean Accuracy | Macro F1 | ASR |
|---|---:|---:|---:|---:|
| Clean baseline | 0% | 0.981481 | 0.981443 | 해당 없음 |
| Label-flip | 5% | 0.918519 | 0.918457 | 해당 없음 |
| Label-flip | 10% | 0.877778 | 0.877582 | 해당 없음 |
| Label-flip | 20% | 0.818519 | 0.818134 | 해당 없음 |
| Toy backdoor | 5% | 0.970370 | 0.970359 | 0.987654 |

## 7. 기말논문 연결

추천 주제는 “학습 데이터 오염과 backdoor 평가를 위한 다중지표 프레임워크”이다. 기여 후보는 clean accuracy, ASR, stealthiness, detection rate, efficiency cost, reproducibility evidence를 함께 기록하는 평가표다.

## 8. AI 활용 고지

Codex를 사용해 문헌 요약, 이론 정리, 코드 작성, Docker 실행 검증, 보고서 구조화, 발표자료 작성을 수행했다. DOI/URL은 확인 가능한 근거를 기록했고, 정량값은 Docker 실행 로그 기준으로 반영했다. 상세 기록은 `05_ai_worklog/`에 있다.

## 9. 참고문헌

1. Léon Bottou, Frank E. Curtis, Jorge Nocedal, “Optimization Methods for Large-Scale Machine Learning,” SIAM Review, 2018. DOI: `10.1137/16M1080173`.
2. Gaurav Menghani, “Efficient Deep Learning: A Survey on Making Deep Learning Models Smaller, Faster, and Better,” arXiv: `2106.08962`.
3. Zhiyi Tian et al., “A Comprehensive Survey on Poisoning Attacks and Countermeasures in Machine Learning,” ACM Computing Surveys. DOI: `10.1145/3551636`.
4. Antonio Emanuele Cinà et al., “Wild Patterns Reloaded: A Survey of Machine Learning Security against Training Data Poisoning,” arXiv: `2205.01992`.
5. Ling-Xin Jin et al., “A survey of backdoor attacks and defences: From deep neural networks to large language models,” Journal of Electronic Science and Technology, 2025. DOI: `10.1016/j.jnlest.2025.100326`.

## 10. 제출 전 점검표

| 점검 항목 | 상태 |
|---|---|
| 논문 요약 5편 | 완료 |
| 논문 비교표 | 완료 |
| AI 원리/보안 이슈 | 완료 |
| Research Track | 완료 |
| 실험 코드 | 완료 |
| 실험 결과 | 완료 |
| AI 활용 고지 | 완료 |
| 발표자료 | 완료 |
