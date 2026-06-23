# W13 실습 폴더

이 폴더는 모델 지식재산(IP)·모델 도난·모델 추출 위협 주차의 안전한 toy 실험 환경, 설정, 결과, 로그, 실습보고서를 관리한다.

## 구성

- `experiment_report.md`: 실습 목표, 평가 설계, 결과 해석
- `Dockerfile`: 재현 가능한 Python 3.11 실행 환경
- `docker-compose.yml`: 로컬 컨테이너 실행 예시
- `pyproject.toml`: uv sync용 주차별 Python 의존성
- `configs/config.yaml`: seed, 데이터, 보안 범위, 결과 기록 상태
- `src/run_experiment.py`: synthetic toy 모델 추출·워터마크 검출 스크립트
- `outputs/`: 실행 후 생성되는 CSV/JSON/run log

## 실행 명령

호스트에서 직접 실행할 수 있다.

```bash
cd 03_weekly_reports/w13_model_stealing_watermarking/04_experiment
python3 src/run_experiment.py --config configs/config.yaml
```

Docker Compose를 사용할 때는 `docker-compose.yml`의 command가 `bash`로 되어 있으므로 다음처럼 명시 실행한다.

```bash
cd 03_weekly_reports/w13_model_stealing_watermarking/04_experiment
docker compose run --rm w13-model-stealing-watermarking python3 src/run_experiment.py --config configs/config.yaml
```

## 의존성 정리

`run_experiment.py`는 `argparse`, `csv`, `json`, `math`, `random`, `time`, `pathlib`, `typing` 등 표준 라이브러리 중심으로 동작한다. `pyyaml`은 `configs/config.yaml`을 읽기 위한 optional 편의 의존성이며, import 실패 시 내장된 단순 YAML parser로 fallback한다. 따라서 `numpy`, `pandas`, `scikit-learn`, `matplotlib`은 제거했다.

## config 필드 사용 상태

| 필드 | 코드 반영 여부 | 메모 |
|---|---|---|
| `week`, `topic`, `seed`, `run_date`, `status` | 반영 | metadata/config에 기록 |
| `data.*` | 반영 | synthetic data 생성에 사용 |
| `experiment.epochs`, `learning_rate`, `regularization`, `query_budgets`, `watermark_triggers`, `watermark_fraction`, `trigger_radius` | 반영 | 학습·질의·trigger-set 구성에 사용 |
| `experiment.victim_model`, `experiment.substitute_model` | 기록용 | 결과 JSON에 기록되며 코드 분기에는 사용하지 않음 |
| `experiment.results_recorded`, `experiment.notes` | 기록용 | 결과 JSON에 기록되며 계산에는 사용하지 않음 |
| `security_scope.allowed`, `security_scope.disallowed` | 기록용 | run metadata와 보고서 안전 범위에 사용 |

## 안전 범위

`query_response_1nn_classifier`는 실제 모델 extraction 방어/공격 구현이 아니라 toy substitute model이다. `trigger_set`은 실제 watermarking scheme이 아니라 deterministic toy ownership signal이다.

이 결과는 synthetic binary classification 기반 toy 실험의 평가 형식 검증용 수치이며, 실제 상용 API, 실제 LLM, 실제 모델 탈취, 무단 대량 질의, 개인정보 기반 모델 추출 또는 소유권 분쟁 증거로 일반화하지 않는다.
