# W04 실습 폴더

이 폴더는 Transformer 변형 & NLP 대적공격·프라이버시 주차의 안전한 toy 실험 환경, 설정, 결과, 로그, 실습보고서를 관리한다.

## 구성

- `experiment_report.md`: 실습 목표, 평가 설계, 결과 기록 위치
- `Dockerfile`: 재현 가능한 Python 3.11 실행 환경
- `docker-compose.yml`: 로컬 컨테이너 실행 예시
- `pyproject.toml`: uv sync용 주차별 Python 의존성
- `configs/config.yaml`: seed, 데이터, 보안 범위, 결과 기록 상태
- `src/run_experiment.py`: synthetic NLP 보안 실험 실행 스크립트
- `outputs/metrics_summary.csv`: 결과 요약 CSV
- `outputs/results.json`: 상세 결과 JSON
- `outputs/run_log.md`: 실행 로그와 결과 근거

## 실행 방법

로컬 Python 실행:

```bash
cd 03_weekly_reports/w04_transformer_nlp_security/04_experiment
python src/run_experiment.py --config configs/config.yaml
```

호스트에 `python` 명령이 없고 `python3`만 있는 환경에서는 다음 명령을 사용한다.

```bash
python3 src/run_experiment.py --config configs/config.yaml
```

Docker Compose 실행:

```bash
cd 03_weekly_reports/w04_transformer_nlp_security/04_experiment
docker compose run --rm w04-transformer-nlp-security python src/run_experiment.py --config configs/config.yaml
```

`docker-compose.yml`의 기본 `command`는 대화형 점검을 위해 `bash`로 유지한다. 실험 자동 실행은 위 `docker compose run` 명령을 사용한다.

## 설정 파일과 코드 일치

`load_config()`는 PyYAML이 설치되어 있으면 `configs/config.yaml` 전체를 읽어 `seed`, `run_date`, `data.type`, `data.personal_data`, `experiment.results_recorded`, `experiment.classifier`, `experiment.attack`, `experiment.defense`, `experiment.notes`, `security_scope.allowed`, `security_scope.disallowed`를 `results.json`에 보존한다.

PyYAML이 없거나 YAML 파싱이 실패하면 안전한 fallback으로 `seed`와 `run_date`만 직접 파싱한다. 이 경우 실험 수치 계산은 계속 가능하지만, 중첩 설정 메타데이터는 결과 JSON에 남지 않으므로 제출 전 PyYAML 환경에서 재실행하는 것이 좋다.

## 의존성 설치 원칙

현재 `run_experiment.py`는 `csv`, `json`, `random`, `re`, `pathlib` 등 표준 라이브러리 중심이며, `pyyaml`만 설정 파일 파싱에 optional로 사용한다. 재현성을 위해 `pyproject.toml` 의존성은 `pyyaml`만 남겼다.

## 안전 범위

실험은 synthetic 프라이버시 위험 프롬프트 기반 안전 toy 실험이다. 실제 개인정보, 실제 운영 서비스, 무단 API 질의, 실제 공격 절차는 포함하지 않는다. 결과는 `outputs/metrics_summary.csv`, `outputs/results.json`, `outputs/run_log.md`에 보존하고, 실험보고서·통합보고서·제출 체크리스트·AI 활용기록에 같은 값을 반영한다.
