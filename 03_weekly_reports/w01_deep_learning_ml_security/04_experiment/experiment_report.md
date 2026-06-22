# 실험 보고서

## 1. 실험 목표

W01 실습의 목표는 딥러닝/ML 보안 평가에서 어떤 지표를 기록해야 하는지 안전한 toy 환경으로 설계하는 것이다. 실험은 “정상 성능만 기록하면 보안성을 설명할 수 없다”는 W01 결론을 확인하는 구조로 둔다.

## 2. 안전 범위

| 구분 | 허용 | 제외 |
|---|---|---|
| 데이터 | 공개 데이터, synthetic data, toy binary classification data | 실제 개인정보, 실제 서비스 로그, 무단 수집 데이터 |
| 공격 시나리오 | label noise, 단순 perturbation, 문헌 기반 위험 분류 | 실제 서비스 침해, 악성코드, 무단 API 질의 |
| 결과 기록 | 실행 로그가 있는 정량값, 문헌 기반 정성 평가 | 실행하지 않은 수치, 출처 없는 성능 주장 |

## 3. 환경

| 항목 | 내용 |
|---|---|
| OS | Ubuntu 24.04 기준 |
| Container | Docker |
| Python | 3.11 |
| Seed | 42 |
| 데이터 | 공개 또는 synthetic 데이터 |
| 상태 | 실행 소스 작성 및 synthetic toy evaluation 실행 완료 |

## 4. 실험 설계

| 단계 | 설계 내용 | 기록할 지표 | 현재 상태 |
|---|---|---|---|
| Clean baseline | 기준 분류 모델을 학습하고 정상 test split에서 평가 | accuracy, precision, recall, F1 | 설계 완료 |
| Label-noise scenario | 안전한 비율의 라벨 노이즈 또는 synthetic perturbation을 적용 | 성능 하락, 오류 유형 | 설계 완료 |
| Robustness check | clean 조건과 perturbation 조건의 차이를 비교 | robustness gap | 설계 완료 |
| Privacy-safe audit | 실제 개인정보 없이 overfitting과 confidence exposure 위험을 정성 점검 | leakage risk label | 설계 완료 |
| Reproducibility check | seed, config, Docker, 실행 로그 보존 여부 점검 | evidence completeness | 설계 완료 |

## 5. 실행 소스

| 항목 | 내용 |
|---|---|
| 소스 파일 | `src/run_experiment.py` |
| 입력 설정 | `configs/config.yaml` |
| 출력 파일 | `outputs/metrics_summary.csv`, `outputs/results.json`, `outputs/run_log.md` |
| 실행 명령 | `python3 src/run_experiment.py` |

## 6. 실행 결과

실행 로그는 `outputs/run_log.md`에 저장했다.

| 조건 | Accuracy | Precision | Recall | F1 | 보안 지표 | 메모 |
|---|---:|---:|---:|---:|---:|---|
| Clean baseline | 0.869444 | 0.867403 | 0.872222 | 0.869806 | 해당 없음 | seed 42 |
| Label-noise training | 0.838889 | 0.827957 | 0.855556 | 0.841530 | performance drop | training label 126개 flip |
| Toy feature perturbation | 0.844444 | 0.848315 | 0.838889 | 0.843575 | robustness gap | Gaussian feature noise |
| Privacy-safe audit | 0.869444 | 해당 없음 | 해당 없음 | 해당 없음 | low_overfitting_signal | train-test gap -0.012301 |

## 7. 재현성 점검

- `configs/config.yaml`에 seed, 데이터 유형, 안전 범위, 결과 기록 상태를 둔다.
- Dockerfile 내부 uv sync와 pyproject.toml로 실행 환경을 고정한다.
- 결과값은 `outputs/metrics_summary.csv`, `outputs/results.json`, `outputs/run_log.md`에 보존한다.
- 실행 소스는 외부 패키지 없이 재실행 가능하도록 표준 라이브러리만 사용한다.

## 8. 해석

W01 실험은 공격 성공을 보여주는 데 목적이 있지 않다. 목표는 ML 보안 보고서에서 clean 성능, robust 성능, privacy risk, reproducibility evidence를 분리해 기록해야 함을 보여주는 것이다.

## 9. 한계

현재 실습은 synthetic data 기반의 안전한 toy evaluation이다. 실제 운영망, 실제 개인정보, 실제 공격 절차를 반영하지 않으므로 결과는 보안 평가 절차를 설명하는 예시로 해석해야 한다.
