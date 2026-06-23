# W07 논문 5편 비교표

## 0. 문서 목적

이 문서는 W07 `P01_summary.md` ~ `P05_summary.md` 재생성 내용을 반영한 논문 비교표다. W07의 핵심 주제는 **LLM 평가체계, LLM 보안·프라이버시, dual-use governance, 멀티모달 LLM 보안, LLM 기반 소프트웨어 보안**이다.

---

## 1. 문헌 검증 및 역할 요약

| ID | 공식 확인 논문 | 공식 출판정보 | DOI/URL | 검증 상태 | W07 내 역할 |
|---|---|---|---|---|---|
| P01 | *A Survey on Evaluation of Large Language Models* | Yupeng Chang et al., ACM TIST 15(3), Article 39, 2024 | `https://doi.org/10.1145/3641289` | 공식 DOI 확인. 강의계획서의 `J. Chang` 및 ACM CSUR 표기 차이 메모 유지 | LLM 평가체계와 benchmark discipline |
| P02 | *Security and Privacy Challenges of Large Language Models: A Survey* | Badhan Chandra Das, M. Hadi Amini, Yanzhao Wu, ACM CSUR 57(6), 2025 | `https://doi.org/10.1145/3712001` | 공식 DOI 확인. 강의계획서의 `Ankur Das` 표기 차이 메모 유지 | LLM 보안·프라이버시 직접 핵심 문헌 |
| P03 | *A survey on large language model (LLM) security and privacy: The Good, The Bad, and The Ugly* | Yifan Yao et al., High-Confidence Computing 4(2), Article 100211, 2024 | `https://doi.org/10.1016/j.hcc.2024.100211` | 공식 DOI 확인. 강의계획서 지정 AI Open 논문과 달라 관련 보조 문헌 처리 | LLM dual-use, governance, 보안 활용/악용 균형 |
| P04 | *A survey on multimodal large language models* | Shukang Yin et al., National Science Review 11(12), Article nwae403, 2024 | `https://doi.org/10.1093/nsr/nwae403` | 공식 DOI 확인. 강의계획서의 `Yongtao Yin` 표기 차이 메모 유지 | 멀티모달 LLM 구조와 visual/OCR 보안 확장 |
| P05 | *When Software Security Meets Large Language Models: A Survey* | Xiaogang Zhu et al., IEEE/CAA Journal of Automatica Sinica 12(2), pp. 317–334, 2025 | `https://doi.org/10.1109/JAS.2024.124971` | 공식 DOI 확인. 강의계획서의 `Shujun Li` 표기 차이 메모 유지 | LLM 기반 소프트웨어 보안과 코드 보안 평가 |

---

## 2. 논문별 핵심 비교표

| 논문 | 연구문제 | 핵심 방법/분류 | AI 원리 기여 | 보안 위협 연결 | 핵심 평가 지표 | 한계/주의 | 기말논문 활용 |
|---|---|---|---|---|---|---|---|
| P01 | LLM을 어떤 능력·위험 축으로 평가할 것인가 | LLM evaluation taxonomy, benchmark survey, human evaluation | LLM 능력 평가를 knowledge, reasoning, instruction following, safety 등으로 분해 | benchmark contamination, hallucination, hidden test leakage, evaluation gaming | `Score_LLM`, `HallucinationRate`, `ContaminationRisk`, citation support, human agreement | 보안 전문 문헌은 아니며, 강의계획서 출판지 표기 차이 있음 | LLM/RAG 평가축, benchmark 오염 방지, W15 evidence chain |
| P02 | LLM 보안·프라이버시 공격과 방어는 어떻게 분류되는가 | prompt attack, jailbreak, leakage, poisoning, backdoor, defense taxonomy | LLM 학습·추론·배포 단계별 위험 구조화 | prompt injection, jailbreak, data leakage, memorization, model extraction, tool misuse | `ASR`, `LeakageRate`, `SecurityUtilityScore`, refusal quality, over-refusal, audit completeness | 실제 공격 절차가 아니라 synthetic/toy 평가로 제한해야 함 | W07 핵심 위협모형, W08 RAG injection, W11 privacy, W14 audit 연결 |
| P03 | LLM은 보안 도구이면서 동시에 어떤 악용·취약성을 만드는가 | Good/Bad/Ugly taxonomy, dual-use governance | LLM을 보안 도구·공격 도구·취약 시스템으로 동시에 해석 | offensive misuse, hallucinated security advice, sensitive log leakage, tool abuse | `Risk_LLM`, `DefenseCoverage`, `SecureAssistScore`, hallucination, unsafe suggestion rate | 강의계획서 지정 AI Open 논문과 달라 관련 보조 문헌으로 표기 | LLM 활용 범위, governance, human review, audit evidence 설계 |
| P04 | 멀티모달 LLM 구조와 보안 공격면은 어떻게 확장되는가 | visual encoder, projector, LLM backbone, instruction tuning, benchmark taxonomy | image/text/video/OCR 정보를 LLM context로 결합하는 구조 설명 | visual prompt injection, OCR injection, grounding failure, multimodal privacy leakage | `GroundingAcc`, `ASR_visual`, OCR leakage, alignment consistency, source traceability | 공격 전문 문헌은 아니므로 P02/P03/W08과 결합 필요 | PDF·이미지·표·스크린샷 RAG 입력 보안, visual provenance, OCR audit |
| P05 | LLM은 소프트웨어 보안 workflow에 어떻게 쓰이고 어떤 위험을 만드는가 | vulnerability detection, secure code generation, program repair, testing, code privacy | code LLM과 software security task 연결 | insecure code generation, flawed patch, secret leakage, dependency risk, tool misuse | `SecureCodeScore`, precision/recall/F1, `SecretLeakageRate`, vulnerability rate, build provenance | 악성코드·실제 취약점 악용 절차는 제외. toy/open-source code만 사용 | 코드·로그·CI/CD·도구 호출 보안 평가, W14 software supply chain 연결 |

---

## 3. 핵심 수식 비교

| ID | 수식/지표 | 용도 |
|---|---|---|
| P01 | `Score_{LLM}=Σ w_k Metric_k` | LLM 다중 평가 점수 |
| P01 | `HallucinationRate=N_unsupported/N_answers` | 근거 없는 응답 비율 |
| P01 | `ContaminationRisk=|D_train∩D_test|/|D_test|` | benchmark contamination 위험 |
| P02 | `ASR=(1/N)Σ 1[fθ(p_i^attack)∈Y_unsafe]` | jailbreak/prompt attack 성공률 |
| P02 | `LeakageRate=N_sensitive output/N_privacy risk prompts` | 민감정보 출력 비율 |
| P02 | `SecurityUtilityScore=Utility−λ₁ASR−λ₂LeakageRate−λ₃OverRefusal` | 보안성과 유용성 균형 |
| P03 | `Risk_LLM=w₁ASR+w₂LeakageRate+w₃MisuseRisk−w₄DefenseCoverage` | dual-use 위험 통합 평가 |
| P03 | `DefenseCoverage=|Controls_applied|/|Controls_required|` | 통제 적용 범위 |
| P04 | `h_v=Pφ(E_v(x_v))` | visual input을 LLM context로 변환하는 구조 |
| P04 | `ASR_visual=(1/N)Σ1[fθ(x_v^attack,x_text)∈Y_unsafe]` | visual jailbreak 평가 |
| P05 | `SecureCodeScore=Utility_code−λVulnRate−μLeakageRisk` | 안전한 코드 생성 평가 |
| P05 | `SecretLeakageRate=N_secret exposed/N_code prompts` | 코드·로그 기반 secret 노출 평가 |

---

## 4. W07 통합 위협모형

| 구분 | 보호 자산 | 공격자 목표 | 방어/통제 | 대표 지표 |
|---|---|---|---|---|
| 평가체계 | benchmark, hidden test, prompt set, judge log | benchmark gaming, evaluation leakage | benchmark provenance, contamination check, human review | contamination risk, human agreement |
| LLM 보안 | system prompt, user prompt, model output, tool credential | jailbreak, prompt injection, harmful output | guardrail, prompt isolation, monitoring | ASR, policy compliance |
| 프라이버시 | training data, fine-tuning data, user prompt, output log | memorization, sensitive leakage, data extraction | masking, access control, logging policy | leakage rate, refusal quality |
| Dual-use governance | security logs, vulnerability reports, automation tools | misuse, hallucinated security advice, tool abuse | human approval, audit log, tool permission | defense coverage, unsafe suggestion rate |
| 멀티모달 입력 | image, OCR text, visual embedding, document screenshot | visual prompt injection, grounding failure | OCR isolation, source labeling, human review | visual ASR, grounding accuracy |
| 소프트웨어 보안 | source code, secret, dependency, build log, CI/CD | insecure code, flawed repair, secret leakage | SAST, secret scan, code review, build provenance | vulnerability rate, secret leakage rate |

---

## 5. 평가 설계 매트릭스

| 평가 목적 | 반드시 포함할 지표 | 필요한 증거 | 연결 문헌 |
|---|---|---|---|
| LLM 기본 성능 평가 | task score, reasoning score, human agreement | benchmark version, prompt, raw output, judge rubric | P01 |
| LLM 안전성 평가 | ASR, unsafe rate, refusal quality, over-refusal | attack prompt set, refusal log, policy 기준 | P02 |
| 프라이버시 평가 | leakage rate, masking recall, output inspection | synthetic privacy prompt, detector rule, raw output | P02 |
| 보안 보조 활용 평가 | utility, hallucination rate, unsafe suggestion rate | synthetic log, human review, evidence chain | P03 |
| 멀티모달 평가 | VQA accuracy, grounding accuracy, visual ASR, OCR leakage | image hash, OCR result, visual prompt, output log | P04 |
| 코드 보안 평가 | test pass rate, vulnerability rate, precision/recall/F1, secret leakage | code snippet, SAST result, secret scan, commit hash | P05 |

---

## 6. 논문 간 차별성

| 논문 | 차별성 |
|---|---|
| P01 | LLM 평가의 상위 구조를 제공한다. 직접 공격 문헌은 아니지만, 보안 평가 지표를 배치하는 기준이 된다. |
| P02 | W07의 가장 직접적인 보안·프라이버시 taxonomy 문헌이다. prompt, data, model, output, tool, log를 공격면으로 정리한다. |
| P03 | LLM을 보안 도구와 공격 도구, 취약 시스템으로 동시에 보는 dual-use 관점을 제공한다. |
| P04 | text-only 보안 평가를 image, OCR, document, visual context가 포함된 multimodal security로 확장한다. |
| P05 | LLM 보안 평가를 소스코드, 취약점, 테스트, CI/CD, secret leakage까지 확장한다. |

---

## 7. 기말논문 활용 구조

| 기말논문 장 | W07 반영 내용 |
|---|---|
| 1장 서론 | LLM 보안은 단일 성능 문제가 아니라 utility, safety, privacy, robustness, auditability의 다중 평가 문제임을 제시 |
| 2장 관련연구 | P01 평가체계, P02/P03 보안·프라이버시, P04 멀티모달, P05 코드보안 문헌 정리 |
| 3장 위협모형 | prompt, context, model, output, tool, log, visual input, code artifact를 보호 자산으로 정의 |
| 4장 연구방법 | ASR, LeakageRate, HallucinationRate, GroundingAcc, SecretLeakageRate, DefenseCoverage를 평가 지표로 설계 |
| 5장 분석 | toy prompt/visual/code evaluation 결과를 실제 서비스 보증으로 과장하지 않고 한계와 함께 제시 |
| 6장 보안적 함의 | human review, access control, prompt-output-tool log, CI/CD gate, MLOps audit 필요성 논의 |

---

## 8. 최종 종합 판단

W07의 5개 문헌은 다음과 같이 연결된다.

```text
P01: 무엇을 평가할 것인가
→ P02: 어떤 LLM 보안·프라이버시 위협이 있는가
→ P03: LLM 활용은 어떤 dual-use governance가 필요한가
→ P04: 멀티모달 입력은 공격면을 어떻게 확장하는가
→ P05: 코드·도구·CI/CD 환경에서 LLM 보안은 어떻게 검증해야 하는가
```

따라서 W07은 W08 RAG/Prompt Injection, W11 Privacy, W14 MLOps, W15 Reproducibility를 연결하는 중심 주차다. 기말논문에서는 W07을 기준으로 **LLM/RAG 보안 평가 프레임워크의 다중지표 구조**를 설계하는 것이 적절하다.
