# W14 One-page Handout

## 핵심 메시지

MLOps 공급망 보안은 모델 성능만으로 설명할 수 없다. 데이터, 모델, config, 로그, 모니터링, artifact inventory가 함께 남아야 운영형 AI 시스템의 재현성과 책임성을 말할 수 있다.

## AI 원리 70%

| 개념 | 요점 |
|---|---|
| MLOps | ML lifecycle을 운영 가능한 시스템으로 관리 |
| Data/model pipeline | 데이터와 모델 산출물의 출처·버전·config 추적 |
| Monitoring/drift | 운영 입력과 출력 분포 변화 감시 |
| AIOps | 로그와 metric을 이용한 incident detection/RCA |
| Edge deployment | 분산 배포에서 artifact/update 관리 중요 |

## 보안 이슈 30%

| 위협 | 통제항목 |
|---|---|
| Data poisoning | dataset hash, provenance |
| Model artifact tampering | model hash, registry control |
| Unsafe update | approval gate, rollback |
| Drift 미탐지 | drift score, monitoring |
| Audit gap | audit coverage, run log |

## W14 실험 결과

| 항목 | 값 |
|---|---:|
| Accuracy | 0.925000 |
| F1 | 0.923077 |
| Dataset hash | `sha256:b9e597bccdbde442` |
| Model hash match | true |
| Re-run consistency | true |
| Drift score | 0.307626 |
| Audit coverage | 1.000000 |
| Inventory coverage | 1.000000 |

Drift score는 평균 표준화 feature shift로, 공격 성공률이나 실제 운영 장애 확률이 아니다. Audit coverage와 inventory coverage는 toy evidence coverage이며 실제 기업 감사 완전성이나 완전한 AI BOM이 아니다.

## 기말논문 연결

W14는 운영형 AI 시스템 보안을 위한 evidence set으로 연결된다. 최소 지표는 dataset hash, model hash, config hash, drift score, audit coverage, artifact inventory다.

## 확인 필요

P03/P04/P05는 로컬 PDF가 대상 논문과 다르므로 최종 인용 전 공식 원문 PDF를 확보해야 한다.

<!-- formula-visual-handout:start -->
## 수식·그래프·그림 보강 요약

| 항목 | 반영 내용 |
|---|---|
| 핵심 수식 | Artifact Integrity Check, Drift와 Audit Coverage |
| 그래프 | `assets/charts/w14_metrics_chart.png` (`metrics_summary.csv` 기반) |
| 다이어그램 | `assets/diagrams/w14_pipeline_diagram.svg` (MLOps supply-chain map) |
| 기호 정의 | 통합보고서와 발표 슬라이드의 수식 블록에 포함 |
| 주의사항 | hash/pass 항목은 시각화에서 제외했으며 원본 CSV와 artifact inventory를 함께 확인해야 한다. |
<!-- formula-visual-handout:end -->
