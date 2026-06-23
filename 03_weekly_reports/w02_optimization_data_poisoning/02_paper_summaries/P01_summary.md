# P01 Summary

## Optimization Methods for Large-Scale Machine Learning — Léon Bottou, Frank E. Curtis, Jorge Nocedal, SIAM Review, 2018

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W02 대규모 최적화 & 데이터 오염 위협 |
| 논문명 | Optimization Methods for Large-Scale Machine Learning |
| 저자 | Léon Bottou, Frank E. Curtis, Jorge Nocedal |
| 학술지 | SIAM Review |
| 권호/쪽 | Vol. 60, No. 2, pp. 223–311 |
| 연도 | 2018 |
| DOI | https://doi.org/10.1137/16M1080173 |
| 논문 유형 | Review / Optimization Methods Survey |
| 로컬 PDF | `01_papers/pdf/01_Bottou_Curtis_Nocedal_2018_Optimization_Methods_Large_Scale_ML.pdf` |
| 강의계획서 지정 논문과 일치 여부 | 일치 |
| 핵심 근거 사용 가능 여부 | 가능 |
| 검증 메모 | W02 `paper_list.md` 기준 DOI, 권호, 쪽 확인 완료. 최종 제출 시 SIAM 공식 서지 형식 재확인 필요 |

---

## 1. 한 문장 요약

이 논문은 대규모 머신러닝 학습을 **기대위험·경험위험 최소화 문제로 정식화하고, stochastic gradient, variance reduction, second-order approximation, regularization, distributed optimization 등 확장 가능한 최적화 방법을 비교하여 대규모 데이터와 고차원 모델 학습의 이론적·실무적 기준을 제공하는 핵심 리뷰 논문**이다.

---

## 2. 연구문제

이 논문의 핵심 연구문제는 다음과 같이 정리할 수 있다.

> 대규모 데이터와 고차원 파라미터를 가진 머신러닝 모델에서 계산 비용, 수렴성, 일반화, 재현성을 균형 있게 달성하기 위해 어떤 최적화 방법을 선택해야 하는가?

### 세부 연구질문

| 번호 | 연구질문 |
|---|---|
| RQ1 | 대규모 머신러닝 학습은 기대위험과 경험위험 최소화 문제로 어떻게 정식화되는가? |
| RQ2 | batch gradient와 stochastic gradient는 계산 비용과 수렴 안정성 측면에서 어떻게 다른가? |
| RQ3 | stochastic gradient의 noise와 variance는 학습 안정성과 일반화에 어떤 영향을 주는가? |
| RQ4 | second-order method와 quasi-Newton method는 어떤 조건에서 효율적이며, 왜 대규모 학습에서 제한이 있는가? |
| RQ5 | 데이터 오염 공격은 학습 목적함수와 gradient 추정 과정을 어떻게 왜곡하는가? |

---

## 3. 핵심 이론 및 수식

> 작성 원칙: GitHub, MS Word, PDF 변환 호환성을 위해 수식은 표 안에 넣지 않고 별도 블록 수식으로 작성한다. 변수 설명은 Markdown 표로 분리한다.

### 3.1 기대위험 최소화

머신러닝의 이상적인 목표는 데이터 분포 $P$에서 기대 손실을 최소화하는 모델 파라미터 $\theta$를 찾는 것이다.

$$
\min_{\theta \in \Theta} R(\theta)
= \mathbb{E}_{(x,y)\sim P}\left[\ell(f_{\theta}(x), y)\right]
$$

| 기호 | 의미 |
|---|---|
| $\theta$ | 모델 파라미터 |
| $\Theta$ | 가능한 파라미터 공간 |
| $P$ | 실제 데이터 분포 |
| $x, y$ | 입력 데이터와 정답 레이블 |
| $f_{\theta}$ | 파라미터 $\theta$를 가진 모델 |
| $\ell(\cdot)$ | 손실함수 |
| $R(\theta)$ | 기대위험 |

### 보안적 의미

기대위험은 실제 운영 분포에서의 평균 성능을 의미한다. 그러나 보안 공격자는 평균 분포가 아니라 특정 취약 영역을 노린다. 따라서 기대위험이 낮아도 데이터 오염, 백도어, 대적 입력, 분포 이동 조건에서는 성능이 무너질 수 있다.

---

### 3.2 경험위험 최소화

실제 학습에서는 전체 분포 $P$를 모르므로 유한한 학습 데이터셋 $D_n$의 평균 손실을 최소화한다.

$$
\min_{\theta \in \Theta} \hat{R}_n(\theta)
= \frac{1}{n}\sum_{i=1}^{n} \ell(f_{\theta}(x_i), y_i)
$$

| 기호 | 의미 |
|---|---|
| $D_n$ | $n$개의 학습 샘플로 구성된 데이터셋 |
| $\hat{R}_n(\theta)$ | 경험위험 |
| $x_i, y_i$ | $i$번째 학습 입력과 정답 |
| $n$ | 학습 샘플 수 |

### 보안적 의미

데이터 오염 공격은 바로 이 경험위험을 구성하는 학습 샘플 또는 라벨을 바꾼다. 오염된 데이터셋 $D_n^{poison}$을 사용하면 모델은 정상 목적함수가 아니라 공격자가 왜곡한 목적함수를 최소화하게 된다.

$$
\hat{R}_{poison}(\theta)
= \frac{1}{n}\sum_{i=1}^{n} \ell(f_{\theta}(x_i^{poison}), y_i^{poison})
$$

| 기호 | 의미 |
|---|---|
| $x_i^{poison}$ | 공격자가 조작했거나 오염된 입력 |
| $y_i^{poison}$ | 공격자가 조작했거나 오염된 레이블 |
| $\hat{R}_{poison}(\theta)$ | 오염 데이터 기준 경험위험 |

---

### 3.3 Stochastic Gradient Descent

대규모 데이터에서는 전체 데이터의 gradient를 매번 계산하기 어렵기 때문에 일부 샘플 또는 mini-batch로 gradient를 추정한다.

$$
\theta_{t+1}
= \theta_t - \eta_t \nabla_{\theta}\ell(f_{\theta_t}(x_{i_t}), y_{i_t})
$$

| 기호 | 의미 |
|---|---|
| $\theta_t$ | $t$번째 반복의 모델 파라미터 |
| $\eta_t$ | $t$번째 학습률 |
| $i_t$ | $t$번째 반복에서 선택된 샘플 인덱스 |
| $\nabla_{\theta}\ell$ | 선택 샘플 기준 손실 gradient |

Mini-batch를 사용할 경우 다음처럼 표현할 수 있다.

$$
g_t = \frac{1}{|B_t|}\sum_{i \in B_t} \nabla_{\theta}\ell(f_{\theta_t}(x_i), y_i)
$$

$$
\theta_{t+1} = \theta_t - \eta_t g_t
$$

| 기호 | 의미 |
|---|---|
| $B_t$ | $t$번째 mini-batch |
| $|B_t|$ | mini-batch 크기 |
| $g_t$ | mini-batch gradient 추정량 |

### 보안적 의미

데이터 오염은 mini-batch gradient $g_t$의 방향을 왜곡할 수 있다. 오염 샘플 비율이 작더라도 반복 학습 과정에서 누적되면 결정경계, class confidence, 특정 트리거 반응이 바뀔 수 있다. 따라서 poisoning 평가는 최종 정확도뿐 아니라 loss curve, gradient norm, class-wise performance, ASR을 함께 봐야 한다.

---

### 3.4 Regularized Optimization

대규모 학습에서는 과적합을 줄이고 일반화를 높이기 위해 정규화 항을 추가한다.

$$
\min_{\theta \in \Theta}
\frac{1}{n}\sum_{i=1}^{n} \ell(f_{\theta}(x_i), y_i)
+ \lambda \Omega(\theta)
$$

| 기호 | 의미 |
|---|---|
| $\lambda$ | 정규화 강도 |
| $\Omega(\theta)$ | 파라미터 복잡도 또는 제약을 나타내는 정규화 함수 |

### 보안적 의미

정규화는 과적합을 완화해 membership inference와 일부 데이터 오염 민감도를 줄일 수 있지만, 모든 보안 공격에 대한 방어는 아니다. 과도한 정규화는 clean accuracy를 낮추고, 특정 공격 조건에서는 robust 성능을 충분히 보장하지 못할 수 있다.

---

## 4. AI 원리 관점 분석

| 항목 | 분석 |
|---|---|
| 기대위험 | 실제 데이터 분포에서 평균 손실을 최소화하는 이상적 목표다. |
| 경험위험 | 유한 학습 데이터에서 평균 손실을 최소화하는 실제 학습 목표다. |
| Batch Gradient | 전체 데이터의 gradient를 계산하므로 안정적이지만 대규모 데이터에서는 비용이 크다. |
| Stochastic Gradient | 일부 샘플 또는 mini-batch로 gradient를 추정하므로 대규모 학습에 적합하지만 noise가 있다. |
| Variance Reduction | stochastic gradient의 분산을 줄여 수렴 안정성을 높인다. |
| Second-order Method | Hessian 또는 곡률 정보를 사용해 빠른 수렴을 노리지만 계산·메모리 비용이 크다. |
| Regularization | 모델 복잡도를 통제해 일반화와 안정성을 높인다. |
| Generalization | 학습 데이터 밖에서 성능을 유지하는 능력이며 보안 평가의 핵심 전제다. |

---

## 5. 보안 이슈 관점 분석

이 논문은 보안 공격 논문은 아니지만 W02의 데이터 오염과 백도어 위협을 이해하기 위한 최적화 기반을 제공한다.

| 보안 항목 | 최적화 관점 해석 |
|---|---|
| 데이터 오염 | 학습 샘플 또는 라벨을 바꿔 경험위험과 gradient 추정량을 왜곡한다. |
| 백도어 | 특정 트리거와 목표 레이블의 조건부 상관을 학습 목적함수에 삽입한다. |
| Class imbalance | 일부 클래스 손실이 과소평가되면 공격 또는 소수 클래스 미탐이 증가한다. |
| 과적합 | 학습 데이터 특이 신호에 민감해져 privacy leakage나 공격 민감도가 증가할 수 있다. |
| 분포 이동 | 학습 분포와 운영 분포가 달라지면 기대위험과 경험위험의 차이가 커진다. |
| 재현성 | seed, batch order, learning rate, optimizer 설정이 결과를 바꿀 수 있다. |

---

## 6. 위협모형

### 6.1 보호 대상

| 보호 대상 | 설명 |
|---|---|
| 학습 데이터 | 입력 데이터, 레이블, 전처리 결과, 데이터 split |
| 최적화 과정 | optimizer, learning rate, batch size, batch order, stopping rule |
| 모델 파라미터 | gradient 업데이트 결과로 형성되는 결정경계와 내부 표현 |
| 검증 데이터 | validation/test split, early stopping 기준, 평가 지표 |
| 실험 로그 | seed, config, loss curve, metric history, dependency version |

### 6.2 공격자 능력

| 공격자 유형 | 가능 행위 |
|---|---|
| Data poisoning attacker | 일부 학습 샘플 또는 레이블을 조작한다. |
| Backdoor attacker | 특정 트리거와 목표 레이블을 연결하는 오염 샘플을 삽입한다. |
| Supply-chain attacker | 데이터셋, 전처리 코드, dependency, optimizer 설정을 조작한다. |
| Insider attacker | 학습 config, seed, checkpoint, 로그를 변경하거나 누락시킨다. |
| Evaluation attacker | validation/test split 또는 metric 선택을 왜곡한다. |

### 6.3 공격 경로

```text
정상 데이터 수집
→ 데이터 일부 또는 라벨 오염
→ mini-batch gradient 추정량 왜곡
→ 반복 SGD 업데이트에 오염 영향 누적
→ 결정경계 또는 특정 트리거 반응 변화
→ clean accuracy 저하, class-wise failure, ASR 증가, 재현성 붕괴 발생
```

---

## 7. 평가방법 및 지표

| 지표 | 의미 | W02/P01에서의 활용 |
|---|---|---|
| Training Loss | 학습 데이터 기준 손실 | 최적화 수렴 상태 확인 |
| Validation Loss | 검증 데이터 기준 손실 | 일반화와 과적합 점검 |
| Clean Accuracy | 정상 테스트셋 정확도 | 기본 성능 확인 |
| Poisoned Accuracy | 오염 조건에서의 정확도 | 데이터 오염 영향 측정 |
| Accuracy Drop | 정상 대비 오염 조건 성능 저하 | 오염 민감도 평가 |
| ASR | 백도어 또는 목표 공격 성공률 | 조건부 공격 효과 평가 |
| Gradient Norm | gradient 크기 | 학습 안정성, 이상 업데이트 감지 |
| Loss Curve Stability | 손실 곡선의 변동성 | optimizer 안정성 확인 |
| Reproducibility | seed/config 고정 후 결과 재현성 | 실험 신뢰도 평가 |

---

## 8. 재현성 점검

이 논문은 최적화 방법 survey이므로 특정 단일 실험을 그대로 재현하기보다는, 최적화와 데이터 오염 실험의 재현성 조건을 체크리스트화하는 방식이 적절하다.

| 항목 | 점검 |
|---|---|
| 데이터셋 | MNIST, CIFAR-10, UCI digits, synthetic classification 등 공개 데이터셋 사용 가능 |
| 모델 | Logistic Regression, MLP, CNN 등 baseline부터 시작 |
| Optimizer | SGD, mini-batch SGD, momentum, Adam 등 명시 필요 |
| Hyperparameter | learning rate, batch size, epoch, weight decay 기록 필요 |
| Seed/Order | seed, data split, batch shuffle order 기록 필요 |
| 오염 설정 | poisoning ratio, label flip rule, trigger pattern, target class 기록 필요 |
| 결과 파일 | loss curve, clean accuracy, poisoned accuracy, ASR, config JSON/CSV 저장 필요 |
| 재현 가능성 판단 | 공개 데이터와 고정 seed 사용 시 중간 이상. 대규모 분산 학습 재현은 비용과 환경 의존성이 큼 |

### W02 실습 연결

W02에서는 다음 최소 실험으로 P01의 핵심 원리를 재현할 수 있다.

1. 공개 또는 synthetic 데이터셋을 로딩한다.
2. train/test split과 seed를 고정한다.
3. baseline optimizer로 clean model을 학습한다.
4. label-flip 또는 trigger 기반 toy poisoning 조건을 만든다.
5. 같은 optimizer와 seed 조건에서 poisoned model을 학습한다.
6. clean accuracy, poisoned accuracy, accuracy drop, ASR, loss curve를 비교한다.
7. 실험 config와 결과를 JSON/CSV로 저장한다.

---

## 9. 논문의 고유 기여

1. 대규모 머신러닝 최적화 문제를 기대위험·경험위험 최소화 관점에서 체계적으로 정리했다.
2. stochastic gradient 방법이 대규모 학습에서 중심이 되는 이유를 계산 비용과 확장성 관점에서 설명했다.
3. noise reduction, second-order method, regularization 등 주요 최적화 방법의 장단점을 비교했다.
4. 학습 과정의 수렴성, 안정성, 일반화가 모델 성능 해석에 중요함을 보여준다.
5. W02의 데이터 오염 공격을 “학습 목적함수와 gradient 추정 과정의 왜곡”으로 해석할 수 있는 이론적 기반을 제공한다.

---

## 10. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 보안 공격 직접성 부족 | 이 논문은 최적화 survey이므로 poisoning, backdoor, evasion 공격을 직접 분류하지 않는다. | P03–P05 poisoning/backdoor 문헌과 결합한다. |
| 최신 foundation model 한계 | 대규모 LLM 학습, RLHF, instruction tuning, RAG pipeline 최적화는 직접 다루지 않는다. | W07, W08, W14와 연결한다. |
| 실험 프로토콜 부재 | survey 논문이므로 단일 재현 실험이 없다. | W02 toy poisoning 실험으로 최적화 관점의 영향을 재현한다. |
| 보안 지표 부재 | clean loss와 수렴성 중심이며 ASR, stealth, robust accuracy는 별도 설계가 필요하다. | 공격 성공률, clean 유지율, detection rate를 추가한다. |
| 대규모 재현 비용 | 실제 대규모 학습 최적화 재현은 계산 자원과 환경 의존성이 크다. | 소규모 공개 데이터에서 원리 검증 중심으로 제한한다. |

---

## 11. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | AI 보안 위협은 추론 시점뿐 아니라 학습 목적함수와 최적화 과정에서 발생할 수 있다는 문제의식 제시 |
| 2장 관련연구 | 대규모 ML 최적화, ERM, SGD, regularization의 이론적 배경 정리 |
| 3장 위협모형 | 데이터 오염 공격자가 학습 데이터와 gradient 흐름을 왜곡하는 경로 정의 |
| 4장 연구방법 | clean/poisoned condition 비교, accuracy drop, ASR, loss curve 기반 평가 설계 |
| 5장 실험/분석 | label-flip 또는 toy backdoor 조건에서 최적화 결과 변화 분석 |
| 6장 보안적 함의 | 학습 재현성, 데이터 무결성, optimizer 설정 보존의 중요성 해석 |
| 7장 결론 | AI 보안 평가는 모델 출력뿐 아니라 학습 과정과 최적화 evidence까지 포함해야 함을 제시 |

---

## 12. 기말논문 연결 3문장

1. 이 주차에서 기말논문에 반영할 개념: 데이터 오염은 단순한 입력 오류가 아니라 경험위험과 stochastic gradient 추정량을 왜곡하여 모델 학습 궤적과 결정경계를 바꾸는 공격이다.
2. 이 주차에서 기말논문에 반영할 표·그림·실험: ERM/SGD 수식, clean vs poisoned loss curve, poisoning ratio별 accuracy drop 표, ASR 계산표를 반영한다.
3. 이 주차가 RAG 문서 오염/LLM 보안 감사 프레임워크와 연결되는 지점: RAG/LLM 환경에서도 학습 데이터, 임베딩 데이터, fine-tuning corpus, 검색 문서가 목적함수와 출력 분포에 영향을 주므로 P01의 최적화 관점을 W08 문서 오염과 W14 MLOps 증거 관리로 확장한다.

---

## 13. 최종 판단

이 논문은 W02의 AI 원리 중심 문헌으로 사용한다. P01은 직접적인 공격 taxonomy를 제공하지는 않지만, 데이터 오염·백도어·학습 재현성 문제를 최적화 관점에서 설명하는 데 핵심이다. 기말논문에서는 P01을 “왜 학습 데이터 조작이 모델 전체의 보안성에 영향을 주는가”를 설명하는 이론 배경으로 두고, P03–P05의 poisoning/backdoor 문헌과 결합하는 것이 적절하다.

---

## 14. 변환 호환성 메모

- GitHub Markdown, MS Word, PDF 변환 호환성을 위해 수식은 LaTeX 블록 수식으로 작성했다.
- 긴 수식은 Markdown 표 안에 넣지 않고 별도 문단으로 분리했다.
- 표에는 변수 설명과 해석만 배치했다.
- DOCX/PDF 변환 시에는 Pandoc 기준으로 다음 명령을 권장한다.

```bash
pandoc P01_summary.md -o P01_summary.docx
pandoc P01_summary.md -o P01_summary.pdf --pdf-engine=xelatex
```
