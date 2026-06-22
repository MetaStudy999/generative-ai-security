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

## 기말논문 연결

W14는 운영형 AI 시스템 보안을 위한 evidence set으로 연결된다. 최소 지표는 dataset hash, model hash, config hash, drift score, audit coverage, artifact inventory다.

## 확인 필요

P03/P04/P05는 로컬 PDF가 대상 논문과 다르므로 최종 인용 전 공식 원문 PDF를 확보해야 한다.
