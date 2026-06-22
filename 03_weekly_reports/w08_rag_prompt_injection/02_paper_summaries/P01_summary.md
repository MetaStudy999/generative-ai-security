# 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 논문 제목 | Graph Retrieval-Augmented Generation: A Survey |
| 저자 | Boci Peng, Yun Zhu, Yongchao Liu, Xiaohe Bo, Haizhou Shi, Chuntao Hong, Yan Zhang, Siliang Tang |
| 학술지/학회 | arXiv / 출판정보 확인 필요 |
| 연도 | 2024 |
| DOI/URL | https://arxiv.org/abs/2408.08921 |
| PDF 파일명 | 01_Peng_et_al_2025_Graph_Retrieval_Augmented_Generation.pdf |
| 강의계획서 표기 | Shiyu Chen et al., ACM Computing Surveys, 2025 |
| 로컬 PDF 표기 | Boci Peng et al., arXiv:2408.08921 |
| 검증 상태 | PDF 첫 페이지와 arXiv ID 확인, DOI는 PDF placeholder라 확정 보류. 강의계획서 표기와 동일 논문 여부 확인 필요 |

## 2. 한 문장 요약

> 이 논문은 일반 RAG가 관계 구조와 전역 정보를 충분히 활용하지 못하는 문제를 GraphRAG 워크플로우 분류로 다루며, graph-based indexing, graph-guided retrieval, graph-enhanced generation이라는 분석 틀을 제시한다.

## 3. 연구문제

RAG가 외부 지식을 검색해 LLM의 환각과 최신성 문제를 줄일 수 있지만, 문서 사이의 관계, citation network, knowledge graph, multi-hop reasoning처럼 구조적 연결이 중요한 상황에서는 단순 semantic similarity 검색만으로 부족하다. 이 논문은 GraphRAG가 어떤 단계와 기술 요소로 구성되는지 체계화한다.

## 4. 핵심 개념

| 개념 | 설명 | W08 연결 |
|---|---|---|
| GraphRAG | 텍스트 chunk만이 아니라 node, edge, path, subgraph를 검색·생성에 활용하는 RAG |
| Graph-Based Indexing | 검색 전에 문서와 entity 관계를 graph 형태로 구축하는 단계 |
| Graph-Guided Retrieval | query와 관련된 graph element를 찾아 관계 기반 context를 구성하는 단계 |
| Graph-Enhanced Generation | 검색된 관계 구조를 generation prompt에 반영하는 단계 |
| Lost in the Middle | 긴 context 안에서 중요한 정보가 묻히는 현상 |

## 5. 방법론

문헌조사 기반 survey다. GraphRAG pipeline을 단계별로 formalize하고, 각 단계의 핵심 기술, training 방법, downstream task, application domain, evaluation 방법, 산업 활용 사례를 분류한다.

## 6. 주요 결과

이 논문은 GraphRAG를 단순 RAG의 확장 기능이 아니라 “관계 구조를 검색과 생성에 주입하는 별도 pipeline”으로 설명한다. W08에서는 이 틀을 활용해 오염 문서가 graph node나 edge로 들어왔을 때 검색·생성 단계 모두에 영향을 줄 수 있음을 정리한다.

## 7. 보안 관점 분석

GraphRAG는 관계 추론 능력을 높이지만, 동시에 오염된 node, forged edge, 악성 subgraph가 검색 근거로 선택될 위험도 만든다. 따라서 prompt injection 방어는 텍스트 chunk 필터링만이 아니라 graph provenance, edge trust, community-level source verification까지 포함해야 한다.

## 8. 한계와 오픈문제

PDF의 DOI가 placeholder로 표시되어 확정 인용에는 arXiv URL만 사용해야 한다. 또한 survey 문헌이므로 GraphRAG 보안성 자체를 실험적으로 검증하지는 않는다. W08 실습에서는 이를 보완하기 위해 synthetic source verification 평가를 별도로 수행했다.

주의: W08의 P01은 arXiv:2408.08921 기준으로 확인했으나, PDF 내부 DOI가 placeholder이므로 DOI를 확정하지 않는다. 강의계획서의 Shiyu Chen et al. / ACM Computing Surveys 2025 표기와 현재 로컬 PDF의 Boci Peng et al. 표기가 동일 논문을 가리키는지 최종 확인이 필요하다.

## 9. 기말 논문에 반영할 부분

기말 논문 관련연구 장에는 GraphRAG의 세 단계 분류를 반영하고, 방법론 장에는 “검색 context에 들어온 문서/관계의 출처 검증”을 RAG 보안 평가 항목으로 넣는다.
