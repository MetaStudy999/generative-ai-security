# W02 발표용 보고서

## 1. 발표 메타정보

| 항목 | 내용 |
|---|---|
| 주차 | W02 |
| 주제 | 대규모 최적화 & 데이터 오염 위협 |
| 발표 시간 | 8-10분 |
| 권장 슬라이드 수 | 12-14장 |
| 핵심 메시지 | 데이터 오염은 학습 목적함수와 gradient를 바꾸며, backdoor 평가는 clean accuracy와 ASR을 분리해야 한다. |
| 발표 근거 | `06_report/final/integrated_report_final.md`, `04_experiment/outputs/run_log.md` |

## 2. 한 문장 요약

W02는 대규모 최적화와 효율적 학습 원리를 바탕으로, 학습 데이터 일부가 조작될 때 모델의 clean accuracy, macro F1, ASR, 재현성 주장이 어떻게 달라지는지를 toy 실험과 문헌 분석으로 설명한다.

## 3. 발표 흐름

| 순서 | 슬라이드 주제 | 핵심 내용 | 시간 |
|---:|---|---|---:|
| 1 | 표지 | W02 주제와 핵심 질문 | 0:30 |
| 2 | 왜 중요한가 | 학습 단계 위협은 최종 모델의 행동을 바꾼다 | 1:00 |
| 3 | AI 원리 | 대규모 최적화, SGD, 효율적 학습 | 2:00 |
| 4 | 보안 이슈 | label-flipping, poisoning, backdoor | 2:00 |
| 5 | 논문 비교 | 최적화/효율화 문헌과 poisoning/backdoor 문헌 연결 | 1:30 |
| 6 | 위협모형/평가 | clean accuracy, macro F1, ASR, 재현성 분리 | 1:30 |
| 7 | Toy 실험 | digits 기반 label-flip/backdoor 결과 | 1:30 |
| 8 | 기말논문 연결 | 데이터 오염 평가 프레임워크로 확장 | 0:45 |
| 9 | 결론/Q&A | 실행 로그와 한계를 함께 말하기 | 0:45 |

## 4. 논문 5편의 발표 역할

| ID | 논문 | 발표에서 맡는 역할 | 강조할 한계 |
|---|---|---|---|
| P01 | Optimization Methods for Large-Scale Machine Learning | 대규모 최적화와 SGD 원리 설명 | 보안 공격 문헌은 아니므로 poisoning 평가는 별도 연결 필요 |
| P02 | Efficient Deep Learning | 압축, 경량화, 비용-속도-품질 trade-off 설명 | P02/P04는 출판 판본 최종 대조 권장 |
| P03 | A Comprehensive Survey on Poisoning Attacks and Countermeasures in Machine Learning | poisoning 공격과 방어 taxonomy 제공 | survey 기반이므로 특정 실험 수치 일반화 주의 |
| P04 | Wild Patterns Reloaded | training data poisoning threat model과 방어 관점 | 로컬 PDF 제목과 출판 판본 대조 필요 |
| P05 | A survey of backdoor attacks and defences | clean accuracy와 ASR 분리의 근거 제공 | LLM backdoor까지 넓게 다루므로 W02 toy 실험은 축소 예시 |

## 5. AI 원리 설명

- 대규모 ML 학습은 손실함수를 최소화하는 파라미터를 찾는 최적화 문제다.
- SGD와 mini-batch 학습은 전체 데이터 대신 일부 샘플로 gradient를 추정해 확장성을 얻는다.
- 데이터나 라벨이 오염되면 empirical risk와 gradient 추정이 바뀌어 decision boundary가 이동할 수 있다.
- 효율적 학습과 모델 경량화는 방어 비용, 재학습 가능성, 탐지 지연시간과도 연결된다.

발표에서는 “poisoning은 테스트 입력 하나가 아니라 학습 목적함수 자체를 바꾸는 위협”이라는 문장으로 AI 원리와 보안 이슈를 연결한다.

## 6. 보안 이슈 설명

| 항목 | 발표 내용 |
|---|---|
| 보호 자산 | 학습 데이터, 라벨, 모델 파라미터, 검증셋, 실행 로그 |
| 공격자 능력 | 일부 라벨 조작, 오염 샘플 삽입, toy trigger 삽입 |
| 공격 경로 | 데이터 수집, 라벨링, 전처리, 학습, 검증 단계 |
| 방어자 가정 | 공개 toy 데이터, seed/config/log 보존, 실제 시스템 공격 제외 |
| 평가 지표 | Clean accuracy, macro F1, accuracy drop, ASR, stealthiness, reproducibility |

Clean accuracy가 높아도 ASR이 높으면 backdoor 관점에서는 실패한 모델일 수 있다. 이 분리를 발표의 중심축으로 둔다.

## 7. 실습/실험 결과

정량값은 `04_experiment/outputs/run_log.md` 기준이다. 이 실험은 scikit-learn digits 공개 데이터셋을 사용한 교육용 toy evaluation이며, 실제 운영 시스템이나 개인정보 데이터는 포함하지 않는다.

| 조건 | Poisoning Rate | Clean Accuracy | Macro F1 | ASR | 발표 해석 |
|---|---:|---:|---:|---:|---|
| Clean baseline | 0% | 0.981481 | 0.981443 | 해당 없음 | 기준 성능 |
| Label-flip | 5% | 0.918519 | 0.918457 | 해당 없음 | 약한 오염에서도 성능 저하 관찰 |
| Label-flip | 10% | 0.877778 | 0.877582 | 해당 없음 | 오염률 증가에 따른 추가 저하 |
| Label-flip | 20% | 0.818519 | 0.818134 | 해당 없음 | 학습 라벨 품질 저하의 영향 확대 |
| Toy backdoor | 5% | 0.970370 | 0.970359 | 0.987654 | 정상 성능을 유지하면서 trigger 조건에서 실패 |

주의: toy backdoor 결과는 안전한 축소 모형의 지표 분리 예시이며, 실제 공격 성능이나 실서비스 취약성으로 일반화하지 않는다.

## 8. 기말논문 연결

| 기말논문 장 | 발표에서 연결할 내용 |
|---|---|
| 서론 | 학습 데이터 오염이 AI 시스템 신뢰성을 흔드는 이유 |
| 관련연구 | 최적화, 효율학습, poisoning, backdoor survey 연결 |
| 연구문제 | 오염률, clean accuracy, ASR, 재현성 근거의 관계 |
| 연구방법 | 위협모형, 평가 프로토콜, Docker 실행 로그 기반 검증 |
| 분석/실험 | label-flip과 toy backdoor를 통한 지표 분리 예시 |
| 보안적 함의 | 무결성, 안전성, 책임성, 재현성 관점 |

## 9. 결론 메시지

1. 최적화는 데이터가 만드는 손실함수와 gradient를 따라 움직인다.
2. 데이터 오염은 학습 목적함수와 decision boundary를 바꿀 수 있다.
3. Backdoor 평가는 clean accuracy와 ASR을 반드시 분리해야 한다.
4. 제출 가능한 AI 보안 실습은 Docker, config, seed, CSV/JSON, run log를 함께 남겨야 한다.

## 10. 예상 질문과 답변

| 질문 | 답변 요지 | 근거 파일 |
|---|---|---|
| 왜 최적화 원리를 먼저 설명하는가? | poisoning은 학습 데이터와 라벨을 바꿔 gradient 추정과 손실함수를 흔드는 공격이므로 최적화 관점이 필요하다. | `03_theory_notes/ai_principle_70.md` |
| Clean accuracy가 높으면 안전한가? | 아니다. backdoor는 정상 입력에서는 높은 성능을 보이면서 trigger 조건에서 높은 ASR을 만들 수 있다. | `04_experiment/outputs/run_log.md` |
| 이 실습이 실제 공격 재현인가? | 아니다. 공개 digits 데이터셋에서 수행한 교육용 toy evaluation이며 실제 시스템, 개인정보, 무단 API는 제외한다. | `04_experiment/experiment_report.md` |
| 기말논문에는 어떻게 반영되는가? | 학습 데이터 오염과 backdoor 평가를 위한 다중지표 프레임워크의 근거 사례로 반영한다. | `08_final_paper_bridge/final_paper_bridge.md` |

## 11. 발표 전 점검

| 확인 | 점검 항목 |
|---|---|
| □ | 발표 수치가 `outputs/run_log.md`, `metrics_summary.csv`, `results.json`과 일치한다. |
| □ | toy 실험 결과를 실제 대규모 모델 공격 성능으로 일반화하지 않는다. |
| □ | P02/P04의 출판 판본 최종 대조 필요성을 숨기지 않는다. |
| □ | 예상 질문 3개 이상을 준비했다. |
