# W08 RAG·프롬프팅 프레임워크 & 프롬프트 인젝션 통합보고서

## 0. 메타정보

| 항목 | 내용 |
|---|---|
| 주차 | W08 |
| 주제 | RAG·프롬프팅 프레임워크 & 프롬프트 인젝션 |
| AI 원리 | RAG, Graph RAG, retrieval, reranking, generation, prompting framework |
| 보안 이슈 | Prompt injection, indirect injection, RAG 문서 오염, tool misuse |
| 문서 상태 | 최종본 |
| 실험 상태 | synthetic toy 실험 실행 완료 |
| 실행 근거 | `04_experiment/outputs/run_log.md`, `metrics_summary.csv`, `results.json` |

## 1. 한 문장 요약

W08는 RAG 시스템을 “검색된 외부 context와 tool action이 연결된 LLM application”으로 보고, 간접 프롬프트 인젝션 위험을 source verification과 human approval gate로 줄일 수 있는지 synthetic 실험과 문헌분석으로 정리한다.

## 2. AI 원리 70% 정리

RAG는 query를 입력받아 외부 문서나 graph DB에서 관련 근거를 검색하고, reranking과 context construction을 거쳐 LLM 답변을 생성한다. GraphRAG는 node, edge, path, subgraph처럼 관계 구조를 검색과 생성에 활용한다. Prompting framework는 data, base, execute, service level로 LLM application을 구성하며, system prompt, user prompt, retrieved context, tool instruction의 경계를 관리한다.

| 개념 | W08 해석 | 보안 연결 |
|---|---|---|
| Retrieval | 질문과 관련된 문서나 graph element를 찾음 | 오염 문서가 유입될 수 있음 |
| Reranking | 관련성·신뢰도 기준으로 후보 순위를 조정 | trust score와 source verification 필요 |
| Generation | 검색 context를 근거로 답변 생성 | context hijacking과 faithfulness 저하 가능 |
| GraphRAG | 관계 기반 검색과 multi-hop reasoning | node/edge provenance 검증 필요 |
| Prompting Framework | prompt, tool, service 실행 계층 | tool misuse와 approval gate 필요 |

## 3. 보안 이슈 30% 정리

Prompt injection은 모델이 instruction과 data를 안정적으로 구분하지 못할 때 발생한다. RAG에서는 악성 지시가 사용자의 직접 입력이 아니라 검색 문서, 웹페이지, PDF, graph element, tool result를 통해 간접적으로 들어올 수 있다.

| 관점 | 관련 위협 | 평가 연결 |
|---|---|---|
| Confidentiality | system prompt leakage, sensitive context exposure | source/log 관리 |
| Integrity | indirect injection, document poisoning | ASR, faithfulness |
| Availability | retrieval manipulation, agent failure | answer rate |
| Privacy | user context leakage | 개인정보 미사용, 로그 최소화 |
| Safety | unsafe answer in medical/safety domain | approval gate, domain review |
| Accountability | source verification failure, audit gap | metadata, run log |

## 4. 논문 5편 요약

| ID | 문헌 | 역할 | DOI/URL 상태 |
|---|---|---|---|
| P01 | Peng et al., *Graph Retrieval-Augmented Generation: A Survey* | GraphRAG workflow와 graph-based indexing/retrieval/generation 정리 | arXiv `2408.08921`, DOI 미확정 |
| P02 | Zhu et al., *Graph-Based Approaches and Functionalities in Retrieval-Augmented Generation* | graph 기능을 database, algorithm, pipeline, task로 분류 | DOI `10.1145/3795880` |
| P03 | Liu et al., *Prompting Frameworks for Large Language Models* | prompting framework의 data/base/execute/service level 정리 | DOI `10.1145/3789253` |
| P04 | Geng et al., *Prompt Injection Attacks on Large Language Models* | prompt injection 공격·원인·방어 taxonomy | DOI `10.32604/cmc.2025.074081` |
| P05 | Lee et al., *Vulnerability of LLMs to Prompt Injection When Providing Medical Advice* | safety-critical domain에서 prompt injection 취약성 실험 사례 | DOI `10.1001/jamanetworkopen.2025.49963` |

## 5. 논문 5편 비교

P01/P02는 RAG와 GraphRAG의 구조를 설명하고, P03은 prompt와 tool orchestration의 engineering layer를 제공한다. P04는 prompt injection 보안 taxonomy를, P05는 의료 조언이라는 safety-critical 사례를 제공한다. 다섯 편을 합치면 “외부 context를 믿기 전에 출처와 권한을 검증해야 한다”는 결론으로 이어진다.

## 6. Research Track

### 6.1 연구문제

RQ1. RAG 시스템에서 간접 프롬프트 인젝션은 검색 문서, prompt 구성, generation, tool action 중 어느 단계에서 가장 큰 위험을 유발하는가?

RQ2. 문서·graph 출처 검증 메타데이터는 RAG 답변의 faithfulness와 prompt injection 방어에 어떤 도움을 줄 수 있는가?

RQ3. Agentic RAG 환경에서 human approval gate와 tool permission policy는 ASR과 tool misuse rate를 얼마나 줄일 수 있는가?

### 6.2 위협모형

| 항목 | 내용 |
|---|---|
| 대상 시스템 | RAG 기반 생성형 AI 시스템, Graph RAG, tool-using agent |
| 보호 자산 | 검색 문서, graph node/edge, vector DB, system prompt, user context, 생성 답변, tool 권한 |
| 공격자 | 악성 문서 작성자, 외부 사용자, compromised content provider |
| 공격 경로 | 웹페이지, PDF, vector DB, graph DB, retrieved context, agent tool call |
| 성공 조건 | 오염 지시가 모델 응답 또는 tool action에 반영됨 |
| 방어자 가정 | source filter, metadata validation, tool permission, human approval 가능 |
| 제외 범위 | 실제 외부 시스템 공격, 실제 의료·금융 시스템 조작, 불법 데이터 접근 |

### 6.3 평가방법

| 평가 항목 | 지표 | W08 실습 연결 |
|---|---|---|
| Retrieval 품질 | Retrieval Relevance | 검색 context 품질 |
| 답변 충실도 | Faithfulness | 근거 왜곡 여부 |
| 공격 효과 | ASR | 오염 지시 반영률 |
| 출처 검증 | Source Verification | 신뢰 가능한 context 비율 |
| 도구 오남용 | Tool Misuse Rate | 비인가 action 위험 |
| 승인 효과 | Human Block Rate | 고위험 action 차단 |
| 재현성 | seed/config/log | outputs 3종 보존 |

### 6.4 재현성

실험은 seed 42, 조건별 40개 synthetic sample, risk threshold 0.55로 실행했다. 산출물은 `04_experiment/outputs/metrics_summary.csv`, `results.json`, `run_log.md`에 저장했다. 실제 LLM/API 호출이 없으므로 수치는 모델 성능이 아니라 평가 프로토콜과 기록 구조 검증용이다.

### 6.5 한계와 오픈문제

P01 DOI는 미확정이며, toy evaluator의 수치는 실제 RAG 제품 보안성으로 일반화할 수 없다. 실제 연구로 확장하려면 공개 benchmark, 복수 모델, 복수 seed, graph provenance 라벨, 사람 평가자 간 agreement가 필요하다.

## 7. 실습 요약

| 조건 | Retrieval Relevance | ASR | Source Verification | Tool Misuse Rate | Faithfulness | Answer Rate |
|---|---:|---:|---:|---:|---:|---:|
| Clean RAG | 0.907887 | 0.000000 | 1.000000 | 0.000000 | 0.907613 | 0.950000 |
| Poisoned document | 0.690091 | 0.575000 | 0.275000 | 0.125000 | 0.458069 | 0.875000 |
| Source filter 적용 | 0.776926 | 0.050000 | 1.000000 | 0.025000 | 0.778693 | 0.800000 |
| Human approval 적용 | 0.764926 | 0.025000 | 1.000000 | 0.000000 | 0.840805 | 0.575000 |

Source filter는 ASR을 0.575000에서 0.050000으로 낮췄고, human approval gate는 tool misuse rate를 0.000000으로 낮췄다. 다만 approval gate 조건에서는 answer rate가 0.575000으로 낮아져 보안성과 사용성의 균형을 함께 봐야 한다.

## 8. AI 활용 기록 요약

Codex를 사용해 로컬 파일 점검, PDF 첫 페이지 기반 서지 보정, synthetic 실험 코드 작성, 실행 결과 정리, 제출본과 발표자료 작성을 수행했다. 정량값은 `outputs/run_log.md`, `metrics_summary.csv`, `results.json`에 있는 값만 사용했다.

## 9. 토론 질문

1. RAG 보안에서 ASR 감소와 answer rate 유지 중 어느 쪽을 우선해야 하는가?
2. GraphRAG의 node/edge provenance를 문서 출처 검증과 같은 방식으로 다룰 수 있는가?
3. Human approval gate는 어떤 risk threshold에서 자동화와 사람 검토의 균형을 잡아야 하는가?

## 10. 기말 논문 연결

W08는 기말논문의 핵심 후보 주제인 “RAG 기반 생성형 AI 시스템에서 간접 프롬프트 인젝션 대응을 위한 출처 검증·승인 게이트 평가 프레임워크”로 직접 연결된다. 관련연구에는 GraphRAG와 prompting framework 문헌을, 방법론에는 synthetic document 실험과 다중 보안 지표를 반영한다.

## 11. 참고문헌 검증표

참고문헌 검증 상태는 `01_papers/doi_check.md`에 관리한다. P01은 arXiv ID만 확정하고 DOI는 미확정으로 유지했다. P02-P05는 PDF 첫 페이지 기준 DOI를 확인했다.

## 12. 자기 점검

| 항목 | 상태 |
|---|---|
| 논문 5편 요약 | 완료 |
| 비교표 | 완료 |
| AI 원리 70% | 완료 |
| 보안 이슈 30% | 완료 |
| Research Track | 완료 |
| synthetic 실험 코드 | 완료 |
| 실행 로그/CSV/JSON | 완료 |
| 제출용 보고서 | 완료 |
| 발표자료 | 완료 |
| AI 활용 고지 | 완료 |
| DOI 임의 생성 방지 | 완료 |
