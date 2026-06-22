# W08 실습 폴더

이 폴더는 RAG·프롬프팅 프레임워크 & 프롬프트 인젝션 주차의 안전한 toy 실험 환경, 설정, 결과, 로그, 실습보고서를 관리한다.

## 구성

- `experiment_report.md`: 실습 목표, 평가 설계, 결과 기록 위치
- `Dockerfile`: 재현 가능한 Python 3.11 실행 환경
- `docker-compose.yml`: 로컬 컨테이너 실행 예시
- `pyproject.toml`: uv sync용 주차별 Python 의존성
- `configs/config.yaml`: seed, 데이터, 보안 범위, 결과 기록 상태
- `outputs/metrics_summary.csv`: 조건별 요약 수치
- `outputs/results.json`: config, 조건 정의, 요약 수치, 샘플 로그
- `outputs/run_log.md`: 사람이 읽는 실행 로그

## 실행 명령

로컬 Python 실행:

```bash
cd 03_weekly_reports/w08_rag_prompt_injection/04_experiment
python3 src/run_experiment.py --config configs/config.yaml
```

Docker Compose 실행:

```bash
cd 03_weekly_reports/w08_rag_prompt_injection/04_experiment
docker compose run --rm w08-rag-prompt-injection python3 src/run_experiment.py --config configs/config.yaml
```

`docker-compose.yml`의 기본 `command`는 대화형 점검을 위해 `bash`로 유지한다. 자동 실행이 필요할 때는 위 `docker compose run --rm ...` 명령을 사용한다.

## 의존성 설치 원칙

`pyproject.toml`의 `dependencies = []` 구조를 유지한다. W08 실험은 표준 라이브러리 기반 toy evaluator이며, 외부 패키지 없이 실행 가능하다.

코드는 `yaml` import를 먼저 시도하지만 PyYAML이 없어도 자체 `parse_simple_yaml()` fallback parser로 `configs/config.yaml`을 읽을 수 있다. 따라서 기본 실행에는 PyYAML 설치가 필요 없다.

## config.yaml과 코드 반영 상태

| config 항목 | 코드 반영 상태 | 비고 |
|---|---|---|
| `week` | 결과 JSON/run log에 보존 | 주차 메타데이터 |
| `topic` | 결과 JSON에 보존 | 주제 메타데이터 |
| `seed` | 사용 | `random.Random(seed)` |
| `run_date` | run log에 사용 | 실행일 기록 |
| `status` | 결과 JSON에 보존 | 실행 상태 |
| `data.type` | 결과 JSON에 보존 | synthetic RAG 문서 |
| `data.personal_data` | 결과 JSON에 보존 | 개인정보 미사용 |
| `data.n_per_condition` | 사용 | 조건별 샘플 수 |
| `data.top_k` | 기록용 필드 | 현재 toy evaluator는 실제 retrieval ranking을 수행하지 않아 계산에는 미사용 |
| `experiment.results_recorded` | 결과 JSON에 보존 | 보고서 정합성 확인용 |
| `experiment.risk_threshold` | 사용 | human approval 판단 |
| `experiment.source_filter_block_rate` | 사용 | source filter 차단 확률 |
| `experiment.human_approval_block_rate` | 사용 | approval gate 차단 확률 |
| `experiment.notes` | 결과 JSON에 보존 | 실험 범위 설명 |
| `security_scope.allowed` | 결과 JSON에 보존 | 허용 범위 |
| `security_scope.disallowed` | 결과 JSON에 보존 | 제외 범위 |

## 안전 범위

W08은 synthetic RAG 문서 기반 안전 toy 실험이다. 실제 LLM/API 호출, 실제 외부 시스템 공격, 실제 의료·금융 시스템 조작, 실제 개인정보 사용, live tool invocation은 포함하지 않는다.

이 결과는 synthetic RAG document와 rule-based toy evaluator를 사용한 평가 형식 검증용 수치이며, 실제 LLM 보안 성능이나 실제 RAG 제품의 안전성으로 일반화하지 않는다.
