# 핵심 용어

| 용어 | 정의 | W08에서의 의미 |
|---|---|---|
| RAG | Retrieval-Augmented Generation | 검색 근거를 LLM context에 넣어 답변하는 구조 |
| Graph RAG | Graph structure를 활용하는 RAG | node/edge/path까지 검증 대상이 됨 |
| Vector DB | embedding 기반 검색 저장소 | 오염 문서가 들어가면 간접 인젝션 경로가 됨 |
| Reranking | 검색 후보 재정렬 | 관련성뿐 아니라 출처 신뢰도도 반영해야 함 |
| Prompting Framework | prompt와 tool 실행을 관리하는 구조 | Data/Base/Execute/Service level의 trust boundary |
| Prompt Injection | 지시문으로 모델 행동을 조작하는 공격 | 직접 입력 또는 검색 context를 통해 발생 |
| Indirect Injection | 외부 자료에 숨은 지시가 모델에 전달되는 공격 | RAG에서 특히 중요한 공격면 |
| Groundedness | 답변이 근거에 기반하는 정도 | 환각과 근거 없는 조작을 줄이는 평가축 |
| Faithfulness | 답변이 근거를 왜곡하지 않는 정도 | 오염 context가 들어오면 급락할 수 있음 |
| Source Verification | 출처와 메타데이터 검증 | W08 실험의 핵심 방어 지표 |
| Tool Misuse | 비인가 또는 부적절한 tool 호출 | agentic RAG에서 human approval 필요 |
| Human Approval Gate | 고위험 action 전 사람 승인을 요구하는 통제 | ASR과 tool misuse를 낮추는 운영 방어 |
