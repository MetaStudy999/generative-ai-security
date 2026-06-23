# W13 실험 보고서

## 1. 실험 목표

W13 실습은 모델 지식재산(IP), 모델 도난, 모델 추출 위협을 실제 서비스가 아닌 synthetic binary classification 기반 안전 toy 실험에서 정량화한다. 목표는 공격 절차를 제공하는 것이 아니라, query budget에 따라 대체 모델의 행동 유사도와 워터마크 검출 지표가 어떻게 변하는지 안전하게 관찰하는 것이다.

본 실습은 실제 상용 API나 실제 LLM을 대상으로 한 모델 추출 공격 재현이 아니라 W13의 핵심인 모델 IP 보안 평가축을 안전하게 설명하기 위한 최소 toy protocol이다. 따라서 synthetic binary classification과 toy logistic victim model, query-response 1NN substitute model을 사용하되, 평가 구조는 이후 실제 model stealing, API abuse monitoring, model watermarking ownership verification에도 확장 가능하도록 query budget, extraction fidelity, substitute accuracy, watermark detection, false positive rate, utility accuracy, reproducibility evidence로 분리하였다.

## 2. 환경

| 항목 | 내용 |
|---|---|
| Python | 3.11 기준 |
| 의존성 | `pyyaml` optional, 나머지는 표준 라이브러리 |
| Seed | 42 |
| 데이터 | synthetic binary classification |
| 개인정보 | 사용하지 않음 |
| 실행일 | 2026-06-22 |
| 결과 근거 | `outputs/metrics_summary.csv`, `outputs/results.json`, `outputs/run_log.md` |

## 3. 실험 설계

| 단계 | 설계 내용 | 기록 위치 |
|---|---|---|
| Victim model | synthetic data로 toy logistic classifier 학습 | `src/run_experiment.py` |
| Watermark trigger set | 20개 synthetic trigger와 signature label 정의 | script 내부 deterministic seed |
| Substitute model | query-response pairs만 보고 1-nearest-neighbor classifier 구성 | query budget 100/500/1000 |
| Extraction fidelity | clean test set에서 victim/substitute 출력 일치율 측정 | metrics |
| Watermark detection | trigger set에서 signature 일치율 측정 | metrics |
| False positive proxy | 무관 clean control model의 trigger 일치율 측정 | metrics |
| Safety scope | 실제 API, 실제 개인정보, 무단 대량 질의 제외 | config/security_scope |

## 4. 실행 명령

```bash
cd 03_weekly_reports/w13_model_stealing_watermarking/04_experiment
python3 src/run_experiment.py --config configs/config.yaml
```

Docker Compose 사용 시:

```bash
cd 03_weekly_reports/w13_model_stealing_watermarking/04_experiment
docker compose run --rm w13-model-stealing-watermarking python3 src/run_experiment.py --config configs/config.yaml
```

## 5. 실험 결과

| 조건 | Query Budget | Watermark Queries Seen | Extraction Fidelity | Substitute Accuracy | Watermark Detection | False Positive Rate | Utility Accuracy | 해석 |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Baseline victim model | 0 | 0 | 1.000000 | 0.868000 | 1.000000 | 0.600000 | 0.868000 | 원 모델은 clean utility와 trigger signature를 유지 |
| Substitute query 100 | 100 | 5 | 0.864000 | 0.812000 | 0.700000 | 0.600000 |  | 적은 질의만으로도 행동 유사도가 높아짐 |
| Substitute query 500 | 500 | 20 | 0.920000 | 0.840000 | 1.000000 | 0.600000 |  | trigger가 모두 관측되며 검출률이 상승 |
| Substitute query 1000 | 1000 | 20 | 0.902000 | 0.822000 | 1.000000 | 0.600000 |  | 1NN toy 특성상 fidelity가 단조 증가하지는 않음 |
| Watermarked ownership check | 0 | 20 | 1.000000 | 0.868000 | 1.000000 | 0.600000 | 0.868000 | toy ownership check upper bound |

## 6. False Positive 해석 보완

본 실험에서 watermark detection은 일부 조건에서 1.000000으로 나타났지만, false positive proxy도 0.600000으로 높게 나타났다. 이는 trigger-set 기반 소유권 검증이 detection rate만으로는 충분하지 않으며, clean control model, unrelated model, random trigger set, 복수 seed, 통계적 유의성 검정이 함께 필요함을 의미한다. 따라서 본 결과는 “소유권 검증 성공”이 아니라 “소유권 검증에는 detection rate와 false positive rate를 함께 기록해야 한다”는 교육용 근거로 해석한다.

| 검증 항목 | 단독 해석 위험 | 보완 지표 |
|---|---|---|
| Watermark Detection | 높으면 소유권 증거처럼 보일 수 있음 | FPR, FNR, p-value, 대조군 |
| False Positive Rate | 높으면 무관 모델도 소유 모델처럼 판단될 수 있음 | unrelated model control, random trigger control |
| Extraction Fidelity | 높으면 추출 위험을 보여주지만 ownership 증거는 아님 | query budget, utility, trigger inheritance |
| Utility Accuracy | 워터마크 삽입이 모델 성능을 해치지 않는지 확인 | clean accuracy, task score |
| Query Budget | 공격 비용과 위험 노출 범위 | rate limit, monitoring, logging |

## 7. 재현성 점검

| 항목 | 상태 | 근거 |
|---|---|---|
| Seed 고정 | 완료 | `configs/config.yaml` |
| 실행 스크립트 보존 | 완료 | `src/run_experiment.py` |
| CSV 결과 | 완료 | `outputs/metrics_summary.csv` |
| JSON 결과 | 완료 | `outputs/results.json` |
| 실행 로그 | 완료 | `outputs/run_log.md` |
| 개인정보 제외 | 완료 | synthetic data only |
| 실제 API 제외 | 완료 | local toy evaluation only |
| outputs-보고서 수치 대조 | 완료 | 세 outputs 파일과 본 보고서 수치 일치 |

## 8. 한계

이 결과는 synthetic binary classification 기반 toy 실험의 평가 형식 검증용 수치이며, 실제 상용 API, 실제 LLM, 실제 모델 탈취, 무단 대량 질의, 개인정보 기반 모델 추출 또는 소유권 분쟁 증거로 일반화하지 않는다.

false positive proxy가 높게 나온 점은 설계 실패가 아니라, ownership verification에서 통계적 신뢰성과 대조군 설계가 필수임을 보여주는 한계로 기록한다.
