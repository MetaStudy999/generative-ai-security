# W01 발표용 보고서

## 1. 발표 메타정보

| 항목 | 내용 |
|---|---|
| 주차 | W01 |
| 주제 | 딥러닝 패러다임 & ML 보안 분류학 |
| 발표 시간 | 8-10분 |
| 권장 슬라이드 수 | 10-13장 |
| 핵심 메시지 | 딥러닝 모델의 보안 평가는 clean 성능, robust 성능, privacy leakage, reproducibility evidence를 분리해서 기록해야 한다. |
| 발표 근거 | `06_report/final/integrated_report_final.md`, `04_experiment/outputs/run_log.md` |

## 2. 한 문장 요약

W01은 딥러닝을 정확도 중심 모델이 아니라 데이터, 학습, 검증, 배포, 모니터링이 연결된 ML 시스템으로 보고, 이후 주차의 공격과 방어를 해석할 공통 보안 평가 프레임을 만든다.

## 3. 발표 흐름

| 순서 | 슬라이드 주제 | 핵심 내용 | 시간 |
|---:|---|---|---:|
| 1 | 표지와 핵심 메시지 | W01의 기준 주차 역할 | 0:40 |
| 2 | 왜 중요한가 | “잘 맞는 모델”과 “보안적으로 충분한 모델”의 차이 | 1:00 |
| 3 | AI 원리 70% | 표현학습, 역전파, 일반화, 과적합 | 1:30 |
| 4 | 보안 이슈 30% | CIA, accountability, ML 생명주기 위험 | 1:20 |
| 5 | 논문 5편의 역할 | 원리, 생명주기, IDS, 대적 공격, 프라이버시 공격 연결 | 1:20 |
| 6 | 위협모형 | Data, training, validation, deployment, monitoring 단계별 위협 | 1:00 |
| 7 | 평가 프레임 | clean, robust, privacy, reproducibility 평가축 | 1:00 |
| 8 | Toy 실험 | synthetic data 기반 안전 실습 설계 | 0:50 |
| 9 | 실험 결과 | label noise와 feature perturbation 조건의 성능 변화 | 1:00 |
| 10 | Privacy-safe audit | train-test gap과 과적합 신호 점검 | 0:40 |
| 11 | 한계 | synthetic toy 결과의 일반화 금지 | 0:40 |
| 12 | 기말 연결 | ML 생명주기 기반 AI 보안 평가 프레임워크 | 0:40 |

## 4. 논문 5편의 발표 역할

| ID | 논문 | 발표에서 맡는 역할 | DOI/URL 상태 |
|---|---|---|---|
| P01 | Deep learning | 딥러닝의 표현학습, 역전파, 일반화 배경 설명 | 확인 |
| P02 | Assuring the Machine Learning Lifecycle | ML 생명주기 보증과 증거 기반 평가의 필요성 | 확인 |
| P03 | A Survey of Data Mining and Machine Learning Methods for Cyber Security Intrusion Detection | 보안 탐지에서 accuracy, false positive, false negative 분리 | 확인 |
| P04 | Adversarial Attacks and Defenses in Machine Learning-Powered Networks | robust 성능과 공격자 가정의 필요성 | 확인 |
| P05 | A Survey of Privacy Attacks in Machine Learning | privacy leakage와 공격자 지식 분류 | 확인 |

## 5. AI 원리 설명

- 딥러닝은 원시 입력에서 계층적 표현을 학습한다.
- 역전파는 손실함수의 gradient를 이용해 파라미터를 갱신한다.
- 일반화는 학습 데이터 밖에서도 성능이 유지되는 성질이다.
- 과적합은 성능 문제이면서 privacy leakage 위험 신호가 될 수 있다.

## 6. 보안 이슈 설명

| 보안 속성 | 발표 내용 |
|---|---|
| Confidentiality | 학습 데이터와 민감 정보가 membership inference, model inversion 등으로 노출될 수 있다. |
| Integrity | adversarial example, poisoning, label noise는 모델 판단을 조작한다. |
| Availability | IDS 미탐, 오탐 폭증, drift 미탐은 운영 가능성을 낮춘다. |
| Accountability | seed, config, 로그가 없으면 보안 주장을 재검토하기 어렵다. |

## 7. 실습/실험 결과

정량값은 `04_experiment/outputs/run_log.md` 기준이다.

| 조건 | Accuracy | Precision | Recall | F1 | 보안 해석 |
|---|---:|---:|---:|---:|---|
| Clean baseline | 0.869444 | 0.867403 | 0.872222 | 0.869806 | 정상 synthetic test split 기준 |
| Label-noise training | 0.838889 | 0.827957 | 0.855556 | 0.841530 | training label 126개 flip 후 성능 저하 |
| Toy feature perturbation | 0.844444 | 0.848315 | 0.838889 | 0.843575 | Gaussian feature noise 조건에서 성능 저하 |

Privacy-safe audit 결과 train accuracy는 0.857143, test accuracy는 0.869444, train-test gap은 -0.012301이며 risk label은 `low_overfitting_signal`이다. 이 결과는 synthetic data의 과적합 신호 점검이며 실제 데이터 대상 membership inference 공격 결과가 아니다.

## 8. 기말논문 연결

| 기말논문 장 | 발표에서 연결할 내용 |
|---|---|
| 서론 | ML 시스템 보안 평가는 정확도만으로 충분하지 않다는 문제 제기 |
| 관련연구 | 딥러닝 원리, ML lifecycle assurance, adversarial ML, privacy attack survey |
| 연구문제 | clean, robust, privacy, reproducibility를 통합한 평가 프레임 |
| 연구방법 | 문헌 매트릭스, 위협모형, safe toy evaluation, 재현성 체크리스트 |
| 분석/실험 | label noise, feature perturbation, privacy-safe audit |
| 보안적 함의 | CIA, accountability, lifecycle assurance 관점 |

## 9. 결론 메시지

1. 딥러닝 원리는 보안 취약성의 기술적 배경이다.
2. ML 보안 평가는 모델 하나가 아니라 생명주기 전체를 대상으로 해야 한다.
3. clean 성능, robust 성능, privacy leakage, reproducibility evidence를 분리해야 한다.
4. 실험 수치는 실행 로그와 CSV/JSON 근거가 있을 때만 주장한다.

## 10. 예상 질문과 답변

| 질문 | 답변 요지 | 근거 파일 |
|---|---|---|
| 왜 실제 보안 데이터셋을 쓰지 않았나? | W01의 목표는 공격 성능 경쟁이 아니라 안전한 toy 환경에서 평가축을 설명하는 것이다. | `04_experiment/experiment_report.md` |
| label-noise 결과가 poisoning 공격을 증명하나? | 아니다. 데이터 품질 저하가 성능에 영향을 줄 수 있음을 보여주는 축소 실험이다. | `04_experiment/outputs/run_log.md` |
| privacy-safe audit은 membership inference 공격인가? | 아니다. synthetic data에서 과적합과 confidence 신호를 점검한 것이다. | `04_experiment/outputs/results.json` |
| DOI/URL 검증은 어디에 있는가? | P01-P05의 DOI/URL과 검증 근거를 별도 표로 정리했다. | `01_papers/doi_check.md` |

## 11. 발표 전 점검

| 확인 | 점검 항목 |
|---|---|
| □ | 발표 수치가 `outputs/run_log.md`, `metrics_summary.csv`, `results.json`과 일치한다. |
| □ | synthetic toy 결과를 실제 운영망 보안성으로 일반화하지 않는다. |
| □ | privacy-safe audit을 실제 개인정보 공격 결과로 설명하지 않는다. |
| □ | 예상 질문 3개 이상을 준비한다. |
