# 위협모형

| 항목 | 내용 |
|---|---|
| 대상 시스템 | RAG 기반 생성형 AI 시스템, Graph RAG, tool-using agent |
| 보호 자산 | 검색 문서, graph node/edge, vector DB, system prompt, user context, 생성 답변, tool 권한, audit log |
| 공격자 | 악성 문서 작성자, 외부 사용자, compromised content provider, 간접 지시문 삽입자 |
| 공격자의 지식 | Black-box 또는 Gray-box |
| 공격자의 능력 | 검색 대상 문서 오염, prompt injection 삽입, 출처 위조, tool 호출 유도, context 조작 |
| 공격 경로 | 웹페이지, PDF, 검색 corpus, vector DB, graph DB, retrieved context, agent tool call |
| 공격 성공 조건 | 오염 지시가 모델 답변 또는 tool action에 반영됨 |
| 방어자 가정 | 문서 출처 검증, 검색 결과 필터링, tool permission, human approval, 로그 보존 가능 |
| 제외 범위 | 실제 외부 시스템 공격, 실제 의료·금융 시스템 조작, 불법 데이터 접근, live API 공격 |

## 공격 시나리오

| 시나리오 | 설명 | 평가 지표 |
|---|---|---|
| Clean RAG | 정상 문서만 검색되는 기준 조건 | Retrieval Relevance, Faithfulness |
| Poisoned document | 오염 문서가 검색 context에 포함 | ASR, Tool Misuse Rate |
| Source filter 적용 | 출처·메타데이터 검증으로 오염 문서 차단 | Source Verification, Source Block Rate |
| Human approval 적용 | 고위험 action을 사람 승인으로 차단 | Human Block Rate, Tool Misuse Rate |

## 안전 원칙

본 위협모형은 synthetic document 기반 평가와 방어 설계를 위한 것이다. 실제 prompt injection payload 재현, 실제 서비스 공격, 실제 환자·개인정보 처리, 무단 tool 호출은 포함하지 않는다.
