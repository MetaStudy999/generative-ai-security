# P01 Summary

## Graph Retrieval-Augmented Generation: A Survey — Boci Peng et al., ACM TOIS, 2025/2026

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W08 RAG & Prompt Injection |
| 논문명 | Graph Retrieval-Augmented Generation: A Survey |
| 저자 | Boci Peng et al. |
| 출판 정보 | ACM Transactions on Information Systems, 44(2), pp. 1–52 |
| DOI | https://doi.org/10.1145/3777378 |
| 보조 URL | https://arxiv.org/abs/2408.08921 |
| 검증 상태 | W08 `paper_list.md` 기준 공식 DOI 확인. 강의계획서 Shiyu Chen/ACM CSUR 표기 차이 메모 유지 |

---

## 1. 한 문장 요약

이 논문은 Graph RAG를 **graph construction, retrieval, reasoning, augmentation, knowledge graph, citation/provenance, graph-enhanced generation** 관점에서 정리하고, W08에서 RAG 문서·노드·엣지·근거 출처가 보안 자산이 됨을 설명하는 관련 핵심 문헌이다.

---

## 2. 핵심 연구질문

| 번호 | 연구질문 |
|---|---|
| RQ1 | RAG에 graph structure를 결합하면 검색과 추론은 어떻게 달라지는가? |
| RQ2 | graph node, edge, evidence path는 어떤 provenance와 감사 가치를 갖는가? |
| RQ3 | graph poisoning, malicious node, edge manipulation은 RAG 출력을 어떻게 왜곡할 수 있는가? |
| RQ4 | Graph RAG의 보안 평가는 retrieval quality와 generation safety를 어떻게 함께 봐야 하는가? |

---

## 3. 핵심 수식·지표

### 3.1 Graph Retrieval

$$
D_k(q)=TopK_{v_i\in V}\; sim(E(q),E(v_i))
$$

### 3.2 Evidence Path Score

$$
Score(q,path)=\alpha\cdot sim(E(q),E(path))+\beta\cdot Trust(path)
$$

| 기호 | 의미 |
|---|---|
| $V$ | graph node 집합 |
| $E(\cdot)$ | embedding 함수 |
| $Trust(path)$ | 출처·검증·신뢰도 점수 |

---

## 4. 위협모형·평가지표

| 항목 | 내용 |
|---|---|
| 보호 자산 | graph node, edge, relation, source document, evidence path, citation |
| 공격자 목표 | malicious node 삽입, edge 조작, evidence path 왜곡, 답변 오염 |
| 공격자 능력 | 문서 업로드, metadata 조작, graph edge poisoning, retrieval ranking 조작 |
| 지표 | retrieval recall, source precision, evidence faithfulness, citation support, injection ASR |
| 재현성 | graph snapshot, node/edge version, retrieval config, prompt, output log 기록 |

---

## 5. 기말논문 연결

Graph RAG는 RAG 보안을 단순 vector retrieval 문제가 아니라 지식 구조와 provenance 문제로 확장한다. 기말논문에서는 문서 출처, graph node/edge 무결성, evidence path 감사표로 반영한다.

---

## 6. 최종 판단

P01은 W08의 RAG 구조와 provenance 평가 배경 문헌이다. 강의계획서 표기 차이 때문에 관련 논문 상태를 유지하되, Graph RAG 보안 평가에는 직접 활용 가능하다.
