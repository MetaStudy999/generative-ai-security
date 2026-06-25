# P01 Summary

## A Review of Abstraction Methods Toward Verifying Neural Networks — Fateh Boudardara et al., ACM TECS, 2024

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W12 신경망 검증(Neural Network Verification) & XAI Robustness |
| 공식 논문명 | A Review of Abstraction Methods Toward Verifying Neural Networks |
| 공식 저자 | Fateh Boudardara et al. |
| 공식 출판 정보 | ACM Transactions on Embedded Computing Systems, 2024 |
| DOI | https://doi.org/10.1145/3617508 |
| 로컬 PDF | `01_papers/pdf/01_RELATED_Meng_et_al_2022_DNN_Robustness_Formal_Verification.pdf` |
| 로컬 PDF 상태 | W12 `paper_list.md` 기준 로컬 PDF는 Meng et al., `Adversarial Robustness of Deep Neural Networks: A Survey from a Formal Verification Perspective`, arXiv:2206.12227, 2022 관련 보조 문헌이다. 공식 P01 DOI 논문과 동일 문헌으로 단정하지 않는다. |
| 검증 상태 | W12 `paper_list.md` 기준 공식 DOI 확인. 강의계획서 표기와 로컬 PDF 파일명·매체 정보 차이 메모 유지 |
| PDF 확인 메모 | repo의 PDF 폴더에 P01 관련 PDF blob이 존재함을 확인했다. 다만 로컬 PDF는 공식 P01 지정 논문과 다르거나 보조 문헌이므로, summary는 공식 DOI 기준 P01을 중심으로 작성하고 로컬 PDF는 formal verification 관점 보완 문헌으로만 해석한다. |
| 핵심 근거 사용 가능 여부 | 가능. W12에서 abstraction 기반 neural network verification, reachability over-approximation, safety property, certified robustness, verification certificate를 설명하는 핵심 문헌으로 사용 |

---

## 1. 한 문장 요약

공식 P01 논문은 신경망 검증에서 입력공간과 hidden-state 공간의 복잡성을 줄이기 위한 abstraction 방법을 **state-space abstraction, abstract interpretation, over-approximation, reachability analysis, safety property, robustness property, soundness-completeness trade-off, verification scalability, certificate generation** 관점에서 정리하며, W12에서 DNN 보안 주장을 empirical adversarial testing이 아니라 **형식 명세와 검증 가능한 보장 범위**로 평가하는 핵심 문헌이다.

---

## 2. 핵심 연구문제

> Deep neural network는 고차원 비선형 함수이므로 모든 입력 영역을 직접 탐색해 안전성을 검증하기 어렵다. Abstraction method는 입력과 중간 activation의 가능한 범위를 보수적으로 근사해 검증을 가능하게 하지만, 정확도·확장성·보장 범위 사이의 trade-off가 발생한다.

| 번호 | 연구질문 |
|---|---|
| RQ1 | 신경망 검증에서 abstraction은 입력공간·activation 공간·출력공간의 상태공간 폭발을 어떻게 줄이는가? |
| RQ2 | Over-approximation, interval abstraction, polyhedral abstraction, zonotope, abstract interpretation, reachability analysis는 safety property 검증에 어떻게 사용되는가? |
| RQ3 | Abstraction 기반 검증은 adversarial robustness, output bound, safety constraint, reachability property를 어떤 조건에서 보장할 수 있는가? |
| RQ4 | Soundness, precision, scalability, verification time, false alarm 사이의 trade-off는 어떻게 평가해야 하는가? |
| RQ5 | 로컬 PDF가 공식 DOI 논문과 다른 관련 문헌일 때, 기말논문에서는 공식 인용과 보조 문헌 해석을 어떻게 분리해야 하는가? |

---

## 3. 논문의 핵심 기여

| 기여 | 설명 | W12 연결 |
|---|---|---|
| Abstraction method taxonomy | 신경망 검증에서 사용되는 abstraction 기법을 체계적으로 정리 | W12 formal verification 핵심 |
| Reachability over-approximation | 입력 영역이 신경망을 통과한 뒤 도달 가능한 출력 범위를 보수적으로 계산하는 관점 제공 | certified robustness 평가 |
| Safety property 중심 | 분류 불변성, output bound, unsafe region 회피 등 명세 기반 검증을 강조 | empirical test와 formal claim 분리 |
| Trade-off 정리 | abstraction precision, verification scalability, soundness, timeout 문제를 비교 | 검증 결과 해석 기준 |
| Certificate reporting 근거 | model, property, input bound, solver, timeout, certificate log를 기록해야 함을 뒷받침 | W15 reproducibility 연결 |

---

## 4. 목차별 핵심 개괄

| 목차 | 핵심 내용 | 비전공자용 이해 |
|---|---|---|
| 1. Introduction | DNN은 높은 성능을 보이지만 adversarial perturbation과 unsafe behavior에 취약할 수 있어 formal verification이 필요하다. | AI가 테스트에서는 잘 맞혀도, 아주 작은 입력 변화에 위험한 결정을 할 수 있다. |
| 2. Neural Network Verification Background | Neural network, activation function, robustness property, safety property, reachability, decision boundary의 기본 개념을 설명한다. | 검증은 “이 입력 범위에서는 AI가 반드시 같은 결정을 하는가”를 수학적으로 확인하는 일이다. |
| 3. Abstraction Principles | 고차원 입력과 중간 activation을 interval, polytope, zonotope 등 더 다루기 쉬운 추상공간으로 근사한다. | 모든 경우를 하나씩 보는 대신 가능한 범위를 큰 상자로 감싸서 안전한지 보는 방식이다. |
| 4. Abstract Interpretation Methods | 신경망 각 layer를 통과할 때 가능한 값의 범위를 전파하고 over-approximation으로 안전성을 확인한다. | 계산 중간값이 어디까지 갈 수 있는지 범위를 계속 추적한다. |
| 5. Reachability and Bound Propagation | 입력 perturbation set이 출력공간에서 어디까지 도달 가능한지 계산한다. | 입력이 조금 바뀌어도 출력이 위험한 영역으로 가는지 확인한다. |
| 6. Precision vs Scalability | 정밀한 abstraction은 느리고, 거친 abstraction은 빠르지만 false alarm이나 inconclusive 결과가 늘 수 있다. | 자세히 검사하면 오래 걸리고, 대충 검사하면 안전한 것도 위험하다고 나올 수 있다. |
| 7. Verification Tools and Certificates | Solver, bound propagation, certificate, timeout, property specification 등 도구와 결과 보고 문제를 다룬다. | 검증 결과는 “무엇을, 어떤 조건에서, 얼마 동안 검사했는지” 함께 기록해야 믿을 수 있다. |
| 8. Limitations and Future Directions | 대형 모델 확장성, convolution/transformer 구조, floating-point error, specification 설계, certificate 표준화가 과제로 남는다. | 큰 AI 모델 전체를 완전히 증명하기는 어렵고, 검증 범위를 명확히 제한해야 한다. |
| 9. Conclusion | Abstraction 기반 검증은 DNN 안전성 주장에 유용하지만, 보장 범위와 한계를 명확히 보고해야 한다. | 검증은 강력하지만 “검증한 범위 안에서만” 의미가 있다. |
| 로컬 관련 PDF 메모 | 로컬 PDF는 Meng et al. formal verification perspective 관련 문헌으로 보이며, 공식 P01과 동일 문헌으로 인용하지 않는다. | PDF가 있다고 해서 공식 지정 논문과 동일하게 인용하면 안 된다. |

---

## 5. 핵심 이론 및 수식

> 아래 수식은 neural network verification과 abstraction 기반 robustness certificate를 W12 보고서에서 설명하기 위한 표준화된 표현이다. 수식은 GitHub, MS Word, PDF 변환 호환성을 위해 Markdown 표 밖의 LaTeX block math로 작성한다.

### 5.1 Robustness Property

입력 $x$ 주변의 perturbation ball 안에서 모델 예측이 변하지 않아야 한다는 명세다.

$$
\forall x' \in B_\epsilon(x),\quad f(x')=f(x)
$$

| 기호 | 의미 |
|---|---|
| $x$ | 기준 입력 |
| $x'$ | perturbation이 적용된 입력 |
| $B_\epsilon(x)$ | $x$ 주변 반경 $\epsilon$의 입력 영역 |
| $f$ | neural network classifier |

### 비전공자용 설명

이미지에 눈에 잘 안 보이는 작은 변화가 있어도 AI가 같은 답을 내야 한다는 조건이다.

### 보안적 의미

이 명세는 특정 입력과 perturbation 범위에 대한 보장이다. 모든 환경과 모든 공격에 대한 안전을 뜻하지 않는다.

---

### 5.2 Reachable Set Over-approximation

입력 집합 $X$가 신경망 $f$를 통과해 도달할 수 있는 출력 집합을 보수적으로 포함하는 집합 $\widehat{R}$을 계산한다.

$$
Reach(f,X)=\{f(x)\mid x\in X\}
$$

$$
Reach(f,X)\subseteq \widehat{R}
$$

| 기호 | 의미 |
|---|---|
| $X$ | 검증 대상 입력 집합 |
| $Reach(f,X)$ | 실제 도달 가능한 출력 집합 |
| $\widehat{R}$ | abstraction으로 계산한 over-approximation |

### 보안적 의미

$\widehat{R}$이 unsafe region과 겹치지 않으면 안전성을 증명할 수 있다. 하지만 $\widehat{R}$이 너무 크면 실제로는 안전해도 검증이 inconclusive가 될 수 있다.

---

### 5.3 Safety Property

출력이 unsafe region에 들어가지 않아야 한다.

$$
\widehat{R}\cap \mathcal{Y}_{unsafe}=\varnothing
$$

| 기호 | 의미 |
|---|---|
| $\mathcal{Y}_{unsafe}$ | 금지된 출력 영역 |
| $\widehat{R}$ | 검증 도구가 계산한 reachable output over-approximation |

### 보안적 의미

자율주행, 의료, 보안 자동대응에서는 특정 unsafe output을 명시하고 해당 영역에 도달하지 않음을 검증해야 한다.

---

### 5.4 Abstract Transformer

각 layer의 가능한 activation 집합을 추상 도메인에서 전파한다.

$$
A_{l+1}=T_l(A_l)
$$

| 기호 | 의미 |
|---|---|
| $A_l$ | layer $l$에서 가능한 activation의 abstract set |
| $T_l$ | layer $l$의 abstract transformer |

### 보안적 의미

Abstract transformer가 sound해야 한다. 즉 실제 가능한 activation을 빠뜨리면 안 된다. 빠뜨리면 잘못된 안전 증명이 될 수 있다.

---

### 5.5 Certified Robust Radius

특정 입력 $x$에 대해 검증된 최대 perturbation radius를 기록할 수 있다.

$$
r_{cert}(x)=\max\{\epsilon\mid \forall x'\in B_\epsilon(x),\; f(x')=f(x)\}
$$

### 보안적 의미

Certified radius는 특정 norm, 특정 입력, 특정 verifier, 특정 timeout 조건에서의 값이다. 다른 norm이나 더 큰 모델에는 일반화되지 않는다.

---

### 5.6 Verified Rate

검증 대상 sample 중 robustness property가 증명된 비율이다.

$$
VerifiedRate=\frac{N_{verified}}{N_{total}}
$$

### 보안적 의미

VerifiedRate가 높을수록 많은 sample에서 formal certificate가 나온 것이다. 단, timeout과 inconclusive case를 별도로 기록해야 한다.

---

### 5.7 Verification Cost

검증 비용은 시간과 메모리를 함께 고려해야 한다.

$$
VerificationCost=Time_{verify}+\lambda Memory_{verify}+\mu TimeoutRate
$$

### 보안적 의미

검증 방법이 너무 느리거나 timeout이 많으면 실무 적용이 어렵다. 따라서 accuracy나 robustness뿐 아니라 verification time도 평가해야 한다.

---

## 6. AI 원리 70% 관점 분석

| 원리 항목 | 설명 | W12/P01에서의 의미 |
|---|---|---|
| Neural Network Verification | 신경망이 명세를 만족하는지 수학적으로 확인 | W12 핵심 원리 |
| Abstraction | 복잡한 상태공간을 다루기 쉬운 추상공간으로 변환 | 확장성 확보 |
| Over-approximation | 실제 reachable set을 포함하는 큰 집합 계산 | soundness 확보 |
| Reachability | 입력 영역이 출력 영역에서 어디로 갈 수 있는지 계산 | safety property 검증 |
| Abstract Interpretation | layer별 activation bound를 추적 | formal verification 대표 방법 |
| Robustness Certificate | 특정 perturbation 범위에서 안전성 증명 | empirical test와 구분 |
| Precision-Scalability Trade-off | 정밀도와 계산비용의 균형 | verifier 선택 기준 |
| Verification Certificate | 검증 결과의 증거와 로그 | W15 재현성 연결 |

---

## 7. 보안 이슈 30% 관점 분석

| 보안 항목 | Verification 관점 해석 | 대표 평가 지표 |
|---|---|---|
| 기밀성 | 검증 대상 모델과 입력 bounds가 민감한 시스템 정보를 포함할 수 있음 | model/config access control |
| 무결성 | 잘못된 abstraction이나 unsound verifier는 허위 안전 증명을 만들 수 있음 | soundness check, certificate validation |
| 가용성 | 검증 비용과 timeout이 크면 운영 적용이 어렵다 | verification time, timeout rate |
| 프라이버시 | 검증 trace와 counterexample이 입력 데이터 정보를 포함할 수 있음 | trace anonymization |
| 안전성 | unsafe output region 도달 가능성을 사전에 확인 | unsafe reachability, verified rate |
| 책임성 | property, model hash, solver, timeout, certificate를 기록해야 감사 가능 | certificate log completeness |

---

## 8. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | DNN decision, safety property, input domain, reachable set, verification certificate, model hash, solver configuration |
| 공격자 목표 | 검증되지 않은 입력 영역에서 오분류 유도, certificate claim 오해 유도, verifier 한계 악용 |
| 공격자 능력 | perturbation 생성, out-of-scope input 사용, distribution shift 유발, verifier timeout/inconclusive 영역 탐색 |
| 공격 경로 | input perturbation → DNN inference → unsafe output 또는 misclassification → certificate scope 밖 claim 악용 |
| 방어자 능력 | formal specification, abstraction verification, adversarial testing, certificate logging, counterexample analysis, scope limitation |
| 제외 범위 | 실제 시스템 공격, adversarial example 생성 절차 제공, 실제 모델 취약점 악용 코드, 검증 범위 밖 안전 보장 주장 |

---

## 9. 평가방법 및 지표

| 평가축 | 지표 | 의미 | W12/P01 활용 |
|---|---|---|---|
| Formal robustness | certified radius, verified rate | 수학적으로 증명된 견고성 | certificate 평가 |
| Safety | unsafe reachability, property violation | unsafe output 도달 여부 | safety claim 검증 |
| Precision | false alarm, inconclusive rate | abstraction이 너무 거친지 | verifier 품질 평가 |
| Scalability | verification time, memory, timeout rate | 대형 모델 적용 가능성 | 실무 적용성 |
| Soundness | certificate validation, solver correctness | 허위 증명 방지 | 신뢰성 평가 |
| Empirical comparison | robust accuracy, adversarial test result | formal과 empirical 결과 비교 | P02/P04 연결 |
| Reproducibility | model hash, property, solver config, seed | 검증 재현 가능성 | W15 evidence chain |
| Bibliographic accuracy | official DOI match, local PDF mismatch flag | 참고문헌 정확성 | 기말논문 검증표 |

---

## 10. 재현성 체크리스트

| 항목 | 기록해야 할 내용 |
|---|---|
| Bibliographic status | 공식 DOI 논문과 로컬 PDF 동일 여부, mismatch flag |
| Model | architecture, dataset, model hash, training config |
| Property | robustness/safety/output bound 명세, norm, epsilon |
| Input domain | input bounds, perturbation set, preprocessing |
| Abstraction method | interval/polytope/zonotope/abstract interpretation 등 |
| Verifier | solver/tool name, version, parameters, timeout |
| Result | verified/violated/inconclusive, certified radius, verified rate |
| Cost | verification time, memory, timeout rate |
| Evidence | certificate log, counterexample trace, config file |
| 한계 | 검증한 property와 input domain 밖에는 안전을 보장하지 않음 |

---

## 11. 논문의 고유 기여

1. Neural network verification에서 abstraction method를 중심으로 formal safety evaluation을 체계화한다.
2. Over-approximation과 reachability analysis를 통해 특정 input region에 대한 안전성을 보수적으로 검증하는 틀을 제공한다.
3. Empirical adversarial testing과 formal verification certificate를 구분해야 함을 설명한다.
4. W12의 adversarial robustness, XAI robustness, Lipschitz robustness, fairness-robustness trade-off 논의를 formal verification 기준으로 연결한다.
5. W12 P01은 로컬 PDF mismatch가 있으므로, 참고문헌 검증표와 공식 DOI 우선 인용의 중요성을 보여주는 사례다.

---

## 12. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 로컬 PDF 불일치 | P01 로컬 PDF는 공식 DOI 논문과 다른 관련 formal verification survey다. | 공식 DOI 기준으로 인용하고 로컬 PDF는 보완 문헌으로 표시 |
| 확장성 문제 | 대형 DNN과 transformer 계열에서 verification cost가 커진다. | small model/toy property 또는 문헌 기반 분석으로 제한 |
| Abstraction precision 한계 | 너무 거친 over-approximation은 inconclusive 결과를 만든다. | inconclusive rate와 timeout rate 기록 |
| Certificate scope 제한 | 특정 input region과 property에 대해서만 보장한다. | limitation statement 필수화 |
| Floating-point·implementation 차이 | 실제 구현과 수학 모델 사이 차이가 있을 수 있다. | solver/tool version과 model hash 기록 |
| Empirical/formal 혼동 | adversarial test 통과가 formal guarantee는 아니다. | formal certificate와 empirical robust accuracy를 분리 보고 |

---

## 13. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | AI 보안 주장은 단순 테스트가 아니라 검증 가능한 명세와 certificate 범위로 제한해야 한다는 문제의식 |
| 2장 관련연구 | 공식 P01 DOI 논문을 abstraction-based neural network verification survey로 정리하고, 로컬 PDF mismatch는 검증표에 기록 |
| 3장 위협모형 | input domain, DNN decision, safety property, verifier, certificate 보호 자산 정의 |
| 4장 연구방법 | robustness property, reachable set, verified rate, verification time, timeout, certificate log 지표 설계 |
| 5장 분석 | empirical test vs formal certificate 비교표와 verifier evidence table 제시 |
| 6장 보안적 함의 | formal verification scope, abstraction 한계, certificate audit, 참고문헌 검증 필요성 해석 |

---

## 14. 기말논문 연결 3문장

1. W12에서 기말논문에 반영할 개념: Neural network verification은 특정 input domain과 safety property에 대해 reachable set이 unsafe region에 들어가지 않음을 증명하는 과정이며, abstraction은 이를 계산 가능하게 만드는 핵심 방법이다.
2. W12에서 기말논문에 반영할 표·그림·실험: robustness property 수식, reachable set over-approximation 그림, verified rate·verification time·timeout rate 평가표, 공식 DOI/로컬 PDF mismatch 검증표를 반영한다.
3. W12가 LLM/RAG 보안 감사 프레임워크와 연결되는 지점: AI 시스템의 안전성 주장을 할 때 model hash, property specification, verification certificate, counterexample trace, evidence log를 W14/W15 evidence chain에 포함해야 한다.

---

## 15. 최종 판단

P01은 W12의 formal verification 핵심 문헌이다. 다만 W12 `paper_list.md` 기준 로컬 PDF는 공식 DOI 논문과 다른 관련 보조 문헌으로 기록되어 있으므로, 기말논문 참고문헌에는 공식 DOI 논문인 Boudardara et al.의 `A Review of Abstraction Methods Toward Verifying Neural Networks`를 우선 사용해야 한다. 로컬 PDF는 Meng et al. formal verification perspective 관련 보완 문헌으로만 제한해 활용하는 것이 적절하다.

---

## 16. 변환 호환성 메모

```bash
pandoc P01_summary.md -o P01_summary.docx
pandoc P01_summary.md -o P01_summary.pdf --pdf-engine=xelatex
```
