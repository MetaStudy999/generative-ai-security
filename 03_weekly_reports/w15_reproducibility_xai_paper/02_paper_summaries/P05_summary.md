# P05 Summary

## Concept-based Explainable Artificial Intelligence: A Survey — ACM Computing Surveys, 2025

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W15 Reproducibility, XAI & Final Paper Bridge |
| 논문명 | Concept-based Explainable Artificial Intelligence: A Survey |
| DOI | https://doi.org/10.1145/3774643 |
| 보조 URL | https://arxiv.org/abs/2312.12936 |
| 검증 상태 | W15 `doi_check.md` 기준 공식 DOI 확인. ACM 권호/issue는 최종 제출 전 재확인 필요 |

---

## 1. 한 문장 요약

이 논문은 concept-based XAI를 **human-understandable concept, TCAV, concept bottleneck, completeness, concept fidelity, annotation cost, concept leakage** 관점에서 정리하며, W15에서 feature-level 설명을 넘어 사람이 이해 가능한 설명 단위를 평가하는 근거를 제공한다.

---

## 2. 핵심 수식·지표

$$
ConceptScore=\frac{1}{N}\sum_{i=1}^{N}sim(c_i, h(x_i))
$$

$$
Completeness=\frac{Perf(f_{concept})}{Perf(f_{original})}
$$

---

## 3. 위협모형·평가지표

| 항목 | 내용 |
|---|---|
| 보호 자산 | concept label, human explanation, model rationale, sensitive concept |
| 위험 | spurious concept, concept leakage, concept manipulation, annotation bias |
| 지표 | concept fidelity, completeness, concept error, human agreement, privacy leakage |
| 재현성 | concept definition, annotator guideline, dataset split, explanation output 기록 |

---

## 4. 기말논문 연결

P05는 기말논문에서 설명가능성을 사람이 이해할 수 있는 개념 단위로 확장하는 근거다. 단, concept 공개가 민감한 업무 규칙이나 개인정보 단서를 노출할 수 있음을 한계로 명시해야 한다.
