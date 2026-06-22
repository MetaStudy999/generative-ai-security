# 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 논문 제목 | Graph-Based Approaches and Functionalities in Retrieval-Augmented Generation: A Comprehensive Survey |
| 저자 | Zulun Zhu, Tiancheng Huang, Kai Wang, Junda Ye, Xinghe Chen, Siqiang Luo |
| 학술지/학회 | ACM Computing Surveys |
| 연도 | 2026 |
| DOI/URL | https://doi.org/10.1145/3795880 |
| PDF 파일명 | 02_Zhu_et_al_2026_Graph_Based_RAG_Comprehensive_Survey.pdf |
| 검증 상태 | PDF 첫 페이지 DOI 확인 |

## 2. 한 문장 요약

> 이 논문은 graph가 RAG에서 수행하는 기능을 database construction, algorithm, pipeline, task 관점으로 분해하며, GraphRAG를 knowledge-graph traversal보다 넓은 기능적 설계 공간으로 정리한다.

## 3. 연구문제

기존 RAG survey가 graph를 주로 knowledge graph traversal로 좁게 다룬 반면, 실제 RAG pipeline에서는 graph가 검색 대상, prompt 구성, pipeline control, complex reasoning에 폭넓게 관여한다. 이 논문은 graph의 기능을 세밀하게 구분하는 연구문제를 다룬다.

## 4. 핵심 개념

| 개념 | 설명 | W08 연결 |
|---|---|---|
| Graph Functionality | graph가 RAG pipeline에서 맡는 역할 분류 |
| Structured Knowledge | entity와 relation을 포함한 외부 지식 |
| Multi-hop Reasoning | 여러 관계를 거쳐 답을 구성하는 추론 |
| Pipeline Control | 검색, prompt 구성, 생성 단계를 graph 정보로 조정하는 기능 |
| Graph-Structured Data | 문서, citation, knowledge graph, social graph 등 관계형 데이터 |

## 5. 방법론

ACM Computing Surveys 형식의 comprehensive survey다. graph 기반 RAG 방법을 데이터베이스 구축, 알고리즘, pipeline, task로 세분화하고, 기존 방법의 공통점과 차이를 정리한다.

## 6. 주요 결과

Graph 기반 RAG는 hallucination 완화뿐 아니라 구조적 지식과 복잡한 reasoning을 보강하는 데 쓰인다. W08의 관점에서는 graph 기능이 늘어날수록 출처, edge trust, retrieval path, prompt context의 감사 가능성이 더 중요해진다.

## 7. 보안 관점 분석

GraphRAG의 공격면은 문서 chunk 오염에서 끝나지 않는다. 공격자가 entity alias, relation, edge weight, graph path를 조작하면 검색 결과가 정상 문서처럼 보이면서도 잘못된 생성 근거를 제공할 수 있다. 따라서 Source Verification은 문서 단위뿐 아니라 graph element 단위로 확장되어야 한다.

## 8. 한계와 오픈문제

본 논문은 graph 기능 분류에 강하지만 prompt injection 방어 실험 자체가 주제는 아니다. 보안 연구로 발전시키려면 graph provenance logging, poisoned edge detection, multi-hop retrieval audit 같은 평가 항목을 추가해야 한다.

## 9. 기말 논문에 반영할 부분

기말 논문에서는 P02를 “보안형 RAG의 검증 대상이 문서 본문뿐 아니라 graph database와 pipeline control까지 확장된다”는 근거로 활용한다.
