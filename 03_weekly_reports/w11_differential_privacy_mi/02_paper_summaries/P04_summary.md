# P04 Summary

## Membership Inference Attacks on Machine Learning: A Survey — Hongsheng Hu et al., ACM Computing Surveys, 2022

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W11 Differential Privacy & Membership Inference |
| 논문명 | Membership Inference Attacks on Machine Learning: A Survey |
| 저자 | Hongsheng Hu et al. |
| 출판 정보 | ACM Computing Surveys, 54(11s), pp. 1–37, 2022 |
| DOI | https://doi.org/10.1145/3523273 |
| 검증 상태 | W11 `paper_list.md` 기준 공식 DOI 확인. 로컬 PDF는 arXiv/ACM preprint 메모 유지 |

---

## 1. 한 문장 요약

이 논문은 membership inference attack을 **black-box/white-box access, shadow model, confidence score, overfitting, attack advantage, defense, evaluation protocol** 관점에서 정리하며, W11의 핵심 프라이버시 공격 문헌이다.

---

## 2. 핵심 연구질문

| 번호 | 연구질문 |
|---|---|
| RQ1 | 공격자는 모델 출력만 보고 학습 데이터 포함 여부를 어떻게 추론하는가? |
| RQ2 | overfitting, confidence score, loss gap은 membership leakage와 어떻게 연결되는가? |
| RQ3 | black-box와 white-box MIA는 위협모형이 어떻게 다른가? |
| RQ4 | DP, regularization, output restriction은 MIA 방어에 어떤 효과와 한계를 갖는가? |

---

## 3. 핵심 수식

### 3.1 Membership Inference Advantage

$$
Adv_{MI}=\Pr[A(z)=1\mid z\in D_{train}]-\Pr[A(z)=1\mid z\notin D_{train}]
$$

### 3.2 Attack Accuracy

$$
Acc_{MI}=\frac{TP+TN}{TP+TN+FP+FN}
$$

**보안 해석:** 모델 정확도가 높아도 학습 데이터 포함 여부가 노출되면 프라이버시 실패다. 따라서 utility와 MI risk를 별도 지표로 보고해야 한다.

---

## 4. 위협모형·평가지표

| 항목 | 내용 |
|---|---|
| 보호 자산 | 학습 데이터 membership, confidence score, model output, gradient |
| 공격자 목표 | 특정 record가 학습에 포함됐는지 추론 |
| 공격자 능력 | black-box query, confidence 관찰, shadow data 보유, white-box 접근 |
| 지표 | MI accuracy, MI advantage, AUC, precision/recall, utility drop |
| 방어 | DP, regularization, confidence masking, output restriction, auditing |

---

## 5. 기말논문 연결

P04는 W11의 핵심 공격 문헌이다. 기말논문에서는 AI 시스템의 개인정보 위험을 단순 데이터 노출이 아니라 모델 출력 기반 추론 위험으로 정의하는 근거로 사용한다.

---

## 6. 최종 판단

P04는 membership inference 평가의 기준 문헌이다. W11에서 DP 방어 효과는 MI advantage 감소와 utility 변화로 함께 평가해야 한다.
