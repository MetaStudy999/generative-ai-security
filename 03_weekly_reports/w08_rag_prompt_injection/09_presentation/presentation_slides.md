# W08 RAG와 Prompt Injection

Research Question: RAG와 Prompt Injection에서 성능 지표와 보안 지표를 어떻게 분리해 평가할 수 있는가?

---

## Core Formula

### Retrieval Score와 Context-Conditioned Generation

$$
s(q,d)=\frac{e(q)^\top e(d)}{\lVert e(q)\rVert_2\lVert e(d)\rVert_2},
\qquad
p(y|q,C)=\prod_{t=1}^{T}p_\theta(y_t|y_{<t},q,C)
$$

| 기호 | 의미 |
|---|---|
| `q,d` | query와 retrieved document |
| `e(\cdot)` | embedding function |
| `C` | retrieved context set |
| `y_t` | 생성 응답의 t번째 토큰 |

- 직관적 의미: RAG는 query와 문서의 유사도로 context를 고르고, 그 context에 조건화해 답을 생성한다.
- 보안적 의미: 검색된 context가 오염되면 생성 단계가 공격 문맥에 영향을 받을 수 있다.
- 평가 지표 연결: retrieval_relevance, faithfulness, source_verification_rate와 연결한다.
- 한계: 표준 RAG 구조 설명이며 특정 벤치마크 수치를 새로 만들지 않는다.

---

## Threat Model

- Diagram: RAG pipeline threat model
- Stages: Query, Retriever, Context Filter, Generator, Verification
- 안전 범위: public, synthetic, toy, local evaluation

![W08 pipeline diagram](assets/diagrams/w08_pipeline_diagram.svg)

---

## Evaluation Protocol

- Metrics: retrieval_relevance, attack_success_rate, source_verification_rate, tool_misuse_rate, faithfulness
- 데이터 출처: `04_experiment/outputs/metrics_summary.csv`

| condition | retrieval_relevance | attack_success_rate | source_verification_rate | tool_misuse_rate | faithfulness |
| --- | --- | --- | --- | --- | --- |
| Clean RAG | 0.908 | 0 | 1 | 0 | 0.908 |
| Poisoned document | 0.69 | 0.575 | 0.275 | 0.125 | 0.458 |
| Source filter 적용 | 0.777 | 0.05 | 1 | 0.025 | 0.779 |
| Human approval 적용 | 0.765 | 0.025 | 1 | 0 | 0.841 |

---

## Figure-first Result

![W08 metrics chart](assets/charts/w08_metrics_chart.svg)

그래프는 RAG 조건별 retrieval_relevance, attack_success_rate, source_verification_rate, tool_misuse_rate, faithfulness를 비교한다. 검색 품질이 좋아도 injection이나 contamination 위험이 별도로 존재할 수 있다. 차트는 output CSV의 수치만 사용한다.

---

## Paper Map

| ID | 논문 역할 | 발표에서 쓰는 위치 | 기말논문 연결 |
|---|---|---|---|
| P01 | 핵심 이론 | Background / Core Formula | RAG와 Prompt Injection의 관련연구 뼈대 |
| P02 | 위협 분류 | Threat Model | 공격자·방어자·보호자산 정의 |
| P03 | 평가 지표 | Evaluation Protocol | 정량 지표와 로그 근거 연결 |
| P04 | 공격·방어 사례 | Security Implication | 보안적 함의와 방어 한계 |
| P05 | 재현성·정책 근거 | Limitation | 확인 필요 항목과 제출 전 검증 |

---

## Limitation

- prompt injection은 방어 평가 관점으로만 설명하고 실제 우회 절차는 제공하지 않는다.
- 원문 DOI/URL과 formal guarantee는 최종 제출 전 확인 필요.
- 실제 운영 시스템 악용 절차나 무단 API 질의 절차는 포함하지 않음.

---

## Final Takeaway

W08의 핵심은 `retrieval_relevance, attack_success_rate, source_verification_rate, tool_misuse_rate, faithfulness`를 성능·보안·재현성 근거로 분리해 기말논문의 평가방법에 연결하는 것이다.
