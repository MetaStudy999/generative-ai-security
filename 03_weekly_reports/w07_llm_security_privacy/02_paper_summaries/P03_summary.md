# P03 Summary

## A survey on large language model (LLM) security and privacy: The Good, The Bad, and The Ugly — Yifan Yao et al., High-Confidence Computing, 2024

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W07 LLM 보안·프라이버시 |
| 논문명 | A survey on large language model (LLM) security and privacy: The Good, The Bad, and The Ugly |
| 저자 | Yifan Yao et al. |
| 공식 출판 정보 | High-Confidence Computing, Vol. 4, No. 2, Article 100211, 2024 |
| DOI | https://doi.org/10.1016/j.hcc.2024.100211 |
| 보조 URL | https://arxiv.org/abs/2312.02003 |
| 검증 상태 | W07 `paper_list.md` 기준 공식 DOI 확인. 강의계획서 지정 AI Open 논문과 제목·저자·출판지가 달라 관련 보조 문헌으로 처리 |
| 핵심 근거 사용 가능 여부 | 관련 보조 문헌으로 사용. LLM security/privacy의 양면성, dual-use risk, 방어 기회 정리에 유용 |

---

## 1. 한 문장 요약

이 논문은 LLM을 **보안을 강화하는 도구**, **공격자가 악용할 수 있는 도구**, **그 자체가 공격받는 시스템**이라는 세 관점으로 나누어 보안·프라이버시 문제를 정리하며, LLM 활용은 편익과 위험을 동시에 평가해야 한다는 dual-use 보안 프레임을 제공한다.

---

## 2. 핵심 연구문제

> LLM은 보안 분야에 어떤 긍정적 기여를 할 수 있으며, 동시에 어떤 악용 가능성과 자체 취약성을 갖는가?

| 번호 | 연구질문 |
|---|---|
| RQ1 | LLM은 취약점 탐지, 보안 로그 분석, 위협 인텔리전스 요약, 보안 교육에 어떻게 활용될 수 있는가? |
| RQ2 | LLM은 jailbreak, prompt injection, privacy leakage, hallucination, malicious automation에 어떻게 악용될 수 있는가? |
| RQ3 | LLM 자체는 poisoning, backdoor, data extraction, model stealing, prompt leakage에 어떤 취약성을 갖는가? |
| RQ4 | LLM 보안 연구는 “도구로서의 LLM”과 “보호 대상으로서의 LLM”을 어떻게 동시에 다뤄야 하는가? |
| RQ5 | 기말논문에서 LLM의 dual-use 위험을 어떤 안전한 toy evaluation과 감사 지표로 제한해 제시할 수 있는가? |

---

## 3. Good / Bad / Ugly 프레임

| 구분 | 의미 | W07 적용 |
|---|---|---|
| Good | LLM이 보안 업무를 보조하는 긍정적 사용 | 로그 요약, 정책 문서 정리, 취약점 설명, 보안 교육 |
| Bad | LLM이 공격·우회·허위정보 생성에 악용될 가능성 | jailbreak, phishing-style prompt, hallucinated security advice |
| Ugly | 책임소재, 악용 자동화, 프라이버시 침해, 사회적 파급 | dual-use governance, human review, audit log 필요 |

---

## 4. 핵심 이론 및 수식

> 아래 수식은 논문이 제시하는 dual-use 관점을 W07 보고서의 평가 지표로 변환한 표현이다. 악용 절차가 아니라 위험 평가 프레임이다.

### 4.1 LLM 보안 위험 점수

$$
Risk_{LLM}=w_1 ASR+w_2 LeakageRate+w_3 MisuseRisk-w_4 DefenseCoverage
$$

| 기호 | 의미 |
|---|---|
| $ASR$ | 공격 또는 우회 프롬프트 성공률 |
| $LeakageRate$ | 민감정보 노출률 |
| $MisuseRisk$ | 악용 가능성 또는 dual-use 위험 수준 |
| $DefenseCoverage$ | 방어·감사·정책 통제가 적용된 범위 |
| $w_i$ | 각 위험 요인의 가중치 |

### 보안적 의미

LLM이 유용하다고 해서 안전한 것은 아니다. 보안 업무 자동화에 쓰는 경우에도 공격 성공률, 정보누출, 악용 가능성, 방어 적용 범위를 함께 평가해야 한다.

---

### 4.2 방어 적용 범위

$$
DefenseCoverage=\frac{|Controls_{applied}|}{|Controls_{required}|}
$$

| 기호 | 의미 |
|---|---|
| $Controls_{applied}$ | 실제 적용된 통제. 예: 필터링, human review, logging, access control |
| $Controls_{required}$ | threat model상 필요한 통제 목록 |

### 보안적 의미

LLM 사용 정책이 문서로만 존재하고 실제 로그·승인·검토가 없으면 방어가 적용되었다고 볼 수 없다. W14/W15의 evidence chain과 직접 연결된다.

---

### 4.3 안전한 보안 보조 성능

$$
SecureAssistScore=Utility_{security}-\lambda_1 HallucinationRate-\lambda_2 UnsafeSuggestionRate-\lambda_3 LeakageRate
$$

| 기호 | 의미 |
|---|---|
| $Utility_{security}$ | 보안 업무 보조 성능 |
| $HallucinationRate$ | 근거 없는 보안 설명 또는 허위 권고 비율 |
| $UnsafeSuggestionRate$ | 위험하거나 부적절한 보안 조언 비율 |
| $LeakageRate$ | 민감정보 노출률 |

### 보안적 의미

LLM이 보안 업무를 도와도 허위 취약점 설명, 부정확한 조치, 민감 로그 노출이 발생하면 운영 위험이 된다.

---

## 5. LLM 보안의 양면성 분석

| 관점 | 설명 | 평가 지표 |
|---|---|---|
| LLM for Security | 보안 로그 요약, 취약점 설명, 정책 검토 등 방어 업무 보조 | utility, hallucination, human review agreement |
| Security of LLM | LLM 자체의 prompt injection, jailbreak, leakage, poisoning 위험 | ASR, leakage rate, refusal quality |
| LLM-enabled Misuse | 사회공학, 허위정보, 악성 자동화 등 악용 위험 | misuse category, safety violation, monitoring coverage |
| Governance | 사용 범위, 승인, 로깅, 책임소재 관리 | defense coverage, audit completeness |

---

## 6. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | 보안 로그, 취약점 리포트, 내부 정책, system prompt, tool credential, 모델 출력, 감사 로그 |
| 공격자 목표 | 안전정책 우회, 민감정보 추출, 보안 자동화 오남용, 허위 보안 조언 생성 |
| 공격자 능력 | prompt 조작, 반복 질의, 간접 지시 삽입, 민감 로그 제공 유도, 도구 권한 오용 유도 |
| 방어자 능력 | red teaming, guardrail, human review, access control, prompt/output logging, approval workflow |
| 제외 범위 | 실제 시스템 공격, 악성코드 작성, 실제 개인정보·취약점 악용 절차 제공 |

---

## 7. 평가방법 및 지표

| 지표 | 의미 | W07/P03 활용 |
|---|---|---|
| Security Utility | LLM이 보안 업무를 얼마나 정확히 보조하는지 | 방어 도구로서의 성능 |
| Hallucination Rate | 허위 보안 설명·근거 없는 권고 비율 | 보안 업무 위험 |
| Unsafe Suggestion Rate | 위험하거나 부적절한 조치 제안 비율 | high-stakes 제한 |
| ASR | 정책 우회·공격 성공률 | 공격 대상으로서의 LLM 평가 |
| Leakage Rate | 민감 로그·정보 노출률 | 프라이버시 평가 |
| Defense Coverage | 필요한 통제 중 실제 적용된 통제 비율 | governance 평가 |
| Audit Completeness | 입력·출력·도구 호출·검토 로그 보존 정도 | W14/W15 연결 |

---

## 8. 재현성 체크리스트

| 항목 | 기록해야 할 내용 |
|---|---|
| 모델 | 모델명, 버전, endpoint, 설정값 |
| 사용 시나리오 | 보안 로그 요약, 취약점 설명, 정책 점검 등 사용 범위 |
| 입력 데이터 | synthetic log 또는 공개 예시만 사용. 실제 민감 로그 제외 |
| 방어 통제 | human review, refusal policy, tool 권한 제한, logging 여부 |
| 출력 검증 | hallucination, unsafe suggestion, leakage 여부 |
| 책임성 | 최종 판단자는 사람이며, LLM 출력은 검토 대상임을 명시 |
| 한계 | toy evaluation 결과를 실제 보안관제 성능으로 일반화하지 않음 |

---

## 9. 논문의 고유 기여

1. LLM을 보안 도구와 보안 대상이라는 양면성으로 동시에 정리한다.
2. LLM security/privacy 연구를 편익, 공격, 방어, 거버넌스의 균형 문제로 보게 한다.
3. W07의 LLM 보안 위협모형을 W14 운영 감사와 연결할 수 있는 governance 관점을 제공한다.
4. 기말논문에서 “LLM을 활용하되, 안전한 범위와 감사 증거를 남긴다”는 원칙의 근거가 된다.

---

## 10. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 관련 보조 문헌 상태 | 강의계획서 지정 문헌과 제목·저자·출판지가 다르다. | paper_list의 관련 문헌 메모 유지 |
| 기술 변화 속도 | LLM 보안·프라이버시 이슈는 빠르게 변한다. | 평가일, 모델 버전, 문헌 기준일 명시 |
| Dual-use 평가 어려움 | 유용한 보안 자동화와 악용 가능성의 경계가 모호하다. | 사용 범위와 제외 범위를 명시 |
| 실제 로그 사용 위험 | 보안 로그에는 민감정보가 포함될 수 있다. | synthetic 또는 공개 데이터만 사용 |
| LLM 평가 편향 | LLM-as-judge와 사람 평가 모두 편향 가능성이 있다. | human review rubric을 기록 |

---

## 11. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | LLM은 보안 자동화 도구이자 공격 대상이라는 양면성 제시 |
| 2장 관련연구 | LLM security/privacy dual-use taxonomy 정리 |
| 3장 위협모형 | 보안 로그, 프롬프트, 도구 권한, 출력, 감사 로그 보호 자산 정의 |
| 4장 연구방법 | security utility, hallucination, leakage, ASR, defense coverage 평가 설계 |
| 5장 분석 | toy security-assist scenario와 한계 제시 |
| 6장 보안적 함의 | human review, governance, audit log, 책임소재 필요성 논의 |

---

## 12. 기말논문 연결 3문장

1. 이 주차에서 기말논문에 반영할 개념: LLM은 보안 업무를 돕는 도구이면서 동시에 보안 공격·프라이버시 누출·악용의 대상이 되므로 dual-use 관점의 통제가 필요하다.
2. 이 주차에서 기말논문에 반영할 표·그림·실험: Good/Bad/Ugly taxonomy, Risk_LLM 수식, DefenseCoverage 수식, security utility와 hallucination/leakage 비교표를 반영한다.
3. 이 주차가 RAG 문서 오염/LLM 보안 감사 프레임워크와 연결되는 지점: W08에서는 RAG 문서와 prompt injection으로, W14/W15에서는 tool 권한·로그·human review evidence chain으로 확장한다.

---

## 13. 최종 판단

P03은 W07의 관련 보조 문헌이다. 지정 문헌과 차이가 있으므로 공식 지정 논문처럼 취급하지 않고, LLM 보안·프라이버시의 양면성과 governance 논리를 보강하는 문헌으로 사용한다.

---

## 14. 변환 호환성 메모

```bash
pandoc P03_summary.md -o P03_summary.docx
pandoc P03_summary.md -o P03_summary.pdf --pdf-engine=xelatex
```
