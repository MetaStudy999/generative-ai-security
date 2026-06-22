# W08 RAG·프롬프팅 프레임워크 & 프롬프트 인젝션

LLM이 검색 문서를 읽는 순간, 문서는 근거이면서 동시에 공격면이 된다.

---

## 1. 핵심 질문

- RAG에서 indirect prompt injection은 어디서 들어오는가
- Source verification은 ASR을 낮출 수 있는가
- Human approval gate는 tool misuse를 막을 수 있는가

---

## 2. AI 원리 70%

| 단계 | 역할 | 보안 연결 |
|---|---|---|
| Retrieval | 관련 문서 검색 | 오염 문서 유입 |
| Reranking | 후보 재정렬 | trust score 필요 |
| Generation | context 기반 답변 | context hijacking |
| Tool action | 외부 행동 | approval gate |

---

## 3. 문헌의 역할

P01/P02는 GraphRAG와 graph 기능, P03은 prompting framework, P04는 prompt injection taxonomy, P05는 safety-critical 취약성 사례를 제공한다.

---

## 4. 위협모형

```text
Poisoned document -> Retrieved context -> LLM answer -> Tool action
```

보호 자산은 검색 문서, vector DB, graph DB, system prompt, user context, tool 권한, audit log다.

---

## 5. 실험 설계

- Synthetic RAG documents
- 조건별 40개, 총 160개 sample
- 실제 LLM/API 호출 없음
- Seed 42
- 지표: Retrieval Relevance, ASR, Source Verification, Tool Misuse Rate, Faithfulness, Answer Rate

---

## 6. 실험 결과

| 조건 | ASR | Source Verification | Tool Misuse |
|---|---:|---:|---:|
| Clean RAG | 0.000000 | 1.000000 | 0.000000 |
| Poisoned document | 0.575000 | 0.275000 | 0.125000 |
| Source filter 적용 | 0.050000 | 1.000000 | 0.025000 |
| Human approval 적용 | 0.025000 | 1.000000 | 0.000000 |

---

## 7. 해석

- Source filter는 ASR을 크게 낮춘다.
- Human approval은 tool misuse를 차단한다.
- 단, answer rate가 낮아질 수 있어 사용성 비용을 함께 봐야 한다.

---

## 8. 기말논문 연결

RAG 기반 생성형 AI 시스템에서 간접 프롬프트 인젝션 대응을 위한 출처 검증·승인 게이트 평가 프레임워크.

---

## 9. 결론

RAG 보안은 “좋은 검색”만의 문제가 아니다. 출처, prompt boundary, tool 권한, 승인 로그를 함께 설계해야 한다.
