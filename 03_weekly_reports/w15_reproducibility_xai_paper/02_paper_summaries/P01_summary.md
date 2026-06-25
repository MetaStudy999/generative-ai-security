# P01 Summary

## A Survey on Evaluation of Large Language Models — Yupeng Chang et al., ACM Transactions on Intelligent Systems and Technology, 2024

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W15 Reproducibility, XAI & Final Paper Bridge |
| 논문명 | A Survey on Evaluation of Large Language Models |
| 저자 | Yupeng Chang et al. |
| 공식 출판 정보 | ACM Transactions on Intelligent Systems and Technology, Vol. 15, Issue 3, Article 39, 2024 |
| DOI | https://doi.org/10.1145/3641289 |
| 로컬 PDF | `01_papers/pdf/01_Chang_et_al_2024_Evaluation_of_LLMs_Survey.pdf` |
| 검증 상태 | W15 `doi_check.md`와 `paper_list.md` 기준 공식 DOI 확인. 원 프롬프트의 ACM Computing Surveys 표기와 다르고, 공식 metadata 기준 ACM Transactions on Intelligent Systems and Technology 논문으로 정리 |
| PDF 확인 메모 | repo의 PDF 폴더에 P01 관련 PDF blob이 존재함을 확인했다. 요약은 로컬 PDF 경로와 W15 `doi_check.md` 및 `paper_list.md`의 공식 DOI 메타데이터 기준으로 보완했다. |
| 핵심 근거 사용 가능 여부 | 가능. W15에서 LLM evaluation taxonomy, benchmark design, contamination risk, hallucination/safety/robustness 평가, human evaluation, reproducibility evidence, final paper evaluation protocol의 핵심 문헌으로 사용 |

---

## 1. 한 문장 요약

이 논문은 대형언어모델(LLM)의 평가를 **benchmark taxonomy, general ability, knowledge, reasoning, coding, alignment, safety, robustness, hallucination, calibration, human evaluation, automated judge, data contamination, prompt sensitivity, model versioning, reproducibility, leaderboard reliability** 관점에서 체계적으로 정리하며, W15에서 최종 논문의 LLM/RAG 보안 평가체계를 단일 점수 중심이 아니라 **성능·근거성·안전성·강건성·재현성·감사 가능성**으로 분리해 설계하는 핵심 문헌이다.

---

## 2. 핵심 연구문제

> LLM은 단순 분류 모델처럼 accuracy 하나로 평가하기 어렵다. 동일 모델도 prompt, decoding setting, benchmark contamination, evaluation rubric, judge model, model version에 따라 결과가 달라질 수 있다. 따라서 LLM/RAG 보안 연구에서는 task score뿐 아니라 hallucination, harmfulness, robustness, privacy, citation faithfulness, human agreement, raw output log까지 함께 보존해야 한다.

| 번호 | 연구질문 |
|---|---|
| RQ1 | LLM 평가는 knowledge, reasoning, coding, instruction following, safety, robustness, factuality, multilingual ability를 어떻게 구분해 측정해야 하는가? |
| RQ2 | Benchmark score는 contamination, prompt sensitivity, sampling randomness, model version change 때문에 얼마나 불안정해질 수 있는가? |
| RQ3 | Human evaluation과 automated LLM-as-a-judge 평가는 어떤 장단점과 bias를 갖는가? |
| RQ4 | RAG/LLM 보안 프레임워크에서는 hallucination, citation faithfulness, unsafe answer, privacy leakage, prompt injection robustness를 어떤 별도 지표로 기록해야 하는가? |
| RQ5 | 기말논문에서 평가 결과를 재현 가능하게 만들기 위해 prompt, model version, decoding config, raw output, judge rubric, evaluation script를 어떻게 evidence chain에 포함해야 하는가? |

---

## 3. 논문의 핵심 기여

| 기여 | 설명 | W15 연결 |
|---|---|---|
| LLM 평가 taxonomy | general capability, knowledge, reasoning, coding, alignment, safety, robustness 등 평가축 정리 | 최종 평가 프레임워크 |
| Benchmark 한계 분석 | contamination, leakage, leaderboard overfitting, prompt sensitivity, metric mismatch 문제 제시 | 재현성·허위 인용 방지 |
| Human/automatic evaluation 비교 | 사람 평가와 자동 judge의 신뢰도·비용·편향을 함께 다룸 | 평가 프로토콜 설계 |
| Safety/factuality 평가 강조 | hallucination, harmfulness, bias, toxicity, robustness 같은 위험 평가 필요성 제시 | AI 보안 평가축 |
| Reproducibility 요구 | model version, prompt, decoding, dataset, scoring script, raw output log의 기록 필요성 제시 | W15 evidence chain |

---

## 4. 목차별 핵심 개괄

| 목차 | 핵심 내용 | 비전공자용 이해 |
|---|---|---|
| 1. Introduction | LLM 성능이 빠르게 발전하면서 평가 기준도 단순 정확도에서 다차원 능력·위험 평가로 확장되었다. | LLM은 똑똑한지뿐 아니라 안전하고 근거 있게 답하는지도 봐야 한다. |
| 2. Evaluation Scope | 일반 지식, 추론, 수학, 코드, 언어 이해, instruction following, alignment, safety 등을 구분한다. | 시험 과목을 나누듯 LLM 능력도 여러 항목으로 나눠 평가한다. |
| 3. Benchmarks | MMLU류 지식 평가, reasoning/coding benchmark, QA, summarization, dialogue, multilingual benchmark를 정리한다. | 여러 시험지를 통해 모델의 다양한 능력을 측정한다. |
| 4. Evaluation Methods | automatic metric, human evaluation, pairwise comparison, LLM-as-a-judge, rubric-based scoring을 비교한다. | 사람이 평가할 수도 있고, 다른 AI가 평가하게 할 수도 있다. |
| 5. Reliability Problems | benchmark contamination, prompt sensitivity, decoding randomness, data leakage, leaderboard gaming 문제가 있다. | 시험문제가 학습 데이터에 섞이면 점수가 과장될 수 있다. |
| 6. Safety and Robustness | hallucination, harmful content, bias, toxicity, jailbreak, adversarial prompt, robustness 평가가 필요하다. | 정답률이 높아도 위험한 답을 하면 좋은 모델이 아니다. |
| 7. Domain and Application Evaluation | 의료, 법률, 교육, 보안, RAG 등 domain-specific evaluation이 필요하다. | 실제 분야별로 필요한 기준이 다르다. |
| 8. Open Challenges | 표준화 부족, hidden test set 관리, reproducibility, dynamic benchmark, human preference bias, cost 문제가 남는다. | 공정하고 재현 가능한 LLM 시험을 만드는 것이 어렵다. |
| 9. Future Directions | 투명한 evaluation protocol, contamination check, robust benchmark, multi-dimensional reporting, audit log가 필요하다. | 모델 점수뿐 아니라 평가 과정 전체를 남겨야 한다. |

---

## 5. 핵심 이론 및 수식

> 아래 수식은 LLM 평가와 W15 최종 논문 평가 프로토콜을 설명하기 위한 표준화된 표현이다. 수식은 GitHub, MS Word, PDF 변환 호환성을 위해 Markdown 표 밖의 LaTeX block math로 작성한다.

### 5.1 Multi-dimensional Evaluation Score

여러 평가축을 가중합으로 묶을 수 있지만, 실제 보고서에서는 세부 지표를 분리 병기해야 한다.

$$
EvalScore=\sum_{k=1}^{K}w_k Metric_k
$$

| 기호 | 의미 |
|---|---|
| $Metric_k$ | reasoning, factuality, safety, robustness, citation 등 개별 지표 |
| $w_k$ | 연구 목적에 따른 가중치 |

### 보안적 의미

단일 score는 위험하다. safety가 낮은 모델이 accuracy가 높다는 이유로 좋은 모델처럼 보일 수 있다.

---

### 5.2 Benchmark Contamination Risk

평가 데이터가 학습 데이터와 겹치는 정도를 측정한다.

$$
ContaminationRisk=\frac{|D_{train}\cap D_{test}|}{|D_{test}|}
$$

### 보안적 의미

contamination이 높으면 모델이 일반화 능력을 보인 것이 아니라 시험문제를 외웠을 가능성이 있다.

---

### 5.3 Hallucination Rate

답변 중 사실과 다르거나 근거 없는 내용을 포함한 비율이다.

$$
HallucinationRate=\frac{N_{unsupported\ or\ false\ answers}}{N_{answers}}
$$

### 보안적 의미

RAG/LLM 보안 연구에서는 hallucination이 잘못된 보안 판단, 허위 취약점, 허위 참고문헌, 잘못된 완화책으로 이어질 수 있다.

---

### 5.4 Citation Faithfulness

제시한 답변이 실제 retrieved evidence 또는 cited source에 의해 지지되는 정도다.

$$
CitationFaithfulness=\frac{N_{claims\ supported\ by\ cited\ evidence}}{N_{claims}}
$$

### 보안적 의미

출처를 달았다는 사실만으로 충분하지 않다. 각 claim이 실제 인용 근거와 일치해야 한다.

---

### 5.5 Safety Score

위험 답변을 줄이고 안전한 대체 응답을 제공하는 정도다.

$$
SafetyScore=1-\frac{N_{unsafe\ responses}}{N_{safety\ test\ cases}}
$$

### 보안적 의미

prompt injection, jailbreak, 악성코드 생성 요청, 개인정보 노출 요청 등에서 안전 응답 여부를 별도로 평가해야 한다.

---

### 5.6 Prompt Sensitivity

prompt 변형에 따라 성능이 얼마나 흔들리는지 측정한다.

$$
PromptSensitivity=\frac{1}{M}\sum_{j=1}^{M}|Score(p_j)-Score(p_0)|
$$

| 기호 | 의미 |
|---|---|
| $p_0$ | 기준 prompt |
| $p_j$ | 변형 prompt |

### 보안적 의미

prompt wording만 바꿔도 결과가 크게 바뀌면 평가 신뢰성이 낮다. prompt와 template을 evidence로 남겨야 한다.

---

### 5.7 Reproducibility Coverage

평가 재현에 필요한 구성요소가 얼마나 기록되어 있는지 평가한다.

$$
ReproCoverage=\frac{|Artifacts_{logged}|}{|Artifacts_{required}|}
$$

| 필수 artifact 예 | 설명 |
|---|---|
| model version | 모델명, 버전, API snapshot |
| prompt | system/user prompt와 template |
| decoding config | temperature, top-p, max tokens, seed |
| benchmark version | dataset version, split, sampling rule |
| raw output | 원문 응답과 post-processing 전 로그 |
| judge rubric | human/LLM judge scoring 기준 |
| scoring script | metric 계산 코드와 commit |

---

## 6. AI 원리 70% 관점 분석

| 원리 항목 | 설명 | W15/P01에서의 의미 |
|---|---|---|
| Benchmark | LLM 능력을 측정하는 평가 데이터셋 | 평가 기준 |
| Capability Evaluation | 지식·추론·코딩·언어 능력 평가 | 성능 평가축 |
| Alignment Evaluation | instruction following, helpfulness, harmlessness 평가 | 안전성 평가 |
| Factuality | 사실성·근거성 평가 | hallucination 관리 |
| Robustness | prompt 변형·adversarial prompt에 대한 안정성 | 보안 평가 |
| Human Evaluation | 사람이 rubric에 따라 평가 | 고비용·고신뢰 평가 |
| LLM-as-a-Judge | 다른 LLM으로 평가 자동화 | 비용 절감·bias 관리 필요 |
| Reproducibility | prompt/config/output/log를 남겨 재현 가능하게 함 | W15 핵심 |

---

## 7. 보안 이슈 30% 관점 분석

| 보안 항목 | LLM Evaluation 관점 해석 | 대표 평가 지표 |
|---|---|---|
| 기밀성 | 평가 prompt, hidden test set, benchmark answer key가 유출되면 평가가 왜곡 | hidden set leakage, access log |
| 무결성 | benchmark contamination, cherry-picking, score manipulation이 평가 무결성 훼손 | ContaminationRisk, protocol audit |
| 가용성 | 평가 비용이 높거나 judge가 불안정하면 지속 평가가 어려움 | evaluation cost, judge failure rate |
| 프라이버시 | 평가 데이터와 raw output에 개인정보 또는 민감 내용 포함 가능 | PII scan, retention policy |
| 안전성 | 높은 성능 모델도 harmful answer, hallucination, jailbreak에 취약할 수 있음 | SafetyScore, hallucination rate |
| 책임성 | 모델 버전, prompt, config, raw output, judge rubric을 남겨야 감사 가능 | ReproCoverage, evidence log completeness |

---

## 8. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | benchmark, hidden test set, answer key, prompt set, scoring script, judge rubric, raw output log, evaluation report |
| 공격자/위험 목표 | benchmark contamination, evaluation gaming, prompt cherry-picking, hidden test leakage, judge manipulation, 결과 과장 |
| 공격자/위험 능력 | training data에 benchmark 포함, prompt 반복 튜닝, favorable subset 선택, judge prompt 조작, metric 선택 편향 |
| 위험 경로 | benchmark 노출 또는 contamination → score 과장 → 안전성/근거성 평가 누락 → 잘못된 모델 선택 또는 논문 주장 과장 |
| 방어자 능력 | hidden test 관리, contamination check, prompt/version logging, multi-metric report, human review, raw output audit |
| 제외 범위 | 벤치마크 유출 방법, 평가 조작 절차, hidden set 탈취, judge 우회 prompt 제공 |

---

## 9. 평가방법 및 지표

| 평가축 | 지표 | 의미 | W15/P01 활용 |
|---|---|---|---|
| 일반 능력 | task accuracy, pass@k, exact match, F1 | 기본 성능 | baseline |
| 근거성 | CitationFaithfulness, support rate | 답변-근거 일치 | RAG 평가 핵심 |
| 환각 | HallucinationRate, unsupported claim rate | 허위 정보 비율 | 안전성 |
| 안전성 | SafetyScore, refusal correctness, harmfulness rate | 위험 응답 억제 | 보안 평가 |
| 강건성 | PromptSensitivity, adversarial prompt robustness | prompt 변형 안정성 | prompt injection 대응 |
| 오염 위험 | ContaminationRisk, duplicate overlap | 평가 신뢰성 | 재현성 |
| 평가 신뢰도 | human agreement, judge consistency | 평가자 신뢰도 | LLM-as-a-judge 관리 |
| 재현성 | ReproCoverage, raw output availability | 결과 재현 가능성 | W15 핵심 |

---

## 10. 재현성 체크리스트

| 항목 | 기록해야 할 내용 |
|---|---|
| Bibliographic status | DOI 기준 서지, 원 프롬프트의 ACM CSUR 표기 차이, 로컬 PDF 판본 상태 |
| Model | model name, provider, version, API date, parameter size if available |
| Prompt | system prompt, user prompt, retrieval prompt, prompt template, language |
| Decoding | temperature, top-p, max tokens, seed, stop sequence |
| Dataset | benchmark name, version, split, sampling rule, contamination check |
| RAG evidence | document corpus version, chunking, embedding model, retriever config, cited evidence |
| Output | raw answer, retrieved context, post-processing rule, refusal text |
| Judge | human/LLM judge, rubric, judge prompt, inter-rater agreement |
| Metrics | accuracy, HallucinationRate, CitationFaithfulness, SafetyScore, PromptSensitivity |
| Evidence | evaluation script commit, raw log hash, result table, error analysis, limitation note |

---

## 11. 논문의 고유 기여

1. LLM 평가를 능력 중심 benchmark에서 안전성·근거성·강건성·재현성까지 확장한다.
2. Benchmark contamination과 leaderboard overfitting의 위험을 강조해 평가 신뢰성을 보안 문제로 다룬다.
3. Human evaluation과 automated judge의 비용·신뢰도·편향 문제를 비교할 근거를 제공한다.
4. RAG/LLM 보안 연구에서 hallucination, citation faithfulness, safety, prompt robustness를 별도 지표로 설계해야 함을 뒷받침한다.
5. W15 최종 논문의 평가방법 장에서 raw output log와 evaluation evidence chain을 요구하는 핵심 근거 문헌이다.

---

## 12. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 표기 차이 | W15 DOI 표 기준 공식 출처는 ACM TIST이며, 원 프롬프트의 ACM CSUR 표기와 다르다. | DOI 기준으로 인용하고 표기 차이 메모 유지 |
| Benchmark 노후화 | 공개 benchmark는 빠르게 오염되고 모델이 과적합될 수 있다. | contamination check와 hidden/manual test 병행 |
| 단일 점수 착시 | EvalScore 하나로 모델 안전성을 설명하기 어렵다. | 성능·근거성·안전성·재현성 분리 보고 |
| Judge bias | LLM-as-a-judge는 특정 모델·문체·언어에 편향될 수 있다. | human review와 judge consistency 기록 |
| Domain mismatch | 일반 benchmark가 AI 보안/RAG 실무 위험을 충분히 반영하지 못한다. | 도메인별 보안 평가셋 설계 |
| Raw log 민감성 | 평가 raw output에 민감 정보가 포함될 수 있다. | PII scan과 log retention policy 추가 |

---

## 13. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | LLM/RAG 보안 평가는 성능뿐 아니라 안전성·근거성·재현성·오염 위험을 함께 봐야 한다는 문제의식 |
| 2장 관련연구 | P01을 LLM evaluation survey 핵심 문헌으로 정리 |
| 3장 위협모형 | benchmark, hidden test set, prompt set, raw output log, judge rubric 보호 자산 정의 |
| 4장 연구방법 | EvalScore, ContaminationRisk, HallucinationRate, CitationFaithfulness, SafetyScore, PromptSensitivity, ReproCoverage 지표 설계 |
| 5장 분석 | LLM/RAG evaluation protocol table과 benchmark contamination control matrix 제시 |
| 6장 보안적 함의 | 모델 점수 과장, evaluation gaming, hallucination, unsafe answer, judge bias, reproducibility evidence 필요성 해석 |

---

## 14. 기말논문 연결 3문장

1. W15에서 기말논문에 반영할 개념: LLM 평가는 task score 하나로 판단할 수 없으며, factuality, hallucination, safety, robustness, contamination, reproducibility를 분리해 기록해야 한다.
2. W15에서 기말논문에 반영할 표·그림·실험: EvalScore, ContaminationRisk, HallucinationRate, CitationFaithfulness, SafetyScore, PromptSensitivity, ReproCoverage 수식표와 LLM/RAG evaluation protocol table을 반영한다.
3. W15 최종 제출과 연결되는 지점: 모든 평가 결과는 model version, prompt, decoding config, benchmark version, raw output, judge rubric, scoring script commit을 evidence chain으로 남겨야 최종 논문의 재현성과 신뢰성을 확보할 수 있다.

---

## 15. 최종 판단

P01은 W15의 LLM/RAG 평가체계 핵심 문헌이다. 기말논문에서 모델이나 RAG 보안 프레임워크를 평가할 때 단일 점수로 결론을 내리면 안 되며, 성능·안전성·근거성·강건성·오염 위험·재현성 지표를 분리해야 한다. 따라서 P01은 **최종 논문의 평가방법, benchmark contamination 통제, hallucination/citation faithfulness 측정, raw output evidence chain 설계의 중심 근거 문헌**으로 사용하는 것이 적절하다.

---

## 16. 변환 호환성 메모

```bash
pandoc P01_summary.md -o P01_summary.docx
pandoc P01_summary.md -o P01_summary.pdf --pdf-engine=xelatex
```
