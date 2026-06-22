# 평가방법

| 평가 항목 | 지표 | 측정 방법 | 필요한 데이터 | 비고 |
|---|---|---|---|---|
| Global Utility | Accuracy / F1 | clean synthetic test set에서 global model 평가 | synthetic test data | 기본 성능 |
| Poisoning Impact | Accuracy drop / ASR 상승 | malicious client rate별 FedAvg 결과 비교 | poisoned local updates | 무결성 |
| Backdoor Success | ASR | class 0 test sample에 toy trigger를 더한 뒤 target class 1 예측률 측정 | triggered synthetic test data | 실제 payload 아님 |
| Privacy Leakage | Privacy leakage proxy | 라운드별 update norm과 update 다양성으로 대용 점수 계산 | simulated client updates | 실제 gradient inversion 아님 |
| Robustness | ASR 감소, robust accuracy | 20% malicious 조건에서 FedAvg와 coordinate median 비교 | clean/poisoned updates | 방어 효과 |
| Communication Cost | Communication bytes | round, client 수, parameter 수 기준 계산 | training config | 운영 비용 |
| Reproducibility | Seed/config/log | config, run log, CSV, JSON 보존 여부 확인 | `04_experiment/outputs/` | 재현성 |

## 그림 1. 연합학습 보안 평가 흐름

```text
Client Local Data
        ↓
Local Training / Local Update
        ↓
Aggregation Server
        ↓
FedAvg or Coordinate Median
        ↓
Global Model
        ↓
Clean Evaluation --> Global Accuracy, Global F1
        ↓
Triggered Evaluation --> ASR
        ↓
Update Exposure Check --> Privacy Leakage Proxy
        ↓
Reproducibility Evidence --> seed, config, outputs, run_log
```

## 실행 결과 요약

| 조건 | Malicious Client Rate | Aggregation | Global Accuracy | Global F1 | ASR | Privacy Leakage Proxy |
|---|---:|---|---:|---:|---:|---:|
| Clean FL | 0% | fedavg | 0.960000 | 0.958042 | 0.136076 | 0.442597 |
| Poisoned FL 10% | 10% | fedavg | 0.953333 | 0.951557 | 0.297468 | 0.428377 |
| Poisoned FL 20% | 20% | fedavg | 0.950000 | 0.948630 | 0.496835 | 0.486591 |
| Robust aggregation 20% | 20% | coordinate_median | 0.955000 | 0.953368 | 0.237342 | 0.439875 |

## 재현성 근거

- 실행 로그: `04_experiment/outputs/run_log.md`
- 정량 CSV: `04_experiment/outputs/metrics_summary.csv`
- 설정과 원시 결과: `04_experiment/outputs/results.json`
- 설정 파일: `04_experiment/configs/config.yaml`
- 실행 코드: `04_experiment/src/run_experiment.py`

## 해석 제한

이 결과는 synthetic federated binary classification 기반 toy 실험의 평가 형식 검증용 수치이며, 실제 FL framework, 실제 secure aggregation, differential privacy, gradient inversion, membership inference, 실제 서비스 보안성으로 일반화하지 않는다.

Privacy Leakage Proxy는 실제 gradient inversion 또는 membership inference 성공률이 아니다. 본 실험은 안전한 synthetic update의 노출 위험 대용 지표만 기록한다.
