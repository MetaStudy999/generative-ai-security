# 평가방법

| 평가 항목 | 지표 | 측정 방법 | W12 outputs 기준 상태 |
|---|---|---|---|
| Clean Performance | Clean Accuracy | 정상 synthetic test data에서 기준 모델 평가 | Clean model 0.818750 |
| Robust Performance | Robust Accuracy | toy perturbation proxy 조건에서 정확도 측정 | Clean model 0.543750 |
| Certified Robustness Proxy | Certified Rate / mean bound margin | 선형 모델 margin bound proxy | Clean model 0.543750, mean bound margin 0.194462 |
| Explanation Stability | Attribution cosine similarity | 입력 변화 전후 feature attribution 비교 | Clean model 0.927782 |
| Fairness Impact | Group accuracy gap | synthetic group별 accuracy gap | Clean model 0.039141 |
| Verification Cost | Runtime ms | bound proxy 계산 시간 측정 | Clean model 0.223524 ms |
| Reproducibility | Seed/config/log completeness | seed, config, Docker, CSV/JSON/run_log 보존 | 완료 |
| Human Review | 원문·DOI·인용 검토 | 출판사/DOI/로컬 PDF 대조 | P01~P05 일부 확인 필요 |

## 실행 전제와 해석 범위

실험 결과는 `04_experiment/outputs/metrics_summary.csv`, `outputs/results.json`, `outputs/run_log.md`가 생성된 뒤에만 보고서에 반영한다. W12의 정량값은 synthetic binary classification 기반 안전 toy 실험에서 산출한 교육용 결과이며, certified rate는 대규모 DNN의 완전한 formal verification 결과가 아니라 선형 모델 bound proxy다.

이 결과는 synthetic binary classification 기반 toy 실험의 평가 형식 검증용 수치이며, 실제 대규모 DNN formal verification, 실제 안전중요 시스템 보증, 실제 운영 모델의 강건성 또는 XAI 안정성으로 일반화하지 않는다.
