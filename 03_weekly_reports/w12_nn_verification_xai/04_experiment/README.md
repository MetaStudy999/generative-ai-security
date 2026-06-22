# W12 실습 폴더

이 폴더는 신경망 검증·정형방법 & 대적방어·XAI·강건성 트레이드오프 주차의 Docker 기반 실습 환경, 설정, 결과, 로그, 실습보고서를 관리한다.

## 구성

- `experiment_report.md`: 실습 목표, 실행 절차, 결과 해석
- `src/run_experiment.py`: synthetic toy robustness/XAI 평가 스크립트
- `outputs/metrics_summary.csv`: 주요 지표 CSV
- `outputs/results.json`: 메타데이터와 지표 JSON
- `outputs/run_log.md`: 실행 로그와 결과 요약
- `Dockerfile`: 재현 가능한 Python 실행 환경
- `docker-compose.yml`: 로컬 컨테이너 실행 예시
- `pyproject.toml`: uv sync용 주차별 Python 의존성
- `configs/config.yaml`: seed, 데이터, 보안 범위, 결과 기록 상태

## 실행

```bash
python3 src/run_experiment.py --config configs/config.yaml
```

Docker 사용 시에는 다음 흐름을 따른다.

```bash
docker build -t w12-aisec .
docker run --rm -it -v "$(pwd)":/workspace w12-aisec bash
python src/run_experiment.py --config configs/config.yaml
```

## 의존성 설치 원칙

WSL 호스트에는 uv를 설치하지 않는다. Dockerfile은 `python:3.11-slim` 기반에서 `COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/`로 uv를 포함하고, 주차별 Python 패키지는 컨테이너 내부에서 `uv sync`로 설치한다.

## 원칙

실행 전에는 결과값을 작성하지 않는다. 실행 후에는 `outputs/metrics_summary.csv`, `outputs/results.json`, `outputs/run_log.md`를 보존하고, 실험보고서·통합보고서·제출 체크리스트·AI 활용기록을 함께 갱신한다. W12는 2026-06-22에 synthetic toy 실험을 실행했으며, 보고서 수치는 outputs 산출물과 일치하는 값만 사용한다.

DOI, URL, 원문 세부 수치는 공식 검증 자료가 있을 때만 확정한다. 본 실험은 실제 안전중요 시스템 공격, 운영 모델 침해, 개인정보 기반 평가를 포함하지 않는다.
