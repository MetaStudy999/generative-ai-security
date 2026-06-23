# P03 Summary

## Explainable AI: Core Ideas, Techniques, and Solutions — Rudresh Dwivedi et al., ACM Computing Surveys, 2023

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W15 Reproducibility, XAI & Final Paper Bridge |
| 논문명 | Explainable AI: Core Ideas, Techniques, and Solutions |
| DOI | https://doi.org/10.1145/3561048 |
| 검증 상태 | W15 `doi_check.md` 기준 공식 DOI 확인. 로컬 PDF는 Mersha et al. 관련 보조 문헌으로 차이 기록 |

---

## 1. 한 문장 요약

이 논문은 XAI의 핵심 개념과 기술을 **interpretability, explainability, fidelity, transparency, post-hoc explanation, human understanding** 관점에서 정리하며, W15의 설명가능성 평가축을 제공한다.

---

## 2. 핵심 수식·지표

$$
Fidelity=1-\frac{1}{N}\sum_{i=1}^{N}\mathbf{1}[g(x_i)\neq f(x_i)]
$$

$$
Stability=1-\frac{\|E(x)-E(x')\|}{\|x-x'\|+\epsilon}
$$

---

## 3. 위협모형·평가지표

| 항목 | 내용 |
|---|---|
| 보호 자산 | explanation, feature attribution, user trust, model decision rationale |
| 위험 | misleading explanation, explanation gaming, privacy leakage, explanation overclaim |
| 지표 | fidelity, stability, comprehensibility, human agreement, explanation robustness |
| 재현성 | explainer, baseline, parameters, visualization setting, human review 기록 |

---

## 4. 기말논문 연결

P03은 기말논문에서 XAI를 단순 그림이 아니라 검증 가능한 평가 대상으로 다루게 해준다. 설명은 충실성·안정성·사용자 이해도를 함께 보고해야 한다.
