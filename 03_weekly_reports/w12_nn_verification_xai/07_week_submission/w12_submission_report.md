# W12 제출용 단일 보고서

## 신경망 검증·정형방법 & 대적방어·XAI·강건성 트레이드오프

## 0. 메타정보

| 항목 | 내용 |
|---|---|
| 주차 | W12 |
| 보고서 제목 | 신경망 검증·정형방법 & 대적방어·XAI·강건성 트레이드오프 |
| 과목 범위 | AI 보안 |
| 작성자 | 박영세 |
| 학번 | 26200122 |
| 작성일 | 2026-06-26 |
| 문서 상태 | 주차별 단일 제출용 보고서 |
| 원본 관리 파일 | `03_weekly_reports/w12_nn_verification_xai/07_week_submission/w12_submission_report.md` |
| Word/PDF 제출본 권장 위치 | `03_weekly_reports/w12_nn_verification_xai/07_week_submission/exports/` |
| 관련 산출물 위치 | `03_weekly_reports/w12_nn_verification_xai/` |
| 안전 범위 | 실제 안전중요 시스템 공격, 운영 모델 침해, 개인정보 기반 평가, 악용 가능한 공격 절차 제외 |
| PDF 검토 상태 | P01~P05 로컬 PDF blob 존재 확인. 제출 본문은 공식 DOI/URL, `paper_list.md`, 논문별 summary, 실험 보고서 기준으로 작성 |
| 제출 전 주의 | W12는 로컬 PDF와 강의계획서 지정 논문 간 표기 차이가 많은 주차다. P01은 공식 DOI 기준 Boudardara et al.로 인용하고, P02~P05는 관련 논문/공식 DOI 기준으로 인용하되 최종 제출 전 원문 또는 출판사 페이지 재확인 필요 |

---

## 초록

본 보고서는 W12 주차의 신경망 검증, 정형방법, 대적방어, XAI 안정성, robustness-accuracy-fairness trade-off를 하나의 제출용 보고서로 통합한다. 딥러닝 모델은 clean test data에서 높은 accuracy를 보일 수 있지만, 작은 입력 변화, explanation manipulation, verification scalability failure, group fairness gap, certified/empirical robustness 혼동에 취약할 수 있다. 본 보고서는 W12 논문 5편을 바탕으로 verification abstraction, adversarial attack/defense taxonomy, adversarial XAI, Lipschitz-based robustness, robustness-accuracy-fairness trade-off를 연결한다. 실습은 실제 운영 모델이나 개인정보 없이 synthetic binary classification과 toy logistic classifier를 사용한 안전한 toy protocol로 수행했으며, clean accuracy, robust accuracy, explanation stability, certified rate proxy, fairness gap, verification cost, reproducibility evidence를 분리 기록하였다. `certified_rate`는 toy 선형 모델의 margin bound proxy이므로 대규모 DNN의 formal verification certificate로 해석하지 않는다.

**키워드:** neural network verification, formal methods, abstraction, adversarial robustness, XAI stability, certified robustness, fairness gap, Lipschitz, reproducibility

---

## 1. 한 문장 요약

W12는 AI 보안 평가가 clean accuracy 하나로 끝나지 않으며, 신경망 검증, empirical robustness, explanation stability, fairness gap, verification cost, reproducibility evidence를 함께 보고해야 함을 보여주는 주차다.

---

## 2. 학습 배경과 주차 목표

### 2.1 이번 주 주제의 위치

W12는 W03의 비전 대적공격, W05의 representation/backdoor, W06의 탐지 신뢰성, W11의 privacy claim 검증을 신경망 검증과 설명가능성 관점으로 확장한다. W12의 핵심은 “성능이 높다”와 “안전하게 검증되었다”를 분리하는 것이다. Formal verification은 입력 범위 전체에 대한 명세 만족을 목표로 하지만 비용이 크고 확장성이 어렵다. Empirical robustness는 실제 평가셋에서의 강건성을 보여주지만 완전한 보증은 아니다. XAI 안정성은 설명이 입력 변화에 얼마나 흔들리는지 보여주지만, 설명 안정성이 곧 안전성을 의미하지는 않는다.

### 2.2 강의계획서상 학습목표

- Neural network verification과 abstraction/reachability 기반 검증의 기본 개념을 이해한다.
- Empirical adversarial robustness와 certified robustness의 차이를 구분한다.
- Adversarial XAI와 explanation manipulation 위협모형을 정리한다.
- Lipschitz regularization과 robustness bound의 직관을 이해한다.
- Robustness, accuracy, fairness, verification cost를 동시에 보고하는 평가표를 설계한다.

### 2.3 이번 주 핵심 질문

1. Clean accuracy가 높아도 robust accuracy가 낮다면 보안 평가는 어떻게 해석해야 하는가?
2. Certified rate proxy와 formal verification certificate는 어떻게 구분해야 하는가?
3. Explanation stability가 높은 모델을 곧바로 안전하다고 말할 수 있는가?
4. Robust defense가 fairness gap을 키울 수 있다면 평가 프로토콜은 어떻게 바뀌어야 하는가?
5. W12의 toy protocol을 실제 DNN verification/XAI 평가로 확장하려면 어떤 안전 조건이 필요한가?

---

## 3. 논문 5편의 서술형 종합 요약

### 3.1 P01. A Review of Abstraction Methods Toward Verifying Neural Networks

P01은 neural network verification에서 abstraction 방법을 정리하는 공식 DOI 기준 문헌이다. 신경망 검증은 입력 영역이 특정 perturbation bound 안에 있을 때 출력이 안전 명세를 만족하는지 확인하는 문제다. ReLU network, interval bound, abstract interpretation, reachability analysis, over-approximation은 복잡한 신경망 계산을 검증 가능한 형태로 근사하기 위해 사용된다.

보안 관점에서 P01은 W12의 formal verification 축을 담당한다. Abstraction은 검증 가능성을 높이지만 보수적인 over-approximation으로 인해 false unknown 또는 느슨한 bound를 만들 수 있다. 따라서 verification result는 accuracy와 별도 지표로 기록해야 하며, certificate가 실제로 어떤 입력 범위와 어떤 명세에 대해 유효한지 명시해야 한다. 다만 로컬 PDF는 Meng et al. 2022 관련 보조 문헌이므로 최종 제출 전 공식 Boudardara et al. 원문 또는 출판사 페이지 대조가 필요하다.

### 3.2 P02. Adversarial Attacks and Defenses in Deep Learning: From a Perspective of Cybersecurity

P02는 adversarial attack과 defense taxonomy를 정리하는 관련 문헌이다. 딥러닝 모델은 작은 perturbation으로도 예측이 바뀔 수 있으며, defense는 adversarial training, input preprocessing, detection, certified defense, robust optimization 등으로 분류된다. Robust evaluation은 clean accuracy와 별도로 robust accuracy, ASR, perturbation budget, defense overhead를 기록해야 한다.

보안 관점에서 P02는 empirical robustness 평가의 근거다. 공격 절차 자체를 재현하지 않더라도, 평가 보고서에는 perturbation bound, threat model, robust accuracy, defense condition, false security claim 방지 문구가 포함되어야 한다. 현재 로컬 PDF는 Ren et al. 2020 Engineering 논문이며, 공식 최종 반영표는 Shuai Zhou et al. ACM CSUR DOI 기준 관련 문헌으로 정리한다.

### 3.3 P03. Adversarial Attacks in Explainable Machine Learning: A Survey of Threats Against Models and Humans

P03은 XAI가 공격받을 수 있다는 점을 정리하는 관련 문헌이다. 설명가능성 도구는 모델 판단의 근거를 보여주지만, 공격자는 예측은 유지하면서 explanation만 바꾸거나, explanation이 민감 feature를 드러내도록 만들거나, 사람이 잘못 신뢰하게 만드는 방향으로 조작할 수 있다.

보안 관점에서 P03은 explanation stability 지표의 근거다. AI 보안 보고서에서 XAI를 단순히 “해석 가능”이라고 표현하기보다, 입력 변화 전후의 explanation consistency, attribution shift, human review 가능성, explanation leakage 위험을 함께 기록해야 한다. 로컬 PDF는 Baniecki/Biecek 2023 관련 보조 문헌이므로 공식 Vadillo et al. DOI 기준 원문 확인이 필요하다.

### 3.4 P04. Adversarial Robustness of Neural Networks from the Perspective of Lipschitz Calculus: A Survey

P04는 Lipschitz 관점에서 adversarial robustness를 해석하는 관련 문헌이다. Lipschitz constant는 입력 변화가 출력 변화로 얼마나 증폭될 수 있는지를 제한하는 개념이다. 모델의 Lipschitz bound가 작으면 작은 입력 변화가 출력에 미치는 영향을 제한할 수 있으므로 robustness certificate 또는 margin bound의 직관적 근거가 된다.

보안 관점에서 P04는 certified robustness와 empirical robustness의 차이를 설명하는 데 사용된다. Lipschitz bound는 이론적 안전 근거가 될 수 있지만, 실제 대규모 DNN에서는 tight bound 계산이 어렵고 clean accuracy와 trade-off가 발생할 수 있다. 현재 로컬 PDF는 Finlay et al. 2018 관련 보조 문헌이며, 공식 최종 반영표는 Zuhlke/Kudenko ACM CSUR DOI 기준으로 정리한다.

### 3.5 P05. Triangular Trade-off between Robustness, Accuracy, and Fairness in Deep Neural Networks: A Survey

P05는 robustness, accuracy, fairness 사이의 trade-off를 다루는 관련 문헌이다. 강건성 향상을 위한 defense가 전체 accuracy를 낮추거나 특정 subgroup의 error를 키울 수 있고, fairness constraint가 robust optimization과 충돌할 수 있다. 따라서 AI 보안 평가는 전체 평균 성능뿐 아니라 group-level risk와 fairness gap을 함께 기록해야 한다.

보안 관점에서 P05는 W12의 fairness gap 지표 근거다. 안전한 모델을 주장하려면 clean accuracy, robust accuracy, certified rate뿐 아니라 subgroup별 성능 차이, calibration, fairness gap을 함께 보고해야 한다. 현재 로컬 PDF는 Singh et al. 2021 관련 보조 문헌이고, 공식 최종 반영표는 Li/Guoqiang Li ACM CSUR DOI 기준으로 정리한다.

---

## 4. 논문 간 연결 관계

W12 논문 5편은 다음 흐름으로 연결된다.

```text
Verification abstraction
→ Empirical adversarial attack/defense taxonomy
→ Adversarial XAI와 explanation stability
→ Lipschitz robustness와 certified bound
→ Robustness-accuracy-fairness trade-off
```

P01은 formal verification과 abstraction을 담당한다. P02는 empirical adversarial attack/defense taxonomy를 제공한다. P03은 explanation stability와 adversarial XAI 위험을 확장한다. P04는 Lipschitz 기반 robustness bound를 설명하고, P05는 robustness, accuracy, fairness를 동시에 봐야 하는 이유를 제공한다. 이 다섯 문헌을 종합하면 W12의 핵심 메시지는 “AI 보안 평가는 정확도, 강건성, 검증 보증, 설명 안정성, 공정성을 분리해서 보고해야 한다”는 것이다.

---

## 5. AI 원리 70% 정리

Neural network verification은 입력 집합 전체에 대해 모델이 safety property를 만족하는지 확인하려는 접근이다. Formal verifier는 abstraction, reachability, bound propagation을 사용해 출력 범위를 추정한다. Empirical robustness는 특정 perturbation 또는 test set 조건에서의 성능을 측정한다. XAI stability는 입력 변화 전후 feature attribution의 일관성을 측정한다. Fairness gap은 group별 성능 차이를 기록한다.

### 5.1 핵심 수식

Robustness property는 perturbation ball 안의 입력이 모두 같은 label을 유지하는지로 표현할 수 있다.

$$
\forall x'\in B_{\epsilon}(x),\quad f(x')=f(x)
$$

Robust accuracy는 perturbation 조건에서도 정답을 맞힌 비율이다.

$$
RobustAcc=\frac{N_{rob}}{N_{test}}
$$

Lipschitz bound는 입력 변화와 출력 변화 사이의 상한을 제공한다.

$$
\left\|f(x)-f(x')\right\| \leq L\left\|x-x'\right\|
$$

Explanation stability는 clean attribution과 perturbed attribution의 cosine similarity로 기록할 수 있다.

$$
XAIStability=\frac{a(x)\cdot a(x')}{\left\|a(x)\right\|\left\|a(x')\right\|}
$$

Fairness gap은 group별 accuracy 차이로 기록한다.

$$
FairGap=\left|Acc_{g0}-Acc_{g1}\right|
$$

Certified rate proxy는 toy setting에서 bound 조건을 만족한 sample 비율로 제한해 기록한다.

$$
CertRate=\frac{N_{cert}}{N_{test}}
$$

| 기호 | 의미 |
|---|---|
| $B_{\epsilon}(x)$ | 입력 $x$ 주변 perturbation ball |
| $N_{rob}$ | 교란 조건에서도 정답인 sample 수 |
| $L$ | Lipschitz constant 또는 bound |
| $a(x)$ | 입력 $x$에 대한 attribution vector |
| $Acc_{g0}, Acc_{g1}$ | group별 accuracy |
| $N_{cert}$ | toy bound proxy를 만족한 sample 수 |

### 5.2 핵심 개념과 보안 연결

| 개념 | AI 원리 | 보안 연결 |
|---|---|---|
| Neural network verification | 입력 범위에서 출력 명세 만족 여부 확인 | formal claim 과장 방지 |
| Abstraction | 복잡한 계산을 over-approximation으로 근사 | 검증 가능성·보수성 trade-off |
| Empirical robustness | test perturbation 조건에서 성능 측정 | robust accuracy, ASR |
| Lipschitz regularization | 입력 변화의 출력 증폭 제한 | certified robustness 직관 |
| XAI stability | explanation 변화의 일관성 측정 | explanation manipulation 대응 |
| Fairness gap | group별 성능 차이 측정 | 방어가 subgroup risk를 키우는지 확인 |

---

## 6. 보안 이슈 30% 정리

신경망 검증과 XAI 보안은 모델 예측의 무결성뿐 아니라 설명 결과, 보증의 범위, 공정성 영향, 검증 비용까지 포함한다. Formal certificate가 아닌 proxy를 certificate처럼 주장하면 safety claim이 과장된다. Explanation stability가 높아도 모델이 안전하다는 보장은 아니며, robust defense가 fairness gap을 키울 수도 있다.

| 보안 속성 | W12에서의 의미 | 대표 위협 | 평가 지표 |
|---|---|---|---|
| Integrity | 입력 perturbation으로 예측·설명이 흔들림 | adversarial input, explanation manipulation | robust accuracy, XAI stability |
| Safety | 검증되지 않은 robust behavior를 안전하다고 오해 | unsupported certificate claim | certified rate, limitation note |
| Availability | 검증 비용과 확장성 문제 | verification scalability failure | verification cost |
| Accountability | 설명과 검증 근거를 추적해야 함 | misleading explanation | attribution log, reproducibility |
| Fairness | defense가 subgroup 성능 차이를 키움 | subgroup risk | fairness gap |

---

## 7. Research Track 분석

### 7.1 연구문제

- RQ1. 신경망 검증, XAI 안정성, robustness-accuracy-fairness trade-off를 어떻게 하나의 보안 평가표로 보고할 것인가?
- RQ2. Clean accuracy와 robust accuracy의 차이는 safety claim에 어떤 영향을 주는가?
- RQ3. Certified rate proxy와 formal certificate를 구분하기 위해 어떤 제한 문구와 근거가 필요한가?
- RQ4. Robustness 방어가 fairness gap과 verification cost에 미치는 영향을 어떻게 기록할 것인가?

### 7.2 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | 모델 예측, robustness claim, certificate/proxy, explanation, fairness metric, run log |
| 공격자 목표 | 예측 변경, explanation manipulation, misleading certificate claim, subgroup risk 증가 |
| 공격자 지식 | 모델 구조 일부, 입력 feature, attribution method, perturbation bound 관찰 가능성 |
| 공격자 능력 | small perturbation, explanation-targeted input 변화, subgroup별 취약 조건 유도 |
| 공격 경로 | input → model prediction → explanation → verification/proxy → safety claim |
| 방어자 능력 | robust training, verification bound, XAI stability check, fairness audit, human review |
| 제외 범위 | 실제 안전중요 시스템 공격, 운영 모델 침해, 개인정보 기반 평가, 악용 가능한 공격 절차 |

### 7.3 평가축

| 평가축 | 질문 | 대표 지표 또는 증거 |
|---|---|---|
| Clean performance | 정상 입력에서 성능이 유지되는가 | clean accuracy |
| Empirical robustness | perturbation 조건에서 성능이 유지되는가 | robust accuracy |
| Explanation stability | 입력 변화 전후 설명이 안정적인가 | explanation stability |
| Certified/proxy robustness | bound 조건을 만족하는가 | certified rate proxy |
| Fairness impact | group별 성능 차이가 커지는가 | fairness gap |
| Verification cost | 검증 또는 proxy 계산 비용이 얼마인가 | verification cost ms |
| Reproducibility evidence | 동일 결과를 다시 만들 수 있는가 | seed, config, CSV, JSON, run log |

### 7.4 재현성

재현성을 위해 seed, synthetic data generation, model type, perturbation epsilon, attribution calculation, bound proxy rule, fairness group split, CSV/JSON/Markdown log를 보존한다. W12 실습은 synthetic binary classification과 toy logistic classifier를 사용하고, 실제 운영 모델이나 개인정보를 사용하지 않는다.

---

## 8. 실습 보고서 및 그래프 수치 검증

본 실습은 실제 대규모 DNN formal verification이나 실제 안전중요 시스템 평가가 아니라 W12의 핵심인 보안 평가축을 안전하게 설명하기 위한 최소 toy protocol이다. Synthetic binary classification과 toy logistic classifier를 사용해 clean model, adversarial input, robust defense, XAI stability check 조건을 분리하였다.

### 8.1 실습 설계

| 항목 | 내용 |
|---|---|
| Dataset | synthetic_binary_classification |
| Model | toy_logistic_classifier |
| Perturbation proxy | 선형 모델 가중치 부호 기반 L-infinity perturbation proxy |
| Epsilon | 0.35 |
| Robust defense | adversarial augmentation + stronger regularization |
| XAI stability | clean/perturbed attribution cosine similarity |
| Certified robustness proxy | linear margin bound proxy |
| Fairness metric | synthetic group별 accuracy gap |
| Outputs | `metrics_summary.csv`, `results.json`, `run_log.md` |

### 8.2 실습 결과 수치

| 조건 | Clean Accuracy | Robust Accuracy | Explanation Stability | Certified Rate | Fairness Gap | Verification Cost ms | 해석 |
|---|---:|---:|---:|---:|---:|---:|---|
| Clean model | 0.818750 | 0.543750 | 0.927782 | 0.543750 | 0.039141 | 0.223524 | 정상 성능은 높지만 perturbation에서 강건성이 낮아짐 |
| Adversarial input | 0.818750 | 0.543750 | 0.862321 | 0.340625 | 0.039141 | 0.190324 | 더 강한 perturbation proxy에서 설명 안정성과 bound proxy가 악화됨 |
| Robust defense | 0.815625 | 0.543750 | 0.927152 | 0.543750 | 0.044823 | 0.191790 | 단순 증강 방어만으로 robust accuracy 개선은 제한적 |
| XAI stability check | 0.815625 | 0.696875 | 0.976252 | 0.696875 | 0.044823 | 0.193048 | 완화된 perturbation 조건에서는 설명 안정성과 bound proxy가 개선됨 |

이 결과는 synthetic binary classification 기반 toy 실험의 평가 형식 검증용 수치이다. `toy_logistic_classifier`는 W12의 평가축을 작게 재현하기 위해 선택했으며 실제 대규모 DNN formal verification이나 안전중요 시스템 평가를 대표하지 않는다. `certified_rate`는 선형 모델 margin bound proxy이며 formal verifier가 발급한 certificate가 아니다.

### 8.3 그래프 수치 검증

현재 제출 보고서의 그래프는 `assets/w12_metric_chart.png`를 참조한다. 확인 가능한 SVG 그래프에는 `clean_accuracy`, `robust_accuracy`, `explanation_stability`, `certified_rate`, `fairness_gap`, `verification_cost_ms` 여섯 series가 표시되어 있다.

| 조건 | 그래프 Clean Acc. | 표 Clean Acc. | 그래프 Robust Acc. | 표 Robust Acc. | 그래프 XAI Stability | 표 XAI Stability | 그래프 Cert. Rate | 표 Cert. Rate | 그래프 Fairness Gap | 표 Fairness Gap | 그래프 Cost ms | 표 Cost ms | 확인 결과 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Clean model | 0.818750 | 0.818750 | 0.543750 | 0.543750 | 0.927782 | 0.927782 | 0.543750 | 0.543750 | 0.039141 | 0.039141 | 0.223524 | 0.223524 | 일치 |
| Adversarial input | 0.818750 | 0.818750 | 0.543750 | 0.543750 | 0.862321 | 0.862321 | 0.340625 | 0.340625 | 0.039141 | 0.039141 | 0.190324 | 0.190324 | 일치 |
| Robust defense | 0.815625 | 0.815625 | 0.543750 | 0.543750 | 0.927152 | 0.927152 | 0.543750 | 0.543750 | 0.044823 | 0.044823 | 0.191790 | 0.191790 | 일치 |
| XAI stability check | 0.815625 | 0.815625 | 0.696875 | 0.696875 | 0.976252 | 0.976252 | 0.696875 | 0.696875 | 0.044823 | 0.044823 | 0.193048 | 0.193048 | 일치 |

<!-- submission-metric-chart:start -->
**그림 1. W12 metrics summary chart**

![W12 metrics summary chart](assets/w12_metric_chart.png)

출처: `04_experiment/outputs/metrics_summary.csv`. 이 그래프는 공개 toy/synthetic 산출물 기반이며 실제 공격 성능이나 운영 환경 성능으로 일반화하지 않는다. 현재 그래프는 clean_accuracy, robust_accuracy, explanation_stability, certified_rate, fairness_gap, verification_cost_ms를 시각화한다.
<!-- submission-metric-chart:end -->

---

## 9. 기말논문 연결

W12는 기말논문에서 “강건성·설명안정성·공정성·재현성을 함께 보고하는 AI 보안 평가 프레임워크”로 확장할 수 있다. 핵심 기여 후보는 verification/XAI/trade-off 문헌 비교표, multi-metric evaluation protocol, synthetic toy 실행 로그 기반 재현성 구조다.

| 기말논문 장 | W12 반영 내용 |
|---|---|
| 1장 서론 | 정확도 중심 AI 보안 평가의 한계 제시 |
| 2장 관련연구 | verification abstraction, adversarial defense, XAI attack, Lipschitz robustness, fairness trade-off 문헌 정리 |
| 3장 위협모형 | 예측, 설명, certificate, fairness metric, verification log 보호 자산 정의 |
| 4장 연구방법 | clean/robust accuracy, explanation stability, certified proxy, fairness gap, cost 설계 |
| 5장 분석 | toy condition별 multi-metric 결과 비교 |
| 6장 결론 | AI 보안 claim은 성능·강건성·설명·공정성·검증 비용을 함께 보고해야 함 |

---

## 10. AI 도구 활용 기록

AI 도구는 문헌 요약, 코드 점검, 문장 구조화, 그래프 생성 보조에 사용하였다. 모든 DOI/URL, 실험 수치, 본문 인용, 결론은 작성자가 outputs 파일과 로컬 참고문헌 검증표를 대조하여 검증한다.

| 항목 | 내용 |
|---|---|
| 사용 도구명 | Codex, ChatGPT 계열 도구 |
| 사용 목적 | 문헌 요약 정리, 보고서 구조화, 안전한 toy/synthetic 실험 결과 표기 점검, 그래프 생성 보조, 제출 전 체크리스트 정리 |
| AI 산출물 반영 위치 | `07_week_submission/w12_submission_report.md`, `07_week_submission/assets/w12_metric_chart.png`, `05_ai_worklog/ai_disclosure_draft.md` |
| 본인 수정 내용 | 주차별 문헌 상태 확인, 실험 수치와 outputs 대조, 안전 범위와 한계 문장 확인, 최종 제출 전 미확정 문헌 분리 |
| 사실관계 검증 방법 | `01_papers/paper_list.md`, `01_papers/doi_check.md`, 강의계획서 문헌표 대조 |
| 실험결과 검증 방법 | `04_experiment/experiment_report.md`, `04_experiment/outputs/metrics_summary.csv`, `results.json`, `run_log.md`의 수치와 보고서 표기 대조 |
| 최종 책임 확인 | AI 산출물은 초안 보조이며 최종 제출자는 원고 내용, 인용, 실험결과, 연구윤리 책임을 확인한다. |

---

## 11. 제출 전 자기 점검표

| 점검 항목 | 상태 | 비고 |
|---|---|---|
| 메타정보 작성 | 완료 | 작성일 2026-06-26 반영 |
| 초록 및 키워드 작성 | 완료 |  |
| AI 원리 70% 정리 | 완료 | 핵심 수식 추가 |
| 보안 이슈 30% 정리 | 완료 |  |
| 논문 5편 서술형 요약 | 완료 |  |
| 논문 간 연결 관계 작성 | 완료 |  |
| Research Track 5요소 작성 | 완료 | 연구문제, 위협모형, 평가방법, 재현성, 한계 |
| P01~P05 PDF blob 확인 | 완료 | GitHub 파일 존재 확인. 원문 PDF 저작권/배포 정책 별도 검토 필요 |
| P01 공식 DOI 검증 | 완료 / 확인 필요 | 로컬 PDF는 Meng et al. 관련 보조 문헌 |
| P02 공식 DOI 검증 | 완료 / 확인 필요 | 로컬 PDF는 Ren et al. 2020, 공식 최종 반영표는 Shuai Zhou et al. |
| P03 공식 DOI 검증 | 완료 / 확인 필요 | 로컬 PDF는 Baniecki/Biecek 관련 보조 문헌 |
| P04 공식 DOI 검증 | 완료 / 확인 필요 | 로컬 PDF는 Finlay et al. 관련 보조 문헌 |
| P05 공식 DOI 검증 | 완료 / 확인 필요 | 로컬 PDF는 Singh et al. 관련 보조 문헌 |
| certified_rate proxy 한계 | 완료 | formal DNN verification certificate 아님 |
| 실험 outputs 파일 존재 확인 | 완료 | 실험 보고서 기준 CSV/JSON/run_log 존재 |
| 실험 결과와 보고서 수치 일치 | 완료 | 실험 보고서 수치 기준 반영 |
| 그래프 수치 확인 | 완료 | 6개 series 기준 표와 일치 |
| AI 활용 고지 작성 | 완료 |  |
| DOCX/PDF 제출본 생성 | 필요 | `07_week_submission/exports/` 권장 |
| 최종 사람이 검토할 항목 표시 | 완료 | 지정 논문/관련 보조 문헌 차이, PDF 보관 정책, Word/PDF 렌더링 |

---

## 12. 참고문헌 검증표

| 번호 | 참고문헌 | DOI/URL | 상태 | 비고 |
|---:|---|---|---|---|
| [1] | Fateh Boudardara et al., “A Review of Abstraction Methods Toward Verifying Neural Networks,” ACM Transactions on Embedded Computing Systems, 2024 | `https://doi.org/10.1145/3617508` | 공식 DOI 확인 | 로컬 PDF는 Meng et al. 관련 보조 문헌 |
| [2] | Shuai Zhou et al., “Adversarial Attacks and Defenses in Deep Learning: From a Perspective of Cybersecurity,” ACM Computing Surveys, 2022 | `https://doi.org/10.1145/3547330` | 공식 DOI 확인 | 로컬 PDF는 Ren et al. 2020 관련 문헌 |
| [3] | Jon Vadillo et al., “Adversarial Attacks in Explainable Machine Learning: A Survey of Threats Against Models and Humans,” WIREs Data Mining and Knowledge Discovery, 2024 | `https://doi.org/10.1002/widm.1567` | 공식 DOI 확인 | 로컬 PDF는 Baniecki/Biecek 관련 보조 문헌 |
| [4] | Monty-Maximilian Zuhlke, Daniel Kudenko, “Adversarial Robustness of Neural Networks from the Perspective of Lipschitz Calculus: A Survey,” ACM Computing Surveys, 2025 | `https://doi.org/10.1145/3648351` | 공식 DOI 확인 | 로컬 PDF는 Finlay et al. 관련 보조 문헌 |
| [5] | Jingyang Li, Guoqiang Li, “Triangular Trade-off between Robustness, Accuracy, and Fairness in Deep Neural Networks: A Survey,” ACM Computing Surveys, 2025 | `https://doi.org/10.1145/3645088` | 공식 DOI 확인 | 로컬 PDF는 Singh et al. 관련 보조 문헌 |

---

## 13. 부록 A. KCI 논문 형식 전환 아이디어

### A.1 제목 후보

| 번호 | 국문 제목 후보 | 영문 제목 후보 | 예상 기여 |
|---:|---|---|---|
| 1 | 신경망 검증과 XAI 안정성을 고려한 AI 보안 다중지표 평가 프레임워크 연구 | A Multi-Metric AI Security Evaluation Framework Considering Neural Network Verification and XAI Stability | 정확도 중심 보고 한계 보완 |
| 2 | AI 모델 보안 평가에서 강건성·설명안정성·공정성의 통합 보고체계 연구 | An Integrated Reporting Framework for Robustness, Explanation Stability, and Fairness in AI Security Evaluation | multi-metric checklist |
| 3 | Certified Robustness Proxy와 Formal Verification Claim 구분을 위한 AI 보안 보고 기준 연구 | A Reporting Standard for Separating Certified Robustness Proxies from Formal Verification Claims | certificate 과장 방지 |

추천 제목은 “신경망 검증과 XAI 안정성을 고려한 AI 보안 다중지표 평가 프레임워크 연구”이다. 국문초록은 verification/XAI/trade-off 문헌 비교와 synthetic toy 실험을 통해 clean accuracy, robust accuracy, explanation stability, certified proxy, fairness gap, verification cost를 분리 보고하는 구조로 구성한다.

### A.2 연구문제

- RQ1. AI 보안 평가에서 강건성, 설명안정성, 공정성, 재현성을 함께 보고하는 최소 지표는 무엇인가?
- RQ2. Certified rate proxy와 formal certificate를 구분하기 위한 보고 기준은 무엇인가?
- RQ3. Robustness defense가 fairness gap과 verification cost에 미치는 영향을 어떻게 해석해야 하는가?

---

## 14. 부록 B. SCI 논문 형식 전환 아이디어

SCI 제목 후보는 “A Multi-Metric Security Evaluation Framework for Neural Network Verification and XAI Stability”이다.

Structured abstract는 Background, Problem, Method, Results, Contribution, Implications로 구성한다. 결과 문장은 W12 toy evaluation이 clean accuracy, robust accuracy, explanation stability, certified proxy, fairness gap, verification cost를 분리 기록했다는 수준으로 제한한다. 실제 대규모 DNN formal verification 또는 safety-critical certification으로 일반화하지 않는다.

| 연구축 | 대표 논문 | 역할 |
|---|---|---|
| Verification abstraction | Boudardara et al. | abstraction, reachability, verification certificate |
| Adversarial attack/defense | Zhou et al. | adversarial objective, robust accuracy, defense taxonomy |
| Adversarial XAI | Vadillo et al. | explanation stability와 explanation attack |
| Lipschitz robustness | Zuhlke and Kudenko | Lipschitz bound, robust margin |
| Robustness-accuracy-fairness | Li and Li | trade-off, subgroup risk, fairness gap |

---

## 15. 부록 C. 제출 파일 위치와 변환 권장

| 파일 | 설명 |
|---|---|
| `07_week_submission/w12_submission_report.md` | 본 제출용 보고서 원본 |
| `07_week_submission/assets/w12_metric_chart.png` | 제출 보고서 그래프 |
| `04_experiment/experiment_report.md` | 실험 근거 보고서 |
| `04_experiment/outputs/` | 실험 결과 근거 파일 위치 |
| `05_ai_worklog/ai_disclosure_draft.md` | AI 활용 고지 근거 |

Word 제출본은 다음 위치에 생성해 관리한다.

```text
03_weekly_reports/w12_nn_verification_xai/07_week_submission/exports/w12_submission_report.docx
```

PDF 제출본은 Word에서 최종 육안 검수 후 다음 위치에 저장한다.

```text
03_weekly_reports/w12_nn_verification_xai/07_week_submission/exports/w12_submission_report.pdf
```

수식은 GitHub와 Word 변환을 모두 고려하여 Markdown 표 안에 넣지 않고, `$$...$$` block math로 유지한다.
