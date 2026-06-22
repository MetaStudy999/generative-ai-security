# W08 RAG·프롬프팅 프레임워크 & 프롬프트 인젝션 통합보고서 초안

본 초안은 최종본과 같은 구조와 수치를 사용한다. 최종 제출용 정리본은 `../final/integrated_report_final.md`를 기준으로 한다.

## 핵심 요약

W08는 RAG 시스템의 간접 프롬프트 인젝션 위험을 GraphRAG, prompting framework, prompt injection survey, 의료 LLM 취약성 연구를 통해 정리하고, synthetic toy 실험으로 source filter와 human approval gate의 효과를 기록했다.

## 실험 요약

| 조건 | Retrieval Relevance | ASR | Source Verification | Tool Misuse Rate | Faithfulness | Answer Rate |
|---|---:|---:|---:|---:|---:|---:|
| Clean RAG | 0.907887 | 0.000000 | 1.000000 | 0.000000 | 0.907613 | 0.950000 |
| Poisoned document | 0.690091 | 0.575000 | 0.275000 | 0.125000 | 0.458069 | 0.875000 |
| Source filter 적용 | 0.776926 | 0.050000 | 1.000000 | 0.025000 | 0.778693 | 0.800000 |
| Human approval 적용 | 0.764926 | 0.025000 | 1.000000 | 0.000000 | 0.840805 | 0.575000 |

## 초안 검토 메모

- P01 DOI는 미확정으로 유지한다.
- P02-P05 DOI는 PDF 첫 페이지 기준으로 확인했다.
- 실험 수치는 `04_experiment/outputs/`의 CSV/JSON/run log와 일치한다.
- 실제 LLM/API, 실제 개인정보, live tool 호출, 실제 공격 payload는 포함하지 않는다.
