# P04 Summary

## Prompt Injection Attacks on Large Language Models: A Survey of Attack Methods, Root Causes, and Defense Strategies — Tongcheng Geng et al., Computers, Materials & Continua, 2026

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W08 RAG & Prompt Injection |
| 논문명 | Prompt Injection Attacks on Large Language Models: A Survey of Attack Methods, Root Causes, and Defense Strategies |
| 저자 | Tongcheng Geng, Zhiyuan Xu, Yubin Qu, W. Eric Wong |
| 출판 정보 | Computers, Materials & Continua, 87(1), pp. 1–10, 2026 |
| DOI | https://doi.org/10.32604/cmc.2025.074081 |
| 검증 상태 | W08 `paper_list.md` 기준 DOI/PDF 확인. Tianlei/Tongcheng 저자명 차이 메모 유지 |

---

## 1. 한 문장 요약

이 논문은 LLM prompt injection을 **attack methods, root causes, direct/indirect injection, instruction hierarchy failure, context contamination, defense strategies** 관점에서 정리하는 W08의 핵심 보안 문헌이다.

---

## 2. 핵심 연구질문

| 번호 | 연구질문 |
|---|---|
| RQ1 | Prompt injection은 direct injection과 indirect injection으로 어떻게 구분되는가? |
| RQ2 | LLM이 system/user/retrieved instruction을 명확히 분리하지 못하는 근본 원인은 무엇인가? |
| RQ3 | RAG 문서와 외부 도구가 prompt injection 공격면을 어떻게 확장하는가? |
| RQ4 | 방어는 input filtering, instruction hierarchy, content isolation, output monitoring으로 어떻게 구성되는가? |

---

## 3. 핵심 수식·지표

### 3.1 Injection Attack Success Rate

$$
ASR_{inj}=\frac{1}{N}\sum_{i=1}^{N}\mathbf{1}[f_\theta(s,u_i,d_i^{mal})=y_i^{attack}]
$$

| 기호 | 의미 |
|---|---|
| $s$ | system prompt |
| $u_i$ | user query |
| $d_i^{mal}$ | 악성 지시문이 포함된 retrieved document |
| $y_i^{attack}$ | 공격자 목표 출력 |

### 3.2 Policy Compliance

$$
Compliance=1-ASR_{inj}-ViolationRate
$$

---

## 4. 위협모형·평가지표

| 항목 | 내용 |
|---|---|
| 보호 자산 | system prompt, developer instruction, user intent, retrieved document, tool permission |
| 공격자 목표 | instruction override, data exfiltration, harmful output, tool misuse |
| 공격자 능력 | user prompt 작성, 웹/문서/검색 결과에 악성 instruction 삽입 |
| 지표 | ASR, policy compliance, over-refusal, detection rate, source isolation success |
| 제외 범위 | 실제 서비스 공격, 유해 지시문 배포, 개인정보 유출 실험 |

---

## 5. 기말논문 연결

P04는 W08의 직접 보안 핵심 문헌이다. 기말논문에서는 RAG 문서 오염을 indirect prompt injection으로 정의하고, ASR·compliance·source isolation·audit log를 평가 지표로 사용한다.

---

## 6. 최종 판단

P04는 W08의 중심 문헌이다. RAG/prompt injection 평가에서 공격자 능력, 신뢰 경계, 방어전략, 실험 한계 문장을 모두 제공한다.
