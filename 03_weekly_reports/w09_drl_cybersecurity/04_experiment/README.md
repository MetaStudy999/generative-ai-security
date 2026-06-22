# W09 실습 폴더

이 폴더는 심층강화학습(DRL) & 사이버보안 적용·보상조작 주차의 synthetic cyber-defense state/action/reward 기반 안전 toy 실험 환경, 설정, 결과, 로그, 실습보고서를 관리한다. 실험 코드는 외부 패키지 없이 Python 표준 라이브러리만으로 실행 가능하다.

## 구성

| 파일/폴더 | 용도 |
|---|---|
| `src/run_experiment.py` | tabular Q-learning 기반 synthetic 실험 스크립트 |
| `configs/config.yaml` | seed, train/eval step, learning parameter, 보안 범위 |
| `outputs/metrics_summary.csv` | 조건별 정량 지표 |
| `outputs/results.json` | config, 조건, Q-table, 샘플 로그 |
| `outputs/run_log.md` | 보고서/발표 인용용 실행 로그 |
| `experiment_report.md` | 실험 설계와 결과 해석 |
| `Dockerfile`, `docker-compose.yml` | 컨테이너 재현 환경 |

## 실행

```bash
cd 03_weekly_reports/w09_drl_cybersecurity/04_experiment
python3 src/run_experiment.py --config configs/config.yaml
```

Docker compose의 기본 command는 `bash`로 유지한다. 컨테이너에서 실험을 자동 실행하려면 다음 명령을 사용한다.

```bash
cd 03_weekly_reports/w09_drl_cybersecurity/04_experiment
docker compose run --rm w09-drl-cybersecurity python3 src/run_experiment.py --config configs/config.yaml
```

`configs/config.yaml`의 `experiment.algorithm`과 `experiment.results_recorded`는 현재 버전에서 학습 분기 제어용이 아니라 결과 JSON과 보고서에 남기는 기록용 메타데이터다. 실제 학습 알고리즘은 `src/run_experiment.py`의 tabular Q-learning 구현으로 고정되어 있다.

## 결과 요약

| 조건 | Average Reward | Detection F1 | Safety Violation Rate | Policy Robustness |
|---|---:|---:|---:|---:|
| Normal reward | 1.085250 | 0.840206 | 0.011667 | 0.838417 |
| Manipulated reward | 0.521167 | 0.617512 | 0.195000 | 0.325000 |
| Robust reward design | 0.910833 | 0.780952 | 0.000000 | 0.709583 |

## 원칙

- 모든 입력은 synthetic toy state이며 실제 네트워크 트래픽, 실제 공격 payload, 개인정보는 포함하지 않는다.
- 결과 수치는 `outputs/run_log.md`, `metrics_summary.csv`, `results.json`과 일치하는 값만 보고서에 사용한다.
- 본 실험은 reward manipulation 효과를 설명하기 위한 재현 가능한 예시이며 실제 IDS/IPS 성능으로 일반화하지 않는다.
- Docker build와 compose 실행은 2026-06-23 보완 점검에서 성공했다.
