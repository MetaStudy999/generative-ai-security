# P05 Summary

## Triangular Trade-off between Robustness, Accuracy, and Fairness in Deep Neural Networks: A Survey — Jingyang Li, Guoqiang Li, ACM Computing Surveys, 2025

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W12 Neural Network Verification & XAI Robustness |
| 논문명 | Triangular Trade-off between Robustness, Accuracy, and Fairness in Deep Neural Networks: A Survey |
| 저자 | Jingyang Li, Guoqiang Li |
| 출판 정보 | ACM Computing Surveys, 2025 |
| DOI | https://doi.org/10.1145/3645088 |
| 검증 상태 | W12 `paper_list.md` 기준 관련 논문 공식 DOI 확인. 로컬 PDF는 Singh et al. 2021 관련 문헌 메모 유지 |

---

## 1. 한 문장 요약

이 논문은 DNN에서 robustness, accuracy, fairness 사이의 삼각 trade-off를 정리하며, W12에서 보안 방어가 성능·공정성·설명가능성에 미치는 부작용까지 함께 평가해야 함을 보여주는 핵심 관련 문헌이다.

---

## 2. 핵심 연구질문

| 번호 | 연구질문 |
|---|---|
| RQ1 | Robustness를 높이면 accuracy나 fairness가 왜 손상될 수 있는가? |
| RQ2 | Fairness 지표는 adversarial robustness 평가와 어떻게 충돌하거나 보완되는가? |
| RQ3 | 안전한 AI 보안 보고서는 robust accuracy 외에 어떤 사회기술적 지표를 포함해야 하는가? |
| RQ4 | 방어 효과를 하나의 성능 점수로 요약하면 어떤 위험이 있는가? |

---

## 3. 핵심 수식

### 3.1 Trade-off Score

$$
Score=\alpha Acc+\beta RobustAcc-\gamma FairnessGap-\lambda Cost
$$

### 3.2 Fairness Gap

$$
FairnessGap=|Metric_{groupA}-Metric_{groupB}|
$$

**보안 해석:** 방어가 전체 robust accuracy를 높여도 특정 집단의 오류율을 높이면 안전하고 공정한 시스템이라고 보기 어렵다.

---

## 4. 위협모형·평가지표

| 항목 | 내용 |
|---|---|
| 보호 자산 | model decision, group-level performance, fairness, robustness claim |
| 공격자/위험 | 특정 집단 취약성, 편향된 방어, robustness overclaim |
| 지표 | clean accuracy, robust accuracy, fairness gap, subgroup FNR/FPR, calibration |
| 재현성 | group definition, dataset split, attack setting, fairness metric 기록 |

---

## 5. 기말논문 연결

P05는 기말논문에서 보안 성능을 accuracy/robustness만으로 판단하지 않고 fairness·subgroup risk·calibration을 함께 보는 근거로 사용한다.

---

## 6. 최종 판단

P05는 W12의 사회기술적 평가축을 담당한다. 공식 DOI 기준 관련 논문으로 사용하고 로컬 PDF 차이 메모는 유지한다.
