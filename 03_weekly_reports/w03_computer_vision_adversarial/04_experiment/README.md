# W03 실습 폴더

이 폴더는 컴퓨터비전 표현학습 & 비전 대적공격 주차의 안전한 synthetic toy 실험 환경, 설정, 결과, 로그, 실습보고서를 관리한다. 실험은 실제 CNN/ViT 공격 재현이 아니라 clean accuracy, robust accuracy, ASR, robust drop, confusion matrix, reproducibility evidence를 분리해 기록하는 최소 protocol이다.

## 구성

| 경로 | 역할 |
|---|---|
| `src/run_experiment.py` | synthetic 8x8 막대 이미지와 nearest-centroid model 기반 toy 실험 |
| `configs/config.yaml` | seed, 데이터, 모델, 공격/방어 점검, 출력 파일, 보안 범위 |
| `outputs/` | CSV, JSON, Markdown 실행 로그, PGM 예시 이미지 |
| `experiment_report.md` | 실험 목적, 안전 범위, 결과, 한계 |
| `Dockerfile` | Python 3.11-slim + uv 기반 재현 환경 |
| `docker-compose.yml` | 컨테이너 셸 진입용 compose 설정 |
| `pyproject.toml` | `pyyaml`만 포함한 최소 의존성 |

## 실행

로컬 Python 실행:

```bash
python3 src/run_experiment.py --config configs/config.yaml
```

Docker compose 실행:

```bash
docker compose run --rm w03-computer-vision-adversarial python src/run_experiment.py --config configs/config.yaml
```

`docker-compose.yml`의 기본 command는 `bash`로 유지한다. 따라서 컨테이너 안에서 수동 점검을 하려면 `docker compose run --rm w03-computer-vision-adversarial`을 사용할 수 있고, 자동 실험 실행은 위 명령처럼 `python src/run_experiment.py --config configs/config.yaml`을 명시한다.

## 의존성 정리

`run_experiment.py`는 표준 라이브러리 중심으로 작성되어 있으며, `pyyaml`이 있으면 YAML 파서를 사용하고 없으면 제한적인 fallback parser를 사용한다. `numpy`, `pandas`, `scikit-learn`, `matplotlib`은 현재 코드가 사용하지 않으므로 제거했다.

## config와 코드 대응

| config 항목 | 코드 반영 방식 |
|---|---|
| `seed` | train/test synthetic data 생성 seed |
| `data.type` | `synthetic_8x8_bar_images` validation |
| `data.personal_data` | `false` validation; 개인정보 미사용 안전 조건 |
| `data.image_size` | 8x8 이미지 크기 |
| `data.n_train_per_class`, `data.n_test_per_class` | 클래스별 train/test 샘플 수 |
| `data.stroke_value`, `data.background_value`, `data.noise_std` | synthetic 막대 이미지 픽셀 생성 |
| `model.type` | `nearest_centroid` validation 및 결과 메타데이터 |
| `attack.type`, `attack.epsilons` | centroid-direction L-infinity toy perturbation 조건 |
| `defense.type`, `defense.levels`, `defense.epsilon` | 2-level feature squeezing check |
| `outputs.*` | CSV, JSON, run log, PGM 파일명 |
| `security_scope.allowed`, `security_scope.disallowed` | 결과 메타데이터와 run log 기록 |

기록용 필드:

- `status`: 사람이 보는 실행 상태 메모다.
- `experiment.results_recorded`, `experiment.notes`: 보고서 관리용 설명 필드다.

## 출력 파일

실행 결과는 다음 파일로 저장된다.

| 파일 | 내용 |
|---|---|
| `outputs/metrics_summary.csv` | 조건별 metrics table |
| `outputs/results.json` | metadata, rows, 예시 배열 |
| `outputs/run_log.md` | 제출 보고서에 붙일 수 있는 실행 로그 |
| `outputs/clean_example.pgm` | clean synthetic 예시 |
| `outputs/adversarial_eps_0_30.pgm` | epsilon 0.30 toy perturbation 예시 |
| `outputs/feature_squeezed_eps_0_30.pgm` | feature squeezing 예시 |

정량 실험 결과는 실행 로그가 있는 값만 보고서에 반영한다. epsilon 0.45 결과는 실제 CNN/ViT 공격 성공이 아니라 synthetic two-class toy decision boundary 전환이다.
