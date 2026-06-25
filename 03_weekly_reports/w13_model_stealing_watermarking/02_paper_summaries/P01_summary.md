# P01 Summary

## I Know What You Trained Last Summer: A Survey on Stealing Machine Learning Models and Defences — Daria/Daryna Oliynyk et al., ACM Computing Surveys, 2023

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W13 Model Stealing & Watermarking |
| 논문명 | I Know What You Trained Last Summer: A Survey on Stealing Machine Learning Models and Defences |
| 저자 | Daria/Daryna Oliynyk et al. |
| 공식 출판 정보 | ACM Computing Surveys, Vol. 55, Issue 14s, pp. 1–41, online 2023-07-17, print 2023-12-31 |
| DOI | https://doi.org/10.1145/3595292 |
| 보조 URL | arXiv `2206.08451` |
| 로컬 PDF | `01_papers/pdf/01_Oliynyk_Mayer_Rauber_2023_Model_Stealing_Survey.pdf` |
| 검증 상태 | W13 `paper_list.md` 기준 공식 DOI 확인. 제목은 `Defences` 표기이며 로컬 PDF는 VOR가 아닌 accepted/arXiv 계열 메타데이터 포함 |
| PDF 확인 메모 | repo의 PDF 폴더에 P01 관련 PDF blob이 존재함을 확인했다. 요약은 로컬 PDF 경로, download source 기록, W13 `paper_list.md`의 공식 DOI 메타데이터 기준으로 보완했다. |
| 핵심 근거 사용 가능 여부 | 가능. W13에서 model stealing, model extraction, black-box query attack, surrogate model, fidelity, query budget, extraction cost, API monitoring, watermarking defense의 핵심 survey 문헌으로 사용 |

---

## 1. 한 문장 요약

이 논문은 machine learning model stealing을 **black-box API query, model extraction, functionality stealing, surrogate model training, decision boundary approximation, confidence/logit leakage, query budget, extraction cost, fidelity, stolen model accuracy, transferability, IP infringement, API abuse monitoring, output restriction, watermarking, fingerprinting, legal/operational defences** 관점에서 체계화하며, W13에서 AI 모델을 단순 소프트웨어가 아니라 **복제·추출·소유권 분쟁의 대상이 되는 지식재산 보안 자산**으로 정의하는 중심 문헌이다.

---

## 2. 핵심 연구문제

> 상용 ML/AI 모델은 API 형태로 공개될수록 유용성이 높아지지만, 공격자가 반복 질의와 출력 관찰만으로 모델의 기능, decision boundary, confidence behavior, sometimes architecture-level behavior를 복제할 수 있다. 따라서 모델 제공자는 사용성·비즈니스 접근성과 IP 보호·오남용 탐지 사이에서 어떤 보안 통제를 설계해야 하는가?

| 번호 | 연구질문 |
|---|---|
| RQ1 | 공격자는 black-box API 질의만으로 victim model의 기능을 어느 정도 복제할 수 있는가? |
| RQ2 | Model stealing 공격의 성공은 fidelity, stolen accuracy, transferability, query budget, extraction cost로 어떻게 평가되는가? |
| RQ3 | Confidence score, logit, probability vector, label-only output은 model extraction 난이도에 어떤 차이를 만드는가? |
| RQ4 | Rate limiting, output restriction, query monitoring, watermarking, fingerprinting, legal notice는 어떤 방어 효과와 한계를 갖는가? |
| RQ5 | LLM/RAG 서비스에서는 모델 자체뿐 아니라 prompt, retrieval index, embedding space, document ranking policy도 추출 대상이 될 수 있는가? |

---

## 3. 논문의 핵심 기여

| 기여 | 설명 | W13 연결 |
|---|---|---|
| Model stealing taxonomy | 모델 추출·기능 복제·파라미터 추정·decision boundary stealing 등 공격 유형 정리 | W13 핵심 공격 분류 |
| Threat model 체계화 | black-box, gray-box, white-box, confidence/logit access, label-only query 조건을 분리 | API 보안 위협모형 설계 |
| 평가 지표 정리 | fidelity, stolen accuracy, query budget, extraction cost, agreement rate, transferability 등 제시 | W13 metric 설계 |
| Defence taxonomy | rate limit, output restriction, perturbation, monitoring, watermark, fingerprint, legal/contractual 대응 정리 | P02~P04 watermarking 연결 |
| IP·운영 보안 연결 | 모델은 학습비용과 데이터·노하우가 축적된 IP 자산이므로 기술·정책·감사를 함께 고려해야 함 | 기말논문 AI 보안 감사 프레임워크 연결 |

---

## 4. 목차별 핵심 개괄

| 목차 | 핵심 내용 | 비전공자용 이해 |
|---|---|---|
| 1. Introduction | MLaaS와 API 기반 AI 서비스가 확산되면서 모델 자체가 공격·복제·IP 침해 대상이 되었다. | AI 모델도 프로그램처럼 훔치거나 복제할 수 있다. |
| 2. Model Stealing Background | 학습된 모델, API query, prediction output, confidence score, surrogate training, extraction attack 개념을 설명한다. | 공격자는 모델에 여러 질문을 던지고 답을 모아 비슷한 모델을 만든다. |
| 3. Attack Taxonomy | equation-solving, path-finding, decision boundary approximation, synthetic query generation, active learning, knowledge distillation 기반 공격을 분류한다. | 질문을 똑똑하게 골라 모델의 경계와 기능을 베끼는 방법들이다. |
| 4. Threat Models | label-only, probability-vector, logits, confidence score, partial information, query-limited setting 등 공격자 접근권한을 구분한다. | 모델이 확률값을 많이 줄수록 공격자가 더 쉽게 베낄 수 있다. |
| 5. Evaluation Metrics | fidelity, stolen model accuracy, agreement, query budget, cost, transferability, attack success를 평가한다. | 훔친 모델이 원래 모델과 얼마나 똑같이 행동하는지와 비용을 함께 본다. |
| 6. Defences | output rounding, confidence masking, rate limiting, anomaly detection, watermarking, fingerprinting, legal/contractual constraints를 정리한다. | 답변 정보를 줄이고, 비정상 질의를 감시하고, 소유권 표식을 심는 방식으로 방어한다. |
| 7. Limitations | 강한 방어는 API 유용성을 낮추고, adaptive attacker는 탐지를 우회할 수 있다. | 너무 막으면 서비스가 불편해지고, 공격자는 더 조심스럽게 훔칠 수 있다. |
| 8. Future Directions | foundation model, LLM API, generative model, watermarking, audit logging, governance가 향후 과제다. | 큰 AI 모델과 RAG 서비스에서는 모델뿐 아니라 프롬프트와 인덱스도 보호해야 한다. |
| 9. Conclusion | 모델 공개성과 IP 보호 사이의 균형이 필요하며, 기술적 방어와 운영 감사를 결합해야 한다. | AI 서비스는 성능뿐 아니라 모델 도난 방지 체계를 갖춰야 한다. |

---

## 5. 핵심 이론 및 수식

> 아래 수식은 model stealing 평가와 W13 API 보안 보고서의 metric 설계를 설명하기 위한 표준화된 표현이다. 실제 공격 자동화 절차가 아니라 방어·감사 평가 지표 중심으로 정리한다.

### 5.1 Model Fidelity

Victim model과 stolen/surrogate model의 예측 일치율이다.

$$
Fidelity=\frac{1}{N}\sum_{i=1}^{N}\mathbf{1}[f_{victim}(x_i)=f_{stolen}(x_i)]
$$

| 기호 | 의미 |
|---|---|
| $f_{victim}$ | 보호 대상 원본 모델 |
| $f_{stolen}$ | 공격자가 학습한 복제 모델 |
| $x_i$ | 평가 입력 |

### 보안적 의미

Fidelity가 높으면 stolen model이 원본 모델의 decision behavior를 잘 복제했다는 뜻이다. 정확도보다 원본과의 일치율이 model stealing 평가의 핵심일 수 있다.

---

### 5.2 Stolen Model Utility

복제 모델이 실제 task에서 어느 정도 성능을 내는지 측정한다.

$$
Acc_{stolen}=\frac{1}{N}\sum_{i=1}^{N}\mathbf{1}[f_{stolen}(x_i)=y_i]
$$

### 보안적 의미

공격자가 원본과 100% 동일하지 않아도 충분한 utility를 얻으면 비즈니스·IP 피해가 발생할 수 있다.

---

### 5.3 Extraction Cost

질의 수와 단가를 곱해 공격 비용을 추정한다.

$$
ExtractionCost=N_{queries}\cdot Cost_{query}
$$

| 기호 | 의미 |
|---|---|
| $N_{queries}$ | API 질의 수 |
| $Cost_{query}$ | 질의 1회당 비용 |

### 보안적 의미

방어는 공격 비용을 높여야 한다. 공격 비용이 모델 개발비보다 훨씬 낮다면 모델 추출 경제성이 생긴다.

---

### 5.4 Query Efficiency

공격자가 질의 1회당 얻는 복제 성능 향상이다.

$$
QueryEfficiency=\frac{Fidelity}{N_{queries}}
$$

### 보안적 의미

높은 query efficiency는 적은 질의로도 모델 행동을 잘 복제한다는 뜻이다. API monitoring은 질의 수뿐 아니라 질의 패턴과 효율성도 봐야 한다.

---

### 5.5 Agreement Gap

복제 모델과 victim model의 불일치 정도다.

$$
AgreementGap=1-Fidelity
$$

### 보안적 의미

AgreementGap이 낮을수록 stolen model이 원본과 거의 같은 decision service를 제공할 수 있다.

---

### 5.6 Detection Rate

방어자가 model stealing 의심 질의를 탐지한 비율이다.

$$
DetectionRate=\frac{TP}{TP+FN}
$$

| 기호 | 의미 |
|---|---|
| $TP$ | 실제 추출 공격을 탐지한 경우 |
| $FN$ | 추출 공격을 놓친 경우 |

### 보안적 의미

DetectionRate만 높고 FPR이 높으면 정상 사용자를 차단할 수 있다. 탐지 성능은 FPR, latency, user friction과 함께 봐야 한다.

---

### 5.7 API Abuse Risk Score

API 기반 모델 추출 위험을 요약하는 지표다.

$$
Risk_{steal}=\alpha Fidelity+\beta QueryEfficiency+\gamma OutputRichness-\lambda DetectionCoverage
$$

| 기호 | 의미 |
|---|---|
| $OutputRichness$ | label, probability, logit 등 출력 정보량 |
| $DetectionCoverage$ | API monitoring과 watermark/fingerprint 검증 범위 |

### 보안적 의미

출력 정보가 풍부하고 탐지 범위가 낮으면 model stealing 위험이 커진다.

---

## 6. AI 원리 70% 관점 분석

| 원리 항목 | 설명 | W13/P01에서의 의미 |
|---|---|---|
| Model Extraction | API 질의로 모델 기능 복제 | W13 핵심 공격 |
| Surrogate Model | victim model을 모방해 학습한 대체 모델 | stealing 결과물 |
| Black-box Query | 내부 파라미터 없이 입력·출력만 관찰 | 현실적 API 공격 조건 |
| Confidence/Logit Output | 확률·logit 등 풍부한 출력 | 공격 정보량 증가 |
| Active Query Selection | 정보를 많이 얻는 질의 선택 | query efficiency 증가 |
| Fidelity | victim과 stolen model의 예측 일치 | 모델 도난 평가 핵심 |
| Query Budget | 공격자가 사용할 수 있는 질의 수 | 비용·탐지 기준 |
| Watermark/Fingerprint | 소유권 검증 또는 추출 탐지 | P02~P04 연결 |

---

## 7. 보안 이슈 30% 관점 분석

| 보안 항목 | Model Stealing 관점 해석 | 대표 평가 지표 |
|---|---|---|
| 기밀성 | 모델 파라미터, decision boundary, confidence behavior가 노출될 수 있음 | output richness, query log exposure |
| 무결성 | stolen model이 원본과 유사한 의사결정을 제공해 IP·서비스 신뢰를 침해 | fidelity, agreement gap |
| 가용성 | 강한 rate limit/output restriction이 정상 API 유용성을 낮출 수 있음 | FPR, user friction, latency |
| 프라이버시 | 모델 추출 과정에서 training data 특성이 간접 노출될 수 있음 | membership leakage, confidence leakage |
| 안전성 | 추출된 surrogate model이 adversarial attack 준비나 방어 우회에 활용될 수 있음 | transferability, attack reuse risk |
| 책임성 | 소유권·방어·탐지 근거를 남겨야 분쟁 대응 가능 | watermark verification, audit log completeness |

---

## 8. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | model parameters, decision boundary, API output, confidence/logit, training investment, model IP, prompt/retrieval policy, query logs |
| 공격자 목표 | 기능 복제, stolen model 학습, 대체 서비스 제공, 방어 우회, IP 침해, downstream attack 준비 |
| 공격자 능력 | black-box API query, confidence/probability 관찰, synthetic input 생성, active learning, surrogate dataset 보유, query 자동화 |
| 공격 경로 | API query generation → victim output collection → surrogate training → fidelity/utility evaluation → stolen service 또는 attack reuse |
| 방어자 능력 | rate limit, output restriction, confidence rounding, anomaly detection, query monitoring, watermarking, fingerprinting, legal/contractual control |
| 제외 범위 | 실제 서비스 대상 무단 대량 질의, 모델 추출 자동화 코드 제공, 우회 절차 제공, 실제 타사 모델 도난 시도 |

---

## 9. 평가방법 및 지표

| 평가축 | 지표 | 의미 | W13/P01 활용 |
|---|---|---|---|
| 복제 유사도 | Fidelity, AgreementGap | victim과 stolen model 행동 일치 | 핵심 stealing 평가 |
| 복제 성능 | Acc_stolen, task utility | stolen model의 실제 유용성 | 공격 피해 평가 |
| 질의 비용 | N_queries, ExtractionCost, QueryEfficiency | 공격 비용과 효율 | API 방어 설계 |
| 출력 정보량 | label/probability/logit availability | 추출 난이도 변화 | output restriction 평가 |
| 탐지 성능 | DetectionRate, FPR, anomaly score | 공격 질의 탐지 | monitoring 평가 |
| 방어 비용 | latency, user friction, utility drop | 정상 서비스 영향 | 실무 적용성 |
| 소유권 검증 | watermark verification rate, fingerprint match | 도난 모델 식별 | P02~P04 연결 |
| 재현성 | query policy, model version, seed, API config | 평가 재현 가능성 | W15 evidence chain |

---

## 10. 재현성 체크리스트

| 항목 | 기록해야 할 내용 |
|---|---|
| Bibliographic status | 공식 DOI 논문과 로컬 PDF의 판본 상태, accepted/arXiv 여부 |
| Victim model | model type, task, output type, confidence/logit 제공 여부 |
| Query setting | query budget, query distribution, synthetic/natural input, rate limit 조건 |
| Attacker knowledge | black-box/gray-box/white-box, architecture prior, auxiliary data 여부 |
| Stolen model | surrogate architecture, training data, optimizer, seed |
| Metrics | fidelity, Acc_stolen, query efficiency, ExtractionCost, transferability |
| Defence setting | output restriction, monitoring, watermark, fingerprint, legal notice |
| Detection logs | anomaly score, TP/FP/FN, FPR, response latency |
| Evidence | query log sample, config, model hash, watermark key handling, verification result |
| 한계 | toy/synthetic extraction 평가를 실제 서비스 모델 도난 가능성으로 과장하지 않음 |

---

## 11. 논문의 고유 기여

1. Model stealing을 ML 보안과 AI 지식재산 보호의 핵심 문제로 체계화한다.
2. Black-box API 환경에서도 모델 기능 복제가 가능하다는 위협을 fidelity·query budget 중심으로 설명한다.
3. Confidence/logit output, query strategy, surrogate training이 extraction success에 미치는 영향을 정리한다.
4. 기술적 방어뿐 아니라 watermarking, fingerprinting, monitoring, legal/contractual control을 함께 고려해야 함을 보여준다.
5. W13의 P02~P04 watermarking/fingerprinting 문헌을 이해하기 위한 공격 배경 문헌으로 적합하다.

---

## 12. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| API 유용성·보안 trade-off | 출력 제한과 rate limit은 정상 사용자 경험을 낮출 수 있다. | user friction과 FPR 병기 |
| Adaptive attacker | 공격자는 탐지를 피하기 위해 질의를 분산하거나 자연스럽게 만들 수 있다. | adaptive risk를 한계로 명시 |
| Foundation model 확장 | LLM은 단순 classifier보다 output space와 기능이 넓어 fidelity 정의가 어렵다. | task-specific fidelity와 behavior similarity 지표 제안 |
| Watermark 우회 | watermark/fingerprint는 제거·변형·distillation에 취약할 수 있다. | P02~P04와 연결해 robustness 검증 |
| 법적 대응 한계 | 기술적 증거가 법적 소유권 증명으로 바로 연결되지는 않는다. | evidence chain과 ownership proof 구분 |
| 공개 저장소 PDF 위험 | 출판사 PDF 원문 공개는 저작권 위험이 있다. | DOI/서지/summary 중심 공개 원칙 유지 |

---

## 13. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | AI 서비스는 모델 자체가 IP 자산이며 API를 통해 추출될 수 있다는 문제의식 |
| 2장 관련연구 | 공식 P01 DOI 논문을 model stealing survey 핵심 문헌으로 정리 |
| 3장 위협모형 | model parameter, decision boundary, API output, confidence/logit, prompt/retrieval policy, query log 보호 자산 정의 |
| 4장 연구방법 | fidelity, Acc_stolen, query budget, ExtractionCost, DetectionRate, watermark verification 지표 설계 |
| 5장 분석 | model stealing attack-defence matrix와 API monitoring evidence table 제시 |
| 6장 보안적 함의 | API 공개성, IP 보호, watermark/fingerprint, query auditing, legal evidence chain 필요성 해석 |

---

## 14. 기말논문 연결 3문장

1. W13에서 기말논문에 반영할 개념: model stealing은 모델 API의 반복 질의와 출력 관찰을 통해 victim model의 기능을 surrogate model로 복제하는 공격이며, fidelity와 query budget이 핵심 평가 지표다.
2. W13에서 기말논문에 반영할 표·그림·실험: model stealing threat model, Fidelity·ExtractionCost·DetectionRate 수식표, output restriction/rate limit/watermark defense matrix, DOI/판본 검증표를 반영한다.
3. W13이 LLM/RAG 보안 감사 프레임워크와 연결되는 지점: LLM/RAG 서비스에서는 모델 가중치뿐 아니라 prompt template, system instruction, retrieval index, document ranking policy, embedding behavior도 추출 대상이 될 수 있으므로 query log와 evidence chain을 W14/W15에 연결해야 한다.

---

## 15. 최종 판단

P01은 W13의 중심 문헌이다. 모델 공개 API의 유용성과 수익성은 높지만, 동시에 model stealing과 IP 침해 위험을 만든다. 따라서 기말논문에서는 P01을 **model stealing threat model, fidelity/query budget 평가, API monitoring, watermark/fingerprint defence의 기본 근거 문헌**으로 사용하고, 최종 인용은 W13 `paper_list.md`의 공식 DOI/ACM 메타데이터 기준으로 정리하는 것이 적절하다.

---

## 16. 변환 호환성 메모

```bash
pandoc P01_summary.md -o P01_summary.docx
pandoc P01_summary.md -o P01_summary.pdf --pdf-engine=xelatex
```
