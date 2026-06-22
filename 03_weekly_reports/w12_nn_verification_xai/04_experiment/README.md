# W12 실습 폴더

이 폴더는 W12 신경망 검증, 정형방법, 대적방어, XAI 안정성, 강건성-정확도-공정성 trade-off 실습을 관리한다. 실습은 실제 운영 모델이나 안전중요 시스템이 아니라 synthetic binary classification 기반 안전 toy 실험으로 수행한다.

## 구성

- `experiment_report.md`: 실습 목표, 실행 절차, 결과 해석, 한계
- `src/run_experiment.py`: 표준 라이브러리 중심의 toy logistic classifier 실험 스크립트
- `configs/config.yaml`: seed, synthetic data, model, epsilon, 보안 범위 설정
- `outputs/metrics_summary.csv`: 주요 지표 CSV
- `outputs/results.json`: 메타데이터와 지표 JSON
- `outputs/run_log.md`: 실행 로그와 결과 요약
- `Dockerfile`: Python 3.11 + uv 기반 실행 환경
- `docker-compose.yml`: 컨테이너 실행용 compose 설정
- `pyproject.toml`: `pyyaml`만 포함한 최소 의존성

## 실행

로컬 Python 실행:

```bash
python3 src/run_experiment.py --config configs/config.yaml
```

Docker compose 실행:

```bash
docker compose run --rm w12-nn-verification-xai python3 src/run_experiment.py --config configs/config.yaml
```

`docker-compose.yml`의 기본 command는 대화형 점검을 위해 `bash`로 유지한다. 자동 실행은 위 compose 명령을 사용한다.

## config와 코드 정합성

| config 항목 | 코드 반영 상태 |
|---|---|
| `week`, `topic`, `run_date`, `status` | `results.json`과 `run_log.md` 메타데이터에 기록 |
| `seed` | train/test/model RNG에 반영 |
| `data.type`, `personal_data`, `train_samples`, `test_samples`, `features`, `noise` | synthetic dataset 생성과 로그에 반영 |
| `data.fairness_group_feature` | synthetic group 분할 feature index로 반영 |
| `experiment.model` | `toy_logistic_classifier` 지원 여부를 코드에서 검증 |
| `experiment.epochs`, `learning_rate`, `regularization`, `robust_regularization` | 학습 루프에 반영 |
| `experiment.epsilon`, `robust_augmentation_copies` | perturbation proxy와 robust augmentation에 반영 |
| `experiment.results_recorded`, `experiment.notes` | 실행 결과 감사용 기록 필드로 `results.json`에 보존 |
| `security_scope.allowed`, `security_scope.disallowed` | `run_log.md`와 `results.json`에 기록 |

## 해석 범위

`adversarial_features()`는 실제 PGD/FGSM 구현이 아니라 선형 모델 가중치 부호 기반 toy perturbation proxy다. `certified_rate`는 선형 로지스틱 모델의 margin과 L-infinity bound를 이용한 bound proxy이며, 실제 대규모 DNN formal verification certificate가 아니다.

이 결과는 synthetic binary classification 기반 toy 실험의 평가 형식 검증용 수치이며, 실제 대규모 DNN formal verification, 실제 안전중요 시스템 보증, 실제 운영 모델의 강건성 또는 XAI 안정성으로 일반화하지 않는다.
