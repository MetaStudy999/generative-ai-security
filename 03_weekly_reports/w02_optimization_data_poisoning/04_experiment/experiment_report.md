# W02 실험 보고서

## 1. 실험 목표

W02 실습은 대규모 최적화와 데이터 오염 위협의 연결을 안전한 공개 toy 환경에서 확인하기 위한 설계다. 목표는 실제 공격 수행이 아니라, label-flipping poisoning과 backdoor trigger가 평가 지표를 어떻게 분리하게 만드는지 이해하는 것이다.

## 2. 안전 범위

| 구분 | 허용 | 제외 |
|---|---|---|
| 데이터 | scikit-learn digits 공개 데이터셋 | 실제 개인정보, 운영 서비스 로그, 무단 수집 데이터 |
| 공격 시나리오 | label-flip 시뮬레이션, 단순 픽셀 trigger 기반 안전한 toy backdoor | 실제 서비스 침해, 악성코드, 무단 API 질의 |
| 결과 기록 | 실행 로그가 있는 정량값, config 기반 재현 정보 | 실행하지 않은 수치, 출처 없는 성능 주장 |

## 3. 환경

| 항목 | 내용 |
|---|---|
| OS | Ubuntu 24.04 기준 |
| Container | Docker |
| Python | 3.11 |
| Dataset | `sklearn.datasets.load_digits` |
| Seed | 42 |
| 현재 상태 | Docker 실행 완료, 정량 결과 `outputs/` 기록 완료 |

## 4. 실험 설계

본 실습은 실제 공격 재현이 아니라 W02의 핵심인 데이터 오염 평가축을 안전하게 설명하기 위한 최소 toy protocol이다. 따라서 scikit-learn digits와 logistic regression을 사용하되, 평가 구조는 이후 딥러닝 모델과 대규모 모델에도 확장 가능하도록 clean accuracy, macro F1, ASR, reproducibility evidence로 분리하였다.

| 단계 | 설계 내용 | 기록할 지표 | 현재 상태 |
|---|---|---|---|
| Clean baseline | 표준화 + Logistic Regression 학습 | accuracy, precision, recall, macro F1 | 실행 완료 |
| Label-flip 5% | 학습 라벨 5%를 다음 클래스로 변경 | accuracy drop, macro F1 | 실행 완료 |
| Label-flip 10% | 학습 라벨 10% 변경 | accuracy drop, macro F1 | 실행 완료 |
| Label-flip 20% | 학습 라벨 20% 변경 | accuracy drop, macro F1 | 실행 완료 |
| Safe toy backdoor 5% | 학습 샘플 일부에 하단 픽셀 trigger 삽입 후 target label 부여 | clean accuracy, ASR | 실행 완료 |

## 5. 실행 소스

| 항목 | 내용 |
|---|---|
| 소스 파일 | `src/run_experiment.py` |
| 입력 설정 | `configs/config.yaml` |
| 출력 파일 | `outputs/metrics_summary.csv`, `outputs/results.json`, `outputs/run_log.md` |
| Docker 실행 | `docker build -t w02-aisec .` 후 `python src/run_experiment.py --config configs/config.yaml` |

## 6. 결과 기록표

정량값은 Docker 컨테이너에서 실제 실행한 `outputs/run_log.md` 기준으로 기록했다.

| 조건 | Poisoning Rate | N Poisoned | Clean Accuracy | Macro F1 | ASR | 해석 |
|---|---:|---:|---:|---:|---:|---|
| Clean baseline | 0% | 0 | 0.981481 | 0.981443 | 해당 없음 | 기준 성능 |
| Label-flip | 5% | 63 | 0.918519 | 0.918457 | 해당 없음 | 약한 라벨 오염 |
| Label-flip | 10% | 126 | 0.877778 | 0.877582 | 해당 없음 | 중간 라벨 오염 |
| Label-flip | 20% | 251 | 0.818519 | 0.818134 | 해당 없음 | 강한 라벨 오염 |
| Safe toy backdoor | 5% | 63 | 0.970370 | 0.970359 | 0.987654 | clean 성능과 조건부 오분류 분리 |

## 7. 재현성 점검

- `configs/config.yaml`에 seed, 모델, 오염률, trigger 위치를 기록했다.
- Dockerfile 내부 uv sync와 pyproject.toml로 실행 환경을 고정했다.
- 결과값은 실제 실행 로그 `outputs/run_log.md` 기준으로 확정했다.
- 코드 실행 시 CSV, JSON, Markdown 로그가 동시에 생성된다.

## 8. 해석 기준

Label-flip 조건은 오염률이 높아질수록 clean accuracy와 macro F1이 낮아지는지를 확인한다. Safe toy backdoor 조건은 clean accuracy가 크게 유지되더라도 ASR이 높게 나올 수 있는지를 확인한다. 이 둘을 분리해야 poisoning과 backdoor를 같은 “오염”이라는 이름으로 뭉개지 않고 평가할 수 있다.

## 9. 한계

Digits는 작은 공개 데이터셋이므로 실제 대규모 모델, foundation model, LLM fine-tuning, 데이터 공급망 공격을 대표하지 않는다. 본 실습은 W02 발표와 보고서에서 평가 지표 구조를 설명하기 위한 안전한 최소 예시로만 사용한다.
