# W08 1페이지 핸드아웃

## 핵심 메시지

RAG 보안은 검색 정확도만의 문제가 아니다. 검색 문서의 출처, prompt boundary, tool 권한, human approval, audit log를 함께 설계해야 indirect prompt injection을 줄일 수 있다.

## AI 원리

| 구성요소 | 의미 |
|---|---|
| RAG | 외부 문서를 검색해 LLM context에 넣고 답변 생성 |
| GraphRAG | node, edge, path, subgraph를 활용한 관계 기반 RAG |
| Prompting Framework | prompt, memory, tool, service 실행을 관리하는 LLM app 구조 |

## 보안 이슈

| 이슈 | 위험 | 대응 |
|---|---|---|
| Indirect prompt injection | 외부 문서가 모델 지시처럼 작동 | source verification |
| RAG 문서 오염 | vector DB/corpus에 악성 문서 포함 | ingestion 검증, metadata |
| Tool misuse | agent가 부적절한 tool action 수행 | permission policy, human approval |
| Safety-critical failure | 의료 등 고위험 조언 왜곡 | domain review, approval gate |

## W08 실험 결과

| 조건 | ASR | Source Verification | Tool Misuse |
|---|---:|---:|---:|
| Clean RAG | 0.000000 | 1.000000 | 0.000000 |
| Poisoned document | 0.575000 | 0.275000 | 0.125000 |
| Source filter 적용 | 0.050000 | 1.000000 | 0.025000 |
| Human approval 적용 | 0.025000 | 1.000000 | 0.000000 |

## 기말논문 연결

추천 주제: RAG 기반 생성형 AI 시스템에서 간접 프롬프트 인젝션 대응을 위한 출처 검증·승인 게이트 평가 프레임워크.

## 한계

본 실험은 synthetic toy evaluator 결과이며 실제 LLM/RAG 제품의 보안 성능으로 일반화하지 않는다.

<!-- formula-visual-handout:start -->
## 수식·그래프·그림 보강 요약

| 항목 | 반영 내용 |
|---|---|
| 핵심 수식 | Retrieval Score와 Context-Conditioned Generation, Injection Success와 Contamination Rate |
| 그래프 | `assets/charts/w08_metrics_chart.png` (`metrics_summary.csv` 기반) |
| 다이어그램 | `assets/diagrams/w08_pipeline_diagram.svg` (RAG pipeline threat model) |
| 기호 정의 | 통합보고서와 발표 슬라이드의 수식 블록에 포함 |
| 주의사항 | prompt injection은 방어 평가 관점으로만 설명하고 실제 우회 절차는 제공하지 않는다. |
<!-- formula-visual-handout:end -->
