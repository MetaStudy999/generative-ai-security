# W12 신경망 검증·XAI·강건성 Trade-off

안전한 AI 평가는 정확도 하나로 끝나지 않는다.

---

## 오늘의 질문

- 모델이 clean test에서 잘 맞으면 충분한가?
- 작은 입력 변화에도 예측과 설명이 안정적인가?
- 검증 비용과 공정성 영향까지 같이 보고했는가?

---

## 문헌 5편의 역할

| 문헌 | 발표 역할 |
|---|---|
| P01 | verification abstraction, 로컬 PDF는 SUBSTITUTE |
| P02 | adversarial attack/defense, DOI/원문 대조 필요 |
| P03 | adversarial XAI, 로컬 PDF는 SUBSTITUTE |
| P04 | Lipschitz robustness, 지정 DOI 확인 필요 |
| P05 | robustness-accuracy-fairness trade-off, 지정 DOI 확인 필요 |

---

## AI 원리 70%

- Neural network verification
- Abstraction and reachability
- Formal robustness certificate
- Lipschitz regularization
- XAI explanation stability

---

## 보안 이슈 30%

- Adversarial input은 예측 무결성을 흔든다.
- Explanation manipulation은 검토자 판단을 흔든다.
- Verification scalability failure는 검증 생략으로 이어진다.
- Robustness, accuracy, fairness는 trade-off를 만들 수 있다.

---

## Toy 실험 설계

| 항목 | 설정 |
|---|---|
| 데이터 | synthetic binary classification |
| 모델 | toy logistic classifier |
| Seed | 42 |
| Perturbation | L-infinity epsilon 0.35 proxy |
| 제외 | 실제 시스템 공격, 개인정보 |

---

## 실험 결과

| 조건 | Clean | Robust | XAI | Certified | Fairness | Cost ms |
|---|---:|---:|---:|---:|---:|---:|
| Clean model | 0.818750 | 0.543750 | 0.927782 | 0.543750 | 0.039141 | 0.223524 |
| Adversarial input | 0.818750 | 0.543750 | 0.862321 | 0.340625 | 0.039141 | 0.190324 |
| Robust defense | 0.815625 | 0.543750 | 0.927152 | 0.543750 | 0.044823 | 0.191790 |
| XAI stability check | 0.815625 | 0.696875 | 0.976252 | 0.696875 | 0.044823 | 0.193048 |

---

## 해석

Clean accuracy가 높아도 robust accuracy는 낮아질 수 있다.

Certified rate는 toy 선형 모델의 bound proxy이며 실제 DNN formal verification certificate가 아니다.

공개 PDF와 DOI/원문 불일치는 최종 제출 전 사람이 재확인해야 한다.

---

## 기말논문 연결

- 성능·강건성·설명안정성·공정성·재현성 통합 평가표
- 위협모형과 평가 프로토콜의 연결
- 실행 로그 기반 연구윤리와 재현성 관리

---

## 결론

W12의 핵심은 "정확도 중심 보고"에서 "보증 가능한 다중지표 보고"로 관점을 바꾸는 것이다.

<!-- formula-visual-supplement:start -->
# 수식·그래프·그림 보강

- 보강 일자: 2026-06-23
- 수식은 표준 정의식 또는 검증 가능한 평가식으로만 작성했다.
- 그래프는 `04_experiment/outputs/metrics_summary.csv`의 기존 수치만 사용했다.
- 다이어그램은 AI-assisted conceptual diagram이며 사실 자료나 실험 결과처럼 해석하지 않는다.

### 핵심 수식: Robustness Objective와 Certified Radius

$$
\min_\theta \mathbb{E}_{(x,y)}\left[\max_{\lVert \delta\rVert\le \epsilon}\ell(f_\theta(x+\delta),y)\right],
\qquad
\forall \delta:\lVert\delta\rVert\le r,\ f(x+\delta)=f(x)
$$

| 기호 | 의미 |
|---|---|
| `\epsilon` | 학습 또는 평가 교란 반경 |
| `r` | certified radius |
| `\delta` | 입력 교란 |
| `\ell` | 손실 함수 |

**직관적 의미:**  
강건 학습은 허용 교란 안에서 최악의 손실을 낮추려는 목표로 표현된다. Certified radius는 주어진 반경 안에서 예측이 바뀌지 않음을 보장하려는 개념이다.

**보안 관점 해석:**  
보안 주장에는 empirical robustness와 formal certificate를 구분해야 한다.

**평가 지표 연결:**  
robust_accuracy, certified_rate, mean_bound_margin, verification_cost_ms와 연결한다.

**한계와 가정:**  
현재 실습의 certified_rate는 formal verification인지 toy proxy인지 최종 검토가 필요하다.

### 핵심 수식: Explanation Stability, Fairness Gap, Verification Cost

$$
Stability=sim(A(x),A(x')),
\qquad
FairGap=\left|\Pr(\hat{y}=1|G=0)-\Pr(\hat{y}=1|G=1)\right|,
\qquad
Cost=\frac{1}{n}\sum_{i=1}^{n}t_i
$$

| 기호 | 의미 |
|---|---|
| `A(x)` | 입력 x에 대한 explanation/attribution |
| `sim` | 설명 간 유사도 |
| `G` | 민감 또는 비교 그룹 변수 |
| `t_i` | verification runtime |

**직관적 의미:**  
설명이 안정적이어야 방어 분석의 근거로 사용할 수 있다. 공정성 gap과 verification cost는 강건성 외의 배포 제약을 나타낸다.

**보안 관점 해석:**  
보안 검증은 robust accuracy 하나가 아니라 explanation stability와 fairness/cost를 함께 본다.

**평가 지표 연결:**  
explanation_stability, fairness_gap, verification_cost_ms와 연결한다.

**한계와 가정:**  
toy binary classification 설정이며 formal proof로 일반화하지 않는다.

### 표 수치 기반 그래프

![W12 metrics chart](assets/charts/w12_metrics_chart.png)

그래프는 clean_accuracy, robust_accuracy, explanation_stability, certified_rate, fairness_gap, verification_cost_ms를 조건별로 표시한다. certified_rate가 toy proxy인지 formal verification 결과인지 문서에서 명확히 구분해야 한다. 모든 값은 W12 output CSV에서 읽었다.

### Threat Model / Pipeline Diagram

![W12 pipeline diagram](assets/diagrams/w12_pipeline_diagram.svg)

이 다이어그램은 `verification-XAI robustness flow`를 발표용으로 요약한 개념도다. 데이터 흐름, 평가 지표, 한계 표시는 `assets/figure_manifest.md`에도 기록했다.

### 확인 필요

- `certified_rate`는 toy proxy 또는 제한 실험인지 formal verification인지 최종 원문 확인이 필요하다.
- 논문별 원문 절·쪽·그림 번호는 최종 제출 전 사람 검토가 필요하다.
<!-- formula-visual-supplement:end -->
