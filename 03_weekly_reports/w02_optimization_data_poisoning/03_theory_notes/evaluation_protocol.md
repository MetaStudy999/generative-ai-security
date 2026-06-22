# W02 평가방법

## 1. 평가 항목

| 평가 항목 | 지표 | 측정 방법 | 필요한 데이터 | 비고 |
|---|---|---|---|---|
| Clean Accuracy | Accuracy, macro F1 | 정상 테스트셋 평가 | Clean test data | 기본 성능 |
| Poisoning Impact | Accuracy drop | 오염률별 모델 재학습 후 비교 | Poisoned train data | availability/integrity 영향 |
| Attack Success Rate | ASR | trigger 삽입 테스트 샘플의 목표 라벨 예측률 | Triggered test data | backdoor 효과 |
| Stealthiness | Clean accuracy 유지율 | clean accuracy와 ASR 동시 비교 | Clean/triggered data | 은닉성 |
| Detection | Detection rate, false positive | 이상치 또는 trigger 탐지 | Inspection data | 방어 평가 |
| Efficiency | Train time, model size, inference cost | 실행 로그와 모델 파일 비교 | Code/config/logs | P02 연결 |
| Reproducibility | Seed, config, command, package version | 동일 설정 반복 실행 | Docker, pyproject.toml/uv sync | 제출 신뢰성 |

## 2. 실험 조건

| 조건 | Poisoning Rate | Clean Accuracy | ASR | 해석 |
|---|---:|---:|---:|---|
| Clean baseline | 0% | 0.981481 | 해당 없음 | 기준 모델 |
| Label-flip | 5% | 0.918519 | 해당 없음 | 약한 오염 |
| Label-flip | 10% | 0.877778 | 해당 없음 | 중간 오염 |
| Label-flip | 20% | 0.818519 | 해당 없음 | 강한 오염 |
| Backdoor | 5% | 0.970370 | 0.987654 | clean 성능과 ASR 동시 확인 |

## 3. 보고 원칙

1. 실행하지 않은 정량값은 채우지 않는다.
2. W02 정량값은 `outputs/results.json`, `outputs/metrics_summary.csv`, `outputs/run_log.md` 기준으로 확정했다.
3. 로컬 호스트에 `scikit-learn`을 설치하지 않고 Docker에서 실행한다.
4. 공격 절차는 공개 toy 데이터셋에서만 사용하고, 실제 서비스나 개인정보에는 적용하지 않는다.
5. 최종 보고서에는 clean accuracy와 ASR을 반드시 분리해 기록한다.
