# W11 실험 실행 로그

| 항목 | 내용 |
|---|---|
| 실행일 | 2026-06-22 |
| Seed | 42 |
| Status | executed |
| 데이터 | synthetic_binary_classification, personal_data=False |
| 모델 | toy_logistic_regression with clipped gradients and DP-like gradient noise |
| Membership threshold | 0.94 |
| 보안 시나리오 | non-DP baseline, DP-like noise low/medium/high |
| 허용 범위 | synthetic toy evaluation and literature-based privacy-risk analysis |
| 제외 범위 | actual personal data, production model probing, unauthorized API queries, real-person membership inference |

## 실행 명령

```bash
python3 src/run_experiment.py --config configs/config.yaml
```

## 주요 지표

| 조건 | Accuracy | Train Accuracy | MI Attack Accuracy | Epsilon Proxy | Utility Drop | Privacy Leakage Score | Noise Multiplier | 해석 |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Non-DP baseline | 0.956250 | 0.965625 | 0.515625 | not_applicable | 0.000000 | 0.014833 | 0.000000 | 표준 라이브러리 기반 synthetic toy 결과이며 정식 DP 보증이 아니다. |
| DP-like noise low | 0.956250 | 0.965625 | 0.515625 | 8.000000 | 0.000000 | 0.014494 | 0.100000 | 표준 라이브러리 기반 synthetic toy 결과이며 정식 DP 보증이 아니다. |
| DP-like noise medium | 0.962500 | 0.965625 | 0.512500 | 3.000000 | 0.000000 | 0.011769 | 0.450000 | 표준 라이브러리 기반 synthetic toy 결과이며 정식 DP 보증이 아니다. |
| DP-like noise high | 0.950000 | 0.962500 | 0.521875 | 1.000000 | 0.006250 | 0.016482 | 1.200000 | 표준 라이브러리 기반 synthetic toy 결과이며 정식 DP 보증이 아니다. |

## Synthetic 샘플 예측 기록

| 조건 | Sample ID | Label | Probability | Prediction |
|---|---|---:|---:|---:|
| Non-DP baseline | test_000 | 1 | 0.999952 | 1 |
| Non-DP baseline | test_001 | 0 | 0.532909 | 1 |
| Non-DP baseline | test_002 | 1 | 0.897177 | 1 |
| DP-like noise low | test_000 | 1 | 0.999959 | 1 |
| DP-like noise low | test_001 | 0 | 0.524147 | 1 |
| DP-like noise low | test_002 | 1 | 0.897328 | 1 |
| DP-like noise medium | test_000 | 1 | 0.999892 | 1 |
| DP-like noise medium | test_001 | 0 | 0.380880 | 0 |
| DP-like noise medium | test_002 | 1 | 0.839101 | 1 |
| DP-like noise high | test_000 | 1 | 0.999997 | 1 |
| DP-like noise high | test_001 | 0 | 0.779031 | 1 |
| DP-like noise high | test_002 | 1 | 0.966004 | 1 |

## 산출물

- `outputs/metrics_summary.csv`
- `outputs/results.json`
- `outputs/run_log.md`

## 한계

이 결과는 DP와 membership inference 평가표를 설명하기 위한 synthetic toy 실험이다. `epsilon_proxy`는 정식 privacy accountant로 계산한 보장이 아니며, noise 강도에 따른 해석용 proxy이다. 실제 개인정보 보호 수준, 실제 서비스 모델의 membership inference 위험, 실제 DP-SGD 보증으로 일반화하지 않는다.
