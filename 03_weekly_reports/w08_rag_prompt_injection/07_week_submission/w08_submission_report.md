# W08 제출용 보고서

## 표지

| 항목 | 내용 |
|---|---|
| 주차 | W08 |
| 보고서 제목 | RAG·프롬프팅 프레임워크 & 프롬프트 인젝션 |
| 과목 범위 | AI 보안 |
| 작성일 | 2026-06-22 |
| 문서 상태 | 제출용 통합본 |
| 관련 산출물 위치 | `03_weekly_reports/w08_rag_prompt_injection/` |
| 실험 근거 | `04_experiment/outputs/run_log.md` |

## 초록

본 보고서는 RAG, GraphRAG, prompting framework의 기본 구조를 AI 원리 관점에서 정리하고, prompt injection, indirect injection, RAG 문서 오염, tool misuse를 보안 이슈 관점에서 분석한다. 문헌 5편을 통해 GraphRAG workflow, graph-based RAG 기능, prompting framework 계층, prompt injection taxonomy, 의료 LLM 취약성 사례를 비교했다. 실습에서는 실제 LLM/API를 호출하지 않고 synthetic RAG document와 rule-based toy evaluator를 사용해 source filter와 human approval gate의 효과를 측정했다. Poisoned document 조건의 ASR은 0.575000이었고, Source filter 적용 후 0.050000, Human approval 적용 후 0.025000으로 낮아졌다.

**키워드:** RAG, GraphRAG, prompt injection, indirect injection, source verification, tool misuse, human approval

## 1. AI 원리 70%

RAG는 query를 기반으로 외부 문서나 graph DB에서 관련 근거를 검색하고, reranking 후 LLM context에 넣어 답변을 생성한다. GraphRAG는 node, edge, path, subgraph처럼 관계 구조를 retrieval과 generation에 활용한다. Prompting framework는 data, base, execute, service level로 LLM application을 구성한다.

## 2. 보안 이슈 30%

| 관점 | 관련 위협 | W08 평가 연결 |
|---|---|---|
| Confidentiality | system prompt leakage, sensitive context exposure | source/log 관리 |
| Integrity | indirect injection, document poisoning | ASR, faithfulness |
| Availability | retrieval manipulation, agent failure | answer rate |
| Privacy | user context leakage | 개인정보 미사용 |
| Safety | unsafe advice in safety-critical domain | approval gate |
| Accountability | source verification failure | metadata, run log |

## 3. 문헌 요약

| ID | 문헌 | DOI/URL 상태 | 활용 |
|---|---|---|---|
| P01 | Peng et al., *Graph Retrieval-Augmented Generation: A Survey* | arXiv `2408.08921`, DOI 미확정 | GraphRAG workflow |
| P02 | Zhu et al., *Graph-Based Approaches and Functionalities in RAG* | DOI `10.1145/3795880` | graph 기능과 provenance |
| P03 | Liu et al., *Prompting Frameworks for Large Language Models* | DOI `10.1145/3789253` | prompting framework 계층 |
| P04 | Geng et al., *Prompt Injection Attacks on LLMs* | DOI `10.32604/cmc.2025.074081` | 공격·원인·방어 taxonomy |
| P05 | Lee et al., *Vulnerability of LLMs to Prompt Injection When Providing Medical Advice* | DOI `10.1001/jamanetworkopen.2025.49963` | safety-critical 취약성 사례 |

## 4. Research Track

| 항목 | 내용 |
|---|---|
| 연구문제 | RAG 시스템에서 indirect injection과 tool misuse를 source verification과 human approval gate로 줄일 수 있는가 |
| 대상 시스템 | RAG 기반 생성형 AI 시스템, Graph RAG, tool-using agent |
| 보호 자산 | 검색 문서, graph node/edge, vector DB, system prompt, user context, 생성 답변, tool 권한 |
| 위협 | 문서 오염, context hijacking, source spoofing, tool misuse |
| 평가 지표 | Retrieval Relevance, ASR, Source Verification, Tool Misuse Rate, Faithfulness, Answer Rate |
| 재현성 | seed 42, config, script, CSV/JSON/run log 보존 |
| 제외 범위 | 실제 외부 시스템 공격, 실제 개인정보 사용, 실제 의료·금융 시스템 조작, live tool 호출 |

## 5. 실습/실험 결과

| 조건 | Retrieval Relevance | ASR | Source Verification | Tool Misuse Rate | Faithfulness | Answer Rate | 해석 |
|---|---:|---:|---:|---:|---:|---:|---|
| Clean RAG | 0.907887 | 0.000000 | 1.000000 | 0.000000 | 0.907613 | 0.950000 | 정상 기준 |
| Poisoned document | 0.690091 | 0.575000 | 0.275000 | 0.125000 | 0.458069 | 0.875000 | 오염 context 유입 위험 |
| Source filter 적용 | 0.776926 | 0.050000 | 1.000000 | 0.025000 | 0.778693 | 0.800000 | 출처 검증으로 ASR 감소 |
| Human approval 적용 | 0.764926 | 0.025000 | 1.000000 | 0.000000 | 0.840805 | 0.575000 | tool misuse 차단, answer rate 감소 |

이 결과는 synthetic toy 실험의 평가 형식 검증용 수치다. 실제 LLM 보안 성능이나 실제 RAG 제품의 안전성으로 일반화하지 않는다.

## 6. 발표자료 위치

| 파일 | 용도 |
|---|---|
| `09_presentation/presentation_report.md` | 발표용 보고서 |
| `09_presentation/presentation_slides.md` | 슬라이드 원본 |
| `09_presentation/presentation_slides.html` | 브라우저 발표용 슬라이드 |
| `09_presentation/speaker_notes.md` | 발표자 대본 |
| `09_presentation/qna.md` | 예상 질문과 답변 |
| `09_presentation/one_page_handout.md` | 1페이지 배포자료 |

## 7. 기말논문 연결

추천 주제는 “RAG 기반 생성형 AI 시스템에서 간접 프롬프트 인젝션 대응을 위한 출처 검증·승인 게이트 평가 프레임워크”이다. W08의 기여 후보는 RAG 위협모형, source verification 지표, tool misuse rate, human approval gate, seed/config/output 기반 재현성 구조이다.

## 8. AI 활용 고지

Codex를 사용해 공통 지침 확인, 로컬 파일 점검, PDF 기반 서지 보정, synthetic 실험 코드 작성과 실행, 제출용 보고서 및 발표자료 작성을 수행했다. 정량값은 `04_experiment/outputs/run_log.md`, `metrics_summary.csv`, `results.json`과 일치하는 값만 사용했다. 상세 기록은 `05_ai_worklog/`에 있다.

## 9. 제출 전 점검표

| 점검 항목 | 상태 |
|---|---|
| 논문 요약 5편 | 완료 |
| 논문 비교표 | 완료 |
| AI 원리/보안 이슈 | 완료 |
| Research Track | 완료 |
| 실험 코드 | 완료 |
| 실험 결과 | 완료 |
| DOI/URL 검증표 | 부분 완료 |
| AI 활용 고지 | 완료 |
| 발표자료 | 완료 |
