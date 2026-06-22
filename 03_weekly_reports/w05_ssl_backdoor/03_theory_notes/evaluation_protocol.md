# 평가방법

| 평가 항목 | 지표 | 측정 방법 | 필요한 데이터 | 비고 |
|---|---|---|---|---|
| Clean Performance | Accuracy/F1/Task score | 정상 조건에서 기준 모델 평가 | 공개 또는 synthetic 데이터 | 기본 성능 |
| Attack Impact | Attack Success Rate/Risk score | Self-supervised pretraining 단계의 공격면, 데이터 오염과 표현공간 왜곡 조건을 모의 | 변형 입력 또는 시나리오 | 악용 절차는 제외 |
| Robust Performance | Robust score | 공격 또는 교란 조건에서 성능 비교 | 교란 데이터 | 강건성 |
| Privacy/Leakage | Leakage score | 민감정보 노출 가능성 점검 | synthetic shadow data | 실제 개인정보 금지 |
| Reproducibility | Seed/config/log completeness | seed, config, Docker, 결과표 보존 여부 점검 | 실행 로그 | W05 toy 실행 완료 |
| Human Review | 검토 완료 여부 | 원문, DOI, 수치, 인용을 사람이 재검토 | 체크리스트 | 최종 책임 |

## 실행 원칙

실험을 수행하지 않은 문서에는 정량값을 비워 두거나 미수행 상태로 표시한다. W05는 synthetic toy 실험을 실행했으므로 정량 수치는 `04_experiment/outputs/run_log.md`, `metrics_summary.csv`, `results.json`에 기록된 값만 사용한다.
