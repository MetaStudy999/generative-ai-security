# 평가방법

| 평가 항목 | 지표 | 측정 방법 | 필요한 데이터 | 비고 |
|---|---|---|---|---|
| Defense Utility | Average Reward | true reward 기준 평균 보상 | synthetic event state | 조작 보상이 아니라 실제 목표 보상 |
| Detection Performance | Detection F1 | attack event에 대응 action을 선택했는지 계산 | attack label, action log | precision/recall 균형 |
| Safety | Safety Violation Rate | 공격 방치 또는 정상 이벤트 과잉 격리 비율 | action log | 자동 대응 안전성 |
| Reward Integrity | Observed Reward vs Average Reward | 학습 reward와 true reward 차이 비교 | reward log | reward hacking 탐지 단서 |
| Policy Robustness | Policy Robustness, Perturbed F1 | alert 관측 교란 조건에서 같은 정책 평가 | perturbed synthetic state | 상태 관측 조작 대응 |
| Reproducibility | Seed/config/output completeness | seed, config, CSV/JSON/run log 보존 | outputs 디렉터리 | 제출 재현성 |

## W09 실행 결과 연결

정량값은 `04_experiment/outputs/run_log.md`, `metrics_summary.csv`, `results.json` 기준으로만 사용한다.

| 조건 | Average Reward | Detection F1 | Safety Violation Rate | Policy Robustness | 해석 |
|---|---:|---:|---:|---:|---|
| Normal reward | 1.085250 | 0.840206 | 0.011667 | 0.838417 | 기준 보상은 높은 탐지 성능과 낮은 안전 위반을 보였다. |
| Manipulated reward | 0.521167 | 0.617512 | 0.195000 | 0.325000 | 조작 보상은 true reward와 robustness를 크게 낮췄다. |
| Robust reward design | 0.910833 | 0.780952 | 0.000000 | 0.709583 | 안전 위반을 제거했지만 오탐 비용으로 F1/보상이 일부 감소했다. |

## 실행 전제

- 모든 입력은 synthetic toy cyber-defense state이다.
- 실제 네트워크 트래픽, 실제 공격 payload, 개인정보는 사용하지 않는다.
- 결과 재생성 명령은 `python3 src/run_experiment.py --config configs/config.yaml`이다.
