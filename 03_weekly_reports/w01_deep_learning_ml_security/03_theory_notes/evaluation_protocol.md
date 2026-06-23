# W01 평가방법

## 0. 문서 목적

이 문서는 W01의 평가 프로토콜을 정의한다. 핵심 원칙은 **정상 성능, 탐지 품질, 공격 영향, 강건성, 프라이버시 위험, 생명주기 보증, human review**를 분리해 기록하는 것이다.

정확도 하나로 ML 시스템의 보안성을 주장하지 않는다.

---

## 1. 평가 원칙

| 원칙 | 설명 |
|---|---|
| 성능과 보안 분리 | clean accuracy와 robust/privacy/security 지표를 분리한다. |
| 안전한 실험 | 공개 또는 synthetic 데이터만 사용하고 실제 서비스 공격은 수행하지 않는다. |
| 지표별 해석 | precision, recall, F1, FAR, ASR, MI advantage는 서로 다른 위험을 설명한다. |
| 재현성 우선 | seed, config, dataset split, model version, run log가 없으면 수치를 확정 주장하지 않는다. |
| 한계 명시 | toy evaluation 결과를 실제 운영 보안성으로 일반화하지 않는다. |
| 사람 검토 | DOI, 수치, 인용, 보안 해석은 최종적으로 사람이 재검토한다. |

---

## 2. 핵심 평가표

| 평가 항목 | 지표 | 측정 방법 | 필요한 데이터 | 관련 논문 | 비고 |
|---|---|---|---|---|---|
| Clean Performance | accuracy, precision, recall, F1 | 정상 test split에서 기준 모델 평가 | 공개 또는 synthetic 데이터 | P01 | 기본 성능 |
| Detection Quality | false positive rate, false negative rate | 보안 탐지 과제에서 오류 유형 분리 | IDS 또는 toy binary classification 데이터 | P03 | 오탐/미탐 비용 분리 |
| Attack Impact | attack success rate, performance drop | 제한된 toy perturbation 또는 문헌 기반 시나리오 비교 | 변형 입력 또는 시나리오 표 | P04 | 실제 악용 절차 제외 |
| Robust Performance | robust accuracy, robustness gap | 공격/교란 조건과 clean 조건 비교 | 교란 데이터 | P04 | clean 성능과 분리 |
| Privacy/Leakage | MI advantage, leakage risk label | synthetic shadow data 또는 문헌 기반 위험 분류 | 실제 개인정보 금지 | P05 | 실제 MIA 결과와 구분 |
| Lifecycle Assurance | evidence completeness, traceability | DOI, PDF, config, seed, log, review 기록 점검 | 문서와 설정 파일 | P02 | 재현성 증거 |
| Human Review | 검토 완료 여부, issue count | 원문, DOI, 수치, 인용을 사람이 재검토 | 체크리스트 | P02-P05 | 최종 책임 |

---

## 3. 핵심 수식

### 3.1 Accuracy

$$
Accuracy=\frac{TP+TN}{TP+TN+FP+FN}
$$

### 3.2 Precision

$$
Precision=\frac{TP}{TP+FP}
$$

### 3.3 Recall

$$
Recall=\frac{TP}{TP+FN}
$$

### 3.4 F1 Score

$$
F1=\frac{2\cdot Precision\cdot Recall}{Precision+Recall}
$$

### 3.5 False Alarm Rate

$$
FAR=\frac{FP}{FP+TN}
$$

### 3.6 Robustness Gap

$$
RobustnessGap=Acc_{clean}-Acc_{robust}
$$

### 3.7 Attack Success Rate

$$
ASR=\frac{N_{successful\ attacks}}{N_{attack\ trials}}
$$

### 3.8 Evidence Coverage

$$
EvidenceCoverage=\frac{|E_{verified}|}{|E_{required}|}
$$

---

## 4. 최소 실험 프로토콜

1. 공개 또는 synthetic 데이터만 사용한다.
2. seed, 데이터 split, 모델 종류, 주요 hyperparameter를 config에 기록한다.
3. clean baseline을 먼저 평가한다.
4. 안전한 toy perturbation 또는 label noise 조건을 적용한다.
5. 성능 하락과 오류 유형을 기록한다.
6. privacy-safe audit은 실제 개인정보나 실제 membership inference 공격이 아니라 synthetic overfitting/confidence 신호 점검으로 제한한다.
7. 실제 개인정보, 실제 서비스 공격, 무단 질의는 수행하지 않는다.
8. 결과값은 실행 로그가 있을 때만 보고서에 적는다.
9. 최종 해석에는 “toy evaluation”과 “문헌 기반 분석”을 구분한다.

---

## 5. 결과 기록 양식

| 조건 | Accuracy | Precision | Recall | F1 | Attack/Leakage 지표 | 근거 파일 | 해석 메모 |
|---|---:|---:|---:|---:|---:|---|---|
| Clean baseline | 실행 후 기록 | 실행 후 기록 | 실행 후 기록 | 실행 후 기록 | 해당 없음 | `metrics_summary.csv`, `run_log.md` | seed/config 확인 |
| Label-noise training | 실행 후 기록 | 실행 후 기록 | 실행 후 기록 | 실행 후 기록 | 성능 하락 | `metrics_summary.csv`, `results.json` | 데이터 오염 toy 조건 |
| Toy feature perturbation | 실행 후 기록 | 실행 후 기록 | 실행 후 기록 | 실행 후 기록 | ASR 또는 performance drop | `metrics_summary.csv`, `results.json` | 악용 세부 절차 제외 |
| Privacy-safe audit | 해당 시 기록 | 해당 시 기록 | 해당 시 기록 | 해당 시 기록 | leakage risk label | `results.json`, `run_log.md` | synthetic data만 사용 |

---

## 6. W01 outputs 기준 결과

> 아래 수치는 W01 synthetic/toy evaluation 결과다. 문헌 원문 실험값이 아니며, 실제 보안성 보증으로 해석하지 않는다.

| 조건 | Accuracy | Precision | Recall | F1 | 비고 |
|---|---:|---:|---:|---:|---|
| Clean baseline | 0.869444 | 0.867403 | 0.872222 | 0.869806 | `metrics_summary.csv` 기준 |
| Label-noise training | 0.838889 | 0.827957 | 0.855556 | 0.841530 | 126개 training label flip |
| Toy feature perturbation | 0.844444 | 0.848315 | 0.838889 | 0.843575 | Gaussian feature noise |

### 6.1 성능 변화 해석

| 비교 | Accuracy 변화 | F1 변화 | 해석 |
|---|---:|---:|---|
| Clean → Label-noise | -0.030555 | -0.028276 | 라벨 오염은 정상 성능과 탐지 품질을 함께 낮춘다. |
| Clean → Toy perturbation | -0.025000 | -0.026231 | 입력 교란은 clean 성능과 다른 별도 robust 평가가 필요함을 보여준다. |

### 6.2 Privacy-safe audit 해석

Privacy-safe audit은 다음과 같이 기록되었다.

| 항목 | 값 | 해석 |
|---|---:|---|
| Train accuracy | 0.857143 | synthetic training split 기준 |
| Test accuracy | 0.869444 | synthetic test split 기준 |
| Train-test gap | -0.012301 | 과적합 신호가 낮은 toy 결과 |
| Risk label | `low_overfitting_signal` | 실제 membership inference 공격 결과가 아님 |

이 결과는 synthetic data의 과적합/confidence 신호 점검이며 실제 membership inference 공격 결과가 아니다.

---

## 7. 해석 기준

| 상황 | 해석 원칙 |
|---|---|
| Clean 성능이 높고 robust 성능이 낮음 | 보안성 주장을 제한한다. |
| Robust 성능이 좋아도 privacy leakage가 큼 | 기밀성 관점의 위험을 별도로 적는다. |
| 오탐이 높음 | 운영자 피로와 alert 무시 위험을 논의한다. |
| 미탐이 높음 | 실제 침해 누락 가능성을 논의한다. |
| 실행값이 없음 | “실행 전” 또는 “문헌 기반 분석”으로 표시한다. |
| P04 관련 논문 사용 | 강의계획서 지정 IEEE COMST 논문 동일성 확인 전까지 주의 메모를 유지한다. |
| PDF 원문 공개 | 공개 저장소에서는 DOI/URL, 서지정보, 요약만 남기는 것을 원칙으로 한다. |

---

## 8. 재현성 체크리스트

| 항목 | 기록 여부 | 비고 |
|---|---|---|
| DOI/URL 검증 | 필수 | `paper_list.md`와 연결 |
| Dataset source | 필수 | 공개/synthetic 여부 명시 |
| Data split | 필수 | train/test 비율, seed 기록 |
| Model config | 필수 | 모델 종류, hyperparameter |
| Random seed | 필수 | 결과 재현 조건 |
| 실행 로그 | 필수 | `run_log.md` |
| 결과 파일 | 필수 | `metrics_summary.csv`, `results.json` |
| AI 활용 고지 | 필수 | `05_ai_worklog`와 연결 |
| Human review | 권장 | 최종 제출 전 확인 |
| 한계 문장 | 필수 | toy evaluation, 실제 공격 아님 명시 |

---

## 9. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 4장 연구방법 | clean/label-noise/toy perturbation/privacy-safe audit protocol |
| 5장 실험/분석 | W01 outputs 기준 결과표와 성능 변화 해석 |
| 6장 보안적 함의 | accuracy 중심 평가의 한계, 오탐/미탐, robust/privacy trade-off |
| 부록 | config, seed, run log, metrics_summary, AI 활용 고지 |

---

## 10. 최종 판단

W01 평가방법은 기초 수준의 toy evaluation으로 적절하다. 다만 다음 원칙을 반드시 유지한다.

```text
정상 성능 ≠ 보안성
toy perturbation ≠ 실제 공격 검증
privacy-safe audit ≠ 실제 membership inference 결과
수치 주장에는 config, seed, output, run_log가 필요
```
