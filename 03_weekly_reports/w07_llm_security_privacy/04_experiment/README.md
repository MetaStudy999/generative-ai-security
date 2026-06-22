# W07 실습 폴더

이 폴더는 LLM 학습·정렬·평가 & LLM 보안·프라이버시 주차의 안전한 synthetic prompt score toy 실험을 관리한다. 실제 LLM/API 호출, 실제 개인정보, 실제 jailbreak 재현, 무단 서비스 질의, exploit instruction은 포함하지 않는다.

## 구성

- `experiment_report.md`: 실습 목표, 평가 설계, 결과 기록 위치
- `src/run_experiment.py`: synthetic prompt category와 rule-based toy guard score simulator
- `configs/config.yaml`: seed, 데이터 유형, guard threshold, 보안 범위, 결과 기록 상태
- `outputs/metrics_summary.csv`: 조건별 핵심 지표 CSV
- `outputs/results.json`: config, 조건 정의, 일부 synthetic sample, 지표 JSON
- `outputs/run_log.md`: 실행일, 명령, 수치, 한계 기록
- `Dockerfile`: Python 3.11 및 uv 기반 실행 환경
- `docker-compose.yml`: 로컬 컨테이너 shell 실행 예시
- `pyproject.toml`: 현재 코드에 필요한 최소 Python 의존성

## 실행

호스트 Python 실행:

```bash
python3 src/run_experiment.py --config configs/config.yaml
```

Docker 실행:

```bash
docker compose run --rm w07-llm-security-privacy python3 src/run_experiment.py --config configs/config.yaml
```

`docker-compose.yml`의 기본 command는 `bash`로 유지한다. 자동 실행이 필요할 때는 위 `docker compose run` 명령을 사용한다.

## 의존성

현재 `run_experiment.py`는 `argparse`, `csv`, `json`, `random`, `pathlib` 등 표준 라이브러리를 중심으로 동작하고, `configs/config.yaml`을 읽기 위해 `pyyaml`만 사용한다. 따라서 `pyproject.toml`의 의존성은 `pyyaml`만 남겼다.

## Config 메모

- `guard_threshold`는 refusal 판정에 실제 사용된다.
- `answer_threshold`는 현재 버전에서 판정 로직에 사용하지 않는 기록용 필드다. 향후 별도의 answerability score를 도입할 때 사용할 수 있다.
- `results_recorded`, `status`, `notes`, `security_scope`는 결과 JSON과 run log의 재현성/감사 메타데이터로 보존된다.

## 결과 원칙

실행 결과는 `outputs/metrics_summary.csv`, `outputs/results.json`, `outputs/run_log.md`에 보존한다. 실험보고서, 통합보고서, 제출 체크리스트, AI 활용기록, 발표자료는 이 출력물의 수치와 일치해야 한다.

이 결과는 synthetic prompt category와 rule-based toy guard score simulator를 사용한 평가 형식 검증용 수치이며, 실제 LLM의 보안 성능, 실제 jailbreak 성공률, 실제 개인정보 누출 가능성, 실제 코드 보안 품질로 일반화하지 않는다.
