# W11 100점형 통합 Summary

## Differential Privacy & Membership Inference

## 0. 문서 목적

이 문서는 W11 개별 논문 summary 5개를 기말논문 작성용 연구 노트로 통합한 100점형 요약본이다. Differential Privacy와 Membership Inference Attack/Defense를 하나의 privacy evaluation framework로 묶는다.

---

## 1. 한 문장 통합 요약

W11은 AI 프라이버시를 **DP 보장, DP-SGD, privacy accounting, membership inference, defense gain, utility loss**로 분리해 평가해야 하며, privacy claim은 epsilon·delta·threat model·empirical leakage 지표 없이 주장해서는 안 된다는 기준을 제공한다.

---

## 2. 문헌 5편 통합 매트릭스

| ID | 논문 | 핵심 역할 | 주요 지표 |
|---|---|---|---|
| P01 | DP Critical Review | DP 오용 방지와 보장 해석 | epsilon, delta, utility trade-off |
| P02 | DP in Centralized DL | DP-SGD와 privacy accounting | clipping, noise multiplier |
| P03 | DP in Deep Learning | DP deep learning 종합 | utility drop, privacy budget |
| P04 | MIA Survey | membership inference 공격 | MI advantage, attack AUC |
| P05 | MIA Defense Survey | MIA 방어체계 | defense gain, utility loss |

---

## 3. 핵심 수식 묶음

$$
\Pr[M(D)\in S]\leq e^{\epsilon}\Pr[M(D')\in S]+\delta
$$

$$
\tilde{g}=\frac{1}{B}\left(\sum_{i=1}^{B}\bar{g}_i+\mathcal{N}(0,\sigma^2C^2I)\right)
$$

$$
Adv_{MI}=\Pr[A(z)=1\mid z\in D_{train}]-\Pr[A(z)=1\mid z\notin D_{train}]
$$

$$
DefenseGain=Adv_{MI}^{before}-Adv_{MI}^{after}
$$

---

## 4. 통합 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | 학습 데이터, 개별 record membership, gradient, model output, confidence score |
| 공격자 목표 | membership inference, attribute inference, reconstruction, model inversion |
| 공격자 능력 | black-box query, confidence 관찰, shadow model, white-box 접근 |
| 방어자 능력 | DP-SGD, clipping/noise, output restriction, regularization, auditing |
| 제외 범위 | 실제 개인정보 데이터 사용, 실서비스 대상 privacy attack |

---

## 5. 통합 평가 지표

| 평가축 | 대표 지표 | 해석 |
|---|---|---|
| Formal Privacy | epsilon, delta, privacy accountant | 이론적 보호 수준 |
| Empirical Leakage | MI advantage, AUC, attack accuracy | 실제 공격 저항성 |
| Utility | accuracy, F1, calibration | 정상 성능 |
| Defense Quality | defense gain, utility loss | 방어 효과와 부작용 |
| Reproducibility | clipping norm, noise multiplier, sampling rate, epoch | 검증 가능성 |

---

## 6. 기말논문 연결 3문장

1. W11에서 기말논문에 반영할 개념: AI 프라이버시는 DP 보장과 empirical membership leakage를 분리해 평가해야 한다.
2. 반영할 표·그림·실험: DP 정의식, DP-SGD 구조, MI advantage, defense gain/utility loss 비교표를 반영한다.
3. W08/W14 연결: RAG/LLM 로그와 학습 데이터도 membership/privacy risk를 가지므로 privacy accounting과 audit log가 필요하다.

---

## 7. 최종 판단

W11은 기말논문의 privacy 평가축을 책임 있게 만드는 핵심 주차다. DP를 적용했다는 주장만으로는 부족하며, epsilon/delta, accountant, utility loss, MI advantage를 모두 보고해야 한다.
