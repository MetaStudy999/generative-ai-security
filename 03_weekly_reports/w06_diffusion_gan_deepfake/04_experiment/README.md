# W06 실습 폴더

이 폴더는 확률생성모형(Diffusion/GAN) & 딥페이크 검출 주차의 Docker 기반 실습 환경, 설정, 결과, 로그, 실습보고서를 관리한다.

## 구성

- `experiment_report.md`: 실습 목표, 평가 설계, 결과 기록 위치
- `Dockerfile`: 재현 가능한 Python 실행 환경
- `docker-compose.yml`: 로컬 컨테이너 실행 예시
- `pyproject.toml`: uv sync용 주차별 Python 의존성
- `configs/config.yaml`: seed, 데이터, 보안 범위, 결과 기록 상태
- `src/run_experiment.py`: synthetic detector score 신뢰성 평가 실행 스크립트
- `outputs/`: 실행 결과 CSV, JSON, run log

## 의존성 설치 원칙

WSL 호스트에는 uv를 설치하지 않는다. Dockerfile은 `python:3.11-slim` 기반에서 `COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/`로 uv를 포함하고, 주차별 Python 패키지는 컨테이너 내부에서 `uv sync`로 설치한다.

## 원칙

실행 결과는 `outputs/metrics_summary.csv`, `outputs/results.json`, `outputs/run_log.md`에 보존한다. 보고서·통합보고서·제출 체크리스트·AI 활용기록은 이 산출물과 일치해야 한다. 실제 딥페이크 생성, 실제 개인정보 사용, 무단 서비스 질의는 포함하지 않는다.
