# P02 Summary

## Recent Advances of Differential Privacy in Centralized Deep Learning: A Systematic Survey — Lea Demelius, Roman Kern, Andreas Trugler, ACM Computing Surveys, 2025

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W11 Differential Privacy & Membership Inference |
| 논문명 | Recent Advances of Differential Privacy in Centralized Deep Learning: A Systematic Survey |
| 저자 | Lea Demelius, Roman Kern, Andreas Trugler |
| 출판 정보 | ACM Computing Surveys, 57(6), pp. 1–28 |
| DOI | https://doi.org/10.1145/3712000 |
| 검증 상태 | W11 `paper_list.md` 기준 공식 DOI 확인. 기존 `Jonathan Demelius` 표기 불일치 메모 유지 |

---

## 1. 한 문장 요약

이 논문은 centralized deep learning에서 DP 적용을 **DP-SGD, gradient clipping, noise multiplier, privacy accountant, composition, utility degradation** 관점에서 체계적으로 정리하며, W11의 실험·보고서 지표 설계에 직접 연결된다.

---

## 2. 핵심 연구질문

| 번호 | 연구질문 |
|---|---|
| RQ1 | DP-SGD는 gradient clipping과 noise addition으로 어떻게 개인정보 노출을 줄이는가? |
| RQ2 | Privacy accountant와 composition은 반복 학습에서 privacy budget을 어떻게 누적 계산하는가? |
| RQ3 | DP 적용 후 accuracy, calibration, fairness, robustness는 어떻게 변하는가? |
| RQ4 | 중앙집중 학습에서 DP와 membership inference 평가를 어떻게 함께 보고할 수 있는가? |

---

## 3. 핵심 수식

### 3.1 Gradient Clipping

$$
\bar{g}_i=g_i\cdot \min\left(1,\frac{C}{\|g_i\|_2}\right)
$$

### 3.2 DP-SGD Noise Addition

$$
\tilde{g}=\frac{1}{B}\left(\sum_{i=1}^{B}\bar{g}_i+\mathcal{N}(0,\sigma^2C^2I)\right)
$$

**보안 해석:** DP-SGD는 개별 sample gradient의 영향을 제한하지만, clipping norm, noise multiplier, sampling rate, epoch 수를 기록하지 않으면 privacy claim을 검증할 수 없다.

---

## 4. 위협모형·평가지표

| 항목 | 내용 |
|---|---|
| 보호 자산 | 학습 샘플, gradient, model parameters, output confidence |
| 공격자 목표 | membership inference, reconstruction, attribute inference |
| 지표 | epsilon, delta, noise multiplier, clipping norm, utility drop, MI advantage |
| 재현성 | batch size, sampling rate, epoch, accountant, seed 기록 |

---

## 5. 기말논문 연결

P02는 DP 적용 실험을 쓸 때 필수 hyperparameter와 privacy accounting을 기록해야 한다는 기준을 제공한다. 기말논문에서는 DP 방어와 utility/MI risk 변화를 함께 제시한다.

---

## 6. 최종 판단

P02는 W11에서 DP-SGD와 centralized deep learning privacy accounting의 핵심 문헌이다.
