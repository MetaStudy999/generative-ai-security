# W08 기여 후보

| 번호 | 기여 후보 | 설명 | 반영 장 |
|---:|---|---|---|
| 1 | RAG prompt injection 위협모형 | 검색 문서, vector DB, graph DB, retrieved context, tool action을 포함한 위협모형 | 연구문제/방법론 |
| 2 | 다중 지표 평가표 | ASR, source verification, tool misuse, faithfulness, answer rate를 함께 기록 | 실험/분석 |
| 3 | 출처 검증 메타데이터 체크리스트 | 문서 ID, 출처, 신뢰도, ingestion 시점, graph edge provenance 기록 | 방법론 |
| 4 | Human approval gate 설계 | 고위험 tool action을 자동 실행하지 않고 승인 로그로 남기는 통제 | 보안적 함의 |
| 5 | 재현성 로그 구조 | seed, config, script, CSV/JSON/run log 보존 | 연구윤리/재현성 |

## 핵심 기여문 초안

본 연구는 RAG 기반 생성형 AI 시스템의 간접 프롬프트 인젝션 위험을 검색 context와 tool action 관점에서 모델링하고, 출처 검증과 human approval gate의 효과를 ASR, source verification, tool misuse rate, faithfulness, answer rate로 함께 평가하는 재현 가능한 toy protocol을 제안한다.
