# P04 Summary

## Prompt Injection Attacks on Large Language Models: A Survey of Attack Methods, Root Causes, and Defense Strategies — Tongcheng Geng et al., Computers, Materials & Continua, 2026

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W08 RAG·프롬프팅 프레임워크 & 프롬프트 인젝션 |
| 논문명 | Prompt Injection Attacks on Large Language Models: A Survey of Attack Methods, Root Causes, and Defense Strategies |
| 저자 | Tongcheng Geng, Zhiyuan Xu, Yubin Qu, W. Eric Wong |
| 공식 출판 정보 | Computers, Materials & Continua, Vol. 87, No. 1, pp. 1–10, 2026 |
| DOI | https://doi.org/10.32604/cmc.2025.074081 |
| 로컬 PDF | `01_papers/pdf/04_Geng_et_al_2025_Prompt_Injection_Attacks_Survey.pdf` |
| 검증 상태 | W08 `paper_list.md` 기준 DOI/PDF 확인. 강의계획서의 `Tianlei Geng` 표기와 공식 DOI 기준 `Tongcheng Geng` 표기 차이 메모 유지 |
| PDF 확인 메모 | repo의 PDF 폴더에 해당 PDF blob이 존재함을 확인했다. 요약은 로컬 PDF 경로와 W08 `paper_list.md`의 공식 DOI 메타데이터 기준으로 보완했다. |
| 핵심 근거 사용 가능 여부 | 가능. W08에서 prompt injection의 공격유형, 근본원인, 방어전략, RAG/agent 보안 평가를 직접 다루는 중심 문헌으로 사용 |

---

## 1. 한 문장 요약

이 논문은 LLM prompt injection을 **direct injection, indirect injection, instruction override, goal hijacking, system prompt leakage, retrieved-context contamination, tool misuse, data exfiltration, root cause, defense strategy** 관점에서 정리하며, W08에서 RAG·프롬프팅·에이전트형 LLM 시스템의 신뢰 경계 붕괴를 분석하는 핵심 보안 문헌이다.

---

## 2. 핵심 연구문제

> LLM은 자연어 지시를 실행하는 구조 때문에 system instruction, user instruction, retrieved document, tool output을 완전히 분리하지 못할 수 있으며, 이 신뢰 경계 실패가 prompt injection으로 어떻게 나타나고 어떤 방어전략으로 완화할 수 있는가?

| 번호 | 연구질문 |
|---|---|
| RQ1 | Prompt injection은 direct injection과 indirect injection으로 어떻게 구분되는가? |
| RQ2 | LLM이 system/developer/user/retrieved/tool instruction을 명확히 분리하지 못하는 근본 원인은 무엇인가? |
| RQ3 | RAG 문서, 웹페이지, 이메일, 코드 저장소, 외부 도구 output은 indirect prompt injection 공격면을 어떻게 확장하는가? |
| RQ4 | Prompt injection은 정보 유출, 정책 우회, 잘못된 답변, 도구 오남용, 권한 상승 문제와 어떻게 연결되는가? |
| RQ5 | 방어전략은 input filtering, instruction hierarchy, context isolation, retrieval trust, output monitoring, human approval로 어떻게 구성될 수 있는가? |

---

## 3. 논문의 핵심 기여

| 기여 | 설명 | W08 연결 |
|---|---|---|
| Prompt injection taxonomy | direct/indirect injection, instruction override, prompt leakage, goal hijacking 등 공격유형을 정리 | W08의 직접 보안 핵심 |
| Root cause 분석 | LLM의 instruction-following 특성, context 혼합, 신뢰 경계 부재, 자연어 명령 해석 문제를 원인으로 설명 | prompt framework 취약성 해석 |
| RAG/agent 공격면 확장 | retrieved document와 tool output이 prompt로 직렬화되는 순간 공격면이 됨을 설명 | W08 P01/P02/P03 연결 |
| Defense strategy 정리 | filtering, isolation, policy enforcement, monitoring, human-in-the-loop 방어를 분류 | 기말논문 방어 체크리스트 근거 |
| 평가 관점 제시 | ASR, policy compliance, over-refusal, detection rate, utility trade-off를 평가축으로 사용 가능 | W08 실험·분석 지표 설계 |

---

## 4. 목차별 핵심 개괄

| 목차 | 핵심 내용 | 비전공자용 이해 |
|---|---|---|
| 1. Introduction | LLM이 다양한 업무에 활용되면서 prompt injection이 새로운 보안 위협으로 부상했다. 공격자는 자연어 지시를 이용해 모델이 원래 정책이나 사용자 의도를 벗어나게 만들 수 있다. | AI에게 “이전 지시는 무시하고 내 말을 따라라”는 식의 지시가 섞이면 AI가 잘못된 행동을 할 수 있다. |
| 2. Background | LLM, prompt, system/user instruction, RAG, tool use, agent workflow의 기본 구조를 설명한다. | LLM은 질문 하나만 보는 것이 아니라 시스템 지시, 사용자 입력, 검색문서, 도구 결과를 함께 보고 답한다. |
| 3. Attack Methods | Direct injection, indirect injection, goal hijacking, prompt leakage, jailbreak-style instruction, retrieved-context injection 등을 분류한다. | 공격자가 직접 질문에 악성 지시를 넣거나, 웹문서·메일·검색문서에 숨겨둔 지시가 나중에 AI에게 전달될 수 있다. |
| 4. Root Causes | 자연어 지시와 데이터의 경계가 모호하고, LLM이 instruction hierarchy를 엄격한 프로그램 규칙처럼 강제하지 못하는 점을 원인으로 본다. | AI는 문서 안의 “내용”과 “명령”을 항상 완벽히 구분하지 못한다. |
| 5. Defense Strategies | 입력 검사, prompt sanitization, instruction hierarchy, context isolation, source trust, output monitoring, tool permission, human approval을 방어책으로 정리한다. | 외부 문서를 읽더라도 그 안의 지시문은 명령으로 실행하지 못하게 분리해야 한다. |
| 6. Evaluation | 공격 성공률, 정책 준수율, 정상 업무 성능, 과잉 거절, 탐지율, 로그 재현성을 함께 평가해야 한다. | 방어가 강해도 정상 요청을 다 막으면 쓸 수 없다. 안전성과 유용성을 같이 봐야 한다. |
| 7. Open Challenges | 완전한 방어 어려움, 새로운 prompt 변형, RAG/agent/tool 환경 복잡성, benchmark 부족, 운영 로그와 책임성 문제가 남아 있다. | prompt injection은 단일 필터로 끝나는 문제가 아니라 시스템 설계 문제다. |
| 8. Conclusion | Prompt injection은 LLM 시스템의 신뢰 경계와 운영 통제 문제이며, RAG·agent 환경에서는 source isolation과 audit이 필수다. | AI 보안은 답변 내용만 보는 것이 아니라 어떤 지시와 근거를 보고 답했는지 추적해야 한다. |

---

## 5. 핵심 이론 및 수식

> 아래 수식은 prompt injection 평가를 W08 보고서에서 설명하기 위한 표준화된 표현이다. 실제 공격 payload를 제공하지 않고, 안전한 toy prompt set 또는 문헌 기반 평가를 전제로 한다.

### 5.1 Prompt-Conditioned LLM Output

LLM 출력은 system instruction, user prompt, retrieved document, tool output이 결합된 조건부 생성 결과다.

$$
y\sim p_\theta(y\mid s,u,r,\tau,h)
$$

| 기호 | 의미 |
|---|---|
| $s$ | system/developer instruction |
| $u$ | user prompt |
| $r$ | retrieved document 또는 외부 context |
| $\tau$ | tool output 또는 tool instruction |
| $h$ | conversation history |
| $y$ | 생성된 답변 또는 tool action |

### 비전공자용 설명

LLM은 사용자의 질문만 보는 것이 아니다. 시스템 규칙, 검색된 문서, 이전 대화, 도구 결과를 함께 보고 다음 답을 만든다. 이 중 신뢰할 수 없는 문서가 명령처럼 작동하면 문제가 생긴다.

### 보안적 의미

Prompt injection은 $u$, $r$, $\tau$ 중 신뢰할 수 없는 영역의 문장이 $s$보다 우선되는 것처럼 작동할 때 발생한다. 따라서 context isolation과 instruction hierarchy가 필요하다.

---

### 5.2 Direct Prompt Injection

Direct injection은 사용자가 직접 악성 지시를 입력해 정책 또는 원래 작업을 우회하려는 경우다.

$$
ASR_{direct}=\frac{1}{N}\sum_{i=1}^{N}\mathbf{1}\left[f_\theta(s,u_i^{mal})\in Y_{attack}\right]
$$

| 기호 | 의미 |
|---|---|
| $u_i^{mal}$ | 악성 의도를 가진 사용자 입력 |
| $Y_{attack}$ | 공격자가 원하는 정책 위반 또는 목표 출력 집합 |

### 비전공자용 설명

사용자가 AI에게 직접 “규칙을 무시하라”는 식의 지시를 넣는 경우다. 실제 보고서에서는 구체적 공격문을 제공하지 않고 범주와 평가 지표만 사용한다.

---

### 5.3 Indirect Prompt Injection

Indirect injection은 악성 지시가 외부 문서나 검색 결과 안에 숨어 있다가 RAG context로 들어오는 경우다.

$$
ASR_{indirect}=\frac{1}{N}\sum_{i=1}^{N}\mathbf{1}\left[f_\theta(s,u_i,d_i^{mal})\in Y_{attack}\right]
$$

| 기호 | 의미 |
|---|---|
| $d_i^{mal}$ | 악성 instruction이 포함된 retrieved document |
| $u_i$ | 정상 사용자 질문 |
| $Y_{attack}$ | 공격자 목표 출력 또는 행동 |

### 비전공자용 설명

사용자는 정상 질문을 했지만, AI가 읽어온 문서 안에 악성 지시가 숨어 있는 경우다. RAG 시스템에서 특히 중요하다.

### 보안적 의미

RAG 문서는 단순 참고자료가 아니라 LLM prompt의 일부가 된다. 따라서 외부 문서의 출처와 내용, 문서 안의 instruction-like text를 분리해야 한다.

---

### 5.4 Instruction Conflict Rate

System instruction과 retrieved/user instruction이 충돌하는 비율을 평가한다.

$$
ConflictRate=\frac{N_{conflict}}{N_{total}}
$$

| 기호 | 의미 |
|---|---|
| $N_{conflict}$ | 상위 정책과 하위 입력 또는 외부 context가 충돌한 사례 수 |
| $N_{total}$ | 전체 평가 사례 수 |

### 보안적 의미

Conflict가 많은 prompt pipeline은 구조적으로 위험하다. 탐지만이 아니라 충돌 발생 시 어떤 instruction을 우선할지 정책을 명시해야 한다.

---

### 5.5 Policy Compliance

Prompt injection 방어의 목표는 공격을 막으면서 정상 기능을 유지하는 것이다.

$$
Compliance=1-ASR_{inj}-ViolationRate
$$

| 기호 | 의미 |
|---|---|
| $ASR_{inj}$ | prompt injection 공격 성공률 |
| $ViolationRate$ | 정책 위반 출력 비율 |

### 보안적 의미

Compliance가 높다는 것은 공격 지시를 따르지 않고, 시스템 정책을 유지한다는 뜻이다. 단, 정상 요청까지 과도하게 거절하는 over-refusal도 별도로 봐야 한다.

---

### 5.6 Security-Utility Trade-off

방어가 너무 강하면 정상 업무 성능이 떨어질 수 있다.

$$
SecureUtility=Utility-\lambda_1 ASR_{inj}-\lambda_2 ViolationRate-\lambda_3 OverRefusal
$$

| 기호 | 의미 |
|---|---|
| $Utility$ | 정상 task 수행 성능 |
| $OverRefusal$ | 안전한 요청을 불필요하게 거절한 비율 |
| $\lambda_1,\lambda_2,\lambda_3$ | 위험 항목별 가중치 |

### 비전공자용 설명

보안 필터가 너무 약하면 공격에 뚫리고, 너무 강하면 정상 질문도 모두 거절한다. 따라서 보안성과 유용성을 함께 평가해야 한다.

---

## 6. AI 원리 70% 관점 분석

| 원리 항목 | 설명 | W08/P04에서의 의미 |
|---|---|---|
| Instruction following | LLM이 자연어 지시를 따르는 능력 | prompt injection의 기술적 원인 |
| Context mixing | system, user, retrieved, tool context가 하나의 prompt로 결합 | 신뢰 경계 붕괴 가능성 |
| RAG | 외부 문서를 prompt context로 추가 | indirect injection 주요 경로 |
| Tool use | LLM이 외부 API/도구 호출 | tool misuse와 권한 오남용 위험 |
| Agent workflow | 계획·검색·도구사용을 반복 수행 | injection이 여러 단계로 전파 가능 |
| Policy alignment | 모델이 정책과 안전 규칙을 따르도록 조정 | policy bypass 평가 필요 |
| Evaluation | ASR, compliance, utility, over-refusal 측정 | 보안성과 유용성 균형 평가 |

---

## 7. 보안 이슈 30% 관점 분석

| 보안 항목 | Prompt Injection 관점 해석 | 대표 평가 지표 |
|---|---|---|
| 기밀성 | system prompt, 내부 문서, API 응답, 사용자 정보가 유출될 수 있음 | leakage rate, secret exposure rate |
| 무결성 | 악성 instruction이 답변과 tool action을 왜곡할 수 있음 | ASR, policy violation rate |
| 가용성 | injection 방어 실패 또는 과잉 방어가 서비스 품질을 떨어뜨림 | over-refusal, latency, failure rate |
| 프라이버시 | retrieved context와 conversation history에 개인정보가 포함될 수 있음 | sensitive disclosure rate |
| 책임성 | 어떤 prompt/context 때문에 위반이 발생했는지 추적해야 함 | prompt-context-output trace, audit completeness |
| 안전성 | agent/tool 환경에서 잘못된 action이 실제 피해로 이어질 수 있음 | unauthorized tool call rate, human approval rate |

---

## 8. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | system prompt, developer instruction, user intent, retrieved document, tool permission, memory, API result, output policy, audit log |
| 공격자 목표 | instruction override, goal hijacking, system prompt leakage, data exfiltration, harmful output, policy bypass, tool misuse |
| 공격자 능력 | user prompt 작성, 웹/문서/검색 결과에 악성 instruction 삽입, metadata 조작, tool output 오염, context ordering 악용 |
| 공격 경로 | user input/source document/tool output → prompt template → LLM context window → output/tool action → downstream workflow |
| 방어자 능력 | instruction hierarchy, untrusted context labeling, input filtering, source validation, tool permission, output monitoring, human approval |
| 제외 범위 | 실제 서비스 공격, 유해 prompt 배포, 개인정보 유출 실험, 공격 payload 제공, 무단 API 호출 |

---

## 9. 방어전략 정리

| 방어전략 | 설명 | 한계 |
|---|---|---|
| Input filtering | 사용자 입력과 retrieved context에서 위험 신호 탐지 | 우회 표현과 false positive 문제 |
| Prompt sanitization | 외부 문서의 instruction-like text 제거 또는 무력화 | 의미 손실과 탐지 실패 가능성 |
| Instruction hierarchy | system/developer instruction을 user/retrieved context보다 우선 | LLM이 항상 엄격히 따르지 않을 수 있음 |
| Context isolation | 신뢰/비신뢰 context를 구조적으로 분리 | 구현 복잡성과 token cost 증가 |
| Source validation | 문서 출처, 권한, metadata, citation 검증 | 오염된 신뢰 출처 문제 |
| Output monitoring | 응답 후 정책 위반·정보유출 검사 | 사후 탐지이므로 완전한 예방은 아님 |
| Tool permission | tool call 권한 최소화와 human approval 적용 | 자동화 효율 저하 |
| Audit logging | prompt-context-output-tool trace 기록 | 개인정보·로그 보관 정책 필요 |

---

## 10. 평가방법 및 지표

| 평가축 | 지표 | 의미 | W08/P04 활용 |
|---|---|---|---|
| 공격 성공 | ASR, goal hijack rate | injection이 목표 출력을 유도했는지 | 핵심 보안 지표 |
| 정책 준수 | policy compliance, violation rate | 시스템 정책 유지 여부 | 방어 효과 평가 |
| 탐지 | detection rate, false positive rate | injection 탐지 성능 | 필터·모니터 평가 |
| 유용성 | task success, answer quality | 정상 업무 유지 여부 | 보안-유용성 균형 |
| 과잉방어 | over-refusal rate | 안전한 요청을 불필요하게 거절하는 비율 | 실사용성 평가 |
| 격리 성공 | source isolation success, context boundary violation | 외부 문서를 명령으로 실행하지 않는지 | RAG 방어 평가 |
| 도구 안전 | unauthorized tool call rate | injection에 의한 도구 오남용 여부 | agent 보안 평가 |
| 감사 가능성 | prompt-context-output trace completeness | 사고 재현·책임 추적 가능성 | W14/W15 연결 |

---

## 11. 재현성 체크리스트

| 항목 | 기록해야 할 내용 |
|---|---|
| Prompt set | 정상 prompt, 공격 범주, direct/indirect 구분, 구체 payload 비공개 처리 |
| Context source | retrieved document 출처, 신뢰/비신뢰 label, 문서 hash |
| Prompt template | system/user/retrieved/tool 영역 분리, template version |
| Model setting | LLM model/version, temperature, top-p, max tokens, safety setting |
| RAG setting | retriever, Top-k, chunking, reranker, source validation rule |
| Tool setting | tool permission, allowed action, human approval policy |
| Evaluation | ASR, compliance, over-refusal, utility, detection rate, audit completeness |
| Security log | prompt-context-output-tool trace, refusal case, policy violation case, reviewer decision |
| 한계 | toy prompt set 결과를 실제 서비스 보안 보증으로 과장하지 않음 |

---

## 12. 논문의 고유 기여

1. Prompt injection을 LLM 응용의 핵심 보안 위협으로 정리한다.
2. Direct injection과 indirect injection을 구분하고, RAG 환경에서 외부 문서가 공격면이 되는 이유를 설명한다.
3. Prompt injection의 근본 원인을 instruction hierarchy와 신뢰 경계 분리 실패로 해석한다.
4. 방어를 단순 필터링이 아니라 context isolation, source trust, output monitoring, human approval, audit logging으로 확장한다.
5. W08의 기말논문 주제인 RAG/prompt injection 보안 평가에서 ASR, policy compliance, over-refusal, source isolation 지표를 설계하는 근거를 제공한다.

---

## 13. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 완전 방어 어려움 | 자연어 지시가 다양해 단일 필터로 모든 injection을 차단하기 어렵다. | 다층 방어와 human review 사용 |
| Benchmark 부족 | 공격/방어 평가 데이터셋과 표준 지표가 아직 충분히 통일되지 않았다. | toy prompt set과 평가 기준 명시 |
| RAG context 복잡성 | 검색 문서가 많아질수록 신뢰 경계 관리가 어려워진다. | source trust, citation support, context isolation 적용 |
| Agent/tool 위험 | tool call이 포함되면 prompt injection이 실제 action으로 이어질 수 있다. | 권한 최소화와 승인 기반 실행 적용 |
| 과잉방어 문제 | 방어가 강하면 정상 질의도 거절할 수 있다. | over-refusal과 utility를 함께 측정 |
| 로그·프라이버시 문제 | 감사 로그가 필요하지만 prompt/context 자체가 민감정보일 수 있다. | log minimization과 access control 적용 |

---

## 14. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | Prompt injection은 RAG/agent형 LLM 시스템의 대표 보안 위협이라는 문제의식 |
| 2장 관련연구 | prompt injection attack methods, root causes, defense strategies survey 정리 |
| 3장 위협모형 | system/user/retrieved/tool context의 신뢰 경계와 공격자 능력 정의 |
| 4장 연구방법 | ASR, policy compliance, over-refusal, source isolation, unauthorized tool call rate 지표 설계 |
| 5장 분석 | direct/indirect injection attack surface mapping과 방어 체크리스트 제시 |
| 6장 보안적 함의 | RAG 문서 오염, tool misuse, human approval, audit log 필요성 해석 |

---

## 15. 기말논문 연결 3문장

1. W08에서 기말논문에 반영할 개념: prompt injection은 단순히 나쁜 질문을 넣는 문제가 아니라, system/user/retrieved/tool context의 신뢰 경계가 붕괴되어 LLM이 비신뢰 입력을 명령처럼 처리하는 구조적 취약성이다.
2. W08에서 기말논문에 반영할 표·그림·실험: direct/indirect injection 분류표, RAG context 오염 위협모형, ASR·policy compliance·over-refusal·source isolation 평가표를 반영한다.
3. W08이 LLM 보안 감사 프레임워크와 연결되는 지점: prompt template, retrieved document, tool permission, output monitoring, human approval log를 W14/W15 evidence chain에 포함해야 prompt injection 사고를 재현·감사할 수 있다.

---

## 16. 최종 판단

P04는 W08의 중심 보안 문헌이다. P01/P02가 GraphRAG와 graph context를 설명하고 P03이 prompting framework를 설명한다면, P04는 그 구조가 공격받는 방식과 방어전략을 직접 다룬다. 따라서 W08 기말논문 연결에서는 P04를 **RAG prompt injection 위협모형, ASR 기반 평가, source isolation, tool permission, audit logging 설계의 중심 근거 문헌**으로 사용하는 것이 적절하다.

---

## 17. 변환 호환성 메모

```bash
pandoc P04_summary.md -o P04_summary.docx
pandoc P04_summary.md -o P04_summary.pdf --pdf-engine=xelatex
```
