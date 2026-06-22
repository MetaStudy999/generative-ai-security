# W03 실습 폴더

이 폴더는 컴퓨터비전 표현학습 & 비전 대적공격 주차의 Docker 기반 실습 환경, 설정, 결과, 로그, 실습보고서를 관리한다.

## 구성

- `experiment_report.md`: 실습 목표, 평가 설계, 결과 기록 위치
- `src/run_experiment.py`: synthetic toy 비전 대적공격 실험 실행 스크립트
- `outputs/`: CSV, JSON, Markdown 실행 로그, PGM 예시 이미지
- `Dockerfile`: 재현 가능한 Python 실행 환경
- `docker-compose.yml`: 로컬 컨테이너 실행 예시
- `pyproject.toml`: uv sync용 주차별 Python 의존성
- `configs/config.yaml`: seed, 데이터, 보안 범위, 결과 기록 상태

## 의존성 설치 원칙

WSL 호스트에는 uv를 설치하지 않는다. Dockerfile은 `python:3.11-slim` 기반에서 `COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/`로 uv를 포함하고, 주차별 Python 패키지는 컨테이너 내부에서 `uv sync`로 설치한다.

## 실행

```bash
python3 src/run_experiment.py --config configs/config.yaml
```

실행 결과는 `outputs/metrics_summary.csv`, `outputs/results.json`, `outputs/run_log.md`와 PGM 예시 이미지 3개로 저장된다.

## 원칙

정량 실험 결과는 실행 로그가 있는 값만 기록한다. DOI, URL, 원문 세부 수치는 최종 검증 자료가 있을 때만 확정한다.
