# P04 Summary

## Adversarial Robustness of Neural Networks from the Perspective of Lipschitz Calculus: A Survey — Monty-Maximilian Zuhlke, Daniel Kudenko, ACM Computing Surveys, 2025

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W12 Neural Network Verification & XAI Robustness |
| 논문명 | Adversarial Robustness of Neural Networks from the Perspective of Lipschitz Calculus: A Survey |
| 저자 | Monty-Maximilian Zuhlke, Daniel Kudenko |
| 출판 정보 | ACM Computing Surveys, 2025 |
| DOI | https://doi.org/10.1145/3648351 |
| 검증 상태 | W12 `paper_list.md` 기준 관련 논문 공식 DOI 확인. 로컬 PDF는 Finlay et al. 2018 관련 문헌 메모 유지 |

---

## 1. 한 문장 요약

이 논문은 Lipschitz calculus 관점에서 신경망 adversarial robustness를 **Lipschitz constant, certified bound, regularization, robustness-accuracy trade-off**로 정리하며, W12의 수학적 강건성 평가축을 제공한다.

---

## 2. 핵심 연구질문

| 번호 | 연구질문 |
|---|---|
| RQ1 | Lipschitz constant는 입력 변화에 대한 출력 민감도를 어떻게 제한하는가? |
| RQ2 | Lipschitz regularization은 adversarial robustness와 어떤 관계가 있는가? |
| RQ3 | Robustness certificate와 empirical attack test는 어떻게 구분해야 하는가? |
| RQ4 | Robustness 향상이 accuracy·fairness·cost와 어떤 trade-off를 만드는가? |

---

## 3. 핵심 수식

### 3.1 Lipschitz Bound

$$
\|f(x)-f(x')\|\leq L\|x-x'\|
$$

### 3.2 Robust Margin 조건

$$
margin(x)>L\epsilon \Rightarrow f(x')=f(x), \quad \forall x'\in B_\epsilon(x)
$$

**보안 해석:** Lipschitz bound는 입력 교란에 대한 출력 변화의 상한을 제공하지만, 실제 모델 전체 안전성을 보장하려면 적용 범위와 가정을 명시해야 한다.

---

## 4. 위협모형·평가지표

| 항목 | 내용 |
|---|---|
| 보호 자산 | decision boundary, margin, robustness certificate |
| 공격자 목표 | small perturbation으로 decision boundary crossing |
| 지표 | Lipschitz estimate, certified radius, robust accuracy, clean accuracy |
| 재현성 | norm, epsilon, bound method, model architecture, solver 기록 |

---

## 5. 기말논문 연결

P04는 W12에서 수학적 강건성을 설명하는 핵심 관련 문헌이다. 기말논문에서는 empirical robust accuracy와 certified bound를 분리하는 근거로 사용한다.

---

## 6. 최종 판단

P04는 관련 문헌으로 사용하되, 로컬 PDF 차이와 강의자료 지정 차이 메모를 유지한다.
