# W12 100점형 통합 Summary

## Neural Network Verification & XAI Robustness

## 0. 문서 목적

이 문서는 W12 개별 논문 summary 5개를 기말논문 작성용 연구 노트로 통합한 100점형 요약본이다. Neural network verification, adversarial robustness, adversarial XAI, Lipschitz robustness, robustness-accuracy-fairness trade-off를 하나의 평가체계로 묶는다.

---

## 1. 한 문장 통합 요약

W12는 AI 보안 주장을 **empirical testing, formal verification, explanation robustness, Lipschitz certificate, accuracy-robustness-fairness trade-off**로 분리해 검토해야 하며, 높은 robust accuracy만으로 안전·공정·설명가능성을 보장할 수 없음을 정리하는 주차다.

---

## 2. 문헌 5편 통합 매트릭스

| ID | 논문 | 핵심 역할 | 주요 지표 |
|---|---|---|---|
| P01 | Abstraction for NN Verification | formal verification 배경 | verified radius, reachability |
| P02 | Adversarial Attacks/Defenses | empirical robustness taxonomy | robust accuracy, ASR |
| P03 | Adversarial XAI | explanation robustness | attribution stability |
| P04 | Lipschitz Robustness | 수학적 robust bound | Lipschitz constant, margin |
| P05 | Robustness-Accuracy-Fairness | 사회기술적 trade-off | fairness gap, subgroup risk |

---

## 3. 핵심 수식 묶음

$$
\forall x' \in B_\epsilon(x), \quad f(x')=f(x)
$$

$$
Reach(f, X) \subseteq \widehat{R}
$$

$$
\|f(x)-f(x')\|\leq L\|x-x'\|
$$

$$
Score=\alpha Acc+\beta RobustAcc-\gamma FairnessGap-\lambda Cost
$$

---

## 4. 통합 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | model decision, safety property, explanation, certificate, subgroup performance |
| 공격자 목표 | 오분류, defense bypass, explanation manipulation, 특정 집단 취약성 이용 |
| 방어자 능력 | formal verification, adversarial testing, XAI audit, Lipschitz regularization, fairness evaluation |
| 제외 범위 | 실제 서비스 공격, 고위험 자동 의사결정 무검증 적용 |

---

## 5. 통합 평가 지표

| 평가축 | 대표 지표 | 해석 |
|---|---|---|
| Empirical Robustness | robust accuracy, ASR | 공격 테스트 성능 |
| Formal Verification | verified rate, certified radius | 명세 기반 보장 |
| Explanation Robustness | attribution stability, explanation distance | 설명 조작 저항성 |
| Mathematical Bound | Lipschitz estimate, margin | 입력 민감도 상한 |
| Fairness | fairness gap, subgroup FNR/FPR | 집단별 위험 |
| Reproducibility | solver, timeout, attack setting, dataset split | 검증 가능성 |

---

## 6. 기말논문 연결 3문장

1. W12에서 기말논문에 반영할 개념: AI 보안 주장은 empirical robustness, formal certificate, explanation stability, fairness를 분리해 검증해야 한다.
2. 반영할 표·그림·실험: verification property, robust accuracy/ASR, Lipschitz bound, explanation stability, fairness gap 비교표를 반영한다.
3. W15 연결: 최종 종합평가에서는 성능·보안·프라이버시·공정성·설명가능성·재현성을 하나의 다중지표 체크리스트로 통합한다.

---

## 7. 최종 판단

W12는 AI 보안 평가를 수학적 검증과 사회기술적 책임성으로 확장하는 주차다. 로컬 PDF와 강의자료 표기 차이가 많은 주차이므로 paper_list의 공식 DOI 기준과 관련 문헌 메모를 반드시 유지해야 한다.
