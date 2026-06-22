# W11 실험 보고서

## 1. 실험 목표

W11 실습은 차등프라이버시(DP)와 membership inference 평가를 안전한 synthetic toy 환경에서 연결하는 것이다. 실제 개인정보, 실제 운영 모델, 실제 개인 대상 membership inference는 사용하지 않는다.

## 2. 환경

| 항목 | 내용 |
|---|---|
| OS | Ubuntu 24.04 기준 |
| Container | Docker 지원, 로컬 `python3` 실행 가능 |
| Python | 3.11 계열 |
| Seed | 42 |
| 데이터 | synthetic binary classification |
| 결과 상태 | 실행 완료 |
| 결과 위치 | `outputs/metrics_summary.csv`, `outputs/results.json`, `outputs/run_log.md` |

## 3. 실행 절차

```bash
python3 src/run_experiment.py --config configs/config.yaml
```

| 단계 | 내용 | 기록 |
|---|---|---|
| 데이터 생성 | synthetic train/test split 생성 | 개인정보 없음 |
| 기준 모델 | toy logistic regression 학습 | Non-DP baseline |
| 방어 조건 | clipped gradient + DP-like noise low/medium/high | 정식 DP 보장 아님 |
| MI 평가 | member/non-member confidence threshold 비교 | MI Attack Accuracy |
| leakage 평가 | mean member confidence와 mean non-member confidence 차이 | Privacy Leakage Score |
| 재현성 | seed/config/CSV/JSON/run log 보존 | 완료 |

## 4. 결과

| 조건 | Accuracy | Train Accuracy | MI Attack Accuracy | Epsilon Proxy | Utility Drop | Privacy Leakage Score | Noise Multiplier |
|---|---:|---:|---:|---:|---:|---:|---:|
| Non-DP baseline | 0.956250 | 0.965625 | 0.515625 | 해당 없음 | 0.000000 | 0.014833 | 0.000000 |
| DP-like noise low | 0.956250 | 0.965625 | 0.515625 | 8.000000 | 0.000000 | 0.014494 | 0.100000 |
| DP-like noise medium | 0.962500 | 0.965625 | 0.512500 | 3.000000 | 0.000000 | 0.011769 | 0.450000 |
| DP-like noise high | 0.950000 | 0.962500 | 0.521875 | 1.000000 | 0.006250 | 0.016482 | 1.200000 |

## 5. 해석

본 toy 결과에서는 medium noise 조건에서 leakage proxy가 가장 낮게 기록되었고, high noise 조건은 accuracy가 0.006250 낮아졌지만 MI attack accuracy는 오히려 높게 나타났다. 이는 noise를 키웠다고 항상 privacy proxy가 단조롭게 개선되는 것은 아니며, 실제 DP 보장을 주장하려면 accountant와 반복 실험이 필요하다는 점을 보여준다.

## 6. 한계

- `epsilon_proxy`는 정식 privacy accountant로 계산한 epsilon이 아니다.
- 데이터는 synthetic이므로 실제 개인 정보 보호 수준으로 일반화하지 않는다.
- MI 평가는 confidence threshold 기반의 안전한 proxy이며 실제 개인 대상 공격 절차가 아니다.
- 최종 연구에서는 DP-SGD 라이브러리와 formal accounting을 별도로 연결해야 한다.
