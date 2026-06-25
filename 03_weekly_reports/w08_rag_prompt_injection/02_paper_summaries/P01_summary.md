# P01 Summary

## Graph Retrieval-Augmented Generation: A Survey — Boci Peng et al., ACM TOIS, 2025/2026

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W08 RAG·프롬프팅 프레임워크 & 프롬프트 인젝션 |
| 논문명 | Graph Retrieval-Augmented Generation: A Survey |
| 저자 | Boci Peng, Yun Zhu, Yongchao Liu, Xiaohe Bo, Haizhou Shi, Chuntao Hong, Yan Zhang, Siliang Tang |
| 공식 출판 정보 | ACM Transactions on Information Systems, 44(2), pp. 1–52; online 2025-12-23, print issue 2026-02-28 |
| DOI | https://doi.org/10.1145/3777378 |
| 보조 URL | https://arxiv.org/abs/2408.08921 |
| 로컬 PDF | `01_papers/pdf/01_Peng_et_al_2025_Graph_Retrieval_Augmented_Generation.pdf` |
| 검증 상태 | W08 `paper_list.md` 기준 공식 DOI 확인. 강의계획서의 `Shiyu Chen et al. / ACM Computing Surveys` 표기와 현재 로컬 PDF/DOI 기준 정보의 차이 메모 유지 |
| PDF 확인 메모 | repo의 PDF 폴더에 해당 PDF blob이 존재함을 확인했다. 요약은 로컬 PDF 경로와 공식 DOI/arXiv 메타데이터 기준으로 보완했다. |
| 핵심 근거 사용 가능 여부 | 가능. W08에서 Graph RAG 구조, graph 기반 검색, evidence path, provenance, RAG 보안 평가의 핵심 배경 문헌으로 사용 |

---

## 1. 한 문장 요약

이 논문은 GraphRAG를 **Graph-Based Indexing, Graph-Guided Retrieval, Graph-Enhanced Generation**의 3단계 workflow로 정식화하고, text-attributed graph, knowledge graph, graph neural network, graph retrieval, subgraph/path/community retrieval, graph-enhanced generation, application, evaluation을 체계화한 survey이며, W08에서 RAG 보안을 단순 문서 검색이 아니라 **node-edge-relation-evidence path-provenance** 보안 문제로 확장하는 핵심 문헌이다.

---

## 2. 핵심 연구문제

> 기존 RAG가 문서 조각 중심 검색에 머무를 때 생기는 관계 정보 누락, 긴 context, 전역 정보 부족 문제를 graph structure로 어떻게 보완하며, 이 과정에서 graph node, edge, relation, evidence path의 무결성과 provenance를 어떻게 평가할 것인가?

| 번호 | 연구질문 |
|---|---|
| RQ1 | GraphRAG는 기존 text-based RAG의 한계인 관계 정보 누락, 중복 context, global information 부족 문제를 어떻게 해결하는가? |
| RQ2 | Graph-Based Indexing, Graph-Guided Retrieval, Graph-Enhanced Generation은 각각 어떤 역할을 하는가? |
| RQ3 | Text-Attributed Graph, Knowledge Graph, GNN, LLM은 GraphRAG pipeline에서 어떻게 결합되는가? |
| RQ4 | Node, edge, path, subgraph, community 단위 retrieval은 evidence faithfulness와 citation support에 어떤 영향을 주는가? |
| RQ5 | Graph poisoning, malicious node insertion, edge manipulation, indirect prompt injection은 GraphRAG 출력을 어떻게 왜곡할 수 있는가? |

---

## 3. 논문의 핵심 기여

| 기여 | 설명 | W08 연결 |
|---|---|---|
| GraphRAG workflow 정식화 | GraphRAG를 G-Indexing, G-Retrieval, G-Generation의 3단계로 구조화 | W08 RAG 구조 분석의 기본 틀 |
| 관련 기술 비교 | RAG, LLMs on Graphs, KBQA와 GraphRAG의 차이를 비교 | 일반 RAG와 Graph RAG 차별성 설명 |
| Graph data 표현 정리 | Text-Attributed Graph, Knowledge Graph, GNN 기반 표현을 정리 | node/edge/relation을 보안 자산으로 정의 |
| Retrieval source와 방법 정리 | node, triple, path, subgraph, community 등 graph element retrieval 정리 | evidence path와 graph provenance 평가 |
| Application/evaluation 정리 | downstream task, benchmark, application domain, industrial use case 논의 | 기말논문 평가 설계와 실제 적용성 연결 |

---

## 4. 목차별 핵심 개괄

| 논문 목차 | 핵심 내용 | 비전공자용 이해 |
|---|---|---|
| 1. Introduction | LLM은 hallucination, domain knowledge 부족, 최신 정보 부족 문제가 있고, RAG는 외부 지식을 검색해 이를 보완한다. 그러나 일반 RAG는 관계 정보를 충분히 반영하지 못하므로 GraphRAG가 필요하다. | 일반 RAG가 “관련 문서 몇 개를 찾아 붙이는 방식”이라면, GraphRAG는 “문서 사이의 관계 지도까지 보고 답하는 방식”이다. |
| 2. Comparison with Related Techniques | RAG, LLMs on Graphs, KBQA와 GraphRAG를 비교한다. GraphRAG는 단순 텍스트 검색이 아니라 graph database에서 관계 지식을 검색해 생성에 활용한다. | GraphRAG는 검색엔진 + 지식지도 + LLM을 결합한 구조다. |
| 3. Preliminaries | Text-Attributed Graph, GNN, Language Model 기본 개념을 설명한다. | 문서를 node와 edge가 있는 지도처럼 바꾸고, 그 지도 위에서 관련 근거를 찾는다. |
| 4. General Process of GraphRAG | GraphRAG의 공통 pipeline을 indexing, retrieval, generation으로 설명한다. | 자료를 그래프로 만들고, 질문에 맞는 부분 그래프를 찾고, 그 근거로 답변한다. |
| 5. Graph-Based Indexing | 원문 문서에서 entity, relation, attribute를 추출하고 graph structure로 저장한다. | 텍스트를 그냥 쌓아두지 않고, 사람·기관·개념·문서의 관계도로 바꾼다. |
| 6. Graph-Guided Retrieval | 질문에 맞는 node, edge, path, subgraph, community를 검색한다. | “한 문서”가 아니라 “관련 개념들이 연결된 경로”를 찾아온다. |
| 7. Graph-Enhanced Generation | 검색된 graph 정보를 LLM이 이해할 수 있는 prompt/context 형태로 변환해 답변 생성에 사용한다. | 그래프에서 찾은 근거를 사람이 읽을 수 있는 문장으로 풀어 LLM에 넣는다. |
| 8. Training | Retriever와 generator를 GraphRAG에 맞게 학습·튜닝하는 방법을 다룬다. | 질문에 맞는 관계 경로를 더 잘 찾고, 답변이 근거를 더 잘 따르도록 훈련한다. |
| 9. Applications and Evaluation | QA, summarization, recommendation, domain knowledge service, 산업 적용, 평가 지표를 정리한다. | GraphRAG는 의료·금융·교육·기업 지식관리처럼 관계가 중요한 분야에 유용하다. |
| 10. Future Prospects | 효율성, 동적 graph update, 평가 benchmark, 신뢰성, 산업 적용, 보안 이슈가 남은 과제다. | 그래프가 계속 바뀔 때 최신성과 신뢰성을 어떻게 지킬지가 중요하다. |
| 11. Conclusion | GraphRAG는 관계 지식을 활용해 RAG의 검색·추론·생성을 개선하는 유망한 방향이다. | 답변을 더 정확하게 만들려면 문서 내용뿐 아니라 문서 간 관계까지 봐야 한다. |

---

## 5. 핵심 이론 및 수식

> 아래 수식은 GraphRAG 구조와 W08 보안 평가를 설명하기 위한 표준화된 표현이다. 수식은 GitHub, MS Word, PDF 변환 호환성을 위해 Markdown 표 밖의 LaTeX block math로 작성한다.

### 5.1 Text-Attributed Graph

GraphRAG에서 문서와 지식은 node와 edge가 textual attribute를 갖는 graph로 표현될 수 있다.

$$
\mathcal{G}=(\mathcal{V},\mathcal{E},\mathcal{A},\{\mathbf{x}_{v}\}_{v\in\mathcal{V}},\{\mathbf{e}_{i,j}\}_{(i,j)\in\mathcal{E}})
$$

| 기호 | 의미 |
|---|---|
| $\mathcal{V}$ | node 집합. 문서, 개체, 개념, 사건 등 |
| $\mathcal{E}$ | edge 집합. node 사이의 관계 |
| $\mathcal{A}$ | adjacency matrix. 연결 구조 |
| $\mathbf{x}_v$ | node의 텍스트 속성 |
| $\mathbf{e}_{i,j}$ | edge의 텍스트 속성 또는 관계 설명 |

### 비전공자용 설명

문서를 그냥 폴더에 넣어두는 것이 아니라, “A는 B와 관련 있고, B는 C의 원인이고, C는 D의 근거다”처럼 연결 지도로 만드는 것이다. 이 지도가 있으면 LLM이 단순히 비슷한 문장만 찾는 것이 아니라 **관계가 이어지는 근거 경로**를 따라갈 수 있다.

### 보안적 의미

GraphRAG의 node와 edge가 오염되면 잘못된 관계가 근거처럼 사용될 수 있다. 따라서 node 출처, edge 생성 근거, graph snapshot, update log가 보안 자산이 된다.

---

### 5.2 Graph Neural Network Message Passing

GNN은 이웃 node와 edge 정보를 모아 node representation을 갱신한다.

$$
\mathbf{h}^{(l)}_i=\textbf{UPD}\left(\mathbf{h}^{(l-1)}_i,\textbf{AGG}_{j\in\mathcal{N}(i)}\textbf{MSG}(\mathbf{h}^{(l-1)}_i,\mathbf{h}^{(l-1)}_j,\mathbf{e}^{(l-1)}_{i,j})\right)
$$

| 기호 | 의미 |
|---|---|
| $\mathbf{h}^{(l)}_i$ | $l$번째 layer에서 node $i$의 representation |
| $\mathcal{N}(i)$ | node $i$의 이웃 node 집합 |
| MSG | 이웃에서 전달되는 message 계산 함수 |
| AGG | 여러 message를 합치는 함수 |
| UPD | node 표현을 갱신하는 함수 |

### 비전공자용 설명

한 사람의 평판을 그 사람 혼자만 보고 판단하지 않고, 주변 사람과 관계를 함께 보고 판단하는 것과 같다. GraphRAG에서는 어떤 node가 중요한지 판단할 때 주변 node와 relation을 같이 본다.

### 보안적 의미

악성 node가 graph에 들어오면 주변 node representation에도 영향을 줄 수 있다. 즉 graph poisoning은 단일 문서 오염보다 넓은 범위의 검색 결과를 왜곡할 수 있다.

---

### 5.3 Graph Retrieval

질문 $q$가 들어오면 관련 node, path, subgraph를 검색한다.

$$
D_k(q)=TopK_{v_i\in\mathcal{V}}\; sim(E(q),E(v_i))
$$

| 기호 | 의미 |
|---|---|
| $q$ | 사용자 질문 |
| $E(\cdot)$ | embedding 함수 |
| $sim$ | 질문과 node 사이의 유사도 |
| $D_k(q)$ | 상위 $k$개 검색 결과 |

### 비전공자용 설명

질문과 가장 비슷한 문서 조각을 찾는 것이 아니라, 질문과 관련 있는 **개념 node**를 찾고 그 주변 관계까지 탐색한다.

### 보안적 의미

악성 문서가 높은 유사도를 갖도록 작성되면 retrieval ranking을 오염시킬 수 있다. 따라서 source precision, node trust, citation support를 같이 봐야 한다.

---

### 5.4 Evidence Path Score

GraphRAG의 강점은 단일 문서가 아니라 evidence path를 근거로 삼을 수 있다는 점이다.

$$
Score(q,path)=\alpha\cdot sim(E(q),E(path))+\beta\cdot Trust(path)+\gamma\cdot Coverage(path)
$$

| 기호 | 의미 |
|---|---|
| $path$ | node와 edge로 연결된 근거 경로 |
| $Trust(path)$ | 출처·검증·권위 기반 신뢰도 |
| $Coverage(path)$ | 질문에 필요한 근거를 얼마나 포괄하는지 |
| $\alpha,\beta,\gamma$ | 유사도·신뢰도·포괄성 가중치 |

### 비전공자용 설명

답변의 근거가 “문서 하나”가 아니라 “A 문서 → B 개념 → C 근거 → D 결론”처럼 이어진 길이라면, 그 길이 얼마나 질문과 관련 있고 믿을 만한지 점수를 매길 수 있다.

### 보안적 의미

공격자는 근거 경로 중간에 악성 node나 조작된 edge를 넣어 답변을 왜곡할 수 있다. 따라서 evidence path 전체의 provenance를 감사해야 한다.

---

### 5.5 Graph-Enhanced Generation

검색된 graph context를 LLM prompt에 넣어 답변을 생성한다.

$$
y \sim p_\theta(y\mid q, C_{graph})
$$

| 기호 | 의미 |
|---|---|
| $y$ | 생성된 답변 |
| $q$ | 사용자 질문 |
| $C_{graph}$ | 검색된 graph context. node, edge, path, subgraph 요약 포함 |
| $p_\theta$ | LLM의 조건부 생성 확률 |

### 비전공자용 설명

LLM에게 질문만 주는 것이 아니라, 관련 지식지도에서 찾아온 근거 묶음을 함께 주고 답하게 하는 것이다.

### 보안적 의미

Graph context 안에 prompt injection 문구, 악성 instruction, 조작된 citation이 포함되면 LLM이 이를 근거처럼 받아들일 수 있다. W08의 prompt injection 주제와 직접 연결된다.

---

## 6. AI 원리 70% 관점 분석

| 원리 항목 | 설명 | W08/P01에서의 의미 |
|---|---|---|
| RAG | 외부 지식을 검색해 LLM 답변에 반영 | hallucination과 최신성 문제 보완 |
| GraphRAG | 외부 지식을 graph structure로 표현하고 검색 | 관계 기반 추론과 evidence path 강화 |
| Text-Attributed Graph | node와 edge가 텍스트 속성을 갖는 graph | 문서·개념·관계의 통합 표현 |
| Knowledge Graph | entity와 relation을 구조화한 지식 표현 | 근거 출처와 관계 의미를 명시 |
| GNN | graph 구조에서 node/edge representation 학습 | graph retrieval과 reasoning 지원 |
| Graph-Guided Retrieval | node, edge, path, subgraph, community 검색 | 단일 문서보다 관계 근거 확보 |
| Graph-Enhanced Generation | graph context를 LLM이 사용할 수 있게 변환 | 답변의 근거성과 설명가능성 향상 |
| Evaluation | retrieval, faithfulness, citation, generation 품질 평가 | RAG 보안 평가 지표 설계 |

---

## 7. 보안 이슈 30% 관점 분석

| 보안 항목 | GraphRAG 관점 해석 | 대표 평가 지표 |
|---|---|---|
| 기밀성 | graph node/edge에 민감 문서, 내부 관계, 사용자 정보가 포함될 수 있음 | sensitive node exposure rate, access-control violation |
| 무결성 | malicious node, edge poisoning, relation manipulation으로 검색 근거가 왜곡될 수 있음 | graph integrity score, poisoned retrieval rate |
| 가용성 | graph가 커질수록 retrieval latency와 update cost가 증가 | latency, graph update cost, retrieval timeout rate |
| 프라이버시 | entity relation이 개인·조직의 숨은 관계를 드러낼 수 있음 | relation leakage risk, k-anonymity-style graph risk |
| 책임성 | 답변 근거가 어떤 node/edge/path에서 왔는지 추적해야 함 | citation support, provenance coverage, audit completeness |
| Prompt Injection | retrieved graph context 안의 악성 instruction이 LLM을 오염시킬 수 있음 | injection ASR, policy compliance, context isolation score |

---

## 8. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | source document, graph node, edge, relation, attribute, embedding, evidence path, citation, graph snapshot, prompt-output log |
| 공격자 목표 | malicious node 삽입, edge 조작, graph poisoning, retrieval ranking 조작, indirect prompt injection, citation spoofing |
| 공격자 능력 | 문서 업로드, metadata 조작, node/edge 생성 규칙 악용, graph update 오염, prompt-like text 삽입 |
| 공격 경로 | source document → graph construction → graph indexing → graph-guided retrieval → graph context prompt → LLM generation |
| 방어자 능력 | source validation, node/edge provenance, graph snapshot, retrieval audit, prompt isolation, citation verification, human review |
| 제외 범위 | 실제 서비스 공격, 무단 내부 문서 사용, 실제 개인정보 graph 구축, 공격 payload 제공 |

---

## 9. 평가방법 및 지표

| 평가축 | 지표 | 의미 | W08/P01 활용 |
|---|---|---|---|
| Retrieval quality | Recall@k, Precision@k, MRR, nDCG | 관련 node/path/subgraph를 잘 찾는지 | Graph retrieval 평가 |
| Evidence faithfulness | evidence support rate, citation support | 답변이 검색 근거와 일치하는지 | hallucination 완화 평가 |
| Graph integrity | edge accuracy, poisoned node rate | graph 구조가 신뢰 가능한지 | graph poisoning 평가 |
| Provenance | node/edge/source traceability | 근거 출처 추적 가능성 | 기말논문 감사표 |
| Robustness | retrieval under noisy graph, graph update stability | graph 변화에도 결과가 안정적인지 | 운영 평가 |
| Prompt injection safety | injection ASR, policy compliance | retrieved graph context에 악성 instruction이 있을 때 안전한지 | W08 P04/P05 연결 |
| Cost | indexing cost, retrieval latency, graph update cost | 실제 운영 가능성 | W14 MLOps 연결 |
| Human review | evidence path review agreement | 사람이 근거 경로를 검토할 수 있는지 | W15 재현성·책임성 연결 |

---

## 10. 재현성 체크리스트

| 항목 | 기록해야 할 내용 |
|---|---|
| Graph source | 원문 문서, KG, database, crawl source, license |
| Graph construction | entity extraction, relation extraction, chunking, summarization, node/edge schema |
| Graph snapshot | graph version, node/edge count, update timestamp, hash |
| Embedding/retriever | embedding model, graph retriever, reranker, Top-k, threshold |
| Prompt/context | graph context serialization 방식, prompt template, context window |
| Generator | LLM model/version, decoding setting, safety policy |
| Evaluation | retrieval metrics, faithfulness, citation support, injection ASR, latency |
| Security log | source-node-edge-path-output trace, human review, failure cases |
| 한계 | toy graph 또는 공개 데이터 결과를 실제 기업 RAG 보안 보증으로 과장하지 않음 |

---

## 11. 논문의 고유 기여

1. GraphRAG를 기존 RAG의 하위 기능이 아니라 독립 workflow로 체계화한다.
2. GraphRAG를 Graph-Based Indexing, Graph-Guided Retrieval, Graph-Enhanced Generation으로 명확히 분해한다.
3. Text-Attributed Graph와 GNN 기반 representation을 GraphRAG의 기초 개념으로 정리한다.
4. Node, edge, path, subgraph, community retrieval이 LLM generation에 주는 이점을 정리한다.
5. W08 보안 관점에서 graph node/edge/provenance가 RAG의 새로운 보호 자산이 됨을 설명할 수 있는 근거를 제공한다.

---

## 12. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 직접 보안 논문은 아님 | 논문은 GraphRAG survey이며 prompt injection 방어 전문 문헌은 아니다. | W08 P04/P05와 결합해 보안 평가로 확장 |
| Graph construction 오류 | entity/relation 추출 오류가 downstream generation까지 전파될 수 있다. | node/edge validation과 provenance check 포함 |
| Dynamic graph 문제 | graph가 계속 업데이트되면 retrieval 결과와 답변 재현성이 흔들릴 수 있다. | graph snapshot과 versioning 필수화 |
| 평가 지표 미성숙 | GraphRAG 특화 benchmark와 security metric이 아직 충분히 표준화되지 않았다. | retrieval-faithfulness-security 통합 지표 설계 |
| 민감 관계 노출 | graph는 숨은 관계를 드러낼 수 있어 privacy risk가 커질 수 있다. | access control, relation masking, audit log 반영 |
| Prompt injection 연결 | retrieved graph context가 LLM prompt로 들어가면 간접 prompt injection 경로가 된다. | context isolation, instruction stripping, policy check 추가 |

---

## 13. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | RAG 보안은 단순 문서 검색 문제가 아니라 graph evidence와 provenance 보안 문제라는 문제의식 |
| 2장 관련연구 | GraphRAG workflow, TAG, KG, GNN, graph retrieval survey 정리 |
| 3장 위협모형 | source document, node, edge, relation, evidence path, graph snapshot, prompt context 보호 자산 정의 |
| 4장 연구방법 | Recall@k, citation support, graph integrity, injection ASR, provenance coverage 지표 설계 |
| 5장 분석 | GraphRAG pipeline과 attack surface mapping 표/그림 제시 |
| 6장 보안적 함의 | graph poisoning, indirect prompt injection, sensitive relation leakage, human review 필요성 해석 |

---

## 14. 기말논문 연결 3문장

1. W08에서 기말논문에 반영할 개념: GraphRAG는 RAG를 단순 vector retrieval에서 graph node, edge, relation, path 기반 retrieval로 확장하므로, 답변의 정확성뿐 아니라 evidence path와 provenance의 무결성을 평가해야 한다.
2. W08에서 기말논문에 반영할 표·그림·실험: Graph-Based Indexing → Graph-Guided Retrieval → Graph-Enhanced Generation pipeline, graph poisoning 위협모형, citation support와 injection ASR 평가표를 반영한다.
3. W08이 LLM 보안 감사 프레임워크와 연결되는 지점: retrieved graph context가 LLM prompt에 주입되는 순간, 악성 node/edge가 indirect prompt injection 또는 citation spoofing으로 작동할 수 있으므로 W14/W15의 evidence chain에 graph snapshot과 node/edge provenance를 포함해야 한다.

---

## 15. 최종 판단

P01은 W08에서 RAG 구조와 provenance 평가를 확장하는 핵심 관련 문헌이다. 강의계획서 표기와 로컬 PDF/공식 DOI 기준 정보가 다르므로 `관련 논문 / 확인` 상태를 유지하되, Graph RAG 보안 평가에는 직접 활용 가능하다. 특히 기말논문에서 RAG 보안 점검표를 만들 경우 P01은 **문서 출처, graph node/edge 무결성, evidence path 감사, citation support 평가**의 근거 문헌으로 사용하는 것이 적절하다.

---

## 16. 변환 호환성 메모

```bash
pandoc P01_summary.md -o P01_summary.docx
pandoc P01_summary.md -o P01_summary.pdf --pdf-engine=xelatex
```
