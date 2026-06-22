# 보안 이슈 30% 정리

## 1. 주요 보안 이슈

W08의 보안 핵심은 간접 프롬프트 인젝션이다. 사용자가 직접 악성 지시를 입력하지 않아도, 검색 문서·웹페이지·PDF·메모리·tool 결과에 포함된 지시가 RAG context로 들어오면 LLM이 이를 따라버릴 수 있다.

| 이슈 | 설명 | 대표 방어 |
|---|---|---|
| Prompt injection | 입력 지시로 모델 행동을 조작 | instruction/data 분리, policy check |
| Indirect prompt injection | 외부 문서에 숨은 지시가 context로 유입 | source verification, content sanitization |
| RAG 문서 오염 | vector DB나 corpus에 악성 문서가 포함 | ingestion 검증, provenance logging |
| 검색 결과 기반 지시문 오염 | 검색 상위 문서가 모델 지시를 바꿈 | reranking, trust score, context isolation |
| Tool-using agent 공격면 | 모델이 외부 도구를 잘못 호출 | permission policy, human approval |
| Context hijacking | retrieved context가 system/user instruction 경계를 흐림 | structured prompt, role separation |
| System prompt leakage | 내부 정책·secret이 답변에 노출 | secret minimization, output filtering |
| Safety-critical vulnerability | 의료·금융 등 고위험 도메인에서 위험 답변 생성 | domain gate, human-in-the-loop |
| 출처 검증 실패 | 답변 근거와 출처를 감사할 수 없음 | citation, metadata, audit log |
| Approval gate 부재 | 고위험 action이 자동 실행됨 | risk score 기반 승인 절차 |

## 2. CIA 관점 분석

| 관점 | 관련 위협 | 설명 |
|---|---|---|
| Confidentiality | System prompt leakage / sensitive context exposure | 검색 context나 agent memory가 내부 지시·민감정보를 노출할 수 있다. |
| Integrity | Prompt injection / document poisoning | 오염 문서가 답변 내용과 tool action을 바꿀 수 있다. |
| Availability | Retrieval manipulation / agent failure | 검색 결과 조작으로 정상 답변 품질이 떨어지거나 agent가 실패할 수 있다. |
| Privacy | User context leakage | 사용자 입력과 검색 context가 로그·도구 호출로 확산될 수 있다. |
| Safety | Unsafe answer in medical/safety domain | 의료 조언처럼 안전이 중요한 영역에서 위험한 권고가 생성될 수 있다. |
| Accountability | Source verification failure / audit gap | 어떤 근거로 답했는지 추적하지 못하면 책임 소재가 불명확해진다. |

## 3. 공격-방어-평가 분류

| 구분 | W08 정의 |
|---|---|
| 공격 자산 | 검색 문서, graph node/edge, vector DB, retrieved context, system prompt, tool permission |
| 공격자 능력 | 오염 문서 삽입, 외부 페이지 조작, context 지시문 삽입, tool 호출 유도 |
| 방어 방법 | source filter, metadata validation, context isolation, policy filter, human approval gate |
| 평가 지표 | ASR, Source Verification, Tool Misuse Rate, Faithfulness, Answer Rate, Block Rate |

## 4. 기말 논문 연결

기말 논문에서는 prompt injection 자체의 공격 절차보다 “RAG pipeline에서 어느 단계가 어떤 지표로 검증되어야 하는가”를 중심으로 다룬다. 이는 안전한 synthetic document 실험과 체크리스트 설계로 충분히 수행 가능하다.
