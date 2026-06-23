# P03 Summary

## Adversarial Attacks in Explainable Machine Learning: A Survey of Threats Against Models and Humans — Jon Vadillo et al., WIREs Data Mining and Knowledge Discovery, 2024

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W12 Neural Network Verification & XAI Robustness |
| 논문명 | Adversarial Attacks in Explainable Machine Learning: A Survey of Threats Against Models and Humans |
| 저자 | Jon Vadillo et al. |
| 출판 정보 | WIREs Data Mining and Knowledge Discovery, 2024 |
| DOI | https://doi.org/10.1002/widm.1567 |
| 검증 상태 | W12 `paper_list.md` 기준 관련 논문 공식 DOI 확인. 로컬 PDF는 Baniecki/Biecek 2023 관련 문헌 메모 유지 |

---

## 1. 한 문장 요약

이 논문은 XAI에 대한 adversarial attack을 **model explanation manipulation, explanation attack, human trust manipulation, adversarial examples against explanations** 관점에서 정리하며, W12에서 설명가능성이 공격면이 될 수 있음을 보여주는 핵심 관련 문헌이다.

---

## 2. 핵심 연구질문

| 번호 | 연구질문 |
|---|---|
| RQ1 | 공격자는 모델 예측뿐 아니라 설명 결과도 조작할 수 있는가? |
| RQ2 | XAI가 사용자의 과신을 유발하면 어떤 보안 위험이 발생하는가? |
| RQ3 | Explanation robustness는 prediction robustness와 어떻게 다른가? |
| RQ4 | AI 보안 보고서에서 설명가능성은 어떤 검증 지표와 함께 제시해야 하는가? |

---

## 3. 핵심 수식

### 3.1 Explanation Stability

$$
Stability=1-\frac{\|E(x)-E(x')\|}{\|x-x'\|+\epsilon}
$$

### 3.2 Explanation Attack Objective

$$
\max_{x'\in B_\epsilon(x)} Dist(E(x),E(x')) \quad \text{s.t.}\quad f(x')=f(x)
$$

**보안 해석:** 예측은 유지되지만 설명만 바뀌면 사용자는 잘못된 원인을 믿을 수 있다. XAI도 검증 대상이다.

---

## 4. 위협모형·평가지표

| 항목 | 내용 |
|---|---|
| 보호 자산 | model explanation, saliency map, feature attribution, human trust |
| 공격자 목표 | 설명 왜곡, 책임 회피, 위험 feature 은폐, 사용자 판단 오도 |
| 지표 | explanation stability, attribution similarity, prediction consistency, human trust error |
| 재현성 | explainer version, baseline, perturbation, seed, visualization setting 기록 |

---

## 5. 기말논문 연결

P03은 기말논문에서 XAI를 단순 시각화가 아니라 보안 평가 대상으로 다루는 근거다. RAG/LLM에서도 citation/explanation이 조작될 수 있으므로 evidence explanation audit로 확장한다.

---

## 6. 최종 판단

P03은 W12의 XAI robustness 핵심 관련 문헌이다. 로컬 PDF 차이 메모를 유지하고 공식 DOI 기준 관련 논문으로 사용한다.
