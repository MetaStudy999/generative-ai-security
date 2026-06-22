# W11 실습 폴더

이 폴더는 차등프라이버시(DP) & 멤버십 추론 공격·방어 주차의 Docker 기반 실습 환경, 설정, 결과, 로그, 실습보고서를 관리한다.

## 구성

- `experiment_report.md`: 실습 목표, 평가 설계, 결과 기록 위치
- `Dockerfile`: 재현 가능한 Python 실행 환경
- `docker-compose.yml`: 로컬 컨테이너 실행 예시
- `pyproject.toml`: uv sync용 주차별 Python 의존성
- `configs/config.yaml`: seed, 데이터, 보안 범위, 결과 기록 상태
- `src/run_experiment.py`: 표준 라이브러리 기반 synthetic toy 실험
- `outputs/`: 실행 후 생성되는 CSV/JSON/run log

## 의존성 설치 원칙

WSL 호스트에는 uv를 설치하지 않는다. Dockerfile은 `python:3.11-slim` 기반에서 `COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/`로 uv를 포함하고, 주차별 Python 패키지는 컨테이너 내부에서 `uv sync`로 설치한다. 현재 toy 실험은 표준 라이브러리만 사용하므로 호스트에서도 바로 실행할 수 있다.

## 실행

```bash
python3 src/run_experiment.py --config configs/config.yaml
```

## 원칙

실행 후에는 `outputs/metrics_summary.csv`, `outputs/results.json`, `outputs/run_log.md`를 보존하고, 실험보고서·통합보고서·제출 체크리스트·AI 활용기록을 함께 갱신한다. DOI, URL, 원문 세부 수치, 실험 결과는 최종 검증 자료가 있을 때만 확정한다.

본 실험의 `epsilon_proxy`는 정식 DP accountant 산출값이 아니라 noise 강도별 비교를 위한 proxy이다. 실제 DP 보장, 실제 개인정보 보호 수준, 실제 운영 모델의 membership inference 위험으로 일반화하지 않는다.
