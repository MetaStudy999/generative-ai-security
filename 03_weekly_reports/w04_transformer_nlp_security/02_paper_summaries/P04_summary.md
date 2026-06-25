# P04 Summary

## A Survey of Adversarial Defenses and Robustness in NLP — Shreya Goyal, Sumanth Doddapaneni, Mitesh M. Khapra, Balaraman Ravindran, ACM Computing Surveys, 2023

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W04 Transformer 변형 & NLP 대적공격·프라이버시 |
| 논문명 | A Survey of Adversarial Defenses and Robustness in NLP |
| 저자 | Shreya Goyal, Sumanth Doddapaneni, Mitesh M. Khapra, Balaraman Ravindran |
| 공식 출판 정보 | ACM Computing Surveys, Vol. 55, No. 14s, pp. 1–39, 2023 |
| DOI | https://doi.org/10.1145/3593042 |
| 보조 URL | https://arxiv.org/abs/2203.06414 |
| 논문 유형 | Survey / NLP Adversarial Robustness Review |
| 로컬 PDF | `01_papers/pdf/04_Goyal_et_al_2023_Adversarial_Defences_Robustness_NLP.pdf` |
| 검증 상태 | W04 `paper_list.md` 기준 ACM CSUR 출판 DOI 확인. arXiv 제목은 `Defences`, ACM/Crossref 제목은 `Defenses`로 표기 차이가 있으며, 강의자료의 `N. Goyal` 표기는 사람 검토 필요 |
| PDF 확인 메모 | repo의 PDF 폴더에 P04 관련 PDF blob이 존재함을 확인했다. 요약은 로컬 PDF 경로와 W04 `paper_list.md`의 공식 DOI/arXiv 메타데이터 기준으로 보완했다. |
| 수식 호환성 | GitHub 수식 렌더링 오류 방지를 위해 `\operatorname`을 사용하지 않고 `\mathrm{...}` 형태로 작성했다. |
| 핵심 근거 사용 가능 여부 | 가능. W04에서 NLP adversarial attack/defense taxonomy, character/word/sentence-level perturbation, semantic-preserving constraint, robust accuracy, ASR, over-refusal, adversarial training, certified robustness의 핵심 보안 문헌으로 사용 |

---

## 1. 한 문장 요약

이 논문은 NLP 모델의 adversarial attack과 defense를 **character-level perturbation, word substitution, synonym/paraphrase attack, sentence-level transformation, semantic-preserving constraint, transfer attack, adversarial training, input preprocessing, detection, certified robustness, robust evaluation, over-refusal** 관점에서 정리하며, W04에서 Transformer/NLP 보안 평가를 **clean accuracy와 robust accuracy, ASR, semantic similarity, fluency, human validity, latency**로 분리해야 함을 제시하는 핵심 보안 survey 문헌이다.

---

## 2. 핵심 연구문제

> 텍스트 adversarial attack은 이미지 공격처럼 단순한 연속 공간의 작은 perturbation으로만 정의할 수 없다. 단어 하나를 바꾸면 의미가 바뀔 수 있고, 문법성·자연스러움·인간 판단 가능성이 평가의 핵심이 된다. 따라서 NLP robustness는 공격 성공률뿐 아니라 semantic similarity와 human validity를 함께 기록해야 한다.

| 번호 | 연구질문 |
|---|---|
| RQ1 | NLP adversarial attack은 character, word, sentence, semantic level에서 어떻게 분류되는가? |
| RQ2 | 의미 보존 조건과 문법성 조건은 텍스트 공격 평가에서 왜 중요한가? |
| RQ3 | Clean accuracy, robust accuracy, ASR, semantic similarity, transferability를 어떻게 함께 측정해야 하는가? |
| RQ4 | NLP defense는 adversarial training, input preprocessing/correction, detection, certified robustness, model architecture 개선으로 어떻게 구분되는가? |
| RQ5 | RAG/LLM prompt injection과 prompt privacy 평가에서 word substitution, paraphrase, indirect instruction이 어떤 방식으로 확장되는가? |

---

## 3. 논문의 핵심 기여

| 기여 | 설명 | W04 연결 |
|---|---|---|
| NLP adversarial taxonomy | character/word/sentence/semantic-level 공격을 체계적으로 분류 | W04 P04 핵심 |
| Defense taxonomy | adversarial training, preprocessing, detection, certified robustness 등을 분류 | 방어 프레임워크 설계 |
| 평가 기준 제시 | ASR, robust accuracy, semantic similarity, fluency, transferability 필요성 강조 | 실험 지표 설계 |
| 의미 보존 문제 강조 | 텍스트 공격은 의미·문법·자연스러움의 제약을 가져야 함 | human validity 연결 |
| LLM/RAG 확장 근거 | paraphrase, context manipulation, prompt variation이 LLM/RAG 공격면으로 확장 가능 | W07/W08 연결 |

---

## 4. 목차별 핵심 개괄

| 목차 | 핵심 내용 | 비전공자용 이해 |
|---|---|---|
| 1. Introduction | NLP 모델도 작은 텍스트 변형에 취약하며 robustness 평가가 필요하다. | 문장을 조금 바꾸면 AI 판단이 바뀔 수 있다. |
| 2. Background | NLP 모델, tokenization, embedding, Transformer, adversarial example의 기본 개념을 설명한다. | 텍스트가 token으로 바뀌고 모델이 판단하는 과정을 이해한다. |
| 3. Attack Taxonomy | character, word, phrase, sentence, semantic-level 공격을 분류한다. | 오타, 동의어, 문장 바꾸기 등 다양한 방식이 있다. |
| 4. Attack Constraints | semantic similarity, fluency, grammaticality, label preservation이 필요하다. | 뜻이 완전히 바뀌면 공격 평가로 보기 어렵다. |
| 5. Defense Methods | adversarial training, input correction, detection, robust representation, certified defense를 정리한다. | 모델을 더 튼튼하게 만들거나 이상 입력을 감지한다. |
| 6. Evaluation Metrics | ASR, robust accuracy, clean accuracy, perturbation rate, transferability, human evaluation을 다룬다. | 공격이 얼마나 성공했는지와 정상 성능이 얼마나 유지되는지 같이 본다. |
| 7. Challenges | 의미 보존 평가, benchmark 표준화, LLM 확장, 방어 비용, over-refusal 문제가 남는다. | 텍스트 보안 평가는 수치 하나로 끝내기 어렵다. |
| 8. Future Directions | semantics-aware robustness, certified NLP, human-centered evaluation, LLM/RAG robustness가 향후 과제다. | 의미를 이해하면서도 안전한 언어 모델이 필요하다. |

---

## 5. 핵심 이론 및 수식

> 수식은 GitHub Markdown/KaTeX 호환성을 우선한다. `\operatorname` 매크로는 사용하지 않고 `\mathrm{...}` 형태로 작성한다.

### 5.1 NLP Adversarial Risk

텍스트 대적위험은 원문 $x$의 의미 보존 변형 집합 $\mathcal{N}(x)$에서 최악 손실을 보는 방식으로 표현할 수 있다.

$$
R_{adv}=\mathbb{E}_{(x,y)}\left[\max_{x_{alt}\in\mathcal{N}(x)}\ell(f_{\theta}(x_{alt}),y)\right]
$$

| 기호 | 의미 |
|---|---|
| $x$ | 원문 입력 |
| $x_{alt}$ | 변형된 텍스트 입력 |
| $\mathcal{N}(x)$ | 의미 보존 또는 제한된 텍스트 변형 집합 |
| $f_{\theta}$ | NLP 모델 |
| $\ell$ | 손실함수 |

### 보안적 의미

NLP 공격은 이미지처럼 연속적인 pixel norm만으로 정의하기 어렵다. 의미 보존, 문법성, fluency, 인간 판단 가능성을 함께 고려해야 한다.

---

### 5.2 Attack Success Rate

공격 성공률은 공격 입력에서 목표 실패가 발생한 비율이다.

$$
ASR=\frac{1}{m}\sum_{j=1}^{m}\mathbf{1}[f_{\theta}(x_j^{adv})\neq y_j]
$$

### 보안적 의미

Clean accuracy가 높아도 ASR이 높으면 모델은 보안적으로 취약하다. W04에서는 toy keyword detector 결과와 실제 Transformer 성능을 분리해 해석해야 한다.

---

### 5.3 Robust Accuracy

공격 또는 변형 텍스트 조건에서 정답을 유지한 비율이다.

$$
Acc_{robust}=\frac{1}{m}\sum_{j=1}^{m}\mathbf{1}[f_{\theta}(x_j^{adv})=y_j]
$$

### 보안적 의미

Robust accuracy는 ASR과 반대 방향의 지표다. 공격 성공률만 보고 결론을 내리지 말고 정상 성능과 robust 성능을 함께 봐야 한다.

---

### 5.4 Semantic Similarity Constraint

텍스트 공격은 원문의 의미를 유지해야 평가가 타당하다.

$$
\mathrm{Sim}(x,x_{alt})\geq \tau
$$

| 기호 | 의미 |
|---|---|
| $\mathrm{Sim}$ | 의미 유사도 함수 |
| $\tau$ | 의미 보존 threshold |

### 보안적 의미

의미가 바뀐 입력으로 모델이 달라지는 것은 보안 취약성이라기보다 다른 입력에 대한 정상 반응일 수 있다. 따라서 semantic similarity와 human validity를 공격 평가에 포함해야 한다.

---

### 5.5 Perturbation Rate

원문 중 얼마나 많은 token이 변경되었는지 측정한다.

$$
PerturbRate=\frac{N_{changed\ tokens}}{N_{total\ tokens}}
$$

### 보안적 의미

적은 변경으로 높은 ASR을 달성하면 모델이 표면 표현 변화에 취약하다는 뜻이다.

---

### 5.6 Over-refusal Rate

방어 모델이 정상 입력을 과도하게 차단한 비율이다.

$$
OverRefusal=\frac{N_{benign\ blocked}}{N_{benign\ inputs}}
$$

### 보안적 의미

방어가 강해도 정상 요청을 많이 막으면 실제 서비스에 적용하기 어렵다. 보안성과 사용성의 trade-off를 같이 평가해야 한다.

---

### 5.7 Transferability

한 모델에서 생성한 공격이 다른 모델에서도 성공하는 비율이다.

$$
TransferRate=\frac{N_{success\ on\ target}}{N_{crafted\ on\ source}}
$$

### 보안적 의미

Transferability가 높으면 black-box 환경에서도 위험이 커진다.

---

### 5.8 NLP Robustness Score

NLP 보안 방어의 품질은 robust 성능, 의미 보존, 과차단, 지연을 함께 반영해야 한다.

$$
NLPRobustScore=Acc_{robust}+\alpha\mathrm{Sim}(x,x_{alt})-\beta ASR-\gamma OverRefusal-\lambda Latency
$$

### 보안적 의미

좋은 방어는 공격을 막으면서도 의미 보존 평가가 타당하고, 정상 요청을 과차단하지 않으며, 운영 지연이 낮아야 한다.

---

## 6. AI 원리 70% 관점 분석

| 원리 항목 | 설명 | W04/P04에서의 의미 |
|---|---|---|
| Character-level Attack | 오탈자, 문자 삽입/삭제, homoglyph 등으로 표면형 교란 | tokenizer 취약성 |
| Word-level Attack | 동의어 치환, 우회 표현, token substitution 사용 | embedding/semantic 취약성 |
| Sentence-level Attack | paraphrase나 문장 구조 변환 | 의미 유지 변형 평가 |
| Semantic Constraint | 의미 보존 여부가 공격 타당성의 핵심 | human validity 필요 |
| Transferability | 한 모델 공격이 다른 모델에도 통할 수 있음 | black-box 위험 |
| Adversarial Training | 공격 예시를 학습에 포함해 robust 성능 향상 | 방어 방법 |
| Detection/Correction | 이상 입력 감지 또는 복원 | 운영 방어 |
| Certified Robustness | 제한된 변형 범위에서 보증 제공 | 고신뢰 방어 과제 |

---

## 7. 보안 이슈 30% 관점 분석

| 보안 항목 | NLP robustness 관점 해석 | 대표 평가 지표 |
|---|---|---|
| 무결성 | 입력 표현을 조금 바꿔 모델 판단을 왜곡 | ASR, robust accuracy |
| 가용성 | 과도한 방어가 정상 입력을 차단하면 서비스성 저하 | OverRefusal, latency |
| 기밀성 | 반복 질의로 모델의 약점과 정책을 추론할 수 있음 | query count, transfer rate |
| 프라이버시 | 입력·로그·출력에 민감정보가 포함될 수 있음 | LeakageRate, PII finding |
| 안전성 | 우회 표현이 정책 필터를 통과해 harmful output을 유도할 수 있음 | unsafe response rate |
| 책임성 | 원문, 변형문, 의미 유사도, 공격 판정, 방어 결과를 기록해야 함 | audit completeness |

---

## 8. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 대상 | 사용자 입력, prompt, tokenizer, embedding, 분류 결과, 정책 판단, NLP filter, prompt wrapper, output log |
| 공격자 목표 | 오분류, policy bypass, keyword filter 우회, harmful output 유도, 민감정보 노출 유도 |
| 공격자 능력 | typo, character edit, word substitution, paraphrase, repeated query, prompt variation, semantic-preserving rewrite |
| 공격 경로 | text input → tokenizer → embedding/Transformer/NLP model → decision/output/log |
| 방어자 능력 | adversarial training, input normalization, detection, semantic validation, human review, output monitoring, logging |
| 제외 범위 | 실제 서비스 무단 공격, 유해 콘텐츠 생성, 개인정보 포함 공격 실험, 공격 prompt 제작 지원 |

---

## 9. 평가방법 및 지표

| 평가축 | 지표 | 의미 | W04/P04 활용 |
|---|---|---|---|
| 정상 성능 | Clean Accuracy, F1 | 정상 텍스트 성능 | baseline utility |
| 공격 성능 | ASR, targeted success | 공격 효과 | robustness 평가 |
| 방어 성능 | Robust Accuracy, RobustDrop | 변형 텍스트 조건 성능 | 방어 성능 |
| 의미 보존 | Semantic Similarity, human validity | 공격 타당성 | 평가 신뢰성 |
| 자연스러움 | Fluency, grammar score | 사람이 보기 자연스러운지 | 품질 평가 |
| 이전성 | TransferRate | 모델 간 공격 이전성 | black-box 위험 |
| 사용자 영향 | OverRefusal, false block rate | 정상 요청 과차단 | usability |
| 운영성 | Latency, runtime overhead | 방어 적용 지연 | deployment 평가 |

---

## 10. 재현성 체크리스트

| 항목 | 기록해야 할 내용 |
|---|---|
| Bibliographic status | DOI, ACM CSUR 출판정보, arXiv 판본, Defenses/Defences 표기 차이 |
| Dataset | 공개 NLP classification dataset 또는 toy prompt set, split |
| Model | keyword detector, small classifier, Transformer model 구분, model hash |
| Attack setting | character/word/sentence 변형, paraphrase rule, query budget |
| Constraint | semantic threshold, fluency rule, grammar check, human validity 기준 |
| Defense | adversarial training, input correction, detection, certified setting 여부 |
| Evaluation | clean accuracy, robust accuracy, ASR, semantic similarity, transferability, over-refusal, latency |
| Evidence | 원문/변형문 pair, model output, metric CSV/JSON, script commit, run log |
| Limitation | toy keyword detector 결과를 실제 Transformer 취약성으로 일반화하지 않음 |
| GitHub math | `\operatorname` 사용 금지, `\mathrm{Sim}` 형태 사용 |

---

## 11. 논문의 고유 기여

1. NLP adversarial attack과 defense taxonomy를 체계적으로 제공한다.
2. 텍스트 공격 평가에서 의미 보존, 문법성, fluency, 인간 판단이 중요함을 정리한다.
3. Clean performance와 robust performance를 분리해야 한다는 핵심 근거를 제공한다.
4. W04 toy word substitution 실험을 안전한 축소 실험으로 해석하게 해준다.
5. W08 RAG prompt injection, W07 LLM security, W15 evaluation/reproducibility로 확장되는 텍스트 robustness 평가 기반을 제공한다.

---

## 12. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| LLM prompt injection 직접성 제한 | NLP adversarial robustness가 중심이며 RAG/agent prompt injection은 별도 문헌 필요 | W08과 연결 |
| 의미 보존 평가 어려움 | semantic similarity 수치만으로 인간 의미 판단을 완전히 대체하기 어렵다. | 예시와 human validity 한계 병기 |
| 최신 LLM 방어 변화 | instruction-tuned LLM의 공격·방어는 빠르게 변한다. | W07/W08 최신 문헌과 결합 |
| 악용 위험 | 공격 절차 상세화는 부적절하다. | toy/public data와 방어 중심으로 제한 |
| 방어 부작용 | 강한 방어가 over-refusal과 latency 증가를 만들 수 있다. | usability와 운영성 지표 병기 |
| 저작권 관리 | PDF 원문을 public repo에 유지하면 권리 조건 검토가 필요하다. | DOI/서지/summary 중심 공개 검토 |

---

## 13. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | NLP 보안 평가는 의미 보존 변형에 대한 모델 안정성까지 포함해야 한다는 문제의식 |
| 2장 관련연구 | NLP adversarial attack/defense taxonomy 정리 |
| 3장 위협모형 | character/word/sentence-level 공격자 능력과 prompt wrapper 우회 경로 정의 |
| 4장 연구방법 | NLP adversarial risk, ASR, robust accuracy, semantic similarity, over-refusal, TransferRate 지표 설계 |
| 5장 분석 | toy word substitution 결과와 한계, clean-robust-over-refusal 비교표 제시 |
| 6장 보안적 함의 | 무결성, 가용성, 책임성, RAG/LLM prompt injection과의 연결 해석 |
| 부록 | 원문/변형문 pair, semantic threshold, human validity note, run log 수록 |

---

## 14. 기말논문 연결 3문장

1. W04에서 기말논문에 반영할 개념: NLP 보안 평가는 의미를 보존하는 텍스트 변형에서 모델 판단이 얼마나 안정적인지 clean accuracy, robust accuracy, ASR로 분리해야 한다.
2. W04에서 기말논문에 반영할 표·그림·실험: NLP adversarial taxonomy, ASR 수식, semantic similarity 조건, clean-robust-over-refusal 비교표를 반영한다.
3. W04가 W08 RAG 문서 오염/LLM 보안 감사 프레임워크와 연결되는 지점: RAG/LLM prompt injection도 텍스트 변형과 의미 보존 우회 표현을 이용하므로, P04의 semantic-preserving robustness 평가를 prompt/context 보안 평가로 확장할 수 있다.

---

## 15. 최종 판단

P04는 W04의 핵심 보안 문헌이다. Transformer/NLP 시스템은 정상 문장에서는 높은 성능을 보여도 character edit, word substitution, paraphrase, semantic-preserving rewrite에 취약할 수 있다. 따라서 기말논문에서는 P04를 **NLP adversarial taxonomy, semantic similarity constraint, clean/robust/ASR 분리 평가, over-refusal 평가, prompt injection 확장 근거 문헌**으로 사용하는 것이 적절하다.

---

## 16. GitHub 수식 호환성 메모

이 파일에서는 GitHub 수식 렌더링 오류 방지를 위해 `\operatorname`을 사용하지 않는다.

| 피해야 할 표현 | 권장 표현 |
|---|---|
| `\operatorname{Sim}` | `\mathrm{Sim}` |
| `\operatorname{argmax}` | `\mathrm{argmax}` 또는 `\arg\max` |
| `\operatorname{softmax}` | `\mathrm{softmax}` |

```bash
pandoc P04_summary.md -o P04_summary.docx
pandoc P04_summary.md -o P04_summary.pdf --pdf-engine=xelatex
```
