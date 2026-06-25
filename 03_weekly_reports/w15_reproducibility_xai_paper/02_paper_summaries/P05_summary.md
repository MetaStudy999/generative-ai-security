# P05 Summary

## Concept-based Explainable Artificial Intelligence: A Survey — Eleonora Poeta et al., ACM Computing Surveys, 2025

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W15 Reproducibility, XAI & Final Paper Bridge |
| 논문명 | Concept-based Explainable Artificial Intelligence: A Survey |
| 저자 | Eleonora Poeta et al. |
| 공식 출판 정보 | ACM Computing Surveys, online publication 2025-11-08, Article 3774643. 권호/issue는 최종 제출 전 ACM 페이지에서 재확인 필요 |
| DOI | https://doi.org/10.1145/3774643 |
| 보조 URL | https://arxiv.org/abs/2312.12936 |
| 로컬 PDF | `01_papers/pdf/05_Poeta_et_al_2025_Concept_Based_XAI_Survey.pdf` |
| 검증 상태 | W15 `doi_check.md`와 `paper_list.md` 기준 arXiv `2312.12936`와 Crossref/DOI metadata가 동일 제목·저자 및 최종 ACM DOI `10.1145/3774643`으로 연결됨. ACM 권호/issue는 최종 제출 전 재확인 필요 |
| PDF 확인 메모 | repo의 PDF 폴더에 P05 관련 PDF blob이 존재함을 확인했다. 요약은 로컬 PDF 경로와 W15 `doi_check.md` 및 `paper_list.md`의 공식 DOI/arXiv 메타데이터 기준으로 보완했다. |
| 핵심 근거 사용 가능 여부 | 가능. W15에서 concept-based XAI, human-understandable concept, TCAV, concept bottleneck, concept completeness, concept fidelity, annotation bias, privacy leakage, final paper explanation evidence의 핵심 문헌으로 사용 |

---

## 1. 한 문장 요약

이 논문은 concept-based explainable AI를 **human-understandable concept, concept activation vector, TCAV, concept bottleneck model, prototype/concept representation, concept discovery, concept annotation, concept completeness, concept fidelity, intervention, causal concept explanation, spurious concept, concept leakage, sensitive concept, annotation bias, human agreement, reproducibility** 관점에서 정리하며, W15에서 XAI 설명을 feature나 saliency 수준을 넘어 **사람이 이해 가능한 의미 단위와 검증 가능한 concept evidence**로 확장하는 핵심 문헌이다.

---

## 2. 핵심 연구문제

> 기존 XAI는 feature attribution이나 saliency map처럼 모델 내부 신호를 시각화하는 데 집중하는 경우가 많다. 그러나 인간 사용자는 픽셀·토큰·임베딩보다 “모양”, “증상”, “행동 패턴”, “보안 이벤트 유형” 같은 개념 단위의 설명을 더 쉽게 이해한다. Concept-based XAI의 핵심은 모델 판단을 사람이 이해 가능한 concept으로 연결하되, concept 정의·주석·완전성·충실성·프라이버시 위험을 함께 평가하는 것이다.

| 번호 | 연구질문 |
|---|---|
| RQ1 | Concept-based XAI에서 concept은 어떻게 정의되며, feature-level explanation과 어떤 차이를 갖는가? |
| RQ2 | TCAV, concept activation vector, concept bottleneck model, concept discovery는 모델 판단을 어떻게 concept 단위로 설명하는가? |
| RQ3 | Concept explanation의 품질은 concept fidelity, completeness, separability, human agreement, intervention consistency로 어떻게 평가해야 하는가? |
| RQ4 | Concept annotation cost, annotation bias, spurious concept, sensitive concept leakage는 어떤 보안·책임성 위험을 만드는가? |
| RQ5 | LLM/RAG 보안 프레임워크에서 concept-based XAI를 활용하면 보안 이벤트, 근거 문서, 답변 판단 이유를 어떻게 사람이 이해 가능한 단위로 설명할 수 있는가? |

---

## 3. 논문의 핵심 기여

| 기여 | 설명 | W15 연결 |
|---|---|---|
| Concept-based XAI taxonomy | 사람이 이해 가능한 concept을 중심으로 XAI 방법을 분류 | W15 P05 핵심 |
| TCAV/CBM 등 방법 정리 | concept activation, concept bottleneck, concept discovery, prototype-based concept 설명 정리 | XAI 방법론 확장 |
| Concept quality 평가 | completeness, fidelity, separability, human agreement, concept error 등 지표 제시 | 기말논문 평가표 설계 |
| Human-centered explanation | 설명 단위를 사람이 이해 가능한 concept으로 변환 | 책임성·사용자 이해 연결 |
| 위험과 한계 제시 | spurious concept, annotation bias, sensitive concept leakage, concept manipulation 위험 강조 | 보안적 함의 및 limitation 작성 근거 |

---

## 4. 목차별 핵심 개괄

| 목차 | 핵심 내용 | 비전공자용 이해 |
|---|---|---|
| 1. Introduction | XAI는 사람이 이해 가능한 설명을 제공해야 하며, concept-based XAI는 이를 concept 단위로 접근한다. | AI 설명을 픽셀·숫자가 아니라 사람이 아는 개념으로 바꾸는 연구다. |
| 2. Background | Concept, representation, attribution, interpretability, human-understandable explanation의 기본 개념을 설명한다. | 모델이 내부적으로 본 특징을 사람이 아는 의미 단위와 연결한다. |
| 3. Concept-based Taxonomy | concept definition, concept discovery, concept bottleneck, concept attribution, concept intervention을 분류한다. | 개념을 사람이 직접 정할 수도 있고, 모델이 발견하게 할 수도 있다. |
| 4. TCAV and CAV Methods | Concept Activation Vector와 TCAV를 통해 특정 concept이 예측에 미치는 영향을 측정한다. | “줄무늬” 같은 개념이 모델 판단에 얼마나 영향을 줬는지 측정한다. |
| 5. Concept Bottleneck Models | 모델이 먼저 concept을 예측하고, 그 concept을 바탕으로 최종 결정을 내리게 한다. | AI가 중간에 사람이 이해 가능한 이유 목록을 만들고 결론을 낸다. |
| 6. Concept Discovery | 사전 정의된 concept이 없을 때 모델 representation에서 의미 있는 concept 후보를 찾는다. | 사람이 미리 알려주지 않아도 모델 내부에서 반복되는 의미 패턴을 찾는다. |
| 7. Evaluation of Concepts | concept fidelity, completeness, purity, separability, stability, human agreement를 평가한다. | 설명 개념도 정확하고 안정적인지 평가해야 한다. |
| 8. Applications | 의료, 비전, 자연어, 보안, 과학, 의사결정 지원에서 concept explanation이 활용된다. | 의사가 이해하는 증상, 보안 분석가가 이해하는 이벤트 유형처럼 설명한다. |
| 9. Challenges | annotation cost, concept ambiguity, spurious concept, privacy leakage, causal validity, benchmark 부족이 과제로 남는다. | 사람이 붙인 개념도 편향되거나 민감정보를 드러낼 수 있다. |
| 10. Future Directions | causal concept learning, interactive concept editing, robust concept explanation, privacy-aware concept XAI가 필요하다. | 앞으로는 개념 설명도 조작에 강하고 개인정보를 보호해야 한다. |

---

## 5. 핵심 이론 및 수식

> 아래 수식은 concept-based XAI 평가와 W15 최종 논문 설명 evidence를 설계하기 위한 표준화된 표현이다. 수식은 GitHub, MS Word, PDF 변환 호환성을 위해 Markdown 표 밖의 LaTeX block math로 작성한다.

### 5.1 Concept Score

모델 내부 표현 $h(x_i)$가 인간 concept $c_i$와 얼마나 일치하는지 측정한다.

$$
ConceptScore=\frac{1}{N}\sum_{i=1}^{N}sim(c_i,h(x_i))
$$

| 기호 | 의미 |
|---|---|
| $c_i$ | 사람이 정의하거나 주석한 concept |
| $h(x_i)$ | 모델의 중간 representation |
| $sim$ | similarity 함수 |

### 보안적 의미

ConceptScore가 높아도 concept 자체가 잘못 정의되었거나 민감정보를 포함하면 위험하다. concept 정의와 주석 지침을 함께 기록해야 한다.

---

### 5.2 Completeness

Concept 기반 모델이 원 모델의 성능을 얼마나 설명·보존하는지 측정한다.

$$
Completeness=\frac{Perf(f_{concept})}{Perf(f_{original})}
$$

### 보안적 의미

Completeness가 낮으면 선택한 concept 집합이 모델 판단을 충분히 설명하지 못한다. 설명에서 빠진 hidden factor가 있을 수 있다.

---

### 5.3 Concept Fidelity

Concept explanation이 원 모델의 decision behavior를 얼마나 충실히 반영하는지 평가한다.

$$
ConceptFidelity=1-\frac{1}{N}\sum_{i=1}^{N}\mathbf{1}[f_{concept}(x_i)\neq f_{original}(x_i)]
$$

### 보안적 의미

Concept-based explanation도 실제 모델을 충실히 반영해야 한다. 사람이 이해하기 쉽다는 이유만으로 정확한 설명이라고 볼 수 없다.

---

### 5.4 TCAV Score

특정 concept 방향이 class 예측에 미치는 민감도를 측정한다.

$$
TCAV_{k,c}=\frac{1}{N}\sum_{i=1}^{N}\mathbf{1}\left[\nabla h_{k}(x_i)\cdot v_c>0\right]
$$

| 기호 | 의미 |
|---|---|
| $h_k$ | class $k$에 대한 model activation 또는 logit |
| $v_c$ | concept $c$의 activation vector |

### 보안적 의미

TCAV는 특정 concept이 예측에 영향을 주는 방향성을 보여줄 수 있지만, concept set 구성과 baseline에 민감하다.

---

### 5.5 Concept Bottleneck Error

Concept 예측 단계에서 발생한 오류가 최종 판단에 미치는 위험을 측정한다.

$$
CBMError=Error(c_{pred},c_{true})+Error(y_{pred},y_{true})
$$

### 보안적 의미

Concept bottleneck model은 설명 가능하지만, concept label이 틀리면 최종 판단도 틀릴 수 있다. concept annotation quality가 중요하다.

---

### 5.6 Human Concept Agreement

여러 주석자나 전문가가 concept 정의에 얼마나 동의하는지 측정한다.

$$
Agreement_C=\frac{N_{agreed\ concepts}}{N_{total\ concepts}}
$$

### 보안적 의미

사람이 이해 가능한 concept이라도 전문가 간 합의가 낮으면 책임 있는 설명으로 쓰기 어렵다.

---

### 5.7 Concept Leakage Risk

Concept 공개가 민감정보나 내부 업무 규칙을 노출할 위험을 요약한다.

$$
ConceptLeakageRisk=\alpha SensitiveConcept+\beta RuleExposure+\gamma MembershipSignal
$$

### 보안적 의미

보안/RAG 시스템에서 concept을 공개하면 민감한 탐지 규칙, 내부 정책, 취약한 패턴이 노출될 수 있다.

---

### 5.8 Concept XAI Evidence Score

Concept-based explanation의 품질과 위험을 종합한다.

$$
ConceptXAIEvidence=\alpha Completeness+\beta ConceptFidelity+\gamma Agreement_C-\lambda ConceptLeakageRisk-\mu AnnotationBias
$$

### 보안적 의미

좋은 concept explanation은 완전하고 충실하며 사람 간 합의가 높고, 민감 concept 노출과 주석 편향이 낮아야 한다.

---

## 6. AI 원리 70% 관점 분석

| 원리 항목 | 설명 | W15/P05에서의 의미 |
|---|---|---|
| Concept-based XAI | 사람이 이해 가능한 concept으로 모델 판단 설명 | P05 핵심 |
| Concept Activation Vector | concept 방향을 activation space에서 표현 | TCAV 기반 |
| TCAV | concept이 class 예측에 미치는 영향 측정 | concept sensitivity |
| Concept Bottleneck Model | concept 예측을 중간 단계로 두는 모델 | 투명한 decision pipeline |
| Concept Discovery | 모델 representation에서 concept 후보를 찾음 | 자동 concept 탐색 |
| Completeness | concept 집합이 모델 성능을 얼마나 설명하는지 | 설명 충분성 |
| Concept Fidelity | concept explanation과 원 모델 동작의 일치 | 설명 충실성 |
| Human Agreement | concept 정의에 대한 사람 간 합의 | 책임성·사용자 이해 |

---

## 7. 보안 이슈 30% 관점 분석

| 보안 항목 | Concept-based XAI 관점 해석 | 대표 평가 지표 |
|---|---|---|
| 기밀성 | concept이 내부 업무 규칙, 민감 속성, 보안 탐지 논리를 노출할 수 있음 | ConceptLeakageRisk |
| 무결성 | spurious concept이나 조작된 concept이 잘못된 설명을 만들 수 있음 | ConceptFidelity, completeness |
| 가용성 | concept annotation과 expert review 비용이 높음 | annotation cost, review latency |
| 프라이버시 | concept label이 민감정보나 membership signal을 포함할 수 있음 | SensitiveConcept, MembershipSignal |
| 안전성 | 잘못된 concept 설명은 human decision을 오도할 수 있음 | human error, Agreement_C |
| 책임성 | concept definition, annotator guideline, dataset split, explanation output 기록 필요 | concept evidence completeness |

---

## 8. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | concept label, concept definition, annotator guideline, human explanation, model rationale, sensitive concept, concept dataset, explanation output |
| 공격자/위험 목표 | spurious concept 삽입, concept manipulation, sensitive concept leakage, concept-based fairwashing, explanation overclaim |
| 공격자/위험 능력 | concept annotation bias 유발, concept set cherry-picking, favorable concept 선택, concept intervention 조작, explanation output 과장 |
| 위험 경로 | concept 정의/주석 → 모델 또는 explainer 학습 → 낮은 fidelity/biased concept → 사용자가 설명을 과신 → 잘못된 보안·정책 판단 |
| 방어자 능력 | concept definition review, annotation guideline, concept fidelity/completeness 평가, human agreement, privacy-aware concept filtering, limitation note |
| 제외 범위 | 민감 concept 추출 절차, 내부 규칙 노출, 허위 concept 조작, 실제 시스템 공격 지원 |

---

## 9. 평가방법 및 지표

| 평가축 | 지표 | 의미 | W15/P05 활용 |
|---|---|---|---|
| Concept 품질 | ConceptScore, purity, separability | concept 표현 품질 | 핵심 평가 |
| 설명 충분성 | Completeness | concept 집합의 설명 범위 | 설명 충분성 |
| 설명 충실성 | ConceptFidelity | 원 모델 동작 반영 | XAI 신뢰성 |
| concept 민감도 | TCAV score | 특정 concept의 class 영향 | concept attribution |
| 주석 품질 | Agreement_C, annotation error | human concept 신뢰도 | 책임성 |
| bottleneck 위험 | CBMError | concept 예측 오류와 최종 오류 | CBM 평가 |
| 보안 위험 | ConceptLeakageRisk, AnnotationBias | 민감 concept·편향 위험 | 보안적 함의 |
| 재현성 | concept definition, annotator guideline, split, output log | 설명 재현성 | W15 evidence chain |

---

## 10. 재현성 체크리스트

| 항목 | 기록해야 할 내용 |
|---|---|
| Bibliographic status | DOI/arXiv 기준 서지, 권호/issue 추가 확인 필요 메모 |
| Concept definition | concept 이름, 정의, 포함/제외 기준, 예시 |
| Annotation | annotator guideline, annotator 수, agreement, conflict resolution |
| Dataset | concept dataset, train/test split, preprocessing, sensitive concept flag |
| Model | original model, concept model, concept bottleneck architecture, checkpoint/hash |
| Explainer | TCAV/CBM/concept discovery method, parameters, baseline, random seed |
| Metrics | ConceptScore, Completeness, ConceptFidelity, TCAV score, Agreement_C, leakage risk |
| Human review | expert reviewer, rubric, disagreement, concept validity note |
| Evidence | concept list, raw explanation, code commit, visualization source, limitation statement |
| 한계 | concept explanation을 모델의 완전한 진실로 과장하지 않고, concept 정의와 주석 편향을 명시 |

---

## 11. 논문의 고유 기여

1. XAI를 feature-level attribution에서 사람이 이해 가능한 concept-level explanation으로 확장한다.
2. TCAV, concept bottleneck, concept discovery 등 concept-based XAI의 주요 방법을 체계화한다.
3. Completeness, concept fidelity, human agreement, annotation bias 등 concept explanation의 평가 기준을 제시한다.
4. Concept 공개가 민감 concept leakage, 내부 규칙 노출, spurious explanation을 만들 수 있음을 보안적 한계로 해석할 수 있게 한다.
5. W15 최종논문에서 설명가능성을 사람에게 의미 있는 단위로 제시하고, 그 설명을 evidence chain으로 검증하는 근거가 된다.

---

## 12. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 권호/issue 추가 확인 | DOI는 확인되었으나 ACM 권호/issue 표기는 최종 제출 전 재확인 필요 | reference verification table 유지 |
| concept 정의 주관성 | 같은 concept도 도메인·전문가에 따라 다르게 정의될 수 있다. | annotator guideline과 agreement 기록 |
| annotation 비용 | concept label 작성에는 전문가 시간과 비용이 필요하다. | 핵심 concept만 선정 |
| spurious concept | 모델이 의미 없는 shortcut concept을 사용할 수 있다. | intervention과 fidelity 평가 병행 |
| 민감 concept leakage | concept 공개가 개인정보·업무규칙·보안탐지 로직을 노출할 수 있다. | sensitive concept redaction 정책 |
| completeness 한계 | 선택한 concept이 모델 판단 전체를 설명하지 못할 수 있다. | Completeness와 limitation 병기 |

---

## 13. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | 설명가능성은 feature-level 시각화를 넘어 사람이 이해 가능한 concept 단위 설명으로 확장되어야 한다는 문제의식 |
| 2장 관련연구 | P05를 concept-based XAI survey 핵심 문헌으로 정리 |
| 3장 위협모형 | concept label, sensitive concept, model rationale, annotator guideline, explanation output 보호 자산 정의 |
| 4장 연구방법 | ConceptScore, Completeness, ConceptFidelity, TCAV, CBMError, Agreement_C, ConceptLeakageRisk, ConceptXAIEvidence 지표 설계 |
| 5장 분석 | Concept-based XAI taxonomy table과 concept evidence matrix 제시 |
| 6장 보안적 함의 | sensitive concept leakage, annotation bias, spurious concept, concept manipulation, concept overclaim 위험 해석 |
| 부록 | concept dictionary, annotator guideline, concept evaluation table, limitation statement 수록 |

---

## 14. 기말논문 연결 3문장

1. W15에서 기말논문에 반영할 개념: Concept-based XAI는 모델 판단을 사람이 이해 가능한 concept으로 설명하지만, concept 자체의 정의·주석·충실성·완전성을 검증해야 한다.
2. W15에서 기말논문에 반영할 표·그림·실험: ConceptScore, Completeness, ConceptFidelity, TCAV, CBMError, Agreement_C, ConceptLeakageRisk, ConceptXAIEvidence 수식표와 concept evidence matrix를 반영한다.
3. W15 최종 제출과 연결되는 지점: RAG/LLM 보안 프레임워크에서는 “민감정보 탐지”, “근거 충분성”, “프롬프트 주입 위험”, “출처 신뢰성” 같은 concept을 정의하고, 각 concept의 주석 기준·평가 결과·한계를 evidence chain에 포함해야 한다.

---

## 15. 최종 판단

P05는 W15의 concept-based XAI 핵심 문헌이다. 기말논문에서 설명가능성을 단순 feature attribution이나 saliency map으로 끝내지 않고, 사람이 이해 가능한 개념 단위로 설명하려면 P05의 taxonomy와 평가 기준이 필요하다. 따라서 P05는 **concept-based XAI, TCAV, concept bottleneck, concept completeness/fidelity, sensitive concept leakage, concept evidence chain의 중심 근거 문헌**으로 사용하는 것이 적절하다.

---

## 16. 변환 호환성 메모

```bash
pandoc P05_summary.md -o P05_summary.docx
pandoc P05_summary.md -o P05_summary.pdf --pdf-engine=xelatex
```
