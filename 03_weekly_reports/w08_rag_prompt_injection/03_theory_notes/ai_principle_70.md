# AI 원리 70% 정리

## 1. 핵심 이론

RAG는 LLM이 답을 생성하기 전에 외부 지식 저장소에서 관련 문서를 검색하고, 그 근거를 prompt context에 넣어 답변을 생성하는 구조다. 기본 pipeline은 query 입력, embedding 또는 sparse retrieval, reranking, context construction, generation, citation/audit logging 순서로 볼 수 있다.

Graph RAG는 여기에 entity, relation, path, subgraph 같은 구조 정보를 추가한다. 단순히 유사한 chunk를 찾는 것이 아니라 문서 사이 관계와 multi-hop path를 활용해 더 넓은 맥락을 구성한다. Prompting framework는 이 RAG pipeline을 template, memory, tool, service orchestration과 연결하는 공학적 구조다.

## 2. 핵심 개념표

| 개념 | 정의 | 직관적 설명 | 관련 논문 |
|---|---|---|---|
| RAG | 검색된 외부 지식을 LLM 생성 context에 결합하는 방식 | 모델 기억만 믿지 않고 근거 자료를 함께 주는 방식 | P01, P02 |
| Retrieval | query와 관련 문서를 후보로 찾는 단계 | 도서관 색인에서 관련 책을 찾는 과정 | P01, P02 |
| Reranking | 후보 문서의 순위를 다시 매기는 단계 | 처음 찾은 자료 중 더 믿을 만한 것을 위로 올림 | P01, P02 |
| Generation | 검색 context를 바탕으로 답변을 생성하는 단계 | 찾은 자료를 읽고 요약 답안을 작성 | P01, P02 |
| Graph RAG | graph 구조를 indexing, retrieval, generation에 쓰는 RAG | 문서 사이 연결선까지 같이 읽는 RAG | P01, P02 |
| Prompting Framework | prompt, context, tool, service 실행을 관리하는 framework | LLM 앱을 조립하는 실행 프레임 | P03 |
| System Prompt | 모델 행동 규칙을 정하는 상위 지시 | 운영 정책과 역할 규칙 | P03, P04 |
| User Prompt | 사용자가 직접 입력하는 요청 | 질문 또는 작업 지시 | P03, P04 |
| Tool Instruction | 외부 도구 호출 조건과 권한 지시 | API를 언제 어떻게 부를지 정하는 규칙 | P03 |
| Retrieved Context | 검색 문서가 prompt에 삽입된 부분 | 답변 근거지만 오염될 수 있는 영역 | P01, P04 |
| Groundedness | 답변이 검색 근거에 기반하는 정도 | 근거 없는 말이 아닌지 확인 | P01, P02 |
| Faithfulness | 답변이 근거 내용을 왜곡하지 않는 정도 | 자료에 충실한 답변인지 확인 | P01, P02 |
| Relevance | 검색 문서가 질문과 관련 있는 정도 | 엉뚱한 문서를 가져오지 않았는지 확인 | P01, P02 |

## 3. 수식 또는 알고리즘

```text
Query q
  -> retrieve top-k documents D_k from corpus/vector DB/graph DB
  -> rerank D_k by relevance, trust, freshness
  -> build context C = system prompt + user prompt + verified evidence
  -> generate answer y = LLM(C)
  -> log evidence ids, source metadata, risk flags
```

W08 실습에서는 실제 LLM 호출 대신 synthetic evaluator를 사용했다. 따라서 `Retrieval Relevance`, `Faithfulness`, `Answer Rate`는 모델 성능 수치가 아니라 평가 기록 구조를 검증하기 위한 toy metric이다.

## 4. 초보자용 설명

RAG는 “검색해서 답하는 LLM”이다. 그런데 검색된 문서 안에 모델에게 몰래 지시하는 문장이 있으면, LLM은 그것을 근거 자료가 아니라 명령처럼 받아들일 수 있다. Graph RAG에서는 문서 본문뿐 아니라 문서 사이 연결 관계도 근거가 되므로, 어떤 문서와 관계를 믿을 수 있는지 함께 확인해야 한다.

## 5. 보안 연구와의 연결

RAG 보안은 retrieval 품질만 보는 문제가 아니다. 검색된 문서가 정상인지, 출처가 검증되었는지, context에 들어간 지시가 system prompt보다 우선되지 않는지, tool action이 사람 승인 없이 실행되지 않는지까지 봐야 한다. 그래서 W08 평가는 `ASR`, `Source Verification`, `Tool Misuse Rate`, `Faithfulness`, `Answer Rate`를 함께 기록한다.
