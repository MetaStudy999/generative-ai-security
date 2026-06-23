# W08 100점형 통합 Summary

## RAG & Prompt Injection

## 0. 문서 목적

이 문서는 W08 개별 논문 summary 5개를 기말논문 작성용 연구 노트로 통합한 100점형 요약본이다. RAG 구조, graph provenance, prompting framework, prompt injection, high-stakes safety를 하나의 평가체계로 묶는다.

---

## 1. 한 문장 통합 요약

W08은 RAG 시스템을 **검색 문서, graph node/edge, prompt template, system/user/retrieved instruction, LLM generation, tool/log audit**로 구성된 보안 대상 시스템으로 보고, prompt injection과 문서 오염을 ASR, policy compliance, evidence faithfulness, source isolation, high-stakes safety로 분리해 평가하는 주차다.

---

## 2. 문헌 5편 통합 매트릭스

| ID | 논문 | 핵심 역할 | 주요 지표 |
|---|---|---|---|
| P01 | Graph RAG Survey | graph RAG 구조와 provenance | evidence path, citation support |
| P02 | Graph-Based RAG Survey | graph 기능·무결성 평가 | graph integrity, source precision |
| P03 | Prompting Frameworks Survey | prompt 구조와 신뢰 경계 | policy compliance, utility |
| P04 | Prompt Injection Survey | 직접 보안 위협 핵심 | injection ASR, source isolation |
| P05 | Medical Prompt Injection | high-stakes safety 사례 | unsafe advice, safe escalation |

---

## 3. 핵심 수식 묶음

### 3.1 RAG Retrieval

$$
D_k(q)=TopK_{d_i\in D}\; sim(E(q),E(d_i))
$$

### 3.2 LLM Conditional Generation

$$
y_t\sim p_\theta(y_t\mid s,u,r,y_{<t})
$$

### 3.3 Prompt Injection ASR

$$
ASR_{inj}=\frac{1}{N}\sum_{i=1}^{N}\mathbf{1}[f_\theta(s,u_i,d_i^{mal})=y_i^{attack}]
$$

### 3.4 Evidence Integrity

$$
IntegrityScore=\frac{|E_{verified}|+|V_{verified}|}{|E|+|V|}
$$

---

## 4. 통합 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | system prompt, retrieved document, graph node/edge, evidence path, citation, tool permission, output log |
| 공격자 목표 | instruction override, 문서 오염, citation 조작, tool misuse, unsafe advice 유도 |
| 공격자 능력 | 악성 문서 삽입, metadata 조작, graph edge poisoning, prompt injection, context stuffing |
| 방어자 능력 | source filtering, instruction hierarchy, context isolation, output monitoring, human review |
| 제외 범위 | 실제 서비스 공격, 의료 조언 생성, 개인정보 포함 실험, 유해 지시문 배포 |

---

## 5. 통합 평가 지표

| 평가축 | 대표 지표 | 해석 |
|---|---|---|
| Retrieval Quality | recall@k, source precision | 올바른 문서 검색 |
| Evidence Faithfulness | citation support, groundedness | 답변이 근거에 기반하는가 |
| Injection Robustness | ASR, policy compliance | 악성 지시문 저항성 |
| Source Isolation | malicious document 영향 차단 | 문서-지시문 분리 성공 |
| Graph Integrity | verified node/edge ratio | graph 무결성 |
| Safety | unsafe advice rate, safe escalation | 고위험 도메인 안전성 |
| Auditability | prompt/context/output/tool log | 사후 검증 가능성 |

---

## 6. 재현성 체크리스트

| 항목 | 필수 기록 |
|---|---|
| Corpus | 문서 버전, 출처, hash, chunking setting |
| Graph | node/edge schema, graph snapshot, update log |
| Retrieval | embedding model, top-k, reranker, filter policy |
| Prompt | system/user/context/template 분리 기록 |
| Attack set | malicious document, injection prompt, expected unsafe target |
| 평가 | ASR, groundedness, compliance, over-refusal, utility |
| 한계 | toy RAG 결과를 실제 의료·법률·금융 안전성으로 일반화 금지 |

---

## 7. 기말논문 연결 3문장

1. W08에서 기말논문에 반영할 개념: RAG 보안은 모델 자체보다 검색 문서, graph 구조, prompt 신뢰 경계, 문서 출처, output audit가 결합된 시스템 보안 문제다.
2. 반영할 표·그림·실험: RAG pipeline, prompt injection ASR, evidence integrity, source isolation, high-stakes safety 평가표를 반영한다.
3. W14 연결: RAG 문서와 graph update는 MLOps 공급망 자산이므로 W08의 provenance·auditability 지표를 W14 운영 감사로 확장한다.

---

## 8. 최종 판단

W08은 기말논문의 핵심 주제 후보와 가장 직접적으로 연결된다. Graph RAG, prompting framework, prompt injection, high-stakes safety를 묶어 “RAG 기반 LLM 시스템의 문서 오염 및 프롬프트 인젝션 평가 프레임워크”로 발전시키는 것이 적절하다.
