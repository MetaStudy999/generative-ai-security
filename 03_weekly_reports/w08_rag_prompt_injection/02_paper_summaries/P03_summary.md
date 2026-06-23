# P03 Summary

## Prompting Frameworks for Large Language Models: A Survey — Xiaoxia Liu et al., ACM Computing Surveys, 2026

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W08 RAG & Prompt Injection |
| 논문명 | Prompting Frameworks for Large Language Models: A Survey |
| 저자 | Xiaoxia Liu et al. |
| 출판 정보 | ACM Computing Surveys, 58(10), Article 255, 38 pages, 2026 |
| DOI | https://doi.org/10.1145/3789253 |
| 검증 상태 | W08 `paper_list.md` 기준 DOI/PDF 확인. 공식 서지 기준 인용 가능 |

---

## 1. 한 문장 요약

이 논문은 LLM prompting framework를 **zero/few-shot prompting, chain-of-thought, tool prompting, retrieval-augmented prompting, prompt optimization, evaluation** 관점에서 정리하고, W08에서 prompt가 보안 정책·검색 context·도구 호출을 제어하는 핵심 공격면이 됨을 설명한다.

---

## 2. 핵심 연구질문

| 번호 | 연구질문 |
|---|---|
| RQ1 | Prompting framework는 LLM 행동을 어떤 방식으로 구조화하는가? |
| RQ2 | CoT, tool prompting, RAG prompting은 어떤 새로운 보안 공격면을 만드는가? |
| RQ3 | Prompt template과 system instruction은 어떻게 감사·버전관리해야 하는가? |
| RQ4 | Prompt injection은 prompt framework의 어떤 신뢰 경계 실패로 볼 수 있는가? |

---

## 3. 핵심 수식·구조

$$
y_t\sim p_\theta(y_t\mid s,u,c,r,y_{<t})
$$

| 기호 | 의미 |
|---|---|
| $s$ | system prompt |
| $u$ | user prompt |
| $c$ | context/history |
| $r$ | retrieved documents |
| $y_t$ | 생성 token |

### 보안 해석

LLM 출력은 system instruction, user input, retrieval context가 결합된 조건부 생성 결과다. 신뢰할 수 없는 문서가 $r$에 들어오면 system policy와 충돌하는 간접 지시가 포함될 수 있다.

---

## 4. 위협모형·평가지표

| 항목 | 내용 |
|---|---|
| 보호 자산 | system prompt, prompt template, retrieved context, tool instruction, output policy |
| 공격자 목표 | prompt injection, system instruction override, tool misuse, policy bypass |
| 공격자 능력 | 악성 문서 삽입, user prompt 조작, indirect instruction 포함 |
| 지표 | ASR, instruction conflict rate, policy compliance, utility, over-refusal |
| 재현성 | prompt template version, system/user/context 분리 로그 필요 |

---

## 5. 기말논문 연결

P03은 W08의 prompt 구조와 신뢰 경계를 정의한다. 기말논문에서는 prompt 구성요소를 system/user/retrieved/tool로 분리하고 각 계층별 방어·감사 지표를 제시한다.

---

## 6. 최종 판단

P03은 W08에서 prompt injection을 구조적으로 해석하기 위한 핵심 문헌이다. RAG 보안 평가의 prompt pipeline 정의에 직접 사용한다.
