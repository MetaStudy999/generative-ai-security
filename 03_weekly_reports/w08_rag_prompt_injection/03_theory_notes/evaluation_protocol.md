# 평가방법

| 평가 항목 | 지표 | 측정 방법 | 필요한 데이터 | 비고 |
|---|---|---|---|---|
| Retrieval Relevance | 평균 relevance score | query-doc pair의 관련성 점수 평균 | synthetic query/doc | 검색 품질 |
| Faithfulness | faithfulness score | 답변이 근거 context를 왜곡하지 않는지 평가 | answer/evidence pair | 환각·조작 방지 |
| Attack Success Rate | ASR | 오염 context가 답변 또는 action에 반영된 비율 | poisoned documents | 공격 효과 |
| Source Verifiability | Source verification rate | 출처·메타데이터가 검증된 비율 | metadata/logs | 신뢰성 |
| Tool Misuse Rate | tool misuse rate | 비인가 또는 부적절한 tool action 비율 | agent logs | 에이전트 보안 |
| Human Approval Effect | human block rate | 승인 게이트가 고위험 action을 차단한 비율 | review logs | 운영 통제 |
| Reproducibility | seed/config/output log | 반복 실행 시 동일 산출물 확인 | config/logs | 재현성 |

## W08 실행 조건

| 항목 | 값 |
|---|---|
| 실행일 | 2026-06-22 |
| Seed | 42 |
| 샘플 수 | 조건별 40개 |
| 데이터 | synthetic RAG documents, no personal data |
| 모델 | rule-based toy RAG prompt-injection evaluator |
| 실행 명령 | `python3 src/run_experiment.py --config configs/config.yaml` |
| 산출물 | `04_experiment/outputs/metrics_summary.csv`, `results.json`, `run_log.md` |

## W08 결과 요약

| 조건 | Retrieval Relevance | ASR | Source Verification | Tool Misuse Rate | Faithfulness | Answer Rate |
|---|---:|---:|---:|---:|---:|---:|
| Clean RAG | 0.907887 | 0.000000 | 1.000000 | 0.000000 | 0.907613 | 0.950000 |
| Poisoned document | 0.690091 | 0.575000 | 0.275000 | 0.125000 | 0.458069 | 0.875000 |
| Source filter 적용 | 0.776926 | 0.050000 | 1.000000 | 0.025000 | 0.778693 | 0.800000 |
| Human approval 적용 | 0.764926 | 0.025000 | 1.000000 | 0.000000 | 0.840805 | 0.575000 |

## 해석 원칙

이 수치는 실제 LLM 성능이 아니라 평가 프로토콜과 기록 구조를 검증하기 위한 toy 실험 결과다. 실제 연구로 확장할 때는 공개 benchmark, 복수 모델, 복수 seed, 독립 라벨러 검토가 필요하다.
