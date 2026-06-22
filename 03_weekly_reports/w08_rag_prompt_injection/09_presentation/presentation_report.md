# W08 발표용 보고서

## 1. 발표 메타정보

| 항목 | 내용 |
|---|---|
| 주차 | W08 |
| 주제 | RAG·프롬프팅 프레임워크 & 프롬프트 인젝션 |
| 발표 시간 | 8-10분 |
| 핵심 메시지 | RAG 보안은 답변 품질 문제가 아니라 검색 context, 출처 검증, tool 권한, human approval이 결합된 시스템 보안 문제다. |

## 2. 한 문장 요약과 발표 흐름

W08는 RAG와 prompting framework를 이해한 뒤, indirect prompt injection이 검색 문서와 tool action을 통해 어떻게 위험해지는지 설명하고, synthetic 실험으로 source filter와 human approval gate의 효과를 보여준다.

발표 흐름은 AI 원리, 보안 이슈, 논문 5편 역할, 실험 결과, 기말논문 연결 순서로 진행한다.

## 3. 논문 5편의 발표 역할

| 논문 | 발표 역할 |
|---|---|
| P01 GraphRAG survey | GraphRAG workflow와 graph element 기반 retrieval 설명 |
| P02 graph-based RAG survey | graph 기능과 provenance 검증 필요성 설명 |
| P03 prompting framework survey | Data/Base/Execute/Service level의 trust boundary 설명 |
| P04 prompt injection survey | direct/indirect/multimodal injection과 방어 taxonomy 설명 |
| P05 medical LLM vulnerability | safety-critical domain에서 prompt injection 위험 설명 |

## 4. AI 원리 70%와 보안 이슈 30%

RAG는 검색된 외부 지식을 LLM context에 넣어 답변을 생성한다. GraphRAG는 문서 사이 관계까지 이용하고, prompting framework는 prompt와 tool 실행을 application level에서 관리한다.

보안 이슈는 retrieved context가 지시문처럼 작동할 수 있다는 점에서 시작한다. 간접 인젝션은 사용자가 직접 공격하지 않아도 외부 문서가 모델 행동을 바꿀 수 있다. Agentic RAG에서는 이 문제가 tool misuse로 이어진다.

## 5. 실습/실험 실행 상태와 결과 근거

실습은 실제 LLM/API를 호출하지 않는 synthetic toy evaluator로 실행했다. 조건별 40개 sample, 총 160개 synthetic sample을 사용했고 seed는 42다.

| 조건 | Retrieval Relevance | ASR | Source Verification | Tool Misuse Rate | Faithfulness | Answer Rate |
|---|---:|---:|---:|---:|---:|---:|
| Clean RAG | 0.907887 | 0.000000 | 1.000000 | 0.000000 | 0.907613 | 0.950000 |
| Poisoned document | 0.690091 | 0.575000 | 0.275000 | 0.125000 | 0.458069 | 0.875000 |
| Source filter 적용 | 0.776926 | 0.050000 | 1.000000 | 0.025000 | 0.778693 | 0.800000 |
| Human approval 적용 | 0.764926 | 0.025000 | 1.000000 | 0.000000 | 0.840805 | 0.575000 |

결과 근거는 `04_experiment/outputs/run_log.md`, `metrics_summary.csv`, `results.json`이다.

## 6. 기말논문 연결 지점

추천 주제는 “RAG 기반 생성형 AI 시스템에서 간접 프롬프트 인젝션 대응을 위한 출처 검증·승인 게이트 평가 프레임워크”다. W08에서 확보한 위협모형, 평가 지표, synthetic 실험 구조를 기말논문의 연구방법과 분석 장에 반영할 수 있다.

## 7. 예상 질문과 답변

Q1. 왜 실제 LLM으로 공격 실험을 하지 않았는가?

A1. 이번 주차 목적은 안전한 평가 프로토콜과 기록 구조 검증이다. 실제 공격 payload나 live API 호출 없이도 ASR, source verification, tool misuse 같은 지표 체계를 설계할 수 있다.

Q2. Human approval gate는 항상 좋은 방어인가?

A2. tool misuse를 0.000000으로 낮췄지만 answer rate도 0.575000으로 낮아졌다. 따라서 고위험 action에만 선택적으로 적용하는 정책이 필요하다.

Q3. P05 의료 논문을 일반 RAG 연구에 어떻게 연결할 수 있는가?

A3. 의료 세부 payload가 아니라 safety-critical domain에서 prompt injection이 단순 품질 문제가 아니라 안전·책임 문제라는 점을 반영한다.
