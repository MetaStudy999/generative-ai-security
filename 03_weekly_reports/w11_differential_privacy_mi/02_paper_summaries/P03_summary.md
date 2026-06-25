# P03 Summary

## Differential privacy in deep learning: A literature survey — Ke Pan et al., Neurocomputing, 2024

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W11 차등프라이버시(Differential Privacy) & Membership Inference |
| 공식 논문명 | Differential privacy in deep learning: A literature survey |
| 공식 저자 | Ke Pan, Yew-Soon Ong, Maoguo Gong, Hui Li, A.K. Qin, Yuan Gao |
| 공식 출판 정보 | Neurocomputing, Vol. 589, Article 127663, 2024 |
| DOI | https://doi.org/10.1016/j.neucom.2024.127663 |
| 로컬 PDF | `01_papers/pdf/03_RELATED_Fu_et_al_2024_Differentially_Private_FL_Review.pdf` |
| 로컬 PDF 상태 | W11 `paper_list.md` 기준 로컬 PDF는 Fu et al.의 DP-FL systematic review 관련 문헌이다. 공식 P03 DOI 논문과 다르므로 지정 논문처럼 인용하지 않는다. |
| 검증 상태 | W11 `paper_list.md` 기준 공식 DOI 확인. 강의자료의 `Zizheng Pan et al.` 표기는 최종 추가 확인 메모 상태로 유지 |
| PDF 확인 메모 | repo의 PDF 폴더에 P03 관련 PDF blob이 존재함을 확인했다. 다만 해당 PDF는 공식 P03 지정 논문과 다르므로, summary는 공식 DOI 기준 P03을 중심으로 작성하고 로컬 PDF는 DP-FL 보완 문헌으로만 해석한다. |
| 핵심 근거 사용 가능 여부 | 가능. 공식 P03은 DP in deep learning 종합 문헌으로, 로컬 관련 PDF는 DP-FL privacy accounting·federated setting 보완 문헌으로 제한적으로 사용 |

---

## 1. 한 문장 요약

공식 P03 논문은 deep learning에서 differential privacy 적용을 **DP definition, DP-SGD, gradient clipping, noise mechanism, privacy accounting, training/output/objective perturbation, utility loss, membership inference mitigation, model performance trade-off, application domain** 관점에서 정리하는 W11의 DP deep learning 종합 문헌이며, 로컬 관련 PDF는 federated learning 맥락에서 DP를 적용할 때 발생하는 **client update privacy, aggregation, non-IID, FL-specific privacy-utility trade-off**를 보완 설명하는 관련 문헌으로만 사용해야 한다.

---

## 2. 핵심 연구문제

> Deep learning 모델은 training data를 기억하거나 output confidence를 통해 개별 sample 정보를 노출할 수 있다. Differential privacy는 이러한 위험을 줄이는 formal privacy framework이지만, 실제 deep learning pipeline에서는 clipping, noise, accountant, training stage, output release, utility degradation을 함께 고려해야 한다.

| 번호 | 연구질문 |
|---|---|
| RQ1 | Deep learning에서 DP는 input, gradient, objective, model parameter, output 단계 중 어디에 적용될 수 있는가? |
| RQ2 | DP-SGD의 gradient clipping과 noise addition은 membership inference와 reconstruction risk를 얼마나 줄일 수 있는가? |
| RQ3 | Noise mechanism, privacy budget, accountant, batch sampling, epoch 수는 utility와 privacy guarantee에 어떤 영향을 주는가? |
| RQ4 | DP deep learning 평가에서 formal epsilon/delta와 empirical membership inference 지표를 어떻게 분리해 보고해야 하는가? |
| RQ5 | 로컬 PDF가 공식 DOI 논문과 다를 때, 관련 PDF의 내용을 지정 논문처럼 인용하지 않고 어떻게 보완 문헌으로 관리해야 하는가? |

---

## 3. 논문의 핵심 기여

| 기여 | 설명 | W11 연결 |
|---|---|---|
| DP in deep learning 체계화 | Deep learning pipeline에서 DP가 적용되는 단계와 기술을 정리 | W11 P01/P02의 DP 정의와 DP-SGD를 넓은 문헌으로 확장 |
| DP mechanism 비교 | input perturbation, objective perturbation, gradient perturbation, output perturbation 등의 차이를 정리 | privacy mechanism taxonomy 작성 근거 |
| Utility trade-off 강조 | DP 적용으로 인한 accuracy drop, convergence delay, calibration/fairness 영향 논의 | W11 평가 지표 설계 |
| Privacy attack 연결 | Membership inference, reconstruction, attribute inference 등 empirical leakage와 DP의 관계 정리 | W11 P04/P05와 연결 |
| 서지 관리 주의 | W11 P03은 로컬 PDF와 공식 DOI가 다르므로 인용 기준을 명확히 해야 함 | 기말논문 참고문헌 검증표 근거 |

---

## 4. 목차별 핵심 개괄

| 목차 | 핵심 내용 | 비전공자용 이해 |
|---|---|---|
| 1. Introduction | Deep learning은 높은 성능을 제공하지만 training sample 정보를 암묵적으로 기억할 수 있어 privacy risk가 있다. DP는 이를 완화하는 대표적 formal privacy 기술이다. | 모델이 학습 데이터의 흔적을 외울 수 있으므로, 개인정보 보호 장치가 필요하다. |
| 2. Differential Privacy Background | DP 정의, epsilon/delta, neighboring dataset, randomized mechanism, composition, privacy budget을 설명한다. | 한 사람의 데이터가 있어도 없어도 결과가 크게 달라지지 않게 만드는 원리다. |
| 3. DP Mechanisms for Deep Learning | DP-SGD, gradient clipping, Gaussian noise, objective/output perturbation, privacy accountant 등 적용 방식을 정리한다. | 학습 중 gradient를 잘라내고 noise를 넣어 개별 데이터 영향력을 낮춘다. |
| 4. Privacy Attacks and DP Effects | Membership inference, model inversion, reconstruction, attribute inference 등 공격과 DP 방어 효과를 연결한다. | 공격자가 모델 답변을 보고 “이 데이터가 학습에 있었는지” 추정하는 위험을 줄이는 것이 목표다. |
| 5. Utility and Performance Trade-off | DP 적용은 accuracy, convergence, calibration, fairness, robustness에 영향을 줄 수 있다. | 개인정보를 더 보호할수록 모델 성능이 떨어질 수 있다. |
| 6. Application Domains | 의료, 금융, 이미지, 텍스트, 추천, 분산학습 등 민감 데이터 환경에서 DP deep learning이 활용된다. | 민감한 데이터가 많은 분야일수록 DP 적용 근거가 중요하다. |
| 7. Challenges | Large model 적용, hyperparameter tuning, privacy accounting, utility degradation, empirical evaluation 표준화가 어렵다. | 큰 모델에 DP를 넣으면 계산 비용과 성능 저하 문제가 커진다. |
| 8. Conclusion | DP deep learning은 formal guarantee와 utility·empirical leakage evaluation을 함께 보고해야 한다. | 수학적 보호와 실제 성능을 동시에 확인해야 한다. |
| 로컬 관련 PDF 메모 | 로컬 PDF는 Fu et al. DP-FL review로 보이며, official P03과 다르다. W10/W11 경계의 DP-FL 보완 문헌으로만 해석한다. | PDF가 있다고 해서 공식 지정 논문과 동일하게 인용하면 안 된다. |

---

## 5. 핵심 이론 및 수식

> 아래 수식은 DP deep learning과 W11 privacy evaluation을 설명하기 위한 표준화된 표현이다. 수식은 GitHub, MS Word, PDF 변환 호환성을 위해 Markdown 표 밖의 LaTeX block math로 작성한다.

### 5.1 Differential Privacy 정의

Randomized mechanism $M$이 모든 neighboring dataset $D,D'$와 모든 출력 집합 $S$에 대해 다음을 만족하면 $(\epsilon,\delta)$-DP라고 한다.

$$
\Pr[M(D)\in S]\leq e^{\epsilon}\Pr[M(D')\in S]+\delta
$$

| 기호 | 의미 |
|---|---|
| $D,D'$ | 한 개 record만 다른 인접 데이터셋 |
| $M$ | randomized mechanism |
| $S$ | 가능한 출력 집합 |
| $\epsilon$ | privacy budget |
| $\delta$ | 실패확률 |

### 보안적 의미

DP는 개별 record가 결과에 미치는 영향을 제한한다. 그러나 epsilon/delta와 적용 mechanism을 명확히 쓰지 않으면 보호 수준을 판단할 수 없다.

---

### 5.2 DP-SGD Gradient Clipping

개별 sample gradient의 norm을 clipping norm $C$ 이하로 제한한다.

$$
\bar{g}_i=g_i\cdot \min\left(1,\frac{C}{\|g_i\|_2}\right)
$$

### 보안적 의미

Clipping은 특정 sample이 gradient에 과도하게 영향을 미치는 것을 막는다. clipping norm이 너무 크면 privacy 효과가 약해지고, 너무 작으면 utility가 낮아질 수 있다.

---

### 5.3 DP-SGD Noise Addition

Clipping된 gradient에 Gaussian noise를 더한다.

$$
\tilde{g}=\frac{1}{B}\left(\sum_{i=1}^{B}\bar{g}_i+\mathcal{N}(0,\sigma^2C^2I)\right)
$$

| 기호 | 의미 |
|---|---|
| $B$ | batch size |
| $\sigma$ | noise multiplier |
| $C$ | clipping norm |

### 보안적 의미

Noise는 privacy를 강화하지만 학습 정확도와 수렴 속도를 낮출 수 있다.

---

### 5.4 Privacy Accounting

반복 학습 과정에서 privacy loss를 accountant로 누적 계산한다.

$$
\epsilon_{total}=Accountant(q,\sigma,T,\delta)
$$

| 기호 | 의미 |
|---|---|
| $q$ | sampling rate |
| $\sigma$ | noise multiplier |
| $T$ | training step 수 |
| $\delta$ | 실패확률 |

### 보안적 의미

같은 noise를 넣어도 epoch와 sampling rate가 다르면 최종 privacy budget이 달라진다. accountant 기록이 없으면 DP claim을 검증하기 어렵다.

---

### 5.5 Utility Drop

DP 적용 전후 성능 손실이다.

$$
UtilityDrop=Acc_{nonDP}-Acc_{DP}
$$

### 보안적 의미

DP 논문은 privacy budget만이 아니라 baseline 대비 utility drop을 함께 제시해야 한다. 성능이 과도하게 낮으면 실무 적용이 어렵다.

---

### 5.6 Membership Inference Risk Reduction

DP 적용 전후 membership inference advantage 차이를 측정한다.

$$
MIReduction=Adv_{MI}^{nonDP}-Adv_{MI}^{DP}
$$

### 보안적 의미

DP의 formal guarantee와 MIA 실험은 서로 다른 증거다. 둘을 함께 제시하면 수학적 보장과 실제 leakage 감소를 구분해 설명할 수 있다.

---

### 5.7 DP-FL Related Risk

로컬 관련 PDF처럼 DP가 Federated Learning에 적용되는 경우, client update privacy와 aggregation risk를 함께 고려한다.

$$
Risk_{DP\text{-}FL}=\alpha LeakageRisk+\beta UtilityDrop+\gamma CommCost-\lambda DefenseCoverage
$$

### 보안적 의미

DP-FL에서는 DP noise가 privacy를 높일 수 있지만, non-IID client drift, communication cost, aggregation robustness와 얽힌다. 따라서 로컬 관련 PDF는 W10/W11 연결 보조 문헌으로만 사용한다.

---

## 6. AI 원리 70% 관점 분석

| 원리 항목 | 설명 | W11/P03에서의 의미 |
|---|---|---|
| DP Deep Learning | 딥러닝 학습 과정에 DP를 적용 | W11 공식 P03의 핵심 |
| DP-SGD | gradient clipping과 noise addition 결합 | 대표 학습 알고리즘 |
| Objective Perturbation | 목적함수에 noise 또는 regularization 추가 | DP 적용 위치 중 하나 |
| Output Perturbation | 모델 출력 또는 결과에 noise 추가 | inference privacy 보호 |
| Privacy Accounting | 반복 학습의 privacy loss 추적 | epsilon_total 산출 근거 |
| Utility Evaluation | accuracy, loss, convergence, calibration 평가 | privacy-utility trade-off |
| Empirical Leakage | MIA, reconstruction, attribute inference 평가 | W11 P04/P05와 연결 |
| DP-FL 보완 | 로컬 PDF의 관련 주제 | 공식 P03과 혼동 금지 |

---

## 7. 보안 이슈 30% 관점 분석

| 보안 항목 | DP Deep Learning 관점 해석 | 대표 평가 지표 |
|---|---|---|
| 기밀성 | training record와 membership 정보 보호 | epsilon, delta, MI advantage |
| 무결성 | noise가 decision boundary와 model calibration을 왜곡할 수 있음 | UtilityDrop, ECE, robustness drop |
| 가용성 | DP 학습은 계산비용과 수렴시간을 증가시킬 수 있음 | training time, convergence delay |
| 프라이버시 | DP scope 밖의 logging, preprocessing, model release에서 leakage 가능 | pipeline leakage check |
| 안전성 | 고위험 domain에서 privacy-utility trade-off가 downstream risk로 연결 | subgroup accuracy, failure case |
| 책임성 | DP 설정·accountant·baseline·attack evaluation을 기록해야 감사 가능 | ReportingCompleteness, accountant log |

---

## 8. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | training data, individual membership, sensitive attribute, gradient, model parameter, model output, privacy accountant log |
| 공격자 목표 | membership inference, model inversion, reconstruction, attribute inference, output confidence exploitation |
| 공격자 능력 | black-box query, white-box access, auxiliary data 보유, repeated query, confidence score 관찰 |
| 공격 경로 | training data → DP/non-DP training → model release/query → output/confidence analysis → privacy inference |
| 방어자 능력 | DP-SGD, clipping, Gaussian noise, accountant, output perturbation, empirical MIA evaluation, pipeline audit |
| 제외 범위 | 실제 개인정보 기반 공격 실험, 실제 민감 데이터 재식별, 공격 코드 제공, 공식 P03과 로컬 관련 PDF 혼동 인용 |

---

## 9. 평가방법 및 지표

| 평가축 | 지표 | 의미 | W11/P03 활용 |
|---|---|---|---|
| Formal privacy | epsilon, delta, epsilon_total | DP 보장 강도 | 공식 DP 평가 |
| Mechanism setting | clipping norm, noise multiplier, sampling rate | DP-SGD 핵심 설정 | 재현성 필수 항목 |
| Utility | accuracy, loss, UtilityDrop | DP 적용 후 성능 손실 | privacy-utility trade-off |
| Empirical leakage | MI advantage, MIReduction, reconstruction error | 실제 leakage 위험 변화 | P04/P05 연결 |
| Robustness/fairness | robustness drop, subgroup accuracy, fairness gap | DP의 부작용 | 고위험 domain 평가 |
| Accounting quality | accountant type, composition scope | privacy budget 계산 근거 | DP claim audit |
| Reporting quality | ReportingCompleteness | hyperparameter·privacy 보고 충분성 | 논문 검수 기준 |
| 서지 정확성 | official DOI match, local PDF mismatch flag | 참고문헌 정확성 | 기말논문 검증표 |

---

## 10. 재현성 체크리스트

| 항목 | 기록해야 할 내용 |
|---|---|
| Bibliographic status | 공식 DOI 논문과 로컬 PDF 동일 여부, mismatch flag |
| Dataset | dataset name, split, sensitive attribute 여부, preprocessing |
| Model | architecture, optimizer, loss, parameter count |
| DP mechanism | DP-SGD, objective perturbation, output perturbation 등 |
| DP-SGD setting | clipping norm, noise multiplier, batch size, sampling rate, epoch |
| Privacy accountant | accountant type, epsilon, delta, epsilon_total, composition scope |
| Baseline | non-DP baseline accuracy/loss와 DP model result |
| Empirical attack | MIA, reconstruction, attribute inference 평가 여부와 지표 |
| Logs | config, seed, accountant log, checkpoint, evaluation script |
| 한계 | 로컬 PDF는 공식 P03 지정 논문이 아니므로 참고문헌에서는 공식 DOI 논문을 우선 사용 |

---

## 11. 논문의 고유 기여

1. Deep learning에서 DP가 적용되는 주요 mechanism과 평가 관점을 종합한다.
2. DP-SGD뿐 아니라 objective/output perturbation과 privacy accounting까지 포함한 broader taxonomy를 제공한다.
3. Privacy 보장과 utility degradation, empirical leakage evaluation을 함께 보고해야 함을 강조한다.
4. W11 P01/P02의 DP 정의·DP-SGD 논의를 더 넓은 DP deep learning 문헌으로 확장한다.
5. W11 P03은 로컬 PDF mismatch를 포함하므로, 기말논문에서 참고문헌 검증표의 중요성을 보여주는 사례이기도 하다.

---

## 12. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 로컬 PDF 불일치 | P03 로컬 PDF는 공식 DOI 논문이 아니라 DP-FL 관련 문헌이다. | 공식 DOI 기준으로 인용하고 로컬 PDF는 관련 보완 문헌으로 표시 |
| Utility trade-off | DP 적용은 accuracy와 convergence를 낮출 수 있다. | UtilityDrop과 baseline 병기 |
| Accounting 복잡성 | accountant와 composition scope가 다르면 epsilon 해석이 달라진다. | accountant type과 입력값 기록 |
| Empirical/formal 혼동 | MIA 실험 감소가 DP formal guarantee를 대체하지 않는다. | formal 지표와 empirical 지표 분리 |
| 대형 모델 적용 어려움 | large model에서 DP training 비용과 utility loss가 크다. | 문헌 기반 비교 또는 toy/small model로 제한 |
| Pipeline leakage | DP mechanism 밖의 preprocessing, logging, output release 위험 | pipeline audit checklist 포함 |

---

## 13. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | DP deep learning은 formal privacy와 utility/empirical leakage를 함께 평가해야 한다는 문제의식 |
| 2장 관련연구 | 공식 P03 DOI 논문을 DP in deep learning literature survey로 정리하고, 로컬 PDF mismatch는 검증표에 기록 |
| 3장 위협모형 | training sample, gradient, model output, confidence score, accountant log 보호 자산 정의 |
| 4장 연구방법 | epsilon, delta, UtilityDrop, MIReduction, ReportingCompleteness, official DOI match 지표 설계 |
| 5장 분석 | DP mechanism taxonomy와 official/local PDF mismatch 관리표 제시 |
| 6장 보안적 함의 | DP 적용 범위, empirical attack 평가, privacy-utility trade-off, 참고문헌 검증 필요성 해석 |

---

## 14. 기말논문 연결 3문장

1. W11에서 기말논문에 반영할 개념: DP in deep learning은 학습 알고리즘, model output, objective, gradient 단계에서 privacy protection을 제공할 수 있지만, epsilon/delta와 utility drop을 함께 보고해야 한다.
2. W11에서 기말논문에 반영할 표·그림·실험: DP mechanism taxonomy, UtilityDrop·MIReduction 비교표, privacy accountant checklist, 공식 DOI와 로컬 PDF mismatch 검증표를 반영한다.
3. W11이 LLM/RAG 보안 감사 프레임워크와 연결되는 지점: LLM/RAG 학습·로그·검색 결과 보호를 DP로 주장하려면 mechanism scope, accountant, empirical leakage evaluation, 참고문헌 검증 증거를 W14/W15 evidence chain에 포함해야 한다.

---

## 15. 최종 판단

P03은 W11의 DP deep learning 종합 문헌이다. 다만 W11 `paper_list.md` 기준 로컬 PDF는 공식 DOI 논문과 다른 DP-FL 관련 문헌이므로, 기말논문 참고문헌에는 공식 DOI 논문인 Ke Pan et al.의 Neurocomputing 논문을 우선 사용해야 한다. 로컬 PDF는 DP-FL와 FL privacy accounting을 보완하는 관련 문헌으로만 제한해 활용하는 것이 적절하다.

---

## 16. 변환 호환성 메모

```bash
pandoc P03_summary.md -o P03_summary.docx
pandoc P03_summary.md -o P03_summary.pdf --pdf-engine=xelatex
```
