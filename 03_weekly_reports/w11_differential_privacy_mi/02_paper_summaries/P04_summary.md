# P04 Summary

## Membership Inference Attacks on Machine Learning: A Survey — Hongsheng Hu et al., ACM Computing Surveys, 2022

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W11 차등프라이버시(Differential Privacy) & Membership Inference |
| 논문명 | Membership Inference Attacks on Machine Learning: A Survey |
| 저자 | Hongsheng Hu, Zoran Salcic, Lichao Sun, Gillian Dobbie, Philip S. Yu, Xuyun Zhang |
| 공식 출판 정보 | ACM Computing Surveys, Vol. 54, No. 11s, pp. 1–37, online 2022-09-09, print 2022-01-31 |
| DOI | https://doi.org/10.1145/3523273 |
| 보조 URL | https://arxiv.org/abs/2103.07853 |
| 로컬 PDF | `01_papers/pdf/04_Hu_et_al_2022_Membership_Inference_Attacks_Survey.pdf` |
| 검증 상태 | W11 `paper_list.md` 기준 공식 DOI 확인. 로컬 PDF는 arXiv/ACM preprint 성격이므로 ACM 최종본과 세부 pagination·표기 차이 메모 유지 |
| PDF 확인 메모 | repo의 PDF 폴더에 해당 PDF blob이 존재함을 확인했다. 요약은 로컬 PDF 경로와 W11 `paper_list.md`의 공식 DOI 메타데이터 기준으로 보완했다. |
| 핵심 근거 사용 가능 여부 | 가능. W11에서 membership inference attack의 위협모형, black-box/white-box 접근, shadow model, confidence leakage, overfitting, attack metric, defense evaluation을 설명하는 핵심 공격 문헌으로 사용 |

---

## 1. 한 문장 요약

이 논문은 machine learning 모델이 특정 record를 학습 데이터에 포함했는지 추론하는 membership inference attack을 **black-box query, white-box access, prediction confidence, loss gap, overfitting, shadow model, attack classifier, model output leakage, attack advantage, AUC, defense mechanism, evaluation protocol** 관점에서 체계화하며, W11에서 privacy risk를 단순 데이터 유출이 아니라 **모델 출력과 학습 흔적을 통한 추론 위험**으로 정의하는 핵심 공격 survey 문헌이다.

---

## 2. 핵심 연구문제

> 학습 데이터가 직접 공개되지 않아도, 공격자는 모델 출력, confidence score, loss, gradient, parameter 접근, shadow data를 이용해 특정 sample이 training set에 포함되었는지를 추론할 수 있다. 이러한 membership inference risk를 어떤 threat model과 metric으로 평가하고, DP·regularization·output restriction 같은 방어 효과를 어떻게 검증할 것인가?

| 번호 | 연구질문 |
|---|---|
| RQ1 | 공격자는 black-box model output만 보고도 특정 record의 training membership을 어떻게 추론할 수 있는가? |
| RQ2 | Prediction confidence, entropy, loss gap, overfitting, generalization gap은 membership leakage와 어떤 관계를 갖는가? |
| RQ3 | Black-box, white-box, label-only, transfer/shadow-model 기반 MIA는 공격자 지식과 접근권한 측면에서 어떻게 다른가? |
| RQ4 | Differential privacy, regularization, model calibration, output restriction, confidence masking, auditing은 MIA 방어에 어떤 효과와 한계를 갖는가? |
| RQ5 | 기말논문에서 DP 방어 효과를 주장하려면 MI advantage, attack accuracy, AUC, utility drop을 어떻게 함께 보고해야 하는가? |

---

## 3. 논문의 핵심 기여

| 기여 | 설명 | W11 연결 |
|---|---|---|
| MIA taxonomy | Membership inference attack을 공격자 접근권한, 지식, 모델 유형, 출력 정보 기준으로 분류 | W11 핵심 공격 taxonomy |
| Leakage 원인 정리 | Overfitting, confidence gap, loss distribution 차이, generalization gap이 membership leakage와 연결됨을 설명 | DP/regularization 방어 근거 |
| Threat model 체계화 | Black-box, white-box, shadow model, auxiliary data 기반 공격 조건을 구분 | W11 위협모형 설계 |
| Evaluation metric 정리 | attack accuracy, advantage, AUC, precision/recall, FPR 등 평가 지표를 정리 | 기말논문 평가표 근거 |
| Defense 비교 | DP, output perturbation/restriction, regularization, model compression, auditing 등의 방어와 trade-off 정리 | W11 P01/P02/P05 연결 |

---

## 4. 목차별 핵심 개괄

| 목차 | 핵심 내용 | 비전공자용 이해 |
|---|---|---|
| 1. Introduction | ML 모델은 학습 데이터의 흔적을 출력에 반영할 수 있으며, 공격자는 특정 sample이 학습에 포함되었는지 추론할 수 있다. | 모델이 직접 데이터를 보여주지 않아도 “이 사람 데이터가 학습에 있었는지”를 추정할 수 있다. |
| 2. Background | Machine learning, training/test data, overfitting, confidence score, privacy leakage, threat model의 기본 개념을 설명한다. | 모델이 학습 데이터를 너무 잘 외우면, 학습한 데이터와 안 한 데이터를 다르게 대할 수 있다. |
| 3. Membership Inference Attack Taxonomy | Black-box, white-box, shadow model, label-only, confidence-based, loss-based, transfer-based MIA를 분류한다. | 공격자는 모델 내부를 몰라도 출력 확률만 보고 추론할 수 있고, 내부 정보를 알면 더 강한 공격이 가능하다. |
| 4. Attack Pipeline | Target model query, feature extraction, shadow model training, attack classifier, membership decision의 일반 흐름을 정리한다. | 비슷한 모델을 만들어 비교하거나, 출력의 확신도를 보고 학습 포함 여부를 판단한다. |
| 5. Factors Affecting MIA | Overfitting, model complexity, dataset size, class imbalance, confidence calibration, output granularity가 공격 성공에 영향을 준다. | 모델이 과하게 자신만만하거나 학습 데이터를 외울수록 공격이 쉬워진다. |
| 6. Defense Mechanisms | DP, regularization, dropout, confidence masking, output restriction, adversarial regularization, auditing을 방어로 정리한다. | 출력 정보를 줄이거나 noise를 넣거나 모델이 데이터를 덜 외우게 만들어 공격을 어렵게 한다. |
| 7. Evaluation Protocol | Attack accuracy, MI advantage, AUC, precision/recall, utility drop을 함께 보고해야 함을 강조한다. | 방어가 개인정보 위험을 줄였는지 보려면 공격 성공률과 모델 성능을 같이 봐야 한다. |
| 8. Challenges and Future Directions | 현실적 threat model, adaptive attacker, foundation model, federated learning, generative model MIA, standardized benchmark가 과제로 남는다. | 실제 환경의 공격자는 더 다양하므로 표준화된 평가가 필요하다. |
| 9. Conclusion | MIA는 ML privacy의 대표 공격이며, DP와 empirical attack evaluation을 결합해 평가해야 한다. | 개인정보 보호 모델이라고 주장하려면 MIA 실험으로 실제 위험도 확인해야 한다. |

---

## 5. 핵심 이론 및 수식

> 아래 수식은 membership inference attack과 W11 privacy risk evaluation을 설명하기 위한 표준화된 표현이다. 실제 공격 코드나 절차 제공이 아니라 평가 지표와 방어 검증 구조를 설명하기 위한 것이다.

### 5.1 Membership Inference Advantage

공격자가 training member와 non-member를 구분하는 능력을 측정한다.

$$
Adv_{MI}=\Pr[A(z)=1\mid z\in D_{train}]-\Pr[A(z)=1\mid z\notin D_{train}]
$$

| 기호 | 의미 |
|---|---|
| $A(z)$ | sample $z$가 학습 데이터에 포함되었다고 판단하는 공격자 |
| $D_{train}$ | target model의 학습 데이터 |
| $Adv_{MI}$ | member와 non-member 구분 이득 |

### 비전공자용 설명

공격자가 “이 데이터가 학습에 들어갔는가?”를 맞히는 능력이 우연보다 얼마나 나은지 보는 지표다.

### 보안적 의미

모델 정확도가 높아도 MI advantage가 높으면 privacy leakage가 존재한다. 따라서 utility와 privacy risk를 분리해서 보고해야 한다.

---

### 5.2 Attack Accuracy

Membership inference 이진분류 정확도다.

$$
Acc_{MI}=\frac{TP+TN}{TP+TN+FP+FN}
$$

| 기호 | 의미 |
|---|---|
| $TP$ | member를 member로 맞힌 경우 |
| $TN$ | non-member를 non-member로 맞힌 경우 |
| $FP$ | non-member를 member로 잘못 판단한 경우 |
| $FN$ | member를 non-member로 놓친 경우 |

### 보안적 의미

Class imbalance가 있으면 accuracy만으로 부족할 수 있으므로 AUC, precision, recall, FPR도 함께 본다.

---

### 5.3 Loss Gap 기반 Leakage

학습 데이터는 일반적으로 non-member보다 낮은 loss를 보일 수 있다.

$$
LossGap=\mathbb{E}_{z\notin D_{train}}[\ell(f_\theta,z)]-\mathbb{E}_{z\in D_{train}}[\ell(f_\theta,z)]
$$

### 보안적 의미

LossGap이 클수록 member와 non-member가 모델 관점에서 더 잘 구분될 수 있다. Overfitting은 MIA 위험을 높인다.

---

### 5.4 Confidence Gap

모델이 member sample에 대해 더 높은 confidence를 보이는 경우 leakage가 발생한다.

$$
ConfGap=\mathbb{E}_{z\in D_{train}}[\max_y p_\theta(y\mid z)]-\mathbb{E}_{z\notin D_{train}}[\max_y p_\theta(y\mid z)]
$$

### 보안적 의미

API가 confidence score나 full probability vector를 제공하면 MIA 위험이 커질 수 있다. Output restriction과 confidence masking은 이를 줄이는 방어다.

---

### 5.5 Generalization Gap

Training accuracy와 test accuracy 차이는 overfitting과 MIA 위험의 간접 신호다.

$$
GenGap=Acc_{train}-Acc_{test}
$$

### 보안적 의미

Generalization gap이 크면 모델이 학습 데이터에 과적합했을 가능성이 있고, 이는 membership inference risk를 높일 수 있다.

---

### 5.6 DP Defense Gain

DP 또는 방어 적용 전후 MI advantage 감소량을 측정한다.

$$
DefenseGain=Adv_{MI}^{baseline}-Adv_{MI}^{defense}
$$

### 보안적 의미

방어가 실제 privacy risk를 줄였는지 보려면 MI advantage 감소를 측정해야 한다. 단, defense gain만 보고하면 안 되고 utility loss도 함께 봐야 한다.

---

### 5.7 Privacy-Utility Joint Score

방어 후 privacy risk 감소와 utility 손실을 함께 고려한다.

$$
JointScore=DefenseGain-\lambda UtilityDrop-\mu LatencyIncrease
$$

### 보안적 의미

MIA를 줄이는 방어가 모델 성능을 크게 떨어뜨리거나 지연을 크게 늘리면 실무 적용성이 낮다. privacy와 utility를 동시에 평가해야 한다.

---

## 6. AI 원리 70% 관점 분석

| 원리 항목 | 설명 | W11/P04에서의 의미 |
|---|---|---|
| Supervised ML Output | 모델이 class probability, confidence, label을 출력 | MIA의 관찰 대상 |
| Overfitting | 학습 데이터를 과도하게 기억 | membership leakage 주요 원인 |
| Shadow Model | target model과 유사한 모델로 attack classifier 학습 | black-box MIA 설명 |
| Attack Classifier | member/non-member를 분류 | MIA 평가 모델 |
| Confidence Score | 출력 확률의 확신도 | leakage feature |
| White-box Access | gradient/parameter/loss 접근 | 더 강한 threat model |
| Generalization Gap | train-test 성능 차이 | MIA 위험 간접 지표 |
| Defense Mechanism | DP, regularization, output restriction | MIA 위험 완화 |

---

## 7. 보안 이슈 30% 관점 분석

| 보안 항목 | MIA 관점 해석 | 대표 평가 지표 |
|---|---|---|
| 기밀성 | 특정 record의 training membership이 노출될 수 있음 | MI advantage, attack accuracy, AUC |
| 무결성 | 방어가 모델 decision boundary와 calibration을 왜곡할 수 있음 | UtilityDrop, calibration error |
| 가용성 | 출력 제한·방어가 API 유용성과 서비스 품질을 낮출 수 있음 | response utility, latency |
| 프라이버시 | membership 자체가 민감정보인 의료·금융 domain에서 위험 | MI success, domain sensitivity |
| 안전성 | privacy leakage가 개인 피해, 차별, 재식별 위험으로 이어질 수 있음 | risk severity, subgroup MI risk |
| 책임성 | 모델 배포 전 MIA audit와 defense evidence가 필요 | audit completeness, experiment trace |

---

## 8. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | training data membership, sensitive record, confidence score, model output, loss, gradient, model parameter, query log |
| 공격자 목표 | 특정 record가 학습 데이터에 포함되었는지 추론, 민감 집단 또는 특정 개인의 participation 유추 |
| 공격자 능력 | black-box query, confidence score 관찰, label-only output 관찰, shadow data 보유, white-box gradient/parameter 접근 |
| 공격 경로 | target sample/query → model output/loss/confidence 관찰 → membership score 계산 → member/non-member decision |
| 방어자 능력 | DP training, regularization, calibration, output restriction, confidence masking, query throttling, MIA audit |
| 제외 범위 | 실제 개인정보 대상 membership 추론, 실제 민감 데이터 재식별, 공격 코드 제공, 무단 모델 질의 자동화 |

---

## 9. 평가방법 및 지표

| 평가축 | 지표 | 의미 | W11/P04 활용 |
|---|---|---|---|
| 공격 성공 | Acc_MI, Adv_MI, AUC | membership 추론 성능 | MIA 핵심 평가 |
| 오류 유형 | precision, recall, FPR, FNR | member/non-member 판단 오류 | balanced evaluation |
| Leakage 원인 | GenGap, LossGap, ConfGap | overfitting·confidence leakage | 위험 원인 분석 |
| 방어 효과 | DefenseGain, MI reduction | 방어 전후 위험 감소 | DP/regularization 평가 |
| Utility | clean accuracy, UtilityDrop | 방어 후 모델 성능 손실 | privacy-utility trade-off |
| 접근권한 | black-box/white-box/label-only setting | 공격자 능력 범위 | threat model 명시 |
| 도메인 위험 | domain sensitivity, subgroup MI risk | 의료·금융 등 민감성 | 고위험 domain 평가 |
| 감사 가능성 | experiment trace, attack config, defense config | 재현성과 책임성 | W15 evidence chain |

---

## 10. 재현성 체크리스트

| 항목 | 기록해야 할 내용 |
|---|---|
| Target model | architecture, train/test split, train/test accuracy, confidence output 여부 |
| Threat model | black-box, white-box, label-only, shadow data 보유 여부 |
| Dataset | member/non-member 구성, class balance, sensitive attribute 여부 |
| Attack setting | attack feature, shadow model 여부, threshold/attack classifier, query limit |
| Metrics | Acc_MI, Adv_MI, AUC, precision, recall, FPR, FNR |
| Leakage cause | GenGap, LossGap, ConfGap, calibration 상태 |
| Defense setting | DP, regularization, output restriction, confidence masking, calibration |
| Utility | baseline accuracy, defense accuracy, UtilityDrop |
| Logs | seed, model checkpoint, attack config, defense config, evaluation script |
| 한계 | toy/synthetic MIA 결과를 실제 개인 membership 노출 보증으로 과장하지 않음 |

---

## 11. 논문의 고유 기여

1. Membership inference attack을 ML privacy의 대표 공격으로 체계화한다.
2. Black-box, white-box, shadow-model, confidence-based, loss-based attack을 threat model별로 정리한다.
3. Overfitting과 confidence leakage가 membership privacy risk를 높인다는 점을 설명한다.
4. DP 방어 효과를 formal epsilon만이 아니라 empirical MI advantage 감소로도 평가해야 함을 보여준다.
5. W11 기말논문에서 privacy risk를 모델 출력 기반 추론 위험으로 정의하는 근거를 제공한다.

---

## 12. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 공격 설정 다양성 | black-box, white-box, label-only에 따라 결과가 크게 달라진다. | threat model을 분리해 표기 |
| Accuracy만으로 불충분 | attack accuracy는 class imbalance에 민감하다. | Adv_MI, AUC, FPR/FNR 병기 |
| 실제 데이터 윤리 문제 | 실제 개인 membership 추론 실험은 개인정보 위험이 크다. | synthetic/toy data와 문헌 기반 분석으로 제한 |
| 방어 trade-off | DP·output restriction은 utility와 API 유용성을 낮출 수 있다. | UtilityDrop과 response utility 병기 |
| Adaptive attacker | 방어를 아는 공격자는 우회 feature를 사용할 수 있다. | adaptive risk를 한계로 명시 |
| Foundation model 확장 | 대규모 모델·생성모델·LLM에서 MIA 평가가 더 복잡하다. | W07/W08/W14와 연결해 향후 과제로 제시 |

---

## 13. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | AI privacy risk는 원본 데이터 유출뿐 아니라 모델 출력 기반 membership 추론 위험이라는 문제의식 |
| 2장 관련연구 | Membership inference attacks survey를 핵심 공격 문헌으로 정리 |
| 3장 위협모형 | training membership, confidence score, model output, loss/gradient, query log 보호 자산 정의 |
| 4장 연구방법 | Adv_MI, Acc_MI, AUC, GenGap, LossGap, ConfGap, DefenseGain, UtilityDrop 지표 설계 |
| 5장 분석 | MIA threat model table과 privacy-utility 평가표 제시 |
| 6장 보안적 함의 | DP, output restriction, regularization, MIA audit, query logging 필요성 해석 |

---

## 14. 기말논문 연결 3문장

1. W11에서 기말논문에 반영할 개념: Membership inference attack은 모델이 학습 데이터를 직접 공개하지 않아도 output confidence, loss, gradient 차이를 통해 특정 record의 학습 포함 여부가 노출될 수 있음을 보여준다.
2. W11에서 기말논문에 반영할 표·그림·실험: black-box/white-box MIA 위협모형표, Adv_MI·Acc_MI·AUC 평가표, GenGap/LossGap/ConfGap 원인 분석표, DefenseGain-UtilityDrop 비교표를 반영한다.
3. W11이 LLM/RAG 보안 감사 프레임워크와 연결되는 지점: LLM/RAG 모델·로그·fine-tuning 데이터 보호를 주장할 때도 membership leakage, output restriction, query auditing, empirical attack evaluation을 W14/W15 evidence chain에 포함해야 한다.

---

## 15. 최종 판단

P04는 W11의 membership inference 공격 기준 문헌이다. P01/P02/P03이 differential privacy의 정의와 적용 방식을 제공한다면, P04는 실제 공격자가 모델 출력과 학습 흔적을 통해 privacy risk를 어떻게 추론하는지 설명한다. 따라서 W11 기말논문 연결에서는 P04를 **MIA threat model, MI advantage, confidence/loss leakage, DP 방어 효과 평가의 중심 근거 문헌**으로 사용하는 것이 적절하다.

---

## 16. 변환 호환성 메모

```bash
pandoc P04_summary.md -o P04_summary.docx
pandoc P04_summary.md -o P04_summary.pdf --pdf-engine=xelatex
```
