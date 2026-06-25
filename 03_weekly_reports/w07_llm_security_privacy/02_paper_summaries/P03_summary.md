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
| 로컬 PDF | `01_papers/pdf/03_Yao_et_al_2024_LLM_Security_Privacy_Good_Bad_Ugly.pdf` |
| 검증 상태 | W07 `paper_list.md` 기준 공식 DOI 확인. 다만 강의계획서 지정 AI Open 논문과 제목·저자·출판지가 달라 `관련 논문 / 확인`으로 처리한다. |
| PDF 확인 메모 | repo의 PDF 폴더에 P03 관련 PDF blob이 존재함을 확인했다. 요약은 로컬 PDF 경로와 W07 `paper_list.md`, `download_source.md`의 공식 DOI/arXiv 메타데이터 기준으로 보완했다. |
| 수식 호환성 | GitHub 수식 렌더링 오류 방지를 위해 `\operatorname`을 사용하지 않고, `\mathrm{...}` 또는 짧은 변수명 중심으로 작성했다. |
| 핵심 근거 사용 가능 여부 | 관련 보조 문헌으로 사용. LLM security/privacy의 dual-use risk, LLM for security, security of LLM, LLM-enabled misuse, governance 정리에 유용하다. |

---

## 1. 한 문장 요약

이 논문은 LLM을 **보안을 강화하는 도구**, **공격자가 악용할 수 있는 도구**, **그 자체가 공격받는 시스템**이라는 세 관점으로 나누어 보안·프라이버시 문제를 정리하며, W07에서 LLM 활용을 단순 도입 효과가 아니라 **편익·악용 가능성·자체 취약성·거버넌스 통제·감사 증거**를 함께 평가해야 하는 dual-use 보안 프레임으로 해석하게 하는 관련 핵심 문헌이다.

---

## 2. 핵심 연구문제

> LLM은 보안 로그 요약, 취약점 설명, 정책 문서 정리처럼 방어 업무를 돕는 도구가 될 수 있다. 동시에 jailbreak, prompt injection, privacy leakage, hallucination, phishing-style abuse, unsafe automation에 악용될 수 있으며, LLM 자체도 poisoning, backdoor, data extraction, model stealing, prompt leakage의 보호 대상이 된다.

| 번호 | 연구질문 |
|---|---|
| RQ1 | LLM은 취약점 탐지, 보안 로그 분석, 위협 인텔리전스 요약, 보안 교육에 어떻게 활용될 수 있는가? |
| RQ2 | LLM은 jailbreak, prompt injection, privacy leakage, hallucination, malicious automation에 어떻게 악용될 수 있는가? |
| RQ3 | LLM 자체는 poisoning, backdoor, data extraction, model stealing, prompt leakage에 어떤 취약성을 갖는가? |
| RQ4 | LLM 보안 연구는 “도구로서의 LLM”과 “보호 대상으로서의 LLM”을 어떻게 동시에 다뤄야 하는가? |
| RQ5 | 기말논문에서 LLM의 dual-use 위험을 어떻게 안전한 toy evaluation, human review, audit evidence로 제한해 제시할 수 있는가? |

---

## 3. Good / Bad / Ugly 프레임

| 구분 | 의미 | W07 적용 |
|---|---|---|
| Good | LLM이 보안 업무를 보조하는 긍정적 사용 | 로그 요약, 정책 문서 정리, 취약점 설명, 보안 교육 |
| Bad | LLM이 공격·우회·허위정보 생성에 악용될 가능성 | jailbreak, prompt injection, phishing-style abuse, hallucinated security advice |
| Ugly | 책임소재, 악용 자동화, 프라이버시 침해, 사회적 파급 | dual-use governance, human review, audit log, safe logging |

---

## 4. 논문의 핵심 기여

| 기여 | 설명 | W07 연결 |
|---|---|---|
| Dual-use taxonomy | LLM을 보안 도구, 공격 도구, 보호 대상이라는 세 관점으로 체계화 | W07 P03 핵심 |
| LLM for Security | 보안 로그 요약, 취약점 분석, 위협 인텔리전스 보조 가능성 정리 | 방어 자동화 가능성 |
| Security of LLM | prompt injection, jailbreak, data leakage, poisoning, backdoor 등 LLM 자체 위험 정리 | LLM 위협모형 |
| LLM-enabled Misuse | 사회공학, 허위정보, 악성 자동화 등 악용 가능성 정리 | dual-use risk 분석 |
| Governance 강조 | human review, access control, logging, red teaming, policy guardrail 필요성 제시 | W14/W15 evidence chain 연결 |

---

## 5. 목차별 핵심 개괄

| 목차 | 핵심 내용 | 비전공자용 이해 |
|---|---|---|
| 1. Introduction | LLM은 보안에 유용하지만 동시에 새로운 공격면과 악용 위험을 만든다. | AI가 방어 도구이면서 공격 도구가 될 수 있다. |
| 2. Background | LLM의 학습, prompting, instruction following, deployment 구조를 설명한다. | LLM이 어떻게 만들어지고 쓰이는지 이해한다. |
| 3. The Good | LLM을 활용한 취약점 탐지, 로그 분석, 보안 문서 요약, 교육, 자동화 보조를 정리한다. | 보안 업무를 빠르게 돕는 긍정적 활용이다. |
| 4. The Bad | LLM이 jailbreak, prompt injection, unsafe generation, hallucination, privacy leakage에 취약함을 다룬다. | AI가 잘못된 답이나 위험한 답을 만들 수 있다. |
| 5. The Ugly | dual-use, 악용 자동화, 책임소재 불명확성, 사회적 영향, 규제·윤리 문제를 논의한다. | 기술 문제가 사회·윤리·운영 문제로 확대된다. |
| 6. Defense and Governance | guardrail, monitoring, red teaming, human review, audit log, access control을 정리한다. | 사람 검토와 기록이 필요하다. |
| 7. Future Directions | trustworthy LLM security, privacy-preserving deployment, safe tool use, auditable AI가 과제로 남는다. | 안전하고 검증 가능한 AI 보안 체계가 필요하다. |

---

## 6. 핵심 이론 및 수식

> 아래 수식은 논문이 제시하는 dual-use 관점을 W07 보고서의 평가 지표로 변환한 표현이다. 악용 절차가 아니라 위험 평가 프레임이다. GitHub 호환성을 위해 `\operatorname`은 사용하지 않는다.

### 6.1 LLM 보안 위험 점수

LLM 시스템의 보안 위험을 공격 성공, 정보 누출, 악용 가능성, 방어 적용 범위로 요약한다.

$$
Risk_{LLM}=w_1ASR+w_2LeakageRate+w_3MisuseRisk-w_4DefenseCoverage
$$

| 기호 | 의미 |
|---|---|
| $ASR$ | 공격 또는 우회 프롬프트 성공률 |
| $LeakageRate$ | 민감정보 노출률 |
| $MisuseRisk$ | 악용 가능성 또는 dual-use 위험 수준 |
| $DefenseCoverage$ | 방어·감사·정책 통제가 적용된 범위 |
| $w_i$ | 각 위험 요인의 가중치 |

### 보안적 의미

LLM이 유용하다고 해서 안전한 것은 아니다. 보안 업무 자동화에 쓰는 경우에도 공격 성공률, 정보 누출, 악용 가능성, 방어 적용 범위를 함께 평가해야 한다.

---

### 6.2 방어 적용 범위

필요한 통제 중 실제 적용된 통제의 비율이다.

$$
DefenseCoverage=\frac{|Controls_{applied}|}{|Controls_{required}|}
$$

### 보안적 의미

LLM 사용 정책이 문서로만 존재하고 실제 로그·승인·검토가 없으면 방어가 적용되었다고 보기 어렵다. W14/W15의 evidence chain과 직접 연결된다.

---

### 6.3 안전한 보안 보조 성능

LLM이 보안 업무를 돕는 경우 성능과 위험을 함께 평가한다.

$$
SecureAssistScore=Utility_{security}-\lambda_1HallucinationRate-\lambda_2UnsafeSuggestionRate-\lambda_3LeakageRate
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

### 6.4 악용 위험 점수

LLM이 악용될 가능성을 자동화 수준, 도메인 위험, 접근성, 감시 수준으로 단순화할 수 있다.

$$
MisuseRisk=AutomationLevel+DomainRisk+AccessEase-MonitoringCoverage
$$

### 보안적 의미

동일한 모델이라도 공개 접근성, 자동화 수준, 도메인 민감도, 모니터링 유무에 따라 악용 위험이 달라진다.

---

### 6.5 감사 완전성

LLM 사용의 사후 검증 가능성을 측정한다.

$$
AuditCompleteness=\frac{|Events_{logged}|}{|Events_{required}|}
$$

| 필수 event 예 | 설명 |
|---|---|
| prompt | 사용자 입력과 시스템 지시 |
| output | 모델 응답 |
| policy decision | 허용·차단·검토 판단 |
| tool call | 외부 도구 호출 여부와 권한 |
| human review | 사람 검토와 승인 기록 |

---

### 6.6 Human Review Coverage

고위험 출력 중 사람이 검토한 비율이다.

$$
HumanReviewCoverage=\frac{N_{reviewed}}{N_{high\ risk}}
$$

### 보안적 의미

보안 자동화에서 최종 책임을 모델에 넘기면 위험하다. 고위험 판단은 사람 검토 비율을 별도로 보고해야 한다.

---

### 6.7 Dual-use Governance Score

LLM 활용의 거버넌스 수준을 방어, 감사, 사람 검토, 권한통제로 요약한다.

$$
GovernanceScore=DefenseCoverage+AuditCompleteness+HumanReviewCoverage+AccessControlScore
$$

### 보안적 의미

LLM 보안은 모델 자체 방어뿐 아니라 기록, 검토, 권한, 승인 체계가 함께 있어야 한다.

---

## 7. LLM 보안의 양면성 분석

| 관점 | 설명 | 평가 지표 |
|---|---|---|
| LLM for Security | 보안 로그 요약, 취약점 설명, 정책 검토 등 방어 업무 보조 | utility, hallucination, human review agreement |
| Security of LLM | LLM 자체의 prompt injection, jailbreak, leakage, poisoning 위험 | ASR, leakage rate, refusal quality |
| LLM-enabled Misuse | 사회공학, 허위정보, 악성 자동화 등 악용 위험 | misuse category, safety violation, monitoring coverage |
| Governance | 사용 범위, 승인, 로깅, 책임소재 관리 | defense coverage, audit completeness |

---

## 8. 보안 이슈 30% 관점 분석

| 보안 항목 | Dual-use LLM 관점 해석 | 대표 평가 지표 |
|---|---|---|
| 기밀성 | 보안 로그, 내부 정책, prompt/output에 민감정보가 포함될 수 있음 | LeakageRate, log leakage |
| 무결성 | hallucination과 prompt injection이 보안 판단을 왜곡할 수 있음 | ASR, hallucination rate |
| 가용성 | 자동화 오남용, 과차단, 과도한 검토 비용이 운영성을 저하시킬 수 있음 | latency, over-refusal, review load |
| 프라이버시 | 민감 로그와 prompt가 output/log/tool call로 재노출될 수 있음 | privacy leakage, retention audit |
| 안전성 | 부정확한 보안 조언, unsafe suggestion, dual-use misuse 가능성 | UnsafeSuggestionRate, MisuseRisk |
| 책임성 | 최종 판단자, human review, tool call, audit log가 연결되어야 함 | AuditCompleteness, HumanReviewCoverage |

---

## 9. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | 보안 로그, 취약점 리포트, 내부 정책, system prompt, user prompt, tool credential, 모델 출력, 감사 로그 |
| 공격자 목표 | 안전정책 우회, 민감정보 추출, 보안 자동화 오남용, 허위 보안 조언 생성, 도구 권한 오남용 |
| 공격자 능력 | prompt 조작, 반복 질의, 간접 지시 삽입, 민감 로그 제공 유도, 도구 권한 오용 유도 |
| 공격 경로 | security task prompt → LLM output → human/tool/action → audit log 또는 외부 노출 |
| 방어자 능력 | red teaming, guardrail, human review, access control, prompt/output logging, approval workflow, safe logging |
| 제외 범위 | 실제 시스템 공격, 악성코드 작성, 실제 개인정보·취약점 악용 절차 제공, 공격 자동화 지침 제공 |

---

## 10. 평가방법 및 지표

| 지표 | 의미 | W07/P03 활용 |
|---|---|---|
| SecurityUtility | LLM이 보안 업무를 얼마나 정확히 보조하는지 | 방어 도구로서의 성능 |
| HallucinationRate | 허위 보안 설명·근거 없는 권고 비율 | 보안 업무 위험 |
| UnsafeSuggestionRate | 위험하거나 부적절한 조치 제안 비율 | high-stakes 제한 |
| ASR | 정책 우회·공격 성공률 | 공격 대상으로서의 LLM 평가 |
| LeakageRate | 민감 로그·정보 노출률 | 프라이버시 평가 |
| MisuseRisk | 악용 가능성 또는 dual-use 위험 | 거버넌스 필요성 |
| DefenseCoverage | 필요한 통제 중 실제 적용된 통제 비율 | governance 평가 |
| AuditCompleteness | 입력·출력·도구 호출·검토 로그 보존 정도 | W14/W15 연결 |
| HumanReviewCoverage | 고위험 판단 중 사람 검토 비율 | 책임성 평가 |

---

## 11. 재현성 체크리스트

| 항목 | 기록해야 할 내용 |
|---|---|
| Bibliographic status | DOI, High-Confidence Computing 출판정보, arXiv 판본, 관련 문헌 상태 |
| Model | 모델명, 버전, endpoint, decoding config |
| Use case | 보안 로그 요약, 취약점 설명, 정책 점검 등 사용 범위 |
| Input data | synthetic log 또는 공개 예시만 사용. 실제 민감 로그 제외 |
| Defense controls | human review, refusal policy, tool 권한 제한, logging 여부 |
| Output validation | hallucination, unsafe suggestion, leakage 여부 |
| Tool governance | tool schema, permission, approval, tool call log |
| Responsibility | 최종 판단자는 사람이며, LLM 출력은 검토 대상임을 명시 |
| Evidence | prompt/output hash, review note, metric table, limitation statement |
| GitHub math | `\operatorname` 사용 금지, 짧은 변수명과 `\mathrm{...}` 형태 사용 |

---

## 12. 논문의 고유 기여

1. LLM을 보안 도구와 보안 대상이라는 양면성으로 동시에 정리한다.
2. LLM security/privacy 연구를 편익, 공격, 방어, 거버넌스의 균형 문제로 보게 한다.
3. W07의 LLM 보안 위협모형을 W14 운영 감사와 연결할 수 있는 governance 관점을 제공한다.
4. 기말논문에서 “LLM을 활용하되, 안전한 범위와 감사 증거를 남긴다”는 원칙의 근거가 된다.
5. W08 RAG, W14 MLOps, W15 재현성·AI 활용 고지와 연결되는 dual-use evidence framework를 제공한다.

---

## 13. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 관련 보조 문헌 상태 | 강의계획서 지정 AI Open 문헌과 제목·저자·출판지가 다르다. | `paper_list.md`의 관련 문헌 메모 유지 |
| 기술 변화 속도 | LLM 보안·프라이버시 이슈는 빠르게 변한다. | 평가일, 모델 버전, 문헌 기준일 명시 |
| Dual-use 평가 어려움 | 유용한 보안 자동화와 악용 가능성의 경계가 모호하다. | 사용 범위와 제외 범위 명시 |
| 실제 로그 사용 위험 | 보안 로그에는 민감정보가 포함될 수 있다. | synthetic 또는 공개 데이터만 사용 |
| LLM 평가 편향 | LLM-as-a-judge와 사람 평가 모두 편향 가능성이 있다. | human review rubric 기록 |
| 책임소재 문제 | AI 보조 결과를 사람이 그대로 수용하면 책임 경계가 모호해진다. | final decision owner와 review log 기록 |

---

## 14. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | LLM은 보안 자동화 도구이자 공격 대상이라는 양면성 제시 |
| 2장 관련연구 | LLM security/privacy dual-use taxonomy 정리 |
| 3장 위협모형 | 보안 로그, 내부 정책, system prompt, tool credential, audit log 보호 자산 정의 |
| 4장 연구방법 | Risk_LLM, DefenseCoverage, SecureAssistScore, MisuseRisk, AuditCompleteness, GovernanceScore 지표 설계 |
| 5장 분석 | Good/Bad/Ugly matrix와 dual-use governance table 제시 |
| 6장 보안적 함의 | 자동화 편익, 악용 가능성, human review, auditability, 책임소재 해석 |
| 부록 | synthetic security task prompt, review rubric, output validation table, limitation statement 수록 |

---

## 15. 기말논문 연결 3문장

1. W07에서 기말논문에 반영할 개념: LLM은 보안 업무를 보조할 수 있지만, 동시에 공격 자동화와 프라이버시 침해를 만들 수 있는 dual-use 기술이다.
2. W07에서 기말논문에 반영할 표·그림·실험: Good/Bad/Ugly matrix, Risk_LLM, DefenseCoverage, SecureAssistScore, MisuseRisk, AuditCompleteness, GovernanceScore 수식표를 반영한다.
3. W07이 W14/W15와 연결되는 지점: LLM 활용 결과는 human review, access control, safe logging, tool permission, AI disclosure와 함께 기록되어야 최종논문의 실무성과 책임성이 확보된다.

---

## 16. 최종 판단

P03은 W07의 관련 보조 문헌이지만, LLM 보안의 dual-use 구조를 설명하는 데 가치가 높다. P02가 LLM 보안·프라이버시 위협모형을 직접 제공한다면, P03은 LLM을 보안 도구로 쓸 때의 편익과 위험, 악용 가능성, 거버넌스 요구를 균형 있게 정리한다. 따라서 기말논문에서는 P03을 **LLM dual-use risk, LLM for security, security of LLM, misuse governance, human review, audit evidence의 근거 문헌**으로 사용하는 것이 적절하다.

---

## 17. GitHub 수식 호환성 메모

이 파일에서는 GitHub 수식 렌더링 오류 방지를 위해 `\operatorname`을 사용하지 않는다.

| 피해야 할 표현 | 권장 표현 |
|---|---|
| `\operatorname{softmax}` | `\mathrm{softmax}` |
| `\operatorname{argmax}` | `\mathrm{argmax}` 또는 `\arg\max` |
| 긴 영문 subscript | 짧은 변수명 사용 후 표에서 의미 설명 |

```bash
pandoc P03_summary.md -o P03_summary.docx
pandoc P03_summary.md -o P03_summary.pdf --pdf-engine=xelatex
```
