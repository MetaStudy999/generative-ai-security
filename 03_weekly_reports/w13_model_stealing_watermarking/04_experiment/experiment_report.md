# W13 실험 보고서

## 1. 실험 목표

W13 실습은 모델 지식재산(IP), 모델 도난, 모델 추출 위협을 실제 서비스가 아닌 synthetic toy 환경에서 정량화하는 것이다. 목표는 공격 절차를 제공하는 것이 아니라, query budget에 따라 대체 모델의 행동 유사도와 워터마크 검출 지표가 어떻게 변하는지 안전하게 관찰하는 것이다.

## 2. 환경

| 항목 | 내용 |
|---|---|
| OS | Ubuntu 24.04 기준 |
| Container | Docker 사용 가능 |
| Python | 3.11 기준, 스크립트는 표준 라이브러리만으로 실행 가능 |
| Package manager | uv, Dockerfile 내부 포함 |
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

Docker 사용 시에는 다음 흐름을 따른다.

```bash
docker build -t w13-aisec .
docker run --rm -it -v "$(pwd)":/workspace w13-aisec bash
python src/run_experiment.py --config configs/config.yaml
```

## 5. 실험 결과

| 조건 | Query Budget | Extraction Fidelity | Substitute Accuracy | Watermark Detection | False Positive Rate | Utility Accuracy | 해석 |
|---|---:|---:|---:|---:|---:|---:|---|
| Baseline victim model | 0 | 1.000000 | 0.868000 | 1.000000 | 0.600000 | 0.868000 | 원 모델은 clean utility와 trigger signature를 유지 |
| Substitute query 100 | 100 | 0.864000 | 0.812000 | 0.700000 | 0.600000 |  | 적은 질의만으로도 행동 유사도가 높아짐 |
| Substitute query 500 | 500 | 0.920000 | 0.840000 | 1.000000 | 0.600000 |  | trigger가 모두 관측되며 검출률이 상승 |
| Substitute query 1000 | 1000 | 0.902000 | 0.822000 | 1.000000 | 0.600000 |  | 1NN toy 특성상 fidelity가 단조 증가하지는 않음 |
| Watermarked ownership check | 0 | 1.000000 | 0.868000 | 1.000000 | 0.600000 | 0.868000 | 소유권 검증 절차의 toy upper bound |

## 6. 해석

query-response 정보만으로 substitute model이 victim behavior에 상당히 접근할 수 있음을 확인했다. 다만 false positive proxy가 0.600000으로 높아, 단순 trigger-set 검출은 강한 소유권 증거로 보기 어렵다. 따라서 W13의 결론은 “워터마크 검출률을 높이면 충분하다”가 아니라 “검출률, 위양성, utility, 재현성을 함께 보고해야 한다”이다.

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

## 8. 한계

본 실습은 교육용 toy evaluation이다. 실제 상용 API, 실제 LLM, 실제 모델 탈취, 무단 대량 질의, 개인정보 기반 평가는 포함하지 않는다. false positive proxy가 높게 나온 점은 설계 실패가 아니라, ownership verification에서 통계적 신뢰성과 대조군 설계가 필수임을 보여주는 한계로 기록한다.
