# P01 Summary

## A Critical Review on the Use (and Misuse) of Differential Privacy in Machine Learning — Alberto Blanco-Justicia et al., ACM Computing Surveys, 2023

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W11 차등프라이버시(Differential Privacy) & Membership Inference |
| 논문명 | A Critical Review on the Use (and Misuse) of Differential Privacy in Machine Learning |
| 저자 | Alberto Blanco-Justicia, David Sanchez, Josep Domingo-Ferrer, Krishnamurty Muralidhar |
| 공식 출판 정보 | ACM Computing Surveys, Vol. 55, No. 8, pp. 1–16, online 2022-12-23, print 2023-08-31 |
| DOI | https://doi.org/10.1145/3547139 |
| 보조 URL | https://arxiv.org/abs/2206.04621 |
| 로컬 PDF | `01_papers/pdf/01_Blanco_Justicia_et_al_2022_Differential_Privacy_Critical_Review.pdf` |
| 검증 상태 | W11 `paper_list.md` 기준 공식 DOI 확인. 로컬 PDF는 arXiv v2이므로 ACM 최종본과 세부 pagination·표기 차이 메모 유지 |
| PDF 확인 메모 | repo의 PDF 폴더에 해당 PDF blob이 존재함을 확인했다. 요약은 로컬 PDF 경로와 W11 `paper_list.md`의 공식 DOI 메타데이터 기준으로 보완했다. |
| 핵심 근거 사용 가능 여부 | 가능. W11에서 DP의 정의, epsilon/delta 해석, privacy guarantee 오용, threat model 정합성, privacy-utility trade-off를 설명하는 핵심 기준 문헌으로 사용 |

---

## 1. 한 문장 요약

이 논문은 machine learning에서 differential privacy가 실제보다 과장되거나 잘못 적용되는 사례를 **DP 정의, neighboring dataset, randomized mechanism, epsilon/delta 해석, composition, privacy budget, threat model, implementation assumption, utility loss, empirical attack evaluation, misleading privacy claims** 관점에서 비판적으로 검토하며, W11에서 “DP를 적용했다”는 주장과 “실제로 개인정보 위험을 줄였다”는 주장을 엄밀히 구분하기 위한 기준 문헌이다.

---

## 2. 핵심 연구문제

> Differential privacy는 수학적으로 명확한 privacy guarantee를 제공하지만, ML 논문과 시스템에서는 epsilon 해석, threat model, composition, implementation, utility trade-off가 불명확하게 보고되어 privacy claim이 과장될 수 있다. 따라서 DP가 무엇을 보장하고 무엇을 보장하지 않는지 어떻게 검증·보고해야 하는가?

| 번호 | 연구질문 |
|---|---|
| RQ1 | Differential privacy는 neighboring dataset에 대해 어떤 확률적 indistinguishability를 보장하며, 이 보장은 membership inference·attribute inference·reconstruction과 어떤 관계를 갖는가? |
| RQ2 | Epsilon과 delta는 어떻게 해석해야 하며, “작은 epsilon이면 무조건 안전하다” 또는 “DP를 썼으니 완전 익명이다” 같은 오용은 어디서 발생하는가? |
| RQ3 | ML에서 DP를 적용할 때 utility drop, privacy budget, composition, clipping, noise mechanism, accountant를 어떻게 명시해야 하는가? |
| RQ4 | DP 보장과 empirical privacy attack 평가를 어떻게 구분해 보고해야 하며, membership inference 실험은 DP claim을 어떻게 보완하는가? |
| RQ5 | 기말논문에서 privacy guarantee를 과장하지 않으려면 threat model, scope, excluded guarantee, implementation assumption을 어떻게 문장화해야 하는가? |

---

## 3. 논문의 핵심 기여

| 기여 | 설명 | W11 연결 |
|---|---|---|
| DP 오용 비판 | ML에서 DP가 marketing label처럼 사용되거나 보장 범위가 과장되는 문제를 지적 | W11의 핵심 문제의식 |
| 수학적 정의와 해석 분리 | DP의 formal guarantee와 실무적 해석 사이의 간극을 설명 | epsilon/delta 해석 기준 |
| Threat model 정합성 강조 | DP가 보호하는 공격과 보호하지 않는 공격을 구분해야 함을 강조 | MIA·attribute inference 평가 연결 |
| Privacy-utility trade-off 강조 | DP 적용 시 utility loss와 privacy budget을 함께 보고해야 함을 제시 | W11 평가 지표 설계 |
| 보고 기준 제공 | epsilon, delta, mechanism, composition, implementation assumption을 명확히 기록해야 함 | 기말논문 재현성·감사 기준 |

---

## 4. 목차별 핵심 개괄

| 목차 | 핵심 내용 | 비전공자용 이해 |
|---|---|---|
| 1. Introduction | DP는 개인정보 보호를 위한 강력한 수학적 프레임워크이지만, ML 분야에서 보장 범위를 잘못 이해하거나 과장하는 경우가 많다. | “DP를 썼다”는 말만으로 개인정보가 완전히 안전하다고 말할 수 없다. |
| 2. Differential Privacy Background | Neighboring dataset, randomized mechanism, epsilon, delta, privacy budget, composition 등 DP 기본 개념을 설명한다. | 한 사람의 데이터가 들어가거나 빠져도 결과가 크게 달라 보이지 않게 만드는 원리다. |
| 3. DP in Machine Learning | DP-SGD, noise addition, clipping, private model training, private query release 등 ML 적용 방식을 정리한다. | 학습 중 gradient를 잘라내고 noise를 넣어 개별 데이터의 흔적을 줄인다. |
| 4. Misuse and Misinterpretation | epsilon을 임의로 선택하거나, delta를 설명하지 않거나, composition을 무시하거나, utility loss를 보고하지 않는 문제를 비판한다. | 개인정보 보호 강도를 제대로 설명하지 않고 “DP 적용”이라고만 쓰면 오해를 만든다. |
| 5. Threat Model Issues | DP가 어떤 공격자를 가정하는지, membership inference와 reconstruction attack을 얼마나 줄이는지 명확히 해야 한다. | 공격자가 무엇을 알고 무엇을 볼 수 있는지 정하지 않으면 보호 주장이 애매하다. |
| 6. Utility and Practical Limits | 강한 DP는 성능 저하를 만들 수 있으며, 실제 ML pipeline의 전처리·후처리·로그도 privacy risk가 될 수 있다. | 개인정보를 더 잘 보호하려면 모델 성능이 떨어질 수 있고, 학습 밖의 로그도 관리해야 한다. |
| 7. Recommendations | DP 논문·시스템은 epsilon/delta, mechanism, accountant, threat model, utility drop, composition, implementation scope를 투명하게 보고해야 한다. | 개인정보 보호 주장을 하려면 수치와 조건, 한계를 같이 적어야 한다. |
| 8. Conclusion | DP는 유용하지만 오용되면 잘못된 안전감을 주므로, formal guarantee와 empirical evaluation을 분리해 보고해야 한다. | DP는 마법이 아니라 조건부 수학 보장이다. 조건과 한계를 같이 써야 한다. |

---

## 5. 핵심 이론 및 수식

> 아래 수식은 Differential Privacy와 W11 privacy evaluation을 설명하기 위한 표준화된 표현이다. 수식은 GitHub, MS Word, PDF 변환 호환성을 위해 Markdown 표 밖의 LaTeX block math로 작성한다.

### 5.1 Differential Privacy 정의

Randomized mechanism $M$이 모든 인접 데이터셋 $D,D'$와 모든 출력 집합 $S$에 대해 다음을 만족하면 $(\epsilon,\delta)$-DP라고 한다.

$$
\Pr[M(D)\in S]\leq e^{\epsilon}\Pr[M(D')\in S]+\delta
$$

| 기호 | 의미 |
|---|---|
| $D,D'$ | 한 개 record만 다른 neighboring dataset |
| $M$ | randomized mechanism |
| $S$ | 가능한 출력 집합 |
| $\epsilon$ | privacy budget. 작을수록 강한 보호 |
| $\delta$ | DP 보장이 실패할 수 있는 작은 확률 |

### 비전공자용 설명

한 사람의 데이터가 들어가든 빠지든 결과가 거의 비슷하게 나오도록 만드는 것이 DP의 핵심이다.

### 보안적 의미

DP는 특정 개인의 데이터 포함 여부를 출력으로부터 구분하기 어렵게 만든다. 그러나 epsilon/delta, mechanism, composition, implementation scope가 명확하지 않으면 실제 보호 수준을 판단할 수 없다.

---

### 5.2 Pure DP와 Approximate DP

Pure DP는 $\delta=0$인 경우다.

$$
\Pr[M(D)\in S]\leq e^{\epsilon}\Pr[M(D')\in S]
$$

Approximate DP는 작은 실패확률 $\delta$를 허용한다.

$$
(\epsilon,\delta)\text{-DP},\qquad \delta>0
$$

### 보안적 의미

$\delta$를 작게 설정하지 않으면 드문 실패 사건이 실제 개인정보 위험으로 이어질 수 있다. 따라서 delta 값을 생략하면 DP claim이 불완전하다.

---

### 5.3 Privacy Loss

특정 출력 $o$가 관찰되었을 때 두 neighboring dataset을 구분하는 정도를 privacy loss로 표현할 수 있다.

$$
L(o)=\log\frac{\Pr[M(D)=o]}{\Pr[M(D')=o]}
$$

### 보안적 의미

Privacy loss가 클수록 출력이 특정 개인의 포함 여부에 더 민감하다는 뜻이다. DP는 이 loss를 epsilon으로 제한하려는 접근이다.

---

### 5.4 Composition of Privacy Budget

여러 번의 DP mechanism을 실행하면 privacy budget이 누적된다.

$$
\epsilon_{total}\approx\sum_{i=1}^{T}\epsilon_i
$$

더 정교한 accountant를 사용하면 tighter bound를 계산할 수 있지만, 핵심은 privacy cost가 반복 질의·반복 학습에서 누적된다는 점이다.

### 보안적 의미

한 번의 DP 질의는 안전해 보여도 여러 번 반복하면 누적 privacy loss가 커진다. ML 학습에서는 epoch, gradient step, hyperparameter search까지 composition에 영향을 줄 수 있다.

---

### 5.5 Privacy-Utility Trade-off

DP는 noise를 통해 privacy를 높이지만 utility를 낮출 수 있다.

$$
UtilityDrop=Acc_{non\text{-}private}-Acc_{DP}
$$

| 기호 | 의미 |
|---|---|
| $Acc_{non\text{-}private}$ | DP 없이 학습한 baseline accuracy |
| $Acc_{DP}$ | DP 적용 후 accuracy |

### 보안적 의미

DP를 적용했다면 privacy budget뿐 아니라 성능 손실도 함께 보고해야 한다. utility loss를 숨기면 실무 적용 가능성을 판단하기 어렵다.

---

### 5.6 Membership Inference Advantage

DP가 empirical privacy risk를 얼마나 낮추는지 membership inference advantage로 보완 평가할 수 있다.

$$
Adv_{MI}=P[A(z)=1\mid z\in D_{train}]-P[A(z)=1\mid z\notin D_{train}]
$$

| 기호 | 의미 |
|---|---|
| $A(z)$ | sample $z$가 training data에 포함되었다고 판단하는 공격자 |
| $D_{train}$ | 학습 데이터 |

### 보안적 의미

DP는 formal guarantee이고 MIA 실험은 empirical leakage evaluation이다. 두 결과를 혼동하지 말고 함께 보고해야 한다.

---

### 5.7 DP Claim Completeness Score

DP claim이 필요한 정보를 얼마나 포함하는지 평가하기 위한 보고 지표다.

$$
DPClaimCompleteness=\frac{|E_{reported}\cap E_{required}|}{|E_{required}|}
$$

| 기호 | 의미 |
|---|---|
| $E_{reported}$ | 논문·보고서에 실제로 기록된 DP 근거 항목 |
| $E_{required}$ | epsilon, delta, mechanism, accountant, clipping, noise, threat model, utility 등 필수 항목 |

### 보안적 의미

“DP 적용”이라고만 쓰면 불충분하다. 어떤 mechanism을 어떤 budget으로, 어떤 데이터와 위협모형에 적용했는지 기록해야 한다.

---

## 6. AI 원리 70% 관점 분석

| 원리 항목 | 설명 | W11/P01에서의 의미 |
|---|---|---|
| Differential Privacy | neighboring dataset의 출력 분포를 비슷하게 유지 | privacy guarantee의 핵심 정의 |
| Randomized Mechanism | noise를 포함한 확률적 알고리즘 | deterministic ML output의 privacy risk 완화 |
| Epsilon | privacy loss 상한 | 해석 오용의 핵심 |
| Delta | DP 실패확률 | 생략하면 보장 범위가 불명확 |
| Composition | 반복 실행 시 privacy budget 누적 | 학습 epoch·질의 반복과 연결 |
| Utility Trade-off | privacy 강화와 모델 성능 사이 균형 | DP 실용성 평가 |
| Threat Model | 공격자 지식과 관찰 가능한 output 정의 | privacy claim 정합성 판단 |
| Empirical Attack Evaluation | MIA 등으로 실제 leakage를 실험적으로 측정 | W11 P04/P05와 연결 |

---

## 7. 보안 이슈 30% 관점 분석

| 보안 항목 | DP 오용 관점 해석 | 대표 평가 지표 |
|---|---|---|
| 기밀성 | 개별 record membership과 민감 속성 보호 | epsilon, delta, MI advantage |
| 무결성 | 잘못된 DP claim이 privacy 보장 수준을 왜곡 | DPClaimCompleteness, audit finding |
| 가용성 | 강한 DP noise가 모델 utility를 크게 낮출 수 있음 | UtilityDrop, convergence delay |
| 프라이버시 | DP scope 밖의 로그·전처리·후처리에서 leakage 가능 | pipeline leakage check |
| 안전성 | privacy claim 과장은 의료·금융 등 민감 domain에서 잘못된 배포 판단을 유도 | domain risk, compliance evidence |
| 책임성 | epsilon/delta/mechanism/accountant를 기록해야 감사 가능 | DP mechanism audit, reproducibility evidence |

---

## 8. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | training data, individual record membership, sensitive attribute, model output, query log, DP configuration, privacy accountant log |
| 공격자 목표 | membership inference, attribute inference, reconstruction, repeated query exploitation, privacy claim confusion exploitation |
| 공격자 능력 | model output 관찰, query 반복, auxiliary data 보유, public statistics 이용, training distribution 일부 지식 보유 |
| 공격 경로 | data preprocessing → DP mechanism/training → model release/query → output/log analysis → privacy inference |
| 방어자 능력 | DP mechanism 설계, epsilon/delta 관리, clipping/noise/accountant 기록, empirical MIA 평가, pipeline audit |
| 제외 범위 | 실제 개인정보 기반 공격 실험, 실제 민감 데이터 재식별, 공격 코드 제공, privacy guarantee 과장 표현 |

---

## 9. 평가방법 및 지표

| 평가축 | 지표 | 의미 | W11/P01 활용 |
|---|---|---|---|
| Formal privacy | epsilon, delta | 수학적 DP 보장 강도 | DP claim의 핵심 |
| Budget accounting | epsilon_total, accountant log | 반복 학습·질의로 인한 누적 privacy cost | composition 평가 |
| Utility | UtilityDrop, accuracy/loss | DP 적용 후 모델 성능 손실 | privacy-utility trade-off |
| Empirical leakage | MI advantage, attack accuracy | 실제 membership leakage 위험 | W11 P04 연결 |
| Mechanism quality | clipping norm, noise multiplier | DP-SGD 또는 mechanism 설정 | 재현성 평가 |
| Claim completeness | DPClaimCompleteness | DP 보고의 충분성 | 논문 검수 기준 |
| Pipeline risk | pre/post-processing leakage check | DP scope 밖 leakage 여부 | 시스템 감사 |
| Compliance | consent, purpose, retention evidence | 정책·감사 증거 | W14/W15 연결 |

---

## 10. 재현성 체크리스트

| 항목 | 기록해야 할 내용 |
|---|---|
| DP definition | pure DP인지 approximate DP인지, neighboring relation 정의 |
| Privacy budget | epsilon, delta, epsilon_total, accountant 방식 |
| Mechanism | Laplace/Gaussian mechanism, DP-SGD, randomized response 등 |
| DP-SGD setting | clipping norm, noise multiplier, batch size, sampling rate, epoch 수 |
| Composition | training step, repeated query, hyperparameter search 포함 여부 |
| Utility | non-private baseline, DP model accuracy/loss, UtilityDrop |
| Threat model | attacker knowledge, observable output, black-box/white-box 조건 |
| Empirical attack | MIA/attribute inference/reconstruction 평가 여부와 지표 |
| Pipeline audit | preprocessing, logging, post-processing, model release scope |
| 한계 | DP 보장이 적용되는 mechanism과 데이터 범위 밖에는 보장하지 않음 |

---

## 11. 논문의 고유 기여

1. ML에서 DP가 잘못 사용되거나 과장되는 문제를 비판적으로 정리한다.
2. DP의 formal guarantee와 실무적 privacy claim을 분리해 이해해야 함을 강조한다.
3. Epsilon/delta, composition, utility loss, mechanism, threat model을 명확히 보고해야 함을 제시한다.
4. W11에서 membership inference와 DP defense를 연결할 때 “DP 적용 여부”보다 “보장 범위와 위협모형 정합성”이 중요하다는 기준을 제공한다.
5. 기말논문에서 privacy guarantee 문장을 과장하지 않게 만드는 검수 기준으로 사용할 수 있다.

---

## 12. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| DP 해석 난이도 | epsilon 값의 실질적 의미를 비전문가가 이해하기 어렵다. | epsilon/delta 설명표와 한계 문장 포함 |
| Utility trade-off | 강한 DP는 모델 성능 저하를 만들 수 있다. | UtilityDrop과 baseline 병기 |
| Composition 복잡성 | 학습·질의 반복에서 privacy budget이 누적된다. | accountant log와 epsilon_total 기록 |
| Pipeline leakage | DP mechanism 밖의 전처리·로그·후처리에서 leakage 가능 | pipeline audit checklist 포함 |
| Empirical attack과 formal guarantee 혼동 | MIA 실험 결과가 DP 보장을 대체하지 않는다. | formal/empirical 지표 분리 |
| Privacy claim 과장 | “DP 적용”이라는 표현만으로 보호 수준을 과장할 수 있다. | DPClaimCompleteness와 limitation statement 작성 |

---

## 13. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | 개인정보 보호 AI에서 DP claim이 과장될 수 있으므로 formal guarantee와 empirical leakage를 분리해야 한다는 문제의식 |
| 2장 관련연구 | DP critical review를 W11 privacy 기준 문헌으로 정리 |
| 3장 위협모형 | training record, membership, sensitive attribute, model output, query log 보호 자산 정의 |
| 4장 연구방법 | epsilon, delta, UtilityDrop, MI advantage, DPClaimCompleteness, pipeline leakage check 지표 설계 |
| 5장 분석 | DP claim checklist와 privacy-utility trade-off 표 제시 |
| 6장 보안적 함의 | DP 적용 범위, composition, utility loss, empirical attack evaluation, 감사 로그 필요성 해석 |

---

## 14. 기말논문 연결 3문장

1. W11에서 기말논문에 반영할 개념: Differential privacy는 강력한 수학적 보호 개념이지만, epsilon/delta, mechanism, composition, threat model을 명확히 제시하지 않으면 privacy guarantee가 과장될 수 있다.
2. W11에서 기말논문에 반영할 표·그림·실험: DP 정의식, privacy-utility trade-off, DP claim completeness checklist, formal guarantee와 membership inference 실험 지표 분리표를 반영한다.
3. W11이 LLM/RAG 보안 감사 프레임워크와 연결되는 지점: RAG/LLM 로그·학습 데이터·사용자 질의 보호를 주장할 때도 DP 적용 범위, query logging, accountant, leakage evaluation, compliance evidence를 W14/W15 evidence chain에 포함해야 한다.

---

## 15. 최종 판단

P01은 W11의 DP 개념·오용 방지 핵심 문헌이다. P02/P03이 DP deep learning 적용과 최신 체계를 제공하고 P04/P05가 membership inference 공격·방어를 다룬다면, P01은 그 모든 논의의 전제가 되는 “privacy guarantee를 어떻게 정확히 말할 것인가”를 제시한다. 따라서 W11 기말논문 연결에서는 P01을 **DP 정의, epsilon/delta 해석, privacy-utility trade-off, DP claim audit의 중심 근거 문헌**으로 사용하는 것이 적절하다.

---

## 16. 변환 호환성 메모

```bash
pandoc P01_summary.md -o P01_summary.docx
pandoc P01_summary.md -o P01_summary.pdf --pdf-engine=xelatex
```
