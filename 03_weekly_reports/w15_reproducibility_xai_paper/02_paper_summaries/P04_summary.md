# P04 Summary

## Explainable Artificial Intelligence (XAI): Concepts, taxonomies, opportunities and challenges toward responsible AI — Alejandro Barredo Arrieta et al., Information Fusion, 2020

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W15 Reproducibility, XAI & Final Paper Bridge |
| 논문명 | Explainable Artificial Intelligence (XAI): Concepts, taxonomies, opportunities and challenges toward responsible AI |
| 저자 | Alejandro Barredo Arrieta et al. |
| 공식 출판 정보 | Information Fusion, Vol. 58, pp. 82–115, 2020 |
| DOI | https://doi.org/10.1016/j.inffus.2019.12.012 |
| 로컬 PDF | `01_papers/pdf/04_Arrieta_et_al_2020_Explainable_AI_Concepts_Taxonomies.pdf` |
| 검증 상태 | W15 `doi_check.md`와 `paper_list.md` 기준 공식 DOI 확인. Information Fusion 58, pp. 82–115로 확인됨 |
| PDF 확인 메모 | repo의 PDF 폴더에 P04 관련 PDF blob이 존재함을 확인했다. 요약은 로컬 PDF 경로와 W15 `doi_check.md` 및 `paper_list.md`의 공식 DOI 메타데이터 기준으로 보완했다. |
| 핵심 근거 사용 가능 여부 | 가능. W15에서 Responsible AI, XAI taxonomy, transparency, interpretability, accountability, trust, human-centered evaluation, explanation risk, final paper security implications의 핵심 문헌으로 사용 |

---

## 1. 한 문장 요약

이 논문은 XAI를 **responsible AI, transparency, interpretability, explainability, accountability, trustworthiness, post-hoc explanation, intrinsic interpretability, model-agnostic/model-specific methods, global/local explanation, human-centered evaluation, ethical risk, fairness, privacy, robustness, automation bias** 관점에서 체계화하며, W15에서 최종 논문의 XAI를 단순한 그림이 아니라 **책임 있는 AI 의사결정의 증거와 거버넌스 통제**로 다루게 하는 핵심 문헌이다.

---

## 2. 핵심 연구문제

> AI 시스템이 사회적·보안적 의사결정에 사용될수록 “모델이 왜 그런 결정을 했는가”를 설명할 수 있어야 한다. 그러나 설명가능성은 단순한 시각화나 친절한 문장이 아니라, 투명성, 책임성, 사용자 이해, 한계 고지, 공정성, 프라이버시, 안전성까지 포함하는 responsible AI의 구성요소다.

| 번호 | 연구질문 |
|---|---|
| RQ1 | Explainability, interpretability, transparency, comprehensibility, accountability는 서로 어떻게 구분되는가? |
| RQ2 | XAI 기법은 model-agnostic/model-specific, global/local, intrinsic/post-hoc 관점에서 어떻게 분류되는가? |
| RQ3 | XAI는 responsible AI에서 trust, fairness, privacy, robustness, accountability와 어떤 관계를 갖는가? |
| RQ4 | 설명은 어떻게 사용자를 돕지만, 동시에 misleading explanation, fairwashing, privacy leakage, automation bias를 만들 수 있는가? |
| RQ5 | 기말논문에서 XAI를 보안적 함의와 책임성 장에 반영하려면 어떤 evidence와 limitation statement가 필요한가? |

---

## 3. 논문의 핵심 기여

| 기여 | 설명 | W15 연결 |
|---|---|---|
| XAI 개념 체계화 | explainability, interpretability, transparency, responsibility 개념을 정리 | W15 이론 기반 |
| XAI taxonomy 제시 | 모델 유형, 설명 범위, 설명 시점, 설명 방식에 따른 분류 제공 | 관련연구 표 설계 |
| Responsible AI 연결 | 설명가능성을 accountability, trust, fairness, privacy와 연결 | 보안적 함의 장 근거 |
| 기회와 한계 정리 | XAI가 신뢰를 높일 수 있지만 오용·과신·프라이버시 위험도 있음을 제시 | threat model 확장 |
| 평가와 governance 필요성 | human-centered evaluation, limitation statement, decision log 기록 필요성 제시 | W15 evidence chain |

---

## 4. 목차별 핵심 개괄

| 목차 | 핵심 내용 | 비전공자용 이해 |
|---|---|---|
| 1. Introduction | AI 모델이 복잡해질수록 설명가능성과 책임성의 필요성이 커진다. | AI가 답만 주는 것이 아니라 이유도 설명해야 한다. |
| 2. Concepts | transparency, interpretability, explainability, comprehensibility, trust, accountability 개념을 정리한다. | 설명 가능하다는 말도 여러 의미가 있으므로 구분해야 한다. |
| 3. XAI Taxonomies | model-agnostic/model-specific, global/local, post-hoc/intrinsic, visual/textual explanation을 분류한다. | 설명 방법은 모델 전체를 설명할 수도 있고, 특정 결과만 설명할 수도 있다. |
| 4. XAI Techniques | surrogate model, feature importance, rule extraction, saliency, example-based, counterfactual explanation을 다룬다. | 복잡한 모델을 쉬운 규칙, 중요한 변수, 반례, 사례로 설명한다. |
| 5. Responsible AI | XAI가 fairness, privacy, robustness, accountability, human oversight와 연결된다. | 설명은 공정하고 책임 있는 AI 운영의 일부다. |
| 6. Opportunities | 고위험 의사결정, 규제 대응, 오류 분석, 사용자 신뢰, 모델 개선에 XAI가 도움을 줄 수 있다. | 설명은 모델을 고치고 감시하는 데도 쓰인다. |
| 7. Challenges | 설명의 충실성, 안정성, 인간 이해, 과신, fairwashing, privacy leakage, evaluation standard 부족이 문제다. | 설명이 있다고 해서 무조건 믿을 수 있는 것은 아니다. |
| 8. Future Directions | robust, reproducible, human-centered, privacy-aware, regulation-aligned XAI가 필요하다. | 설명도 안전하고 재현 가능해야 한다. |
| 9. Conclusion | XAI는 responsible AI를 위한 핵심 도구지만, 설명의 품질과 한계를 함께 평가해야 한다. | 좋은 설명은 근거와 한계가 함께 있어야 한다. |

---

## 5. 핵심 이론 및 수식

> 아래 수식은 Responsible AI와 XAI 평가를 W15 최종 논문에 반영하기 위한 표준화된 표현이다. 실제 논문의 고유 정량식이라기보다 기말논문 평가표 설계를 위한 지표다.

### 5.1 Responsible AI Score

Responsible AI 수준은 투명성, 책임성, 강건성, 공정성, 프라이버시 위험을 함께 고려한다.

$$
ResponsibleAIScore=Transparency+Accountability+Robustness+Fairness-PrivacyRisk
$$

### 보안적 의미

설명가능성은 독립 지표가 아니라 responsible AI의 한 축이다. 설명이 좋아도 privacy risk가 크거나 accountability evidence가 없으면 책임 있는 AI라고 보기 어렵다.

---

### 5.2 Explanation Quality

설명 품질은 fidelity, stability, comprehensibility를 함께 평가한다.

$$
ExplanationQuality=w_1Fidelity+w_2Stability+w_3Comprehensibility
$$

| 기호 | 의미 |
|---|---|
| $Fidelity$ | 설명이 실제 모델 동작을 충실히 반영하는 정도 |
| $Stability$ | 작은 변화에도 설명이 안정적인 정도 |
| $Comprehensibility$ | 사람이 이해 가능한 정도 |

---

### 5.3 Transparency Coverage

모델 의사결정과 운영 과정 중 설명·문서화된 부분의 비율이다.

$$
TransparencyCoverage=\frac{|Elements_{documented}|}{|Elements_{required}|}
$$

### 보안적 의미

모델 구조, 데이터, 평가, 한계, decision log가 문서화되어야 감사 가능하다.

---

### 5.4 Accountability Coverage

책임소재와 승인·검토 증거가 있는 의사결정의 비율이다.

$$
AccountabilityCoverage=\frac{|Decisions_{with\ owner\ and\ evidence}|}{|Decisions_{total}|}
$$

### 보안적 의미

누가 어떤 근거로 모델을 승인했고, 어떤 한계를 알고 있었는지 기록되어야 한다.

---

### 5.5 Trust Calibration Gap

사용자의 신뢰 수준과 실제 설명 품질 사이의 차이다.

$$
TrustGap=|Trust_{user}-ExplanationQuality|
$$

### 보안적 의미

설명이 그럴듯해서 사용자가 과신하면 automation bias가 발생한다. 신뢰는 설명 품질과 맞게 보정되어야 한다.

---

### 5.6 Fairwashing Risk

공정하지 않은 모델을 그럴듯한 설명으로 포장할 위험을 측정한다.

$$
FairwashingRisk=ExplanationPersuasiveness-FairnessEvidence
$$

### 보안적 의미

설명이 설득력 있어도 실제 fairness evidence가 부족하면 설명은 책임성이 아니라 은폐 도구가 될 수 있다.

---

### 5.7 Responsible XAI Evidence Score

XAI evidence의 신뢰성을 종합한다.

$$
ResponsibleXAIEvidence=\alpha Fidelity+\beta Stability+\gamma AccountabilityCoverage+\delta TransparencyCoverage-\lambda PrivacyRisk-\mu TrustGap
$$

### 보안적 의미

책임 있는 XAI는 설명 품질, 투명성, 책임성, 프라이버시 보호, 신뢰 보정이 함께 충족되어야 한다.

---

## 6. AI 원리 70% 관점 분석

| 원리 항목 | 설명 | W15/P04에서의 의미 |
|---|---|---|
| Explainability | 모델 의사결정 이유를 설명 | 책임성 근거 |
| Interpretability | 사람이 이해 가능한 구조·결과 | 인간 검토 가능성 |
| Transparency | 모델·데이터·과정 공개·문서화 | 감사 가능성 |
| Post-hoc Explanation | 학습 후 explainer로 설명 | 실무 활용성 |
| Intrinsic Explanation | 해석 가능한 모델 구조 자체 | 고위험 분야 선호 |
| Human-centered XAI | 사용자 이해와 의사결정 지원 | human review |
| Responsible AI | 공정성·책임성·프라이버시·안전성 포함 | 보안적 함의 |
| Limitation Statement | 설명의 범위와 한계 고지 | 오해 방지 |

---

## 7. 보안 이슈 30% 관점 분석

| 보안 항목 | Responsible XAI 관점 해석 | 대표 평가 지표 |
|---|---|---|
| 기밀성 | 설명이 모델 내부 정보나 민감 데이터를 노출할 수 있음 | PrivacyRisk, sensitive exposure |
| 무결성 | 설명이 실제 모델 동작과 다르면 의사결정 근거가 왜곡됨 | Fidelity, fairwashing risk |
| 가용성 | 복잡한 XAI 계산과 human review가 운영 비용을 증가 | explanation latency, review cost |
| 프라이버시 | feature attribution과 example explanation이 개인정보를 드러낼 수 있음 | privacy-aware explanation check |
| 안전성 | 그럴듯한 설명은 automation bias와 과신을 유발 | TrustGap, human error rate |
| 책임성 | decision rationale, owner, limitation, review log가 필요 | AccountabilityCoverage |

---

## 8. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | user trust, explanation, decision rationale, accountability evidence, transparency document, limitation statement, human review log |
| 공격자/위험 목표 | misleading explanation, fairwashing, privacy leakage, automation bias, explanation overclaim, responsibility shifting |
| 공격자/위험 능력 | favorable explanation 선택, visualization cherry-picking, explainer parameter 조작, limitation omission, persuasive but low-fidelity narrative 생성 |
| 위험 경로 | 모델 판단 생성 → 선택적 explanation 제시 → 한계 고지 누락 → 사용자가 과신 → 잘못된 보안·정책·운영 결정 |
| 방어자 능력 | fidelity/stability 평가, multiple explainer 비교, limitation statement, human review, privacy-aware explanation, accountability log |
| 제외 범위 | 허위 설명 조작 방법, 개인정보 추출 절차, 모델 내부정보 탈취, 타인 기만용 설명 작성 지원 |

---

## 9. 평가방법 및 지표

| 평가축 | 지표 | 의미 | W15/P04 활용 |
|---|---|---|---|
| 설명 품질 | ExplanationQuality, fidelity, stability | 설명 신뢰성 | 핵심 XAI 평가 |
| 투명성 | TransparencyCoverage | 문서화·공개 범위 | 감사 가능성 |
| 책임성 | AccountabilityCoverage | owner·evidence 연결 | responsible AI |
| 신뢰 보정 | TrustGap | 과신·불신 위험 | human-centered 평가 |
| 공정성 위험 | FairwashingRisk | 설명으로 편향을 은폐하는 위험 | 보안적 함의 |
| 프라이버시 | PrivacyRisk, sensitive exposure | 설명의 정보 노출 위험 | privacy-aware XAI |
| 운영성 | review cost, explanation latency | 실무 적용성 | MLOps 연결 |
| 재현성 | explainer config, decision log, limitation statement | 설명 재현성 | W15 evidence chain |

---

## 10. 재현성 체크리스트

| 항목 | 기록해야 할 내용 |
|---|---|
| Bibliographic status | DOI 기준 서지, 로컬 PDF와 공식 DOI 일치 여부 |
| Model | model version, task, dataset, checkpoint/hash |
| Explainer | method, library version, baseline, parameters, random seed |
| Explanation target | sample ID, decision ID, input, output, confidence, selected class |
| Responsible AI evidence | fairness result, privacy check, robustness result, limitation statement |
| Human review | reviewer, rubric, trust rating, disagreement, action taken |
| Accountability | decision owner, approval, review date, exception reason |
| Transparency | model card, data card, evaluation card, XAI figure source |
| Logs | raw explanation artifact, visualization setting, script commit, report hash |
| 한계 | 설명을 모델의 완전한 진실로 과장하지 않고, 설명의 적용 범위와 불확실성을 명시 |

---

## 11. 논문의 고유 기여

1. XAI를 responsible AI의 핵심 구성요소로 정리한다.
2. XAI taxonomy를 통해 다양한 설명기법을 체계적으로 분류한다.
3. 설명가능성이 투명성, 책임성, 사용자 신뢰, 공정성, 프라이버시와 연결됨을 강조한다.
4. 설명이 오히려 오도·과신·fairwashing·privacy leakage를 만들 수 있음을 보안적 위험으로 해석할 수 있게 한다.
5. W15 최종논문에서 보안적 함의와 책임성 장을 작성할 때 XAI evidence와 limitation statement를 포함해야 함을 뒷받침한다.

---

## 12. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 설명의 과신 위험 | 그럴듯한 explanation이 실제 모델 동작을 충분히 반영하지 않을 수 있다. | fidelity와 limitation 병기 |
| Responsible AI 범위 넓음 | 투명성·공정성·프라이버시·책임성을 모두 정량화하기 어렵다. | 최소 통제 지표로 분리 보고 |
| Human evaluation 주관성 | 사용자 이해와 신뢰 평가는 개인·도메인에 따라 다르다. | rubric과 reviewer 기록 유지 |
| Fairwashing 가능성 | 설명이 편향이나 위험을 은폐하는 데 쓰일 수 있다. | fairness evidence와 함께 제시 |
| Privacy-aware XAI 부족 | 설명이 민감 feature나 훈련 사례를 노출할 수 있다. | privacy leakage check 추가 |
| 표준화 부족 | XAI 평가와 responsible AI 보고 양식이 완전히 표준화되어 있지 않다. | 자체 evidence table과 검증표 설계 |

---

## 13. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | XAI는 신뢰 가능한 AI 보안 프레임워크의 책임성 근거라는 문제의식 |
| 2장 관련연구 | P04를 Responsible XAI taxonomy 핵심 문헌으로 정리 |
| 3장 위협모형 | user trust, decision rationale, accountability evidence, limitation statement 보호 자산 정의 |
| 4장 연구방법 | ResponsibleAIScore, ExplanationQuality, TransparencyCoverage, AccountabilityCoverage, TrustGap, FairwashingRisk, ResponsibleXAIEvidence 지표 설계 |
| 5장 분석 | Responsible XAI control table과 explanation evidence/limitation matrix 제시 |
| 6장 보안적 함의 | fairwashing, automation bias, privacy leakage, accountability gap, responsible AI governance 해석 |
| 부록 | model card, data card, explainer config, human review rubric, limitation statement 수록 |

---

## 14. 기말논문 연결 3문장

1. W15에서 기말논문에 반영할 개념: XAI는 모델 설명 기법의 문제가 아니라 responsible AI를 위한 투명성, 책임성, 신뢰 보정, 한계 고지의 구조다.
2. W15에서 기말논문에 반영할 표·그림·실험: ResponsibleAIScore, ExplanationQuality, TransparencyCoverage, AccountabilityCoverage, TrustGap, FairwashingRisk, ResponsibleXAIEvidence 수식표와 Responsible XAI control table을 반영한다.
3. W15 최종 제출과 연결되는 지점: 보안적 함의 장에서는 XAI 결과와 함께 fairness evidence, privacy check, human review, limitation statement, decision owner를 연결해야 책임 있는 AI 보안 프레임워크가 된다.

---

## 15. 최종 판단

P04는 W15의 책임 있는 XAI와 보안적 함의 장을 뒷받침하는 핵심 문헌이다. 기말논문에서 XAI를 단순 시각화로 쓰면 부족하며, 투명성·책임성·신뢰 보정·공정성·프라이버시·한계 고지를 함께 포함해야 한다. 따라서 P04는 **Responsible XAI taxonomy, accountability evidence, fairwashing risk, automation bias, responsible AI governance의 중심 근거 문헌**으로 사용하는 것이 적절하다.

---

## 16. 변환 호환성 메모

```bash
pandoc P04_summary.md -o P04_summary.docx
pandoc P04_summary.md -o P04_summary.pdf --pdf-engine=xelatex
```
