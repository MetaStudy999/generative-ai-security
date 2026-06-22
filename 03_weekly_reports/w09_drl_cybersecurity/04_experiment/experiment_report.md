# W09 실험 보고서

## 1. 실험 목표

DRL 기반 사이버 방어 에이전트에서 reward manipulation이 정책 성능과 안전성에 미치는 영향을 안전한 synthetic toy 환경에서 확인한다. 실제 시스템 침해, 실제 네트워크 트래픽, 개인정보, 무단 공격 자동화는 제외한다.

## 2. 환경

| 항목 | 내용 |
|---|---|
| OS | Ubuntu 24.04 기준 |
| Container | Docker 또는 로컬 Python 3 |
| Python | 3.11 호환 스크립트, 표준 라이브러리 기반 |
| Algorithm | tabular Q-learning |
| Seed | 42 |
| 데이터 | synthetic toy cyber-defense states |
| 결과 상태 | 실행 완료, 2026-06-23 로컬 Python 및 Docker compose 재실행 확인 |

## 3. Toy 환경 정의

| 구성 | 값 |
|---|---|
| State | `(alert_level, asset_critical, vulnerable)` |
| Action | `monitor`, `isolate`, `patch`, `escalate` |
| True reward | 탐지 성공, 적절한 대응, 운영 비용, 안전 위반을 반영 |
| Manipulated reward | 공격 미대응 패널티를 약화하고 자동 격리 비용을 과장 |
| Robust reward | reward clipping, safety penalty, 불확실 상태 escalation 보상을 추가 |
| Safety violation | 공격 이벤트를 monitor로 방치하거나 정상 이벤트를 isolate하는 경우 등 |

## 4. 실행 절차

```bash
cd 03_weekly_reports/w09_drl_cybersecurity/04_experiment
python3 src/run_experiment.py --config configs/config.yaml
```

생성 산출물:

| 파일 | 내용 |
|---|---|
| `outputs/metrics_summary.csv` | 조건별 주요 지표 |
| `outputs/results.json` | config, 조건, 학습 Q-table, 샘플 로그 |
| `outputs/run_log.md` | 제출/보고서 인용용 실행 로그 |

## 5. 실험 결과

| 조건 | Average Reward | Detection F1 | Safety Violation Rate | Policy Robustness | 해석 |
|---|---:|---:|---:|---:|---|
| Normal reward | 1.085250 | 0.840206 | 0.011667 | 0.838417 | 기준 보상은 탐지 성능과 안전성 균형이 가장 좋았다. |
| Manipulated reward | 0.521167 | 0.617512 | 0.195000 | 0.325000 | 조작 보상은 true reward, F1, robustness를 낮추고 안전 위반을 높였다. |
| Robust reward design | 0.910833 | 0.780952 | 0.000000 | 0.709583 | 안전 위반을 제거했지만 false positive 비용 때문에 F1과 보상이 일부 낮아졌다. |

## 6. 해석

Observed reward 기준으로는 manipulated reward 조건이 나쁘지 않아 보일 수 있지만, true reward 기준 Average Reward는 0.521167로 떨어졌다. 이는 보상 신호가 조작되면 agent가 “좋은 점수”를 받는 방향으로 행동해도 실제 보안 목표는 악화될 수 있음을 보여준다.

## 7. 재현성 점검

- `configs/config.yaml`에 seed, train/eval step, learning parameter, security scope를 기록했다.
- `src/run_experiment.py`는 표준 라이브러리만 사용한다.
- 정량값은 `outputs/run_log.md`, `metrics_summary.csv`, `results.json`과 일치한다.
- `experiment.algorithm`과 `experiment.results_recorded`는 현재 버전에서 기록용 메타데이터이며, 실제 실행 알고리즘은 tabular Q-learning으로 고정되어 있다.
- 로컬 실행 명령과 Docker compose 실행 명령 모두 정상 종료했다.

## 8. 한계

이 결과는 synthetic toy cyber-defense state/action/reward simulation의 평가 형식 검증용 수치이며, 실제 IDS/IPS 제품, 실제 운영망, 실제 neural DRL policy의 보안 성능으로 일반화하지 않는다.
