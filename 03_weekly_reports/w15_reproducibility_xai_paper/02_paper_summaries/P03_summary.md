# P03 Summary

## Explainable AI: Core Ideas, Techniques, and Solutions — Rudresh Dwivedi et al., ACM Computing Surveys, 2023

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W15 Reproducibility, XAI & Final Paper Bridge |
| 공식 논문명 | Explainable AI: Core Ideas, Techniques, and Solutions |
| 공식 저자 | Rudresh Dwivedi et al. |
| 공식 출판 정보 | ACM Computing Surveys, Vol. 55, Issue 9, Article 131, 2023 |
| DOI | https://doi.org/10.1145/3561048 |
| 로컬 PDF | `01_papers/pdf/03_RELATED_Mersha_et_al_2024_Explainable_AI_Survey.pdf` |
| 로컬 PDF 상태 | W15 `doi_check.md` 기준 로컬 PDF는 `Mersha et al., Explainable Artificial Intelligence: A Survey of Needs, Techniques, Applications, and Future Direction` 관련 보조 문헌이다. 공식 P03 DOI 논문과 동일 문헌으로 단정하지 않는다. |
| 검증 상태 | W15 `doi_check.md` 기준 공식 DOI 확인. 공식 metadata의 제1저자는 Rudresh Dwivedi로 기록되어 있으며, 원 프롬프트의 Vivek Dwivedi 표기 및 로컬 PDF 차이는 최종 반영표 기준 공식 출판정보로 정리한다. |
| PDF 확인 메모 | repo의 PDF 폴더에 P03 관련 PDF blob이 존재함을 확인했다. 다만 로컬 PDF는 공식 P03 지정 논문과 다른 XAI survey 보조 문헌이므로, summary는 공식 DOI 기준 P03을 중심으로 작성하고 로컬 PDF는 XAI needs/applications/future direction 보완 문헌으로만 해석한다. |
| 핵심 근거 사용 가능 여부 | 가능. W15에서 XAI core ideas, interpretability, explainability, transparency, post-hoc explanation, fidelity, stability, human-centered explanation, explanation evaluation, final paper XAI evidence의 핵심 문헌으로 사용 |

---

## 1. 한 문장 요약

공식 P03 논문은 XAI를 **interpretability, explainability, transparency, model-specific/model-agnostic explanation, post-hoc explanation, ante-hoc/interpretable model, feature attribution, surrogate explanation, example-based explanation, counterfactual explanation, saliency, fidelity, stability, comprehensibility, human trust, explanation robustness, explanation misuse, reproducibility of explanations** 관점에서 정리하며, W15에서 최종 논문의 XAI를 단순 시각화가 아니라 **검증 가능한 설명 evidence와 평가 지표**로 다루게 하는 핵심 문헌이다.

---

## 2. 핵심 연구문제

> XAI는 모델을 설명하는 그림이나 문장을 생성하는 것에서 끝나지 않는다. 설명이 실제 모델 동작을 충실하게 반영하는지, 작은 입력 변화에도 안정적인지, 사람이 이해할 수 있는지, 설명이 오히려 사용자를 오도하거나 개인정보를 노출하지 않는지 평가해야 한다. 따라서 최종 논문에서 XAI는 시각자료가 아니라 fidelity·stability·human agreement·reproducibility가 기록된 평가 대상이어야 한다.

| 번호 | 연구질문 |
|---|---|
| RQ1 | Interpretability, explainability, transparency는 어떤 차이를 가지며, XAI 연구에서 어떻게 구분해야 하는가? |
| RQ2 | Model-agnostic, model-specific, post-hoc, ante-hoc explanation은 각각 어떤 장단점과 적용 조건을 갖는가? |
| RQ3 | Feature attribution, surrogate model, saliency map, counterfactual explanation, example-based explanation은 어떤 방식으로 모델 판단을 설명하는가? |
| RQ4 | 좋은 설명은 fidelity, stability, comprehensibility, human agreement, robustness 기준에서 어떻게 평가되어야 하는가? |
| RQ5 | AI 보안·RAG·LLM 평가에서 설명은 어떤 경우에 misleading explanation, privacy leakage, explanation overclaim 위험을 만들 수 있는가? |

---

## 3. 논문의 핵심 기여

| 기여 | 설명 | W15 연결 |
|---|---|---|
| XAI 핵심 개념 정리 | interpretability, explainability, transparency, trustworthiness의 개념을 구분 | W15 XAI 이론 기반 |
| 기법 taxonomy 제시 | feature attribution, surrogate explanation, saliency, counterfactual, example-based explanation 등 정리 | 최종 논문 관련연구 |
| 평가 기준 제시 | fidelity, stability, comprehensibility, human trust, robustness 등 설명 품질 기준 제시 | XAI 평가표 설계 |
| 한계와 위험 강조 | 설명이 모델을 충실히 반영하지 않거나 사용자를 오도할 수 있음을 제시 | 보안적 함의 |
| 재현성 요구 연결 | explainer, baseline, parameters, visualization setting, human review 기록 필요성 제시 | W15 evidence chain |

---

## 4. 목차별 핵심 개괄

| 목차 | 핵심 내용 | 비전공자용 이해 |
|---|---|---|
| 1. Introduction | 복잡한 AI 모델의 결정 과정을 이해하고 신뢰하기 위해 XAI가 필요하다. | AI가 왜 그런 답을 했는지 설명하는 기술이다. |
| 2. Core Concepts | interpretability, explainability, transparency, trust, accountability의 차이를 설명한다. | 설명 가능하다는 말에도 여러 단계가 있다. |
| 3. Taxonomy of XAI | model-specific/model-agnostic, global/local, intrinsic/post-hoc, visual/textual explanation을 분류한다. | 설명은 전체 모델을 설명할 수도 있고, 한 개 결과만 설명할 수도 있다. |
| 4. Feature Attribution | 입력 feature가 예측에 얼마나 기여했는지 계산하는 방법을 정리한다. | 어떤 단어, 픽셀, 변수 때문에 이런 결과가 나왔는지 보는 방식이다. |
| 5. Surrogate Explanations | 복잡한 모델 주변을 단순 모델로 근사해 설명한다. | 어려운 모델을 잠시 쉬운 모델로 흉내 내 설명한다. |
| 6. Counterfactual Explanations | 어떤 입력을 어떻게 바꾸면 결과가 바뀌는지 제시한다. | “이 조건이 달랐다면 다른 결과가 나왔을 것”을 설명한다. |
| 7. Example-based Explanations | 유사 사례, prototype, influential sample을 통해 모델 판단을 설명한다. | 과거 어떤 사례와 비슷해서 이렇게 판단했는지 보여준다. |
| 8. Evaluation of XAI | fidelity, stability, human interpretability, usefulness, robustness, fairness를 평가한다. | 설명도 정확하고 안정적인지 검사해야 한다. |
| 9. Applications and Challenges | 의료, 금융, 보안, 법률 등 고위험 분야에서 XAI의 필요성과 한계를 논의한다. | 중요한 분야일수록 설명과 책임성이 더 중요하다. |
| 10. Future Directions | human-centered XAI, reproducible XAI, robust explanation, privacy-aware explanation이 과제로 남는다. | 설명도 검증 가능하고 안전해야 한다. |
| 로컬 관련 PDF 메모 | 로컬 PDF는 Mersha et al.의 관련 XAI survey로, official P03와 동일 문헌으로 인용하지 않는다. | PDF가 있다고 해서 공식 지정 논문으로 인용하면 안 된다. |

---

## 5. 핵심 이론 및 수식

> 아래 수식은 XAI 설명 품질과 W15 최종 논문 XAI evidence chain을 설명하기 위한 표준화된 표현이다. 수식은 GitHub, MS Word, PDF 변환 호환성을 위해 Markdown 표 밖의 LaTeX block math로 작성한다.

### 5.1 Explanation Fidelity

설명 모델 $g$가 원 모델 $f$의 판단을 얼마나 충실히 근사하는지 측정한다.

$$
Fidelity=1-\frac{1}{N}\sum_{i=1}^{N}\mathbf{1}[g(x_i)\neq f(x_i)]
$$

| 기호 | 의미 |
|---|---|
| $f$ | 설명 대상 원 모델 |
| $g$ | 설명용 surrogate 또는 explainer model |
| $x_i$ | 평가 입력 |

### 보안적 의미

fidelity가 낮은 설명은 실제 모델 동작과 다를 수 있다. 설명이 그럴듯해도 모델을 충실히 반영하지 않으면 잘못된 보안 판단으로 이어진다.

---

### 5.2 Explanation Stability

입력이 조금 바뀌었을 때 설명이 과도하게 흔들리는지 평가한다.

$$
Stability=1-\frac{\|E(x)-E(x')\|}{\|x-x'\|+\epsilon}
$$

| 기호 | 의미 |
|---|---|
| $E(x)$ | 입력 $x$에 대한 explanation |
| $x'$ | 작은 변형 입력 |
| $\epsilon$ | 0 나눗셈 방지 상수 |

### 보안적 의미

입력이 거의 같은데 설명이 크게 바뀌면 설명의 신뢰성이 낮다. adversarial explanation attack 탐지에도 중요하다.

---

### 5.3 Local Explanation Agreement

동일 sample에 대해 여러 explainer 또는 human reviewer가 얼마나 일치하는지 측정한다.

$$
Agreement=\frac{1}{M}\sum_{j=1}^{M}\mathbf{1}[E_j(x)\approx E_{ref}(x)]
$$

### 보안적 의미

설명 평가에는 사람의 이해와 전문가 검토가 필요할 수 있다. Agreement가 낮으면 설명 결과를 단정적으로 해석하면 안 된다.

---

### 5.4 Explanation Complexity

설명이 얼마나 간결한지 측정한다.

$$
Complexity(E)=|Features_{used}|+|Rules|+Depth_{tree}
$$

### 보안적 의미

설명이 너무 복잡하면 사람이 이해하기 어렵고, 너무 단순하면 모델 동작을 왜곡할 수 있다.

---

### 5.5 Explanation Robustness

공격 또는 변형 후에도 설명이 유지되는 정도다.

$$
Robustness_E=\frac{Sim(E(x),E(x'))}{1+AttackStrength}
$$

### 보안적 의미

설명은 adversarial perturbation, prompt change, data shift에도 일정 수준 안정성을 가져야 한다.

---

### 5.6 Explanation Privacy Risk

설명이 민감한 training data나 private feature를 노출할 위험을 요약한다.

$$
PrivacyRisk_E=\alpha SensitiveFeatureExposure+\beta TrainingExampleLeakage+\gamma MembershipSignal
$$

### 보안적 의미

설명은 투명성을 높이지만, 지나친 설명은 개인정보나 모델 내부 정보를 노출할 수 있다.

---

### 5.7 XAI Evidence Score

설명 품질과 재현성을 종합적으로 평가한다.

$$
XAIEvidence=\alpha Fidelity+\beta Stability+\gamma Agreement-\lambda Complexity-\mu PrivacyRisk_E
$$

### 보안적 의미

좋은 XAI evidence는 충실하고 안정적이며 사람이 검토 가능하고, 과도한 복잡도와 프라이버시 노출 위험이 낮아야 한다.

---

## 6. AI 원리 70% 관점 분석

| 원리 항목 | 설명 | W15/P03에서의 의미 |
|---|---|---|
| Interpretability | 모델 구조나 결과를 사람이 이해할 수 있는 정도 | XAI 핵심 개념 |
| Explainability | 모델 판단에 대한 설명을 제공하는 능력 | 최종 논문 설명 근거 |
| Transparency | 모델 내부와 과정의 공개·추적 가능성 | audit 가능성 |
| Post-hoc Explanation | 학습 후 별도 explainer로 설명 | LIME/SHAP류 접근 |
| Ante-hoc/Intrinsic Model | 구조 자체가 해석 가능한 모델 | 투명성 높은 설계 |
| Feature Attribution | feature 기여도 계산 | RAG/LLM 근거성 연결 |
| Counterfactual Explanation | 결과가 바뀌는 최소 변화 설명 | 정책·대응 해석 |
| Human-centered XAI | 사용자 이해와 의사결정 지원 | 책임성·검토 가능성 |

---

## 7. 보안 이슈 30% 관점 분석

| 보안 항목 | XAI 관점 해석 | 대표 평가 지표 |
|---|---|---|
| 기밀성 | 설명이 모델 내부, 민감 feature, training example을 노출할 수 있음 | PrivacyRisk_E, leakage check |
| 무결성 | 설명이 실제 모델 동작과 다르면 사용자를 오도 | Fidelity, agreement |
| 가용성 | 복잡한 설명 계산이 비용과 지연을 만들 수 있음 | explanation latency, complexity |
| 프라이버시 | feature attribution과 example explanation이 개인정보를 드러낼 수 있음 | sensitive feature exposure |
| 안전성 | 잘못된 설명은 잘못된 의료·보안·법률 판단을 유도 | human error rate, explanation usefulness |
| 책임성 | explainer, baseline, parameter, visualization setting을 기록해야 감사 가능 | XAI evidence completeness |

---

## 8. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | explanation, feature attribution, saliency map, counterfactual, model decision rationale, user trust, explainer config, human review log |
| 공격자/위험 목표 | misleading explanation 생성, explanation gaming, explanation manipulation, privacy leakage, explanation overclaim |
| 공격자/위험 능력 | input perturbation, prompt manipulation, explainer parameter 조작, favorable example 선택, visualization cherry-picking |
| 위험 경로 | model output 생성 → explainer 적용 → 낮은 fidelity/불안정 설명 → 사용자가 잘못된 근거를 신뢰 → 잘못된 보안·정책 결정 |
| 방어자 능력 | fidelity/stability evaluation, multiple explainer comparison, human review, baseline logging, privacy-aware explanation, limitation note |
| 제외 범위 | 실제 explanation attack 구현, 개인정보 추출 절차, 모델 내부정보 탈취, 허위 설명 조작 지원 |

---

## 9. 평가방법 및 지표

| 평가축 | 지표 | 의미 | W15/P03 활용 |
|---|---|---|---|
| 충실성 | Fidelity, local fidelity | 설명이 원 모델을 잘 반영하는지 | 핵심 XAI 평가 |
| 안정성 | Stability, Robustness_E | 작은 변화에도 설명이 안정적인지 | 설명 신뢰성 |
| 이해가능성 | Complexity, comprehensibility score | 사람이 이해 가능한지 | human-centered 평가 |
| 사람 검토 | Agreement, human usefulness | 전문가·사용자 일치도 | 책임성 평가 |
| 프라이버시 | PrivacyRisk_E, sensitive feature exposure | 설명의 정보 노출 위험 | 보안 평가 |
| 재현성 | explainer version, baseline, parameter log | 설명 재현 가능성 | W15 evidence chain |
| 위험성 | misleading explanation rate | 오도 가능성 | 안전성 평가 |
| 서지 정확성 | official DOI match, local PDF mismatch flag | 참고문헌 정확성 | reference audit |

---

## 10. 재현성 체크리스트

| 항목 | 기록해야 할 내용 |
|---|---|
| Bibliographic status | 공식 DOI 논문과 로컬 PDF 동일 여부, related flag |
| Model | model name, version, checkpoint/hash, task, dataset |
| Explainer | method name, library version, parameters, baseline/background data |
| Input | sample ID, preprocessing, perturbation 조건, prompt if LLM/RAG |
| Output | model prediction, confidence, generated answer, retrieved evidence |
| Explanation | attribution vector, saliency map, rule, counterfactual, visualization raw file |
| Evaluation | fidelity, stability, agreement, complexity, privacy risk |
| Human review | reviewer, rubric, disagreement note, decision log |
| Evidence | script commit, figure source, config, seed, raw explanation artifact |
| 한계 | 설명을 모델 진실 전체로 과장하지 않고, 설명 범위와 불확실성을 명시 |

---

## 11. 논문의 고유 기여

1. XAI의 핵심 개념과 주요 기법을 체계적으로 정리한다.
2. 설명가능성을 단순 시각화가 아니라 fidelity, stability, human understanding, robustness 기준으로 평가해야 함을 제시한다.
3. 설명이 신뢰와 책임성을 높일 수 있지만, 동시에 오도·과신·프라이버시 노출 위험을 만들 수 있음을 보여준다.
4. W15 최종논문의 XAI 장에서 explanation evidence와 reproducibility checklist를 설계하는 핵심 근거가 된다.
5. 로컬 PDF가 official P03와 다른 관련 문헌이므로, 최종 제출에서 reference verification과 related-paper flag를 유지해야 함을 보여준다.

---

## 12. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 로컬 PDF 불일치 | P03 로컬 PDF는 Mersha et al. 관련 XAI survey이며 공식 DOI 논문과 다르다. | 공식 DOI 기준으로 인용하고 관련 PDF 차이 메모 유지 |
| 설명의 충실성 한계 | post-hoc explainer는 실제 모델 동작을 완전히 반영하지 못할 수 있다. | Fidelity와 limitation 병기 |
| 설명 안정성 문제 | 작은 입력 변화에도 attribution이 크게 변할 수 있다. | Stability와 Robustness_E 평가 |
| 인간 이해의 주관성 | 사용자가 이해했다고 해서 설명이 정확한 것은 아니다. | human agreement와 expert review 기록 |
| 프라이버시 위험 | 설명이 민감 feature나 training example을 드러낼 수 있다. | PrivacyRisk_E와 redaction policy 추가 |
| 시각화 과신 | saliency map이나 attribution figure가 과도하게 설득력 있게 보일 수 있다. | raw data, baseline, method parameter 공개 |

---

## 13. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | AI 보안 연구에서 설명가능성은 신뢰와 감사 가능성의 핵심 요소라는 문제의식 |
| 2장 관련연구 | P03을 XAI core ideas, techniques, solutions 핵심 문헌으로 정리하고 로컬 PDF mismatch는 검증표에 기록 |
| 3장 위협모형 | explanation, attribution, counterfactual, user trust, explainer config, human review log 보호 자산 정의 |
| 4장 연구방법 | Fidelity, Stability, Agreement, Complexity, Robustness_E, PrivacyRisk_E, XAIEvidence 지표 설계 |
| 5장 분석 | XAI method taxonomy, explanation quality table, RAG answer evidence explanation table 제시 |
| 6장 보안적 함의 | misleading explanation, explanation overclaim, privacy leakage, human trust risk, reproducibility evidence 필요성 해석 |
| 부록 | explainer configuration, figure source, human review rubric, limitation note 수록 |

---

## 14. 기말논문 연결 3문장

1. W15에서 기말논문에 반영할 개념: XAI는 AI 모델의 판단을 설명하는 기술이지만, 설명 자체도 fidelity, stability, comprehensibility, privacy risk 기준으로 검증되어야 한다.
2. W15에서 기말논문에 반영할 표·그림·실험: Fidelity, Stability, Agreement, Complexity, Robustness_E, PrivacyRisk_E, XAIEvidence 수식표와 XAI method taxonomy table을 반영한다.
3. W15 최종 제출과 연결되는 지점: XAI 그림과 설명에는 explainer method, baseline, parameter, input sample, model version, raw explanation artifact, human review rubric이 연결되어야 최종 논문의 설명가능성과 재현성을 확보할 수 있다.

---

## 15. 최종 판단

P03은 W15의 XAI 평가축 핵심 문헌이다. 기말논문에서 설명가능성을 단순 그림이나 보조 시각자료로 처리하면 부족하며, 설명의 충실성·안정성·이해가능성·프라이버시 위험·재현성을 함께 평가해야 한다. 따라서 P03은 **XAI taxonomy, explanation quality metric, misleading explanation risk, XAI evidence chain, 최종 논문 설명가능성 장의 중심 근거 문헌**으로 사용하는 것이 적절하다.

---

## 16. 변환 호환성 메모

```bash
pandoc P03_summary.md -o P03_summary.docx
pandoc P03_summary.md -o P03_summary.pdf --pdf-engine=xelatex
```
