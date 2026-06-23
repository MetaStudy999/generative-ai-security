# P03 Summary

## Differential privacy in deep learning: A literature survey — Ke Pan et al., Neurocomputing, 2024

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W11 Differential Privacy & Membership Inference |
| 논문명 | Differential privacy in deep learning: A literature survey |
| 저자 | Ke Pan et al. |
| 출판 정보 | Neurocomputing, 589, Article 127663, 2024 |
| DOI | https://doi.org/10.1016/j.neucom.2024.127663 |
| 검증 상태 | W11 `paper_list.md` 기준 공식 DOI 확인. 로컬 PDF는 관련 DP-FL 문헌이라 지정 논문처럼 인용하지 않는 메모 유지 |

---

## 1. 한 문장 요약

이 논문은 deep learning에서 differential privacy 적용을 **training algorithm, model architecture, noise mechanism, privacy accounting, utility loss, application domain** 관점에서 정리하며, W11에서 DP를 딥러닝 보안 평가로 연결하는 종합 문헌이다.

---

## 2. 핵심 연구질문

| 번호 | 연구질문 |
|---|---|
| RQ1 | Deep learning에서 DP는 어떤 단계에 적용될 수 있는가? |
| RQ2 | Noise mechanism과 clipping은 모델 성능과 개인정보 보호에 어떤 trade-off를 만드는가? |
| RQ3 | DP deep learning 평가에서 utility, privacy, robustness를 어떻게 함께 보고해야 하는가? |
| RQ4 | 로컬 PDF와 공식 DOI 문헌이 다른 경우 참고문헌 관리를 어떻게 해야 하는가? |

---

## 3. 핵심 수식

$$
\Pr[M(D)\in S]\leq e^{\epsilon}\Pr[M(D')\in S]+\delta
$$

$$
UtilityDrop=Acc_{nonDP}-Acc_{DP}
$$

**보안 해석:** DP 적용은 이론적 개인정보 보호를 제공할 수 있지만, utility drop과 empirical leakage reduction을 별도로 확인해야 한다.

---

## 4. 위협모형·평가지표

| 항목 | 내용 |
|---|---|
| 보호 자산 | 학습 데이터, gradient, model output, confidence score |
| 공격자 목표 | membership inference, model inversion, attribute inference |
| 방어 | DP-SGD, output perturbation, objective perturbation, clipping/noise |
| 지표 | epsilon, delta, utility drop, MI advantage, privacy accountant |

---

## 5. 기말논문 연결

P03은 DP in DL의 넓은 문헌 맥락을 제공한다. 최종 보고서에서는 공식 DOI 논문과 로컬 관련 PDF를 혼동하지 않고, 공식 서지 기준으로 인용한다.

---

## 6. 최종 판단

P03은 W11의 DP deep learning 종합 문헌이다. 로컬 PDF 차이 메모를 유지하면서 공식 DOI 기준으로 사용한다.
