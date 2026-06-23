# W02 발표 1페이지 요약

## 핵심 메시지

학습은 데이터가 만드는 손실함수를 따라 움직인다. 데이터가 오염되면 gradient와 decision boundary가 바뀌고, 정상 성능과 공격 조건 성능이 달라질 수 있다.

## AI 원리 70%

| 원리 | 의미 | 보안 연결 |
|---|---|---|
| 대규모 최적화 | 손실함수를 최소화하는 파라미터 탐색 | 데이터 조작이 목적함수를 바꿈 |
| SGD | 일부 샘플로 gradient 추정 | 오염 샘플이 update 방향에 영향 |
| 일반화 | 새 데이터에서 성능 유지 | clean과 공격 조건 성능 분리 |
| 효율적 학습 | 비용, 속도, 메모리 절감 | 방어 비용과 재학습 가능성 |

## 보안 이슈 30%

| 위협 | 설명 | 지표 |
|---|---|---|
| Label-flipping | 라벨 변경으로 학습 왜곡 | accuracy drop |
| Poisoning | 학습 데이터 조작 | clean accuracy, macro F1 |
| Backdoor | trigger 조건부 오분류 | ASR |
| Provenance failure | 오염 출처 추적 실패 | 로그, 데이터 이력 |

## 논문 5편

P01은 최적화, P02는 효율성, P03은 poisoning taxonomy, P04는 training data poisoning threat model, P05는 backdoor와 ASR 평가를 제공한다.

## 기말논문 연결

추천 주제: 학습 데이터 오염과 backdoor 평가를 위한 다중지표 프레임워크

핵심 지표: clean accuracy, macro F1, ASR, stealthiness, detection rate, efficiency cost, reproducibility evidence

<!-- formula-visual-handout:start -->
## 수식·그래프·그림 보강 요약

| 항목 | 반영 내용 |
|---|---|
| 핵심 수식 | ERM, Poisoned Empirical Risk, SGD Update, Accuracy Drop와 ASR |
| 그래프 | `assets/charts/w02_metrics_chart.png` (`metrics_summary.csv` 기반) |
| 다이어그램 | `assets/diagrams/w02_pipeline_diagram.svg` (training-data poisoning evaluation flow) |
| 기호 정의 | 통합보고서와 발표 슬라이드의 수식 블록에 포함 |
| 주의사항 | toy backdoor는 공개 toy 데이터 기반 안전 실습이며 실제 시스템 악용 절차로 일반화하지 않는다. |
<!-- formula-visual-handout:end -->
