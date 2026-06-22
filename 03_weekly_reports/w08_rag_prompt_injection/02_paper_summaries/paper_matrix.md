# W08 논문 5편 비교표

| 논문 | 연구문제 | 핵심 방법 | 데이터/실험 | AI 원리 기여 | 보안 위협 연결 | 평가 지표 | 한계 | 내 논문 활용 |
|---|---|---|---|---|---|---|---|---|
| P01 | GraphRAG는 어떤 workflow와 기술 요소로 구성되는가 | GraphRAG workflow, indexing, retrieval, generation survey | arXiv/PDF 기준 문헌조사 | graph-based retrieval, node/edge/path/subgraph 기반 reasoning | graph node/edge poisoning, 관계 기반 context manipulation | downstream task, retrieval/generation evaluation, graph provenance | DOI placeholder, ACM 출판정보 확인 필요, 강의계획서 Shiyu Chen et al. 표기와 동일 여부 확인 필요 | GraphRAG 단계별 공격면 정의 |
| P02 | Graph 기능은 RAG pipeline에서 어떤 역할을 하는가 | database, algorithm, pipeline, task 차원의 graph functionality taxonomy | ACM CSUR survey | graph-based augmentation과 provenance 확장 | poisoned edge/path, source spoofing, provenance failure | graph function category, retrieval quality, source verification | 강의계획서 Jianxiang Li et al. 표기와 현재 DOI 기준 Zulun Zhu et al. 차이 확인 필요 | source verification 범위를 graph element까지 확장 |
| P03 | Prompting framework는 LLM application 생명주기를 어떻게 설명하는가 | data/base/execute/service level taxonomy | ACM CSUR survey | prompt, tool, service orchestration 구조 | tool instruction pollution, prompt boundary failure, service-level audit gap | framework layer, lifecycle component, audit point | 공격 성공률 직접 실험은 아님 | agentic RAG trust boundary 설계 |
| P04 | Prompt injection의 공격 유형, 원인, 방어는 무엇인가 | systematic review of attack methods, root causes, defense strategies | 2022-2025년 prompt injection 연구 종합 | instruction/data boundary 실패 설명 | direct/indirect injection, multimodal injection, tool misuse | ASR, detection rate, protection rate, defense taxonomy | 연구별 환경 차이로 수치 직접 비교 제한, Tianlei/Tongcheng Geng 표기 차이 확인 필요 | ASR/source/tool 지표의 보안 근거 |
| P05 | Safety-critical domain에서 prompt injection은 어떤 피해를 만들 수 있는가 | medical advice prompt injection vulnerability study | patient-LLM dialogue 또는 의료 조언 시나리오 | 안전중요 도메인에서 LLM application 평가 | unsafe medical advice, persistence, harm potential | injection success, persistence, harm level, safety review | 의료 도메인 중심, 강의계획서 제목과 현재 제목 차이 확인 필요 | human approval gate와 domain review 필요성 근거 |

## 종합 비교

### 1. 문헌별 역할

P01/P02는 GraphRAG와 graph-based RAG 구조 문헌이다. P01은 GraphRAG workflow를 graph-based indexing, graph-guided retrieval, graph-enhanced generation으로 정리하고, P02는 graph 기능을 database, algorithm, pipeline, task 수준으로 세분화한다.

P03은 prompting framework와 agentic LLM application layer 문헌이다. Data, base, execute, service level은 RAG 시스템에서 context, prompt template, tool action, 서비스 운영의 trust boundary를 구분하는 데 유용하다.

P04는 prompt injection taxonomy와 방어전략 문헌이다. Direct, indirect, multimodal injection과 방어 접근을 정리하므로 W08 실습의 ASR, source verification, tool misuse 지표의 근거가 된다.

P05는 safety-critical medical advice 사례 문헌이다. 의료 조언 환경에서는 prompt injection이 단순 답변 품질 문제가 아니라 실제 위해 가능성과 규제·승인 절차 문제로 확대될 수 있음을 보여준다.

### 2. W08 핵심 연결부

W08의 핵심 연결부는 retrieved context를 신뢰하기 전에 source, provenance, tool permission, human approval을 검증해야 한다는 점이다. GraphRAG에서는 검증 대상이 문서 chunk에서 node, edge, path, subgraph provenance로 확장되고, agentic RAG에서는 tool permission과 approval gate가 추가된다.

### 3. 실험과 문헌의 관계

W08 toy 실험은 실제 RAG/LLM 제품 평가가 아니라 ASR, source verification, tool misuse, faithfulness, answer rate 기록 구조를 설명하는 synthetic 실험이다. 따라서 Poisoned document 조건의 ASR 0.575000은 실제 제품 공격 성공률이 아니라, 평가 프로토콜이 오염 context와 방어 조건을 분리해 기록할 수 있음을 보이는 수치다.

### 4. 아직 해결되지 않은 문제

GraphRAG와 prompting framework 문헌은 보안 지표가 부족하고, prompt injection survey와 의료 실험은 각 도메인·모델·설정 차이 때문에 일관된 평가 프로토콜이 부족하다. 또한 P01, P02, P04, P05는 강의계획서 지정 정보와 현재 로컬 PDF/DOI 기준 정보가 달라 최종 제출 전 사람 검토가 필요하다.

### 5. 기말 논문 주제로 발전 가능한 연결부

W08의 가장 강한 연결부는 "RAG 기반 생성형 AI 시스템에서 간접 프롬프트 인젝션 대응을 위한 출처 검증·tool 승인·재현성 평가 프레임워크"다. 이는 문헌분석, synthetic document 모의실험, source/provenance 체크리스트, approval gate 정책 설계로 수행 가능하다.
