# W08 실험 보고서

## 1. 실습 목적

본 실습은 실제 LLM/API 호출이나 실제 prompt injection 공격 재현이 아니라 W08의 핵심인 RAG 보안 평가축을 안전하게 설명하기 위한 최소 toy protocol이다. 따라서 synthetic RAG 문서와 rule-based toy evaluator를 사용하되, 평가 구조는 이후 실제 RAG, GraphRAG, agentic tool-use 환경에도 확장 가능하도록 retrieval relevance, ASR, source verification, tool misuse rate, faithfulness, answer rate, source block rate, human block rate, reproducibility evidence로 분리하였다.

핵심 질문은 "출처 검증 메타데이터와 human approval gate가 오염 문서 기반 ASR과 tool misuse를 낮추는지, 그리고 그 과정에서 retrieval relevance와 answer rate가 어떻게 변하는지 기록할 수 있는가"이다.

## 2. 실험 범위

| 항목 | 내용 |
|---|---|
| 데이터 | synthetic RAG documents |
| evaluator | rule-based toy RAG prompt-injection evaluator |
| 조건 | Clean RAG, Poisoned document, Source filter, Human approval |
| 샘플 수 | 조건별 40개, 총 160개 |
| seed | 42 |
| 실행일 | 2026-06-22 |
| 제외 범위 | 실제 LLM/API 호출, 실제 외부 시스템 공격, 실제 개인정보, live tool invocation, exploit instruction |

## 3. 산출물 확인

| 파일 | 존재 여부 | 비고 |
|---|---|---|
| `outputs/metrics_summary.csv` | 존재 | 조건별 집계 수치 |
| `outputs/results.json` | 존재 | config, 조건 정의, metrics, 샘플 로그 |
| `outputs/run_log.md` | 존재 | 사람이 읽는 실행 로그 |

세 파일의 주요 수치는 일치한다. 보고서와 발표자료의 정량값은 `outputs/metrics_summary.csv`를 기준으로 통일한다.

## 4. 실험 설계

| 단계 | 설명 | 산출물 |
|---|---|---|
| Synthetic query/doc 조건 생성 | Clean RAG, Poisoned document, Source filter, Human approval 조건별 40개 | 총 160개 synthetic sample |
| RAG 보안 지표 계산 | Retrieval relevance, ASR, source verification, tool misuse, faithfulness, answer rate | `metrics_summary.csv` |
| 방어 효과 기록 | Source block rate, human block rate 기록 | `results.json`, `run_log.md` |
| 재현성 기록 | seed, config, 실행 범위, output 파일명 보존 | `run_log.md` |

## 5. 실험 결과

| 조건 | Retrieval Relevance | ASR | Source Verification | Tool Misuse Rate | Faithfulness | Answer Rate | Source Block Rate | Human Block Rate | 해석 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Clean RAG | 0.907887 | 0.000000 | 1.000000 | 0.000000 | 0.907613 | 0.950000 | 0.000000 | 0.000000 | 정상 문서만 검색되는 기준 조건 |
| Poisoned document | 0.690091 | 0.575000 | 0.275000 | 0.125000 | 0.458069 | 0.875000 | 0.000000 | 0.000000 | 오염 문서가 context에 들어오는 취약 조건 |
| Source filter 적용 | 0.776926 | 0.050000 | 1.000000 | 0.025000 | 0.778693 | 0.800000 | 0.892857 | 0.000000 | 출처 검증으로 ASR이 크게 낮아짐 |
| Human approval 적용 | 0.764926 | 0.025000 | 1.000000 | 0.000000 | 0.840805 | 0.575000 | 0.814815 | 1.000000 | 승인 게이트가 tool misuse를 0으로 낮추지만 answer rate도 감소 |

## 6. 해석

Poisoned document 조건에서는 ASR이 0.575000, tool misuse rate가 0.125000으로 나타났다. Source filter 적용 후 ASR은 0.050000으로 낮아졌고, source verification은 1.000000으로 올라갔다. Human approval 적용 조건에서는 ASR이 0.025000, tool misuse rate가 0.000000이었으나 answer rate는 0.575000으로 낮아졌다.

이 해석은 안전한 toy evaluator의 산출물에 한정된다. ASR 0.575000은 실제 RAG 제품의 공격 성공률이 아니며, human approval gate 결과도 실제 운영 방어 효과를 보증하지 않는다.

## 7. 재현성 점검

| 항목 | 상태 |
|---|---|
| config seed 반영 | 완료 |
| 조건별 샘플 수 반영 | 완료 |
| `risk_threshold` 반영 | 완료 |
| `source_filter_block_rate` 반영 | 완료 |
| `human_approval_block_rate` 반영 | 완료 |
| `data.top_k` 반영 | 기록용 필드. 현재 toy evaluator 계산에는 미사용 |
| PyYAML fallback | 완료. PyYAML이 없어도 자체 parser로 실행 가능 |
| `dependencies = []` 유지 | 완료 |
| Docker compose 실행 명령 문서화 | 완료 |

## 8. 한계

이 결과는 synthetic RAG document와 rule-based toy evaluator를 사용한 평가 형식 검증용 수치이며, 실제 LLM 보안 성능이나 실제 RAG 제품의 안전성으로 일반화하지 않는다.

실제 연구로 확장하려면 공개 benchmark, 복수 LLM, 복수 seed, 독립 라벨러 검토, source/provenance metadata schema, 안전한 red-team 절차가 필요하다.
