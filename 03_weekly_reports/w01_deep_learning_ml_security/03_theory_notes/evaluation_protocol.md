# 평가방법

## 1. 평가 원칙

W01 평가방법은 정상 성능, 보안 강건성, 프라이버시 위험, 재현성을 분리해 기록한다. 하나의 accuracy 수치로 모델의 보안성을 주장하지 않는다.

## 2. 핵심 평가표

| 평가 항목 | 지표 | 측정 방법 | 필요한 데이터 | 비고 |
|---|---|---|---|---|
| Clean Performance | accuracy, precision, recall, F1 | 정상 test split에서 기준 모델 평가 | 공개 또는 synthetic 데이터 | 기본 성능 |
| Detection Quality | false positive rate, false negative rate | 보안 탐지 과제에서 오류 유형 분리 | IDS 또는 toy binary classification 데이터 | P03 연결 |
| Attack Impact | attack success rate, performance drop | 제한된 toy perturbation 또는 문헌 기반 시나리오 비교 | 변형 입력 또는 시나리오 표 | 실제 악용 절차 제외 |
| Robust Performance | robust accuracy, robustness gap | 공격/교란 조건과 clean 조건 비교 | 교란 데이터 | P04 연결 |
| Privacy/Leakage | attack advantage, leakage risk label | synthetic shadow data 또는 문헌 기반 위험 분류 | 실제 개인정보 금지 | P05 연결 |
| Lifecycle Assurance | evidence completeness | DOI, PDF, config, seed, log, review 기록 점검 | 문서와 설정 파일 | P02 연결 |
| Human Review | 검토 완료 여부 | 원문, DOI, 수치, 인용을 사람이 재검토 | 체크리스트 | 최종 책임 |

## 3. 최소 실험 프로토콜

1. 공개 또는 synthetic 데이터만 사용한다.
2. seed, 데이터 split, 모델 종류, 주요 hyperparameter를 config에 기록한다.
3. clean baseline을 먼저 평가한다.
4. 안전한 toy perturbation 또는 label noise 조건을 적용한다.
5. 성능 하락과 오류 유형을 기록한다.
6. 실제 개인정보, 실제 서비스 공격, 무단 질의는 수행하지 않는다.
7. 결과값은 실행 로그가 있을 때만 보고서에 적는다.

## 4. 결과 기록 양식

| 조건 | Accuracy | Precision | Recall | F1 | Attack/Leakage 지표 | 메모 |
|---|---:|---:|---:|---:|---:|---|
| Clean baseline | 실행 후 기록 | 실행 후 기록 | 실행 후 기록 | 실행 후 기록 | 해당 없음 | seed/config 확인 |
| Toy perturbation | 실행 후 기록 | 실행 후 기록 | 실행 후 기록 | 실행 후 기록 | ASR 또는 performance drop | 악용 세부 절차 제외 |
| Privacy-safe audit | 해당 시 기록 | 해당 시 기록 | 해당 시 기록 | 해당 시 기록 | leakage risk label | synthetic data만 사용 |

## 5. 해석 기준

- Clean 성능이 높아도 robust 성능이 낮으면 보안성 주장은 제한한다.
- Robust 성능이 좋아도 privacy leakage가 크면 기밀성 관점의 위험을 별도로 적는다.
- 실험값이 없으면 “실행 전”으로 표시하고, 문헌 기반 분석과 정량 실험을 혼동하지 않는다.
- P04는 현재 arXiv 논문 기준으로 정리되어 있으므로, 강의계획서 지정 IEEE Communications Surveys & Tutorials 논문과 동일 여부를 최종 제출 전 확인한다.
- 공개 GitHub 저장소에서는 출판사 PDF 원문 대신 DOI/URL, 서지정보, 요약만 남기는 것을 원칙으로 한다.

## 6. W01 outputs 기준 결과

| 조건 | Accuracy | Precision | Recall | F1 | 비고 |
|---|---:|---:|---:|---:|---|
| Clean baseline | 0.869444 | 0.867403 | 0.872222 | 0.869806 | `metrics_summary.csv` 기준 |
| Label-noise training | 0.838889 | 0.827957 | 0.855556 | 0.841530 | 126개 training label flip |
| Toy feature perturbation | 0.844444 | 0.848315 | 0.838889 | 0.843575 | Gaussian feature noise |

Privacy-safe audit은 train accuracy 0.857143, test accuracy 0.869444, train-test gap -0.012301, risk label `low_overfitting_signal`로 기록되었다. 이는 synthetic data의 과적합/confidence 신호 점검이며 실제 membership inference 공격 결과가 아니다.
