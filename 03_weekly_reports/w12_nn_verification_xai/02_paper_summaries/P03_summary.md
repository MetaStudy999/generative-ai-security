# P03 Summary

## Adversarial Attacks in Explainable Machine Learning: A Survey of Threats Against Models and Humans — Jon Vadillo et al., WIREs Data Mining and Knowledge Discovery, 2024

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W12 신경망 검증(Neural Network Verification) & XAI Robustness |
| 공식 논문명 | Adversarial Attacks in Explainable Machine Learning: A Survey of Threats Against Models and Humans |
| 공식 저자 | Jon Vadillo et al. |
| 공식 출판 정보 | WIREs Data Mining and Knowledge Discovery, 2024 |
| DOI | https://doi.org/10.1002/widm.1567 |
| 로컬 PDF | `01_papers/pdf/03_RELATED_Baniecki_Biecek_2023_Adversarial_XAI_Survey.pdf` |
| 로컬 PDF 상태 | W12 `paper_list.md` 기준 로컬 PDF는 Hubert Baniecki and Przemyslaw Biecek, `Adversarial attacks and defenses in explainable artificial intelligence: A survey`, arXiv:2306.06123 관련 보조 문헌이다. 공식 P03 DOI 논문과 동일 문헌으로 단정하지 않는다. |
| 검증 상태 | W12 `paper_list.md` 기준 관련 논문 공식 DOI 확인. 강의계획서의 `G. Vadillo et al.` 표기와 최종 반영표의 `Jon Vadillo et al.` 표기 차이, 로컬 PDF 차이 메모 유지 |
| PDF 확인 메모 | repo의 PDF 폴더에 P03 관련 PDF blob이 존재함을 확인했다. 다만 로컬 PDF는 공식 P03 지정 논문과 다르거나 보조 문헌이므로, summary는 공식 DOI 기준 P03을 중심으로 작성하고 로컬 PDF는 adversarial XAI 보완 문헌으로만 해석한다. |
| 핵심 근거 사용 가능 여부 | 가능. W12에서 XAI explanation robustness, attribution manipulation, explanation attack, human trust manipulation, evidence explanation audit를 설명하는 핵심 관련 문헌으로 사용 |

---

## 1. 한 문장 요약

공식 P03 논문은 explainable machine learning에서 발생하는 adversarial attacks를 **explanation manipulation, attribution attack, saliency map distortion, prediction-preserving explanation attack, explanation-preserving prediction attack, human trust manipulation, explanation robustness, model-human threat, auditability** 관점에서 정리하며, W12에서 설명가능성(XAI)을 단순 시각화 도구가 아니라 **공격자가 조작할 수 있는 보안 자산과 감사 대상**으로 재정의하는 핵심 관련 문헌이다.

---

## 2. 핵심 연구문제

> XAI는 모델의 판단 근거를 설명해 신뢰와 책임성을 높이기 위한 기술이지만, 공격자가 설명 결과를 조작하면 사용자는 잘못된 원인을 믿거나 위험 feature를 보지 못할 수 있다. 따라서 XAI 보안 평가는 예측 정확도뿐 아니라 설명 안정성, attribution 일관성, 인간 의사결정 영향까지 함께 다루어야 한다.

| 번호 | 연구질문 |
|---|---|
| RQ1 | 공격자는 모델 예측을 바꾸지 않고도 saliency map, feature attribution, counterfactual explanation 같은 설명 결과를 조작할 수 있는가? |
| RQ2 | Explanation attack은 prediction attack과 어떤 점에서 다르며, 두 공격은 독립적 또는 결합적으로 발생할 수 있는가? |
| RQ3 | XAI가 사용자 신뢰를 높이는 동시에 공격자가 신뢰를 악용할 수 있는 공격면이 되는가? |
| RQ4 | Explanation robustness는 stability, attribution similarity, faithfulness, prediction consistency, human trust error로 어떻게 평가할 수 있는가? |
| RQ5 | 로컬 PDF가 공식 DOI 논문과 다른 관련 문헌일 때, XAI robustness summary와 참고문헌 인용을 어떻게 분리 관리해야 하는가? |

---

## 3. 논문의 핵심 기여

| 기여 | 설명 | W12 연결 |
|---|---|---|
| Adversarial XAI taxonomy | XAI를 대상으로 하는 공격을 explanation manipulation, attribution attack, model-human attack으로 분류 | W12 XAI robustness 핵심 |
| Prediction과 explanation 분리 | 예측은 유지되지만 설명만 변하는 공격, 설명은 유지되지만 예측이 변하는 공격을 구분 | explanation stability 평가 근거 |
| Human trust 관점 | 설명 조작이 사용자 판단과 책임성에 미치는 영향을 threat model에 포함 | 보안 보고서의 설명 감사 연결 |
| Evaluation metric 정리 | attribution similarity, explanation stability, faithfulness, prediction consistency 등을 강조 | W12 평가표 설계 |
| 로컬 PDF 관리 주의 | W12 P03은 공식 DOI와 로컬 PDF가 다르므로 인용 기준 분리가 필요 | 기말논문 참고문헌 검증표 근거 |

---

## 4. 목차별 핵심 개괄

| 목차 | 핵심 내용 | 비전공자용 이해 |
|---|---|---|
| 1. Introduction | XAI는 모델 결정의 근거를 설명하지만, 설명 자체도 공격 대상이 될 수 있다. | AI가 답만 틀리는 것이 아니라 “왜 그렇게 판단했는지” 설명도 속일 수 있다. |
| 2. Background on XAI | Saliency map, feature attribution, LIME/SHAP, counterfactual explanation, example-based explanation 등 XAI 유형을 정리한다. | AI 판단에서 어느 feature가 중요했는지 보여주는 다양한 방법이 있다. |
| 3. Adversarial Threats to Explanations | 입력 perturbation이나 모델 조작으로 설명 결과를 왜곡하는 공격을 분류한다. | 사람이 보기에는 비슷한 입력인데 설명 그림이나 중요 feature가 크게 달라질 수 있다. |
| 4. Attacks Against Models and Humans | 공격은 모델 예측뿐 아니라 인간 사용자의 신뢰, 판단, 책임 추적을 오도할 수 있다. | 사용자가 설명을 믿고 잘못된 결정을 할 수 있다. |
| 5. Explanation Robustness Metrics | Explanation stability, attribution similarity, faithfulness, prediction consistency, human trust error 등을 평가한다. | 설명이 입력의 작은 변화에도 안정적인지, 실제 모델 판단과 맞는지 확인해야 한다. |
| 6. Defenses and Auditing | Robust explanation, stable attribution, explanation ensemble, sanity check, adversarial testing, human-centered audit가 필요하다. | 설명도 테스트하고 감사해야 한다. 예쁜 그림이라고 믿으면 안 된다. |
| 7. Challenges | 설명의 정답 부재, 사람 평가의 주관성, visualization 설정 민감성, adaptive explanation attack이 과제로 남는다. | 설명이 좋은지 나쁜지 평가하기가 어렵고, 설정 하나로 다르게 보일 수 있다. |
| 8. Future Directions | XAI robustness benchmark, human-in-the-loop evaluation, explanation certificate, governance, audit log가 필요하다. | 설명가능성도 표준화된 보안 평가와 기록이 필요하다. |
| 로컬 관련 PDF 메모 | 로컬 PDF는 Baniecki/Biecek 2023 adversarial XAI 관련 문헌으로 보이며, official P03과 동일 문헌으로 단정하지 않는다. | PDF가 있다고 해서 공식 지정 논문과 동일하게 인용하면 안 된다. |

---

## 5. 핵심 이론 및 수식

> 아래 수식은 XAI robustness와 adversarial explanation 평가를 W12 보고서에서 설명하기 위한 표준화된 표현이다. 실제 공격 절차 제공이 아니라 평가 지표와 감사 구조를 설명하기 위한 것이다.

### 5.1 Explanation Function

모델 $f$와 입력 $x$에 대해 설명기 $E$가 feature attribution 또는 explanation을 생성한다.

$$
e=E(f,x)
$$

| 기호 | 의미 |
|---|---|
| $f$ | target model |
| $x$ | 입력 |
| $E$ | explainer 또는 explanation method |
| $e$ | saliency map, attribution vector, counterfactual explanation 등 |

### 보안적 의미

보호 대상은 모델 예측뿐 아니라 explanation output이다. explanation이 조작되면 모델 감사와 사용자 판단이 왜곡될 수 있다.

---

### 5.2 Explanation Stability

입력의 작은 변화에 대해 explanation이 얼마나 안정적인지 평가한다.

$$
Stability=1-\frac{\|E(f,x)-E(f,x')\|}{\|x-x'\|+\eta}
$$

| 기호 | 의미 |
|---|---|
| $x'$ | perturbation된 입력 |
| $\eta$ | 분모 안정화를 위한 작은 값 |

### 보안적 의미

예측이 같아도 explanation이 크게 바뀌면 사용자가 판단 근거를 잘못 이해할 수 있다.

---

### 5.3 Prediction-Preserving Explanation Attack

예측은 유지하되 설명만 바꾸는 공격 목표다.

$$
\max_{x'\in B_\epsilon(x)} Dist(E(f,x),E(f,x'))\quad \text{s.t.}\quad f(x')=f(x)
$$

### 보안적 의미

이 경우 일반 accuracy나 robust accuracy만 보면 공격을 놓친다. XAI 보안에서는 prediction consistency와 explanation similarity를 함께 봐야 한다.

---

### 5.4 Explanation-Preserving Prediction Attack

설명은 비슷하게 유지하면서 예측을 바꾸는 공격도 가능하다.

$$
\max_{x'\in B_\epsilon(x)} \ell(f(x'),y)\quad \text{s.t.}\quad Sim(E(f,x),E(f,x'))\geq \tau
$$

### 보안적 의미

설명이 비슷하게 보인다고 해서 예측이 안전하다는 뜻은 아니다. 설명과 예측의 결합 평가가 필요하다.

---

### 5.5 Attribution Similarity

두 explanation의 유사도를 측정한다.

$$
AttributionSim=\frac{E(f,x)\cdot E(f,x')}{\|E(f,x)\|\|E(f,x')\|}
$$

### 보안적 의미

Saliency map이나 feature attribution이 얼마나 일관적인지 정량화할 수 있다. 단, visualization normalization 설정에 민감하므로 기록이 필요하다.

---

### 5.6 Faithfulness Gap

Explanation이 실제 모델 판단에 얼마나 충실한지 평가한다.

$$
FaithfulnessGap=|Importance_{explanation}-Impact_{model}|
$$

### 보안적 의미

설명이 보기에는 그럴듯해도 실제 모델 판단 원인과 다르면 책임 추적에 실패한다.

---

### 5.7 Human Trust Error

설명 조작이 사용자 판단을 얼마나 오도했는지 평가한다.

$$
HumanTrustError=\frac{N_{wrong\ decisions\ with\ misleading\ explanations}}{N_{decisions\ with\ explanations}}
$$

### 보안적 의미

XAI는 사람을 설득하는 도구이므로, 설명 조작은 모델 보안뿐 아니라 인간 의사결정 보안 문제다.

---

## 6. AI 원리 70% 관점 분석

| 원리 항목 | 설명 | W12/P03에서의 의미 |
|---|---|---|
| Explainable AI | 모델 판단 근거를 사람이 이해할 수 있게 표현 | 설명 자체가 평가 대상 |
| Feature Attribution | feature별 중요도 계산 | 공격자가 조작할 수 있는 출력 |
| Saliency Map | 입력 영역별 중요도 시각화 | visualization attack 대상 |
| Counterfactual Explanation | 입력 변화와 decision 변화를 연결 | 조작 시 잘못된 행동 지침 유도 가능 |
| Explanation Stability | 작은 입력 변화에 설명이 안정적인지 | XAI robustness 핵심 지표 |
| Faithfulness | 설명이 실제 모델 판단 원인을 반영하는지 | 신뢰성 평가 |
| Human-Centered XAI | 사람이 설명을 보고 판단 | trust manipulation threat |
| Explanation Audit | 설명 생성 과정과 설정 기록 | W15 evidence chain 연결 |

---

## 7. 보안 이슈 30% 관점 분석

| 보안 항목 | Adversarial XAI 관점 해석 | 대표 평가 지표 |
|---|---|---|
| 기밀성 | explanation이 민감 feature나 내부 모델 동작을 노출할 수 있음 | explanation leakage risk |
| 무결성 | attribution과 saliency가 조작되어 잘못된 판단 근거 제공 | attribution similarity, faithfulness gap |
| 가용성 | 복잡한 explanation defense가 inference latency와 사용자 경험을 저하시킬 수 있음 | explanation latency, usability cost |
| 프라이버시 | explanation이 training data나 민감 속성을 암시할 수 있음 | feature leakage, example leakage |
| 안전성 | 잘못된 explanation이 의료·보안·법률 판단을 오도할 수 있음 | human trust error, safety decision error |
| 책임성 | 설명 생성 설정과 결과를 기록해야 감사 가능 | explainer config completeness, explanation audit log |

---

## 8. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | model explanation, saliency map, feature attribution, counterfactual explanation, human trust, audit evidence, explainer configuration |
| 공격자 목표 | 설명 왜곡, 위험 feature 은폐, 책임 회피, 사용자 판단 오도, 모델 예측과 설명의 불일치 유도 |
| 공격자 능력 | input perturbation, explanation query, surrogate model 보유, explainer setting 관찰, visualization normalization 악용 |
| 공격 경로 | input perturbation → model prediction → explanation generation → user/auditor interpretation → wrong trust decision |
| 방어자 능력 | explanation robustness test, sanity check, attribution similarity 평가, faithfulness audit, human-in-the-loop evaluation, config logging |
| 제외 범위 | 실제 시스템 공격, 구체적 adversarial example 생성 절차, 사람 대상 조작 실험, 악용 코드 제공 |

---

## 9. 평가방법 및 지표

| 평가축 | 지표 | 의미 | W12/P03 활용 |
|---|---|---|---|
| 예측 일관성 | prediction consistency, robust accuracy | 예측이 유지되는지 | P02와 연결 |
| 설명 안정성 | Stability, AttributionSim | 설명이 작은 변화에 안정적인지 | XAI robustness 핵심 |
| 설명 충실도 | FaithfulnessGap, deletion/insertion score | 설명이 실제 모델 원인과 맞는지 | 책임성 평가 |
| 사용자 영향 | HumanTrustError, trust calibration | 설명이 사람 판단에 미치는 영향 | model-human threat |
| 공격 성공 | explanation attack success, distortion score | 설명 조작 성공 정도 | adversarial XAI 평가 |
| 비용 | explanation latency, usability cost | 설명 방어의 운영 비용 | 실무 적용성 |
| 재현성 | explainer version, baseline, visualization setting | 설명 재현 가능성 | W15 evidence chain |
| 서지 정확성 | official DOI match, local PDF mismatch flag | 참고문헌 정확성 | 기말논문 검증표 |

---

## 10. 재현성 체크리스트

| 항목 | 기록해야 할 내용 |
|---|---|
| Bibliographic status | 공식 DOI 논문과 로컬 PDF 동일 여부, mismatch flag |
| Model | architecture, dataset, model hash, prediction output |
| Explainer | LIME/SHAP/saliency/Integrated Gradients/counterfactual 등 method와 version |
| Explanation setting | baseline, reference, normalization, visualization scale, random seed |
| Attack setting | perturbation norm, epsilon, prediction-preserving 여부, target explanation 여부 |
| Metrics | Stability, AttributionSim, FaithfulnessGap, HumanTrustError, prediction consistency |
| Human evaluation | 사람 평가 여부, 평가자 수, task, bias control |
| Logs | input/output, explanation image/vector, config, seed, failure case |
| Local PDF note | 로컬 PDF는 Baniecki/Biecek 관련 문헌임을 별도 표시하고 공식 P03처럼 인용하지 않음 |
| 한계 | explanation robustness 결과를 전체 모델 안전성 보장으로 과장하지 않음 |

---

## 11. 논문의 고유 기여

1. Explainable machine learning 자체가 adversarial attack의 대상이 될 수 있음을 체계화한다.
2. Prediction robustness와 explanation robustness를 분리해 평가해야 함을 보여준다.
3. Saliency map, feature attribution, counterfactual explanation 등 XAI output의 조작 가능성을 threat model에 포함한다.
4. XAI의 보안 문제를 사람의 신뢰·판단·책임성 문제까지 확장한다.
5. W12 기말논문에서 evidence explanation audit와 citation/explanation robustness 평가표를 설계하는 근거를 제공한다.

---

## 12. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 로컬 PDF 불일치 | P03 로컬 PDF는 공식 DOI 논문과 다른 Baniecki/Biecek 관련 문헌이다. | 공식 DOI 기준으로 인용하고 로컬 PDF는 보완 문헌으로 표시 |
| 설명 정답 부재 | explanation은 ground truth가 명확하지 않은 경우가 많다. | stability, faithfulness, human evaluation을 병행 |
| Visualization 민감성 | normalization, color map, baseline 설정에 따라 설명이 달라진다. | explainer setting과 visualization config 기록 |
| Human evaluation 비용 | 사람 판단 영향 평가가 어렵고 주관적이다. | toy task와 제한된 human-trust rubric 제안 |
| Adaptive attacker | 공격자가 explainer를 알고 우회할 수 있다. | adaptive explanation attack을 한계로 명시 |
| Prediction과 explanation 분리 | 예측이 안전해도 explanation이 위험할 수 있고, 반대도 가능하다. | prediction consistency와 explanation stability를 함께 보고 |

---

## 13. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | 설명가능성은 신뢰를 높이는 동시에 공격자가 조작할 수 있는 보안 자산이라는 문제의식 |
| 2장 관련연구 | 공식 P03 DOI 논문을 adversarial XAI survey로 정리하고, 로컬 PDF mismatch는 검증표에 기록 |
| 3장 위협모형 | explanation, attribution, saliency map, human trust, audit evidence 보호 자산 정의 |
| 4장 연구방법 | Stability, AttributionSim, FaithfulnessGap, HumanTrustError, prediction consistency 지표 설계 |
| 5장 분석 | prediction robustness와 explanation robustness 분리표, XAI audit workflow 제시 |
| 6장 보안적 함의 | RAG/LLM citation explanation, evidence manipulation, human trust audit 필요성 해석 |

---

## 14. 기말논문 연결 3문장

1. W12에서 기말논문에 반영할 개념: XAI 보안은 모델 예측이 맞는지뿐 아니라 설명이 안정적이고 충실하며 사용자의 판단을 오도하지 않는지를 함께 평가해야 한다.
2. W12에서 기말논문에 반영할 표·그림·실험: explanation attack objective, Stability·AttributionSim·FaithfulnessGap 평가표, prediction robustness vs explanation robustness 비교표, 공식 DOI/로컬 PDF mismatch 검증표를 반영한다.
3. W12가 LLM/RAG 보안 감사 프레임워크와 연결되는 지점: RAG/LLM의 citation, rationale, chain-of-evidence도 explanation output이므로, citation manipulation, evidence mismatch, user trust error, explanation audit log를 W14/W15 evidence chain에 포함해야 한다.

---

## 15. 최종 판단

P03은 W12의 XAI robustness 핵심 관련 문헌이다. 다만 W12 `paper_list.md` 기준 로컬 PDF는 공식 DOI 논문과 다른 Baniecki/Biecek 2023 adversarial XAI 관련 문헌으로 기록되어 있으므로, 기말논문 참고문헌에는 공식 DOI 논문인 Jon Vadillo et al.의 WIREs Data Mining and Knowledge Discovery 논문을 우선 사용해야 한다. 로컬 PDF는 adversarial XAI 일반 배경을 보완하는 관련 문헌으로만 제한해 활용하는 것이 적절하다.

---

## 16. 변환 호환성 메모

```bash
pandoc P03_summary.md -o P03_summary.docx
pandoc P03_summary.md -o P03_summary.pdf --pdf-engine=xelatex
```
