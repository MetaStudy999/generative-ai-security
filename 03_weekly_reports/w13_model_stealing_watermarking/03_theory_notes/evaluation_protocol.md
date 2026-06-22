# 평가방법

| 평가 항목 | 지표 | 측정 방법 | 필요한 데이터 | 비고 |
|---|---|---|---|---|
| Extraction Fidelity | Agreement rate | 원 모델과 추출 모델의 출력 일치율 | Synthetic test set | 모델 행동 유사도 |
| Substitute Accuracy | Accuracy | 대체 모델의 true label 기준 성능 | Synthetic clean test data | 공격자가 얻은 모델의 효용 |
| Query Cost | Number of queries | 대체 모델 학습에 사용한 질의 수 | Query-response pairs | 100/500/1000 비교 |
| Watermark Detectability | Detection rate | trigger set에서 signature label 일치율 | Watermark trigger set | 소유권 검증 proxy |
| False Positive Rate | FPR proxy | 무관 clean model이 trigger signature와 우연히 일치한 비율 | Non-watermarked control model | 낮을수록 좋음 |
| Utility Loss | Accuracy drop / quality loss | victim model의 clean utility 확인 | Synthetic clean test data | 본 실험은 victim utility 0.868000 |
| Robustness | Detection after extraction | substitute model에서 watermark signal 유지 여부 | Extracted substitute models | 추출 후 검출 |
| Reproducibility | Seed/run log | config, CSV, JSON, run log 대조 | `04_experiment/outputs/` | seed 42 |

## 실행 결과 요약

| 조건 | Query Budget | Extraction Fidelity | Substitute Accuracy | Watermark Detection | False Positive Rate | Utility Accuracy |
|---|---:|---:|---:|---:|---:|---:|
| Baseline victim model | 0 | 1.000000 | 0.868000 | 1.000000 | 0.600000 | 0.868000 |
| Substitute query 100 | 100 | 0.864000 | 0.812000 | 0.700000 | 0.600000 |  |
| Substitute query 500 | 500 | 0.920000 | 0.840000 | 1.000000 | 0.600000 |  |
| Substitute query 1000 | 1000 | 0.902000 | 0.822000 | 1.000000 | 0.600000 |  |
| Watermarked ownership check | 0 | 1.000000 | 0.868000 | 1.000000 | 0.600000 | 0.868000 |

## 해석 원칙

결과는 `04_experiment/outputs/run_log.md`, `metrics_summary.csv`, `results.json`과 일치한다. 본 수치는 로컬 synthetic toy 실험이며 실제 API, 실제 LLM, 실제 상용 모델의 추출 위험을 직접 측정한 결과가 아니다. false positive proxy가 0.600000으로 높기 때문에, 본 trigger-set 설계는 강한 소유권 증거가 아니라 평가 절차의 필요성을 보여주는 교육용 예시다.
