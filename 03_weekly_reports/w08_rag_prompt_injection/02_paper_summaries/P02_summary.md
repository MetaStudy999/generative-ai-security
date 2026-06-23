# P02 Summary

## Graph-Based Approaches and Functionalities in Retrieval-Augmented Generation: A Comprehensive Survey — Zulun Zhu et al., ACM Computing Surveys, 2026

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W08 RAG & Prompt Injection |
| 논문명 | Graph-Based Approaches and Functionalities in Retrieval-Augmented Generation: A Comprehensive Survey |
| 저자 | Zulun Zhu et al. |
| 출판 정보 | ACM Computing Surveys, 58(10), Article 261, 38 pages, 2026 |
| DOI | https://doi.org/10.1145/3795880 |
| 검증 상태 | W08 `paper_list.md` 기준 DOI/PDF 확인. 강의계획서 저자명·제목 차이 메모 유지 |

---

## 1. 한 문장 요약

이 논문은 RAG에서 graph-based approach와 기능을 **indexing, retrieval, reasoning, explainability, knowledge grounding, graph update, evaluation** 관점에서 정리하고, W08에서 RAG 보안을 graph provenance와 retrieval integrity 문제로 확장한다.

---

## 2. 핵심 연구질문

| 번호 | 연구질문 |
|---|---|
| RQ1 | Graph-based RAG는 vector-only RAG의 어떤 한계를 보완하는가? |
| RQ2 | graph construction과 graph update 과정은 어떤 보안 위험을 만드는가? |
| RQ3 | Graph reasoning은 답변 설명가능성과 citation support를 어떻게 개선할 수 있는가? |
| RQ4 | Graph node/edge poisoning을 어떻게 평가하고 감사할 수 있는가? |

---

## 3. 핵심 수식·지표

$$
R(q)=\operatorname{Retrieve}(q,G=(V,E))
$$

$$
IntegrityScore=\frac{|E_{verified}|+|V_{verified}|}{|E|+|V|}
$$

| 기호 | 의미 |
|---|---|
| $G=(V,E)$ | graph 구조 |
| $V_{verified},E_{verified}$ | 검증된 node/edge |
| $IntegrityScore$ | graph 무결성 점수 |

---

## 4. 위협모형·평가지표

| 항목 | 내용 |
|---|---|
| 보호 자산 | graph schema, node, edge, retrieval result, explanation path |
| 공격자 목표 | 오염 node 삽입, edge 조작, reasoning path 왜곡, citation 오염 |
| 공격자 능력 | 문서·노드 기여, metadata 조작, graph update 오염 |
| 지표 | graph integrity, evidence coverage, retrieval precision, answer faithfulness, ASR |

---

## 5. 기말논문 연결

P02는 RAG 평가에 graph 무결성, evidence path, explanation path를 추가하는 근거로 사용한다. W14 MLOps에서는 graph snapshot과 update approval log로 확장한다.

---

## 6. 최종 판단

P02는 W08의 graph-based RAG 관련 핵심 보조 문헌이다. 강의계획서 표기 차이 메모를 유지하고 공식 DOI 기준으로 인용한다.
