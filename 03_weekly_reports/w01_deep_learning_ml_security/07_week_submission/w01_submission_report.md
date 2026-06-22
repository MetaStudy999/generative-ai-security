# W01 제출용 보고서

## 표지

| 항목 | 내용 |
|---|---|
| 주차 | W01 |
| 보고서 제목 | 딥러닝 패러다임 & ML 보안 분류학 |
| 과목 범위 | AI 보안 |
| 작성자 | 박영세 |
| 학번 | 26200122 |
| 작성일 | W01 주차 일정 |
| 문서 상태 | 제출용 통합본 |
| 관련 산출물 위치 | `03_weekly_reports/w01_deep_learning_ml_security/` |

## 초록

본 보고서는 딥러닝 패러다임과 ML 보안 분류학을 연결하여, 인공지능 모델을 단순한 정확도 산출 도구가 아니라 데이터, 학습, 검증, 배포, 모니터링이 결합된 ML 시스템으로 해석한다. 이를 위해 딥러닝의 표현학습, 역전파, 일반화, 과적합 개념을 정리하고, ML 생명주기 보증, 침입탐지, 대적 공격, 프라이버시 공격 문헌을 비교하였다. 또한 safe synthetic toy evaluation을 수행하여 clean baseline, label-noise training, feature perturbation 조건에서 성능 변화를 확인하고, privacy-safe overfitting audit을 통해 실제 개인정보나 운영 시스템을 사용하지 않는 안전한 실습 절차를 제시하였다. 결론적으로 ML 보안 평가는 clean performance, robust performance, privacy leakage, reproducibility evidence를 분리해 기록해야 하며, 이 프레임은 기말 논문의 “ML 생명주기 기반 AI 보안 평가 프레임워크”로 확장될 수 있다.

**키워드:** 딥러닝, ML 보안, 생명주기 보증, 대적 공격, 프라이버시 공격, 재현성

## 1. 서론

딥러닝은 이미지, 음성, 자연어 등 복잡한 데이터에서 높은 성능을 보이는 핵심 AI 기술이다. 그러나 AI 보안 관점에서 중요한 질문은 단순히 “정확도가 높은가”가 아니다. 모델이 어떤 데이터로 학습되었는지, 어떤 공격자 가정에서 평가되었는지, 입력 교란이나 라벨 품질 저하에 얼마나 취약한지, 학습 데이터의 민감 정보가 출력이나 모델 파라미터에 반영될 수 있는지까지 함께 검토해야 한다.

W01의 목적은 이후 주차의 poisoning, adversarial example, privacy attack, MLOps supply chain 논의를 해석하기 위한 기준 프레임을 만드는 것이다. 본 보고서는 딥러닝 원리 70%, 보안 이슈 30%의 비중으로 구성하며, 문헌 분석과 안전한 toy 실습을 결합한다.

## 2. 딥러닝 원리 정리

딥러닝의 핵심은 다층 신경망이 원시 입력에서 계층적 표현을 학습한다는 점이다. LeCun, Bengio, Hinton의 Deep learning 논문은 표현학습, 역전파, CNN/RNN 계열 모델의 기본 원리를 정리한다. 보안 관점에서 이 원리는 중요하다. 공격자가 모델 입력이나 데이터 분포를 조작할 때 실제로 영향을 받는 것은 모델의 내부 표현과 decision boundary이기 때문이다.

학습은 손실함수를 최소화하는 파라미터를 찾는 과정이며, 일반화는 학습 데이터 밖에서도 성능이 유지되는지를 의미한다. 과적합은 일반적인 성능 저하 문제에 그치지 않고 membership inference와 같은 privacy leakage 위험의 배경이 될 수 있다. 따라서 AI 보안 보고서에서는 clean accuracy뿐 아니라 일반화 격차, 공격 조건 성능, 프라이버시 위험을 분리해 기록해야 한다.

| 핵심 개념 | 의미 | 보안 연결 |
|---|---|---|
| 표현학습 | 원시 입력에서 유용한 특징을 모델이 직접 학습 | 대적 입력이 내부 표현을 왜곡할 수 있음 |
| 역전파 | gradient를 이용한 파라미터 갱신 | gradient 기반 공격의 기술적 배경 |
| 일반화 | 새 데이터에서도 성능이 유지되는 성질 | clean 성능과 robust 성능의 분리 필요 |
| 과적합 | 학습 데이터에 과도하게 맞는 상태 | privacy leakage와 membership inference 위험 신호 |

## 3. ML 보안 이슈 정리

ML 보안 이슈는 전통적인 CIA 관점과 accountability 관점으로 나누어 볼 수 있다. Confidentiality는 학습 데이터와 민감 정보 노출 문제로 이어지고, integrity는 adversarial example이나 poisoning처럼 모델 판단을 조작하는 공격과 연결된다. Availability는 침입탐지 모델의 오탐 증가나 미탐 증가처럼 운영 가능성을 흔드는 문제다. Accountability는 seed, config, 로그, 코드가 남아 있지 않아 보안 주장을 검증하지 못하는 문제와 연결된다.

| 보안 속성 | ML 보안 문제 | 대표 위협 |
|---|---|---|
| Confidentiality | 학습 데이터와 민감 정보 노출 | membership inference, model inversion |
| Integrity | 예측 결과 조작 | adversarial example, poisoning |
| Availability | 탐지 실패 또는 오탐 폭증 | IDS 미탐, 오탐 비용 증가 |
| Accountability | 결과 재현과 책임 추적 실패 | seed, config, 로그 누락 |

## 4. 관련 문헌 5편 요약

| ID | 논문 | 핵심 기여 | 본 보고서 활용 |
|---|---|---|---|
| P01 | Deep learning | 딥러닝의 표현학습과 역전파 원리 정리 | AI 원리의 배경 |
| P02 | Assuring the Machine Learning Lifecycle | ML 생명주기별 보증 요건과 방법 정리 | 위협모형과 재현성 프레임 |
| P03 | ML Methods for Cyber Security Intrusion Detection | 침입탐지 ML 방법과 평가 지표 분류 | 탐지 지표와 보안 데이터 한계 |
| P04 | Adversarial Attacks and Defenses in ML-Powered Networks | 대적 공격·방어 taxonomy와 방어 한계 정리 | robust 평가 기준 |
| P05 | Privacy Attacks in Machine Learning | privacy attack taxonomy와 threat model 정리 | leakage risk 평가축 |

다섯 편의 문헌은 서로 다른 층위의 문제를 다룬다. P01은 원리 중심, P02는 생명주기 보증 중심, P03은 보안 탐지 응용 중심, P04는 무결성 공격 중심, P05는 기밀성 공격 중심이다. 이를 종합하면 ML 보안 평가는 단일 모델 성능표가 아니라 공격자 지식, 보호 자산, 방어 가정, 평가 지표, 재현성 증거를 함께 기록하는 구조여야 한다.

## 5. ML 생명주기 기반 위협모형

본 보고서의 대상 시스템은 딥러닝 또는 일반 ML 모델을 포함한 보안 응용 시스템이다. 보호 자산은 학습 데이터, 모델 파라미터, 입력 데이터, 출력 정보, 평가셋, 운영 로그다. 공격자는 white-box, gray-box, black-box, data contributor, operator로 구분한다.

**그림 1. ML 생명주기 기반 보안 평가 프레임**

```text
Data -> Training -> Validation -> Deployment -> Monitoring
  |        |            |             |             |
라벨품질   poisoning    robust 평가    evasion       drift
민감정보   overfitting  leakage 평가   extraction    incident log
```

이 프레임에서 보안 평가는 모델 파일 하나가 아니라 데이터 관리, 학습, 검증, 배포, 모니터링 단계 전체를 대상으로 수행해야 한다. 특히 검증 단계에서 clean accuracy만 보고하면 입력 교란, privacy leakage, 재현성 부족을 놓칠 수 있다.

## 6. 평가방법

W01의 평가축은 다음 네 가지로 정리한다.

| 평가축 | 질문 | 대표 지표 또는 증거 |
|---|---|---|
| Clean performance | 정상 조건에서 잘 맞는가 | accuracy, precision, recall, F1 |
| Robust performance | 교란 조건에서도 유지되는가 | robust accuracy, attack impact |
| Privacy leakage | 데이터 포함 여부나 민감 정보가 새는가 | leakage risk, train-test gap, attack advantage |
| Reproducibility | 같은 결과를 다시 만들 수 있는가 | seed, config, code, logs, DOI/URL 검증 |

이 구분의 핵심은 clean accuracy와 security robustness를 분리하는 것이다. 정상 조건 성능이 높더라도 라벨 오염, 입력 교란, 모델 추출, membership inference 등 보안 조건에서는 다른 결과가 나올 수 있다.

## 7. 실습 설계

실습은 안전한 synthetic toy evaluation으로 제한하였다. 실제 개인정보, 실제 운영 서비스, 무단 API 질의, 악성코드 실행은 포함하지 않았다. 실습 소스는 `04_experiment/src/run_experiment.py`에 작성했으며 Python 표준 라이브러리만 사용한다.

| 항목 | 내용 |
|---|---|
| 데이터 | synthetic binary classification data |
| 모델 | toy logistic regression |
| 조건 1 | clean baseline |
| 조건 2 | label-noise training |
| 조건 3 | toy feature perturbation |
| 조건 4 | privacy-safe overfitting/confidence audit |
| 결과 위치 | `04_experiment/outputs/` |

## 8. 실습 결과

실습은 `python3 src/run_experiment.py`로 실행되었고, 결과는 `metrics_summary.csv`, `results.json`, `run_log.md`로 저장되었다.

| 조건 | Accuracy | Precision | Recall | F1 | 보안 해석 |
|---|---:|---:|---:|---:|---|
| Clean baseline | 0.869444 | 0.867403 | 0.872222 | 0.869806 | 정상 synthetic test split 기준 |
| Label-noise training | 0.838889 | 0.827957 | 0.855556 | 0.841530 | training label 126개 flip 후 성능 저하 |
| Toy feature perturbation | 0.844444 | 0.848315 | 0.838889 | 0.843575 | Gaussian feature noise 조건에서 성능 저하 |

Privacy-safe audit 결과 train accuracy는 0.857143, test accuracy는 0.869444, train-test gap은 -0.012301로 나타났고 risk label은 `low_overfitting_signal`로 기록되었다. 이 결과는 synthetic data의 과적합 신호 점검이며, 실제 데이터 대상 membership inference 공격 결과로 해석하지 않는다.

## 9. 결과 해석

실습 결과는 정상 조건 accuracy만으로 모델 보안성을 설명할 수 없다는 점을 보여준다. 라벨 노이즈 조건에서는 clean baseline보다 accuracy와 F1이 낮아졌고, feature perturbation 조건에서도 성능 저하가 관찰되었다. 이는 ML 보안 평가에서 데이터 품질, 입력 안정성, 교란 조건 평가가 별도로 필요함을 의미한다.

다만 본 실습은 synthetic toy evaluation이므로 실제 운영망 보안성을 직접 대표하지 않는다. 본 보고서에서 주장할 수 있는 범위는 “평가축을 분리해 기록하는 방식의 예시”와 “라벨 품질 저하 및 입력 교란이 성능에 영향을 줄 수 있음을 안전한 환경에서 확인”한 수준이다.

## 10. 한계와 오픈 문제

첫째, synthetic toy data는 실제 보안 데이터셋의 class imbalance, concept drift, 공격 다양성을 충분히 반영하지 못한다. 둘째, survey taxonomy를 실제 시스템 평가로 연결하려면 공격자 지식, 데이터셋, 방어 설정, 운영 환경을 추가로 명시해야 한다. 셋째, privacy risk는 단일 지표로 요약하기 어렵고 utility/privacy trade-off를 동반한다. 넷째, 재현성 증거는 보안 주장 자체가 아니라 보안 주장을 검토할 수 있게 하는 최소 조건이다.

## 11. 기말 논문 연결

W01은 기말 논문의 상위 프레임을 제공한다. 발전 가능한 주제는 “ML 생명주기 기반 AI 보안 평가 프레임워크”이다. 이후 주차의 poisoning, adversarial example, LLM security, RAG prompt injection, federated learning, differential privacy, MLOps supply chain 이슈를 데이터 관리, 모델 학습, 검증, 배포·운영 단계에 매핑할 수 있다.

예상 기여는 다음과 같다.

1. ML 생명주기 단계별 보안 위협 분류
2. clean, robust, privacy, reproducibility 평가축 통합
3. 주차별 문헌을 연결한 AI 보안 평가 체크리스트 제안
4. safe toy evaluation과 문헌 매트릭스를 결합한 재현 가능한 분석 절차 제시

## 12. AI 활용 고지

| 항목 | 작성 내용 |
|---|---|
| 사용한 AI 도구명 | Codex |
| 사용 일자 | W01 주차 일정 |
| 사용 목적 | 논문 요약 보강, 개념 설명, 보고서 구조화, DOI/URL 검증표 정리, 실습 소스 작성, 제출용 보고서 통합 |
| AI 산출물 반영 위치 | `03_weekly_reports/w01_deep_learning_ml_security/` 하위 Markdown 및 HTML 파일 |
| 본인 검토 필요 항목 | 최종 제출 양식, 원문 세부 수치, 참고문헌 스타일 |
| 사실관계 검증 방법 | 로컬 PDF 메타데이터, DOI/arXiv 페이지, 실행 로그, 수업 자료와 대조 |
| 실험결과 처리 | `src/run_experiment.py` 실행 로그 기준으로 synthetic toy 결과만 기록 |
| 최종 책임 확인 | 최종 제출자는 원고의 내용, 인용, 실험결과, 연구윤리 책임을 확인해야 한다. |

## 13. 참고문헌

1. Yann LeCun, Yoshua Bengio, and Geoffrey Hinton, “Deep learning,” Nature, 521, 436-444, 2015. DOI: 10.1038/nature14539.
2. Rob Ashmore, Radu Calinescu, and Colin Paterson, “Assuring the Machine Learning Lifecycle: Desiderata, Methods, and Challenges,” ACM Computing Surveys, 54(5), 2021. DOI: 10.1145/3453444.
3. Anna L. Buczak and Erhan Guven, “A Survey of Data Mining and Machine Learning Methods for Cyber Security Intrusion Detection,” IEEE Communications Surveys & Tutorials, 18(2), 1153-1176, 2016. DOI: 10.1109/COMST.2015.2494502.
4. Yulong Wang, Tong Sun, Shenghong Li, Xin Yuan, Wei Ni, Ekram Hossain, and H. Vincent Poor, “Adversarial Attacks and Defenses in Machine Learning-Powered Networks: A Contemporary Survey,” arXiv preprint, 2023. DOI: 10.48550/arXiv.2303.06302.
5. Maria Rigaki and Sebastian Garcia, “A Survey of Privacy Attacks in Machine Learning,” ACM Computing Surveys, 2023. DOI: 10.1145/3624010.

## 14. 제출 전 점검표

| 점검 항목 | 상태 | 근거 |
|---|---|---|
| 논문 5편 요약 반영 | 완료 | `02_paper_summaries/` |
| 논문 비교표 반영 | 완료 | `02_paper_summaries/paper_matrix.md` |
| AI 원리 70% 반영 | 완료 | `03_theory_notes/ai_principle_70.md` |
| 보안 이슈 30% 반영 | 완료 | `03_theory_notes/security_issue_30.md` |
| Research Track 반영 | 완료 | 위협모형, 평가방법, 오픈문제 |
| 실습 소스 작성 | 완료 | `04_experiment/src/run_experiment.py` |
| 실습 결과 기록 | 완료 | `04_experiment/outputs/run_log.md` |
| DOI/URL 검증 | 완료 | `01_papers/doi_check.md` |
| AI 활용 고지 | 완료 | `05_ai_worklog/ai_disclosure_draft.md` |
| 발표자료 생성 | 완료 | `09_presentation/` |

## 부록 A. 제출 파일 위치

| 파일 | 설명 |
|---|---|
| `07_week_submission/w01_submission_report.md` | 본 제출용 보고서 |
| `06_report/final/integrated_report_final.md` | 주차 통합 최종보고서 |
| `04_experiment/src/run_experiment.py` | 실습 소스 |
| `04_experiment/outputs/run_log.md` | 실습 실행 로그 |
| `01_papers/doi_check.md` | DOI/URL 검증표 |
| `05_ai_worklog/ai_disclosure_draft.md` | AI 활용 고지서 초안 |
| `09_presentation/w01_presentation.html` | 발표자료 |
