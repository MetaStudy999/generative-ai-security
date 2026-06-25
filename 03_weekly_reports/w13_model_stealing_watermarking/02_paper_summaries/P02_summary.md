# P02 Summary

## Securing Large Language Models: A Survey of Watermarking and Fingerprinting Techniques — Peigen Ye et al., ACM Computing Surveys, 2026

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W13 Model Stealing & Watermarking |
| 공식 논문명 | Securing Large Language Models: A Survey of Watermarking and Fingerprinting Techniques |
| 공식 저자 | Peigen Ye et al. |
| 공식 출판 정보 | ACM Computing Surveys, 2026 |
| DOI | https://doi.org/10.1145/3773028 |
| 로컬 PDF | `01_papers/pdf/02_RELATED_Liang_et_al_2024_LLM_Watermarking_Survey.pdf` |
| 로컬 PDF 상태 | W13 `paper_list.md`와 `download_source.md` 기준 로컬 PDF는 Yuqing Liang et al., `Watermarking Techniques for Large Language Models: A Survey`, arXiv:2409.00089v1 관련 보조 문헌이다. 강의자료 표기 문헌 및 공식 DOI 후보와 동일 문헌으로 단정하지 않는다. |
| 검증 상태 | W13 `paper_list.md` 기준 관련 논문 DOI `10.1145/3773028` 확인. 강의자료 표기 `Y. Ye et al., A Survey of Watermarking and Fingerprinting Techniques for Deep Learning Models, ACM Computing Surveys, 2024`와 로컬 PDF·확인 DOI 사이 차이 메모 유지 |
| PDF 확인 메모 | repo의 PDF 폴더에 P02 관련 PDF blob이 존재함을 확인했다. 다만 로컬 PDF는 공식 P02 후보와 다른 LLM watermarking 보조 문헌이므로, summary는 공식 DOI 기준 관련 논문과 로컬 PDF의 공통 주제인 LLM watermarking/fingerprinting 중심으로 작성하고, 로컬 PDF는 보조 문헌으로만 해석한다. |
| 핵심 근거 사용 가능 여부 | 가능. W13에서 LLM watermarking, fingerprinting, generated text provenance, model ownership verification, detector robustness, paraphrase/translation removal attack, FPR/FNR 평가의 핵심 관련 문헌으로 사용 |

---

## 1. 한 문장 요약

P02 관련 문헌은 LLM watermarking과 fingerprinting을 **generated text provenance, model ownership verification, text watermark, statistical detector, greenlist/redlist token biasing, semantic watermark, model fingerprint, trigger-based ownership proof, robustness against paraphrasing·translation·summarization·fine-tuning, detectability-utility trade-off, false positive/false negative risk** 관점에서 정리하며, W13에서 model stealing 이후의 **소유권 증명과 생성물 출처 추적**을 평가하는 핵심 보조 문헌이다.

---

## 2. 핵심 연구문제

> LLM 서비스는 출력 텍스트가 복제·재배포·변형되기 쉽고, 모델 자체도 API 질의나 fine-tuning을 통해 도용될 수 있다. Watermarking과 fingerprinting은 생성물 출처와 모델 소유권을 증명하려는 기술이지만, 탐지 가능성, 텍스트 품질, 사용자 프라이버시, 공격 내성, 오탐·미탐 비용 사이의 trade-off가 발생한다.

| 번호 | 연구질문 |
|---|---|
| RQ1 | LLM watermark와 model fingerprint는 각각 생성 텍스트 provenance와 모델 소유권을 어떻게 보호하는가? |
| RQ2 | Token-level watermark, semantic watermark, syntactic watermark, model fingerprint, trigger-based verification은 어떤 가정과 한계를 갖는가? |
| RQ3 | Paraphrase, translation, summarization, sampling change, fine-tuning, distillation, watermark removal attack은 watermark detectability를 얼마나 약화시키는가? |
| RQ4 | Watermark detector의 detection rate, FPR, FNR, robustness, text utility, perplexity, semantic preservation을 어떻게 함께 평가해야 하는가? |
| RQ5 | LLM/RAG 서비스에서 watermark/fingerprint 증거를 W13 model stealing, W14 MLOps supply chain, W15 evidence chain과 어떻게 연결할 수 있는가? |

---

## 3. 논문의 핵심 기여

| 기여 | 설명 | W13 연결 |
|---|---|---|
| Watermarking taxonomy | token-level, semantic, syntactic, distribution-shift, key-based watermarking 정리 | 생성 텍스트 provenance 평가 |
| Fingerprinting taxonomy | model behavior, trigger set, challenge-response, ownership verification 방식 정리 | model stealing 이후 소유권 증명 |
| Robustness 평가 | paraphrase, translation, summarization, editing, sampling, fine-tuning 공격에 대한 내성 논의 | watermark removal threat model |
| 오탐·미탐 지표 강조 | FPR/FNR, detection threshold, ROC/AUC, confidence score를 함께 봐야 함 | 법적·운영 리스크 평가 |
| Utility trade-off | watermark 삽입이 fluency, perplexity, semantic quality, user experience에 미치는 영향 정리 | 실서비스 적용성 판단 |

---

## 4. 목차별 핵심 개괄

| 목차 | 핵심 내용 | 비전공자용 이해 |
|---|---|---|
| 1. Introduction | LLM 생성 텍스트와 모델 소유권을 검증하기 위해 watermarking/fingerprinting이 필요하다. | AI가 만든 글인지, 어느 모델이 만든 글인지 추적하려는 기술이다. |
| 2. Background | LLM sampling, token probability, decoding, detector, ownership verification, provenance 개념을 설명한다. | 모델이 다음 단어를 고를 때 특정 패턴을 살짝 넣어 나중에 찾는 방식이다. |
| 3. Text Watermarking | greenlist/redlist, logit bias, statistical watermark, semantic/syntactic watermark 등 텍스트 출력 기반 기법을 정리한다. | 글의 품질은 크게 해치지 않으면서 보이지 않는 통계적 흔적을 넣는다. |
| 4. Model Fingerprinting | 모델의 고유 행동, trigger query, challenge-response, fingerprint vector로 소유권을 검증하는 접근을 다룬다. | 모델에 특수 질문을 했을 때 소유자만 아는 반응이 나오게 하는 방식이다. |
| 5. Robustness and Attacks | paraphrase, translation, summarization, editing, fine-tuning, distillation, collusion 등이 watermark/fingerprint를 약화시킨다. | 글을 바꾸거나 번역하면 워터마크가 흐려질 수 있다. |
| 6. Evaluation Metrics | detection rate, FPR/FNR, AUC, robustness under attacks, utility drop, text quality를 함께 평가한다. | 잘 잡는 것도 중요하지만, 아닌 것을 AI 글이라고 잘못 잡는 것도 큰 문제다. |
| 7. Deployment and Ethics | false accusation, privacy, user consent, transparency, legal evidence, adversarial users 등 운영 이슈를 논의한다. | 워터마크 탐지는 법적·사회적 책임과 연결되므로 신중해야 한다. |
| 8. Future Directions | robust semantic watermark, multilingual setting, open-source model, RAG/citation provenance, benchmark 표준화가 과제로 남는다. | 앞으로는 여러 언어, RAG, 오픈소스 모델까지 추적 체계가 필요하다. |
| 로컬 PDF 메모 | 로컬 PDF는 Liang et al. 2024 LLM watermarking survey로, official P02 후보와 동일 문헌이 아니다. | PDF가 있다고 해서 공식 지정 논문으로 인용하면 안 된다. |

---

## 5. 핵심 이론 및 수식

> 아래 수식은 LLM watermarking/fingerprinting 평가를 설명하기 위한 표준화된 표현이다. 실제 우회 절차가 아니라 탐지·방어·감사 지표 중심으로 정리한다.

### 5.1 Watermark Detection Score

검출기는 생성 텍스트에서 watermark token 또는 pattern이 기대치보다 많이 나타나는지를 통계량으로 측정할 수 있다.

$$
DetectionScore=\frac{N_{marked}-\mathbb{E}[N_{marked}]}{\sqrt{Var(N_{marked})}}
$$

| 기호 | 의미 |
|---|---|
| $N_{marked}$ | watermark 규칙에 부합하는 token 또는 pattern 수 |
| $\mathbb{E}[N_{marked}]$ | watermark가 없을 때의 기대값 |
| $Var(N_{marked})$ | 분산 |

### 보안적 의미

DetectionScore가 높으면 watermark가 삽입되었을 가능성이 커진다. 단, threshold 선택에 따라 FPR/FNR이 달라진다.

---

### 5.2 False Positive / False Negative Rate

워터마크 검출 시스템의 오탐과 미탐을 측정한다.

$$
FPR=\frac{FP}{FP+TN},\qquad FNR=\frac{FN}{FN+TP}
$$

### 보안적 의미

FPR이 높으면 사람이 쓴 글을 AI 글로 오판할 수 있고, FNR이 높으면 watermark가 있는 글을 놓친다. 법적·운영 환경에서는 두 지표 모두 중요하다.

---

### 5.3 Detection Rate

워터마크가 있는 생성물을 올바르게 탐지한 비율이다.

$$
DetectionRate=\frac{TP}{TP+FN}
$$

### 보안적 의미

DetectionRate만 높아도 FPR이 높으면 실서비스에 부적합할 수 있다. detection rate는 threshold, text length, language, decoding setting과 함께 보고해야 한다.

---

### 5.4 Robustness under Paraphrase

문장 변형 후에도 watermark가 유지되는지 측정한다.

$$
Robustness_{para}=\frac{DetectionRate_{after\ paraphrase}}{DetectionRate_{before\ paraphrase}}
$$

### 보안적 의미

paraphrase 후 detection rate가 급락하면 실전에서 watermark가 쉽게 약화될 수 있다.

---

### 5.5 Utility Drop

워터마크 삽입이 텍스트 품질에 미치는 영향을 측정한다.

$$
UtilityDrop=Quality_{clean}-Quality_{watermarked}
$$

| 기호 | 의미 |
|---|---|
| $Quality_{clean}$ | watermark 없는 출력 품질 |
| $Quality_{watermarked}$ | watermark 삽입 출력 품질 |

### 보안적 의미

워터마크가 강해도 텍스트 품질이 크게 낮아지면 서비스 적용성이 떨어진다.

---

### 5.6 Fingerprint Verification Score

모델 소유권 검증에서 challenge set에 대한 expected response 일치도를 볼 수 있다.

$$
FingerprintScore=\frac{1}{M}\sum_{j=1}^{M}\mathbf{1}[f(q_j)=r_j]
$$

| 기호 | 의미 |
|---|---|
| $q_j$ | 소유권 검증용 challenge query |
| $r_j$ | 소유자가 기대하는 response 또는 behavior |

### 보안적 의미

FingerprintScore는 모델이 특정 소유자의 fingerprint를 유지하는지 보는 지표다. 단, 정상 모델의 우연 일치와 적응형 공격을 함께 고려해야 한다.

---

### 5.7 Watermark Risk Score

탐지·품질·강건성·오탐 위험을 함께 고려하는 요약 지표다.

$$
Risk_{wm}=\alpha FNR+\beta FPR+\gamma UtilityDrop-\lambda Robustness_{attack}
$$

### 보안적 의미

좋은 watermark는 detection이 잘 되고, 공격 후에도 유지되며, 텍스트 품질을 크게 해치지 않고, 오탐을 낮춰야 한다.

---

## 6. AI 원리 70% 관점 분석

| 원리 항목 | 설명 | W13/P02에서의 의미 |
|---|---|---|
| Text Watermarking | 생성 텍스트에 통계적 또는 의미적 흔적 삽입 | provenance 추적 |
| Model Fingerprinting | 모델의 고유 응답 패턴으로 소유권 검증 | model stealing 대응 |
| Statistical Detection | watermark pattern이 우연보다 많은지 검정 | detection score 산출 |
| Token Biasing | 특정 token 집합을 더 선택하게 유도 | greenlist/redlist 계열 |
| Semantic Watermark | 의미 단위에서 watermark 유지 | paraphrase robustness 목표 |
| Thresholding | detection score를 기준으로 판정 | FPR/FNR trade-off |
| Robustness Evaluation | paraphrase/translation/fine-tuning 후 검출성 평가 | 우회 내성 |
| Utility Evaluation | fluency, perplexity, semantic quality 평가 | 서비스 품질 |

---

## 7. 보안 이슈 30% 관점 분석

| 보안 항목 | Watermark/Fingerprint 관점 해석 | 대표 평가 지표 |
|---|---|---|
| 기밀성 | watermark key와 fingerprint trigger가 노출되면 우회 가능 | key leakage risk |
| 무결성 | 생성물 provenance와 소유권 증거가 위·변조될 수 있음 | verification score, tamper evidence |
| 가용성 | 강한 watermark가 텍스트 품질과 응답 속도를 저하시킬 수 있음 | UtilityDrop, latency |
| 프라이버시 | 사용자 텍스트에 watermark 추적 정보를 넣는 경우 고지·동의 문제가 발생 | consent, traceability risk |
| 안전성 | 잘못된 검출은 false accusation과 법적 분쟁을 만들 수 있음 | FPR, confidence interval |
| 책임성 | detector version, key management, threshold, evidence log가 필요 | audit log completeness |

---

## 8. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | generated text provenance, model ownership, watermark key, fingerprint trigger, detector threshold, evidence log |
| 공격자 목표 | watermark 제거, detection evasion, false ownership claim, watermark forgery, stolen model의 fingerprint 제거 |
| 공격자 능력 | paraphrase, translation, summarization, editing, sampling 변경, fine-tuning/distillation, detector probing |
| 공격 경로 | watermarked output 생성 → post-processing/translation/paraphrase → detector score 감소 → provenance 부인 또는 소유권 분쟁 |
| 방어자 능력 | robust watermark, semantic watermark, key management, detector calibration, fingerprint challenge, audit logging |
| 제외 범위 | 실제 서비스 워터마크 제거 절차, 우회 코드, 타사 모델 소유권 허위 주장, watermark key 노출 |

---

## 9. 평가방법 및 지표

| 평가축 | 지표 | 의미 | W13/P02 활용 |
|---|---|---|---|
| 검출 성능 | DetectionRate, AUC, DetectionScore | watermark 탐지력 | 핵심 평가 |
| 오탐·미탐 | FPR, FNR, threshold sensitivity | false accusation/미탐 위험 | 법적·운영 리스크 |
| 강건성 | paraphrase/translation/fine-tuning robustness | 변형 후 watermark 유지 | 우회 내성 |
| 품질 | UtilityDrop, perplexity, semantic similarity | 텍스트 유용성 | 서비스 적용성 |
| 소유권 검증 | FingerprintScore, verification success | model ownership proof | model stealing 대응 |
| 비용 | detection latency, generation overhead | 운영 비용 | MLOps 연결 |
| 보안관리 | key rotation, detector version, threshold log | 감사 가능성 | W15 evidence chain |
| 서지 정확성 | official DOI match, local PDF mismatch flag | 참고문헌 정확성 | 기말논문 검증표 |

---

## 10. 재현성 체크리스트

| 항목 | 기록해야 할 내용 |
|---|---|
| Bibliographic status | 공식 DOI 논문과 로컬 PDF 동일 여부, related flag |
| Model | model name/version, decoding method, temperature, top-p, seed |
| Watermark method | token-level/semantic/syntactic, key 사용 여부, detector 방식 |
| Fingerprint method | trigger/challenge set, expected response, ownership threshold |
| Dataset | prompt set, language, domain, text length distribution |
| Attack/robustness setting | paraphrase, translation, summarization, editing, fine-tuning 조건 |
| Metrics | DetectionRate, FPR, FNR, AUC, UtilityDrop, Robustness_para, FingerprintScore |
| Threshold | detector threshold, confidence interval, calibration data |
| Evidence | detector version, key handling, log hash, evaluation script, failure case |
| 한계 | watermark 검출을 법적 소유권 확정이나 AI 생성 여부 절대 판정으로 과장하지 않음 |

---

## 11. 논문의 고유 기여

1. LLM watermarking과 fingerprinting을 generated text provenance와 model ownership verification의 두 축으로 정리한다.
2. Detection score, FPR/FNR, robustness, utility를 함께 고려해야 함을 보여준다.
3. Paraphrase, translation, summarization, fine-tuning, distillation이 watermark/fingerprint를 약화시킬 수 있음을 위협모형에 포함한다.
4. W13 P01의 model stealing 문제에 대해 사후 소유권 검증과 provenance evidence를 제공하는 방어 관점을 제공한다.
5. 로컬 PDF가 official P02 후보와 다른 관련 문헌이므로, 참고문헌 검증표와 보조 문헌 관리의 중요성을 보여준다.

---

## 12. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 로컬 PDF 불일치 | P02 로컬 PDF는 Liang et al. LLM watermarking survey이며, 공식 DOI 후보와 동일 문헌이 아니다. | 공식 DOI/관련 PDF를 분리 표기 |
| 오탐 위험 | watermark detector가 사람이 쓴 글을 AI 생성물로 잘못 판단할 수 있다. | FPR, confidence interval, threshold 기록 |
| 변형 공격 취약성 | paraphrase·translation·summarization 후 watermark가 약화될 수 있다. | robustness under transformation 평가 |
| Utility trade-off | watermark 삽입이 fluency나 semantic quality를 낮출 수 있다. | UtilityDrop과 human evaluation 병기 |
| Key management | watermark key가 유출되면 위조·제거가 가능하다. | key rotation과 접근통제 메모 |
| 법적 증거 한계 | watermark 검출만으로 소유권·출처를 절대 입증하기 어렵다. | evidence chain과 detector uncertainty 병기 |

---

## 13. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | 생성형 AI 모델과 산출물은 provenance와 소유권 검증이 필요한 보안 자산이라는 문제의식 |
| 2장 관련연구 | 공식 P02 DOI 후보를 LLM watermarking/fingerprinting 관련 문헌으로 정리하고, 로컬 PDF mismatch는 검증표에 기록 |
| 3장 위협모형 | generated text, watermark key, fingerprint trigger, detector threshold, evidence log 보호 자산 정의 |
| 4장 연구방법 | DetectionScore, FPR/FNR, Robustness_para, UtilityDrop, FingerprintScore 지표 설계 |
| 5장 분석 | watermark/fingerprint threat-defense-metric matrix와 detector evidence table 제시 |
| 6장 보안적 함의 | AI 생성물 추적, 모델 소유권 검증, 오탐 책임, key management, audit evidence 필요성 해석 |

---

## 14. 기말논문 연결 3문장

1. W13에서 기말논문에 반영할 개념: watermarking은 생성 텍스트 provenance를 추적하고 fingerprinting은 모델 소유권을 검증하는 기술이며, 둘 다 detection rate뿐 아니라 FPR/FNR과 utility를 함께 평가해야 한다.
2. W13에서 기말논문에 반영할 표·그림·실험: DetectionScore, FPR/FNR, Robustness under Paraphrase, UtilityDrop, FingerprintScore 수식표와 watermark/fingerprint defence matrix를 반영한다.
3. W13이 LLM/RAG 보안 감사 프레임워크와 연결되는 지점: RAG/LLM 산출물의 citation, generated answer, retrieved evidence에도 provenance 표시와 detector/audit log가 필요하며, 이 증거는 W14/W15 evidence chain으로 연결한다.

---

## 15. 최종 판단

P02는 W13에서 model stealing 이후의 소유권 검증과 생성물 출처 추적을 담당하는 핵심 관련 문헌이다. 다만 W13 `paper_list.md` 기준 로컬 PDF는 Liang et al.의 LLM watermarking survey이며, 공식 DOI 후보인 Peigen Ye et al.의 ACM Computing Surveys 문헌과 동일하다고 단정하면 안 된다. 기말논문에서는 P02를 **LLM watermarking/fingerprinting, generated text provenance, model ownership verification, FPR/FNR 기반 detector evaluation의 관련 근거 문헌**으로 사용하고, 공식 DOI·로컬 PDF 차이는 검증표에 유지하는 것이 적절하다.

---

## 16. 변환 호환성 메모

```bash
pandoc P02_summary.md -o P02_summary.docx
pandoc P02_summary.md -o P02_summary.pdf --pdf-engine=xelatex
```
