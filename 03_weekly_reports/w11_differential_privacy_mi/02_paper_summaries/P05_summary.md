# P05 Summary

## Defenses to Membership Inference Attacks: A Survey — Li Hu et al., ACM Computing Surveys, 2024

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W11 Differential Privacy & Membership Inference |
| 논문명 | Defenses to Membership Inference Attacks: A Survey |
| 저자 | Li Hu et al. |
| 출판 정보 | ACM Computing Surveys, 56(4), pp. 1–34, 2024 |
| DOI | https://doi.org/10.1145/3620667 |
| 검증 상태 | W11 `paper_list.md` 기준 공식 DOI 확인. 로컬 PDF는 관련 FL-MIA survey라 지정 논문처럼 인용하지 않는 메모 유지 |

---

## 1. 한 문장 요약

이 논문은 membership inference attack 방어를 **regularization, confidence masking, adversarial training, differential privacy, knowledge distillation, output perturbation, auditing** 관점에서 정리하며, W11에서 empirical MIA 방어 평가를 설계하는 핵심 문헌이다.

---

## 2. 핵심 연구질문

| 번호 | 연구질문 |
|---|---|
| RQ1 | MIA 방어는 학습 단계·출력 단계·후처리 단계에서 어떻게 적용되는가? |
| RQ2 | 방어가 MI risk를 낮추면서도 utility를 유지하는지 어떻게 평가하는가? |
| RQ3 | DP와 비-DP 방어의 장단점은 무엇인가? |
| RQ4 | 방어가 confidence만 숨기고 실제 leakage를 줄이지 못하는 경우를 어떻게 검증하는가? |

---

## 3. 핵심 수식

### 3.1 Defense Effectiveness

$$
DefenseGain=Adv_{MI}^{before}-Adv_{MI}^{after}
$$

### 3.2 Utility Loss

$$
UtilityLoss=Acc_{before}-Acc_{after}
$$

**보안 해석:** 좋은 방어는 membership inference advantage를 낮추면서 utility loss를 과도하게 만들지 않아야 한다.

---

## 4. 위협모형·평가지표

| 항목 | 내용 |
|---|---|
| 보호 자산 | 학습 데이터 membership, model output, confidence, loss signal |
| 공격자 목표 | membership 추론 |
| 방어 위치 | training, regularization, output perturbation, DP, auditing |
| 지표 | MI advantage, AUC, defense gain, utility loss, calibration, over-privacy cost |

---

## 5. 기말논문 연결

P05는 W11의 방어 문헌이다. 기말논문에서는 DP만이 아니라 regularization, output restriction, auditing을 포함해 privacy-utility trade-off 표를 구성한다.

---

## 6. 최종 판단

P05는 membership inference 방어체계의 핵심 문헌이다. 공식 DOI 문헌과 로컬 관련 PDF 차이를 유지하고, 최종 참고문헌은 공식 서지 기준으로 사용한다.
