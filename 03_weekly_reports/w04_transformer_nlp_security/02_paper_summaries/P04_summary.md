# P04 Summary

## A Survey of Adversarial Defenses and Robustness in NLP — Shreya Goyal et al., ACM Computing Surveys, 2023

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W04 Transformer 변형 & NLP 대적공격·프라이버시 |
| 논문명 | A Survey of Adversarial Defenses and Robustness in NLP |
| 저자 | Shreya Goyal, Sumanth Doddapaneni, Mitesh M. Khapra, Balaraman Ravindran |
| 학술지 | ACM Computing Surveys |
| 권호/쪽 | Vol. 55, No. 14s, pp. 1–39 |
| 연도 | 2023 |
| DOI | https://doi.org/10.1145/3593042 |
| 보조 URL | https://arxiv.org/abs/2203.06414 |
| 논문 유형 | Survey / NLP Adversarial Robustness Review |
| 로컬 PDF | `01_papers/pdf/04_Goyal_et_al_2023_Adversarial_Defences_Robustness_NLP.pdf` |
| 강의계획서 지정 논문과 일치 여부 | 일치. 단, 강의자료의 `N. Goyal` 표기는 사람 검토 필요 |
| 핵심 근거 사용 가능 여부 | 가능 |
| 검증 메모 | W04 `paper_list.md` 기준 ACM CSUR 출판 DOI 확인. arXiv 제목은 `Defences`, ACM 제목은 `Defenses` |

---

## 1. 한 문장 요약

이 논문은 NLP 모델의 adversarial attack과 defense를 **character-level, word substitution, paraphrase, sentence-level, semantic-preserving perturbation, transfer attack, robustness evaluation** 관점에서 정리하고, clean accuracy와 attack success rate를 분리해 평가해야 함을 제시하는 W04의 핵심 보안 survey 논문이다.

---

## 2. 연구문제

> 의미를 크게 훼손하지 않는 텍스트 변형이 NLP 모델의 판단을 어떻게 바꾸며, 이를 방어하고 평가하기 위해 어떤 threat model과 지표가 필요한가?

| 번호 | 연구질문 |
|---|---|
| RQ1 | NLP adversarial attack은 character, word, sentence, semantic level에서 어떻게 분류되는가? |
| RQ2 | 의미 보존 조건과 문법성 조건은 텍스트 공격 평가에 왜 중요한가? |
| RQ3 | Robust accuracy, ASR, semantic similarity, transferability를 어떻게 함께 측정해야 하는가? |
| RQ4 | NLP defense는 adversarial training, input preprocessing, detection, certified robustness로 어떻게 구분되는가? |
| RQ5 | W04 toy word substitution 결과를 실제 Transformer 취약성으로 과장하지 않기 위해 어떤 한계가 필요한가? |

---

## 3. 핵심 이론 및 수식

### 3.1 NLP Adversarial Risk

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

### 3.2 Attack Success Rate

공격 성공률은 공격 입력에서 목표 실패가 발생한 비율이다.

$$
ASR=\frac{1}{m}\sum_{j=1}^{m}\mathbf{1}[f_{\theta}(x_j^{adv})\neq y_j]
$$

| 기호 | 의미 |
|---|---|
| $ASR$ | Attack Success Rate |
| $x_j^{adv}$ | 대적 텍스트 입력 |
| $y_j$ | 정답 레이블 |
| $m$ | 공격 평가 샘플 수 |

### 보안적 의미

Clean accuracy가 높아도 ASR이 높으면 모델은 보안적으로 취약하다. W04에서는 keyword detector toy 결과와 실제 Transformer 성능을 분리해 해석해야 한다.

---

### 3.3 Semantic Similarity Constraint

텍스트 공격은 원문의 의미를 유지해야 평가가 타당하다.

$$
Sim(x,x_{alt}) \geq \tau
$$

| 기호 | 의미 |
|---|---|
| $Sim(\cdot)$ | 의미 유사도 함수 |
| $\tau$ | 의미 보존 threshold |

### 보안적 의미

의미가 바뀐 입력으로 모델이 달라지는 것은 보안 취약성이라기보다 다른 입력에 대한 정상 반응일 수 있다. 따라서 semantic similarity와 human validity를 공격 평가에 포함해야 한다.

---

## 4. AI 원리 관점 분석

| 항목 | 분석 |
|---|---|
| Character-level Attack | 오탈자, 문자 삽입/삭제, homoglyph 등으로 표면형을 교란한다. |
| Word-level Attack | 동의어 치환, 우회 표현, token substitution을 사용한다. |
| Sentence-level Attack | paraphrase나 문장 구조 변환으로 모델 판단을 흔든다. |
| Semantic Constraint | 의미 보존 여부가 공격 타당성의 핵심이다. |
| Transferability | 한 모델에서 만든 공격이 다른 모델에도 통할 수 있다. |
| Defense | adversarial training, input correction, detection, certified robustness 등이 있다. |

---

## 5. 보안 이슈 관점 분석

| 보안 항목 | NLP robustness 관점 해석 |
|---|---|
| 무결성 | 입력 표현을 조금 바꿔 모델 판단을 왜곡한다. |
| 가용성 | 과도한 방어가 정상 입력을 차단하면 서비스성이 낮아진다. |
| 기밀성 | 공격자가 반복 질의로 모델의 약점과 정책을 추론할 수 있다. |
| 책임성 | 원문, 변형문, 의미 유사도, 공격 판정, 방어 결과를 기록해야 한다. |
| 운영 리스크 | 키워드 필터는 우회 표현에 취약하고, 과차단/미탐 trade-off가 발생한다. |

---

## 6. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 대상 | 사용자 입력, 분류 결과, 정책 판단, NLP filter, prompt wrapper |
| 공격자 목표 | 오분류, policy bypass, keyword filter 우회, harmful output 유도 |
| 공격자 능력 | typo, character edit, word substitution, paraphrase, repeated query |
| 공격 경로 | text input → tokenizer → Transformer/NLP model → decision/output |
| 제외 범위 | 실제 서비스 무단 공격, 유해 콘텐츠 생성, 개인정보 포함 공격 실험 |

---

## 7. 평가방법 및 지표

| 지표 | 의미 | W04/P04에서의 활용 |
|---|---|---|
| Clean Accuracy | 정상 텍스트 성능 | baseline utility |
| Robust Accuracy | 변형 텍스트 조건 성능 | 방어 성능 |
| ASR | 공격 성공률 | 공격 효과 |
| Semantic Similarity | 원문과 변형문의 의미 유사도 | 공격 타당성 |
| Fluency/Grammar | 자연스러움 | human validity |
| Transferability | 모델 간 공격 이전성 | black-box 위험 |
| Over-refusal | 정상 요청 과차단 | 방어 부작용 |
| Latency | 방어 적용 지연 | 운영 가능성 |

---

## 8. 재현성 점검

| 항목 | 점검 |
|---|---|
| 데이터 | 공개 NLP classification dataset 또는 toy prompt set |
| 공격 | 안전한 word substitution, typo, paraphrase toy set만 사용 |
| 모델 | keyword detector, small classifier, Transformer model 구분 |
| 설정 | transformation rule, semantic threshold, seed 기록 |
| 평가 | clean accuracy, ASR, semantic similarity, over-refusal 분리 |
| 한계 | toy keyword detector 결과를 실제 Transformer 취약성으로 일반화하지 않음 |

---

## 9. 논문의 고유 기여

1. NLP adversarial attack과 defense taxonomy를 제공한다.
2. 텍스트 공격 평가에서 의미 보존과 자연스러움이 중요함을 정리한다.
3. Clean performance와 robust performance를 분리해야 한다는 핵심 근거를 제공한다.
4. W04 toy word substitution 실험을 안전한 축소 실험으로 해석하게 해준다.

---

## 10. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| LLM prompt injection 직접성 제한 | NLP adversarial robustness가 중심이며 RAG/agent prompt injection은 별도 문헌 필요 | W08과 연결한다. |
| 의미 보존 평가 어려움 | semantic similarity 수치만으로 인간 의미 판단을 대체하기 어렵다. | 예시와 한계를 병기한다. |
| 최신 LLM 방어 변화 | instruction-tuned LLM의 공격·방어는 빠르게 변한다. | W07/W08 최신 문헌과 결합한다. |
| 악용 위험 | 공격 절차 상세화는 부적절하다. | toy/public data와 방어 중심으로 제한한다. |

---

## 11. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 2장 관련연구 | NLP adversarial attack/defense taxonomy |
| 3장 위협모형 | character/word/sentence level 공격자 능력 정의 |
| 4장 연구방법 | robust accuracy, ASR, semantic similarity, over-refusal 지표 설계 |
| 5장 분석 | toy word substitution 결과와 한계 제시 |
| 6장 보안적 함의 | 무결성, 가용성, 책임성 해석 |

---

## 12. 기말논문 연결 3문장

1. 이 주차에서 기말논문에 반영할 개념: NLP 보안 평가는 의미를 보존하는 텍스트 변형에서 모델 판단이 얼마나 안정적인지 clean/robust/ASR로 분리해야 한다.
2. 이 주차에서 기말논문에 반영할 표·그림·실험: NLP adversarial taxonomy, ASR 수식, semantic similarity 조건, clean-robust-over-refusal 비교표를 반영한다.
3. 이 주차가 RAG 문서 오염/LLM 보안 감사 프레임워크와 연결되는 지점: RAG/LLM prompt injection도 텍스트 변형과 의미 보존 우회 표현을 이용하므로 P04의 NLP robustness 지표를 W08의 prompt injection 평가로 확장한다.

---

## 13. 최종 판단

P04는 W04의 핵심 보안 문헌이다. P01–P03이 Transformer 구조와 효율성을 제공한다면, P04는 NLP 입력 교란과 robust evaluation의 기준을 제공한다.

---

## 14. 변환 호환성 메모

```bash
pandoc P04_summary.md -o P04_summary.docx
pandoc P04_summary.md -o P04_summary.pdf --pdf-engine=xelatex
```
