# W09 1페이지 요약

## 주제

심층강화학습(DRL) & 사이버보안 적용·보상조작

## 핵심 메시지

DRL 기반 사이버 방어 에이전트는 reward가 흔들리면 높은 점수 뒤에 안전하지 않은 정책을 학습할 수 있다.

## AI 원리

| 개념 | 설명 |
|---|---|
| State | alert, 자산 중요도, 취약 여부 |
| Action | monitor, isolate, patch, escalate |
| Reward | 탐지 성공, 운영 비용, 안전 위반 |
| Policy | 상태별 대응 전략 |

## 보안 이슈

- Reward manipulation: 학습 보상 신호 왜곡
- State observation manipulation: alert/log 조작
- Unsafe automated response: 공격 방치 또는 정상 이벤트 과잉 격리
- Verification difficulty: stochastic environment에서 안전성 보증 어려움

## 실험 결과

| 조건 | Average Reward | Detection F1 | Safety Violation Rate | Policy Robustness |
|---|---:|---:|---:|---:|
| Normal reward | 1.085250 | 0.840206 | 0.011667 | 0.838417 |
| Manipulated reward | 0.521167 | 0.617512 | 0.195000 | 0.325000 |
| Robust reward design | 0.910833 | 0.780952 | 0.000000 | 0.709583 |

## 결론

Detection F1만으로 DRL 방어 정책을 평가하면 부족하다. true reward, observed reward, safety violation, policy robustness를 함께 기록해야 한다.

## 기말논문 연결

DRL 기반 사이버 방어 에이전트의 보상조작 위협과 안전성 평가 프레임워크.

<!-- formula-visual-handout:start -->
## 수식·그래프·그림 보강 요약

| 항목 | 반영 내용 |
|---|---|
| 핵심 수식 | MDP Tuple, Return, Bellman Equation, Reward Manipulation Proxy |
| 그래프 | `assets/charts/w09_metrics_chart.png` (`metrics_summary.csv` 기반) |
| 다이어그램 | `assets/diagrams/w09_pipeline_diagram.svg` (MDP security evaluation flow) |
| 기호 정의 | 통합보고서와 발표 슬라이드의 수식 블록에 포함 |
| 주의사항 | DRL 환경은 toy simulation이며 실제 네트워크 공격 자동화 절차를 제공하지 않는다. |
<!-- formula-visual-handout:end -->
