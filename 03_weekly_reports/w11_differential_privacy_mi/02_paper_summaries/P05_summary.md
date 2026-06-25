# P05 Summary

## Defenses to Membership Inference Attacks: A Survey — Li Hu et al., ACM Computing Surveys, 2024

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W11 차등프라이버시(Differential Privacy) & Membership Inference |
| 공식 논문명 | Defenses to Membership Inference Attacks: A Survey |
| 공식 저자 | Li Hu, Anli Yan, Hongyang Yan, Jin Li, Teng Huang, Yingying Zhang, Changyu Dong, Chunsheng Yang |
| 공식 출판 정보 | ACM Computing Surveys, Vol. 56, No. 4, pp. 1–34, online 2023-11-10, print 2024-04-30 |
| DOI | https://doi.org/10.1145/3620667 |
| 로컬 PDF | `01_papers/pdf/05_RELATED_Bai_et_al_2024_MIA_Attacks_Defenses_FL_Survey.pdf` |
| 로컬 PDF 상태 | W11 `paper_list.md` 기준 로컬 PDF는 Bai et al.의 FL-MIA 관련 survey로, 공식 P05 DOI 논문과 다르다. 지정 논문처럼 인용하지 않는다. |
| 검증 상태 | W11 `paper_list.md` 기준 공식 DOI 확인. 강의자료의 `Hongsheng Hu et al.` 표기는 P04와 혼동 가능성이 있어 최종 추가 확인 메모 유지 |
| PDF 확인 메모 | repo의 PDF 폴더에 P05 관련 PDF blob이 존재함을 확인했다. 다만 해당 PDF는 공식 P05 지정 논문과 다르므로, summary는 공식 DOI 기준 P05를 중심으로 작성하고 로컬 PDF는 FL-MIA 보완 문헌으로만 해석한다. |
| 핵심 근거 사용 가능 여부 | 가능. 공식 P05는 MIA 방어 taxonomy의 핵심 문헌이고, 로컬 관련 PDF는 federated learning 환경의 MIA 공격·방어 보완 문헌으로 제한적으로 사용 |

---

## 1. 한 문장 요약

공식 P05 논문은 membership inference attack 방어를 **regularization, data augmentation, adversarial training, confidence masking, output restriction, differential privacy, knowledge distillation, model compression, calibration, auditing, empirical defense evaluation** 관점에서 체계화하며, W11에서 DP뿐 아니라 비-DP 방어까지 포함해 **DefenseGain과 UtilityLoss를 함께 평가하는 privacy-utility trade-off 기준**을 제공하는 핵심 방어 survey 문헌이다.

---

## 2. 핵심 연구문제

> Membership inference attack은 모델 출력과 학습 흔적을 이용해 특정 record가 training data에 포함되었는지 추론한다. 방어자는 학습 단계, 모델 구조, 출력 단계, 후처리, 감사 단계에서 어떤 방법으로 MI risk를 줄이고, 방어 효과와 utility 손실을 어떻게 함께 평가해야 하는가?

| 번호 | 연구질문 |
|---|---|
| RQ1 | MIA 방어는 training-time, model-time, output-time, post-processing, auditing 단계에서 어떻게 분류되는가? |
| RQ2 | Differential privacy, regularization, dropout, label smoothing, adversarial regularization, knowledge distillation, output restriction은 각각 어떤 방식으로 MI risk를 줄이는가? |
| RQ3 | 방어가 confidence score만 숨기고 실제 membership leakage를 줄이지 못하는 경우를 어떻게 검증할 수 있는가? |
| RQ4 | 좋은 방어는 MI advantage를 낮추면서 clean accuracy, calibration, fairness, response utility를 얼마나 보존해야 하는가? |
| RQ5 | 공식 DOI 논문과 로컬 관련 PDF가 다를 때, 최종 보고서에서는 참고문헌·PDF·summary를 어떻게 분리 관리해야 하는가? |

---

## 3. 논문의 핵심 기여

| 기여 | 설명 | W11 연결 |
|---|---|---|
| MIA defense taxonomy | MIA 방어를 학습 단계, 출력 단계, 모델 구조, 사후 감사 단계로 분류 | W11 방어 핵심 문헌 |
| DP와 비-DP 방어 비교 | DP, regularization, output restriction, distillation, adversarial training의 장단점 비교 | P01/P02 DP와 P04 MIA 공격 연결 |
| Defense-utility trade-off 강조 | 방어가 privacy risk를 낮추더라도 utility·calibration·fairness 비용이 발생할 수 있음을 설명 | 기말논문 평가표 근거 |
| 실증 평가 필요성 제시 | MI advantage, AUC, defense gain, utility loss, adaptive attack을 함께 봐야 함을 제시 | empirical privacy evaluation 연결 |
| 로컬 PDF 관리 주의 | W11 P05는 공식 DOI와 로컬 PDF가 다르므로 인용 기준 분리가 필요 | 참고문헌 검증표 근거 |

---

## 4. 목차별 핵심 개괄

| 목차 | 핵심 내용 | 비전공자용 이해 |
|---|---|---|
| 1. Introduction | MIA는 모델이 학습 데이터를 얼마나 기억하는지를 이용한 대표 privacy attack이며, 방어는 모델 성능과 개인정보 보호를 동시에 고려해야 한다. | 모델이 특정 사람 데이터를 배웠는지 들키지 않도록 방어해야 한다. |
| 2. Background on MIA | Black-box, white-box, confidence-based, loss-based, shadow-model 기반 MIA의 원리를 정리한다. | 공격자는 모델 답변의 확신도나 loss를 보고 학습 포함 여부를 추정한다. |
| 3. Defense Taxonomy | Regularization, dropout, label smoothing, distillation, DP, output perturbation, confidence masking, auditing 등 방어를 분류한다. | 모델이 데이터를 덜 외우게 하거나, 출력에서 민감한 단서를 덜 주게 만드는 방법이다. |
| 4. Training-time Defenses | Regularization, data augmentation, adversarial regularization, DP-SGD처럼 학습 과정에서 leakage를 줄이는 방법을 다룬다. | 학습할 때부터 특정 데이터가 모델에 너무 강하게 남지 않도록 조절한다. |
| 5. Output-time Defenses | Confidence masking, top-k output, label-only output, output perturbation처럼 API 출력 정보를 제한한다. | 모델이 너무 자세한 확률값을 주면 공격이 쉬워지므로, 출력 정보를 줄이는 방어다. |
| 6. Evaluation Metrics | MI advantage, attack accuracy, AUC, precision/recall, utility loss, calibration, defense cost를 함께 보고해야 한다. | 방어가 공격을 막는지와 모델이 여전히 쓸 만한지를 같이 봐야 한다. |
| 7. Challenges | Adaptive attacker, over-privacy cost, defense transferability, benchmark 부족, utility-fairness trade-off가 남아 있다. | 공격자가 방어를 알고 우회하면 기존 방어가 약해질 수 있다. |
| 8. Conclusion | MIA 방어는 단일 기법보다 threat model, metric, utility, audit evidence를 결합한 평가가 필요하다. | 개인정보 보호는 방어 이름보다 실제 공격 성공률과 성능 변화를 함께 봐야 한다. |
| 로컬 관련 PDF 메모 | 로컬 PDF는 Bai et al.의 FL-MIA 관련 survey로 보이며, official P05와 다르다. W10 FL security와 W11 MIA를 연결하는 보완 자료로만 사용한다. | PDF가 있다고 해서 공식 지정 논문으로 인용하면 안 된다. |

---

## 5. 핵심 이론 및 수식

> 아래 수식은 MIA 방어 평가와 W11 privacy-utility trade-off를 설명하기 위한 표준화된 표현이다. 실제 공격 코드나 유해 절차가 아니라 방어 성능과 재현성 평가를 위한 지표다.

### 5.1 Defense Effectiveness

방어 전후 membership inference advantage 감소량을 측정한다.

$$
DefenseGain=Adv_{MI}^{before}-Adv_{MI}^{after}
$$

| 기호 | 의미 |
|---|---|
| $Adv_{MI}^{before}$ | 방어 적용 전 membership inference advantage |
| $Adv_{MI}^{after}$ | 방어 적용 후 membership inference advantage |

### 비전공자용 설명

방어를 적용한 뒤 공격자가 “이 데이터가 학습에 있었는지” 맞히는 능력이 얼마나 줄었는지 보는 지표다.

---

### 5.2 Utility Loss

방어 적용으로 인해 정상 모델 성능이 얼마나 감소했는지 측정한다.

$$
UtilityLoss=Acc_{before}-Acc_{after}
$$

| 기호 | 의미 |
|---|---|
| $Acc_{before}$ | 방어 전 모델 정확도 |
| $Acc_{after}$ | 방어 후 모델 정확도 |

### 보안적 의미

좋은 방어는 privacy risk를 낮추면서 utility loss를 과도하게 만들지 않아야 한다.

---

### 5.3 Privacy-Utility Efficiency

방어 효율은 privacy 개선량 대비 utility 비용으로 볼 수 있다.

$$
DefenseEfficiency=\frac{DefenseGain}{UtilityLoss+\epsilon_{cost}}
$$

| 기호 | 의미 |
|---|---|
| $\epsilon_{cost}$ | 0으로 나누는 것을 피하기 위한 작은 안정화 값 |

### 보안적 의미

DefenseGain이 커도 UtilityLoss가 지나치게 크면 실무 적용성이 낮다. 방어는 효과와 비용을 함께 비교해야 한다.

---

### 5.4 MIA Attack AUC Reduction

방어 전후 MIA AUC 감소를 평가한다.

$$
AUCReduction=AUC_{MI}^{before}-AUC_{MI}^{after}
$$

### 보안적 의미

Attack accuracy는 class imbalance에 민감할 수 있으므로 AUC 감소도 함께 보는 것이 좋다.

---

### 5.5 Calibration Cost

일부 방어는 confidence calibration을 악화시킬 수 있다.

$$
CalibrationCost=ECE_{after}-ECE_{before}
$$

| 기호 | 의미 |
|---|---|
| $ECE$ | Expected Calibration Error |

### 보안적 의미

Confidence masking이나 output perturbation은 MIA를 줄일 수 있지만, 모델 확신도의 품질을 왜곡할 수 있다.

---

### 5.6 Over-Privacy Cost

방어가 과도해서 정상 사용성과 성능을 지나치게 낮추는 비용이다.

$$
OverPrivacyCost=\lambda UtilityLoss+\mu CalibrationCost+\nu LatencyIncrease
$$

### 보안적 의미

개인정보 보호만 극단적으로 높이면 모델이 쓸모없어질 수 있다. 특히 의료·금융·보안 분야에서는 utility와 safety도 함께 고려해야 한다.

---

### 5.7 FL-MIA Related Defense Risk

로컬 관련 PDF처럼 federated learning 맥락의 MIA 방어를 볼 때는 client update와 aggregation audit를 함께 고려한다.

$$
Risk_{FL\text{-}MIA}=\alpha LeakageRisk+\beta ClientHeterogeneity+\gamma AuditGap-\lambda DefenseCoverage
$$

### 보안적 의미

FL-MIA에서는 model output뿐 아니라 client update, aggregation, non-IID client heterogeneity가 membership risk와 방어 난이도를 바꾼다. 따라서 로컬 관련 PDF는 W10/W11 연결 보조 문헌으로 제한해 활용한다.

---

## 6. AI 원리 70% 관점 분석

| 원리 항목 | 설명 | W11/P05에서의 의미 |
|---|---|---|
| MIA Defense | membership leakage를 줄이는 방어 | 공식 P05의 핵심 |
| Regularization | 모델이 학습 데이터를 덜 외우게 함 | overfitting 완화 |
| Differential Privacy | 개별 sample 영향 제한 | formal privacy defense |
| Output Restriction | confidence/probability vector 제공 제한 | black-box MIA 완화 |
| Knowledge Distillation | teacher-student 학습으로 leakage 완화 가능 | 모델 구조 기반 방어 |
| Calibration | confidence quality 관리 | output defense 부작용 평가 |
| Auditing | 배포 전후 MIA 위험 측정 | empirical privacy evidence |
| FL-MIA 보완 | 로컬 PDF의 관련 주제 | 공식 P05와 혼동 금지 |

---

## 7. 보안 이슈 30% 관점 분석

| 보안 항목 | MIA Defense 관점 해석 | 대표 평가 지표 |
|---|---|---|
| 기밀성 | training membership 노출 위험을 줄임 | DefenseGain, Adv_MI, AUC reduction |
| 무결성 | 방어가 decision boundary와 calibration을 바꿀 수 있음 | CalibrationCost, UtilityLoss |
| 가용성 | 출력 제한·DP·auditing이 latency와 API 유용성을 낮출 수 있음 | LatencyIncrease, response utility |
| 프라이버시 | membership 자체가 민감정보인 domain에서 방어 필요 | MI risk, subgroup MI risk |
| 안전성 | 과도한 방어로 downstream task 성능이 낮아지면 안전 문제 발생 | OverPrivacyCost, failure case |
| 책임성 | 방어 전후 MIA audit evidence를 남겨야 함 | audit completeness, defense config trace |

---

## 8. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | training data membership, model output, confidence score, loss signal, query log, defense config, audit evidence |
| 공격자 목표 | 특정 record가 학습 데이터에 포함되었는지 추론, 방어 후에도 confidence/loss gap을 이용한 membership 추론 |
| 공격자 능력 | black-box query, confidence score 관찰, label-only 관찰, auxiliary/shadow data 보유, white-box 접근 가능성 |
| 공격 경로 | target sample query → model output/confidence/loss feature → membership score → defense 우회 또는 membership decision |
| 방어자 능력 | DP, regularization, output restriction, confidence masking, distillation, calibration, query throttling, MIA auditing |
| 제외 범위 | 실제 개인정보 대상 membership 추론, 실제 민감 데이터 재식별, 공격 코드 제공, 공식 P05와 로컬 관련 PDF 혼동 인용 |

---

## 9. 평가방법 및 지표

| 평가축 | 지표 | 의미 | W11/P05 활용 |
|---|---|---|---|
| 방어 효과 | DefenseGain, AUCReduction, MI reduction | MIA 위험 감소 | 방어 핵심 평가 |
| 공격 성공 | Adv_MI, Acc_MI, AUC, FPR/FNR | 방어 후 공격 잔여 위험 | empirical attack evaluation |
| Utility | clean accuracy, UtilityLoss | 방어 후 모델 성능 손실 | privacy-utility trade-off |
| Calibration | ECE, CalibrationCost | confidence 품질 변화 | output defense 평가 |
| 비용 | LatencyIncrease, memory/training overhead | 방어 운영 비용 | MLOps 평가 |
| 과잉보호 | OverPrivacyCost | utility·calibration·latency 손실 | 실무 적용성 평가 |
| 접근권한 | black-box/white-box/label-only | 공격자 능력 범위 | threat model 명시 |
| 서지 정확성 | official DOI match, local PDF mismatch flag | 참고문헌 정확성 | 기말논문 검증표 |

---

## 10. 재현성 체크리스트

| 항목 | 기록해야 할 내용 |
|---|---|
| Bibliographic status | 공식 DOI 논문과 로컬 PDF 동일 여부, mismatch flag |
| Target model | architecture, train/test split, train/test accuracy, confidence output 여부 |
| Threat model | black-box, white-box, label-only, shadow data 보유 여부 |
| Defense setting | DP, regularization, output restriction, distillation, confidence masking, auditing |
| Attack evaluation | Adv_MI, Acc_MI, AUC, precision/recall, FPR/FNR |
| Utility evaluation | baseline accuracy, defense accuracy, UtilityLoss, calibration |
| Cost | training time, inference latency, memory overhead, API response restriction |
| Logs | seed, model checkpoint, attack config, defense config, evaluation script |
| Local PDF note | 로컬 PDF가 FL-MIA 관련 문헌임을 별도 표시하고 공식 P05처럼 인용하지 않음 |
| 한계 | toy/synthetic MIA 방어 결과를 실제 개인 privacy 보증으로 과장하지 않음 |

---

## 11. 논문의 고유 기여

1. Membership inference attack 방어를 체계적으로 분류한 W11의 핵심 방어 문헌이다.
2. DP뿐 아니라 regularization, output restriction, distillation, calibration, auditing 등 비-DP 방어까지 비교한다.
3. 방어 성능을 DefenseGain 하나로만 보지 않고 UtilityLoss, CalibrationCost, OverPrivacyCost와 함께 해석해야 함을 제시한다.
4. W11 P04의 MIA 공격 taxonomy와 직접 연결되어 공격-방어-평가 matrix를 구성할 수 있다.
5. 공식 DOI와 로컬 관련 PDF가 다른 사례이므로, 참고문헌 검증표와 PDF 관리의 중요성을 보여준다.

---

## 12. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 로컬 PDF 불일치 | P05 로컬 PDF는 공식 DOI 논문이 아니라 FL-MIA 관련 survey다. | 공식 DOI 기준으로 인용하고 로컬 PDF는 관련 보완 문헌으로 표시 |
| Adaptive attacker | 방어를 아는 공격자는 confidence 외 다른 feature를 사용할 수 있다. | adaptive risk를 한계로 명시 |
| Output masking의 한계 | confidence를 숨겨도 label-only MIA가 가능할 수 있다. | label-only threat model 포함 |
| Utility trade-off | 강한 방어는 accuracy, calibration, latency를 악화시킬 수 있다. | UtilityLoss와 CalibrationCost 병기 |
| DP 비용 | DP는 formal guarantee를 제공하지만 utility와 training cost가 커질 수 있다. | epsilon/delta와 UtilityLoss 함께 보고 |
| Benchmark 부족 | 방어 비교가 dataset, model, attack setting에 따라 달라진다. | attack-defense-metric matrix와 config log 필수화 |

---

## 13. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | AI privacy 방어는 DP 하나가 아니라 MIA 방어 taxonomy와 privacy-utility trade-off로 평가해야 한다는 문제의식 |
| 2장 관련연구 | 공식 P05 DOI 논문을 MIA defense survey로 정리하고, 로컬 PDF mismatch는 검증표에 기록 |
| 3장 위협모형 | training membership, model output, confidence, query log, defense config 보호 자산 정의 |
| 4장 연구방법 | DefenseGain, UtilityLoss, AUCReduction, CalibrationCost, OverPrivacyCost, official DOI match 지표 설계 |
| 5장 분석 | MIA attack-defense-metric matrix와 공식/로컬 PDF mismatch 관리표 제시 |
| 6장 보안적 함의 | DP, regularization, output restriction, auditing, privacy-utility trade-off, 참고문헌 검증 필요성 해석 |

---

## 14. 기말논문 연결 3문장

1. W11에서 기말논문에 반영할 개념: MIA 방어는 DP만으로 한정되지 않으며, regularization, output restriction, distillation, calibration, auditing을 포함한 defense taxonomy와 privacy-utility trade-off로 평가해야 한다.
2. W11에서 기말논문에 반영할 표·그림·실험: DefenseGain, UtilityLoss, AUCReduction, CalibrationCost, OverPrivacyCost를 포함한 MIA attack-defense-metric matrix와 공식 DOI/로컬 PDF mismatch 검증표를 반영한다.
3. W11이 LLM/RAG 보안 감사 프레임워크와 연결되는 지점: LLM/RAG 모델·로그·fine-tuning 데이터 보호에서도 membership leakage 방어, output restriction, query auditing, defense config, compliance evidence를 W14/W15 evidence chain에 포함해야 한다.

---

## 15. 최종 판단

P05는 W11의 membership inference 방어체계 핵심 문헌이다. 다만 W11 `paper_list.md` 기준 로컬 PDF는 공식 DOI 논문과 다른 FL-MIA 관련 survey이므로, 기말논문 참고문헌에는 공식 DOI 논문인 Li Hu et al.의 ACM Computing Surveys 논문을 우선 사용해야 한다. 로컬 PDF는 federated learning 환경의 MIA 공격·방어를 보완하는 관련 문헌으로만 제한해 활용하는 것이 적절하다.

---

## 16. 변환 호환성 메모

```bash
pandoc P05_summary.md -o P05_summary.docx
pandoc P05_summary.md -o P05_summary.pdf --pdf-engine=xelatex
```
