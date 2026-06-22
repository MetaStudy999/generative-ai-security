# 평가방법

| 평가 항목 | 지표 | 측정 방법 | 필요한 데이터 | 비고 |
|---|---|---|---|---|
| Clean Performance | Accuracy/F1/Task score | 정상 조건에서 기준 모델 평가 | 공개 또는 synthetic 데이터 | 기본 성능 |
| Attack Impact | Attack Success Rate/Risk score | 비전 기반 대적공격, White-box attack 조건을 모의 | 변형 입력 또는 시나리오 | 악용 절차는 제외 |
| Robust Performance | Robust score | 공격 또는 교란 조건에서 성능 비교 | 교란 데이터 | 강건성 |
| Privacy/Leakage | Leakage score | 민감정보 노출 가능성 점검 | synthetic shadow data | 실제 개인정보 금지 |
| Reproducibility | Seed/config/log completeness | seed, config, Docker, 결과표 보존 여부 점검 | 실행 로그 | W03 toy 결과 기록 완료 |
| Human Review | 검토 완료 여부 | 원문, DOI, 수치, 인용을 사람이 재검토 | 체크리스트 | 최종 책임 |

## 실행 상태

W03 toy 실험은 `04_experiment/src/run_experiment.py`로 실행했고, 정량 수치는 `04_experiment/outputs/run_log.md`에 기록했다. Clean baseline은 accuracy/macro F1 1.000000이며, 중심점 방향 L-infinity perturbation은 epsilon 0.45에서 accuracy 0.000000, ASR 1.000000으로 결정 경계 전환을 보였다. 이 수치는 synthetic toy 평가의 결과이며 실제 CNN/ViT 강건성으로 일반화하지 않는다.
