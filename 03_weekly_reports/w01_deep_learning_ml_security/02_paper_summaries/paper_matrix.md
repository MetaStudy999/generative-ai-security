# W01 논문 5편 비교표

## 0. 문서 목적

이 문서는 W01 `P01_summary.md` ~ `P05_summary.md` 100점형 보완 내용을 반영한 논문 비교표다. W01의 핵심 주제는 **딥러닝 기본 원리, ML 생명주기 보증, 침입탐지 응용, 대적공격·강건성, ML 프라이버시 공격**이다.

---

## 1. 문헌 검증 및 역할 요약

| ID | 공식 확인 논문 | 공식 출판정보 | DOI/URL | 검증 상태 | W01 내 역할 |
|---|---|---|---|---|---|
| P01 | *Deep learning* | Yann LeCun, Yoshua Bengio, Geoffrey Hinton, Nature, 2015 | `https://doi.org/10.1038/nature14539` | 공식 DOI 확인 | 딥러닝 표현학습·역전파·CNN/RNN 원리 배경 |
| P02 | *Assuring the Machine Learning Lifecycle: Desiderata, Methods, and Challenges* | Rob Ashmore, Radu Calinescu, Colin Paterson, ACM Computing Surveys, 2021 | `https://doi.org/10.1145/3453444` | 공식 DOI 확인 | ML 생명주기 보증, evidence chain, 재현성 프레임 |
| P03 | *A Survey of Data Mining and Machine Learning Methods for Cyber Security Intrusion Detection* | Anna L. Buczak, Erhan Guven, IEEE Communications Surveys & Tutorials, 2016 | `https://doi.org/10.1109/COMST.2015.2494502` | 공식 DOI 확인 | 침입탐지 응용, 보안 데이터셋, 오탐/미탐 평가 |
| P04 | *Adversarial Attacks and Defenses in Machine Learning-Powered Networks: A Contemporary Survey* | Yulong Wang et al., arXiv, 2023 | `https://arxiv.org/abs/2303.06302` | 관련 논문 / 확인. 강의계획서 지정 IEEE COMST 논문 동일성 확인 필요 | 대적공격·방어 taxonomy, robust evaluation |
| P05 | *A Survey of Privacy Attacks in Machine Learning* | Maria Rigaki, Sebastian Garcia, ACM Computing Surveys, 2023 | `https://doi.org/10.1145/3624010` | 공식 DOI 확인 | membership/property/model leakage 등 ML privacy threat taxonomy |

---

## 2. 논문별 핵심 비교표

| 논문 | 연구문제 | 핵심 방법/분류 | AI 원리 기여 | 보안 위협 연결 | 핵심 평가 지표 | 한계/주의 | 기말논문 활용 |
|---|---|---|---|---|---|---|---|
| P01 | 딥러닝은 어떻게 계층적 표현을 학습하고 일반화하는가 | 다층 신경망, 역전파, CNN/RNN, representation learning | 경험위험최소화, gradient descent, backpropagation, hierarchical feature learning | gradient 기반 공격, 표현공간 취약성, data/model dependency | training/validation accuracy, loss, generalization gap, representation quality | 직접 보안 논문은 아니므로 threat model은 파생적으로 구성 | AI 원리와 보안 취약성의 기술적 배경 |
| P02 | ML 시스템 안전성을 생명주기 증거로 어떻게 보증할 것인가 | lifecycle 단계화, assurance case, verification evidence, traceability | ML 모델을 단일 artifact가 아니라 data-model-deployment pipeline으로 이해 | data quality failure, model verification gap, deployment drift, monitoring failure | evidence coverage, traceability, lifecycle risk, reproducibility score | 공격별 정량 프로토콜은 별도 설계 필요 | 위협모형, 재현성, 평가 프로토콜의 뼈대 |
| P03 | 침입탐지에 어떤 ML/데이터마이닝 방법과 평가지표가 적합한가 | IDS survey, classification/clustering/anomaly detection, confusion matrix | supervised/unsupervised ML을 보안 탐지 task에 매핑 | 오탐, 미탐, data drift, class imbalance, label quality 문제 | detection rate, false alarm rate, precision, recall, F1, ROC/AUC | 공개 데이터셋과 실제 운영망 사이의 domain gap 존재 | 보안 탐지 성능 지표와 운영 지표 설계 |
| P04 | 대적공격과 방어를 어떤 위협모형과 지표로 검증할 것인가 | adversarial attack/defense taxonomy, robust optimization, clean-robust trade-off | 입력 교란, decision boundary, robust training의 원리 설명 | evasion, transfer attack, physical attack, gradient masking, adaptive attack | ASR, robust accuracy, clean accuracy, perturbation budget, defense cost | 관련 arXiv 논문 기준. 강의계획서 지정 IEEE COMST 논문 동일성 확인 필요 | adversarial robustness 장과 공격-방어 평가표 |
| P05 | ML 프라이버시 공격은 어떤 자산과 공격자 지식을 노리는가 | privacy attack taxonomy, membership inference, model inversion, property inference | generalization gap과 output confidence가 privacy leakage로 이어지는 구조 설명 | membership inference, model inversion, property inference, data extraction | MI advantage, leakage risk, utility/privacy trade-off, DP budget | privacy risk를 단일 지표로 요약하기 어렵고 threat model 의존성 큼 | privacy leakage 평가축과 W11 DP/MIA 연결 |

---

## 3. 핵심 수식 비교

| ID | 수식/지표 | 용도 |
|---|---|---|
| P01 | `R(θ)=E[ℓ(f_θ(x),y)]` | 경험위험·학습 목표 이해 |
| P01 | `θ ← θ − η∇_θ L(θ)` | gradient descent와 역전파 기반 학습 |
| P02 | `LifecycleRisk = DataRisk + ModelRisk + DeploymentRisk + MonitoringGap` | ML 생명주기 위험 분해 |
| P02 | `EvidenceCoverage=|E_verified|/|E_required|` | 보증 증거 충족률 |
| P03 | `Precision=TP/(TP+FP)` | 침입탐지 오탐 영향 평가 |
| P03 | `Recall=TP/(TP+FN)` | 침입탐지 미탐 영향 평가 |
| P03 | `F1=2·Precision·Recall/(Precision+Recall)` | precision/recall 균형 평가 |
| P04 | `max_{δ∈Δ} ℓ(f_θ(x+δ),y)` | adversarial risk/공격 목적함수 |
| P04 | `RobustAcc=(1/n)Σ1[f_θ(x_i^adv)=y_i]` | 공격 조건 정확도 |
| P04 | `ASR=(1/n)Σ1[f_θ(x_i^adv)=y_target]` | 공격 성공률 |
| P05 | `Adv_MI=P[A(z)=1|z∈D_train]-P[A(z)=1|z∉D_train]` | membership inference advantage |
| P05 | `PrivacyUtilityScore=Utility−λ·LeakageRisk` | privacy-utility trade-off |

---

## 4. W01 통합 위협모형

| 구분 | 보호 자산 | 공격자/위험 | 방어·통제 | 대표 지표 |
|---|---|---|---|---|
| 딥러닝 원리 | 학습 데이터, 파라미터, 표현공간, gradient | overfitting, gradient 기반 공격, representation leakage | regularization, validation, robust evaluation | loss, accuracy, generalization gap |
| 생명주기 보증 | data pipeline, model artifact, deployment config, monitoring log | data drift, verification gap, 운영 failure | evidence chain, traceability, monitoring, rollback | evidence coverage, reproducibility score |
| 침입탐지 | network traffic, alert, label, IDS model | evasion, false negative, alert flooding, dataset shift | threshold tuning, anomaly detection, human review | detection rate, FAR, F1, ROC/AUC |
| 대적 강건성 | classifier decision, input integrity, model boundary | evasion, transfer attack, physical/adaptive attack | adversarial training, detection, robust testing | ASR, robust accuracy, perturbation budget |
| 프라이버시 | training membership, sensitive attribute, model output | membership inference, inversion, property inference | DP, output restriction, regularization, auditing | MI advantage, leakage rate, utility drop |

---

## 5. 평가 설계 매트릭스

| 평가 목적 | 반드시 포함할 지표 | 필요한 증거 | 연결 문헌 |
|---|---|---|---|
| 딥러닝 기본 성능 평가 | train/test accuracy, loss, generalization gap | dataset split, model config, seed, training log | P01 |
| ML 생명주기 보증 | evidence coverage, traceability, deployment risk | data version, model version, verification log, deployment log | P02 |
| 침입탐지 평가 | precision, recall, F1, FAR, detection rate | confusion matrix, threshold, dataset description, class distribution | P03 |
| 대적 강건성 평가 | clean accuracy, robust accuracy, ASR, perturbation budget | attack setting, defense config, adversarial examples, seed | P04 |
| 프라이버시 평가 | MI advantage, leakage risk, utility/privacy trade-off | attack model, output access level, defense setting, privacy budget | P05 |

---

## 6. 논문 간 차별성

| 논문 | 차별성 |
|---|---|
| P01 | AI 원리의 출발점이다. 보안 논문은 아니지만 이후 adversarial/privacy/security 논문의 기술적 배경이 된다. |
| P02 | 모델을 단독 산출물이 아니라 생명주기 전체의 보증 대상으로 본다. W14/W15의 운영·재현성 체계와 직접 연결된다. |
| P03 | 보안 탐지 응용에서 오탐·미탐·데이터셋 편향 문제가 왜 중요한지 보여준다. |
| P04 | 모델 무결성 공격과 방어를 robust accuracy/ASR로 분리해 평가하게 한다. 단, 지정 논문 동일성 확인이 남아 있다. |
| P05 | 모델 출력이 학습 데이터 membership과 민감 속성을 누출할 수 있음을 보여준다. W11 DP/MIA의 선행 연결점이다. |

---

## 7. 기말논문 활용 구조

| 기말논문 장 | W01 반영 내용 |
|---|---|
| 1장 서론 | ML 시스템은 성능뿐 아니라 생명주기 보증, 보안성, 프라이버시, 재현성을 함께 평가해야 한다는 문제의식 |
| 2장 관련연구 | 딥러닝 원리, ML assurance, IDS, adversarial robustness, privacy attack 문헌 정리 |
| 3장 위협모형 | data/model/deployment/alert/privacy 자산과 공격자 능력 정의 |
| 4장 연구방법 | clean utility, detection, robust accuracy, ASR, MI advantage, evidence coverage 지표 설계 |
| 5장 분석 | toy evaluation 또는 문헌 기반 비교를 실제 운영 보증으로 과장하지 않고 한계 제시 |
| 6장 보안적 함의 | MLOps, privacy, robustness, human review, audit evidence 필요성 논의 |

---

## 8. 최종 종합 판단

W01의 5개 문헌은 다음과 같이 연결된다.

```text
P01: 딥러닝 원리와 표현학습
→ P02: ML 생명주기 보증과 evidence chain
→ P03: 보안 탐지 응용과 confusion-matrix 기반 운영 지표
→ P04: 대적공격·강건성 평가
→ P05: 프라이버시 공격과 leakage 평가
```

따라서 W01은 전체 AI 보안 강의의 기준축이다. 이후 W02~W15의 poisoning, computer vision adversarial, LLM security, RAG injection, FL, DP, verification, MLOps는 모두 W01의 **원리-생명주기-탐지-무결성-기밀성** 프레임으로 확장해 해석할 수 있다.
