# W01 실습 폴더

이 폴더는 딥러닝 패러다임 & ML 보안 분류학 주차의 Docker 기반 실습 설계를 관리한다. W01 실습은 실제 서비스나 실제 개인정보를 대상으로 하지 않고, 공개 데이터 또는 synthetic data에서 ML 보안 평가 항목을 어떻게 기록할지 정의하는 데 목적이 있다.

실행 소스는 Python 표준 라이브러리만 사용하므로 별도 패키지 설치 없이 실행할 수 있다.

## 구성

- `experiment_report.md`: 실습 목표, 안전 범위, 평가 설계, 결과 기록 양식
- `src/run_experiment.py`: synthetic data 기반 실습 실행 소스
- `Dockerfile`: 재현 가능한 Python 실행 환경
- `docker-compose.yml`: 로컬 컨테이너 실행 예시
- `pyproject.toml`: uv sync용 주차별 Python 의존성
- `configs/config.yaml`: seed, 데이터, 보안 범위, 결과 기록 상태
- `outputs/`: 실행 후 결과 파일 저장 위치

## config/code 정합성 메모

`configs/config.yaml`의 `data.synthetic.n_redundant`와 `data.synthetic.n_classes`는 현재 버전에서는 기록용 필드다. `src/run_experiment.py`는 `n_samples`, `n_features`, `n_informative`, `class_sep`, `test_size`를 실제 synthetic data 생성에 사용하고, binary label은 score의 median threshold로 만든다. 결과 수치 변경을 피하기 위해 이번 보완에서는 실행 코드 로직을 바꾸지 않았다.

## 의존성 설치 원칙

WSL 호스트에는 uv를 설치하지 않는다. Dockerfile은 `python:3.11-slim` 기반에서 `COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/`로 uv를 포함하고, 주차별 Python 패키지는 컨테이너 내부에서 `uv sync`로 설치한다. W01은 별도 서드파티 패키지가 없으므로 `pyproject.toml`의 의존성 배열을 비워 둔다.

## 실행 원칙

1. 실제 개인정보와 실제 서비스 공격은 사용하지 않는다.
2. 공격 절차를 악용 가능하게 상세화하지 않는다.
3. 결과값은 실행 로그가 생긴 뒤에만 기록한다.
4. 문헌 기반 분석과 실험 결과를 구분한다.
5. 제출 시에는 seed, config, Docker 환경, 결과표의 빈칸 여부를 함께 설명한다.

## 실행 방법

패키지 설치 없이 직접 실행(선택):

```bash
python3 src/run_experiment.py
```

Docker Compose로 실행:

```bash
docker compose run --rm w01-deep-learning-ml-security python src/run_experiment.py
```

실행 결과는 `outputs/metrics_summary.csv`, `outputs/results.json`, `outputs/run_log.md`에 저장된다.
