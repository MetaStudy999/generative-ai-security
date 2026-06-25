# P05 Summary

## Privacy Preserving Prompt Engineering: A Survey — Kennedy Edemacu, Xintao Wu, ACM Computing Surveys, 2025

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W04 Transformer 변형 & NLP 대적공격·프라이버시 |
| 논문명 | Privacy Preserving Prompt Engineering: A Survey |
| 저자 | Kennedy Edemacu, Xintao Wu |
| 공식 출판 정보 | ACM Computing Surveys, Vol. 57, No. 10, pp. 1–36, 2025 |
| DOI | https://doi.org/10.1145/3729219 |
| 보조 URL | https://arxiv.org/abs/2404.06001 |
| 논문 유형 | Survey / Privacy-Preserving Prompt Engineering Review |
| 로컬 PDF | `01_papers/pdf/05_Edemacu_Wu_2025_Privacy_Preserving_Prompt_Engineering.pdf` |
| 검증 상태 | W04 `paper_list.md` 기준 ACM CSUR 2025 출판 DOI 확인. `download_source.md` 기준 로컬 PDF 파일명과 DOI/arXiv 출처가 대응됨 |
| PDF 확인 메모 | repo의 PDF 폴더에 P05 관련 PDF blob이 존재함을 확인했다. 요약은 로컬 PDF 경로와 W04 `paper_list.md`, `download_source.md`의 공식 DOI/arXiv 메타데이터 기준으로 보완했다. |
| 수식 호환성 | GitHub 수식 렌더링 오류 방지를 위해 `\operatorname`을 사용하지 않고 `\mathrm{...}` 형태로 작성했다. |
| 핵심 근거 사용 가능 여부 | 가능. W04에서 prompt privacy, ICL leakage, privacy-preserving prompt engineering, masking, rewriting, policy wrapper, output auditing, tool/log leakage, leakage-utility-over-refusal trade-off의 핵심 문헌으로 사용 |

---

## 1. 한 문장 요약

이 논문은 LLM prompting과 in-context learning에서 발생하는 개인정보·민감정보·영업비밀 노출 위험을 **prompt privacy, ICL example leakage, RAG context leakage, masking, rewriting, anonymization, policy control, privacy wrapper, output auditing, tool-call argument leakage, prompt/output logging risk, privacy-utility trade-off** 관점에서 정리하며, W04에서는 프롬프트 보안 평가를 **leakage rate, masking precision/recall, utility, over-refusal, policy compliance, latency, auditability**로 분리해 측정해야 함을 보여주는 핵심 survey 문헌이다.

---

## 2. 핵심 연구문제

> LLM은 사용자의 자연어 prompt, few-shot example, RAG context, output, log, tool-call argument를 모두 처리한다. 이 과정에서 개인정보, 내부 문서, 업무 규칙, 영업비밀, 민감 속성이 입력이나 출력으로 노출될 수 있다. Privacy-preserving prompt engineering은 단순 마스킹이 아니라, 민감정보 탐지와 정상 utility 유지, 과차단 최소화, 감사 로그 보존을 함께 설계해야 한다.

| 번호 | 연구질문 |
|---|---|
| RQ1 | Prompt privacy 위험은 input prompt, ICL example, retrieved context, model output, tool-call argument, log 중 어디에서 발생하는가? |
| RQ2 | Few-shot prompt와 in-context learning example은 어떤 방식으로 개인정보와 내부 지식을 노출할 수 있는가? |
| RQ3 | Masking, anonymization, rewriting, policy control, privacy wrapper, output auditing은 각각 어떤 장단점과 실패 조건을 갖는가? |
| RQ4 | Leakage rate를 낮추는 방어가 utility 저하, over-refusal, latency 증가를 만들 때 이를 어떻게 함께 평가해야 하는가? |
| RQ5 | W04 toy prompt masking 실험을 실제 LLM privacy guarantee로 과장하지 않으려면 어떤 재현성·한계 메모가 필요한가? |

---

## 3. 논문의 핵심 기여

| 기여 | 설명 | W04 연결 |
|---|---|---|
| Prompt privacy taxonomy | prompt, ICL, context, output, log, tool-call 단계별 privacy risk 정리 | W04 P05 핵심 |
| Privacy-preserving prompt engineering 정리 | masking, rewriting, anonymization, policy wrapper, auditing 접근 비교 | 연구방법 설계 |
| Leakage-utility trade-off 강조 | leakage 감소만이 아니라 task utility와 over-refusal을 함께 봐야 함 | 평가 지표 설계 |
| 운영 관점 포함 | 실제 API, SaaS LLM, agent tool call, logging policy의 위험을 고려 | W14 MLOps 연결 |
| 안전한 실험 원칙 제공 | 실제 개인정보 대신 synthetic privacy-risk prompt와 placeholder 중심 평가 필요 | 윤리·재현성 확보 |

---

## 4. 목차별 핵심 개괄

| 목차 | 핵심 내용 | 비전공자용 이해 |
|---|---|---|
| 1. Introduction | LLM prompt에는 사용자의 민감정보와 업무 데이터가 포함될 수 있어 privacy-preserving prompting이 필요하다. | AI에게 질문할 때 개인정보를 같이 보내면 위험할 수 있다. |
| 2. Prompting and ICL Background | prompt, instruction, few-shot example, context window, in-context learning 구조를 설명한다. | 예시를 넣어 AI가 답하게 만드는 과정에서도 정보가 노출될 수 있다. |
| 3. Threats to Prompt Privacy | prompt leakage, ICL leakage, context leakage, output leakage, log leakage, tool leakage를 분류한다. | 입력·출력·로그·도구 호출 모두 유출 경로다. |
| 4. Privacy-Preserving Methods | masking, anonymization, rewriting, encryption-style wrapper, policy-based control, output filtering을 정리한다. | 민감값을 가리거나 바꾸거나 출력 전에 검사한다. |
| 5. Evaluation | leakage rate, masking precision/recall, utility, over-refusal, latency, policy compliance를 평가한다. | 누출을 줄이면서도 일을 제대로 수행하는지 본다. |
| 6. Applications | 기업 문서, 의료, 법률, 교육, RAG, agent workflow에서 prompt privacy가 중요하다. | 민감한 업무 분야일수록 prompt 관리가 필요하다. |
| 7. Challenges | 간접 식별자, 문맥 기반 유출, false positive/negative, utility loss, prompt injection 우회가 과제로 남는다. | 단순 정규식으로는 모든 개인정보를 잡기 어렵다. |
| 8. Future Directions | privacy-aware LLM systems, auditable prompt pipelines, policy-aligned wrappers, safe logging이 필요하다. | AI 사용 기록과 보호 조치를 함께 남겨야 한다. |

---

## 5. 핵심 이론 및 수식

> 수식은 GitHub Markdown/KaTeX 호환성을 우선한다. `\operatorname` 매크로는 사용하지 않고 `\mathrm{...}` 형태로 작성한다.

### 5.1 Privacy Leakage Rate

프라이버시 위험 prompt 중 민감정보가 출력된 비율을 leakage rate로 표현할 수 있다.

$$
LeakageRate=\frac{N_{sensitive\ output}}{N_{privacy\ risk\ prompts}}
$$

| 기호 | 의미 |
|---|---|
| $N_{privacy\ risk\ prompts}$ | privacy-risk 평가 입력 수 |
| $N_{sensitive\ output}$ | 민감정보 노출 판정 수 |

### 보안적 의미

Leakage rate가 낮아도 utility가 크게 손상되거나 정상 요청을 과차단하면 방어가 실용적이지 않다. 따라서 leakage와 utility를 함께 평가해야 한다.

---

### 5.2 Masking Function

프롬프트 민감정보는 placeholder로 치환할 수 있다.

$$
x^{masked}=M(x;\mathcal{P})
$$

| 기호 | 의미 |
|---|---|
| $x$ | 원본 프롬프트 |
| $M$ | 민감정보 마스킹 함수 |
| $\mathcal{P}$ | 개인정보 패턴 또는 탐지 정책 |
| $x^{masked}$ | 마스킹된 프롬프트 |

### 보안적 의미

Masking은 직접적인 민감값 노출을 줄일 수 있지만, 문맥 정보가 사라져 모델 utility가 낮아질 수 있다. 또한 regex 기반 masking은 우회 표현, 간접 식별자, 문맥 기반 개인정보를 놓칠 수 있다.

---

### 5.3 Masking Precision and Recall

민감정보 탐지·마스킹의 정확도를 precision과 recall로 측정한다.

$$
Precision_{mask}=\frac{TP_{mask}}{TP_{mask}+FP_{mask}}
$$

$$
Recall_{mask}=\frac{TP_{mask}}{TP_{mask}+FN_{mask}}
$$

### 보안적 의미

Recall이 낮으면 민감정보를 놓치고, precision이 낮으면 과도한 마스킹으로 utility가 떨어진다.

---

### 5.4 Privacy-Utility Trade-off

프라이버시 보호는 utility와 trade-off를 가질 수 있다.

$$
PrivacyUtilityScore=Utility-\lambda LeakageRate-\mu OverRefusal
$$

| 기호 | 의미 |
|---|---|
| $Utility$ | 정상 task 품질 |
| $LeakageRate$ | 민감정보 노출률 |
| $OverRefusal$ | 정상 요청을 과도하게 거절한 비율 |
| $\lambda,\mu$ | 위험 항목 가중치 |

### 보안적 의미

무조건 거절하거나 과도하게 마스킹하면 leakage는 줄어도 서비스 가치가 사라질 수 있다. 실무형 prompt privacy는 “누출 감소 + 정상 utility 유지 + 과차단 최소화”를 함께 만족해야 한다.

---

### 5.5 Over-refusal Rate

정상 요청이 방어 정책에 의해 불필요하게 차단된 비율이다.

$$
OverRefusal=\frac{N_{benign\ refused}}{N_{benign\ requests}}
$$

### 보안적 의미

Over-refusal이 높으면 사용자는 우회 표현을 찾거나 보안 wrapper를 꺼버릴 가능성이 커진다.

---

### 5.6 Policy Compliance

프롬프트 처리 과정이 사전 정의된 privacy policy를 준수한 비율이다.

$$
PolicyCompliance=\frac{N_{policy\ compliant}}{N_{total\ cases}}
$$

### 보안적 의미

개별 leakage 여부뿐 아니라 탐지, 마스킹, 출력 차단, 로그 저장 정책의 전체 준수 여부를 봐야 한다.

---

### 5.7 Prompt Privacy Risk

프롬프트 기반 LLM 시스템의 privacy risk를 입력, context, output, log, tool 위험으로 분해한다.

$$
PromptPrivacyRisk=InputLeakage+ContextLeakage+OutputLeakage+LogLeakage+ToolLeakage-MaskingCoverage
$$

### 보안적 의미

Prompt privacy는 입력 하나만 보호하는 문제가 아니다. RAG context, output, log, external tool argument까지 전체 경로를 관리해야 한다.

---

### 5.8 Audit Completeness

탐지·마스킹·출력 차단·검토 로그가 얼마나 완전한지 측정한다.

$$
AuditCompleteness=\frac{|Events_{logged}|}{|Events_{required}|}
$$

### 보안적 의미

사후 검증을 위해 어떤 민감정보가 탐지되고, 어떤 항목이 마스킹되었고, 어떤 출력이 차단되었는지 로그가 필요하다. 단, 로그 자체가 민감정보를 다시 저장하지 않도록 placeholder와 hash 중심으로 설계해야 한다.

---

## 6. AI 원리 70% 관점 분석

| 원리 항목 | 설명 | W04/P05에서의 의미 |
|---|---|---|
| Prompting | 사용자가 자연어로 작업 지시와 데이터를 함께 제공 | privacy leakage 출발점 |
| In-context Learning | few-shot 예시가 context에 포함 | ICL example leakage 위험 |
| Context Window | 긴 prompt나 RAG 문서가 입력으로 결합 | context leakage 증가 |
| Output Generation | 모델이 context에 근거해 답변 생성 | 민감정보 재출력 가능 |
| Masking | 민감값을 placeholder로 치환 | 기본 방어 방법 |
| Rewriting | 민감정보를 줄이도록 prompt 재작성 | utility와 privacy 균형 |
| Policy Wrapper | 입력·출력·로그에 정책 적용 | 운영 통제 |
| Tool Use | 외부 API 호출 인자 생성 | tool-call leakage 위험 |

---

## 7. 보안 이슈 30% 관점 분석

| 보안 항목 | Prompt Privacy 관점 해석 | 대표 평가 지표 |
|---|---|---|
| 기밀성 | prompt, ICL example, RAG 문서, output, log의 민감정보 보호가 핵심 | LeakageRate, redaction miss |
| 프라이버시 | 개인정보, 민감 속성, 영업비밀, 내부 문서가 prompt에 포함될 수 있음 | PII detection, policy compliance |
| 무결성 | privacy policy가 prompt injection이나 우회 표현으로 무력화될 수 있음 | policy bypass rate |
| 가용성 | 과도한 마스킹과 거절은 정상 업무 처리를 방해 | OverRefusal, utility drop |
| 책임성 | 어떤 민감정보를 탐지·마스킹·출력 차단했는지 감사 로그 필요 | AuditCompleteness |
| 운영 리스크 | 실제 API, SaaS LLM, agent tool 호출, 로그 저장 정책이 위험을 증폭 | ToolLeakage, LogLeakage |

---

## 8. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 대상 | 사용자 프롬프트, ICL 예시, RAG context, output, tool call argument, log, prompt template, privacy policy |
| 공격자 목표 | 민감정보 유출, policy bypass, masking 우회, log leakage 유도, tool-call argument leakage 유도 |
| 공격자 능력 | privacy-risk prompt 작성, 간접 식별자 포함, 우회 표현 사용, 반복 질의, prompt injection, context stuffing |
| 공격 경로 | prompt/context → privacy wrapper/model input → output/tool/log → external exposure |
| 방어자 능력 | synthetic test, masking, rewriting, PII scan, output filtering, policy wrapper, safe logging, human review |
| 제외 범위 | 실제 개인정보 사용, 실제 API 대상 유출 실험, 무단 로그 접근, 개인정보 탈취 절차 제공 |

---

## 9. 평가방법 및 지표

| 평가축 | 지표 | 의미 | W04/P05 활용 |
|---|---|---|---|
| 누출 | LeakageRate | 민감정보 출력 비율 | privacy 핵심 지표 |
| 탐지 | Recall_mask, Precision_mask | 민감정보 탐지·마스킹 품질 | 방어 평가 |
| 사용성 | Utility, utility drop | 정상 작업 품질 | 실무성 평가 |
| 과차단 | OverRefusal | 정상 요청 거절률 | 부작용 평가 |
| 정책 준수 | PolicyCompliance | 개인정보 정책 준수율 | 운영 통제 |
| 운영성 | Latency | 마스킹·검사 지연 | 실시간 적용성 |
| 감사성 | AuditCompleteness | 탐지·마스킹·출력 판단 로그 | 사후 검증 |
| 로그 안전성 | LogLeakage, raw value retention | 로그 재유출 위험 | safe logging |

---

## 10. 재현성 체크리스트

| 항목 | 기록해야 할 내용 |
|---|---|
| Bibliographic status | DOI, ACM CSUR 출판정보, arXiv 판본, 로컬 PDF 상태 |
| Data | synthetic privacy-risk prompt만 사용. 실제 개인정보 제외 |
| Sensitive types | 이름, 전화번호, 이메일, 주민번호형 패턴, 내부 문서명 등 toy pattern 정의 |
| Defense | masking, rewriting, refusal, policy wrapper, output filtering 조건 기록 |
| Policy | 개인정보 패턴, 마스킹 규칙, 출력 차단 기준, 로그 저장 기준 |
| Evaluation | LeakageRate, Precision_mask, Recall_mask, Utility, OverRefusal, PolicyCompliance, Latency |
| Logs | 원본 민감값 저장 금지, placeholder/hash 중심 기록, raw prompt 보관 여부 명시 |
| Environment | model/API version, prompt template, decoding config, script commit |
| Human review | false positive/false negative 예시와 한계 검토 |
| GitHub math | `\operatorname` 사용 금지, `\mathrm{...}` 형태 사용 |

---

## 11. 논문의 고유 기여

1. Prompt engineering과 ICL 환경에서의 privacy risk를 체계화했다.
2. Prompt masking, rewriting, policy control, privacy-preserving prompting을 비교할 수 있는 기준을 제공한다.
3. Leakage만이 아니라 utility, over-refusal, latency, auditability를 함께 평가해야 함을 보여준다.
4. W04와 W08의 prompt/RAG 보안 주제를 privacy 관점으로 연결하는 핵심 문헌이다.
5. W14 MLOps와 W15 reproducibility 관점에서 safe logging, AI disclosure, evidence chain의 필요성을 뒷받침한다.

---

## 12. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 최신 분야 | prompt privacy는 빠르게 변하므로 후속 문헌 보강 필요 | W07/W08 최신 LLM 보안 문헌과 연결 |
| 실제 데이터 사용 제한 | 개인정보를 실제로 넣고 실험하면 윤리·법적 위험이 있다 | synthetic prompt만 사용 |
| 탐지 한계 | regex/masking은 간접 식별자와 문맥 정보 누출을 놓칠 수 있다 | false negative와 한계 명시 |
| Utility 측정 어려움 | 마스킹 후 작업 품질 저하를 정량화하기 어렵다 | simple task utility와 human review 병기 |
| 로그 재유출 위험 | 감사 로그가 원본 민감값을 저장하면 2차 유출이 된다 | placeholder/hash logging 적용 |
| 방어 우회 | prompt injection과 우회 표현이 privacy wrapper를 약화시킬 수 있다 | policy bypass test 추가 |

---

## 13. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | 생성형 AI prompt에 민감정보가 포함되는 위험 제시 |
| 2장 관련연구 | privacy-preserving prompt engineering survey 정리 |
| 3장 위협모형 | prompt/context/output/log/tool call leakage 경로 정의 |
| 4장 연구방법 | LeakageRate, Precision_mask, Recall_mask, PrivacyUtilityScore, OverRefusal, PolicyCompliance, AuditCompleteness 지표 설계 |
| 5장 분석 | synthetic privacy-risk prompt 실험 결과와 한계 제시 |
| 6장 보안적 함의 | 기밀성, 프라이버시, 책임성, 감사 가능성, safe logging 해석 |
| 부록 | synthetic prompt set, masking rule, placeholder policy, output audit log 수록 |

---

## 14. 기말논문 연결 3문장

1. W04에서 기말논문에 반영할 개념: 프롬프트 보안은 입력 보안만이 아니라 ICL example, RAG context, output, tool-call argument, log까지 포함하는 privacy pipeline 문제다.
2. W04에서 기말논문에 반영할 표·그림·실험: LeakageRate, Precision_mask, Recall_mask, PrivacyUtilityScore, OverRefusal, PolicyCompliance, PromptPrivacyRisk, AuditCompleteness 수식표와 synthetic privacy-risk prompt 평가표를 반영한다.
3. W04가 W08/W14/W15와 연결되는 지점: RAG 문서 오염과 agent tool use에서도 prompt privacy 위험이 반복되므로, W15 최종 제출에는 prompt template, masking rule, output audit, safe logging, AI 활용 고지를 evidence chain으로 남겨야 한다.

---

## 15. 최종 판단

P05는 W04의 prompt privacy 핵심 문헌이다. 이 논문은 LLM/RAG/agent 환경에서 민감정보가 prompt, ICL example, context, output, tool argument, log를 통해 어떻게 유출될 수 있는지 설명하고, 이를 leakage-utility-over-refusal-auditability 관점에서 평가하게 해준다. 따라서 기말논문에서는 P05를 **privacy-preserving prompt engineering, synthetic privacy-risk prompt 평가, masking precision/recall, safe logging, prompt privacy threat model의 중심 근거 문헌**으로 사용하는 것이 적절하다.

---

## 16. GitHub 수식 호환성 메모

이 파일에서는 GitHub 수식 렌더링 오류 방지를 위해 `\operatorname`을 사용하지 않는다.

| 피해야 할 표현 | 권장 표현 |
|---|---|
| `\operatorname{mask}` | `\mathrm{mask}` 또는 함수명 일반 문자 |
| `\operatorname{argmax}` | `\mathrm{argmax}` 또는 `\arg\max` |
| `\operatorname{softmax}` | `\mathrm{softmax}` |

```bash
pandoc P05_summary.md -o P05_summary.docx
pandoc P05_summary.md -o P05_summary.pdf --pdf-engine=xelatex
```
