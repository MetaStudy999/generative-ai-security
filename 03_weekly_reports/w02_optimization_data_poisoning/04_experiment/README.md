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

## 실행 방법

```bash
docker build -t w02-aisec .
docker run --rm -it -v $(pwd):/workspace w02-aisec bash
python src/run_experiment.py --config configs/config.yaml
```

호스트 Python 환경에 `scikit-learn`이나 uv를 설치하지 말고 위 Docker 절차로 실행한다.

## 안전 원칙

- 공개 toy 데이터셋만 사용한다.
- label-flipping과 trigger는 교육용 시뮬레이션으로 제한한다.
- 실제 서비스, 실제 개인정보, 무단 API, 악성코드, 운영 시스템 공격은 제외한다.
- 실행 로그가 생성되기 전까지 정량 결과를 임의로 작성하지 않는다.
