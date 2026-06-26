# W11 제출용 단일 보고서

## 차등프라이버시(DP) & 멤버십 추론 공격·방어

## 0. 메타정보

| 항목 | 내용 |
|---|---|
| 주차 | W11 |
| 보고서 제목 | 차등프라이버시(DP) & 멤버십 추론 공격·방어 |
| 과목 범위 | AI 보안 |
| 작성자 | 박영세 |
| 학번 | 26200122 |
| 작성일 | 2026-06-26 |
| 문서 상태 | 주차별 단일 제출용 보고서 |
| 원본 관리 파일 | `03_weekly_reports/w11_differential_privacy_mi/07_week_submission/w11_submission_report.md` |
| Word/PDF 제출본 권장 위치 | `03_weekly_reports/w11_differential_privacy_mi/07_week_submission/exports/` |
| 관련 산출물 위치 | `03_weekly_reports/w11_differential_privacy_mi/` |
| 안전 범위 | 실제 개인정보, 실제 운영 모델/API, 실제 개인 대상 membership inference, 무단 privacy probing 제외 |
| PDF 검토 상태 | P01~P05 로컬 PDF blob 존재 확인. 제출 본문은 DOI/URL, `paper_list.md`, 논문별 summary, 실험 보고서 기준으로 작성 |
| 제출 전 주의 | P03/P05는 로컬 PDF가 지정 논문과 다른 관련 보조 문헌 상태이므로 최종 제출 전 지정 논문 원문 확보 필요. `epsilon_proxy`는 formal privacy accountant 값이 아님 |

---

## 초록

본 보고서는 W11 주차의 차등프라이버시(Differential Privacy, DP)와 membership inference 공격·방어를 하나의 제출용 보고서로 통합한다. DP는 인접 데이터셋에서 한 레코드의 포함 여부가 모델 출력 분포에 미치는 영향을 제한하는 privacy 개념이지만, 실제 ML/DL 연구에서 epsilon, delta, privacy accounting, utility drop, membership inference risk, 재현성 근거가 함께 보고되지 않으면 privacy claim이 과장될 수 있다. 본 보고서는 W11 논문 5편을 바탕으로 DP misuse, centralized DP-DL, DP deep learning survey, membership inference attack taxonomy, membership inference defense taxonomy를 연결하고, synthetic binary classification과 toy logistic regression을 사용한 안전한 toy protocol로 accuracy, train accuracy, MI attack accuracy, epsilon proxy, utility drop, privacy leakage score, noise multiplier, reproducibility evidence를 분리 기록하였다. 실험 결과는 실제 개인정보 보호 수준, 실제 운영 모델의 membership inference 위험, formal DP-SGD 보장, formal privacy accounting 결과를 의미하지 않으며 평가 구조를 설명하는 안전한 예시로 한정한다.

**키워드:** differential privacy, DP-SGD, membership inference, privacy claim, privacy accounting, epsilon, utility drop, leakage score, reproducibility

---

## 1. 한 문장 요약

W11은 DP와 membership inference 방어가 적용 여부만으로 privacy claim을 보장하지 않으며, epsilon/accounting, utility, MI risk, leakage score, 재현성 증거를 함께 보고해야 함을 보여주는 주차다.

---

## 2. 학습 배경과 주차 목표

### 2.1 이번 주 주제의 위치

W11은 W10의 연합학습 privacy leakage 논의를 DP와 membership inference 평가로 확장한다. W10에서 local update와 aggregation 단계의 privacy risk를 다루었다면, W11은 privacy claim 자체가 어떤 근거를 갖고 검증되어야 하는지 다룬다. DP는 강력한 이론적 개념이지만, 실제 연구 보고서에서는 epsilon, delta, clipping, noise scale, accountant, utility drop, membership inference residual risk가 함께 제시되어야 한다.

### 2.2 강의계획서상 학습목표

- DP의 epsilon/delta 정의와 인접 데이터셋 개념을 이해한다.
- DP-SGD의 gradient clipping, noise injection, privacy accounting 구조를 정리한다.
- Membership inference attack의 black-box/white-box/gray-box 위협모형을 이해한다.
- MI defense의 utility-privacy trade-off를 accuracy, leakage, calibration 관점에서 정리한다.
- Safe toy 실험을 통해 utility와 privacy risk proxy를 분리 보고한다.

### 2.3 이번 주 핵심 질문

1. DP claim은 왜 epsilon 하나만으로 충분하지 않은가?
2. Formal accountant 없이 `epsilon_proxy`를 사용할 때 어떤 연구윤리적 한계가 있는가?
3. MI attack accuracy와 privacy leakage score는 왜 함께 봐야 하는가?
4. Utility drop이 작다고 privacy risk가 반드시 낮아지는가?
5. P03/P05처럼 로컬 PDF와 공식 지정 논문이 다를 때 보고서 인용은 어떻게 관리해야 하는가?

---

## 3. 논문 5편의 서술형 종합 요약

### 3.1 P01. A Critical Review on the Use (and Misuse) of Differential Privacy in Machine Learning

P01은 DP claim의 오용과 reporting 책임을 비판적으로 정리하는 문헌이다. DP는 강력한 수학적 privacy guarantee이지만, epsilon 값만 제시하거나, 적용 단위가 sample-level인지 user-level인지 명확히 하지 않거나, privacy accountant와 utility trade-off를 누락하면 실제 보호 수준을 과장할 수 있다.

보안 관점에서 P01은 W11의 privacy claim checklist 근거다. AI 보안 보고서에서 “DP 적용”이라고 쓰려면 적용 위치, 인접 데이터셋 정의, clipping 기준, noise scale, accountant, epsilon/delta, utility drop, residual attack risk를 함께 명시해야 한다. 그렇지 않으면 privacy label은 있지만 검증 가능한 privacy evidence는 없는 상태가 된다.

### 3.2 P02. Recent Advances of Differential Privacy in Centralized Deep Learning: A Systematic Survey

P02는 중앙집중형 deep learning에서 DP 적용 흐름을 정리한다. 대표 방식은 DP-SGD이며, 각 mini-batch에서 per-sample gradient를 clipping하고 noise를 추가한 뒤 privacy accountant로 누적 privacy loss를 계산한다. 이 과정은 모델 utility, training stability, batch size, clipping norm, noise multiplier, accountant choice에 영향을 받는다.

보안 관점에서 P02는 DP-SGD와 privacy auditing의 실무적 평가 기준을 제공한다. 단순히 noise를 추가했다고 DP가 보장되는 것이 아니며, formal privacy accounting이 필요하다. 강의자료의 `Jonathan Demelius` 표기는 공식 메타데이터와 맞지 않고, 현재 확인 가능한 공식 저자는 Lea Demelius, Roman Kern, Andreas Trugler로 기록한다.

### 3.3 P03. Differential privacy in deep learning: A literature survey

P03은 공식 DOI 기준 deep learning에서 DP를 다루는 문헌으로 정리한다. Deep learning에서는 sample-level DP, user-level DP, client-level DP, centralized DP, federated DP 등 적용 단위와 위협모형이 다양하다. DP를 적용해도 utility drop, calibration shift, convergence instability, residual membership inference risk는 남을 수 있다.

보안 관점에서 P03은 W11의 DP deep learning 관련연구 축을 담당한다. 다만 현재 로컬 PDF는 Fu et al.의 differentially private federated learning review로, 공식 DOI 기준 Pan et al. 논문 원문과 다르다. 따라서 보고서 본문과 참고문헌은 공식 DOI 기준으로 작성하되, 최종 제출 전 지정 논문 PDF 또는 출판사 원문을 확보해야 한다.

### 3.4 P04. Membership Inference Attacks on Machine Learning: A Survey

P04는 membership inference attack taxonomy를 정리하는 핵심 보안 문헌이다. Membership inference는 특정 record가 모델 학습 데이터에 포함되었는지를 output confidence, loss, prediction vector, shadow model, white-box gradient/logit signal 등을 통해 추론하는 공격이다. 공격자는 black-box, gray-box, white-box 지식 수준에 따라 서로 다른 공격 신호를 사용할 수 있다.

보안 관점에서 P04는 W11의 핵심 위협모형 근거다. 모델이 train data에 과적합하거나 confidence score가 과도하게 뚜렷하면 membership inference risk가 커질 수 있다. 따라서 train accuracy, test accuracy, generalization gap, MI attack accuracy, leakage score를 함께 기록해야 한다.

### 3.5 P05. Defenses to Membership Inference Attacks: A Survey

P05는 membership inference defense taxonomy를 정리한다. 방어는 regularization, confidence masking, output perturbation, label-only prediction, adversarial regularization, differential privacy, calibration, ensemble, early stopping 등으로 구성될 수 있다. 방어는 privacy risk를 낮출 수 있지만 동시에 utility drop과 calibration change를 만들 수 있다.

보안 관점에서 P05는 MI defense를 평가할 때 단일 방어 적용 여부가 아니라 defense gain, utility loss, leakage reduction, residual risk를 함께 보고해야 함을 보여준다. 다만 현재 로컬 PDF는 Bai et al.의 federated learning membership inference survey로, 공식 DOI 기준 Li Hu et al. 논문 원문과 다르다. 최종 제출 전 지정 원문 확보 또는 관련 보조 문헌 표기를 명확히 해야 한다.

---

## 4. 논문 간 연결 관계

W11 논문 5편은 다음 흐름으로 연결된다.

```text
DP claim misuse와 reporting 책임
→ Centralized DP-DL와 DP-SGD/accounting
→ DP in deep learning 적용 범위
→ Membership inference attack taxonomy
→ Membership inference defense와 utility-privacy trade-off
```

P01은 DP claim의 오용을 방지하는 reporting 기준을 제시한다. P02는 DP-SGD와 privacy accountant의 실무 구조를 제공한다. P03은 deep learning에서 DP 적용 범위와 trade-off를 확장한다. P04는 membership inference 위협모형을 제공하고, P05는 defense taxonomy와 utility loss를 정리한다. 이 다섯 문헌을 종합하면 W11의 핵심 메시지는 “privacy claim은 이론적 보장, 공격 위험, utility, 재현성 증거를 함께 제시할 때만 검증 가능하다”는 것이다.

---

## 5. AI 원리 70% 정리

DP는 한 record의 포함 여부가 알고리즘 출력 분포에 주는 영향을 제한한다. DP-SGD는 gradient clipping과 noise injection을 통해 training 과정에서 privacy loss를 제한하려 하지만, formal accountant 없이는 실제 epsilon을 주장할 수 없다. Membership inference는 모델 confidence, loss, prediction pattern을 이용해 train membership을 추정한다. 따라서 W11에서는 DP 적용 여부와 MI 위험을 분리하지 않고 함께 평가한다.

### 5.1 핵심 수식

Differential privacy의 기본 정의는 인접 데이터셋 $D$와 $D'$에 대해 다음과 같이 표현한다.

$$
Pr[M(D)\in S] \leq e^{\epsilon}Pr[M(D')\in S]+\delta
$$

| 기호 | 의미 |
|---|---|
| $M$ | randomized mechanism |
| $D,D'$ | 하나의 record만 다른 adjacent datasets |
| $S$ | 가능한 출력 event 집합 |
| $\epsilon$ | privacy loss upper bound |
| $\delta$ | 작은 실패 확률 |

DP-SGD에서는 per-sample gradient를 clipping한 뒤 noise를 추가한다.

$$
\bar{g}_i=g_i\cdot \min\left(1,\frac{C}{\left\|g_i\right\|_2}\right)
$$

$$
\tilde{g}=\frac{1}{B}\left(\sum_{i=1}^{B}\bar{g}_i+\mathcal{N}(0,\sigma^2C^2I)\right)
$$

Membership inference attack accuracy는 member/non-member 판별 정확도로 기록한다.

$$
MIAcc=\frac{TP_m+TN_m}{N_m+N_{nm}}
$$

Privacy leakage score는 toy protocol에서 member confidence와 non-member confidence의 차이로 기록한다.

$$
LeakScore=\left|Conf_{member}-Conf_{nonmember}\right|
$$

Utility drop은 baseline accuracy 대비 방어 조건의 성능 하락으로 기록한다.

$$
UtilityDrop=Acc_{base}-Acc_{def}
$$

| 기호 | 의미 |
|---|---|
| $g_i$ | $i$번째 sample gradient |
| $C$ | clipping norm |
| $B$ | batch size |
| $\sigma$ | noise multiplier |
| $TP_m$ | member를 member로 맞힌 수 |
| $TN_m$ | non-member를 non-member로 맞힌 수 |
| $N_m$ | member sample 수 |
| $N_{nm}$ | non-member sample 수 |

### 5.2 핵심 개념과 보안 연결

| 개념 | AI 원리 | 보안 연결 |
|---|---|---|
| Differential Privacy | adjacent dataset 출력 분포 차이 제한 | privacy claim의 수학적 근거 |
| DP-SGD | gradient clipping + noise addition | formal accountant 없이는 보장 주장 불가 |
| Privacy accountant | 누적 privacy loss 계산 | epsilon/delta 보고 필수 |
| Membership inference | 출력 confidence로 학습 포함 여부 추론 | overfitting과 output leakage 위험 |
| MI defense | regularization, masking, DP, calibration | utility-privacy trade-off 발생 |
| Privacy claim checklist | epsilon, utility, risk, 재현성 동시 보고 | 과장된 privacy claim 방지 |

---

## 6. 보안 이슈 30% 정리

Membership inference attack은 모델 출력이나 confidence score로 학습 데이터 포함 여부를 추론한다. Membership inference 방어는 privacy risk를 낮출 수 있지만 utility drop과 calibration 변화를 함께 고려해야 한다. 본 보고서는 실제 개인정보, 실제 개인 대상 membership inference, 운영 모델/API 무단 질의, 실제 서비스 privacy probing을 포함하지 않는다.

| 보안 속성 | W11에서의 의미 | 대표 위협 | 평가 지표 |
|---|---|---|---|
| Confidentiality | 학습 데이터 포함 여부와 민감 속성 노출 | membership inference, confidence leakage | MI attack accuracy, leakage score |
| Integrity | privacy claim의 검증 가능성 훼손 | accountant 누락, epsilon 오용 | reporting checklist |
| Utility | privacy 방어로 성능 저하 | excessive noise, over-regularization | accuracy, utility drop |
| Accountability | privacy claim 재현 가능성 | seed/config/accountant 누락 | reproducibility evidence |
| Compliance | 개인정보 보호 주장과 실제 증거 불일치 | unverifiable privacy claim | epsilon/delta/accounting report |

---

## 7. Research Track 분석

### 7.1 연구문제

- RQ1. Privacy claim 검증을 위해 어떤 최소 지표를 함께 보고해야 하는가?
- RQ2. DP-like noise 조건에서 utility, MI attack accuracy, leakage score는 어떻게 달라지는가?
- RQ3. `epsilon_proxy`와 formal DP accountant 값은 어떻게 구분해야 하는가?
- RQ4. P03/P05처럼 로컬 PDF와 공식 지정 문헌이 다를 때 인용과 증거 관리는 어떻게 해야 하는가?

### 7.2 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | 학습 데이터 포함 여부, 모델 confidence, training log, privacy claim, accountant report |
| 공격자 목표 | 특정 record의 train membership 추론, confidence gap 이용, privacy claim 과장 유도 |
| 공격자 지식 | black-box output 관찰, gray-box evaluator, 내부 auditor |
| 공격자 능력 | model query, output confidence 관찰, shadow/proxy threshold 평가 |
| 공격 경로 | train/test split → model confidence → membership signal → privacy claim 검증 실패 |
| 방어자 능력 | DP-SGD, clipping/noise, accountant, output restriction, calibration, regularization |
| 제외 범위 | 실제 개인정보 사용, 실제 개인 대상 공격, 운영 API 무단 질의, 실제 privacy probing |

### 7.3 평가축

| 평가축 | 질문 | 대표 지표 또는 증거 |
|---|---|---|
| Utility | 모델 성능이 유지되는가 | accuracy, train accuracy |
| Membership inference risk | train membership 추정이 가능한가 | MI attack accuracy |
| Privacy leakage | confidence gap이 남는가 | privacy leakage score |
| DP/accounting | privacy claim이 formal하게 계산되었는가 | epsilon, delta, accountant |
| Defense cost | 방어로 성능이 얼마나 하락하는가 | utility drop |
| Reproducibility evidence | 동일 결과를 다시 만들 수 있는가 | seed, config, CSV, JSON, run log |

### 7.4 재현성

재현성을 위해 seed, synthetic data generation, train/test split, noise multiplier, epsilon proxy, model setting, CSV/JSON/Markdown log를 보존한다. W11 실습은 synthetic binary classification을 사용하고, 실제 개인정보나 실제 운영 모델을 사용하지 않는다.

---

## 8. 실습 보고서 및 그래프 수치 검증

본 실습은 실제 개인정보나 실제 운영 모델을 대상으로 한 membership inference 공격 재현이 아니라 W11의 핵심인 privacy claim 평가축을 안전하게 설명하기 위한 최소 toy protocol이다. Synthetic binary classification과 toy logistic regression을 사용하되, 평가 구조는 이후 formal DP-SGD, privacy accountant, membership inference benchmark에도 확장 가능하도록 accuracy, train accuracy, MI attack accuracy, privacy leakage score, utility drop, epsilon/accounting, reproducibility evidence로 분리하였다.

### 8.1 실습 설계

| 항목 | 내용 |
|---|---|
| Dataset | Synthetic binary classification |
| Model | Toy logistic regression |
| Conditions | Non-DP baseline, DP-like noise low/medium/high |
| DP-like mechanism | clipped gradient + toy Gaussian noise |
| MI evaluation | member/non-member confidence threshold 비교 |
| Leakage proxy | mean member confidence와 mean non-member confidence 차이 |
| Output files | `metrics_summary.csv`, `results.json`, `run_log.md` |

### 8.2 실습 결과 수치

| 조건 | Accuracy | Train Accuracy | MI Attack Accuracy | Epsilon Proxy | Utility Drop | Privacy Leakage Score | Noise Multiplier | 해석 |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Non-DP baseline | 0.956250 | 0.965625 | 0.515625 | 해당 없음 | 0.000000 | 0.014833 | 0.000000 | 기준 조건 |
| DP-like noise low | 0.956250 | 0.965625 | 0.515625 | 8.000000 | 0.000000 | 0.014494 | 0.100000 | 낮은 toy noise 조건 |
| DP-like noise medium | 0.962500 | 0.965625 | 0.512500 | 3.000000 | 0.000000 | 0.011769 | 0.450000 | leakage proxy가 가장 낮게 기록됨 |
| DP-like noise high | 0.950000 | 0.962500 | 0.521875 | 1.000000 | 0.006250 | 0.016482 | 1.200000 | utility drop 발생, MI proxy는 단조 개선되지 않음 |

본 toy 결과에서는 medium noise 조건에서 leakage proxy가 가장 낮게 기록되었고, high noise 조건은 accuracy가 0.006250 낮아졌지만 MI attack accuracy는 오히려 높게 나타났다. 이는 noise를 키웠다고 항상 privacy proxy가 단조롭게 개선되는 것은 아니며, 실제 DP 보장을 주장하려면 accountant와 반복 실험이 필요하다는 점을 보여준다.

### 8.3 그래프 수치 검증

현재 제출 보고서의 그래프는 `assets/w11_metric_chart.png`를 참조한다. 확인 가능한 SVG 그래프에는 `accuracy`, `mi_attack_accuracy`, `epsilon_proxy`, `privacy_leakage_score`, `utility_drop`, `noise_multiplier` 여섯 series가 표시되어 있다. Train accuracy는 표에는 포함하지만 현재 그래프 series에는 포함되어 있지 않다.

| 조건 | 그래프 Accuracy | 표 Accuracy | 그래프 MI Acc. | 표 MI Acc. | 그래프 Epsilon Proxy | 표 Epsilon Proxy | 그래프 Leakage | 표 Leakage | 그래프 Utility Drop | 표 Utility Drop | 그래프 Noise | 표 Noise | 확인 결과 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Non-DP baseline | 0.956250 | 0.956250 | 0.515625 | 0.515625 | 해당 없음 | 해당 없음 | 0.014833 | 0.014833 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 일치 |
| DP-like noise low | 0.956250 | 0.956250 | 0.515625 | 0.515625 | 8.000000 | 8.000000 | 0.014494 | 0.014494 | 0.000000 | 0.000000 | 0.100000 | 0.100000 | 일치 |
| DP-like noise medium | 0.962500 | 0.962500 | 0.512500 | 0.512500 | 3.000000 | 3.000000 | 0.011769 | 0.011769 | 0.000000 | 0.000000 | 0.450000 | 0.450000 | 일치 |
| DP-like noise high | 0.950000 | 0.950000 | 0.521875 | 0.521875 | 1.000000 | 1.000000 | 0.016482 | 0.016482 | 0.006250 | 0.006250 | 1.200000 | 1.200000 | 일치 |

<!-- submission-metric-chart:start -->
**그림 1. W11 metrics summary chart**

![W11 metrics summary chart](assets/w11_metric_chart.png)

출처: `04_experiment/outputs/metrics_summary.csv`. 이 그래프는 공개 toy/synthetic 산출물 기반이며 실제 공격 성능이나 운영 환경 성능으로 일반화하지 않는다. 현재 그래프는 accuracy, mi_attack_accuracy, epsilon_proxy, privacy_leakage_score, utility_drop, noise_multiplier를 시각화한다.
<!-- submission-metric-chart:end -->

---

## 9. 기말논문 연결

W11은 기말논문에서 “AI 보안 연구에서 Privacy Claim 검증을 위한 다중지표 평가 프레임워크”로 발전 가능하다. 핵심 기여는 accuracy, train accuracy, MI attack accuracy, privacy leakage score, utility drop, epsilon/accounting, reproducibility evidence를 분리 보고하는 구조이다.

| 기말논문 장 | W11 반영 내용 |
|---|---|
| 1장 서론 | privacy claim이 단일 epsilon 또는 DP 적용 여부만으로 검증되지 않는다는 문제의식 |
| 2장 관련연구 | DP misuse, centralized DP-DL, DP deep learning, MI attack, MI defense 문헌 정리 |
| 3장 위협모형 | member/non-member, confidence leakage, privacy claim overstatement 정의 |
| 4장 연구방법 | accuracy, MI attack accuracy, leakage score, utility drop, accounting evidence 설계 |
| 5장 분석 | Non-DP와 DP-like noise 조건별 toy result 비교 |
| 6장 결론 | privacy claim은 utility·risk·accounting·재현성을 함께 제시해야 함 |

---

## 10. AI 도구 활용 기록

AI 도구는 문헌 요약, 코드 점검, 문장 구조화, 그래프 생성 보조에 사용하였다. 모든 DOI/URL, 실험 수치, 본문 인용, 결론은 작성자가 outputs 파일과 로컬 참고문헌 검증표를 대조하여 검증한다.

| 항목 | 내용 |
|---|---|
| 사용 도구명 | Codex, ChatGPT 계열 도구 |
| 사용 목적 | 문헌 요약 정리, 보고서 구조화, 안전한 toy/synthetic 실험 결과 표기 점검, 그래프 생성 보조, 제출 전 체크리스트 정리 |
| AI 산출물 반영 위치 | `07_week_submission/w11_submission_report.md`, `07_week_submission/assets/w11_metric_chart.png`, `05_ai_worklog/ai_disclosure_draft.md` |
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
| P01/P02/P04 DOI 검증 | 완료 / 확인 필요 | 로컬 PDF는 arXiv/preprint 판본 가능성 |
| P03 지정 논문 원문 확보 | 확인 필요 | 현재 로컬 PDF는 관련 보조 문헌 원문 |
| P05 지정 논문 원문 확보 | 확인 필요 | 현재 로컬 PDF는 관련 보조 문헌 원문 |
| epsilon_proxy 한계 명시 | 완료 | formal privacy accountant 아님 |
| 실험 outputs 파일 존재 확인 | 완료 | 실험 보고서 기준 CSV/JSON/run_log 존재 |
| 실험 결과와 보고서 수치 일치 | 완료 | 실험 보고서 수치 기준 반영 |
| 그래프 수치 확인 | 완료 | accuracy/MI acc./epsilon proxy/leakage/utility/noise 기준 표와 일치 |
| AI 활용 고지 작성 | 완료 |  |
| DOCX/PDF 제출본 생성 | 필요 | `07_week_submission/exports/` 권장 |
| 최종 사람이 검토할 항목 표시 | 완료 | P03/P05 원문 확보, PDF 보관 정책, Word/PDF 렌더링 |

---

## 12. 참고문헌 검증표

| 번호 | 참고문헌 | DOI/URL | 상태 | 비고 |
|---:|---|---|---|---|
| [1] | Alberto Blanco-Justicia et al., “A Critical Review on the Use (and Misuse) of Differential Privacy in Machine Learning,” ACM Computing Surveys, 2022/2023 | `https://doi.org/10.1145/3547139`; arXiv `https://arxiv.org/abs/2206.04621` | DOI 확인 | 로컬 PDF는 arXiv v2 |
| [2] | Lea Demelius, Roman Kern, Andreas Trugler, “Recent Advances of Differential Privacy in Centralized Deep Learning: A Systematic Survey,” ACM Computing Surveys, 2025 | `https://doi.org/10.1145/3712000`; arXiv `https://arxiv.org/abs/2309.16398` | DOI 확인 | 강의자료 `Jonathan Demelius` 표기 확인 필요 |
| [3] | Ke Pan et al., “Differential privacy in deep learning: A literature survey,” Neurocomputing, 2024 | `https://doi.org/10.1016/j.neucom.2024.127663` | DOI 확인 | 현재 로컬 PDF와 공식 지정 논문이 다름. 지정 원문 확보 필요 |
| [4] | Hongsheng Hu et al., “Membership Inference Attacks on Machine Learning: A Survey,” ACM Computing Surveys, 2022 | `https://doi.org/10.1145/3523273`; arXiv `https://arxiv.org/abs/2103.07853` | DOI 확인 | 로컬 PDF는 arXiv/ACM preprint |
| [5] | Li Hu et al., “Defenses to Membership Inference Attacks: A Survey,” ACM Computing Surveys, 2023/2024 | `https://doi.org/10.1145/3620667` | DOI 확인 | 현재 로컬 PDF와 공식 지정 논문이 다름. 지정 원문 확보 필요 |

---

## 13. 부록 A. KCI 논문 형식 전환 아이디어

### A.1 제목 후보

| 번호 | 국문 제목 후보 | 영문 제목 후보 | 예상 기여 |
|---:|---|---|---|
| 1 | AI 보안 연구에서 Privacy Claim 검증을 위한 다중지표 평가 프레임워크 연구 | A Multi-Metric Evaluation Framework for Verifying Privacy Claims in AI Security Research | DP reporting checklist |
| 2 | 차등프라이버시 기반 학습에서 Utility와 Membership Inference 위험의 Trade-off 분석 | An Analysis of the Trade-off Between Utility and Membership Inference Risk in Differential Privacy-Based Learning | utility-risk 동시 평가 |
| 3 | Membership Inference 방어 평가를 위한 Accuracy·Leakage·Accounting 통합 보고체계 연구 | An Integrated Reporting Framework of Accuracy, Leakage, and Accounting for Membership Inference Defense Evaluation | 재현성 중심 claim 검증 |

추천 제목은 “AI 보안 연구에서 Privacy Claim 검증을 위한 다중지표 평가 프레임워크 연구”이다. 국문초록은 DP misuse, DP-DL, MI attack/defense 문헌을 비교하고 synthetic toy 실험으로 privacy claim 검증 항목을 제안하는 방향으로 구성한다.

### A.2 연구문제

- RQ1. DP 기반 AI 보안 연구에서 privacy claim 검증을 위한 최소 보고 항목은 무엇인가?
- RQ2. Utility와 MI attack risk는 DP-like noise 조건에서 어떤 trade-off를 보이는가?
- RQ3. Formal accounting 없이 epsilon proxy를 사용할 경우 어떤 제한 문구와 재현성 증거가 필요한가?

---

## 14. 부록 B. SCI 논문 형식 전환 아이디어

SCI 제목 후보는 “A Multi-Metric Framework for Verifying Privacy Claims Against Membership Inference Risk in Differentially Private Machine Learning”이다.

Structured abstract는 Background, Problem, Method, Results, Contribution, Implications로 구성한다. 결과 문장은 W11 toy evaluation에서 medium noise 조건의 leakage proxy가 가장 낮았고, high noise 조건에서는 utility drop이 발생했으나 MI proxy가 단조 개선되지 않았다는 수준으로 제한한다. 실제 DP 보장이나 실제 membership inference 위험으로 일반화하지 않는다.

| 연구축 | 대표 논문 | 역할 |
|---|---|---|
| DP misuse and reporting | Blanco-Justicia et al. | DP claim misuse와 reporting responsibility |
| Centralized DP-DL | Demelius et al. | DP-SGD, clipping, noise, privacy auditing |
| DP in deep learning | Pan et al. | DP 적용 범위와 utility trade-off |
| Membership inference attacks | Hu et al. | MI attack taxonomy |
| Membership inference defenses | Li Hu et al. | MI defense taxonomy와 utility loss |

---

## 15. 부록 C. 제출 파일 위치와 변환 권장

| 파일 | 설명 |
|---|---|
| `07_week_submission/w11_submission_report.md` | 본 제출용 보고서 원본 |
| `07_week_submission/assets/w11_metric_chart.png` | 제출 보고서 그래프 |
| `04_experiment/experiment_report.md` | 실험 근거 보고서 |
| `04_experiment/outputs/` | 실험 결과 근거 파일 위치 |
| `05_ai_worklog/ai_disclosure_draft.md` | AI 활용 고지 근거 |

Word 제출본은 다음 위치에 생성해 관리한다.

```text
03_weekly_reports/w11_differential_privacy_mi/07_week_submission/exports/w11_submission_report.docx
```

PDF 제출본은 Word에서 최종 육안 검수 후 다음 위치에 저장한다.

```text
03_weekly_reports/w11_differential_privacy_mi/07_week_submission/exports/w11_submission_report.pdf
```

수식은 GitHub와 Word 변환을 모두 고려하여 Markdown 표 안에 넣지 않고, `$$...$$` block math로 유지한다.
