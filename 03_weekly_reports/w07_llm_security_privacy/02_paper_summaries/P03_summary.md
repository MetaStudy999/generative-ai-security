# P03 Summary

## A survey on large language model (LLM) security and privacy: The Good, The Bad, and The Ugly — Yifan Yao et al., High-Confidence Computing, 2024

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W07 LLM 보안·프라이버시 |
| 논문명 | A survey on large language model (LLM) security and privacy: The Good, The Bad, and The Ugly |
| 저자 | Yifan Yao et al. |
| 출판 정보 | High-Confidence Computing, 4(2), Article 100211, 2024 |
| DOI | https://doi.org/10.1016/j.hcc.2024.100211 |
| 보조 URL | https://arxiv.org/abs/2312.02003 |
| 검증 상태 | W07 `paper_list.md` 기준 공식 DOI 확인. 강의계획서 지정 AI Open 논문과 제목·저자·출판지 차이로 관련 보조 문헌 처리 |

---

## 1. 한 문장 요약

이 논문은 LLM 보안과 프라이버시를 **LLM for security, attacks on LLMs, privacy risks, misuse, defense opportunities** 관점에서 정리하며, W07에서 LLM의 양면성—보안 도구이자 공격 대상—을 설명하는 관련 핵심 문헌이다.

---

## 2. 핵심 연구질문

| 번호 | 연구질문 |
|---|---|
| RQ1 | LLM은 보안 자동화에 어떤 긍정적 기여를 할 수 있는가? |
| RQ2 | LLM 자체는 prompt attack, data leakage, backdoor, poisoning에 어떻게 취약한가? |
| RQ3 | LLM misuse와 dual-use risk는 어떤 정책·감사 체계가 필요한가? |
| RQ4 | 관련 보조 문헌으로 사용할 때 강의계획서 지정 문헌 차이를 어떻게 명시해야 하는가? |

---

## 3. 핵심 수식·지표

$$
Risk_{LLM}=w_1 ASR+w_2 LeakageRate+w_3 MisuseRisk-w_4 DefenseCoverage
$$

| 기호 | 의미 |
|---|---|
| $ASR$ | 공격 성공률 |
| $LeakageRate$ | 민감정보 노출률 |
| $MisuseRisk$ | 악용 가능성 위험 |
| $DefenseCoverage$ | 방어·감사 적용 범위 |

---

## 4. 보안 분석

| 축 | 내용 |
|---|---|
| Good | 취약점 분석, 로그 요약, 보안 교육, 정책 점검에 활용 가능 |
| Bad | jailbreak, prompt injection, data extraction, hallucination 위험 |
| Ugly | 악성 자동화, 사회공학, dual-use, 책임 소재 문제 |
| Defense | red teaming, guardrail, monitoring, provenance, human oversight 필요 |

---

## 5. 위협모형·평가지표

| 항목 | 내용 |
|---|---|
| 보호 자산 | prompt, output, training data, tool access, security workflow |
| 공격자 능력 | prompt 조작, 반복 질의, 안전정책 우회, 도구 오남용 유도 |
| 평가 지표 | ASR, leakage, misuse category, defense coverage, audit log completeness |
| 한계 | 공식 지정 논문과 차이가 있으므로 최종 제출 전 관련 문헌 표기를 명확히 해야 함 |

---

## 6. 기말논문 연결

P03은 LLM 보안의 양면성을 설명하는 관련 보조 문헌이다. 기말논문에서는 “LLM을 보안 도구로 쓰는 동시에 LLM 자체를 보안 평가 대상으로 삼아야 한다”는 논리를 제공한다.

---

## 7. 최종 판단

P03은 W07의 관련 보조 문헌이다. 공식 지정 문헌과 다르다는 검증 메모를 유지하되, LLM security/privacy taxonomy 구성에는 활용 가치가 있다.
