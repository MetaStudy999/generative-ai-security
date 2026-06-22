# 실험 보고서

## 1. 실험 목표

W08 실습은 RAG 기반 생성형 AI 시스템에서 간접 프롬프트 인젝션이 검색 context와 tool action에 미치는 위험을 안전한 synthetic 환경에서 평가하는 것이다. 실제 LLM, 외부 API, 실제 개인정보, 실제 공격 payload, live tool 호출은 사용하지 않았다.

핵심 질문은 “출처 검증 메타데이터와 human approval gate가 오염 문서 기반 ASR과 tool misuse를 낮추는지, 그리고 그 과정에서 retrieval relevance와 answer rate가 어떻게 변하는지 기록할 수 있는가”이다.

## 2. 환경

| 항목 | 내용 |
|---|---|
| OS | Ubuntu 24.04 기준 |
| Container | Docker 사용 가능, 호스트 `python3` 실행 검증 |
| Python | 3.11 계열 또는 호스트 `python3` |
| Package | 표준 라이브러리만 사용 |
| Seed | 42 |
| 데이터 | synthetic RAG documents, no personal data |
| 실행 명령 | `python3 src/run_experiment.py --config configs/config.yaml` |
| 결과 상태 | 실행 완료 |

## 3. 실행 절차

| 단계 | 설계 내용 | 결과 기록 |
|---|---|---|
| Synthetic query/doc 조건 생성 | Clean RAG, Poisoned document, Source filter, Human approval 조건별 40개 | 총 160개 synthetic sample |
| 오염 context 판정 | 조건별 poison probability와 source filter block rate 적용 | `results.json` sample log |
| RAG 보안 지표 계산 | Retrieval relevance, ASR, source verification, tool misuse, faithfulness, answer rate | `metrics_summary.csv` |
| 방어 효과 기록 | Source block rate와 human block rate 계산 | `run_log.md` |
| 재현성 보존 | config, seed, CSV, JSON, run log 저장 | `outputs/` 보존 |

## 4. 결과

정량값은 `outputs/run_log.md`, `outputs/metrics_summary.csv`, `outputs/results.json`과 일치한다.

| 조건 | Retrieval Relevance | ASR | Source Verification | Tool Misuse Rate | Faithfulness | Answer Rate | 해석 |
|---|---:|---:|---:|---:|---:|---:|---|
| Clean RAG | 0.907887 | 0.000000 | 1.000000 | 0.000000 | 0.907613 | 0.950000 | 정상 문서만 검색되는 기준 조건 |
| Poisoned document | 0.690091 | 0.575000 | 0.275000 | 0.125000 | 0.458069 | 0.875000 | 오염 문서가 context에 들어오면 ASR과 tool misuse가 증가 |
| Source filter 적용 | 0.776926 | 0.050000 | 1.000000 | 0.025000 | 0.778693 | 0.800000 | 출처 검증으로 ASR이 크게 낮아짐 |
| Human approval 적용 | 0.764926 | 0.025000 | 1.000000 | 0.000000 | 0.840805 | 0.575000 | 승인 게이트가 tool misuse를 0으로 낮추지만 answer rate도 감소 |

## 5. 해석

Poisoned document 조건에서는 ASR이 0.575000, tool misuse rate가 0.125000으로 나타났다. Source filter 적용 후 ASR은 0.050000으로 낮아졌고, source verification은 1.000000으로 올라갔다. Human approval 적용 조건에서는 ASR이 0.025000, tool misuse rate가 0.000000이었으나 answer rate는 0.575000으로 낮아졌다.

따라서 RAG prompt injection 방어는 단일 목표 최적화가 아니다. 출처 필터는 공격 성공을 줄이면서 답변 가능성을 비교적 유지하지만, human approval gate는 고위험 action 차단에는 강한 대신 사용성 비용이 생긴다.

## 6. 재현성 점검

- `configs/config.yaml`에 seed, sample 수, risk threshold, source filter block rate, human approval block rate를 기록했다.
- `src/run_experiment.py`는 동일 seed로 CSV/JSON/run log를 모두 생성한다.
- 실행 산출물은 `outputs/metrics_summary.csv`, `outputs/results.json`, `outputs/run_log.md`에 보존했다.
- 실제 공격 payload, 실제 개인정보, 외부 API 질의, 실제 tool 호출은 포함하지 않았다.

## 7. 한계

본 실습은 평가 프로토콜과 재현성 기록 구조를 설명하기 위한 synthetic toy 실험이다. 수치는 실제 LLM의 prompt injection 방어 성능, 실제 의료·금융 시스템 위험도, 실제 RAG 제품의 보안 수준으로 일반화하지 않는다.
