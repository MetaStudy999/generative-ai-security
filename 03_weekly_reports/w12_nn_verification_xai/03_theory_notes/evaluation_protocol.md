# 평가방법

| 평가 항목 | 지표 | 측정 방법 | 필요한 데이터 | W12 실행 상태 |
|---|---|---|---|---|
| Clean Performance | Clean Accuracy | 정상 조건에서 기준 모델 평가 | synthetic test data | 완료, 0.818750 |
| Robust Performance | Robust Accuracy | perturbation 조건에서 정확도 측정 | perturbed test data | 완료, 0.543750 |
| Certified Robustness | Certified Rate / bound margin | 선형 모델 L-infinity bound proxy | model weights, specification | 완료, 0.543750 |
| Explanation Stability | Attribution cosine similarity | 입력 변조 전후 feature attribution 비교 | clean/perturbed samples | 완료, 0.927782 |
| Fairness Impact | Group accuracy gap | synthetic group별 accuracy gap | group-labeled synthetic data | 완료, 0.039141 |
| Verification Cost | Runtime ms | bound 계산 시간 측정 | verification logs | 완료, 0.184215 ms |
| Reproducibility | Seed/config/log completeness | seed, config, Docker, 결과표 보존 여부 점검 | 실행 로그 | 완료 |
| Human Review | 검토 완료 여부 | 원문, DOI, 수치, 인용을 사람이 재검토 | 체크리스트 | DOI/원문 대조 남음 |

## 실행 전제와 해석 범위

실험 결과는 `04_experiment/outputs/run_log.md`, `metrics_summary.csv`, `results.json`이 생성된 뒤에만 보고서에 반영한다. W12의 정량값은 synthetic toy classification에서 산출한 교육용 결과이며, certified rate는 대규모 DNN의 완전한 formal verification 결과가 아니라 선형 모델 bound proxy다.
