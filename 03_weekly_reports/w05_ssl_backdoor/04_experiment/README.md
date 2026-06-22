# W05 실습 폴더

이 폴더는 자기지도학습·파운데이션 모델 & Poisoning/Backdoor 주차의 synthetic 2차원 표현공간 클러스터 기반 안전 toy 실험을 관리한다.

## 1. 구성

- `experiment_report.md`: 실습 목표, 평가 설계, 결과 기록 위치
- `Dockerfile`: Python 3.11 + uv 기반 실행 환경
- `docker-compose.yml`: 로컬 컨테이너 실행 예시, 기본 command는 `bash`
- `pyproject.toml`: 현재 코드가 실제 사용하는 Python 의존성. `pyyaml`만 필요하다
- `configs/config.yaml`: seed, 데이터, 보안 범위, 결과 기록 상태
- `src/run_experiment.py`: synthetic representation backdoor toy 실험 스크립트
- `outputs/metrics_summary.csv`: 주요 지표 요약
- `outputs/results.json`: 설정, 지표, 예측 샘플 기록
- `outputs/run_log.md`: 실행 명령, 결과표, 한계 기록

## 2. 실행

호스트 Python 실행:

```bash
python3 src/run_experiment.py --config configs/config.yaml
```

Docker 실행:

```bash
docker compose run --rm w05-ssl-backdoor python3 src/run_experiment.py --config configs/config.yaml
```

`docker-compose.yml`의 기본 command는 인터랙티브 점검을 위해 `bash`로 유지한다.

## 3. config.yaml 필드 사용 여부

| 필드 | 코드 사용 여부 | 비고 |
|---|---|---|
| `seed` | 계산 사용 | synthetic split, clean consistency noise seed |
| `run_date` | 기록 사용 | `outputs/run_log.md` 실행일 |
| `data.type` | 기록 사용 | `results.json` metadata |
| `data.personal_data` | 기록 사용 | 개인정보 미사용 명시 |
| `data.train_per_class` | 계산 사용 | train split 크기 |
| `data.test_per_class` | 계산 사용 | test split 크기 |
| `data.cluster_std` | 계산 사용 | cluster 생성 표준편차 |
| `experiment.results_recorded` | 기록 사용 | `results.json` metadata |
| `experiment.poison_rate` | 계산 사용 | poisoned sample 수 |
| `experiment.trigger_vector` | 계산 사용 | trigger 적용 embedding 이동 |
| `experiment.defense_threshold` | 계산 사용 | consistency distance threshold |
| `experiment.notes` | 기록 사용 | `results.json` metadata |
| `security_scope.allowed` | 기록 사용 | 안전 범위 명시 |
| `security_scope.disallowed` | 기록 사용 | 제외 범위 명시 |

## 4. 의존성 원칙

`run_experiment.py`는 `argparse`, `csv`, `json`, `math`, `random`, `pathlib` 등 표준 라이브러리 중심으로 동작한다. YAML 설정 파일을 읽기 위해 `pyyaml`만 필요하며, `numpy`, `pandas`, `scikit-learn`, `matplotlib`은 현재 코드에서 사용하지 않아 제거했다.

## 5. 안전 범위

본 실험은 synthetic 2D representation만 사용하며 실제 개인정보, 실제 서비스, 무단 공격 절차를 포함하지 않는다.

## 6. 한계

이 결과는 synthetic 2D representation toy 실험의 평가 형식 검증용 수치이며, 실제 SSL 모델, foundation model, 상용 시스템의 poisoning/backdoor 보안 성능으로 일반화하지 않는다.
