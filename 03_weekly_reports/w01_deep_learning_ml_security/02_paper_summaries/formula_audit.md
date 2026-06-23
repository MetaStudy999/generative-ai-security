# W01 수식·알고리즘 반영 감사표

## 0. 감사 목적

이 문서는 `03_weekly_reports/w01_deep_learning_ml_security/02_paper_summaries/P01_summary.md` ~ `P05_summary.md`에 반영된 수식·알고리즘·평가지표를 점검하기 위한 감사표다. W01의 핵심 축은 **딥러닝 원리, ML 생명주기 보증, 침입탐지 지표, 대적 강건성, 프라이버시 공격**이다.

---

## 1. 점검 범위와 기준

| 항목 | 내용 |
|---|---|
| 점검 범위 | `P01_summary.md` ~ `P05_summary.md`, `paper_matrix.md`, `paper_list.md` |
| 점검 목적 | 각 논문 summary에 핵심 수식·알고리즘·평가지표가 포함되었는지 확인 |
| 수식 작성 원칙 | GitHub, MS Word, PDF 변환 호환성을 위해 Markdown 표 밖의 LaTeX block math 사용 |
| 원문 인용 원칙 | 대표 수식은 W01 보고서 설명용 표준 정의식으로 사용하며, 원문 직접 전사가 아님을 명시 |
| 검증 주의 | 원문 절/쪽/그림/알고리즘 번호는 최종 제출 전 별도 확인 필요 |
| 저작권 주의 | PDF 원문은 공개 GitHub 저장소에서 저작권 위험이 있으므로 DOI/URL·서지정보 중심 공개 권장 |

---

## 2. 논문별 수식 반영 현황

| ID | 논문 | 현재 수식·지표 반영 상태 | 대표 수식·알고리즘 | 원문 확인 상태 | 보강 필요성 | 판정 |
|---|---|---|---|---|---|---|
| P01 | *Deep learning* | 반영 완료 | 경험위험, gradient descent, 역전파 기반 학습, generalization gap | DOI/서지는 확인. 원문 수식 위치는 최종 제출 전 확인 필요 | 수식은 표준 정의식으로 충분. 원문 직접 인용 금지 유지 | 완료 |
| P02 | *Assuring the Machine Learning Lifecycle* | 반영 완료 | lifecycle risk, evidence coverage, assurance evidence chain | DOI/서지는 확인. 절차·지표 중심 문헌이므로 수식은 보고서용 정형화 표현 | 수식보다 절차·체크리스트 중심 유지 | 완료 |
| P03 | *ML Methods for Cyber Security Intrusion Detection* | 반영 완료 | binary classifier, confusion matrix, precision, recall, F1, false alarm rate | DOI/서지는 확인. 지표는 표준 정의식 | 침입탐지 운영 지표와 threshold 기록 필요 | 완료 |
| P04 | *Adversarial Attacks and Defenses in ML-Powered Networks* | 반영 완료 / 검증 주의 | adversarial perturbation objective, robust optimization, robust accuracy, ASR | arXiv DOI 확인. 강의계획서 지정 IEEE COMST 논문과 동일성 최종 확인 필요 | 최종 제출 전 지정 논문 교체 여부 또는 관련 논문 사용 사유 명시 | 완료 / 주의 |
| P05 | *A Survey of Privacy Attacks in Machine Learning* | 반영 완료 | membership inference advantage, generalization gap, privacy-utility trade-off, DP 정의식 | DOI/서지는 확인. 지표는 표준 정의식 | W11 DP/MIA와 연결해 privacy budget과 utility drop 병기 | 완료 |

---

## 3. 핵심 수식·지표 감사표

### 3.1 P01 — 딥러닝 원리

| 수식·지표 | 목적 | 감사 판정 |
|---|---|---|
| `R(θ)=E[ℓ(f_θ(x),y)]` | 경험위험 또는 기대위험을 통한 학습 목표 설명 | 반영 적절 |
| `θ ← θ − η∇_θ L(θ)` | gradient descent와 역전파 기반 parameter update 설명 | 반영 적절 |
| `GeneralizationGap = Acc_train − Acc_test` | 과적합·일반화 차이 설명 | 반영 적절 |

**보안 연결:** gradient와 representation은 adversarial attack, membership inference, model inversion의 기술적 배경이 된다.

---

### 3.2 P02 — ML 생명주기 보증

| 수식·지표 | 목적 | 감사 판정 |
|---|---|---|
| `LifecycleRisk = DataRisk + ModelRisk + DeploymentRisk + MonitoringGap` | ML 시스템 위험을 생명주기 단계별로 분해 | 반영 적절 |
| `EvidenceCoverage = |E_verified| / |E_required|` | 보증 증거 충족률 평가 | 반영 적절 |
| `TraceabilityScore` 또는 checklist 기반 evidence chain | 데이터·모델·검증·배포 로그 추적성 | 절차형 지표로 유지 적절 |

**보안 연결:** 공격·방어 성능보다 중요한 것은 어떤 데이터, 설정, 모델, 로그가 해당 주장을 뒷받침하는지 남기는 것이다.

---

### 3.3 P03 — 침입탐지 평가 지표

| 수식·지표 | 목적 | 감사 판정 |
|---|---|---|
| `Precision = TP/(TP+FP)` | 오탐이 많은 IDS의 신뢰도 평가 | 반영 적절 |
| `Recall = TP/(TP+FN)` | 공격 미탐 위험 평가 | 반영 적절 |
| `F1 = 2·Precision·Recall/(Precision+Recall)` | precision과 recall 균형 평가 | 반영 적절 |
| `FAR = FP/(FP+TN)` | false alarm rate 운영 지표 | 반영 적절 |

**보안 연결:** 침입탐지는 accuracy만으로 부족하다. 공격 탐지율, 오탐률, 미탐률, class imbalance를 함께 봐야 한다.

---

### 3.4 P04 — 대적공격·강건성

| 수식·지표 | 목적 | 감사 판정 |
|---|---|---|
| `max_{δ∈Δ} ℓ(f_θ(x+δ),y)` | adversarial perturbation 목적함수 | 반영 적절 |
| `min_θ E[max_{δ∈Δ} ℓ(f_θ(x+δ),y)]` | robust optimization 구조 | 반영 적절 |
| `RobustAcc = (1/n)Σ1[f_θ(x_i^adv)=y_i]` | 공격 조건 정확도 | 반영 적절 |
| `ASR = (1/n)Σ1[f_θ(x_i^adv)=y_target]` | 공격 성공률 | 반영 적절 |

**보안 연결:** clean accuracy와 robust accuracy를 분리해야 한다. P04는 관련 arXiv 논문 기준이므로 최종 제출 전 강의계획서 지정 논문 동일성 확인이 필요하다.

---

### 3.5 P05 — 프라이버시 공격

| 수식·지표 | 목적 | 감사 판정 |
|---|---|---|
| `Adv_MI = P[A(z)=1|z∈D_train] − P[A(z)=1|z∉D_train]` | membership inference advantage 측정 | 반영 적절 |
| `GeneralizationGap = Acc_train − Acc_test` | overfitting과 membership leakage 연결 | 반영 적절 |
| `PrivacyUtilityScore = Utility − λ·LeakageRisk` | privacy-utility trade-off 설명 | 반영 적절 |
| `(ε,δ)-DP` 정의식 | DP 기반 방어의 이론적 배경 | W11과 연결해 사용 적절 |

**보안 연결:** 프라이버시 평가는 유출률, 공격 advantage, utility drop을 함께 봐야 한다.

---

## 4. 변환 호환성 점검

| 점검 항목 | 상태 | 비고 |
|---|---|---|
| Markdown 표 내부 복잡 수식 사용 | 피함 | 수식은 표 밖 block math 권장 |
| LaTeX block math 사용 | 반영 | GitHub/Word/PDF 변환에 유리 |
| HTML `<br>` 기반 수식 삽입 | 사용 지양 | 변환 깨짐 방지 |
| 원문 직접 수식 전사 | 지양 | 표준 정의식 / 보고서용 표현으로 사용 |
| pandoc 변환 | 가능 | `pandoc *.md -o *.docx` 또는 PDF 변환 가능 |

---

## 5. 최종 제출 전 확인 필요 항목

| 항목 | 필요 조치 | 우선순위 |
|---|---|---|
| P04 지정 논문 동일성 | 강의계획서 지정 IEEE COMST 논문과 현재 arXiv 관련 논문 동일성 확인 | 높음 |
| 원문 절/쪽 번호 | 최종 보고서에서 수식·그림을 직접 인용할 경우 원문 페이지 확인 | 중간 |
| PDF 공개 위험 | 공개 GitHub 제출 전 PDF 원문 삭제 또는 비공개 저장소 전환 검토 | 높음 |
| 수식 렌더링 | GitHub preview와 docx/pdf 변환 결과 확인 | 중간 |
| 기말논문 연결 | W01 수식이 W02~W15 평가 지표와 중복·충돌하지 않는지 최종 점검 | 중간 |

---

## 6. 종합 판정

W01의 수식·알고리즘 반영 상태는 **완료**로 판단한다. 다만 P04는 강의계획서 지정 논문 동일성 확인이 남아 있으므로 `완료 / 검증 주의`로 표시한다.

W01의 수식 구성은 전체 강의의 기본 평가축으로 사용 가능하다.

```text
P01: 학습 원리와 일반화
→ P02: 생명주기 evidence chain
→ P03: 침입탐지 confusion-matrix 지표
→ P04: 대적 강건성·ASR
→ P05: 프라이버시 leakage·MI advantage
```
