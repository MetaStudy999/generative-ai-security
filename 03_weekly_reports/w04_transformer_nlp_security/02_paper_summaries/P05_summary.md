# P05 Summary

## Privacy Preserving Prompt Engineering: A Survey — Kennedy Edemacu, Xintao Wu, ACM Computing Surveys, 2025

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W04 Transformer 변형 & NLP 대적공격·프라이버시 |
| 논문명 | Privacy Preserving Prompt Engineering: A Survey |
| 저자 | Kennedy Edemacu, Xintao Wu |
| 학술지 | ACM Computing Surveys |
| 권호/쪽 | Vol. 57, No. 10, pp. 1–36 |
| 연도 | 2025 |
| DOI | https://doi.org/10.1145/3729219 |
| 보조 URL | https://arxiv.org/abs/2404.06001 |
| 논문 유형 | Survey / Privacy-Preserving Prompt Engineering Review |
| 로컬 PDF | `01_papers/pdf/05_Edemacu_Wu_2025_Privacy_Preserving_Prompt_Engineering.pdf` |
| 강의계획서 지정 논문과 일치 여부 | 일치 |
| 핵심 근거 사용 가능 여부 | 가능 |
| 검증 메모 | W04 `paper_list.md` 기준 ACM CSUR 2025 출판 DOI 확인. Article 번호는 추가 확인 메모 |

---

## 1. 한 문장 요약

이 논문은 LLM prompting과 in-context learning에서 발생하는 민감정보 노출 위험을 **prompt privacy, ICL leakage, masking, rewriting, policy control, privacy-preserving prompt engineering, output auditing** 관점에서 정리하고, 프롬프트 보안 평가가 leakage rate와 utility/over-refusal을 동시에 측정해야 함을 보여주는 핵심 survey 논문이다.

---

## 2. 연구문제

> 사용자 프롬프트, ICL 예시, 검색 문서, 모델 출력, 로그, 외부 도구 호출 인자에서 민감정보가 어떻게 노출될 수 있으며, 이를 어떤 prompt engineering·policy·masking·auditing 방법으로 줄일 수 있는가?

| 번호 | 연구질문 |
|---|---|
| RQ1 | Prompt privacy 위험은 입력, context, output, log, tool call 중 어디에서 발생하는가? |
| RQ2 | ICL example과 few-shot prompt는 어떤 방식으로 민감정보를 노출할 수 있는가? |
| RQ3 | Masking, rewriting, policy control, privacy wrapper는 각각 어떤 장단점이 있는가? |
| RQ4 | Leakage rate, utility, over-refusal, policy compliance를 어떻게 함께 평가해야 하는가? |
| RQ5 | W04 toy prompt masking 결과를 실제 LLM privacy guarantee로 과장하지 않기 위해 어떤 한계가 필요한가? |

---

## 3. 핵심 이론 및 수식

### 3.1 Privacy Leakage Rate

프라이버시 위험 prompt 중 민감정보가 출력된 비율을 leakage rate로 표현할 수 있다.

$$
LeakageRate=\frac{N_{sensitive\_output}}{N_{privacy\_risk\_prompts}}
$$

| 기호 | 의미 |
|---|---|
| $N_{privacy\_risk\_prompts}$ | privacy-risk 평가 입력 수 |
| $N_{sensitive\_output}$ | 민감정보 노출 판정 수 |

### 보안적 의미

Leakage rate가 낮아도 utility가 크게 손상되거나 정상 요청을 과차단하면 방어가 실용적이지 않다. 따라서 leakage와 utility를 함께 평가해야 한다.

---

### 3.2 Masking Function

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

### 3.3 Privacy-Utility Trade-off

프라이버시 보호는 utility와 trade-off를 가질 수 있다.

$$
PrivacyUtilityScore = Utility - \lambda LeakageRate - \mu OverRefusal
$$

| 기호 | 의미 |
|---|---|
| $Utility$ | 정상 task 품질 |
| $LeakageRate$ | 민감정보 노출률 |
| $OverRefusal$ | 정상 요청을 과도하게 거절한 비율 |
| $\lambda,\mu$ | 위험 항목 가중치 |

### 보안적 의미

무조건 거절하거나 과도하게 마스킹하면 leakage는 줄어도 서비스 가치가 사라질 수 있다. 따라서 실무형 prompt privacy는 “누출 감소 + 정상 유틸리티 유지 + 과차단 최소화”를 함께 만족해야 한다.

---

## 4. AI 원리 관점 분석

| 항목 | 분석 |
|---|---|
| Prompting | 사용자가 자연어로 작업 지시와 데이터를 함께 제공한다. |
| ICL | few-shot 예시가 context에 포함되며 민감정보가 함께 들어갈 수 있다. |
| Context Window | 긴 prompt나 RAG 문서가 민감정보 포함 가능성을 높인다. |
| Output Generation | 모델은 context에 근거해 민감정보를 재출력하거나 요약할 수 있다. |
| Tool Use | 외부 API 호출 인자에 민감정보가 포함될 수 있다. |
| Logging | prompt와 output log가 2차 유출 경로가 될 수 있다. |

---

## 5. 보안 이슈 관점 분석

| 보안 항목 | Prompt Privacy 관점 해석 |
|---|---|
| 기밀성 | prompt, ICL example, RAG 문서, output, log의 민감정보 보호가 핵심이다. |
| 프라이버시 | 개인정보, 민감 속성, 영업비밀, 내부 문서가 prompt에 포함될 수 있다. |
| 무결성 | privacy policy가 prompt injection이나 우회 표현으로 무력화될 수 있다. |
| 가용성 | 과도한 마스킹과 거절은 정상 업무 처리를 방해한다. |
| 책임성 | 어떤 민감정보를 탐지·마스킹·출력 차단했는지 감사 로그가 필요하다. |
| 운영 리스크 | 실제 API, SaaS LLM, agent tool 호출, 로그 저장 정책이 위험을 증폭한다. |

---

## 6. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 대상 | 사용자 프롬프트, ICL 예시, RAG context, output, tool call argument, log |
| 공격자 목표 | 민감정보 유출, policy bypass, masking 우회, log leakage 유도 |
| 공격자 능력 | privacy-risk prompt 작성, 간접 식별자 포함, 우회 표현 사용, 반복 질의 |
| 공격 경로 | prompt/context → model input → output/tool/log → external exposure |
| 제외 범위 | 실제 개인정보 사용, 실제 API 대상 유출 실험, 무단 로그 접근 |

---

## 7. 평가방법 및 지표

| 지표 | 의미 | W04/P05에서의 활용 |
|---|---|---|
| Leakage Rate | 민감정보 출력 비율 | privacy 핵심 지표 |
| Masking Recall | 민감정보를 탐지·마스킹한 비율 | 방어 탐지력 |
| Masking Precision | 마스킹된 항목 중 실제 민감정보 비율 | 과마스킹 평가 |
| Utility | 정상 작업 품질 | 방어 후 사용성 |
| Over-refusal | 정상 요청 거절률 | 과차단 부작용 |
| Policy Compliance | 개인정보 정책 준수율 | 운영 통제 평가 |
| Latency | 마스킹·검사 지연 | 실시간 적용 가능성 |
| Auditability | 탐지·마스킹·출력 판단 로그 여부 | 사후 검증 가능성 |

---

## 8. 재현성 점검

| 항목 | 점검 |
|---|---|
| 데이터 | synthetic privacy-risk prompt만 사용. 실제 개인정보 제외 |
| 민감정보 유형 | 이름, 전화번호, 이메일, 주민번호형 패턴, 내부 문서명 등 toy pattern 정의 |
| 방어 | masking, rewriting, refusal, policy wrapper 조건 기록 |
| 평가 | leakage rate, masking precision/recall, utility, over-refusal 분리 |
| 로그 | 원본 민감값을 저장하지 않고 hash/placeholders 중심으로 기록 |
| 한계 | regex 기반 synthetic check 결과를 실제 LLM privacy guarantee로 해석하지 않음 |

---

## 9. 논문의 고유 기여

1. Prompt engineering과 ICL 환경에서의 privacy risk를 체계화했다.
2. Prompt masking, rewriting, policy control, privacy-preserving prompting을 비교할 수 있는 기준을 제공한다.
3. Leakage만이 아니라 utility와 over-refusal을 함께 평가해야 함을 보여준다.
4. W04와 W08의 prompt/RAG 보안 주제를 privacy 관점으로 연결하는 핵심 문헌이다.

---

## 10. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 최신 분야 | prompt privacy는 빠르게 변하므로 후속 문헌 보강 필요 | W07/W08 최신 LLM 보안 문헌과 연결한다. |
| 실제 데이터 사용 제한 | 개인정보를 실제로 넣고 실험하면 윤리·법적 위험이 있다. | synthetic prompt만 사용한다. |
| 탐지 한계 | regex/masking은 간접 식별자와 문맥 정보 누출을 놓칠 수 있다. | 한계와 false negative를 명시한다. |
| Utility 측정 어려움 | 마스킹 후 작업 품질 저하를 정량화하기 어렵다. | simple task utility와 human review 항목을 병기한다. |

---

## 11. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | 생성형 AI prompt에 민감정보가 포함되는 위험 제시 |
| 2장 관련연구 | privacy-preserving prompt engineering survey 정리 |
| 3장 위협모형 | prompt/context/output/log/tool call leakage 경로 정의 |
| 4장 연구방법 | leakage rate, masking precision/recall, utility, over-refusal 평가 설계 |
| 5장 분석 | synthetic privacy-risk prompt 실험 결과와 한계 제시 |
| 6장 보안적 함의 | 기밀성, 프라이버시, 책임성, 감사 가능성 해석 |

---

## 12. 기말논문 연결 3문장

1. 이 주차에서 기말논문에 반영할 개념: 프롬프트 보안은 입력 민감정보를 숨기는 문제뿐 아니라 context, output, tool call, log 전 과정의 leakage를 평가하는 문제다.
2. 이 주차에서 기말논문에 반영할 표·그림·실험: leakage rate 수식, masking function, privacy-utility score, 민감정보 유형별 평가표를 반영한다.
3. 이 주차가 RAG 문서 오염/LLM 보안 감사 프레임워크와 연결되는 지점: RAG 문서와 LLM 로그에도 민감정보가 포함될 수 있으므로 P05의 prompt privacy 지표를 W08 문서 출처 검증과 W14 감사 로그 설계로 확장한다.

---

## 13. 최종 판단

P05는 W04의 핵심 프라이버시 문헌이다. P04가 NLP robustness를 담당한다면, P05는 prompt privacy와 leakage/utility trade-off를 담당한다. 기말논문에서는 prompt 기반 AI 시스템의 민감정보 보호 평가체계의 핵심 관련연구로 사용한다.

---

## 14. 변환 호환성 메모

```bash
pandoc P05_summary.md -o P05_summary.docx
pandoc P05_summary.md -o P05_summary.pdf --pdf-engine=xelatex
```
