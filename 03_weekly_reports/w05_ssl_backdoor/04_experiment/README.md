# W05 실습 폴더

이 폴더는 자기지도학습·파운데이션 모델 & Poisoning/Backdoor 주차의 Docker 기반 실습 환경, 설정, 결과, 로그, 실습보고서를 관리한다.

## 구성

- `experiment_report.md`: 실습 목표, 평가 설계, 결과 기록 위치
- `Dockerfile`: 재현 가능한 Python 실행 환경
- `docker-compose.yml`: 로컬 컨테이너 실행 예시
- `pyproject.toml`: uv sync용 주차별 Python 의존성
- `configs/config.yaml`: seed, 데이터, 보안 범위, 결과 기록 상태
- `src/run_experiment.py`: synthetic 표현공간 backdoor toy 실험 스크립트
- `outputs/metrics_summary.csv`: 주요 지표 요약
- `outputs/results.json`: 설정, 지표, 예측 샘플 기록
- `outputs/run_log.md`: 실행 명령, 결과표, 한계 기록

## 의존성 설치 원칙

WSL 호스트에는 uv를 설치하지 않는다. Dockerfile은 `python:3.11-slim` 기반에서 `COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/`로 uv를 포함하고, 주차별 Python 패키지는 컨테이너 내부에서 `uv sync`로 설치한다.

## 원칙

실행 결과는 `outputs/metrics_summary.csv`, `outputs/results.json`, `outputs/run_log.md`에 보존한다. DOI, URL, 원문 세부 수치, 실험 결과는 검증 자료가 있을 때만 확정한다.

## 실행

```bash
python3 src/run_experiment.py --config configs/config.yaml
```

본 실험은 synthetic 2D representation만 사용하며 실제 개인정보, 실제 서비스, 무단 공격 절차를 포함하지 않는다.
