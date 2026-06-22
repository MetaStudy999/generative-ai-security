# W12 실험 보고서

## 1. 실험 목표

W12 실습은 신경망 검증, 대적 강건성, XAI 설명 안정성을 실제 운영 시스템이 아닌 synthetic toy 환경에서 함께 측정하는 것이다. 목표는 공격 절차를 재현하는 것이 아니라, clean accuracy, robust accuracy, explanation stability, certified rate, fairness gap, verification cost를 같은 로그 구조로 보고하는 연습이다.

## 2. 환경

| 항목 | 내용 |
|---|---|
| OS | Ubuntu 24.04 기준 |
| Container | Docker 사용 가능 |
| Python | 3.11 기준, 스크립트는 표준 라이브러리로 실행 가능 |
| Package manager | uv, Dockerfile 내부 포함 |
| Seed | 42 |
| 데이터 | synthetic binary classification |
| 개인정보 | 사용하지 않음 |
| 실행일 | 2026-06-22 |
| 결과 근거 | `outputs/metrics_summary.csv`, `outputs/results.json`, `outputs/run_log.md` |

## 3. 실험 설계

| 단계 | 설계 내용 | 기록 위치 |
|---|---|---|
| 기준 모델 | synthetic 4-feature binary data에 toy logistic classifier 학습 | `src/run_experiment.py` |
| 대적 입력 | 선형 모델 가중치 부호를 이용한 L-infinity epsilon perturbation proxy | `epsilon: 0.35` |
| Robust defense | 대적 증강 샘플과 더 큰 regularization으로 방어 모델 학습 | config 및 script |
| XAI 안정성 | clean/perturbed feature attribution의 cosine similarity 측정 | metrics |
| Certified robustness | 선형 모델 margin bound 기반 certified rate proxy 계산 | metrics |
| 공정성 영향 | synthetic group별 accuracy gap 측정 | metrics |
| Verification cost | bound 계산 시간(ms) 기록 | metrics |

## 4. 실행 명령

```bash
cd 03_weekly_reports/w12_nn_verification_xai/04_experiment
python3 src/run_experiment.py --config configs/config.yaml
```

Docker 사용 시에는 다음 흐름을 따른다.

```bash
docker build -t w12-aisec .
docker run --rm -it -v "$(pwd)":/workspace w12-aisec bash
python src/run_experiment.py --config configs/config.yaml
```

## 5. 실험 결과

| 조건 | Clean Accuracy | Robust Accuracy | Explanation Stability | Certified Rate | Fairness Gap | Verification Cost ms | 해석 |
|---|---:|---:|---:|---:|---:|---:|---|
| Clean model | 0.818750 | 0.543750 | 0.927782 | 0.543750 | 0.039141 | 0.184215 | 정상 성능은 높지만 perturbation에서 강건성이 낮아짐 |
| Adversarial input | 0.818750 | 0.543750 | 0.862321 | 0.340625 | 0.039141 | 0.176522 | 더 강한 perturbation 가정에서 설명 안정성과 certificate가 악화됨 |
| Robust defense | 0.815625 | 0.543750 | 0.927152 | 0.543750 | 0.044823 | 0.151595 | 단순 증강 방어만으로 robust accuracy 개선은 제한적 |
| XAI stability check | 0.815625 | 0.696875 | 0.976252 | 0.696875 | 0.044823 | 0.148367 | 완화된 perturbation 조건에서는 설명 안정성과 certificate가 개선됨 |

## 6. 해석

Clean accuracy와 robust accuracy 사이의 차이는 일반 성능만으로 모델 안전성을 주장하기 어렵다는 점을 보여준다. Explanation stability는 입력 변화가 설명 결과를 얼마나 흔드는지 보는 지표이며, certified rate는 이 toy 선형 모델에서만 가능한 간단한 bound proxy다. 따라서 본 결과는 대규모 DNN에 대한 완전한 formal verification이나 실제 안전중요 시스템의 보증으로 해석하지 않는다.

## 7. 재현성 점검

| 항목 | 상태 | 근거 |
|---|---|---|
| Seed 고정 | 완료 | `configs/config.yaml` |
| 실행 스크립트 보존 | 완료 | `src/run_experiment.py` |
| CSV 결과 | 완료 | `outputs/metrics_summary.csv` |
| JSON 결과 | 완료 | `outputs/results.json` |
| 실행 로그 | 완료 | `outputs/run_log.md` |
| 개인정보 제외 | 완료 | synthetic data only |

## 8. 한계

본 실습은 교육용 toy evaluation이다. 대적 예제 생성, robust training, formal bound, XAI attribution을 모두 단순화했으며 실제 운영 모델 침해, 안전중요 시스템 공격, 개인정보 기반 평가는 포함하지 않는다.
