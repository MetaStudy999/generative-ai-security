# W13 평가방법

| 평가 항목 | 지표 | 측정 방법 | 필요한 데이터 | 해석 원칙 |
|---|---|---|---|---|
| Extraction Fidelity | Agreement rate | victim과 substitute의 출력 일치율 | Synthetic test set | 모델 행동 유사도이며 ownership 증거는 아님 |
| Substitute Accuracy | Accuracy | true label 기준 대체 모델 성능 | Synthetic clean test data | 공격자가 얻은 모델의 utility proxy |
| Query Cost | Number of queries | 대체 모델 학습에 사용한 질의 수 | Query-response pairs | 공격 비용과 API 노출 범위 |
| Watermark Detectability | Detection rate | trigger set에서 signature label 일치율 | Watermark trigger set | FPR과 함께 해석 |
| False Positive Rate | FPR proxy | 무관 clean control model이 trigger signature와 우연히 일치한 비율 | Non-watermarked control model | 높으면 소유권 주장의 신뢰도 약화 |
| Utility Loss | Accuracy drop / quality loss | victim model의 clean utility 확인 | Synthetic clean test data | 본 실험은 victim utility 0.868000 |
| Robustness | Detection after extraction | substitute model에서 watermark signal 유지 여부 | Extracted substitute models | 모델 추출 이후 검출 가능성 |
| Reproducibility | Seed/run log | config, CSV, JSON, run log 대조 | `04_experiment/outputs/` | seed 42 |

## 실행 결과 요약

| 조건 | Query Budget | Extraction Fidelity | Substitute Accuracy | Watermark Detection | False Positive Rate | Utility Accuracy |
|---|---:|---:|---:|---:|---:|---:|
| Baseline victim model | 0 | 1.000000 | 0.868000 | 1.000000 | 0.600000 | 0.868000 |
| Substitute query 100 | 100 | 0.864000 | 0.812000 | 0.700000 | 0.600000 |  |
| Substitute query 500 | 500 | 0.920000 | 0.840000 | 1.000000 | 0.600000 |  |
| Substitute query 1000 | 1000 | 0.902000 | 0.822000 | 1.000000 | 0.600000 |  |
| Watermarked ownership check | 0 | 1.000000 | 0.868000 | 1.000000 | 0.600000 | 0.868000 |

## False Positive 해석 보완

본 실험에서 watermark detection은 일부 조건에서 1.000000으로 나타났지만, false positive proxy도 0.600000으로 높게 나타났다. 이는 trigger-set 기반 소유권 검증이 detection rate만으로는 충분하지 않으며, clean control model, unrelated model, random trigger set, 복수 seed, 통계적 유의성 검정이 함께 필요함을 의미한다. 따라서 본 결과는 “소유권 검증 성공”이 아니라 “소유권 검증에는 detection rate와 false positive rate를 함께 기록해야 한다”는 교육용 근거로 해석한다.

| 검증 항목 | 단독 해석 위험 | 보완 지표 |
|---|---|---|
| Watermark Detection | 높으면 소유권 증거처럼 보일 수 있음 | FPR, FNR, p-value, 대조군 |
| False Positive Rate | 높으면 무관 모델도 소유 모델처럼 판단될 수 있음 | unrelated model control, random trigger control |
| Extraction Fidelity | 높으면 추출 위험을 보여주지만 ownership 증거는 아님 | query budget, utility, trigger inheritance |
| Utility Accuracy | 워터마크 삽입이 모델 성능을 해치지 않는지 확인 | clean accuracy, task score |
| Query Budget | 공격 비용과 위험 노출 범위 | rate limit, monitoring, logging |

## 해석 원칙

결과는 `04_experiment/outputs/run_log.md`, `metrics_summary.csv`, `results.json`과 일치한다. 본 수치는 로컬 synthetic toy 실험이며 실제 API, 실제 LLM, 실제 상용 모델의 추출 위험을 직접 측정한 결과가 아니다.
