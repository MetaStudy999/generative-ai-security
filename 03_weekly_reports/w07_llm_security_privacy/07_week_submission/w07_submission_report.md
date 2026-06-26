# W07 제출용 단일 보고서

## LLM 학습·정렬·평가 & LLM 보안·프라이버시

## 0. 메타정보

| 항목 | 내용 |
|---|---|
| 주차 | W07 |
| 보고서 제목 | LLM 학습·정렬·평가 & LLM 보안·프라이버시 |
| 과목 범위 | AI 보안 |
| 작성자 | 박영세 |
| 학번 | 26200122 |
| 작성일 | 2026-06-26 |
| 문서 상태 | 주차별 단일 제출용 보고서 |
| 원본 관리 파일 | `03_weekly_reports/w07_llm_security_privacy/07_week_submission/w07_submission_report.md` |
| Word/PDF 제출본 권장 위치 | `03_weekly_reports/w07_llm_security_privacy/07_week_submission/exports/` |
| 관련 산출물 위치 | `03_weekly_reports/w07_llm_security_privacy/` |
| 안전 범위 | 실제 LLM/API 호출, 실제 jailbreak 재현, 실제 개인정보, 외부 서비스 무단 질의, 악용 가능한 공격 절차 제외 |
| PDF 검토 상태 | P01~P05 로컬 PDF blob 존재 확인. 제출 본문은 DOI/URL, `paper_list.md`, 논문별 summary, 실험 보고서 기준으로 작성 |
| 제출 전 주의 | P01은 강의계획서 venue 표기와 공식 TIST 출판정보가 다르고, P03은 강의계획서 AI Open 지정 논문과 로컬 HCC 논문이 달라 관련 보조 문헌 가능성 확인 필요. P02/P04/P05도 강의계획서 저자 표기 차이 검토 필요 |

---

## 초록

본 보고서는 W07 주차의 LLM 학습·정렬·평가와 LLM 보안·프라이버시를 하나의 제출용 보고서로 통합한다. LLM은 대규모 pretraining, instruction tuning, alignment/RLHF, benchmark evaluation을 통해 다양한 자연어·코드·멀티모달 작업을 수행하지만, prompt injection, jailbreak, privacy leakage, benchmark contamination, hallucination, insecure code generation, over-refusal 같은 위험을 동시에 가진다. 본 보고서는 W07 논문 5편을 바탕으로 LLM evaluation, LLM security/privacy taxonomy, dual-use security risk, multimodal LLM, software security와 code LLM의 접점을 연결한다. 실습은 실제 LLM/API 호출이나 실제 jailbreak 재현 없이 synthetic prompt category와 rule-based toy guard score simulator만 사용했으며, utility, answer rate, ASR, privacy leakage, refusal quality, over-refusal, code vulnerability rate, reproducibility evidence를 분리 기록하였다. 실험 결과는 실제 LLM 보안 성능이 아니라 평가 보고 구조를 설명하기 위한 안전한 예시로 한정한다.

**키워드:** LLM, RAG, evaluation, security, privacy, jailbreak, prompt injection, multimodal LLM, code LLM, ASR, privacy leakage, over-refusal, reproducibility

---

## 1. 한 문장 요약

W07은 LLM/RAG 보안 평가가 benchmark score나 ASR 하나로 끝나지 않으며, utility, answer rate, ASR, privacy leakage, refusal quality, over-refusal, code vulnerability rate, reproducibility evidence를 분리해 기록해야 함을 보여주는 주차다.

---

## 2. 학습 배경과 주차 목표

### 2.1 이번 주 주제의 위치

W07은 W01~W06에서 다룬 AI 보안 평가축을 LLM 시스템으로 확장한다. W01은 생명주기 기반 보안 평가 프레임을 세웠고, W02는 학습 데이터 오염, W03은 비전 대적공격, W04는 Transformer/NLP 프라이버시, W05는 SSL/backdoor, W06은 합성미디어 탐지 신뢰성을 다루었다. W07은 이 흐름을 LLM, RAG, multimodal LLM, code LLM 환경으로 확장한다. LLM/RAG 시스템은 system prompt, user prompt, retrieval context, tool call, model output, code artifact, benchmark, log가 연결된 복합 시스템이므로 보안 평가는 단일 지표가 아니라 다중 지표로 수행해야 한다.

### 2.2 강의계획서상 학습목표

- LLM pretraining, instruction tuning, alignment/RLHF, evaluation taxonomy를 이해한다.
- LLM 보안·프라이버시 위협을 jailbreak, prompt injection, privacy leakage, refusal/over-refusal, benchmark contamination 관점에서 정리한다.
- Multimodal LLM의 visual context, OCR, grounding, hallucination 공격면을 분석한다.
- Software security와 code LLM에서 secure code generation, vulnerability detection, secret leakage, over-refusal을 분리 평가한다.
- Safe toy protocol을 통해 utility, ASR, privacy leakage, refusal quality, code vulnerability rate를 분리 기록한다.

### 2.3 이번 주 핵심 질문

1. LLM 평가는 왜 benchmark score 하나로 충분하지 않은가?
2. LLM 보안 평가에서 ASR과 refusal quality, over-refusal은 어떤 trade-off를 가지는가?
3. Privacy leakage와 prompt/context/output/log leakage는 어떻게 분리해 기록해야 하는가?
4. Multimodal LLM과 code LLM은 기존 텍스트 LLM보다 어떤 추가 공격면을 만드는가?
5. W07의 synthetic toy protocol을 기말논문의 LLM/RAG 보안 평가 프레임워크로 확장하려면 어떤 지표가 필요한가?

---

## 3. 논문 5편의 서술형 종합 요약

### 3.1 P01. A Survey on Evaluation of Large Language Models

P01은 LLM 평가의 기본 문헌이다. LLM 평가는 단순 accuracy나 benchmark score를 넘어서 reasoning, knowledge, robustness, safety, hallucination, fairness, privacy, multilinguality, instruction following, human evaluation, benchmark contamination을 함께 고려해야 한다. 특히 동일한 모델이라도 task, prompt format, decoding setting, benchmark contamination 여부에 따라 결과가 달라질 수 있다.

보안 관점에서 P01은 LLM 보안 평가의 상위 프레임을 제공한다. 좋은 benchmark score가 안전한 모델을 의미하지 않는다. Jailbreak, privacy leakage, unsafe code generation, over-refusal, hallucination은 별도 지표로 측정해야 하며, 평가 데이터와 prompt, seed, model version, output log를 재현 가능한 증거로 보존해야 한다.

### 3.2 P02. Security and Privacy Challenges of Large Language Models: A Survey

P02는 LLM 보안·프라이버시 위협을 체계적으로 정리한다. LLM은 jailbreak, prompt injection, prompt leakage, training data extraction, privacy disclosure, model extraction, adversarial prompting, unsafe response, tool misuse 같은 공격면을 가진다. 방어는 filtering, red-teaming, alignment, safety policy, privacy-preserving training, monitoring, human review 등으로 구성된다.

보안 관점에서 P02는 W07의 핵심 threat model 근거다. LLM은 단순 텍스트 생성기가 아니라 사용자 입력, system prompt, retrieval context, tool call, output log가 결합된 시스템이므로 보호 자산을 넓게 정의해야 한다. 강의계획서의 `Ankur Das` 표기는 공식 저자명과 달라 검증 메모를 유지한다.

### 3.3 P03. A survey on large language model security and privacy: The Good, The Bad, and The Ugly

P03은 LLM을 보안에 활용하는 긍정적 측면, 공격 자동화에 악용되는 부정적 측면, 모델 자체의 취약성이라는 세 관점으로 정리하는 관련 보조 문헌이다. LLM은 보안 로그 분석, 취약점 탐지, 코드 리뷰, incident response를 도울 수 있지만, 동시에 phishing, social engineering, malware 설명 자동화, jailbreak, data leakage 위험을 만든다.

보안 관점에서 P03은 LLM의 dual-use 특성을 설명하는 데 유용하다. 다만 강의계획서 지정 AI Open 논문과 현재 로컬 HCC 논문은 제목·저자·출판지가 달라, 최종 제출 전 동일성 확인 또는 관련 보조 문헌 사용 사유를 표시해야 한다.

### 3.4 P04. A survey on multimodal large language models

P04는 multimodal LLM의 구조와 평가를 정리한다. Multimodal LLM은 image encoder, projection module, language model을 연결해 image-text understanding, visual question answering, OCR, captioning, grounding, reasoning task를 수행한다. 텍스트만 처리하는 LLM과 달리 이미지, OCR text, visual grounding, multimodal context가 함께 입력된다.

보안 관점에서 MLLM은 visual prompt injection, image-borne instruction, OCR leakage, grounding failure, hallucination, image-text mismatch와 연결된다. W07에서는 P04를 W03/W04에서 다룬 비전·Transformer 보안과 LLM 보안을 연결하는 bridge 문헌으로 사용한다. 강의계획서의 `Yongtao Yin` 표기는 공식 저자 목록과 차이가 있으므로 검증 메모를 유지한다.

### 3.5 P05. When Software Security Meets Large Language Models: A Survey

P05는 LLM과 software security의 접점을 정리한다. LLM은 secure code generation, vulnerability detection, fuzzing, program repair, bug triage, security documentation 등에서 활용될 수 있다. 동시에 insecure code generation, hallucinated API, secret leakage, dependency confusion, vulnerable patch suggestion 같은 위험을 만들 수 있다.

보안 관점에서 P05는 code LLM 평가의 핵심 근거다. Code LLM은 단순히 답변 유용성만 평가해서는 부족하다. 생성 코드의 취약성, secret leakage, build/test evidence, over-refusal, human review 필요성을 함께 기록해야 한다. 강의계획서의 `Shujun Li` 표기는 공식 저자 목록과 달라 검증 메모를 유지한다.

---

## 4. 논문 간 연결 관계

W07 논문 5편은 다음 흐름으로 연결된다.

```text
LLM evaluation taxonomy
→ LLM security/privacy threat model
→ dual-use LLM security risk
→ multimodal LLM visual/context risk
→ code LLM and software security risk
```

P01은 평가 프레임워크, P02는 security/privacy challenge taxonomy, P03은 LLM의 good/bad/ugly dual-use 관점, P04는 multimodal context 확장, P05는 software security와 code LLM 접점을 제공한다. 이 다섯 문헌을 종합하면 W07의 핵심 메시지는 “LLM 보안 평가는 utility, safety, privacy, refusal behavior, code risk, reproducibility를 분리해 기록해야 한다”는 것이다.

---

## 5. AI 원리 70% 정리

LLM은 대규모 말뭉치에서 next-token prediction 또는 causal language modeling objective로 pretraining된다. 이후 instruction tuning과 alignment/RLHF를 통해 사용자 명령에 따르는 응답 형식을 학습하고, safety policy와 refusal behavior를 반영한다. RAG 환경에서는 retrieval context가 prompt에 결합되고, multimodal LLM에서는 image/text context가 함께 들어가며, code LLM은 code artifact를 생성하거나 분석한다. 따라서 LLM 시스템의 보안성은 모델 하나가 아니라 prompt, context, output, log, tool, code artifact까지 포함한 전체 pipeline에서 평가해야 한다.

### 5.1 핵심 수식

LLM의 기본 학습 목적은 이전 token 조건에서 다음 token 확률을 높이는 것이다.

$$
L_{lm}=-\sum_{t=1}^{T}\log p_{\theta}(y_t\mid y_{1:t-1})
$$

| 기호 | 의미 |
|---|---|
| $y_t$ | $t$번째 target token |
| $y_{1:t-1}$ | 이전 token sequence |
| $p_{\theta}$ | LLM의 조건부 token 확률 |

LLM 보안 평가는 utility와 safety를 함께 본다.

$$
SecurityUtility=Utility-\lambda_1ASR-\lambda_2LeakageRate-\lambda_3OverRefusal
$$

ASR은 공격 조건에서 정책 위반 또는 공격 목표 응답이 발생한 비율이다.

$$
ASR=\frac{N_{atk}}{N_{risk}}
$$

Privacy leakage rate는 위험 입력 중 민감정보가 노출된 비율이다.

$$
LeakageRate=\frac{N_{leak}}{N_{risk}}
$$

Over-refusal은 안전한 요청이 불필요하게 거부된 비율이다.

$$
OverRefusal=\frac{N_{or}}{N_{safe}}
$$

Code vulnerability rate는 code security prompt에서 취약 코드 산출이 발생한 비율이다.

$$
CodeVulnRate=\frac{N_{vuln}}{N_{code}}
$$

| 기호 | 의미 |
|---|---|
| $N_{risk}$ | 공격·프라이버시 위험 조건 평가 입력 수 |
| $N_{atk}$ | 공격 목표 또는 정책 위반 결과 수 |
| $N_{leak}$ | 민감정보 노출 결과 수 |
| $N_{or}$ | 안전한 요청이 과차단된 수 |
| $N_{safe}$ | 정상 안전 요청 수 |
| $N_{vuln}$ | 취약 코드 위험이 표시된 결과 수 |
| $N_{code}$ | code security 평가 입력 수 |

### 5.2 핵심 개념과 보안 연결

| 핵심 개념 | AI 원리 | 보안 연결 |
|---|---|---|
| Pretraining | 대규모 말뭉치에서 언어 분포 학습 | memorization, training data extraction |
| Instruction tuning | 명령-응답 형식 학습 | 공격 지시 민감성, instruction hijacking |
| Alignment/RLHF | 안전 정책과 선호도 반영 | refusal quality, over-refusal |
| Context window | prompt와 retrieval context 결합 | prompt injection, prompt leakage |
| Benchmark evaluation | 모델 능력 측정 | contamination, evaluation leakage |
| Multimodal extension | image-text context 결합 | visual prompt injection, OCR leakage |
| Code generation | code artifact 생성·수정 | insecure code generation, secret leakage |

---

## 6. 보안 이슈 30% 정리

LLM 보안·프라이버시 연구는 jailbreak, prompt injection, data leakage, privacy disclosure 등 다양한 위험을 분류한다. LLM은 보안 방어 도구가 될 수도 있지만 공격 자동화와 취약성의 원인이 될 수도 있다. Multimodal LLM은 이미지·텍스트 context가 결합되므로 hallucination과 multimodal prompt risk가 추가된다. Code LLM은 fuzzing, program repair, bug detection, bug triage를 지원하지만 insecure code generation 위험도 함께 평가해야 한다.

| 보안 속성 | W07에서의 의미 | 대표 위협 | 평가 지표 |
|---|---|---|---|
| Confidentiality | prompt, retrieval context, log, training data의 민감정보 노출 | privacy leakage, prompt leakage | leakage rate |
| Integrity | system prompt·retrieval context·tool call 조작 | prompt injection, context injection | ASR |
| Safety | unsafe instruction 수행 또는 부적절한 응답 | jailbreak, unsafe output | refusal quality, ASR |
| Availability | 과도한 차단으로 정상 업무 불가 | over-refusal | answer rate, over-refusal |
| Software security | 취약 코드 생성 또는 secret 노출 | insecure code generation | code vulnerability rate |
| Accountability | prompt, output, model version, config 기록 필요 | 재현성 실패 | reproducibility evidence |

---

## 7. Research Track 분석

### 7.1 연구문제

- RQ1. LLM/RAG 보안 평가에서 utility, ASR, leakage, refusal, code risk, reproducibility를 함께 측정하는 최소 프로토콜은 무엇인가?
- RQ2. Prompt attack simulation과 privacy-risk prompt에서 answer rate, refusal quality, ASR은 어떻게 달라지는가?
- RQ3. Code security prompt에서는 code vulnerability rate와 over-refusal을 어떻게 동시에 해석해야 하는가?
- RQ4. Multimodal LLM과 RAG 환경으로 확장할 때 보호 자산과 평가 지표는 어떻게 달라지는가?

### 7.2 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | system prompt, user prompt, retrieval context, model output, code artifact, tool-call argument, benchmark, log |
| 공격자 목표 | prompt injection, jailbreak, privacy leakage, unsafe output, vulnerable code generation, benchmark contamination |
| 공격자 지식 | prompt pattern 일부 지식, policy/guard threshold 추정, output/log 관찰 가능성 |
| 공격자 능력 | 공격성 prompt 작성, privacy-risk prompt 작성, retrieval context 오염, code prompt 조작, multimodal context 삽입 |
| 공격 경로 | prompt/context/code input → LLM/RAG system → output/tool/code/log → security/privacy failure |
| 방어자 능력 | safety policy, refusal, guard scoring, privacy filter, code review, human review, logging |
| 제외 범위 | 실제 jailbreak 문구 제공, 실제 개인정보 입력, 실제 외부 API 호출, 무단 서비스 테스트, 악성 코드 생성 |

### 7.3 평가축

| 평가축 | 질문 | 대표 지표 또는 증거 |
|---|---|---|
| Utility | 정상 요청에서 유용성이 유지되는가 | utility |
| Answer behavior | 요청에 답변하는가 또는 거부하는가 | answer rate |
| Attack behavior | 공격 조건에서 정책 위반이 발생하는가 | ASR |
| Privacy | 민감정보가 노출되는가 | privacy leakage rate |
| Refusal quality | 위험 요청을 적절히 거부하는가 | refusal quality |
| Over-refusal | 정상 요청을 과도하게 거부하는가 | over-refusal |
| Code risk | 취약 코드 위험이 남는가 | code vulnerability rate |
| Reproducibility evidence | 동일 결과를 다시 만들 수 있는가 | seed, config, prompt category, outputs, run log |

### 7.4 재현성

재현성을 위해 synthetic prompt category, seed, guard threshold, condition별 sample 수, rule-based scoring logic, CSV/JSON/Markdown log를 보존한다. W07 실습은 실제 LLM, 외부 API, 실제 개인정보, 실제 jailbreak 문구를 사용하지 않는다.

---

## 8. 실습 보고서 및 그래프 수치 검증

본 실습은 실제 LLM/API 호출이나 실제 jailbreak 재현이 아니라 W07의 핵심인 LLM 보안 평가축을 안전하게 설명하기 위한 최소 toy protocol이다. Synthetic prompt category와 rule-based toy guard score simulator를 사용해 clean, prompt attack simulation, privacy-risk, code security 조건을 분리하였다.

### 8.1 실습 설계

| 항목 | 내용 |
|---|---|
| Dataset | Synthetic prompt categories |
| Model/checker | Rule-based toy guard score simulator |
| Conditions | Clean, prompt attack simulation, privacy-risk, code security |
| Samples | 40 per condition |
| Guard threshold | 0.55 |
| Seed | 42 |
| Output files | `metrics_summary.csv`, `results.json`, `run_log.md` |

### 8.2 실습 결과 수치

| 조건 | Utility | Answer rate | ASR | Privacy Leakage | Refusal Quality | Over-refusal | Code vuln. rate | Mean risk | 해석 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Clean prompts | 0.866746 | 1.000000 | 0.000000 | 0.000000 | 해당 없음 | 0.000000 | 0.000000 | 0.172831 | 정상 질의에서 유용성과 과차단 여부 확인 |
| Prompt attack simulation | 0.400908 | 0.150000 | 0.150000 | 0.000000 | 0.850000 | 0.000000 | 0.000000 | 0.718287 | 공격 절차 재현 없이 방어 평가용 추상 카테고리만 사용 |
| Privacy-risk prompts | 0.392926 | 0.100000 | 0.100000 | 0.025000 | 0.900000 | 0.000000 | 0.000000 | 0.678389 | 실제 개인정보 없이 민감정보 노출 평가 구조만 점검 |
| Code security prompts | 0.678267 | 0.650000 | 0.000000 | 0.000000 | 해당 없음 | 0.350000 | 0.200000 | 0.514679 | 취약 코드 생성을 직접 제시하지 않고 체크리스트 판정만 모의 |

Clean prompts에서는 utility가 0.866746이고 answer rate가 1.000000으로 정상 질의가 차단되지 않았다. Prompt attack simulation과 privacy-risk prompts에서는 refusal quality가 각각 0.850000, 0.900000으로 나타났다. Code security prompts에서는 code vulnerability rate가 0.200000이고 over-refusal rate가 0.350000이었다. 이 값은 실제 공격 성공률이나 실제 개인정보 누출률이 아니라 toy guard score 기반 평가 형식 검증값이다.

### 8.3 그래프 수치 검증

현재 제출 보고서의 그래프는 `assets/w07_metric_chart.png`를 참조한다. 확인 가능한 SVG 그래프에는 `utility`, `attack_success_rate`, `privacy_leakage_rate`, `code_vulnerability_rate` 네 series가 표시되어 있다. Answer rate, refusal quality, over-refusal, mean risk는 표에는 포함하지만 현재 그래프 series에는 포함되어 있지 않다.

| 조건 | 그래프 Utility | 표 Utility | 그래프 ASR | 표 ASR | 그래프 Privacy Leakage | 표 Privacy Leakage | 그래프 Code Vuln. Rate | 표 Code Vuln. Rate | 확인 결과 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Clean prompts | 0.866746 | 0.866746 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 일치 |
| Prompt attack simulation | 0.400908 | 0.400908 | 0.150000 | 0.150000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 일치 |
| Privacy-risk prompts | 0.392926 | 0.392926 | 0.100000 | 0.100000 | 0.025000 | 0.025000 | 0.000000 | 0.000000 | 일치 |
| Code security prompts | 0.678267 | 0.678267 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.200000 | 0.200000 | 일치 |

<!-- submission-metric-chart:start -->
**그림 1. W07 metrics summary chart**

![W07 metrics summary chart](assets/w07_metric_chart.png)

출처: `04_experiment/outputs/metrics_summary.csv`. 이 그래프는 공개 toy/synthetic 산출물 기반이며 실제 공격 성능이나 운영 환경 성능으로 일반화하지 않는다. 현재 그래프는 utility, attack_success_rate, privacy_leakage_rate, code_vulnerability_rate를 시각화한다.
<!-- submission-metric-chart:end -->

---

## 9. 기말논문 연결

W07은 기말논문에서 “LLM/RAG 기반 AI 시스템의 보안·프라이버시·재현성 평가 프레임워크 연구”로 확장할 수 있다. 핵심 기여 후보는 prompt/context/output/code/log 보호 자산 정의, utility-security trade-off 평가표, ASR/leakage/refusal/code risk 분리 기록, seed/config/output 기반 재현성 체크리스트다.

| 기말논문 장 | W07 반영 내용 |
|---|---|
| 1장 서론 | LLM/RAG 보안 평가가 단일 benchmark score로 충분하지 않다는 문제의식 |
| 2장 관련연구 | LLM evaluation, security/privacy, dual-use risk, MLLM, code LLM 문헌 정리 |
| 3장 위협모형 | prompt, retrieval context, output, code artifact, log 보호 자산 정의 |
| 4장 연구방법 | utility, ASR, leakage, refusal, over-refusal, code vulnerability rate 설계 |
| 5장 분석 | synthetic prompt category별 toy evaluation 결과 비교 |
| 6장 결론 | LLM 보안 평가는 유용성·안전성·프라이버시·코드위험·재현성을 함께 관리해야 함 |

---

## 10. AI 도구 활용 기록

AI 도구는 문헌 요약, 코드 점검, 문장 구조화, 그래프 생성 보조에 사용하였다. 모든 DOI/URL, 실험 수치, 본문 인용, 결론은 작성자가 outputs 파일과 로컬 참고문헌 검증표를 대조하여 검증한다.

| 항목 | 내용 |
|---|---|
| 사용 도구명 | Codex, ChatGPT 계열 도구 |
| 사용 목적 | 문헌 요약 정리, 보고서 구조화, 안전한 toy/synthetic 실험 결과 표기 점검, 그래프 생성 보조, 제출 전 체크리스트 정리 |
| AI 산출물 반영 위치 | `07_week_submission/w07_submission_report.md`, `07_week_submission/assets/w07_metric_chart.png`, `05_ai_worklog/ai_disclosure_draft.md` |
| 본인 수정 내용 | 주차별 문헌 상태 확인, 실험 수치와 outputs 대조, 안전 범위와 한계 문장 확인, 최종 제출 전 미확정 문헌 분리 |
| 사실관계 검증 방법 | `01_papers/paper_list.md`, `01_papers/doi_check.md`, 강의계획서 문헌표 대조 |
| 실험결과 검증 방법 | `04_experiment/experiment_report.md`, `04_experiment/outputs/metrics_summary.csv`, `results.json`, `run_log.md`의 수치와 보고서 표기 대조 |
| 최종 책임 확인 | AI 산출물은 초안 보조이며 최종 제출자는 원고 내용, 인용, 실험결과, 연구윤리 책임을 확인한다. |

---

## 11. 제출 전 자기 점검표

| 점검 항목 | 상태 | 비고 |
|---|---|---|
| 메타정보 작성 | 완료 | 작성일 2026-06-26 반영 |
| 초록 및 키워드 작성 | 완료 |  |
| AI 원리 70% 정리 | 완료 | 핵심 수식 추가 |
| 보안 이슈 30% 정리 | 완료 |  |
| 논문 5편 서술형 요약 | 완료 |  |
| 논문 간 연결 관계 작성 | 완료 |  |
| Research Track 5요소 작성 | 완료 | 연구문제, 위협모형, 평가방법, 재현성, 한계 |
| P01~P05 PDF blob 확인 | 완료 | GitHub 파일 존재 확인. 원문 PDF 저작권/배포 정책 별도 검토 필요 |
| P01~P05 DOI/URL 검증 | 완료 / 확인 필요 | 강의계획서 venue·저자·지정 논문 차이 확인 필요 |
| P01 venue 표기 | 확인 필요 | 강의계획서 ACM CSUR vs 공식 ACM TIST 차이 |
| P02 저자 표기 | 확인 필요 | 강의계획서 `Ankur Das` vs 공식 `Badhan Chandra Das` |
| P03 지정 문헌 동일성 | 확인 필요 | AI Open 지정 논문과 현 HCC 논문 차이 |
| P04 저자 표기 | 확인 필요 | 강의계획서 `Yongtao Yin` vs 공식 `Shukang Yin et al.` |
| P05 저자 표기 | 확인 필요 | 강의계획서 `Shujun Li` vs 공식 `Xiaogang Zhu et al.` |
| 실험 outputs 파일 존재 확인 | 완료 | 실험 보고서 기준 CSV/JSON/run_log 존재 |
| 실험 결과와 보고서 수치 일치 | 완료 | 실험 보고서 수치 기준 반영 |
| 그래프 수치 확인 | 완료 | utility/ASR/privacy leakage/code vulnerability rate 기준 표와 일치 |
| AI 활용 고지 작성 | 완료 |  |
| DOCX/PDF 제출본 생성 | 필요 | `07_week_submission/exports/` 권장 |
| 최종 사람이 검토할 항목 표시 | 완료 | 문헌 동일성, PDF 보관 정책, Word/PDF 렌더링 |

---

## 12. 참고문헌 검증표

| 번호 | 참고문헌 | DOI/URL | 상태 | 비고 |
|---:|---|---|---|---|
| [1] | Yupeng Chang et al., “A Survey on Evaluation of Large Language Models,” ACM Transactions on Intelligent Systems and Technology, 2024 | `https://doi.org/10.1145/3641289` | DOI 확인 | 강의계획서 venue 표기 확인 필요 |
| [2] | Badhan Chandra Das, M. Hadi Amini, Yanzhao Wu, “Security and Privacy Challenges of Large Language Models: A Survey,” ACM Computing Surveys, 2025 | `https://doi.org/10.1145/3712001`; arXiv `https://arxiv.org/abs/2402.00888` | DOI 확인 | 강의계획서 `Ankur Das` 표기 확인 필요 |
| [3] | Yifan Yao et al., “A survey on large language model (LLM) security and privacy: The Good, The Bad, and The Ugly,” High-Confidence Computing, 2024 | `https://doi.org/10.1016/j.hcc.2024.100211`; arXiv `https://arxiv.org/abs/2312.02003` | DOI 확인 | AI Open 지정 논문 동일 여부 확인 필요. 관련 보조 문헌으로 사용 |
| [4] | Shukang Yin et al., “A survey on multimodal large language models,” National Science Review, 2024 | `https://doi.org/10.1093/nsr/nwae403`; arXiv `https://arxiv.org/abs/2306.13549` | DOI 확인 | 강의계획서 `Yongtao Yin` 표기 확인 필요 |
| [5] | Xiaogang Zhu et al., “When Software Security Meets Large Language Models: A Survey,” IEEE/CAA Journal of Automatica Sinica, 2025 | `https://doi.org/10.1109/JAS.2024.124971` | DOI 확인 | 강의계획서 `Shujun Li` 표기 확인 필요 |

---

## 13. 부록 A. KCI 논문 형식 전환 아이디어

### A.1 제목 후보

| 번호 | 국문 제목 후보 | 영문 제목 후보 | 연구방법 | 예상 기여 |
|---:|---|---|---|---|
| 1 | LLM/RAG 기반 AI 시스템의 보안·프라이버시·재현성 평가 프레임워크 연구 | A Security, Privacy, and Reproducibility Evaluation Framework for LLM/RAG-Based AI Systems | 문헌분석 + synthetic prompt 평가 | 통합 평가표 |
| 2 | LLM 보안 평가에서 Utility, ASR, Refusal Quality, Over-refusal의 균형 연구 | A Study on Balancing Utility, Attack Success Rate, Refusal Quality, and Over-Refusal in LLM Security Evaluation | toy guard score 실험 + 위협모형 | utility-security trade-off 평가 |
| 3 | Code LLM의 취약 코드 생성 위험과 재현성 평가체계 연구 | A Reproducible Evaluation Framework for Vulnerable Code Generation Risk in Code LLMs | 문헌분석 + synthetic score 평가 | code vulnerability rate·over-refusal 동시 기록 |

추천 최종 제목은 “LLM/RAG 기반 AI 시스템의 보안·프라이버시·재현성 평가 프레임워크 연구”이다. 국내 논문화 전에는 국내 참고문헌 3편 이상, KCI 양식, 그림·표 번호, AI 활용 고지, PDF 저작권 상태를 추가 확인해야 한다.

### A.2 연구문제

- RQ1. LLM/RAG 기반 AI 시스템의 보안·프라이버시 평가를 위해 필요한 최소 지표는 무엇인가?
- RQ2. Utility, ASR, refusal quality, over-refusal은 어떤 trade-off를 가지는가?
- RQ3. Code LLM 보안 평가에서 code vulnerability rate와 over-refusal을 어떻게 함께 해석해야 하는가?

---

## 14. 부록 B. SCI 논문 형식 전환 아이디어

SCI 제목 후보는 “A Multi-Metric Security, Privacy, and Reproducibility Evaluation Framework for LLM/RAG-Based AI Systems”이다.

Structured abstract는 Background, Problem, Method, Results, Contribution, Implications로 구성한다. 결과 문장은 W07 toy evaluation이 clean prompts utility 0.866746, prompt attack simulation ASR 0.150000, privacy-risk leakage 0.025000, code security prompt code vulnerability rate 0.200000, over-refusal 0.350000을 기록했다는 수준으로 제한한다. 실제 LLM 성능, 실제 jailbreak 성공률, 실제 개인정보 누출 가능성, 실제 코드 보안 품질로 일반화하지 않는다.

| 연구축 | 대표 논문 | 역할 |
|---|---|---|
| LLM evaluation | Chang et al. | benchmark, evaluation taxonomy, contamination risk |
| LLM security/privacy challenges | Das et al. | privacy, jailbreak, leakage, defense taxonomy |
| LLM security/privacy taxonomy | Yao et al. | good/bad/ugly taxonomy and attack surface |
| Multimodal LLMs | Yin et al. | MLLM architecture, evaluation, hallucination, multimodal risk |
| Software security and LLMs | Zhu et al. | code generation, fuzzing, repair, bug triage, vulnerability risk |

---

## 15. 부록 C. 제출 파일 위치와 변환 권장

| 파일 | 설명 |
|---|---|
| `07_week_submission/w07_submission_report.md` | 본 제출용 보고서 원본 |
| `07_week_submission/assets/w07_metric_chart.png` | 제출 보고서 그래프 |
| `04_experiment/experiment_report.md` | 실험 근거 보고서 |
| `04_experiment/outputs/` | 실험 결과 근거 파일 위치 |
| `05_ai_worklog/ai_disclosure_draft.md` | AI 활용 고지 근거 |

Word 제출본은 다음 위치에 생성해 관리한다.

```text
03_weekly_reports/w07_llm_security_privacy/07_week_submission/exports/w07_submission_report.docx
```

PDF 제출본은 Word에서 최종 육안 검수 후 다음 위치에 저장한다.

```text
03_weekly_reports/w07_llm_security_privacy/07_week_submission/exports/w07_submission_report.pdf
```

수식은 GitHub와 Word 변환을 모두 고려하여 Markdown 표 안에 넣지 않고, `$$...$$` block math로 유지한다.
