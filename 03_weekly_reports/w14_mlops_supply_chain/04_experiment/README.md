# W14 실습 폴더

이 폴더는 MLOps/DevOps·데이터/모델 파이프라인·공급망 보안 주차의 Docker 기반 실습 환경, 설정, 결과, 로그, 실습보고서를 관리한다.

## 구성

- `src/run_experiment.py`: synthetic toy MLOps pipeline 실행 코드
- `experiment_report.md`: 실습 목표, 평가 설계, 실행 결과
- `Dockerfile`: 재현 가능한 Python 실행 환경
- `docker-compose.yml`: 로컬 컨테이너 실행 예시
- `pyproject.toml`: uv sync용 주차별 Python 의존성
- `configs/config.yaml`: seed, 데이터, 보안 범위, 실행 상태
- `outputs/`: 실행 결과, hash, audit log, artifact inventory

## 실행 방법

```bash
python3 03_weekly_reports/w14_mlops_supply_chain/04_experiment/src/run_experiment.py --config 03_weekly_reports/w14_mlops_supply_chain/04_experiment/configs/config.yaml
```

Docker 사용 시:

```bash
docker build -t w14-aisec .
docker run --rm -it -v "$(pwd):/workspace" w14-aisec bash
python src/run_experiment.py --config configs/config.yaml
```

## 의존성 설치 원칙

WSL 호스트에는 uv를 설치하지 않는다. Dockerfile은 `python:3.11-slim` 기반에서 `COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/`로 uv를 포함하고, 주차별 Python 패키지는 컨테이너 내부에서 `uv sync`로 설치한다.

## 실행 결과

본 주차 실험은 2026-06-22에 synthetic toy data로 실행 완료했다. 핵심 결과는 다음과 같다.

| 항목 | 값 |
|---|---:|
| Baseline accuracy | 0.925000 |
| Baseline F1 | 0.923077 |
| Drift score | 0.307626 |
| Re-run consistency | true |
| Audit coverage | 1.000000 |
| Inventory coverage | 1.000000 |

정량값은 `outputs/run_log.md`, `outputs/metrics_summary.csv`, `outputs/results.json`을 근거로만 사용한다. DOI, URL, 원문 세부 수치는 최종 검증 자료가 있을 때만 확정한다.
