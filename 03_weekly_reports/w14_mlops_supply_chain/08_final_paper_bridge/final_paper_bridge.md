# W14 기말논문 연결표

## 1. 이번 주차에서 얻은 연구 주제 후보

| 번호 | 주제 후보 | 대상 시스템 | 보안 위협 | 방법론 | 기여 가능성 |
|---:|---|---|---|---|---|
| 1 | 운영형 AI 시스템 보안을 위한 MLOps evidence set 연구 | MLOps pipeline | supply chain attack, artifact tampering, audit gap | 문헌분석 + toy pipeline 평가 | 높음 |
| 2 | ML 모델 배포 파이프라인의 데이터·모델·config 무결성 검증 연구 | ML deployment pipeline | data poisoning, model tampering, config drift | hash 검증, artifact inventory, 재실행 점검 | 높음 |
| 3 | Drift monitoring과 incident response를 포함한 AI assurance case 설계 | 운영 AI 시스템 | drift 미탐지, 로그 누락, rollback 실패 | 평가표 설계, monitoring 지표, audit coverage | 보통 |

## 2. 기말 논문에 반영할 내용

| 논문 장 | 반영 가능 내용 |
|---|---|
| 서론 | 연구용 ML과 운영용 ML 시스템 사이의 보안·재현성 격차 |
| 관련연구 | MLOps practices, ML deployment challenge, AIOps, edge AI, DL for SE |
| 연구문제 | ML 공급망과 운영 파이프라인 보안 evidence set |
| 연구방법 | 문헌분석, 위협모형, 보안통제 매핑, toy pipeline 체크리스트 |
| 분석/실험 | dataset hash, model hash, config hash, drift score, audit coverage, inventory coverage |
| 보안적 함의 | 기밀성, 무결성, 가용성, 프라이버시, 안전성, 책임성 관점 |
| 결론 | MLOps 보안통제 및 assurance case 프레임워크 제안 |

## 3. W14에서 확정한 실험 연결

| 항목 | 결과 | 논문 활용 |
|---|---:|---|
| Baseline accuracy | 0.925000 | 정상 조건 기준선 |
| Baseline F1 | 0.923077 | 분류 균형 지표 |
| Drift score | 0.307626 | 운영 monitoring 지표 |
| Re-run consistency | true | 재현성 근거 |
| Audit coverage | 1.000000 | 책임추적 근거 |
| Inventory coverage | 1.000000 | AI BOM/ML artifact inventory 근거 |

## 4. 주의할 점

P03/P04/P05는 로컬 PDF가 대상 논문과 다르므로 최종 논문 인용 전 공식 원문 확인이 필요하다. W14 toy 실험은 실제 운영 보안성 증명이 아니라 보안 평가 evidence 구조를 보이는 제한된 실습이다.
