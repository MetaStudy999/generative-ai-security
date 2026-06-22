# 실험 보고서

## 1. 실험 목표

W10 실습은 연합학습(FL)에서 malicious client 비율과 aggregation rule이 global utility와 backdoor-style ASR에 미치는 영향을 synthetic federated binary classification 기반 안전 toy 실험으로 확인하는 것이다. 실제 개인정보, 실제 FL 서비스, 무단 클라이언트 접속, 운영 시스템 공격은 포함하지 않는다.

## 2. 환경

| 항목 | 내용 |
|---|---|
| OS | Ubuntu 24.04 기준 |
| Container | Dockerfile 제공, 로컬 실행은 Python 3.11 호환 코드 |
| Python | 3.11 기준 |
| Seed | 42 |
| 데이터 | synthetic federated binary classification |
| Client 수 | 10 |
| Client별 샘플 | 80 |
| Test sample | 600 |
| 모델 | toy logistic regression |
| 라운드 | 25 |
| 로컬 epoch | 3 |
| 결과 상태 | 실행 완료 |

## 3. 실행 절차

```bash
python3 03_weekly_reports/w10_federated_learning_security/04_experiment/src/run_experiment.py --config 03_weekly_reports/w10_federated_learning_security/04_experiment/configs/config.yaml
```

Docker 사용 시에는 `04_experiment/`에서 다음 절차를 따른다.

```bash
docker compose run --rm w10-federated-learning-security python3 src/run_experiment.py --config configs/config.yaml
```

## 4. 실험 조건

| 조건 | Malicious Client Rate | Aggregation | 설명 |
|---|---:|---|---|
| Clean FL | 0% | fedavg | 악성 client 없는 기준 조건 |
| Poisoned FL 10% | 10% | fedavg | 10% client가 synthetic toy poisoned update 제출 |
| Poisoned FL 20% | 20% | fedavg | 20% client가 synthetic toy poisoned update 제출 |
| Robust aggregation 20% | 20% | coordinate_median | 같은 20% 조건에서 median 기반 robust aggregation 적용 |

## 5. 결과

| 조건 | Malicious Client Rate | Global Accuracy | Global F1 | ASR | Privacy Leakage Proxy | 해석 |
|---|---:|---:|---:|---:|---:|---|
| Clean FL | 0% | 0.960000 | 0.958042 | 0.136076 | 0.442597 | 기준 FedAvg 조건 |
| Poisoned FL | 10% | 0.953333 | 0.951557 | 0.297468 | 0.428377 | clean 성능은 유지되지만 ASR 상승 |
| Poisoned FL | 20% | 0.950000 | 0.948630 | 0.496835 | 0.486591 | 악성 client 비율 증가에 따라 ASR 크게 상승 |
| Robust aggregation | 20% | 0.955000 | 0.953368 | 0.237342 | 0.439875 | coordinate median이 ASR을 낮췄지만 완전 제거는 아님 |

## 6. 결과 파일

| 파일 | 내용 |
|---|---|
| `outputs/run_log.md` | 사람이 읽는 실행 로그와 지표 요약 |
| `outputs/metrics_summary.csv` | 조건별 정량 지표 |
| `outputs/results.json` | config, 원시 결과, round log |

## 7. 재현성 점검

- `configs/config.yaml`에 seed, 데이터, 실험 조건을 기록했다.
- `src/run_experiment.py`는 synthetic data만 생성하며 외부 네트워크나 실제 개인정보를 사용하지 않는다.
- 결과값은 `outputs/run_log.md`, `metrics_summary.csv`, `results.json`과 보고서 표가 일치해야 한다.
- `experiment.malicious_client_rates`, `experiment.robust_aggregation_rate`, `experiment.results_recorded`, `experiment.notes`는 현재 코드에서 조건 생성에 직접 쓰이지 않는 기록용 필드다. 실제 조건은 `src/run_experiment.py`의 `CONDITIONS`에 고정되어 있다.
- 2026-06-23 보완 검증에서 로컬 실행 결과가 기존 outputs와 일치했고, Docker build와 `docker compose run` 명령이 정상 종료되었다.

## 8. 한계

본 실습은 학습 목적의 toy simulation이다. 실제 FL framework, 실제 secure aggregation, differential privacy, gradient inversion, membership inference를 구현하지 않았다. Privacy Leakage Proxy는 실제 privacy attack 성공률이 아니라 update 노출 위험을 설명하기 위한 대용 지표다.

이 결과는 synthetic federated binary classification 기반 toy 실험의 평가 형식 검증용 수치이며, 실제 FL framework, 실제 secure aggregation, differential privacy, gradient inversion, membership inference, 실제 서비스 보안성으로 일반화하지 않는다.
