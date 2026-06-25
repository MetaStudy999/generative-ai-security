# P04 Summary

## Adversarial Robustness of Neural Networks from the Perspective of Lipschitz Calculus: A Survey — Monty-Maximilian Zuhlke, Daniel Kudenko, ACM Computing Surveys, 2025

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W12 신경망 검증(Neural Network Verification) & XAI Robustness |
| 공식 논문명 | Adversarial Robustness of Neural Networks from the Perspective of Lipschitz Calculus: A Survey |
| 공식 저자 | Monty-Maximilian Zuhlke, Daniel Kudenko |
| 공식 출판 정보 | ACM Computing Surveys, 2025 |
| DOI | https://doi.org/10.1145/3648351 |
| 로컬 PDF | `01_papers/pdf/04_RELATED_Finlay_et_al_2018_Lipschitz_Adversarial_Robustness.pdf` |
| 로컬 PDF 상태 | W12 `paper_list.md` 기준 로컬 PDF는 Chris Finlay et al., `Lipschitz Regularized Deep Neural Networks Generalize and are Adversarially Robust`, arXiv:1808.09540 관련 보조 문헌이다. 공식 P04 DOI 논문과 동일 문헌으로 단정하지 않는다. |
| 검증 상태 | W12 `paper_list.md` 기준 관련 논문 공식 DOI 확인. 강의자료의 `Inaki Pérez et al.` 표기와 최종 반영표의 `Monty-Maximilian Zuhlke, Daniel Kudenko` 표기 차이, 로컬 PDF 차이 메모 유지 |
| PDF 확인 메모 | repo의 PDF 폴더에 P04 관련 PDF blob이 존재함을 확인했다. 다만 로컬 PDF는 공식 P04 지정 논문과 다르거나 보조 문헌이므로, summary는 공식 DOI 기준 P04를 중심으로 작성하고 로컬 PDF는 Lipschitz regularization 보완 문헌으로만 해석한다. |
| 핵심 근거 사용 가능 여부 | 가능. W12에서 Lipschitz constant, robust margin, certified robustness, Lipschitz regularization, clean-robust trade-off를 설명하는 핵심 관련 문헌으로 사용 |

---

## 1. 한 문장 요약

공식 P04 논문은 신경망의 adversarial robustness를 **Lipschitz calculus, Lipschitz constant, local/global sensitivity, margin-based robustness, certified radius, spectral norm, gradient norm, Lipschitz regularization, robustness-accuracy trade-off, verification bound** 관점에서 정리하며, W12에서 경험적 adversarial testing과 수학적 robustness bound를 구분해 설명하는 핵심 관련 문헌이다.

---

## 2. 핵심 연구문제

> 신경망이 입력 변화에 얼마나 민감한지는 Lipschitz constant와 margin으로 분석할 수 있다. Lipschitz bound가 작고 decision margin이 충분히 크면 작은 perturbation에 대한 certified robustness를 주장할 수 있지만, 실제 모델에서는 bound의 tightness, norm 선택, 계산 비용, clean accuracy와의 trade-off가 문제다.

| 번호 | 연구질문 |
|---|---|
| RQ1 | Lipschitz constant는 입력 perturbation이 출력 변화에 미치는 영향을 어떻게 상한으로 제한하는가? |
| RQ2 | Local Lipschitz bound와 global Lipschitz bound는 adversarial robustness 평가에서 어떤 차이를 갖는가? |
| RQ3 | Robust margin 조건은 certified radius와 prediction invariance를 어떻게 연결하는가? |
| RQ4 | Lipschitz regularization, spectral normalization, gradient penalty는 robust accuracy와 clean accuracy에 어떤 trade-off를 만드는가? |
| RQ5 | 로컬 PDF가 공식 DOI 논문과 다른 관련 문헌일 때, Lipschitz robustness summary와 참고문헌 인용을 어떻게 분리 관리해야 하는가? |

---

## 3. 논문의 핵심 기여

| 기여 | 설명 | W12 연결 |
|---|---|---|
| Lipschitz 관점 체계화 | adversarial robustness를 입력 변화 대비 출력 변화의 상한으로 해석 | W12 수학적 robustness 평가축 |
| Robust margin 조건 제시 | margin과 Lipschitz bound로 certified robustness를 설명 | P01 verification과 연결 |
| 정규화 방법 비교 | Lipschitz regularization, spectral norm control, gradient penalty 등 방법을 정리 | empirical/certified defense 연결 |
| Bound tightness 문제 강조 | 너무 느슨한 bound는 의미 있는 certificate를 제공하기 어렵다는 점을 제시 | formal-empirical gap 해석 |
| 로컬 PDF 관리 주의 | W12 P04는 공식 DOI와 로컬 PDF가 다르므로 인용 기준 분리가 필요 | 기말논문 참고문헌 검증표 근거 |

---

## 4. 목차별 핵심 개괄

| 목차 | 핵심 내용 | 비전공자용 이해 |
|---|---|---|
| 1. Introduction | Adversarial robustness는 작은 입력 변화에도 모델 출력이 안정적인지를 다루며, Lipschitz calculus는 이를 수학적으로 분석하는 도구다. | AI가 작은 노이즈에도 답을 바꾸지 않는지 수학적으로 보는 방법이다. |
| 2. Lipschitz Basics | 함수의 입력 변화와 출력 변화 사이의 상한을 Lipschitz constant로 정의한다. | 입력이 조금 바뀌었을 때 출력이 얼마나 크게 바뀔 수 있는지 제한하는 숫자다. |
| 3. Neural Network Lipschitz Bounds | layer별 operator norm, activation function, composition rule을 이용해 전체 network bound를 추정한다. | 여러 층을 거치며 변화가 얼마나 커질 수 있는지 계산한다. |
| 4. Robustness and Margin | decision margin이 Lipschitz bound와 perturbation radius보다 크면 예측 불변성을 보일 수 있다. | 정답과 두 번째 후보의 차이가 충분히 크면 작은 교란에도 답이 바뀌지 않는다. |
| 5. Lipschitz Regularization | 학습 중 Lipschitz constant나 gradient norm을 제한해 모델을 덜 민감하게 만드는 방법을 정리한다. | 모델이 입력 변화에 과민하게 반응하지 않도록 훈련하는 것이다. |
| 6. Certified and Empirical Robustness | Lipschitz bound 기반 certificate와 adversarial attack 기반 empirical test를 구분한다. | 공격 테스트에서 버틴 것과 수학적으로 보장된 것은 다르다. |
| 7. Trade-offs | Lipschitz constraint는 robustness를 높일 수 있지만 clean accuracy, expressivity, training cost, fairness에 영향을 줄 수 있다. | 모델을 너무 둔하게 만들면 평소 성능이 낮아질 수 있다. |
| 8. Challenges | tight bound 계산, large model scalability, norm 선택, local/global bound 차이, benchmark 표준화가 과제로 남는다. | 실제 큰 모델에서 정확한 bound를 빠르게 계산하기는 어렵다. |
| 로컬 관련 PDF 메모 | 로컬 PDF는 Finlay et al. 2018 Lipschitz regularized DNN 관련 문헌으로 보이며, official P04와 동일 문헌으로 단정하지 않는다. | PDF가 있다고 해서 공식 지정 논문과 동일하게 인용하면 안 된다. |

---

## 5. 핵심 이론 및 수식

> 아래 수식은 Lipschitz robustness와 W12 robustness certificate 평가를 설명하기 위한 표준화된 표현이다. 실제 공격 절차 제공이 아니라 평가 지표와 방어 검증 구조를 설명하기 위한 것이다.

### 5.1 Lipschitz Bound

함수 $f$가 Lipschitz constant $L$을 가지면 입력 변화에 대한 출력 변화가 다음처럼 제한된다.

$$
\|f(x)-f(x')\|\leq L\|x-x'\|
$$

| 기호 | 의미 |
|---|---|
| $f$ | neural network 또는 classifier score function |
| $x,x'$ | 원본 입력과 perturbation 입력 |
| $L$ | Lipschitz constant |

### 비전공자용 설명

입력이 조금 바뀌었을 때 출력이 얼마나 크게 바뀔 수 있는지를 제한하는 안전벨트 같은 수식이다.

### 보안적 의미

$L$이 작을수록 입력 변화에 둔감하다는 뜻이지만, $L$만 작다고 모든 공격을 막는 것은 아니다. margin과 입력 영역도 함께 봐야 한다.

---

### 5.2 Network Lipschitz Bound via Layers

여러 layer의 Lipschitz 상수를 곱해 전체 network의 상한을 추정할 수 있다.

$$
L_f\leq \prod_{l=1}^{m} L_l
$$

| 기호 | 의미 |
|---|---|
| $L_l$ | layer $l$의 Lipschitz bound |
| $L_f$ | 전체 network의 Lipschitz bound |

### 보안적 의미

Layer별 norm이 커지면 전체 bound가 빠르게 커질 수 있다. Spectral normalization이나 weight regularization은 layer별 bound를 줄이는 방법이다.

---

### 5.3 Robust Margin 조건

분류 margin이 perturbation으로 인한 최대 출력 변화보다 크면 예측이 유지될 수 있다.

$$
margin(x)>L\epsilon \Rightarrow f(x')=f(x),\quad \forall x'\in B_\epsilon(x)
$$

| 기호 | 의미 |
|---|---|
| $margin(x)$ | 정답 class score와 경쟁 class score 사이의 차이 |
| $\epsilon$ | perturbation radius |
| $L$ | Lipschitz bound |

### 보안적 의미

이 조건은 특정 norm, 특정 bound, 특정 입력 영역에서만 의미가 있다. Certificate claim에는 norm과 epsilon을 반드시 적어야 한다.

---

### 5.4 Certified Radius

Lipschitz bound와 margin을 이용해 보장 가능한 perturbation radius를 추정할 수 있다.

$$
r_{cert}(x)=\frac{margin(x)}{L}
$$

### 보안적 의미

$L$이 너무 느슨하게 추정되면 certified radius가 매우 작아져 실용적 의미가 약해진다. tight bound가 중요하다.

---

### 5.5 Lipschitz Regularization Objective

학습 objective에 Lipschitz 관련 penalty를 추가할 수 있다.

$$
\min_\theta \mathcal{L}_{task}(\theta)+\lambda \Omega_{Lip}(\theta)
$$

| 기호 | 의미 |
|---|---|
| $\mathcal{L}_{task}$ | 원래 task loss |
| $\Omega_{Lip}$ | Lipschitz 또는 gradient norm 관련 penalty |
| $\lambda$ | regularization strength |

### 보안적 의미

정규화 강도가 너무 약하면 robustness 효과가 작고, 너무 강하면 clean accuracy와 표현력이 떨어질 수 있다.

---

### 5.6 Local Lipschitz Sensitivity

특정 입력 주변의 local sensitivity를 측정할 수 있다.

$$
L_{local}(x)=\sup_{x'\in B_\epsilon(x)}\frac{\|f(x)-f(x')\|}{\|x-x'\|}
$$

### 보안적 의미

Global bound보다 local bound가 더 tight할 수 있다. 그러나 local bound는 특정 영역 밖 안전성을 보장하지 않는다.

---

### 5.7 Clean-Robust-Lipschitz Trade-off

Lipschitz regularization은 clean accuracy와 robust accuracy의 균형을 바꿀 수 있다.

$$
Tradeoff=Acc_{clean}+\alpha RobustAcc-\beta L_{estimate}-\gamma Cost_{train}
$$

### 보안적 의미

좋은 robustness 방법은 robust accuracy를 높이면서 clean accuracy, 계산비용, fairness를 과도하게 희생하지 않아야 한다.

---

## 6. AI 원리 70% 관점 분석

| 원리 항목 | 설명 | W12/P04에서의 의미 |
|---|---|---|
| Lipschitz Constant | 입력 변화 대비 출력 변화의 상한 | 수학적 robustness 핵심 |
| Local/Global Bound | 특정 입력 주변 vs 전체 영역 bound | certificate scope 구분 |
| Margin | class score 차이 | robust radius 계산 근거 |
| Spectral Norm | layer의 operator norm 제어 | Lipschitz bound 감소 방법 |
| Gradient Norm | 입력 민감도와 관련 | regularization 대상 |
| Lipschitz Regularization | 모델 민감도를 줄이는 학습법 | empirical/certified defense 연결 |
| Certified Radius | 보장 가능한 perturbation 크기 | formal claim 기준 |
| Trade-off | clean accuracy·robustness·cost 균형 | P05와 연결 |

---

## 7. 보안 이슈 30% 관점 분석

| 보안 항목 | Lipschitz Robustness 관점 해석 | 대표 평가 지표 |
|---|---|---|
| 기밀성 | 모델 구조와 bound 정보가 공격자에게 단서가 될 수 있음 | model/config access control |
| 무결성 | 입력 perturbation이 decision boundary를 넘도록 유도할 수 있음 | robust accuracy, ASR |
| 가용성 | Lipschitz regularization과 certificate 계산이 학습·추론 비용을 증가 | training cost, verification time |
| 프라이버시 | robustness 평가 trace가 민감한 입력 데이터를 포함할 수 있음 | trace anonymization |
| 안전성 | 작은 perturbation에도 안전한 출력 유지가 중요 | certified radius, robust margin |
| 책임성 | norm, epsilon, bound method, solver를 기록해야 claim 감사 가능 | bound report completeness |

---

## 8. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | decision boundary, margin, Lipschitz bound, certified radius, model configuration, robustness certificate |
| 공격자 목표 | small perturbation으로 decision boundary crossing, bound가 약한 영역 탐색, defense bypass |
| 공격자 능력 | input perturbation, surrogate model 사용, norm/budget 내 탐색, confidence 관찰, gradient 접근 가능성 |
| 공격 경로 | clean input → perturbation within budget → output shift bounded/unbounded → misclassification 또는 unsafe decision |
| 방어자 능력 | Lipschitz regularization, spectral normalization, gradient penalty, certified radius 계산, adversarial testing, certificate logging |
| 제외 범위 | 실제 시스템 공격, 구체적 adversarial example 생성 절차, 악용 코드, 검증 범위 밖 안전 보장 주장 |

---

## 9. 평가방법 및 지표

| 평가축 | 지표 | 의미 | W12/P04 활용 |
|---|---|---|---|
| 민감도 | Lipschitz estimate, local sensitivity | 입력 변화에 대한 출력 변화 상한 | 핵심 분석 |
| 인증 강건성 | certified radius, certified robust rate | 수학적 보장 범위 | P01 연결 |
| 경험적 강건성 | robust accuracy, ASR | attack test 결과 | P02 연결 |
| 정상 성능 | clean accuracy | 원본 입력 성능 | utility baseline |
| Trade-off | clean-robust gap, Cost_train | 성능·강건성·비용 균형 | P05 연결 |
| Bound 품질 | bound tightness, inconclusive rate | certificate 유용성 | 검증 품질 |
| 재현성 | norm, epsilon, bound method, solver | 결과 재현 가능성 | W15 evidence chain |
| 서지 정확성 | official DOI match, local PDF mismatch flag | 참고문헌 정확성 | 기말논문 검증표 |

---

## 10. 재현성 체크리스트

| 항목 | 기록해야 할 내용 |
|---|---|
| Bibliographic status | 공식 DOI 논문과 로컬 PDF 동일 여부, mismatch flag |
| Model | architecture, dataset, model hash, training config |
| Norm/budget | $L_p$ norm, epsilon, input bounds |
| Bound method | spectral norm, interval bound, local/global Lipschitz, solver/tool |
| Regularization | penalty type, $\lambda$, gradient/spectral constraint |
| Evaluation | clean accuracy, robust accuracy, certified radius, Lipschitz estimate |
| Cost | training time, verification time, memory, timeout |
| Comparison | adversarial attack result와 certified result 분리 |
| Logs | seed, config, model checkpoint, bound report, failure case |
| 한계 | 특정 norm과 input domain 밖에는 robustness를 보장하지 않음 |

---

## 11. 논문의 고유 기여

1. Adversarial robustness를 Lipschitz calculus 관점에서 체계적으로 설명한다.
2. 입력 민감도, margin, certified radius를 연결해 수학적 robustness claim을 구성하는 방법을 제공한다.
3. Lipschitz regularization과 spectral norm 제어 같은 방어법의 원리와 한계를 정리한다.
4. Empirical robust accuracy와 certified Lipschitz bound를 분리해 보고해야 함을 보여준다.
5. W12 P04는 로컬 PDF mismatch가 있으므로 참고문헌 검증표와 공식 DOI 우선 인용의 중요성을 보여주는 사례다.

---

## 12. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 로컬 PDF 불일치 | P04 로컬 PDF는 공식 DOI 논문과 다른 Finlay et al. 2018 관련 문헌이다. | 공식 DOI 기준으로 인용하고 로컬 PDF는 보완 문헌으로 표시 |
| Bound tightness 문제 | Global Lipschitz bound는 너무 느슨해 실용성이 낮을 수 있다. | local bound와 certified radius를 구분 |
| Clean accuracy 손실 | 강한 Lipschitz regularization은 표현력과 성능을 낮출 수 있다. | clean accuracy와 robust accuracy 병기 |
| Norm 의존성 | 특정 norm에서의 robustness가 다른 norm으로 일반화되지 않는다. | norm/epsilon을 명시 |
| 계산 비용 | bound 계산과 regularization 비용이 클 수 있다. | verification/training cost 기록 |
| Formal/empirical 혼동 | Lipschitz estimate가 낮아도 empirical attack 평가와 certificate 범위가 다를 수 있다. | empirical result와 certified result 분리 |

---

## 13. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | adversarial robustness는 입력 민감도와 margin을 통해 수학적으로 분석할 수 있다는 문제의식 |
| 2장 관련연구 | 공식 P04 DOI 논문을 Lipschitz calculus 기반 robustness survey로 정리하고, 로컬 PDF mismatch는 검증표에 기록 |
| 3장 위협모형 | decision boundary, margin, Lipschitz bound, certified radius, certificate 보호 자산 정의 |
| 4장 연구방법 | Lipschitz estimate, certified radius, robust accuracy, clean accuracy, bound tightness, cost 지표 설계 |
| 5장 분석 | Lipschitz bound와 robust margin 관계 그림, empirical vs certified robustness 비교표 제시 |
| 6장 보안적 함의 | Lipschitz claim 범위, norm 의존성, clean-robust trade-off, 참고문헌 검증 필요성 해석 |

---

## 14. 기말논문 연결 3문장

1. W12에서 기말논문에 반영할 개념: Lipschitz constant는 입력 변화에 대한 출력 변화의 상한을 제공하며, margin이 $L\epsilon$보다 크면 특정 perturbation 범위에서 prediction invariance를 주장할 수 있다.
2. W12에서 기말논문에 반영할 표·그림·실험: Lipschitz bound 수식, robust margin 조건, certified radius·robust accuracy·clean accuracy 비교표, 공식 DOI/로컬 PDF mismatch 검증표를 반영한다.
3. W12가 LLM/RAG 보안 감사 프레임워크와 연결되는 지점: LLM/RAG 모델의 embedding perturbation, retrieval score perturbation, confidence shift도 sensitivity bound와 margin 관점으로 분석할 수 있으며, bound method와 evidence log를 W14/W15 evidence chain에 포함해야 한다.

---

## 15. 최종 판단

P04는 W12의 Lipschitz 기반 adversarial robustness 핵심 관련 문헌이다. 다만 W12 `paper_list.md` 기준 로컬 PDF는 공식 DOI 논문과 다른 Finlay et al. 2018 Lipschitz regularization 관련 문헌으로 기록되어 있으므로, 기말논문 참고문헌에는 공식 DOI 논문인 Zuhlke and Kudenko의 ACM Computing Surveys 논문을 우선 사용해야 한다. 로컬 PDF는 Lipschitz regularization 일반 배경을 보완하는 관련 문헌으로만 제한해 활용하는 것이 적절하다.

---

## 16. 변환 호환성 메모

```bash
pandoc P04_summary.md -o P04_summary.docx
pandoc P04_summary.md -o P04_summary.pdf --pdf-engine=xelatex
```
