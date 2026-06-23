# P01 Summary

## A Critical Review on the Use (and Misuse) of Differential Privacy in Machine Learning — Alberto Blanco-Justicia et al., ACM Computing Surveys, 2023

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W11 Differential Privacy & Membership Inference |
| 논문명 | A Critical Review on the Use (and Misuse) of Differential Privacy in Machine Learning |
| 저자 | Alberto Blanco-Justicia et al. |
| 출판 정보 | ACM Computing Surveys, 55(8), pp. 1–16 |
| DOI | https://doi.org/10.1145/3547139 |
| 검증 상태 | W11 `paper_list.md` 기준 공식 DOI 확인. 로컬 PDF는 arXiv v2 메모 유지 |

---

## 1. 한 문장 요약

이 논문은 ML에서 differential privacy를 사용하는 방식과 오용 사례를 **privacy definition, epsilon interpretation, threat model, utility trade-off, misleading claims** 관점에서 비판적으로 검토하며, W11의 DP 평가 기준을 제공한다.

---

## 2. 핵심 연구질문

| 번호 | 연구질문 |
|---|---|
| RQ1 | DP는 어떤 수학적 보장을 제공하며 어떤 보장을 제공하지 않는가? |
| RQ2 | epsilon 값을 어떻게 해석해야 하며 오용은 어디서 발생하는가? |
| RQ3 | ML에서 DP를 적용할 때 utility와 privacy trade-off를 어떻게 보고해야 하는가? |
| RQ4 | 기말논문에서 privacy guarantee를 과장하지 않으려면 어떤 문장이 필요한가? |

---

## 3. 핵심 수식

### 3.1 Differential Privacy

$$
\Pr[M(D)\in S]\leq e^{\epsilon}\Pr[M(D')\in S]+\delta
$$

| 기호 | 의미 |
|---|---|
| $D,D'$ | 한 개 레코드만 다른 인접 데이터셋 |
| $M$ | randomized mechanism |
| $\epsilon,\delta$ | privacy budget과 실패 확률 |

### 3.2 Privacy-Utility Trade-off

$$
Tradeoff=Utility-\lambda\epsilon-\mu\delta
$$

**보안 해석:** 작은 epsilon은 강한 보호를 뜻하지만, 실제 보호 수준은 threat model, composition, implementation, data pipeline에 좌우된다.

---

## 4. 위협모형·평가지표

| 항목 | 내용 |
|---|---|
| 보호 자산 | 학습 데이터, 개별 record membership, 민감 속성, output log |
| 공격자 목표 | membership inference, attribute inference, reconstruction |
| 지표 | epsilon, delta, utility drop, MI advantage, DP mechanism audit |
| 재현성 | epsilon/delta, clipping, noise multiplier, composition accounting 기록 |

---

## 5. 기말논문 연결

P01은 DP를 “마법의 개인정보 보호”로 쓰지 않도록 하는 비판적 기준이다. 기말논문에서는 privacy guarantee와 empirical leakage evaluation을 분리해 기술한다.

---

## 6. 최종 판단

P01은 W11의 DP 개념·오용 방지 핵심 문헌이다. DP 적용 여부보다 epsilon 해석과 위협모형 정합성이 중요하다.
