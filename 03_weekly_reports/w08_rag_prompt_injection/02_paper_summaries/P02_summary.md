# P02 Summary

## Graph-Based Approaches and Functionalities in Retrieval-Augmented Generation: A Comprehensive Survey — Zulun Zhu et al., ACM Computing Surveys, 2026

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W08 RAG·프롬프팅 프레임워크 & 프롬프트 인젝션 |
| 논문명 | Graph-Based Approaches and Functionalities in Retrieval-Augmented Generation: A Comprehensive Survey |
| 저자 | Zulun Zhu, Tiancheng Huang, Kai Wang, Junda Ye, Xinghe Chen, Siqiang Luo |
| 공식 출판 정보 | ACM Computing Surveys, Vol. 58, No. 10, Article 261, 38 pages, 2026 |
| DOI | https://doi.org/10.1145/3795880 |
| 로컬 PDF | `01_papers/pdf/02_Zhu_et_al_2026_Graph_Based_RAG_Comprehensive_Survey.pdf` |
| 검증 상태 | W08 `paper_list.md` 기준 DOI/PDF 확인. 강의계획서의 `Jianxiang Li et al.` 표기와 공식 DOI 기준 `Zulun Zhu et al.` 표기 차이 메모 유지 |
| PDF 확인 메모 | repo의 PDF 폴더에 해당 PDF blob이 존재함을 확인했다. 요약은 로컬 PDF 경로와 W08 `paper_list.md`의 공식 DOI 메타데이터 기준으로 보완했다. |
| 핵심 근거 사용 가능 여부 | 가능. W08에서 graph-based RAG 기능, graph retrieval, graph integrity, graph update, explanation path, RAG 보안 평가의 핵심 관련 문헌으로 사용 |

---

## 1. 한 문장 요약

이 논문은 RAG 시스템에서 graph-based approach가 수행하는 기능을 **graph construction, graph indexing, graph retrieval, graph reasoning, graph-enhanced generation, explainability, update/maintenance, evaluation** 관점에서 정리하며, W08에서 RAG 보안을 단순 prompt injection 방어가 아니라 **graph node·edge·schema·evidence path·citation·update log의 무결성과 provenance 문제**로 확장하는 핵심 survey 문헌이다.

---

## 2. 핵심 연구문제

> Graph-based RAG는 vector-only RAG가 놓치기 쉬운 구조적 관계와 추론 경로를 어떻게 보완하며, graph construction·retrieval·reasoning·update 과정에서 발생하는 무결성·프라이버시·프롬프트 인젝션 위험을 어떻게 평가할 것인가?

| 번호 | 연구질문 |
|---|---|
| RQ1 | Graph-based RAG는 vector-only RAG의 어떤 한계, 특히 관계 정보 누락·근거 경로 부재·설명가능성 부족을 보완하는가? |
| RQ2 | Graph construction, graph indexing, graph update 과정에서 node/edge/schema 오류는 downstream generation에 어떤 영향을 주는가? |
| RQ3 | Graph retrieval은 node, edge, path, subgraph, community 단위 검색을 통해 answer faithfulness와 citation support를 어떻게 개선하는가? |
| RQ4 | Graph reasoning과 explanation path는 사용자가 답변의 근거를 검토하는 데 어떤 감사 가치를 제공하는가? |
| RQ5 | Malicious node insertion, edge poisoning, metadata manipulation, retrieved-context prompt injection은 Graph-RAG의 출력과 안전성을 어떻게 왜곡하는가? |

---

## 3. 논문의 핵심 기여

| 기여 | 설명 | W08 연결 |
|---|---|---|
| Graph-based RAG 기능 분류 | RAG에서 graph가 수행하는 retrieval, reasoning, explanation, grounding 기능을 정리 | W08 RAG 구조 보완 |
| Graph construction/update 문제 제시 | 문서에서 entity/relation/schema를 추출하고 갱신하는 과정의 복잡성 제시 | graph provenance와 update approval log 필요 |
| Graph retrieval 방식 정리 | node, edge, path, subgraph, community 기반 retrieval을 구분 | evidence path와 citation support 평가 |
| Graph reasoning 기능 강조 | 단순 유사도 검색보다 관계 추론과 multi-hop reasoning을 지원 | 답변 설명가능성과 근거성 강화 |
| 평가·한계·미래방향 정리 | graph integrity, efficiency, scalability, dynamic update, benchmark 문제 제시 | W14 MLOps, W15 reproducibility 연결 |

---

## 4. 목차별 핵심 개괄

| 목차 | 핵심 내용 | 비전공자용 이해 |
|---|---|---|
| 1. Introduction | LLM의 hallucination과 최신 지식 부족을 RAG가 보완하지만, 일반 RAG는 문서 간 관계와 multi-hop reasoning을 충분히 반영하지 못한다. Graph-based RAG는 구조화된 지식과 관계를 활용해 이를 보완한다. | 일반 RAG가 “문서 검색”이라면 graph-based RAG는 “문서와 개념의 관계 지도 검색”이다. |
| 2. Background | RAG, knowledge graph, graph database, graph neural network, LLM 기반 reasoning 개념을 설명한다. | 그래프는 점(node)과 선(edge)으로 지식을 표현하는 지도다. |
| 3. Graph Construction | 문서에서 entity, relation, event, attribute를 추출해 graph schema와 node/edge로 만든다. | 긴 문서를 사람·기관·개념·사건의 관계도로 바꾸는 단계다. |
| 4. Graph-Based Retrieval | 질문과 관련된 node, edge, path, subgraph, community를 찾는다. | 질문에 대한 답을 찾을 때 문장 하나가 아니라 관련 개념들이 이어진 길을 찾는다. |
| 5. Graph Reasoning and Generation | 검색된 graph context를 이용해 LLM이 답변하고, 근거 경로와 explanation path를 제공한다. | “왜 그런 답을 했는지”를 관계 경로로 설명할 수 있다. |
| 6. Functionalities | Graph-based RAG의 주요 기능을 knowledge grounding, explainability, reasoning, personalization, update, domain adaptation으로 정리한다. | 그래프를 쓰면 답변의 근거, 관계, 맥락, 최신 업데이트를 더 잘 관리할 수 있다. |
| 7. Evaluation | Retrieval precision, answer faithfulness, graph integrity, citation support, efficiency, scalability를 평가해야 한다. | 답이 맞는지만 보지 말고, 근거가 맞는지, 관계가 맞는지, 빠르게 검색되는지도 봐야 한다. |
| 8. Applications | QA, recommendation, scientific discovery, enterprise knowledge management, domain-specific assistant 등 적용 사례를 정리한다. | 기업 문서, 논문, 의료·금융 지식처럼 관계가 중요한 분야에 적합하다. |
| 9. Challenges and Future Directions | Dynamic graph, noisy graph, graph poisoning, scalability, benchmark 부족, privacy, security 문제가 남아 있다. | 지식지도가 계속 바뀌거나 누군가 지도를 조작하면 답변도 틀릴 수 있다. |
| 10. Conclusion | Graph-based RAG는 RAG의 검색·추론·설명가능성을 강화하지만, graph 품질·무결성·평가체계가 중요하다. | 관계 지도를 잘 만들고 지켜야 더 믿을 수 있는 RAG가 된다. |

---

## 5. 핵심 이론 및 수식

> 아래 수식은 graph-based RAG의 구조와 W08 보안 평가를 설명하기 위한 표준화된 표현이다. 수식은 GitHub, MS Word, PDF 변환 호환성을 위해 Markdown 표 밖의 LaTeX block math로 작성한다.

### 5.1 Graph Representation

Graph-based RAG는 문서와 지식을 graph $G$로 표현한다.

$$
G=(V,E,R,A)
$$

| 기호 | 의미 |
|---|---|
| $V$ | node 집합. 문서, chunk, entity, concept, event 등 |
| $E$ | edge 집합. node 사이의 연결 |
| $R$ | relation type. 원인, 포함, 참조, 동일, 소속 등 관계 유형 |
| $A$ | node/edge attribute. text, metadata, source, timestamp 등 |

### 비전공자용 설명

문서를 그냥 줄글로 저장하지 않고, “사람 A가 회사 B에 소속되어 있고, 회사 B가 기술 C를 개발했다”처럼 관계표로 바꾸는 것이다. 이 관계표가 있으면 LLM은 단순히 비슷한 문장을 찾는 것이 아니라 **관계가 이어지는 근거**를 찾을 수 있다.

### 보안적 의미

Graph의 node, edge, relation type, metadata가 오염되면 잘못된 관계가 사실처럼 검색된다. 따라서 graph schema와 source metadata는 보호 자산이다.

---

### 5.2 Graph-Based Retrieval

질문 $q$에 대해 graph에서 관련 node, edge, path, subgraph를 검색한다.

$$
R(q)=\operatorname{Retrieve}(q,G=(V,E))
$$

좀 더 구체적으로는 embedding similarity와 graph relation score를 함께 사용할 수 있다.

$$
Score(q,v_i)=\alpha\cdot sim(E(q),E(v_i))+\beta\cdot Rel(q,v_i)+\gamma\cdot Trust(v_i)
$$

| 기호 | 의미 |
|---|---|
| $q$ | 사용자 질문 |
| $v_i$ | 후보 node |
| $E(\cdot)$ | embedding 함수 |
| $Rel(q,v_i)$ | 질문과 node의 관계 적합성 |
| $Trust(v_i)$ | node 출처와 검증 신뢰도 |
| $\alpha,\beta,\gamma$ | 유사도·관계·신뢰도 가중치 |

### 비전공자용 설명

검색 결과를 고를 때 “질문과 단어가 비슷한가?”만 보는 것이 아니라 “이 정보가 어떤 관계를 통해 연결되는가?”, “출처가 믿을 만한가?”도 함께 보는 방식이다.

### 보안적 의미

공격자는 질문과 유사한 악성 node를 삽입하거나 metadata를 조작해 검색 순위를 높일 수 있다. 따라서 retrieval precision과 node trust를 함께 평가해야 한다.

---

### 5.3 Graph Integrity Score

Graph node와 edge가 검증되었는지 비율로 무결성을 평가할 수 있다.

$$
IntegrityScore=\frac{|V_{verified}|+|E_{verified}|}{|V|+|E|}
$$

| 기호 | 의미 |
|---|---|
| $V_{verified}$ | 출처와 내용이 검증된 node 집합 |
| $E_{verified}$ | 근거가 확인된 edge 집합 |
| $|V|+|E|$ | 전체 node와 edge 수 |

### 비전공자용 설명

지식지도 안에 있는 점과 선 중에서 “출처가 확인된 것”이 얼마나 되는지 보는 점수다.

### 보안적 의미

Graph integrity가 낮으면 RAG 답변이 틀린 근거를 바탕으로 생성될 수 있다. W08에서는 graph integrity를 prompt injection 방어 이전의 기본 전제조건으로 본다.

---

### 5.4 Evidence Coverage

질문에 답하기 위해 필요한 근거 중 검색된 graph context가 얼마나 포함하는지 평가한다.

$$
EvidenceCoverage=\frac{|Evidence_{retrieved}\cap Evidence_{required}|}{|Evidence_{required}|}
$$

| 기호 | 의미 |
|---|---|
| $Evidence_{retrieved}$ | graph retrieval이 가져온 근거 |
| $Evidence_{required}$ | 올바른 답변에 필요한 근거 |

### 비전공자용 설명

정답을 설명하려면 근거 5개가 필요한데 검색 결과가 그중 3개만 가져왔다면 coverage는 낮다. 답이 그럴듯해도 근거가 부족할 수 있다.

### 보안적 의미

근거가 빠진 답변은 hallucination으로 이어질 수 있고, 공격자가 일부 근거만 선택적으로 노출하면 편향된 답변이 생성될 수 있다.

---

### 5.5 Explanation Path Score

Graph-based RAG는 답변을 뒷받침하는 reasoning path를 제공할 수 있다.

$$
ExplainScore(q,path)=\alpha\cdot Relevance(q,path)+\beta\cdot Faithfulness(path,y)+\gamma\cdot Trust(path)
$$

| 기호 | 의미 |
|---|---|
| $path$ | node-edge-node로 이어지는 설명 경로 |
| $y$ | 생성된 답변 |
| $Relevance$ | 질문과 경로의 관련성 |
| $Faithfulness$ | 답변이 해당 경로를 실제로 따르는 정도 |
| $Trust$ | 경로 출처와 검증 신뢰도 |

### 비전공자용 설명

LLM 답변 뒤에 “이 결론은 A 자료 → B 관계 → C 근거에서 나왔다”는 설명 경로를 붙일 수 있다. 이 경로가 맞는지 점수화하는 것이다.

### 보안적 의미

공격자가 reasoning path 중간의 edge를 조작하면 답변이 틀린 방향으로 유도될 수 있다. 그래서 explanation path도 감사 대상이다.

---

### 5.6 Graph-Enhanced Generation

검색된 graph context를 LLM에 넣어 답변을 생성한다.

$$
y\sim p_\theta(y\mid q,C_G)
$$

| 기호 | 의미 |
|---|---|
| $y$ | 생성된 답변 |
| $q$ | 사용자 질문 |
| $C_G$ | graph retrieval로 얻은 context |
| $p_\theta$ | LLM의 조건부 생성 확률 |

### 비전공자용 설명

LLM에게 질문만 던지는 것이 아니라, 질문과 관련된 관계 지도를 잘라서 함께 보여준 뒤 답하게 하는 구조다.

### 보안적 의미

Graph context에 악성 instruction, 조작된 citation, 숨은 prompt injection 문구가 들어 있으면 LLM 답변이 오염될 수 있다. 따라서 graph context serialization과 prompt isolation이 필요하다.

---

## 6. AI 원리 70% 관점 분석

| 원리 항목 | 설명 | W08/P02에서의 의미 |
|---|---|---|
| RAG | 외부 지식을 검색해 LLM 답변에 추가 | hallucination 완화와 최신 지식 반영 |
| Graph-based RAG | 지식을 graph로 구조화해 검색·추론에 사용 | 관계 기반 retrieval과 reasoning 강화 |
| Knowledge Graph | entity와 relation을 명시적으로 표현 | citation과 evidence path 추적에 유리 |
| Graph Database | node/edge query와 path search 지원 | 대규모 지식 검색 운영 기반 |
| Graph Retrieval | node, edge, path, subgraph 단위 검색 | 단일 chunk보다 풍부한 근거 제공 |
| Graph Reasoning | multi-hop 관계를 따라 답변 근거 구성 | 설명가능성·근거성 강화 |
| Graph Update | 지식 graph를 지속적으로 갱신 | 최신성·재현성·무결성 문제 발생 |
| Graph Evaluation | retrieval, faithfulness, integrity, latency 측정 | RAG 보안 평가 지표 설계 |

---

## 7. 보안 이슈 30% 관점 분석

| 보안 항목 | Graph-based RAG 관점 해석 | 대표 평가 지표 |
|---|---|---|
| 기밀성 | graph가 내부 문서, 조직 관계, 사용자 관계, 민감 entity를 노출할 수 있음 | sensitive node exposure rate, relation leakage risk |
| 무결성 | node/edge poisoning, relation manipulation으로 검색 근거가 오염될 수 있음 | IntegrityScore, poisoned retrieval rate |
| 가용성 | graph 규모와 update 빈도가 커지면 retrieval latency와 timeout이 증가 | latency, timeout rate, update cost |
| 프라이버시 | relation graph가 개인·조직의 숨은 관계를 드러낼 수 있음 | relation masking rate, privacy leakage audit |
| 책임성 | 답변 근거가 어떤 source-node-edge-path에서 왔는지 추적해야 함 | provenance coverage, audit completeness |
| Prompt Injection | graph context 안의 악성 instruction이 LLM으로 전달될 수 있음 | injection ASR, policy compliance, context isolation score |

---

## 8. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | graph schema, source document, node, edge, relation, attribute, embedding, retrieval result, explanation path, citation, graph snapshot, update log, prompt-output log |
| 공격자 목표 | 악성 node 삽입, edge 조작, relation manipulation, metadata 오염, retrieval ranking 조작, citation spoofing, indirect prompt injection |
| 공격자 능력 | 문서·노드 기여, metadata 조작, graph update 오염, entity/relation extraction 오류 유도, prompt-like text 삽입 |
| 공격 경로 | source document → graph construction → graph update/indexing → graph retrieval → explanation path → graph context prompt → LLM output |
| 방어자 능력 | source validation, node/edge verification, schema validation, graph snapshot, update approval, retrieval audit, prompt isolation, citation verification |
| 제외 범위 | 실제 기업 graph 공격, 무단 내부 문서 사용, 실제 개인정보 graph 구축, 공격 payload 제공 |

---

## 9. 평가방법 및 지표

| 평가축 | 지표 | 의미 | W08/P02 활용 |
|---|---|---|---|
| Retrieval quality | Recall@k, Precision@k, MRR, nDCG | 관련 node/path/subgraph 검색 성능 | Graph retrieval 평가 |
| Graph integrity | IntegrityScore, verified node/edge rate | graph 구조의 검증 정도 | graph poisoning 평가 |
| Evidence coverage | EvidenceCoverage | 필요한 근거를 충분히 가져왔는지 | hallucination 완화 평가 |
| Explanation quality | ExplainScore, path faithfulness | 답변 설명 경로의 타당성 | human review 지원 |
| Answer faithfulness | faithfulness score, citation support | 답변이 graph 근거와 일치하는지 | RAG 출력 검증 |
| Security robustness | poisoned retrieval rate, injection ASR | 오염 graph/context에서 안전한지 | W08 P04/P05 연결 |
| Update reliability | update approval rate, rollback success | graph 변경 관리 가능성 | W14 MLOps 연결 |
| Cost | indexing cost, retrieval latency, graph update cost | 운영 가능성 | 실서비스 평가 |

---

## 10. 재현성 체크리스트

| 항목 | 기록해야 할 내용 |
|---|---|
| Graph source | 원문 문서, database, crawl source, license, collection date |
| Graph schema | node type, edge type, relation schema, attribute schema |
| Construction method | entity extraction, relation extraction, chunking, summarization, deduplication |
| Graph snapshot | graph version, node/edge count, update timestamp, hash |
| Retriever | graph query method, embedding model, reranker, Top-k, threshold |
| Generator | LLM model/version, prompt template, decoding setting, safety policy |
| Evaluation | retrieval metrics, integrity score, evidence coverage, faithfulness, injection ASR, latency |
| Security log | source-node-edge-path-output trace, update approval, human review, failure cases |
| 한계 | toy graph 또는 공개 데이터 결과를 실제 기업 RAG 보안 보증으로 과장하지 않음 |

---

## 11. 논문의 고유 기여

1. Graph-based approach를 RAG의 기능 관점에서 체계적으로 분류한다.
2. Graph construction, retrieval, reasoning, explanation, update가 RAG 성능과 신뢰성에 미치는 영향을 정리한다.
3. GraphRAG 평가에서 retrieval quality뿐 아니라 graph integrity, evidence coverage, explanation path가 중요함을 설명할 수 있는 근거를 제공한다.
4. W08 보안 관점에서 node/edge poisoning, graph update 오염, citation spoofing, indirect prompt injection을 분석할 수 있는 구조를 제공한다.
5. W14 MLOps와 W15 reproducibility에서 graph snapshot, update approval, audit log를 요구하는 근거 문헌으로 활용 가능하다.

---

## 12. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 직접 prompt injection 방어 논문은 아님 | Graph-based RAG survey이며 공격·방어 상세 실험 논문은 아니다. | W08 P04/P05와 결합해 보안 평가로 확장 |
| Graph construction 오류 | entity/relation extraction 오류가 graph 전체 품질을 낮춘다. | source validation과 node/edge verification 포함 |
| Dynamic graph 재현성 | graph가 계속 바뀌면 같은 질문에 다른 답이 나올 수 있다. | graph snapshot, version, update log 필수화 |
| Graph poisoning 위험 | 악성 node/edge가 검색과 reasoning path를 오염시킬 수 있다. | integrity score, poisoned retrieval rate 측정 |
| 민감 관계 노출 | graph는 숨은 관계를 드러내 privacy risk가 커질 수 있다. | access control, relation masking, audit log 반영 |
| 평가 표준 부족 | Graph-based RAG 전용 security benchmark가 아직 부족하다. | retrieval-faithfulness-integrity-injection 통합 지표 제안 |

---

## 13. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | RAG 보안은 vector retrieval뿐 아니라 graph structure와 update integrity 문제라는 문제의식 |
| 2장 관련연구 | Graph-based RAG approach와 functionality survey 정리 |
| 3장 위협모형 | graph schema, node, edge, relation, update log, explanation path 보호 자산 정의 |
| 4장 연구방법 | IntegrityScore, EvidenceCoverage, ExplainScore, injection ASR, provenance coverage 지표 설계 |
| 5장 분석 | Graph construction → retrieval → reasoning → generation attack surface mapping 표/그림 제시 |
| 6장 보안적 함의 | graph poisoning, relation leakage, update approval, human review, context isolation 필요성 해석 |

---

## 14. 기말논문 연결 3문장

1. W08에서 기말논문에 반영할 개념: Graph-based RAG는 LLM의 답변 근거를 vector chunk에서 graph node, edge, relation, path로 확장하므로, 검색 품질뿐 아니라 graph integrity와 explanation path faithfulness를 평가해야 한다.
2. W08에서 기말논문에 반영할 표·그림·실험: graph construction-update-retrieval-generation pipeline, node/edge poisoning 위협모형, IntegrityScore·EvidenceCoverage·injection ASR 평가표를 반영한다.
3. W08이 LLM 보안 감사 프레임워크와 연결되는 지점: graph context가 LLM prompt로 직렬화되는 순간, 오염된 node/edge와 prompt-like text가 indirect prompt injection으로 작동할 수 있으므로 graph snapshot과 update approval log를 W14/W15 evidence chain에 포함해야 한다.

---

## 15. 최종 판단

P02는 W08에서 Graph-based RAG의 기능과 보안 평가축을 확장하는 핵심 관련 문헌이다. 강의계획서의 저자명·제목 표기와 공식 DOI 기준 정보가 다르므로 `관련 논문 / 확인` 메모를 유지하되, Graph RAG 보안 평가에는 직접 활용 가능하다. 특히 기말논문에서 RAG 보안 점검표를 만들 경우 P02는 **graph integrity, evidence coverage, explanation path, graph update approval, relation leakage 평가**의 근거 문헌으로 사용하는 것이 적절하다.

---

## 16. 변환 호환성 메모

```bash
pandoc P02_summary.md -o P02_summary.docx
pandoc P02_summary.md -o P02_summary.pdf --pdf-engine=xelatex
```
