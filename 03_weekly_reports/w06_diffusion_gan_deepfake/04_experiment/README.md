# W06 실습 폴더

이 폴더는 확률생성모형(Diffusion/GAN) & 딥페이크 검출 주차의 안전한 synthetic detector score toy 실험을 관리한다. 실제 딥페이크 생성, 실제 개인정보 사용, 실제 운영 서비스 질의는 포함하지 않는다.

## 구성

- `experiment_report.md`: 실습 목표, 평가 설계, 결과 기록 위치
- `Dockerfile`: 재현 가능한 Python 3.11 실행 환경
- `docker-compose.yml`: 로컬 컨테이너 실행 예시
- `pyproject.toml`: uv sync용 주차별 Python 의존성
- `configs/config.yaml`: seed, synthetic score 분포, threshold, review band, 보안 범위
- `src/run_experiment.py`: synthetic detector score 신뢰성 평가 실행 스크립트
- `outputs/`: 실행 결과 CSV, JSON, run log

## 실행

호스트 Python으로 실행:

```bash
python3 src/run_experiment.py --config configs/config.yaml
```

Docker compose로 실행:

```bash
docker compose run --rm w06-diffusion-gan-deepfake python3 src/run_experiment.py --config configs/config.yaml
```

`docker-compose.yml`의 기본 command는 대화형 점검을 위해 `bash`로 유지한다. 자동 실험 실행은 위 명령처럼 command를 명시한다.

## 의존성

현재 스크립트는 `argparse`, `csv`, `json`, `math`, `random`, `pathlib` 등 표준 라이브러리와 선택적 YAML 로딩용 `pyyaml`만 사용한다. 따라서 `pyproject.toml`에는 `pyyaml`만 남겼다. `numpy`, `pandas`, `scikit-learn`, `matplotlib`은 현재 실험 코드에서 사용하지 않아 제거했다.

## config.yaml 필드 사용 현황

| 필드 | 사용 방식 |
|---|---|
| `week`, `topic`, `run_date`, `status` | 실행 로그와 `results.json`에 보존되는 기록용 메타데이터 |
| `seed` | synthetic score 난수 생성에 사용 |
| `data.type`, `data.personal_data` | 안전 범위와 데이터 성격을 문서화하는 기록용 필드 |
| `data.n_per_label` | real/fake label별 sample 수 생성에 사용 |
| `data.domains.*.name` | sample ID와 로그의 도메인명에 사용 |
| `data.domains.*.real_mean`, `fake_mean`, `std` | synthetic detector score 분포 생성에 사용 |
| `experiment.detector_threshold` | threshold-based toy detector 판정에 사용 |
| `experiment.review_band` | human review routing 구간 계산에 사용 |
| `experiment.results_recorded`, `experiment.notes` | `results.json`에 보존되는 기록용 필드 |
| `security_scope.allowed`, `security_scope.disallowed` | 안전 범위 문서화와 결과 JSON 보존용 필드 |

## 산출물

실행 결과는 다음 파일에 보존한다.

- `outputs/metrics_summary.csv`
- `outputs/results.json`
- `outputs/run_log.md`

보고서·통합보고서·제출 체크리스트·AI 활용기록·발표자료는 이 산출물과 일치해야 한다.
