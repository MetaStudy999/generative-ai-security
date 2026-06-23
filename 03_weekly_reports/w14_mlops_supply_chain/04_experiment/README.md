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

`04_experiment/` 폴더 밖에서 실행할 때:

```bash
python3 03_weekly_reports/w14_mlops_supply_chain/04_experiment/src/run_experiment.py --config 03_weekly_reports/w14_mlops_supply_chain/04_experiment/configs/config.yaml
```

`04_experiment/` 폴더 안에서 실행할 때:

```bash
python3 src/run_experiment.py --config configs/config.yaml
```

Docker 사용 시:

```bash
docker compose run --rm w14-mlops-supply-chain python3 src/run_experiment.py --config configs/config.yaml
```

`docker-compose.yml`의 기본 command는 대화형 점검을 위해 `bash`로 유지한다. 자동 실행이 필요할 때는 위 `docker compose run` 명령을 사용한다.

2026-06-23 점검에서 `docker compose build`와 위 실행 명령이 성공했으며, 컨테이너 내부에는 `pyyaml==6.0.3`만 설치되었다.

## 의존성 설치 원칙

WSL 호스트에는 uv를 설치하지 않는다. Dockerfile은 `python:3.11-slim` 기반에서 `COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/`로 uv를 포함하고, 주차별 Python 패키지는 컨테이너 내부에서 `uv sync`로 설치한다. 현재 코드는 표준 라이브러리 중심으로 동작하며, `pyyaml`만 있으면 YAML config를 읽고, 없으면 내장 단순 YAML parser로 fallback한다.

`pyproject.toml` 의존성은 재현성을 위해 `pyyaml`만 남겼다. `numpy`, `pandas`, `scikit-learn`, `matplotlib`은 현재 코드에서 사용하지 않으므로 제거했다.

## config 필드 사용 현황

| config 항목 | 코드 반영 여부 | 비고 |
|---|---|---|
| `week`, `topic`, `run_date`, `status` | 반영 | `results.json` metadata와 `run_log.md`에 기록 |
| `seed` | 반영 | synthetic data와 모델 학습 재현성에 사용 |
| `data.type`, `data.personal_data` | 반영 | metadata와 안전 범위 설명에 사용 |
| `data.train_samples`, `data.test_samples`, `data.feature_count`, `data.drift_shift` | 반영 | synthetic dataset 생성에 사용 |
| `experiment.model`, `epochs`, `learning_rate`, `l2`, `drift_threshold` | 반영 | toy logistic regression 및 drift alert 계산에 사용 |
| `experiment.results_recorded`, `experiment.notes` | 기록용 | config와 `results.json`에 보존되는 문서화 필드이며 실행 분기에는 사용하지 않음 |
| `security_scope.allowed`, `security_scope.disallowed` | 반영 | `results.json`, `audit_log.jsonl`에 기록 |
| `audit.required_fields` | 반영 | audit coverage 계산에 사용 |

`results.json`에는 full `config_sha256`, `dataset_sha256`, `model_sha256`가 보존된다. 보고서 표에는 가독성을 위해 dataset hash를 `sha256:b9e597bccdbde442`처럼 축약해 표시한다.

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

## 결과 해석 주의

Drift score 0.307626은 synthetic reference distribution과 drifted sample distribution 사이의 평균 표준화 feature shift이며, 실제 운영 장애 확률 또는 공격 성공률이 아니다. threshold 0.25를 초과했으므로 toy pipeline에서는 drift alert 조건으로 기록한다.

Audit coverage 1.000000은 toy audit record의 필수 필드 10개가 채워졌다는 뜻이고, 실제 기업 감사 완전성을 의미하지 않는다. Inventory coverage 1.000000은 toy AI BOM/ML artifact inventory 최소 항목의 name/type 충족률이며, 완전한 AI BOM이나 SBOM, license, vulnerability scan을 의미하지 않는다.

이 결과는 synthetic MLOps toy pipeline 기반 평가 형식 검증용 수치이며, 실제 model registry, CI/CD, Kubernetes, package vulnerability scanner, production telemetry, 실제 기업 공급망 보안 수준으로 일반화하지 않는다.
