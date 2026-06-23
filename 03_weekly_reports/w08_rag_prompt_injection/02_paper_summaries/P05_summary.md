# P05 Summary

## Vulnerability of Large Language Models to Prompt Injection When Providing Medical Advice — Ro Woon Lee et al., JAMA Network Open, 2025

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W08 RAG & Prompt Injection |
| 논문명 | Vulnerability of Large Language Models to Prompt Injection When Providing Medical Advice |
| 저자 | Ro Woon Lee et al. |
| 출판 정보 | JAMA Network Open, 8(12):e2549963, 2025 |
| DOI | https://doi.org/10.1001/jamanetworkopen.2025.49963 |
| 검증 상태 | W08 `paper_list.md` 기준 DOI/PDF 확인. 강의계획서 제목과 동일 여부 추가 확인 메모 유지 |

---

## 1. 한 문장 요약

이 논문은 의료 조언 맥락에서 LLM이 prompt injection에 취약할 수 있음을 보여주는 고위험 응용 사례 문헌이며, W08에서 prompt injection 평가가 단순 보안 문제가 아니라 의료·법률·금융 등 high-stakes domain의 안전 문제임을 설명한다.

---

## 2. 핵심 연구질문

| 번호 | 연구질문 |
|---|---|
| RQ1 | 의료 조언 제공 상황에서 prompt injection은 어떤 방식으로 모델 응답을 왜곡할 수 있는가? |
| RQ2 | High-stakes domain에서 LLM 안전성 평가는 일반 챗봇 평가와 무엇이 다른가? |
| RQ3 | 공격 성공 여부뿐 아니라 harmful advice, refusal, escalation, citation support를 어떻게 봐야 하는가? |
| RQ4 | 기말논문에서 실제 의료 조언을 생성하지 않고 안전하게 사례를 활용하려면 어떤 범위 제한이 필요한가? |

---

## 3. 핵심 수식·지표

$$
UnsafeAdviceRate=\frac{N_{unsafe\ medical\ outputs}}{N_{injection\ prompts}}
$$

$$
SafeEscalationRate=\frac{N_{refer\ to\ professional}}{N_{high\ risk\ prompts}}
$$

| 기호 | 의미 |
|---|---|
| $UnsafeAdviceRate$ | 위험 응답 비율 |
| $SafeEscalationRate$ | 전문가 상담·안전 안내로 전환한 비율 |

---

## 4. 위협모형·평가지표

| 항목 | 내용 |
|---|---|
| 보호 자산 | 환자 안전, 의료 정보 신뢰성, 사용자 개인정보, 시스템 정책 |
| 공격자 목표 | 위험 조언 유도, 안전정책 우회, 근거 없는 의료정보 생성 |
| 공격자 능력 | injection prompt 작성, 문서/컨텍스트 오염, 반복 질의 |
| 지표 | unsafe advice rate, refusal quality, safe escalation, citation support, hallucination |
| 제외 범위 | 실제 환자 상담, 진단·치료 지시 생성, 개인정보 기반 실험 |

---

## 5. 기말논문 연결

P05는 prompt injection의 high-stakes 사례로 활용한다. 기말논문에서는 의료 내용을 직접 조언하지 않고, “고위험 도메인에서는 안전한 거절·전문가 안내·근거 확인·감사 로그가 필수”라는 평가 원칙으로 반영한다.

---

## 6. 최종 판단

P05는 W08의 관련 보조 문헌이다. prompt injection이 실제 사회적 피해로 연결될 수 있음을 보여주므로, RAG/LLM 보안 평가에 high-stakes safety 항목을 추가하는 근거가 된다.
