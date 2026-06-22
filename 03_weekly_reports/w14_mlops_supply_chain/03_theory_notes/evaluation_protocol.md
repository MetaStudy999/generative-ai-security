# 평가방법

| 평가 항목 | 지표 | 측정 방법 | 필요한 데이터 | 이번 실행 결과 | 비고 |
|---|---|---|---|---|---|
| Pipeline Integrity | Dataset/model/config hash | 데이터·모델·config의 SHA-256 기록과 재검증 | Pipeline metadata | dataset `sha256:b9e597bccdbde442`, model hash match true | 무결성 |
| Deployment Reliability | Re-run consistency | 동일 seed/config 재실행 후 dataset/model hash 비교 | Config, seed, artifact | true | 재현성 |
| Drift Detection | Drift score | 기준 test set과 drifted sample의 평균 표준화 feature shift 계산 | Monitoring sample | 0.307626, threshold 0.25 초과 | 모델 감시 |
| Baseline Utility | Accuracy/F1 | 정상 synthetic test set에서 toy model 평가 | Synthetic test data | accuracy 0.925000, F1 0.923077 | 기준 성능 |
| Incident Response | Audit evidence availability | 사고 후 필요한 run metadata와 artifact 목록 보존 여부 | Run log, audit log | audit coverage 1.000000 | 대응력 |
| Auditability | Audit coverage | 필수 감사 필드 10개 중 기록된 비율 | Logs/metadata | 1.000000 | 책임성 |
| Supply Chain Risk | Inventory coverage | AI BOM/ML artifact inventory 최소 항목 충족 여부 | artifact_inventory.json | 1.000000 | 공급망 |

## 실행 전제

실험은 2026-06-22 local synthetic toy 환경에서 실행했다. 모든 정량값은 `04_experiment/outputs/run_log.md`, `metrics_summary.csv`, `results.json`과 일치하는 값만 적었다.

## 결과 해석 원칙

- Accuracy/F1은 모델 성능의 기준선일 뿐 공급망 보안성을 직접 의미하지 않는다.
- Hash와 inventory는 변조 탐지와 책임추적의 출발점이지 완전한 방어가 아니다.
- Drift score는 입력 분포 변화 경보이며, 원인 분석이나 자동 롤백은 별도 운영 절차가 필요하다.
- 실제 개인정보, 실제 운영 로그, 실제 악성 패키지 또는 공격 payload는 사용하지 않는다.
