# P02 Summary

## Recent Advances of Differential Privacy in Centralized Deep Learning: A Systematic Survey — Lea Demelius, Roman Kern, Andreas Trugler, ACM Computing Surveys, 2025

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W11 차등프라이버시(Differential Privacy) & Membership Inference |
| 논문명 | Recent Advances of Differential Privacy in Centralized Deep Learning: A Systematic Survey |
| 저자 | Lea Demelius, Roman Kern, Andreas Trugler |
| 공식 출판 정보 | ACM Computing Surveys, Vol. 57, No. 6, pp. 1–28, online 2025-02-10, print 2025-06-30 |
| DOI | https://doi.org/10.1145/3712000 |
| 보조 URL | https://arxiv.org/abs/2309.16398 |
| 로컬 PDF | `01_papers/pdf/02_Demelius_et_al_2025_Centralized_Deep_Learning_DP_Survey.pdf` |
| 검증 상태 | W11 `paper_list.md` 기준 공식 DOI 확인. 기존 강의계획서/프롬프트의 `Jonathan Demelius` 표기는 공식 메타데이터와 맞지 않아 불일치 메모 유지 |
| PDF 확인 메모 | repo의 PDF 폴더에 해당 PDF blob이 존재함을 확인했다. 요약은 로컬 PDF 경로와 W11 `paper_list.md`의 공식 DOI 메타데이터 기준으로 보완했다. |
| 핵심 근거 사용 가능 여부 | 가능. W11에서 centralized deep learning의 DP-SGD, gradient clipping, noise addition, privacy accountant, composition, utility degradation, reporting protocol을 설명하는 핵심 문헌으로 사용 |

---

## 1. 한 문장 요약

이 논문은 centralized deep learning에서 differential privacy 적용 연구를 **DP-SGD, per-sample gradient clipping, Gaussian noise addition, sampling rate, privacy accountant, composition, privacy budget, utility degradation, hyperparameter sensitivity, robustness·fairness·calibration impact, empirical leakage evaluation** 관점에서 체계적으로 정리하며, W11에서 DP 실험을 보고할 때 필요한 기술 항목과 재현성 기준을 제공하는 핵심 survey 문헌이다.

---

## 2. 핵심 연구문제

> 중앙집중 deep learning에서 DP를 적용하려면 개별 sample gradient의 영향을 제한하고 noise를 추가해 privacy budget을 관리해야 한다. 이때 clipping norm, noise multiplier, sampling rate, training epoch, accountant 선택, model architecture, utility loss는 privacy 보장과 실사용 성능에 어떤 영향을 주는가?

| 번호 | 연구질문 |
|---|---|
| RQ1 | DP-SGD는 per-sample gradient clipping과 Gaussian noise addition을 통해 개별 training sample의 영향을 어떻게 제한하는가? |
| RQ2 | Privacy accountant와 composition은 반복 학습 과정에서 epsilon/delta를 어떻게 추적하며, sampling rate와 epoch 수는 privacy budget에 어떤 영향을 주는가? |
| RQ3 | DP 적용 후 accuracy, calibration, robustness, fairness, convergence speed는 어떻게 변하며 어떤 utility trade-off가 발생하는가? |
| RQ4 | Centralized deep learning에서 DP formal guarantee와 membership inference empirical evaluation을 어떻게 함께 보고해야 하는가? |
| RQ5 | 기말논문에서 DP 실험을 수행하지 않더라도 clipping norm, noise multiplier, accountant, utility drop을 어떤 체크리스트로 정리해야 하는가? |

---

## 3. 논문의 핵심 기여

| 기여 | 설명 | W11 연결 |
|---|---|---|
| DP deep learning survey | 중앙집중 deep learning에서 DP 적용 연구를 체계적으로 정리 | W11 P01의 DP 개념을 실제 학습 절차로 확장 |
| DP-SGD 핵심 요소 정리 | per-sample clipping, noise addition, mini-batch sampling, accountant의 역할 설명 | W11 핵심 수식·실험 설계 |
| Privacy accounting 강조 | composition과 accountant 없이는 privacy claim을 검증하기 어렵다는 점 제시 | DP claim audit 연결 |
| Utility degradation 분석 | DP 적용이 accuracy, convergence, calibration, fairness에 미치는 영향 정리 | privacy-utility trade-off 평가 |
| Reporting protocol 근거 | epsilon/delta, clipping, noise, sampling, epoch, seed 기록 필요성 제시 | 기말논문 재현성 체크리스트 |

---

## 4. 목차별 핵심 개괄

| 목차 | 핵심 내용 | 비전공자용 이해 |
|---|---|---|
| 1. Introduction | Deep learning은 대규모 데이터에서 강력하지만, 모델이 training sample 정보를 기억하거나 누출할 수 있다. DP는 이를 완화하는 formal privacy framework다. | 딥러닝 모델이 학습 데이터의 흔적을 외워버릴 수 있으므로, 학습 중 개인정보 흔적을 줄이는 장치가 필요하다. |
| 2. Differential Privacy Background | DP 정의, epsilon/delta, randomized mechanism, composition, privacy budget 개념을 설명한다. | 한 사람의 데이터가 있어도 없어도 학습 결과가 크게 달라지지 않게 하는 원리다. |
| 3. DP in Deep Learning | DP-SGD를 중심으로 gradient clipping, noise addition, sampling, accountant, optimizer 변형을 정리한다. | 각 샘플의 영향력을 제한하고 noise를 섞어 특정 개인 데이터가 모델에 과하게 반영되지 않게 한다. |
| 4. Privacy Accounting | RDP, moments accountant, advanced composition 등 privacy loss를 추적하는 방식을 다룬다. | 학습을 반복할수록 개인정보 비용이 쌓이므로 이를 장부처럼 계산해야 한다. |
| 5. Utility and Performance | DP는 accuracy와 convergence speed를 낮출 수 있으며, model size, dataset, clipping norm, noise multiplier에 민감하다. | 개인정보를 더 강하게 보호할수록 모델 성능이 떨어질 수 있다. |
| 6. Robustness, Fairness, Calibration | DP가 일반 정확도 외에도 subgroup fairness, calibration, uncertainty, robustness에 영향을 줄 수 있음을 논의한다. | 전체 정확도가 괜찮아도 특정 집단 성능이나 확신도 품질이 나빠질 수 있다. |
| 7. Evaluation and Reporting | DP 실험은 epsilon/delta, noise multiplier, clipping norm, sampling rate, epoch, accountant, baseline utility를 투명하게 보고해야 한다. | “DP 적용”이라고만 쓰면 부족하고, 어떤 설정으로 얼마나 보호했는지 적어야 한다. |
| 8. Challenges and Future Work | 대형 모델, foundation model, transfer learning, hyperparameter tuning, privacy amplification, practical utility가 향후 과제다. | 큰 모델에 DP를 적용하면 비용과 성능 문제가 더 커진다. |
| 9. Conclusion | Centralized deep learning의 DP 연구는 formal guarantee와 practical performance를 함께 보고해야 한다. | 수학적 보호와 실제 성능을 분리해서 동시에 평가해야 한다. |

---

## 5. 핵심 이론 및 수식

> 아래 수식은 DP-SGD와 centralized deep learning privacy accounting을 W11 보고서에서 설명하기 위한 표준화된 표현이다. 수식은 GitHub, MS Word, PDF 변환 호환성을 위해 Markdown 표 밖의 LaTeX block math로 작성한다.

### 5.1 Per-sample Gradient Clipping

각 sample gradient의 L2 norm이 clipping norm $C$를 넘지 않도록 제한한다.

$$
\bar{g}_i=g_i\cdot \min\left(1,\frac{C}{\|g_i\|_2}\right)
$$

| 기호 | 의미 |
|---|---|
| $g_i$ | sample $i$의 gradient |
| $\bar{g}_i$ | clipping 후 gradient |
| $C$ | clipping norm |

### 비전공자용 설명

한 사람의 데이터가 모델 업데이트에 너무 큰 영향을 주지 못하게 gradient 크기를 잘라내는 것이다.

### 보안적 의미

Clipping이 없으면 특정 sample이 update에 큰 영향을 줄 수 있고, 이는 membership inference나 reconstruction risk를 키울 수 있다. clipping norm은 반드시 보고해야 한다.

---

### 5.2 DP-SGD Noise Addition

Clipping된 gradient 합에 Gaussian noise를 추가한 뒤 mini-batch 평균 gradient로 사용한다.

$$
\tilde{g}=\frac{1}{B}\left(\sum_{i=1}^{B}\bar{g}_i+\mathcal{N}(0,\sigma^2C^2I)\right)
$$

| 기호 | 의미 |
|---|---|
| $B$ | batch size |
| $\sigma$ | noise multiplier |
| $C$ | clipping norm |
| $I$ | identity matrix |

### 보안적 의미

Noise multiplier가 클수록 privacy는 강해질 수 있지만, 모델 학습은 어려워지고 utility drop이 커질 수 있다.

---

### 5.3 Privacy Budget Accounting

DP-SGD는 여러 step의 privacy loss를 누적 관리해야 한다.

$$
\epsilon_{total}=Accountant(q,\sigma,T,\delta)
$$

| 기호 | 의미 |
|---|---|
| $q$ | sampling rate |
| $\sigma$ | noise multiplier |
| $T$ | training step 수 |
| $\delta$ | 실패확률 |
| $Accountant$ | RDP accountant, moments accountant 등 privacy accountant |

### 보안적 의미

같은 noise multiplier라도 sampling rate와 step 수가 다르면 최종 epsilon이 달라진다. 따라서 epsilon만이 아니라 accountant 입력값도 함께 기록해야 한다.

---

### 5.4 Utility Drop

DP 적용 후 모델 성능 손실을 측정한다.

$$
UtilityDrop=Acc_{non\text{-}private}-Acc_{DP}
$$

| 기호 | 의미 |
|---|---|
| $Acc_{non\text{-}private}$ | DP 없이 학습한 기준 모델 정확도 |
| $Acc_{DP}$ | DP 적용 모델 정확도 |

### 보안적 의미

Privacy 보장만 보고하면 실사용 가능성을 판단하기 어렵다. DP 실험은 utility drop을 반드시 병기해야 한다.

---

### 5.5 Privacy-Utility Score

privacy와 utility를 함께 고려하는 요약 지표를 만들 수 있다.

$$
PUScore=Acc_{DP}-\lambda\epsilon_{total}-\mu UtilityDrop
$$

### 보안적 의미

epsilon이 낮아도 accuracy가 지나치게 낮거나 utility drop이 크면 실무적으로 어렵다. 반대로 accuracy가 높아도 epsilon이 너무 크면 privacy 보장이 약하다.

---

### 5.6 Membership Inference Advantage under DP

DP 적용 전후 MIA 위험 감소를 비교한다.

$$
MIReduction=Adv_{MI}^{non\text{-}private}-Adv_{MI}^{DP}
$$

| 기호 | 의미 |
|---|---|
| $Adv_{MI}^{non\text{-}private}$ | 비공개 보호 없이 학습한 모델의 MIA advantage |
| $Adv_{MI}^{DP}$ | DP 적용 모델의 MIA advantage |

### 보안적 의미

DP formal guarantee와 별개로 empirical MIA 위험도 함께 측정하면 실제 privacy risk 변화를 더 잘 설명할 수 있다.

---

### 5.7 Reporting Completeness

DP deep learning 실험이 필요한 설정을 얼마나 보고했는지 평가한다.

$$
ReportingCompleteness=\frac{|H_{reported}\cap H_{required}|}{|H_{required}|}
$$

| 기호 | 의미 |
|---|---|
| $H_{reported}$ | 보고서에 실제 기록된 hyperparameter·privacy 항목 |
| $H_{required}$ | epsilon, delta, clipping, noise, sampling, epoch, accountant, seed, baseline 등 필수 항목 |

### 보안적 의미

DP-SGD는 hyperparameter에 매우 민감하므로, 설정이 빠지면 실험 재현과 privacy claim 검증이 어렵다.

---

## 6. AI 원리 70% 관점 분석

| 원리 항목 | 설명 | W11/P02에서의 의미 |
|---|---|---|
| Centralized Deep Learning | 하나의 training pipeline에서 모델을 학습 | FL과 달리 서버가 데이터와 학습을 중앙 관리 |
| DP-SGD | SGD에 clipping과 noise를 추가 | DP deep learning의 표준 접근 |
| Per-sample Gradient | 각 sample의 gradient를 따로 계산 | 개별 데이터 영향 제한의 전제 |
| Clipping Norm | gradient 영향력 상한 | privacy와 utility를 모두 좌우 |
| Noise Multiplier | Gaussian noise 크기 | privacy budget과 accuracy trade-off |
| Privacy Accountant | composition으로 누적 privacy loss 계산 | epsilon_total 산출 근거 |
| Utility Evaluation | accuracy, loss, convergence, calibration | DP 실용성 판단 |
| Empirical Leakage Test | MIA 등으로 leakage를 보완 평가 | W11 P04/P05와 연결 |

---

## 7. 보안 이슈 30% 관점 분석

| 보안 항목 | DP-SGD 관점 해석 | 대표 평가 지표 |
|---|---|---|
| 기밀성 | 개별 training sample의 영향과 membership 노출을 줄임 | epsilon, delta, MI advantage |
| 무결성 | 과도한 noise가 모델 품질과 decision boundary를 왜곡할 수 있음 | UtilityDrop, calibration error |
| 가용성 | DP 학습은 계산비용과 수렴시간을 증가시킬 수 있음 | training time, convergence round |
| 프라이버시 | clipping/noise/accountant가 없으면 DP claim 검증 불가 | ReportingCompleteness, accountant log |
| 안전성 | 의료·금융 모델에서 privacy와 accuracy trade-off가 downstream risk를 만들 수 있음 | subgroup performance, failure case |
| 책임성 | DP 설정과 privacy budget을 기록해야 감사 가능 | DP mechanism audit, seed/config log |

---

## 8. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | training sample, membership, sensitive attribute, per-sample gradient, model parameter, confidence output, privacy accountant log |
| 공격자 목표 | membership inference, reconstruction, attribute inference, repeated query leakage, confidence exploitation |
| 공격자 능력 | model output 관찰, confidence score 접근, auxiliary data 보유, white-box/black-box 조건, repeated query 수행 |
| 공격 경로 | centralized training data → per-sample gradient → clipped/noisy update → DP model release → model query/output analysis → privacy inference |
| 방어자 능력 | DP-SGD, clipping, Gaussian noise, privacy accountant, output restriction, MIA evaluation, pipeline audit |
| 제외 범위 | 실제 개인정보 기반 공격 실험, 실제 민감 데이터 재식별, 공격 코드 제공, privacy guarantee 과장 표현 |

---

## 9. 평가방법 및 지표

| 평가축 | 지표 | 의미 | W11/P02 활용 |
|---|---|---|---|
| Formal privacy | epsilon_total, delta | DP 보장 강도 | privacy accounting 결과 |
| Mechanism setting | clipping norm, noise multiplier, sampling rate | DP-SGD 핵심 설정 | 재현성 필수 항목 |
| Utility | clean accuracy, loss, UtilityDrop | DP 후 성능 변화 | privacy-utility trade-off |
| Learning behavior | convergence speed, training stability | DP 학습 안정성 | 실험 해석 |
| Empirical leakage | MI advantage, MIReduction | 실제 MIA 위험 변화 | W11 P04 연결 |
| Calibration/fairness | ECE, subgroup accuracy, fairness gap | DP가 품질과 공정성에 미치는 영향 | 고위험 domain 평가 |
| Reporting quality | ReportingCompleteness | DP 실험 보고 충분성 | 논문 검수 기준 |
| Cost | training time, memory overhead | per-sample gradient와 noise 비용 | 운영 가능성 평가 |

---

## 10. 재현성 체크리스트

| 항목 | 기록해야 할 내용 |
|---|---|
| Dataset | dataset name, train/test split, sensitive attribute 여부, preprocessing |
| Model | architecture, parameter count, optimizer, loss function |
| DP mechanism | DP-SGD 여부, Gaussian mechanism, clipping norm, noise multiplier |
| Privacy accounting | epsilon, delta, accountant type, sampling rate, training step, epoch 수 |
| Training setting | batch size, learning rate, seed, augmentation, early stopping |
| Baseline | non-private baseline accuracy/loss와 DP model result |
| Utility metrics | accuracy, loss, calibration, subgroup performance, UtilityDrop |
| Empirical attack | MIA/attribute inference/reconstruction 평가 여부와 지표 |
| Logs | config file, accountant log, checkpoint, random seed, evaluation script |
| 한계 | DP 보장이 적용된 mechanism과 데이터 범위 밖에는 보장하지 않음 |

---

## 11. 논문의 고유 기여

1. Centralized deep learning에서 DP 적용 연구를 체계적으로 정리한다.
2. DP-SGD의 핵심 구성요소인 per-sample clipping, noise addition, privacy accountant를 명확히 설명한다.
3. DP 실험 보고에서 epsilon/delta만이 아니라 clipping norm, noise multiplier, sampling rate, epoch, accountant를 함께 제시해야 함을 강조한다.
4. DP가 accuracy뿐 아니라 calibration, fairness, robustness, convergence에 미치는 영향을 평가해야 함을 보여준다.
5. W11 기말논문에서 DP 방어와 MIA empirical evaluation을 연결하는 방법론적 근거를 제공한다.

---

## 12. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| Utility 손실 | 강한 DP는 정확도와 수렴을 저하시킬 수 있다. | non-private baseline과 UtilityDrop 병기 |
| Hyperparameter 민감성 | clipping norm, noise multiplier, sampling rate가 결과를 크게 바꾼다. | ReportingCompleteness 체크리스트 적용 |
| Accountant 선택 차이 | accountant 방식에 따라 epsilon 계산이 달라질 수 있다. | accountant type과 입력값 기록 |
| 대형 모델 적용 어려움 | per-sample gradient와 noise 때문에 계산비용이 크다. | toy/small model 또는 문헌 기반 비교로 제한 |
| Empirical attack과 formal guarantee 차이 | MIA 감소가 곧 DP 보장을 의미하지는 않는다. | formal 지표와 empirical 지표 분리 |
| Pipeline leakage | DP-SGD 밖의 preprocessing, logging, post-processing은 별도 위험이다. | pipeline audit 포함 |

---

## 13. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | DP deep learning은 privacy 보장과 utility trade-off를 함께 보고해야 한다는 문제의식 |
| 2장 관련연구 | centralized deep learning DP systematic survey로 정리 |
| 3장 위협모형 | training sample, gradient, model parameter, output confidence, accountant log 보호 자산 정의 |
| 4장 연구방법 | clipping norm, noise multiplier, epsilon_total, UtilityDrop, MIReduction, ReportingCompleteness 지표 설계 |
| 5장 분석 | DP-SGD workflow와 privacy accounting checklist 표 제시 |
| 6장 보안적 함의 | DP-SGD 적용 범위, composition, empirical leakage evaluation, utility/fairness/cost 해석 |

---

## 14. 기말논문 연결 3문장

1. W11에서 기말논문에 반영할 개념: DP-SGD는 per-sample gradient clipping과 Gaussian noise addition으로 개별 training sample의 영향력을 제한하지만, epsilon_total은 sampling rate, noise multiplier, training step, accountant에 따라 달라진다.
2. W11에서 기말논문에 반영할 표·그림·실험: DP-SGD workflow, clipping/noise/accountant 설정표, UtilityDrop과 MIReduction 비교표, ReportingCompleteness checklist를 반영한다.
3. W11이 LLM/RAG 보안 감사 프레임워크와 연결되는 지점: LLM/RAG 학습·로그 보호에 DP를 주장하려면 clipping/noise/accountant, query/logging scope, empirical leakage evaluation, compliance evidence를 W14/W15 evidence chain에 포함해야 한다.

---

## 15. 최종 판단

P02는 W11에서 DP-SGD와 centralized deep learning privacy accounting의 핵심 문헌이다. P01이 DP 오용 방지와 claim audit 기준을 제공한다면, P02는 실제 deep learning 학습에서 DP를 구현·보고·평가하는 방법론을 제공한다. 따라서 W11 기말논문 연결에서는 P02를 **DP-SGD, privacy accountant, utility degradation, MIA empirical evaluation 병행 보고의 중심 근거 문헌**으로 사용하는 것이 적절하다.

---

## 16. 변환 호환성 메모

```bash
pandoc P02_summary.md -o P02_summary.docx
pandoc P02_summary.md -o P02_summary.pdf --pdf-engine=xelatex
```
