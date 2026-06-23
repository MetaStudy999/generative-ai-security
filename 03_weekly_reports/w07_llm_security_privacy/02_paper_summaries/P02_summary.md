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
| 강의계획서 표기와 차이 | 강의계획서에는 `Ankur Das et al.`로 표기되어 있으나, repo의 공식 확인 정보는 `Badhan Chandra Das, M. Hadi Amini, Yanzhao Wu`임 |
| 핵심 근거 사용 가능 여부 | 가능. W07의 직접 보안·프라이버시 핵심 문헌으로 사용 |

---

## 1. 한 문장 요약

이 논문은 LLM의 보안과 프라이버시 문제를 **프롬프트 공격, jailbreak, 데이터 유출, 학습 데이터 기억, 모델 추출, poisoning, backdoor, 악용 가능성, 방어·거버넌스** 관점에서 체계화하여, LLM 보안 평가가 입력·학습·추론·출력·배포·로그 전 과정의 시스템 리스크 평가로 설계되어야 함을 보여주는 핵심 survey 문헌이다.

---

## 2. 핵심 연구문제

> LLM은 어떤 보안·프라이버시 위협에 노출되어 있으며, 방어자는 유용성, 안전성, 프라이버시, 강건성, 감사 가능성을 어떻게 함께 평가해야 하는가?

| 번호 | 연구질문 |
|---|---|
| RQ1 | LLM 위협은 학습 데이터, 모델 파라미터, 프롬프트, 출력, 도구 호출, 로그 중 어디에서 발생하는가? |
| RQ2 | Prompt injection, jailbreak, adversarial prompt는 시스템 지시와 안전정책을 어떻게 약화시키는가? |
| RQ3 | Training data memorization, prompt leakage, model inversion, membership inference는 어떤 프라이버시 위험으로 이어지는가? |
| RQ4 | Poisoning과 backdoor는 LLM의 pretraining, fine-tuning, instruction tuning, RAG context에 어떻게 침투할 수 있는가? |
| RQ5 | Guardrail, filtering, red teaming, monitoring, audit log는 어떤 평가 지표와 함께 검증되어야 하는가? |

---

## 3. 논문의 핵심 기여

| 기여 | 설명 | W07 연결 |
|---|---|---|
| 위협 taxonomy | LLM 보안·프라이버시 위협을 공격면별로 정리 | W07 threat model의 중심 |
| 프롬프트 공격 정리 | jailbreak, direct/indirect prompt injection, prompt manipulation을 설명 | W08 RAG prompt injection으로 확장 |
| 프라이버시 위험 정리 | memorization, leakage, extraction, inference 공격을 포함 | W11 DP/MIA와 연결 |
| 방어·거버넌스 관점 | guardrail, monitoring, red teaming, access control, audit를 강조 | W14 MLOps 감사와 연결 |
| 평가 지표 기반 | ASR, leakage rate, refusal quality, over-refusal, utility를 분리 | 기말논문 방법론에 직접 반영 |

---

## 4. 핵심 이론 및 수식

> 아래 수식은 논문이 정리한 보안·프라이버시 문제를 W07 보고서에서 평가하기 위해 표준화한 표현이다. 공격 절차를 재현하기 위한 단계가 아니라 평가 지표 정의용이다.

### 4.1 공격 성공률

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

### 4.2 프라이버시 누출률

프라이버시 평가에서는 민감정보가 응답 또는 로그에 노출된 비율을 측정한다.

$$
LeakageRate=\frac{N_{sensitive\ output}}{N_{privacy\ risk\ prompts}}
$$

| 기호 | 의미 |
|---|---|
| $N_{privacy\ risk\ prompts}$ | 민감정보 노출 가능성을 평가하기 위한 프롬프트 수 |
| $N_{sensitive\ output}$ | 민감정보 또는 민감 패턴이 출력된 사례 수 |

### 보안적 의미

Leakage rate는 단순한 출력 품질이 아니라 기밀성 지표다. prompt, RAG context, tool argument, output log 모두 누출 경로가 될 수 있다.

---

### 4.3 안전성·유용성 균형

보안 방어는 위험 응답을 줄이면서 정상 유용성도 유지해야 한다.

$$
SecurityUtilityScore=Utility-\lambda_1 ASR-\lambda_2 LeakageRate-\lambda_3 OverRefusal
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

## 5. LLM 보안·프라이버시 공격면

| 공격면 | 주요 위험 | 대표 지표 | 연결 주차 |
|---|---|---|---|
| 학습 데이터 | memorization, poisoning, backdoor | leakage, ASR, data lineage | W05, W11 |
| 프롬프트 입력 | jailbreak, direct prompt injection | ASR, policy compliance | W08 |
| 검색 컨텍스트 | indirect prompt injection, 문서 오염 | source isolation, citation support | W08 |
| 출력 | harmful response, hallucination, 민감정보 재출력 | unsafe rate, hallucination rate | W07, W15 |
| 도구 호출 | 권한 오남용, 외부 API leakage | tool misuse rate, audit log | W14 |
| 운영 로그 | prompt/output 저장에 따른 2차 유출 | log leakage, retention audit | W14, W15 |

---

## 6. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | system prompt, user prompt, training data, fine-tuning data, RAG context, model output, tool credential, audit log |
| 공격자 목표 | 안전정책 우회, 위험 응답 유도, 민감정보 추출, 모델 동작 추론, 악성 도구 호출 유도 |
| 공격자 능력 | adversarial prompt 작성, 반복 질의, 문서 오염, 간접 지시 삽입, 출력 관찰 |
| 방어자 능력 | policy wrapper, content filtering, prompt isolation, red teaming, monitoring, access control, human review |
| 제외 범위 | 실제 서비스 대상 공격, 개인정보 포함 실험, 악성코드 실행, 유해 지시문 제공 |

---

## 7. 평가방법 및 지표

| 지표 | 의미 | W07/P02 활용 |
|---|---|---|
| ASR | 공격 목표 응답 비율 | jailbreak/prompt injection 저항성 |
| Leakage Rate | 민감정보 출력 비율 | prompt privacy, memorization 평가 |
| Refusal Quality | 위험 요청을 적절히 거절하는 정도 | safety alignment 평가 |
| Over-refusal | 정상 요청까지 거절하는 비율 | utility 손실 평가 |
| Utility | 정상 과업 성능 | 방어 부작용 확인 |
| Policy Compliance | 사전 정의 정책 준수율 | guardrail 평가 |
| Audit Completeness | prompt/output/tool/log 보존 정도 | W14/W15 evidence chain |
| Human Review Agreement | 사람 검토와 모델 판단 일치도 | high-stakes evaluation |

---

## 8. 재현성 체크리스트

| 항목 | 기록해야 할 내용 |
|---|---|
| 모델 | 모델명, 버전, API/로컬 여부, decoding setting |
| 프롬프트 | clean prompt, attack prompt, privacy-risk prompt, system prompt 분리 |
| 데이터 | synthetic prompt set 사용 여부, 개인정보 미사용 여부 |
| 방어 | filtering rule, refusal policy, guardrail version, human review rule |
| 출력 | raw output, policy decision, refusal 여부, leakage 여부 |
| 도구 | tool schema, tool 권한, tool call log |
| 평가 | ASR, leakage rate, utility, over-refusal, policy compliance |
| 한계 | toy prompt 결과를 실제 LLM 안전성 보증으로 일반화하지 않음 |

---

## 9. 논문의 고유 기여

1. LLM 보안과 프라이버시 위협을 종합적으로 분류했다.
2. 프롬프트 기반 공격과 학습·배포 단계 위협을 하나의 시스템 리스크로 볼 수 있게 했다.
3. 프라이버시 누출과 안전성 위반을 단순 품질 문제가 아니라 별도 평가축으로 분리했다.
4. W08 RAG prompt injection, W11 privacy, W14 MLOps 감사로 확장 가능한 공통 평가 구조를 제공한다.

---

## 10. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 빠른 기술 변화 | LLM 공격·방어는 빠르게 변한다. | 평가일과 모델 버전을 명시한다. |
| 실제 위험 실험 제한 | 실제 개인정보·운영 API 대상 실험은 부적절하다. | synthetic prompt와 toy evaluation으로 제한한다. |
| 방어 일반화 한계 | 한 guardrail이 모든 우회 표현을 막지 못한다. | 방어 범위와 한계를 명시한다. |
| 측정 편향 | ASR, leakage, refusal 판단 기준이 평가자에 따라 달라질 수 있다. | rubric과 human review 기준을 기록한다. |
| utility와 safety trade-off | 안전성 강화가 정상 사용성을 낮출 수 있다. | over-refusal과 utility를 함께 보고한다. |

---

## 11. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | LLM 보안은 모델 정확도 문제가 아니라 입력·출력·도구·로그 전 과정의 시스템 리스크라는 문제의식 |
| 2장 관련연구 | LLM 보안·프라이버시 taxonomy 정리 |
| 3장 위협모형 | prompt, context, model, output, tool, log 공격면 정의 |
| 4장 연구방법 | ASR, leakage rate, refusal quality, over-refusal, utility 평가 설계 |
| 5장 분석 | toy prompt set 기반 안전한 평가 결과와 한계 제시 |
| 6장 보안적 함의 | high-stakes domain, audit log, human review 필요성 설명 |

---

## 12. 기말논문 연결 3문장

1. 이 주차에서 기말논문에 반영할 개념: LLM 보안은 jailbreak나 prompt injection 하나로 축소되지 않고, 학습 데이터·프롬프트·검색 문서·출력·도구 호출·로그를 포괄하는 시스템 보안 문제다.
2. 이 주차에서 기말논문에 반영할 표·그림·실험: LLM 보안 위협모형, ASR 수식, leakage rate 수식, refusal/over-refusal/utility 비교표를 반영한다.
3. 이 주차가 RAG 문서 오염/LLM 보안 감사 프레임워크와 연결되는 지점: W08에서는 검색 문서와 prompt injection으로 확장하고, W14/W15에서는 prompt-output-tool log와 human review evidence chain으로 확장한다.

---

## 13. 최종 판단

P02는 W07의 직접 보안·프라이버시 핵심 문헌이다. P01이 LLM 평가의 상위 taxonomy를 제공한다면, P02는 실제 LLM 보안 평가에서 무엇을 보호하고 어떤 지표로 측정할지를 정의한다.

---

## 14. 변환 호환성 메모

```bash
pandoc P02_summary.md -o P02_summary.docx
pandoc P02_summary.md -o P02_summary.pdf --pdf-engine=xelatex
```
