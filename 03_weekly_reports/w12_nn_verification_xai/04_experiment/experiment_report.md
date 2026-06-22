# W12 실험 보고서

## 1. 실험 목표

W12 실습은 신경망 검증, 대적 강건성, XAI 설명 안정성, 공정성 영향, 검증 비용을 실제 운영 시스템이 아닌 synthetic binary classification 기반 안전 toy 실험에서 함께 기록하는 것이다. 목표는 공격 절차를 재현하는 것이 아니라 clean accuracy, robust accuracy, explanation stability, certified rate, fairness gap, verification cost를 같은 로그 구조로 보고하는 연습이다.

본 실습은 실제 대규모 DNN formal verification이나 실제 안전중요 시스템 평가가 아니라 W12의 핵심인 보안 평가축을 안전하게 설명하기 위한 최소 toy protocol이다. 따라서 synthetic binary classification과 toy logistic classifier를 사용하되, 평가 구조는 이후 실제 neural network verification, certified defense, adversarial XAI, fairness-aware robustness 평가에도 확장 가능하도록 clean accuracy, robust accuracy, explanation stability, certified rate, fairness gap, verification cost, reproducibility evidence로 분리하였다.

## 2. 환경

| 항목 | 내용 |
|---|---|
| Python | 3.11 기준 |
| Package | 표준 라이브러리 중심, YAML 로딩용 `pyyaml` |
| Seed | 42 |
| 데이터 | synthetic_binary_classification |
| 개인정보 | 사용하지 않음 |
| 실행일 | 2026-06-22 |
| 재실행 확인 | 2026-06-23 로컬 Python 실행 성공 |
| 결과 근거 | `outputs/metrics_summary.csv`, `outputs/results.json`, `outputs/run_log.md` |

## 3. 실험 설계

| 단계 | 설계 내용 | 기록 위치 |
|---|---|---|
| 기준 모델 | synthetic 4-feature binary data에 toy logistic classifier 학습 | `src/run_experiment.py` |
| 대적 입력 | 선형 모델 가중치 부호를 이용한 L-infinity epsilon perturbation proxy | `epsilon: 0.35` |
| Robust defense | 대적 증강 샘플과 더 큰 regularization으로 방어 모델 학습 | config 및 script |
| XAI 안정성 | clean/perturbed feature attribution의 cosine similarity 측정 | metrics |
| Certified robustness proxy | 선형 모델 margin bound 기반 certified rate proxy 계산 | metrics |
| 공정성 영향 | `data.fairness_group_feature`로 나눈 synthetic group별 accuracy gap 측정 | metrics |
| Verification cost | bound proxy 계산 시간(ms) 기록 | metrics |

## 4. 실행 명령

```bash
cd 03_weekly_reports/w12_nn_verification_xai/04_experiment
python3 src/run_experiment.py --config configs/config.yaml
```

Docker compose 사용 시:

```bash
cd 03_weekly_reports/w12_nn_verification_xai/04_experiment
docker compose run --rm w12-nn-verification-xai python3 src/run_experiment.py --config configs/config.yaml
```

## 5. config/code 정합성 점검

| 항목 | 점검 결과 |
|---|---|
| `data.fairness_group_feature` | 데이터 생성 시 synthetic group 분할 feature index로 반영하도록 보완 |
| `experiment.model` | `toy_logistic_classifier`가 아니면 실행 중단하도록 검증 |
| `experiment.results_recorded` | 결과 감사용 기록 필드로 `results.json`에 보존 |
| `adversarial_features()` | 실제 PGD/FGSM이 아니라 선형 가중치 부호 기반 toy perturbation proxy |
| `certified_rate` | 선형 모델 margin bound proxy. formal DNN verification certificate 아님 |
| `pyproject.toml` | 과도한 의존성 제거, `pyyaml`만 유지 |

## 6. 실험 결과

| 조건 | Clean Accuracy | Robust Accuracy | Explanation Stability | Certified Rate | Fairness Gap | Verification Cost ms | 해석 |
|---|---:|---:|---:|---:|---:|---:|---|
| Clean model | 0.818750 | 0.543750 | 0.927782 | 0.543750 | 0.039141 | 0.223524 | 정상 성능은 높지만 perturbation에서 강건성이 낮아짐 |
| Adversarial input | 0.818750 | 0.543750 | 0.862321 | 0.340625 | 0.039141 | 0.190324 | 더 강한 perturbation proxy에서 설명 안정성과 bound proxy가 악화됨 |
| Robust defense | 0.815625 | 0.543750 | 0.927152 | 0.543750 | 0.044823 | 0.191790 | 단순 증강 방어만으로 robust accuracy 개선은 제한적 |
| XAI stability check | 0.815625 | 0.696875 | 0.976252 | 0.696875 | 0.044823 | 0.193048 | 완화된 perturbation 조건에서는 설명 안정성과 bound proxy가 개선됨 |

## 7. 해석

Clean accuracy와 robust accuracy 사이의 차이는 일반 성능만으로 모델 안전성을 주장하기 어렵다는 점을 보여준다. Explanation stability는 입력 변화가 설명 결과를 얼마나 흔드는지 보는 지표이며, certified rate는 이 toy 선형 모델에서만 가능한 간단한 bound proxy다. 따라서 본 결과는 대규모 DNN에 대한 완전한 formal verification이나 실제 안전중요 시스템의 보증으로 해석하지 않는다.

이 결과는 synthetic binary classification 기반 toy 실험의 평가 형식 검증용 수치이며, 실제 대규모 DNN formal verification, 실제 안전중요 시스템 보증, 실제 운영 모델의 강건성 또는 XAI 안정성으로 일반화하지 않는다.

## 8. 재현성 점검

| 항목 | 상태 | 근거 |
|---|---|---|
| Seed 고정 | 완료 | `configs/config.yaml` |
| 실행 스크립트 보존 | 완료 | `src/run_experiment.py` |
| CSV 결과 | 완료 | `outputs/metrics_summary.csv` |
| JSON 결과 | 완료 | `outputs/results.json` |
| 실행 로그 | 완료 | `outputs/run_log.md` |
| 개인정보 제외 | 완료 | synthetic data only |
| 문서 수치 동기화 | 완료 | 보고서·제출본·발표자료는 outputs 기준 |

## 9. 한계

본 실습은 교육용 toy evaluation이다. 대적 예제 생성, robust training, formal bound, XAI attribution을 모두 단순화했으며 실제 운영 모델 침해, 안전중요 시스템 공격, 개인정보 기반 평가는 포함하지 않는다.
