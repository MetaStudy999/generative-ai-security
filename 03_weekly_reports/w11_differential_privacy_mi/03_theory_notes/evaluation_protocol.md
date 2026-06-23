# 평가방법

| 평가 항목 | 지표 | 측정 방법 | 필요한 데이터 | 비고 |
|---|---|---|---|---|
| Model Utility | Accuracy | 정상 test set 평가 | synthetic train/test data | 기본 성능 |
| Privacy Budget | epsilon/delta 또는 epsilon proxy | privacy accountant 또는 실습용 proxy 기록 | training config | W11 toy 실험의 `epsilon_proxy`는 정식 DP 보장 아님 |
| Membership Inference Risk | MI attack accuracy | member/non-member confidence threshold 비교 | synthetic evaluation split | 실제 개인 대상 추론 제외 |
| Privacy Leakage | leakage score | mean member confidence와 non-member confidence 차이 | model outputs | confidence gap proxy |
| Utility Drop | accuracy drop | baseline 대비 DP-like 조건 accuracy 변화 | baseline/defense metrics | defense 비용 |
| Stability | seed/config/output 보존 | 동일 seed 반복 가능성 확인 | config/logs | 재현성 |
| Reference Integrity | DOI/PDF 일치 상태 | 로컬 PDF, 강의자료, DOI 표 대조 | `01_papers/` | 관련 논문 PDF 표시 |

## W11 실행 결과 요약

| 조건 | Accuracy | Train Accuracy | MI Attack Accuracy | Epsilon Proxy | Utility Drop | Privacy Leakage Score | Noise Multiplier |
|---|---:|---:|---:|---:|---:|---:|---:|
| Non-DP baseline | 0.956250 | 0.965625 | 0.515625 | 해당 없음 | 0.000000 | 0.014833 | 0.000000 |
| DP-like noise low | 0.956250 | 0.965625 | 0.515625 | 8.000000 | 0.000000 | 0.014494 | 0.100000 |
| DP-like noise medium | 0.962500 | 0.965625 | 0.512500 | 3.000000 | 0.000000 | 0.011769 | 0.450000 |
| DP-like noise high | 0.950000 | 0.962500 | 0.521875 | 1.000000 | 0.006250 | 0.016482 | 1.200000 |

정량값은 `04_experiment/outputs/run_log.md`, `metrics_summary.csv`, `results.json` 기준이다. 결과는 synthetic binary classification 기반 toy 평가이며 실제 DP 보장이나 실제 모델 privacy risk로 일반화하지 않는다. `noise_multiplier`는 toy gradient noise scale이고, `epsilon_proxy`는 formal privacy accountant가 산출한 epsilon이 아니다.
