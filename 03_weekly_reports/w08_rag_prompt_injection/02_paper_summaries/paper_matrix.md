# W08 논문 5편 비교표

| 논문 | 연구문제 | 핵심 방법 | 데이터/실험 | 보안 위협 | 평가 지표 | 한계 | 내 논문 활용 |
|---|---|---|---|---|---|---|---|
| P01 | GraphRAG는 어떤 workflow와 기술 요소로 구성되는가 | GraphRAG survey, workflow formalization | 문헌조사, arXiv PDF | graph node/edge 오염, 관계 기반 context 조작 | downstream task, evaluation methodology 분류 | DOI placeholder, 보안 실험 없음 | GraphRAG 단계별 공격면 정의 |
| P02 | graph 기능은 RAG pipeline에서 어떤 역할을 하는가 | graph functionality taxonomy | ACM CSUR survey | graph provenance 부재, poisoned edge/path | database, algorithm, pipeline, task 분류 | prompt injection 방어 직접 실험 아님 | source verification 범위를 graph element까지 확장 |
| P03 | prompting framework를 어떤 생명주기로 설명할 수 있는가 | Data/Base/Execute/Service level taxonomy | ACM CSUR survey | tool instruction 오염, service-level audit gap | framework layer, lifecycle component | 공격 성공률 측정 없음 | agentic RAG trust boundary 설계 |
| P04 | prompt injection의 공격 유형, 원인, 방어는 무엇인가 | systematic review | 2022-2025년 연구 128편 종합 | direct, indirect, multimodal injection | ASR, detection/protection rate, defense taxonomy | 연구별 환경 달라 수치 직접 비교 제한 | ASR/source/tool 지표의 근거 |
| P05 | 의료 조언 LLM은 prompt injection에 얼마나 취약한가 | controlled simulation | 216 patient-LLM dialogue, POC validation | safety-critical advice manipulation | injection success, persistence, harm level | 의료 도메인 중심, payload 공개 제한 | Safety와 approval gate 필요성 근거 |

## 종합 비교

### 1. 공통적으로 다루는 문제

다섯 편은 RAG/LLM application에서 외부 context가 모델 행동을 바꾼다는 점을 공통으로 보여준다. P01/P02는 검색 context와 graph 구조를, P03은 prompt와 tool orchestration을, P04/P05는 prompt injection의 공격·방어·안전성 문제를 다룬다.

### 2. 논문 간 차이점

P01/P02는 AI 원리와 시스템 구조 중심이고, P03은 prompting framework의 engineering layer를 정리한다. P04는 prompt injection 전반의 보안 taxonomy이며, P05는 의료 도메인에서 실제로 위험한 권고가 유도될 수 있음을 실험적으로 보여주는 safety-critical 사례다.

### 3. 아직 해결되지 않은 문제

GraphRAG와 prompting framework 문헌은 보안 지표가 부족하고, prompt injection survey와 의료 실험은 각 도메인·모델·설정 차이 때문에 일관된 평가 프로토콜이 부족하다. 따라서 W08 연구는 ASR만이 아니라 source verification, tool misuse, faithfulness, answer rate를 함께 기록해야 한다.

### 4. 기말 논문 주제로 발전 가능한 연결부

W08의 가장 강한 연결부는 “RAG 기반 생성형 AI 시스템에서 간접 프롬프트 인젝션 대응을 위한 출처 검증·tool 승인·재현성 평가 프레임워크”다. 이는 문헌분석, synthetic document 모의실험, 체크리스트 설계로 수행 가능하다.
