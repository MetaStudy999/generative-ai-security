# W02 실습 폴더

이 폴더는 대규모 최적화 & 데이터 오염 위협 주차의 Docker 기반 toy experiment를 관리한다. 실습은 scikit-learn의 공개 digits 데이터셋을 사용하며, 실제 개인정보나 운영 시스템은 포함하지 않는다.

## 구성

| 파일/폴더 | 용도 |
|---|---|
| `src/run_experiment.py` | clean baseline, label-flip, toy backdoor 평가 실행 |
| `configs/config.yaml` | seed, 데이터, 모델, 오염률, trigger 위치, 출력 파일 설정 |
| `experiment_report.md` | 실험 목적, 절차, 결과 기록 기준 |
| `pyproject.toml` | uv sync용 주차별 Python 의존성 |
| `Dockerfile` | 재현 가능한 Python 실행 환경 |
| `docker-compose.yml` | 로컬 컨테이너 실행 예시 |
| `outputs/` | 실행 후 CSV/JSON/로그가 저장되는 위치 |

## 의존성 설치 원칙

WSL 호스트에는 uv를 설치하지 않는다. Dockerfile은 `python:3.11-slim` 기반에서 `COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/`로 uv를 포함하고, 주차별 Python 패키지는 컨테이너 내부에서 `uv sync`로 설치한다.

현재 `src/run_experiment.py` 실행에는 `numpy`, `pyyaml`, `scikit-learn`이 직접 사용된다. `pandas`와 `matplotlib`은 향후 결과표/그림 자동 생성용 후보 의존성으로 보존했으며, 현재 실험 실행에는 필수적이지 않다.

## 실행 방법

```bash
docker build -t w02-aisec .
docker run --rm -it -v $(pwd):/workspace w02-aisec bash
python src/run_experiment.py --config configs/config.yaml
```

`docker-compose.yml`의 기본 command는 컨테이너에 들어가 점검할 수 있도록 `bash`로 유지한다. 실험을 compose로 바로 실행하려면 다음 명령을 사용한다.

```bash
docker compose run --rm w02-optimization-data-poisoning python src/run_experiment.py --config configs/config.yaml
```

호스트 Python 환경에 `scikit-learn`이나 uv를 설치하지 말고 위 Docker 절차로 실행한다.

## config-code 정합성

| config 항목 | 코드 반영 여부 | 비고 |
|---|---|---|
| `seed` | 사용 | train/test split, 모델 seed, poisoning sampling |
| `data.test_size` | 사용 | `train_test_split` |
| `data.name` | 기록용 | 현재 코드는 `sklearn.datasets.load_digits`를 고정 사용 |
| `model.max_iter` | 사용 | `LogisticRegression(max_iter=...)` |
| `poisoning.label_flip_rates` | 사용 | 5%, 10%, 20% label flip 반복 |
| `poisoning.label_flip_offset` | 사용 | 라벨을 다음 클래스로 이동 |
| `backdoor.poison_rate` | 사용 | 안전한 toy backdoor 오염 샘플 수 |
| `backdoor.target_label` | 사용 | trigger 조건 목표 라벨 |
| `backdoor.trigger_value` | 사용 | trigger 픽셀 값 |
| `backdoor.trigger_pixels` | 사용 | trigger 픽셀 위치 |
| `outputs.directory` | 사용 | 출력 폴더 |
| `outputs.metrics_csv` | 사용 | CSV 파일명 |
| `outputs.results_json` | 사용 | JSON 파일명 |
| `outputs.run_log` | 사용 | Markdown 로그 파일명 |
| `status` | 기록용 | 실행 로직에는 영향 없음 |

## 안전 원칙

- 공개 toy 데이터셋만 사용한다.
- label-flipping과 trigger는 교육용 시뮬레이션으로 제한한다.
- 실제 서비스, 실제 개인정보, 무단 API, 악성코드, 운영 시스템 공격은 제외한다.
- 실행 로그가 생성되기 전까지 정량 결과를 임의로 작성하지 않는다.

## outputs 확인

2026-06-22 점검 기준 다음 파일이 존재한다.

| 파일 | 존재 여부 | 비고 |
|---|---|---|
| `outputs/metrics_summary.csv` | 존재 | 실험 결과 CSV |
| `outputs/results.json` | 존재 | metadata와 row별 결과 |
| `outputs/run_log.md` | 존재 | 보고서 수치 기준 로그 |
