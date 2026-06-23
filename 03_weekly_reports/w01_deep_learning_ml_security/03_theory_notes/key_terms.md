# W01 핵심 용어

## 0. 문서 목적

이 문서는 W01의 핵심 용어를 **정의 → 수식/지표 → 관련 논문 → 후속 주차 연결** 구조로 정리한다. 단순 용어 암기가 아니라, 각 용어가 AI 보안 평가에서 어떤 지표와 위협모형으로 연결되는지 확인하기 위한 이론 노트다.

---

## 1. 핵심 용어 표

| 용어 | 작업 정의 | 대표 수식·지표 | 관련 논문 | 후속 연결 |
|---|---|---|---|---|
| Deep Learning | 여러 층의 신경망이 원시 입력에서 계층적 표현을 학습하는 방법 | loss, accuracy, representation quality | P01 | W03 CV, W04 Transformer, W12 verification |
| Representation Learning | 사람이 직접 설계한 특징 대신 모델이 task에 유용한 특징 공간을 학습하는 과정 | embedding, feature map | P01 | adversarial vulnerability, privacy leakage |
| Empirical Risk Minimization | 학습 데이터에서 평균 손실을 최소화하는 학습 원리 | `R(θ)=E[ℓ(f_θ(x),y)]` | P01 | W02 optimization, W03 adversarial training |
| Gradient Descent | 손실의 기울기를 따라 파라미터를 갱신하는 절차 | `θ ← θ − η∇_θL(θ)` | P01 | gradient attack, backpropagation |
| Backpropagation | 손실의 gradient를 출력층에서 입력층 방향으로 전파해 파라미터를 갱신하는 알고리즘 | chain rule 기반 gradient | P01 | FGSM/PGD, saliency, privacy attack |
| Generalization | 학습 데이터 밖의 새로운 데이터에서도 성능이 유지되는 성질 | train-test gap | P01, P02, P05 | W11 membership inference |
| Generalization Gap | 학습 성능과 테스트 성능의 차이 | `Acc_train − Acc_test` 또는 `Loss_test − Loss_train` | P01, P05 | privacy leakage risk |
| Overfitting | 학습 데이터에는 과도하게 맞지만 새 데이터에는 취약한 상태 | high train acc / low test acc | P01, P05 | MIA, memorization |
| ML Lifecycle | 데이터 수집, 전처리, 학습, 검증, 배포, 모니터링의 반복 과정 | lifecycle risk, evidence coverage | P02 | W14 MLOps, W15 evidence chain |
| Evidence Chain | 성능·보안 주장을 뒷받침하는 DOI, config, seed, output, log, human review의 연결 | `EvidenceCoverage` | P02 | W15 reproducibility |
| Intrusion Detection | 네트워크·시스템 로그에서 정상/공격 행위를 구분하는 보안 기능 | precision, recall, F1, FAR | P03 | W09 cyber defense, W14 monitoring |
| False Positive | 정상 행위를 공격으로 잘못 판단하는 오류 | `FP/(FP+TN)` | P03 | alert fatigue, availability risk |
| False Negative | 공격 행위를 정상으로 잘못 판단하는 오류 | `FN/(TP+FN)` | P03 | 침해 미탐, security failure |
| Precision | 탐지한 공격 중 실제 공격 비율 | `TP/(TP+FP)` | P03 | IDS 품질 평가 |
| Recall | 실제 공격 중 탐지한 비율 | `TP/(TP+FN)` | P03 | 미탐 위험 평가 |
| F1 Score | precision과 recall의 조화평균 | `2PR/(P+R)` | P03 | 불균형 데이터 평가 |
| Adversarial Example | 사람에게는 거의 같아 보이지만 모델 예측을 바꾸도록 조작된 입력 | perturbation budget `ε` | P04 | W03/W12 robustness |
| Attack Success Rate | 공격 조건에서 목표 오분류·회피가 성공한 비율 | `ASR` | P04 | W03, W08, W13 |
| Robust Accuracy | 공격 또는 교란 조건에서도 유지되는 정확도 | `RobustAcc` | P04 | clean-robust trade-off |
| Clean Accuracy | 공격이 없는 정상 조건의 정확도 | `Acc_clean` | P01, P04 | robust accuracy와 비교 |
| Robustness Gap | clean accuracy와 robust accuracy의 차이 | `Acc_clean − Acc_robust` | P04 | defense 부작용 분석 |
| Membership Inference | 특정 샘플이 학습 데이터에 포함됐는지 추론하는 공격 | `Adv_MI` | P05 | W11 MIA |
| Model Inversion | 모델 출력이나 confidence로 입력 특성 또는 민감정보를 복원하려는 공격 | reconstruction risk | P05 | privacy leakage |
| Property Inference | 학습 데이터 집합의 민감 속성이나 통계적 특징을 추론하는 공격 | property leakage | P05 | W10 FL privacy |
| Privacy-Utility Trade-off | 프라이버시 보호를 강화할수록 정상 utility가 낮아질 수 있는 관계 | `Utility − λ·LeakageRisk` | P05 | W11 DP, W10 FL |
| Differential Privacy | 단일 데이터 포인트의 포함 여부가 출력에 미치는 영향을 제한하는 보호 원리 | `(ε,δ)-DP` | P05 | W11 DP-SGD |
| Benchmark Contamination | 평가 데이터가 학습 데이터에 포함되거나 benchmark 패턴이 노출되는 위험 | overlap ratio | P02 | W15 평가오염 |
| Reproducibility | 같은 코드·데이터·설정으로 결과를 다시 만들 수 있는 성질 | seed/config/log | P02-P05 | W14/W15 |

---

## 2. 초보자용 핵심 연결

W01의 핵심은 다음 흐름이다.

```text
딥러닝은 표현을 학습한다.
→ 표현과 gradient는 성능의 원천이지만 공격면도 된다.
→ 보안 시스템에서는 accuracy만 보지 않고 오탐, 미탐, 강건성, 프라이버시를 분리해야 한다.
→ 모든 주장은 DOI, config, seed, output log, human review로 증명되어야 한다.
```

---

## 3. 용어 간 관계도

| 출발 개념 | 연결 개념 | 보안 의미 |
|---|---|---|
| Backpropagation | Gradient-based attack | 학습에 쓰인 gradient 구조가 공격에도 활용될 수 있다. |
| Overfitting | Membership inference | 학습 데이터를 과도하게 기억하면 membership leakage 위험이 커진다. |
| Clean Accuracy | Robust Accuracy | 정상 성능과 공격 조건 성능은 다르다. |
| Precision/Recall | IDS 운영 비용 | 오탐과 미탐은 서로 다른 운영 비용을 만든다. |
| ML Lifecycle | Evidence Chain | 모델 성능보다 데이터·설정·로그·배포 증거가 중요하다. |
| Differential Privacy | Privacy-Utility Trade-off | 프라이버시 보호와 유틸리티 사이에는 비용이 있다. |

---

## 4. 기말논문 반영 메모

기말논문에서는 이 용어표를 다음 위치에 활용한다.

| 기말논문 장 | 활용 방식 |
|---|---|
| 2장 관련연구 | 딥러닝·ML 보안 기본 용어 정의 |
| 3장 위협모형 | 보호 자산과 공격면 용어 표준화 |
| 4장 연구방법 | clean/robust/privacy/reproducibility 지표 정의 |
| 5장 분석 | 실험 결과표의 지표 해석 기준 |
| 6장 보안적 함의 | accuracy 중심 평가의 한계 설명 |
