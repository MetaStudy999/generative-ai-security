# P02 Summary

## Security and Privacy Challenges of Large Language Models: A Survey — Badhan Chandra Das, M. Hadi Amini, Yanzhao Wu, ACM Computing Surveys, 2025

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W07 LLM 보안·프라이버시 |
| 논문명 | Security and Privacy Challenges of Large Language Models: A Survey |
| 저자 | Badhan Chandra Das, M. Hadi Amini, Yanzhao Wu |
| 공식 출판 정보 | ACM Computing Surveys, Vol. 57, No. 6, pp. 1–39, 2025 |
| DOI | https://doi.org/10.1145/3712001 |
| 보조 URL | https://arxiv.org/abs/2402.00888 |
| 로컬 PDF | `01_papers/pdf/02_Das_et_al_2025_LLM_Security_Privacy_Challenges.pdf` |
| 검증 상태 | W07 `paper_list.md`와 `download_source.md` 기준 공식 DOI 확인. 강의계획서에는 `Ankur Das et al.`로 표기되어 있으나, repo의 공식 확인 정보는 `Badhan Chandra Das, M. Hadi Amini, Yanzhao Wu`임 |
| PDF 확인 메모 | repo의 PDF 폴더에 P02 관련 PDF blob이 존재함을 확인했다. 요약은 로컬 PDF 경로와 W07 `paper_list.md`, `download_source.md`의 공식 DOI/arXiv 메타데이터 기준으로 보완했다. |
| 수식 호환성 | GitHub 수식 렌더링 오류 방지를 위해 `\operatorname`을 사용하지 않고 `\mathrm{...}` 형태로 작성했다. 긴 영문 subscript는 렌더링 오류를 줄이기 위해 짧은 변수명으로 분리했다. |
| 핵심 근거 사용 가능 여부 | 가능. W07의 직접 보안·프라이버시 핵심 문헌으로 사용 |

---

## 1. 한 문장 요약

이 논문은 LLM의 보안과 프라이버시 문제를 **prompt injection, jailbreak, adversarial prompt, training data memorization, prompt leakage, model extraction, membership inference, poisoning, backdoor, hallucination, harmful response, tool misuse, audit/log leakage, guardrail, monitoring, governance** 관점에서 체계화하며, W07에서 LLM 보안 평가를 입력·학습·추론·출력·도구·로그 전 과정의 **시스템 리스크 평가**로 설계해야 함을 보여주는 핵심 survey 문헌이다.

---

## 2. 핵심 연구문제

> LLM은 사전학습 데이터, fine-tuning 데이터, system prompt, user prompt, RAG context, model output, tool call, audit log가 연결된 시스템이다. 따라서 보안·프라이버시 위협도 모델 하나가 아니라 전체 LLM lifecycle과 운영 파이프라인에서 발생한다.

| 번호 | 연구질문 |
|---|---|
| RQ1 | LLM 위협은 학습 데이터, 모델 파라미터, 프롬프트, 검색 context, 출력, 도구 호출, 로그 중 어디에서 발생하는가? |
| RQ2 | Prompt injection, jailbreak, adversarial prompt는 system instruction과 safety policy를 어떻게 약화시키는가? |
| RQ3 | Training data memorization, prompt leakage, model extraction, membership inference는 어떤 프라이버시 위험으로 이어지는가? |
| RQ4 | Poisoning과 backdoor는 pretraining, fine-tuning, instruction tuning, RAG context, tool workflow에 어떻게 침투할 수 있는가? |
| RQ5 | Guardrail, filtering, red teaming, monitoring, access control, audit log는 어떤 지표로 검증되어야 하는가? |

---

## 3. 논문의 핵심 기여

| 기여 | 설명 | W07 연결 |
|---|---|---|
| 위협 taxonomy | LLM 보안·프라이버시 위협을 공격면별로 정리 | W07 threat model의 중심 |
| 프롬프트 공격 정리 | jailbreak, direct/indirect prompt injection, prompt manipulation을 설명 | W08 RAG prompt injection으로 확장 |
| 프라이버시 위험 정리 | memorization, leakage, extraction, inference 공격을 포함 | W11 DP/MIA와 연결 |
| 학습·배포 위험 연결 | poisoning, backdoor, malicious fine-tuning, unsafe deployment를 체계화 | W05/W14 연결 |
| 방어·거버넌스 관점 | guardrail, monitoring, red teaming, access control, audit를 강조 | W14 MLOps 감사와 연결 |
| 평가 지표 기반 | ASR, leakage rate, refusal quality, over-refusal, utility를 분리 | 기말논문 방법론에 직접 반영 |

---

## 4. 목차별 핵심 개괄

| 목차 | 핵심 내용 | 비전공자용 이해 |
|---|---|---|
| 1. Introduction | LLM은 강력하지만 보안·프라이버시 위협이 커서 체계적 평가가 필요하다. | 똑똑한 AI일수록 악용과 정보 유출 위험도 커진다. |
| 2. LLM Background | pretraining, fine-tuning, instruction tuning, prompting, RLHF, deployment 흐름을 설명한다. | LLM이 만들어지고 서비스되는 과정을 이해한다. |
| 3. Security Threats | prompt injection, jailbreak, adversarial prompt, poisoning, backdoor, harmful generation을 정리한다. | AI에게 위험한 지시를 숨겨 넣거나 안전장치를 우회할 수 있다. |
| 4. Privacy Threats | memorization, training data leakage, prompt leakage, membership inference, model extraction을 다룬다. | AI가 학습했거나 입력받은 민감정보를 다시 말할 수 있다. |
| 5. Misuse and Abuse | phishing, social engineering, malicious automation, unsafe code generation 등의 악용 가능성을 논의한다. | AI가 공격 자동화에 악용될 수 있다. |
| 6. Defense Methods | content filtering, guardrails, red teaming, privacy-preserving training, monitoring, access control을 정리한다. | 위험한 입력·출력을 막고 사용 기록을 감시한다. |
| 7. Evaluation and Governance | ASR, leakage, refusal, over-refusal, auditability, policy compliance를 함께 평가해야 한다. | 안전성은 점수 하나로 측정할 수 없다. |
| 8. Open Challenges | 빠른 기술 변화, 평가 표준 부족, dual-use 문제, deployment risk, 법·윤리 문제가 남는다. | 기술뿐 아니라 운영·윤리·감사 체계도 필요하다. |

---

## 5. 핵심 이론 및 수식

> 아래 수식은 논문이 정리한 보안·프라이버시 문제를 W07 보고서에서 평가하기 위해 표준화한 표현이다. 공격 절차를 재현하기 위한 단계가 아니라 평가 지표 정의용이다. GitHub 호환성을 위해 `\operatorname`은 사용하지 않는다.

### 5.1 공격 성공률

LLM 보안 공격 평가에서는 공격 프롬프트가 위험 응답, 정책 위반 응답, 또는 공격자 목표 응답을 유도한 비율을 측정한다.

$$
ASR=\frac{1}{N}\sum_{i=1}^{N}\mathbf{1}\left[f_\theta(p_i^{attack})\in Y_{unsafe}\right]
$$

| 기호 | 의미 |
|---|---|
| $ASR$ | Attack Success Rate |
| $p_i^{attack}$ | 공격 또는 우회 목적의 평가 프롬프트 |
| $Y_{unsafe}$ | 위험·정책 위반·공격자 목표 응답 집합 |
| $N$ | 평가 프롬프트 수 |

### 보안적 의미

ASR이 높으면 모델이 정상 benchmark에서 좋은 점수를 받더라도 보안적으로 취약하다. W07에서는 ASR을 실제 공격 절차가 아니라 안전한 toy prompt set과 방어 평가 지표로 제한한다.

---

### 5.2 프라이버시 누출률

프라이버시 평가에서는 민감정보가 응답 또는 로그에 노출된 비율을 측정한다.

$$
LeakageRate=\frac{N_{leak}}{N_{risk}}
$$

| 기호 | 의미 |
|---|---|
| $N_{risk}$ | privacy-risk 평가 입력 수 |
| $N_{leak}$ | 민감정보 또는 민감 패턴이 출력·로그에 노출된 사례 수 |

### 보안적 의미

Leakage rate는 단순한 출력 품질이 아니라 기밀성 지표다. prompt, RAG context, tool argument, output log 모두 누출 경로가 될 수 있다.

---

### 5.3 안전성·유용성 균형

보안 방어는 위험 응답을 줄이면서 정상 유용성도 유지해야 한다.

$$
SecurityUtilityScore=Utility-\lambda_1ASR-\lambda_2LeakageRate-\lambda_3OverRefusal
$$

| 기호 | 의미 |
|---|---|
| $Utility$ | 정상 작업 성능 또는 사용자 과업 성공률 |
| $ASR$ | 공격 성공률 |
| $LeakageRate$ | 민감정보 노출률 |
| $OverRefusal$ | 정상 요청을 과도하게 거절한 비율 |
| $\lambda_i$ | 각 위험 항목의 가중치 |

### 보안적 의미

무조건 거절하는 방어는 leakage와 ASR을 낮출 수 있지만 정상 과업을 방해한다. 따라서 refusal quality와 over-refusal을 동시에 측정해야 한다.

---

### 5.4 Refusal Quality

위험 요청을 적절히 거절하고 정상 요청은 처리하는 능력을 분리해 평가한다.

$$
RefusalQuality=\frac{N_{unsafe\ refused}}{N_{unsafe\ requests}}
$$

$$
OverRefusal=\frac{N_{benign\ refused}}{N_{benign\ requests}}
$$

### 보안적 의미

Refusal quality가 높아도 over-refusal이 높으면 실무 적용성이 낮다. 안전성과 사용성을 같이 보고해야 한다.

---

### 5.5 Policy Compliance

모델과 guardrail이 사전 정의한 보안 정책을 준수한 비율이다.

$$
PolicyCompliance=\frac{N_{compliant}}{N_{total}}
$$

### 보안적 의미

LLM 보안에서는 각 응답이 정책 기준을 만족하는지, 거절이 필요한 경우 제대로 거절했는지, 로그와 도구 호출이 정책에 맞는지 확인해야 한다.

---

### 5.6 Defense Coverage

위협 항목 중 방어 또는 모니터링이 적용된 비율이다.

$$
DefenseCoverage=\frac{|Threats_{covered}|}{|Threats_{total}|}
$$

### 보안적 의미

prompt injection만 막고 privacy leakage나 tool misuse를 방치하면 전체 방어 체계가 불완전하다.

---

### 5.7 Audit Completeness

보안 평가와 운영 감사에 필요한 이벤트가 기록된 비율이다.

$$
AuditCompleteness=\frac{|Events_{logged}|}{|Events_{required}|}
$$

### 보안적 의미

prompt, output, policy decision, tool call, human review, model version이 연결되어야 사후 검증이 가능하다. 단, 로그 자체가 민감정보를 재저장하지 않도록 placeholder/hash 중심으로 관리해야 한다.

---

### 5.8 LLM Security Risk

LLM 시스템의 주요 보안·프라이버시 위험을 요약한다.

$$
LLMRisk=PromptRisk+DataRisk+OutputRisk+ToolRisk+LogRisk-DefenseCoverage
$$

### 보안적 의미

LLM 보안은 prompt 하나만 막는 문제가 아니다. 데이터, 출력, 도구, 로그, 운영 정책까지 통합 관리해야 한다.

---

## 6. LLM 보안·프라이버시 공격면

| 공격면 | 주요 위험 | 대표 지표 | 연결 주차 |
|---|---|---|---|
| 학습 데이터 | memorization, poisoning, backdoor | leakage, ASR, data lineage | W05, W11 |
| 프롬프트 입력 | jailbreak, direct prompt injection | ASR, policy compliance | W08 |
| 검색 컨텍스트 | indirect prompt injection, 문서 오염 | source isolation, citation support | W08 |
| 출력 | harmful response, hallucination, 민감정보 재출력 | unsafe rate, hallucination rate | W07, W15 |
| 도구 호출 | 권한 오남용, 외부 API leakage | tool misuse rate, audit log | W14 |
| 운영 로그 | prompt/output 저장에 따른 2차 유출 | log leakage, retention audit | W14, W15 |

---

## 7. 보안 이슈 30% 관점 분석

| 보안 항목 | LLM security/privacy 관점 해석 | 대표 평가 지표 |
|---|---|---|
| 기밀성 | prompt, RAG context, output, log, tool argument에 민감정보 포함 가능 | LeakageRate, log leakage |
| 무결성 | prompt injection, poisoning, backdoor가 모델 판단과 정책을 왜곡 | ASR, policy compliance |
| 가용성 | 강한 guardrail과 red-team 필터가 latency와 over-refusal을 증가 | latency, OverRefusal |
| 프라이버시 | memorization, membership inference, prompt leakage가 개인정보 유출로 연결 | MI signal, leakage test |
| 안전성 | harmful response, unsafe code, dangerous advice, jailbreak 위험 | unsafe rate, refusal quality |
| 책임성 | prompt/output/tool/log/human-review evidence가 있어야 감사 가능 | AuditCompleteness |

---

## 8. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | system prompt, user prompt, training data, fine-tuning data, RAG context, model output, tool credential, audit log |
| 공격자 목표 | 안전정책 우회, 위험 응답 유도, 민감정보 추출, 모델 동작 추론, 악성 도구 호출 유도 |
| 공격자 능력 | adversarial prompt 작성, 반복 질의, 문서 오염, 간접 지시 삽입, 출력 관찰, 우회 표현 사용 |
| 공격 경로 | prompt/context/tool input → LLM reasoning/output → tool call/log → policy decision 또는 external exposure |
| 방어자 능력 | policy wrapper, content filtering, prompt isolation, red teaming, monitoring, access control, human review, safe logging |
| 제외 범위 | 실제 서비스 대상 공격, 개인정보 포함 실험, 악성코드 실행, 유해 지시문 제공, 공격 절차 상세화 |

---

## 9. 평가방법 및 지표

| 지표 | 의미 | W07/P02 활용 |
|---|---|---|
| ASR | 공격 목표 응답 비율 | jailbreak/prompt injection 저항성 |
| LeakageRate | 민감정보 출력·로그 노출 비율 | prompt privacy, memorization 평가 |
| RefusalQuality | 위험 요청을 적절히 거절하는 정도 | safety alignment 평가 |
| OverRefusal | 정상 요청까지 거절하는 비율 | utility 손실 평가 |
| Utility | 정상 과업 성능 | 방어 부작용 확인 |
| PolicyCompliance | 사전 정의 정책 준수율 | guardrail 평가 |
| DefenseCoverage | 위협 대비 방어 적용 범위 | 보안 통제 범위 |
| AuditCompleteness | prompt/output/tool/log 보존 정도 | W14/W15 evidence chain |
| HumanReviewAgreement | 사람 검토와 모델 판단 일치도 | high-stakes evaluation |

---

## 10. 재현성 체크리스트

| 항목 | 기록해야 할 내용 |
|---|---|
| Bibliographic status | DOI, ACM CSUR 출판정보, arXiv 판본, 강의계획서 표기 차이, 로컬 PDF 상태 |
| Model | 모델명, 버전, API/로컬 여부, decoding setting |
| Prompt | clean prompt, attack prompt, privacy-risk prompt, system prompt 분리 |
| Data | synthetic prompt set 사용 여부, 개인정보 미사용 여부 |
| Defense | filtering rule, refusal policy, guardrail version, human review rule |
| Output | raw output, policy decision, refusal 여부, leakage 여부 |
| Tool | tool schema, tool 권한, tool call log |
| Evaluation | ASR, LeakageRate, Utility, OverRefusal, PolicyCompliance, AuditCompleteness |
| Limitation | toy prompt 결과를 실제 LLM 안전성 보증으로 일반화하지 않음 |
| GitHub math | `\operatorname` 사용 금지, 짧은 변수명과 `\mathrm{...}` 형태 사용 |

---

## 11. 논문의 고유 기여

1. LLM 보안과 프라이버시 위협을 종합적으로 분류했다.
2. 프롬프트 기반 공격과 학습·배포 단계 위협을 하나의 시스템 리스크로 볼 수 있게 했다.
3. 프라이버시 누출과 안전성 위반을 단순 품질 문제가 아니라 별도 평가축으로 분리했다.
4. W08 RAG prompt injection, W11 privacy, W14 MLOps 감사로 확장 가능한 공통 평가 구조를 제공한다.
5. 기말논문에서 LLM 보안 평가를 utility, ASR, leakage, refusal, over-refusal, auditability로 분리하는 근거가 된다.

---

## 12. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 빠른 기술 변화 | LLM 공격·방어는 빠르게 변한다. | 평가일과 모델 버전을 명시 |
| 실제 위험 실험 제한 | 실제 개인정보·운영 API 대상 실험은 부적절하다. | synthetic prompt와 toy evaluation으로 제한 |
| 방어 일반화 한계 | 한 guardrail이 모든 우회 표현을 막지 못한다. | 방어 범위와 한계 명시 |
| 평가 표준 부족 | ASR, refusal, leakage, utility 정의가 연구마다 다를 수 있다. | 자체 평가 프로토콜 명시 |
| 로그 재유출 위험 | 감사 로그가 원본 prompt/output을 그대로 저장하면 2차 유출 가능 | placeholder/hash logging 적용 |
| 강의계획서 표기 차이 | 강의계획서의 저자 표기와 공식 metadata가 다르다. | DOI 기준 인용, 차이 메모 유지 |

---

## 13. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | LLM 보안은 모델 단독 문제가 아니라 prompt, data, output, tool, log가 연결된 시스템 리스크라는 문제의식 |
| 2장 관련연구 | LLM security/privacy challenge survey로 P02 정리 |
| 3장 위협모형 | system prompt, user prompt, RAG context, tool credential, audit log 보호 자산 정의 |
| 4장 연구방법 | ASR, LeakageRate, SecurityUtilityScore, RefusalQuality, PolicyCompliance, DefenseCoverage, AuditCompleteness, LLMRisk 지표 설계 |
| 5장 분석 | LLM attack surface matrix와 defense coverage table 제시 |
| 6장 보안적 함의 | prompt injection, memorization, leakage, guardrail 한계, safe logging, auditability 해석 |
| 부록 | synthetic prompt set, guardrail rule, output audit, model version, limitation statement 수록 |

---

## 14. 기말논문 연결 3문장

1. W07에서 기말논문에 반영할 개념: LLM 보안은 prompt injection과 jailbreak뿐 아니라 training data leakage, memorization, poisoning, output leakage, tool misuse, audit log leakage까지 포함하는 시스템 리스크다.
2. W07에서 기말논문에 반영할 표·그림·실험: ASR, LeakageRate, SecurityUtilityScore, PolicyCompliance, DefenseCoverage, AuditCompleteness, LLMRisk 수식표와 LLM attack surface matrix를 반영한다.
3. W07이 W08/W14/W15와 연결되는 지점: RAG 문서 오염, agent tool call, MLOps audit, final evidence chain에서도 prompt/output/tool/log 보호가 반복되므로 P02의 taxonomy를 전체 기말논문 구조에 반영한다.

---

## 15. 최종 판단

P02는 W07의 직접 보안·프라이버시 핵심 문헌이다. 이 논문은 LLM의 위험을 prompt 공격 하나로 축소하지 않고, 학습 데이터·프롬프트·검색 context·출력·도구 호출·로그까지 포함하는 시스템 공격면으로 정리한다. 따라서 기말논문에서는 P02를 **LLM 보안·프라이버시 위협모형, ASR/leakage/refusal/over-refusal 지표, guardrail 평가, safe logging, audit evidence chain의 중심 근거 문헌**으로 사용하는 것이 적절하다.

---

## 16. GitHub 수식 호환성 메모

이 파일에서는 GitHub 수식 렌더링 오류 방지를 위해 `\operatorname`을 사용하지 않는다.

| 피해야 할 표현 | 권장 표현 |
|---|---|
| `\operatorname{softmax}` | `\mathrm{softmax}` |
| `\operatorname{argmax}` | `\mathrm{argmax}` 또는 `\arg\max` |
| 긴 영문 subscript | 짧은 변수명 사용 후 표에서 의미 설명 |

```bash
pandoc P02_summary.md -o P02_summary.docx
pandoc P02_summary.md -o P02_summary.pdf --pdf-engine=xelatex
```
