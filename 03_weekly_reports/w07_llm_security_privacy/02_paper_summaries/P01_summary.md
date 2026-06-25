# P01 Summary

## A Survey on Evaluation of Large Language Models — Yupeng Chang et al., ACM Transactions on Intelligent Systems and Technology, 2024

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W07 LLM 보안·프라이버시 |
| 논문명 | A Survey on Evaluation of Large Language Models |
| 저자 | Yupeng Chang et al. |
| 공식 출판 정보 | ACM Transactions on Intelligent Systems and Technology, Vol. 15, No. 3, Article 39, pp. 1–45, 2024 |
| DOI | https://doi.org/10.1145/3641289 |
| 로컬 PDF | `01_papers/pdf/01_Chang_et_al_2024_Evaluation_of_LLMs_Survey.pdf` |
| 검증 상태 | W07 `paper_list.md`와 `download_source.md` 기준 공식 DOI 확인. 강의계획서의 `J. Chang et al.` 및 ACM Computing Surveys 표기는 실제 확인 정보와 차이가 있어 메모 유지 |
| PDF 확인 메모 | repo의 PDF 폴더에 P01 관련 PDF blob이 존재함을 확인했다. 요약은 로컬 PDF 경로와 W07 `paper_list.md`, `download_source.md`의 공식 DOI 메타데이터 기준으로 보완했다. |
| 수식 호환성 | GitHub 수식 렌더링 오류 방지를 위해 `\operatorname`을 사용하지 않고 `\mathrm{...}` 형태로 작성했다. |
| 핵심 근거 사용 가능 여부 | 가능. W07에서 LLM evaluation taxonomy, benchmark contamination, hallucination, safety, robustness, privacy, human evaluation, LLM-as-a-judge, reproducibility evidence의 핵심 평가체계 문헌으로 사용 |

---

## 1. 한 문장 요약

이 논문은 대규모 언어모델 평가를 **knowledge, reasoning, coding, instruction following, alignment, safety, robustness, privacy, hallucination, factuality, bias, toxicity, human evaluation, automated evaluation, LLM-as-a-judge, benchmark contamination, reproducibility** 관점에서 체계화하며, W07에서는 LLM 보안·프라이버시 평가를 단일 benchmark 점수가 아니라 **성능·안전성·강건성·프라이버시·근거성·재현성**으로 분리해 측정해야 함을 보여주는 핵심 survey 문헌이다.

---

## 2. 핵심 연구문제

> LLM은 일반 NLP 모델보다 평가 대상이 넓다. 지식과 추론 능력이 높더라도 hallucination, privacy leakage, jailbreak, prompt injection, bias, toxic output, benchmark contamination이 남을 수 있다. 따라서 LLM 보안 평가는 task score와 별도로 safety, robustness, privacy, factuality, reproducibility evidence를 기록해야 한다.

| 번호 | 연구질문 |
|---|---|
| RQ1 | LLM 평가는 knowledge, reasoning, coding, language generation, instruction following, tool use를 어떻게 구분해야 하는가? |
| RQ2 | Benchmark score가 높더라도 hallucination, privacy leakage, jailbreak, bias, toxicity가 남는 이유는 무엇인가? |
| RQ3 | Automatic metric, human evaluation, LLM-as-a-judge는 각각 어떤 장단점과 평가 편향을 갖는가? |
| RQ4 | Benchmark contamination, hidden test leakage, leaderboard overfitting을 어떻게 통제해야 하는가? |
| RQ5 | W07의 LLM 보안·프라이버시 평가를 W08 RAG, W14 MLOps, W15 재현성 evidence chain으로 어떻게 확장할 수 있는가? |

---

## 3. 논문의 핵심 기여

| 기여 | 설명 | W07 연결 |
|---|---|---|
| LLM 평가 범위 정리 | 일반 능력, 지식, 추론, 코딩, instruction following, safety, robustness 등 평가축을 분리 | LLM 보안 평가표의 상위 구조 제공 |
| Benchmark taxonomy 제공 | 다양한 benchmark와 task 유형을 분류 | 평가 데이터 오염·과적합 위험 분석 |
| Human/automatic evaluation 비교 | 자동 지표, 사람 평가, LLM-as-a-judge의 장단점과 bias 논의 | 평가 신뢰성·책임성 연결 |
| Safety/robustness 평가 연결 | 일반 성능과 위험 조건 성능을 분리해야 함 | jailbreak, prompt injection, harmful response 평가 |
| 재현성 요구 강조 | model version, prompt, decoding config, judge rubric, raw output log 필요 | W14/W15 evidence chain으로 연결 |

---

## 4. 목차별 핵심 개괄

| 목차 | 핵심 내용 | 비전공자용 이해 |
|---|---|---|
| 1. Introduction | LLM의 능력과 위험이 커지면서 평가도 다차원 구조가 필요해졌다. | AI를 한 시험 점수로만 평가하면 위험하다. |
| 2. Evaluation Targets | 지식, 추론, 코딩, 생성, 지시 이행, 안전성, 강건성 등 평가 대상을 구분한다. | 과목별 시험처럼 능력을 나눠 본다. |
| 3. Benchmarks | MMLU류 지식 평가, reasoning, coding, QA, summarization, dialogue, multilingual benchmark를 정리한다. | 여러 시험지를 통해 모델 능력을 본다. |
| 4. Evaluation Methods | automatic metrics, human evaluation, pairwise comparison, LLM-as-a-judge를 비교한다. | 사람이 평가할 수도 있고, 다른 AI가 평가할 수도 있다. |
| 5. Reliability Problems | contamination, prompt sensitivity, decoding randomness, benchmark leakage, leaderboard gaming 문제가 있다. | 시험문제를 미리 봤다면 점수가 과장된다. |
| 6. Safety and Robustness | hallucination, toxicity, harmfulness, jailbreak, adversarial prompt, bias, privacy leakage 평가가 필요하다. | 똑똑해도 위험한 답을 하면 좋은 모델이 아니다. |
| 7. Domain Evaluation | 의료, 법률, 보안, 교육, RAG 등 domain-specific evaluation이 필요하다. | 실제 분야별로 위험 기준이 다르다. |
| 8. Open Challenges | 표준화 부족, 동적 benchmark, 평가 비용, human preference bias, 재현성 문제가 남는다. | 공정하고 반복 가능한 평가가 어렵다. |

---

## 5. 핵심 이론 및 수식

> 수식은 GitHub Markdown/KaTeX 호환성을 우선한다. `\operatorname` 매크로는 사용하지 않고 `\mathrm{...}` 형태로 작성한다.

### 5.1 Multi-Metric LLM Evaluation

LLM 평가는 하나의 점수가 아니라 여러 지표의 가중 결합으로 표현할 수 있다.

$$
Score_{LLM}=\sum_{k=1}^{K}w_k\cdot Metric_k
$$

| 기호 | 의미 |
|---|---|
| $Metric_k$ | 정확도, reasoning, safety, robustness, hallucination, privacy 등 개별 지표 |
| $w_k$ | 평가 목적별 가중치 |
| $K$ | 평가 지표 수 |

### 보안적 의미

LLM이 특정 benchmark에서 높은 점수를 받아도 안전한 모델이라는 뜻은 아니다. 보안 평가에서는 utility, hallucination, privacy leakage, jailbreak resistance, prompt injection resistance를 분리해야 한다.

---

### 5.2 Hallucination Rate

모델 응답 중 근거가 없거나 제공된 source와 불일치하는 응답 비율이다.

$$
HallucinationRate=\frac{N_{unsupported}}{N_{answers}}
$$

### 보안적 의미

환각은 단순 품질 문제가 아니라 보안 문제다. 보안관제, RAG, 법률, 의료, 정책 판단에서는 근거 없는 답변이 잘못된 의사결정과 책임소재 불명확성으로 이어질 수 있다.

---

### 5.3 Benchmark Contamination Risk

평가 데이터가 학습 데이터에 포함되었거나 모델이 benchmark 패턴을 사전에 접했을 가능성을 평가한다.

$$
ContaminationRisk=\frac{|D_{train}\cap D_{test}|}{|D_{test}|}
$$

| 기호 | 의미 |
|---|---|
| $D_{train}$ | 학습 또는 사전학습 데이터셋 |
| $D_{test}$ | 평가 데이터셋 |
| $D_{train}\cap D_{test}$ | 학습 데이터와 평가 데이터의 중복 영역 |

### 보안적 의미

평가 데이터 오염이 있으면 실제 능력보다 높은 성능을 보고할 수 있다. 최종 보고서에서는 contamination을 직접 계산하지 못하더라도 평가 데이터 출처와 한계를 명시해야 한다.

---

### 5.4 Safety-Utility Score

보안 평가에서는 유틸리티와 위험 지표를 함께 봐야 한다.

$$
SafetyUtilityScore=Utility-\lambda_1HallucinationRate-\lambda_2UnsafeRate-\lambda_3LeakageRate
$$

| 기호 | 의미 |
|---|---|
| $Utility$ | 정상 task 수행 성능 |
| $UnsafeRate$ | 유해·정책 위반 응답 비율 |
| $LeakageRate$ | 민감정보 노출 비율 |
| $\lambda_i$ | 위험 지표의 상대 가중치 |

### 보안적 의미

무조건 거절하는 모델은 안전해 보일 수 있지만 utility가 낮다. 반대로 utility만 높은 모델은 위험 응답을 낼 수 있다. Refusal quality와 over-refusal을 함께 기록해야 한다.

---

### 5.5 Jailbreak Attack Success Rate

위험 prompt가 안전 정책을 우회해 목표 응답을 얻은 비율이다.

$$
ASR_{jailbreak}=\frac{N_{policy\ bypass}}{N_{attack\ prompts}}
$$

### 보안적 의미

LLM 보안 평가에서는 단순 정확도보다 policy bypass 성공률이 중요하다. 단, 실제 악용 가능한 공격 절차를 상세 제공하지 않고 방어·평가 중심으로 제한해야 한다.

---

### 5.6 Privacy Leakage Rate

모델 응답에서 개인정보, 비밀정보, 내부 정보가 노출된 비율이다.

$$
LeakageRate=\frac{N_{leaked\ responses}}{N_{privacy\ risk\ prompts}}
$$

### 보안적 의미

Prompt, ICL example, RAG context, log에 포함된 민감정보가 출력으로 재노출될 수 있다. W04 P05 및 W08 RAG 보안과 직접 연결된다.

---

### 5.7 Citation Support Score

응답의 claim이 인용 source에 의해 뒷받침되는 정도다.

$$
CitationSupport=\frac{N_{claims\ supported}}{N_{claims}}
$$

### 보안적 의미

RAG/LLM 평가에서는 출처를 제시했다는 사실보다 claim이 실제 source와 일치하는지가 중요하다.

---

### 5.8 Reproducibility Coverage

평가 재현에 필요한 artifact가 얼마나 기록되었는지 측정한다.

$$
ReproCoverage=\frac{|Artifacts_{logged}|}{|Artifacts_{required}|}
$$

| 필수 artifact 예 | 설명 |
|---|---|
| model version | 모델명, provider, API snapshot |
| prompt | system/user prompt와 template |
| decoding config | temperature, top-p, max tokens, seed |
| benchmark version | dataset version, split, sampling rule |
| raw output | 원문 응답과 후처리 전 로그 |
| judge rubric | 사람 또는 LLM judge 평가 기준 |

---

## 6. LLM 평가 축 정리

| 평가 축 | 설명 | 대표 지표 | W07 보안 연결 |
|---|---|---|---|
| Knowledge | 사실 지식과 domain knowledge | QA accuracy, factuality | hallucination, citation support |
| Reasoning | 수리·논리·다단계 추론 | reasoning accuracy, chain validity | reasoning hallucination |
| Coding | 코드 생성·수정 능력 | pass@k, test pass rate | insecure code, secret leakage |
| Instruction Following | 지시 준수 능력 | task success, format compliance | system/user instruction conflict |
| Alignment/Safety | 정책·안전 기준 준수 | refusal quality, unsafe rate | jailbreak, harmful response |
| Robustness | 입력 교란·우회 표현 대응 | robust accuracy, ASR | prompt injection, adversarial prompt |
| Privacy | 민감정보 보호 | leakage rate, memorization risk | prompt privacy, data extraction |
| Reproducibility | 평가 재현 가능성 | prompt log, model version, seed | W14/W15 evidence chain |

---

## 7. 보안 이슈 30% 관점 분석

| 보안 항목 | LLM 평가 관점 해석 | 대표 평가 지표 |
|---|---|---|
| 기밀성 | prompt, ICL example, RAG context, output log에 민감정보 포함 가능 | LeakageRate, PII finding |
| 무결성 | prompt injection, benchmark contamination, cherry-picking이 평가와 출력을 왜곡 | ASR, contamination risk |
| 가용성 | 평가 비용과 latency가 높으면 지속적 red-team 평가가 어려움 | evaluation cost, latency |
| 프라이버시 | training data memorization과 context 재노출 위험 | privacy leakage, memorization signal |
| 안전성 | harmful output, hallucination, toxic/bias output 위험 | UnsafeRate, HallucinationRate |
| 책임성 | model version, prompt, judge rubric, raw output을 남겨야 감사 가능 | ReproCoverage, audit completeness |

---

## 8. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | 평가 데이터셋, hidden test set, prompt set, system prompt, retrieved context, model output, judge rubric, evaluation log |
| 공격자 목표 | benchmark gaming, 평가 점수 과장, hallucination 유도, safety policy 우회, 민감정보 추출 |
| 공격자 능력 | prompt 조작, benchmark pattern 학습, repeated query, indirect prompt injection, context stuffing, favorable subset 선택 |
| 공격 경로 | prompt/context 입력 → LLM 응답 생성 → judge/scoring → 점수 보고 또는 서비스 decision |
| 방어자 능력 | prompt set versioning, benchmark provenance, contamination check, human review, judge rubric, raw output logging |
| 제외 범위 | 실제 서비스 대상 jailbreak 실험, 민감정보 포함 prompt 사용, 비공개 benchmark 유출, 공격 절차 상세화 |

---

## 9. 평가방법 및 지표

| 지표 | 의미 | W07/P01에서의 활용 |
|---|---|---|
| Task Score | 정상 task 수행 성능 | utility baseline |
| HallucinationRate | 근거 없는 응답 비율 | factuality·RAG 평가 |
| CitationSupport | 응답이 source로 뒷받침되는 정도 | W08 RAG 연결 |
| UnsafeRate | 유해·정책 위반 응답 비율 | safety 평가 |
| RefusalQuality | 위험 요청을 적절히 거절하는 정도 | alignment 평가 |
| OverRefusal | 정상 요청까지 과도하게 거절하는 비율 | utility 손실 평가 |
| LeakageRate | 민감정보 노출 비율 | privacy 평가 |
| ASR_jailbreak | 공격 prompt 성공률 | robustness 평가 |
| HumanAgreement | 평가자 간 일치도 | human evaluation 신뢰성 |
| ReproCoverage | prompt/model/config/output 보존 정도 | W15 evidence chain |

---

## 10. 재현성 체크리스트

| 항목 | 기록해야 할 내용 |
|---|---|
| Bibliographic status | DOI, ACM TIST 출판정보, 강의계획서 표기 차이, 로컬 PDF 상태 |
| Model | 모델명, provider, version, API/로컬 여부, checkpoint |
| Prompt | system prompt, user prompt, retrieved context, prompt template |
| Decoding | temperature, top-p, max tokens, seed 가능 여부 |
| Evaluation data | benchmark 이름, version, split, 생성 방식, contamination 한계 |
| Judge | 사람 평가자, rubric, LLM judge 모델, judge prompt, 평가 기준 |
| Output | raw output, score, error case, hallucination case, refusal case |
| Security evaluation | ASR_jailbreak, LeakageRate, refusal/over-refusal, CitationSupport |
| Evidence | config file, result table, metric CSV/JSON, script commit, limitation note |
| GitHub math | `\operatorname` 사용 금지, `\mathrm{...}` 형태 사용 |

---

## 11. 논문의 고유 기여

1. LLM 평가를 능력 중심 benchmark에서 안전성·강건성·프라이버시·재현성까지 확장했다.
2. 단일 점수 대신 다중 평가축을 통해 모델의 실제 위험을 분리해 봐야 함을 정리했다.
3. Benchmark contamination과 evaluation reproducibility 문제를 LLM 평가의 핵심 위험으로 제시했다.
4. W07의 보안·프라이버시 평가표를 설계하는 상위 평가 프레임워크를 제공한다.
5. W08 RAG, W14 MLOps, W15 final evidence chain으로 연결되는 평가 방법론의 기반이 된다.

---

## 12. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 보안 전문 문헌은 아님 | LLM 보안·프라이버시 공격 자체보다는 평가 survey다. | W07 P02/P03 보안 문헌과 결합 |
| 공식 출판정보 차이 | 강의계획서 표기와 공식 DOI 메타데이터가 다르다. | DOI 기준 서지 사용, 차이 메모 유지 |
| Benchmark 빠른 노후화 | 공개 benchmark는 모델에 의해 빠르게 오염될 수 있다. | contamination 한계와 hidden/manual test 병기 |
| LLM-as-a-judge bias | 자동 judge는 특정 문체·모델·언어에 편향될 수 있다. | human review와 judge rubric 기록 |
| 단일 점수 착시 | 종합 점수가 safety/privacy 위험을 가릴 수 있다. | 지표 분리 보고 |
| 실험 윤리 | jailbreak/privacy prompt를 실제 민감정보로 실험하면 위험하다. | synthetic prompt와 방어 중심 평가로 제한 |

---

## 13. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | LLM 보안 평가는 단순 task score가 아니라 safety·privacy·factuality·reproducibility를 포함해야 한다는 문제의식 |
| 2장 관련연구 | P01을 LLM evaluation taxonomy의 핵심 문헌으로 정리 |
| 3장 위협모형 | benchmark, prompt, retrieved context, model output, judge rubric, evaluation log 보호 자산 정의 |
| 4장 연구방법 | Score_LLM, HallucinationRate, ContaminationRisk, SafetyUtilityScore, ASR_jailbreak, LeakageRate, ReproCoverage 지표 설계 |
| 5장 분석 | LLM evaluation axis table과 security/privacy metric matrix 제시 |
| 6장 보안적 함의 | benchmark gaming, hallucination, privacy leakage, jailbreak, over-refusal, judge bias 해석 |
| 부록 | prompt set, raw output, judge rubric, model/config log, limitation statement 수록 |

---

## 14. 기말논문 연결 3문장

1. W07에서 기말논문에 반영할 개념: LLM 보안 평가는 일반 task score와 별도로 hallucination, unsafe response, privacy leakage, jailbreak ASR, over-refusal, citation support를 분리해야 한다.
2. W07에서 기말논문에 반영할 표·그림·실험: LLM evaluation taxonomy, SafetyUtilityScore, ContaminationRisk, LeakageRate, ASR_jailbreak, ReproCoverage 수식표를 반영한다.
3. W07이 W15 최종 제출과 연결되는 지점: 모든 LLM 평가 결과는 model version, prompt, decoding config, benchmark version, raw output, judge rubric, limitation note를 evidence chain으로 남겨야 한다.

---

## 15. 최종 판단

P01은 W07의 LLM 평가체계 핵심 문헌이다. 직접적인 보안 공격·방어 survey는 아니지만, LLM 보안·프라이버시 논문을 평가할 때 어떤 지표를 분리해야 하는지 정의한다. 따라서 기말논문에서는 P01을 **LLM evaluation taxonomy, hallucination/safety/privacy/robustness 평가, benchmark contamination 통제, 재현성 evidence 설계의 중심 근거 문헌**으로 사용하는 것이 적절하다.

---

## 16. GitHub 수식 호환성 메모

이 파일에서는 GitHub 수식 렌더링 오류 방지를 위해 `\operatorname`을 사용하지 않는다.

| 피해야 할 표현 | 권장 표현 |
|---|---|
| `\operatorname{softmax}` | `\mathrm{softmax}` |
| `\operatorname{argmax}` | `\mathrm{argmax}` 또는 `\arg\max` |
| `\operatorname{sim}` | `\mathrm{sim}` |

```bash
pandoc P01_summary.md -o P01_summary.docx
pandoc P01_summary.md -o P01_summary.pdf --pdf-engine=xelatex
```
