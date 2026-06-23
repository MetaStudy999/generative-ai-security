# W14 MLOps Supply Chain Toy Pipeline Run Log

## 1. 실행 메타데이터

| 항목 | 값 |
|---|---|
| 주차 | W14 |
| 주제 | MLOps/DevOps·데이터/모델 파이프라인·공급망 보안 |
| 실행일 | 2026-06-22 |
| Seed | 42 |
| 데이터 | synthetic_mlops_binary_classification |
| 개인정보 사용 | false |
| 모델 | toy_logistic_regression |
| 상태 | executed |

## 2. 해시와 재현성

| 항목 | 값 |
|---|---|
| Config SHA-256 | `bf70c5860357c21c289e0507fbe6df25b5a239fe43656e53c731b6047e092002` |
| Dataset SHA-256 | `b9e597bccdbde442522edac38adba4f62be507680b053883620e5defeb4cd5ff` |
| Model SHA-256 | `5ae625dca9cecba7e20c73cbae71f3416be800418bbd93c3c4d3b1555e2a1ce9` |
| Re-run consistency | true |

## 3. 실험 결과

| 점검 항목 | 측정 지표 | 결과 | 보안 의미 |
|---|---|---:|---|
| Baseline model | Accuracy | 0.925000 | 정상 조건 기준 성능 |
| Baseline model | F1 | 0.923077 | 정상 조건 분류 균형 |
| Data versioning | Dataset hash | `sha256:b9e597bccdbde442` | 데이터 무결성 기준점 |
| Model artifact verification | Model hash match | true | 모델 아티팩트 변조 탐지 기준 |
| Re-run consistency | Model/data hash match | true | 동일 config/seed 재실행 가능성 |
| Drift monitoring | Mean standardized feature shift | 0.307626 | 입력 분포 변화 감시 |
| Drifted model | Accuracy under drift | 0.925000 | 분포 변화 조건 성능 |
| Log audit | Audit coverage | 1.000000 | toy 필수 로그 필드 보존률 |
| Artifact inventory | Inventory coverage | 1.000000 | toy AI BOM/ML artifact inventory 최소 항목 충족률 |

## 4. 해석

- Synthetic 기준 모델은 accuracy 0.925000, F1 0.923077로 정상 조건 기준선을 만들었다.
- Drift score는 0.307626이며 threshold 0.25 기준으로 drift_detected=true이다. 이 값은 공격 성공률이나 실제 운영 장애 확률이 아니라 synthetic 기준 데이터와 drifted 데이터 사이의 평균 표준화 feature shift이다.
- Dataset, config, model hash와 audit log를 함께 남겨 모델 아티팩트 변조와 결과 재현성 점검의 toy evidence set을 확보했다. Audit coverage와 inventory coverage는 실제 기업 보안 보증이나 완전한 AI BOM이 아니라 최소 필드 충족률이다.

## 5. 제외 범위

실제 운영 서비스 침해, 무단 시스템 접근, 실제 악성 패키지 배포, 실제 개인정보 사용은 포함하지 않는다.
