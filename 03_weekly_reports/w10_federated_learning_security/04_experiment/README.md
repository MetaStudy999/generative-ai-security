# W10 실습 폴더

이 폴더는 연합학습(FL) & FL 위협·방어·정책 주차의 Docker 기반 실습 환경, 설정, 결과, 로그, 실습보고서를 관리한다.

## 구성

- `experiment_report.md`: 실습 목표, 평가 설계, 결과 기록 위치
- `Dockerfile`: 재현 가능한 Python 실행 환경
- `docker-compose.yml`: 로컬 컨테이너 실행 예시
- `pyproject.toml`: uv sync용 주차별 Python 의존성
- `configs/config.yaml`: seed, 데이터, 보안 범위, 결과 기록 상태
- `src/run_experiment.py`: synthetic FL toy 실험 실행 코드
- `outputs/metrics_summary.csv`: 조건별 정량 지표
- `outputs/results.json`: 설정, 결과, round log 원본
- `outputs/run_log.md`: 사람이 읽는 실행 로그

## 의존성 설치 원칙

WSL 호스트에는 uv를 설치하지 않는다. Dockerfile은 `python:3.11-slim` 기반에서 `COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/`로 uv를 포함하고, 주차별 Python 패키지는 컨테이너 내부에서 `uv sync`로 설치한다.

## 원칙

본 주차 실험은 2026-06-22에 synthetic toy data로 실행 완료했다. 결과값은 `outputs/metrics_summary.csv`, `outputs/results.json`, `outputs/run_log.md`를 근거로만 작성한다. DOI, URL, 원문 세부 수치, 실험 결과는 최종 검증 자료가 있을 때만 확정한다.
