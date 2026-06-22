# W12 제출용 보고서

## 표지

| 항목 | 내용 |
|---|---|
| 주차 | W12 |
| 보고서 제목 | 신경망 검증·정형방법 & 대적방어·XAI·강건성 트레이드오프 |
| 과목 범위 | AI 보안 |
| 작성일 | 2026-06-22 |
| 문서 상태 | 제출용 통합본 |
| 관련 산출물 위치 | `03_weekly_reports/w12_nn_verification_xai/` |
| 실험 근거 | `04_experiment/outputs/run_log.md` |

## 초록

본 보고서는 신경망 검증, abstraction, formal methods, robustness certificate를 AI 원리 관점에서 정리하고, 대적방어, XAI 공격면, robustness-accuracy-fairness trade-off를 보안 관점에서 분석한다. 문헌 5편은 verification abstraction, adversarial attack/defense, adversarial XAI, Lipschitz robustness, triangular trade-off를 담당한다. 실습은 실제 시스템이나 개인정보 없이 synthetic binary classification으로 수행했으며, clean model 기준 clean accuracy 0.818750, robust accuracy 0.543750, explanation stability 0.927782, certified rate 0.543750을 기록했다. 단, certified rate는 toy 선형 모델의 bound proxy이므로 대규모 DNN의 완전한 formal verification 결과로 해석하지 않는다.

**키워드:** neural network verification, formal methods, adversarial robustness, XAI stability, certified robustness, fairness gap, reproducibility

## 1. AI 원리 70%

신경망 검증은 입력 perturbation 범위에서 모델 출력이 명세를 만족하는지 확인하는 절차다. 경험적 평가는 테스트셋의 평균 성능을 측정하지만, 정형검증은 abstraction, reachability, bound, certificate를 사용해 보증 가능한 영역을 다룬다. XAI는 예측을 설명하는 도구지만, 설명 자체가 perturbation에 불안정하면 책임성과 신뢰성 평가가 약해진다.

## 2. 보안 이슈 30%

| 관점 | 관련 위협 | W12 평가 연결 |
|---|---|---|
| Confidentiality | explanation leakage | 설명이 민감 feature 의존성을 드러낼 수 있음 |
| Integrity | adversarial input, explanation manipulation | robust accuracy, explanation stability |
| Availability | verification scalability failure | verification cost |
| Safety | unverified robust behavior | certified rate와 제외 범위 명시 |
| Accountability | misleading explanation | XAI stability와 human review |
| Fairness | group별 성능 차이 | fairness gap |

## 3. 문헌 요약

| ID | 문헌 | DOI/URL 상태 | 활용 |
|---|---|---|---|
| P01 | A Review of Abstraction Methods Toward Verifying Neural Networks | 확인 필요, 로컬 PDF는 `SUBSTITUTE` | abstraction 기반 verification 분류 |
| P02 | Adversarial Attacks and Defenses in Deep Learning | 확인 필요, 로컬 PDF명 대조 필요 | 공격·방어 taxonomy |
| P03 | Adversarial machine learning attacks against explainable artificial intelligence: A review | 확인 필요, 로컬 PDF는 `SUBSTITUTE` | XAI 공격면 |
| P04 | Adversarial Robustness of Neural Networks from Lipschitz Regularization: A Survey | 확인 필요, 로컬 PDF는 `SUBSTITUTE` | Lipschitz robustness |
| P05 | The Triangular Trade-off between Robustness, Accuracy, and Fairness | 확인 필요, 로컬 PDF는 `SUBSTITUTE` | 강건성·정확도·공정성 trade-off |

## 4. Research Track

| 항목 | 내용 |
|---|---|
| 연구문제 | 신경망 검증, XAI 안정성, robustness-accuracy-fairness trade-off를 어떻게 하나의 보안 평가표로 보고할 것인가 |
| 대상 시스템 | 딥러닝 분류 모델, XAI 설명 시스템, verification pipeline |
| 보호 자산 | 모델 예측, 강건성 보증, 설명 결과, 공정성 지표, 안전 판단 |
| 위협 | adversarial input, explanation manipulation, verification scalability failure |
| 평가 지표 | Clean Accuracy, Robust Accuracy, Explanation Stability, Certified Rate, Fairness Gap, Verification Cost |
| 재현성 | seed 42, config, script, CSV/JSON/run log 보존 |
| 제외 범위 | 실제 안전중요 시스템 공격, 운영 모델 침해, 개인정보 기반 평가 |

## 5. 실습/실험 결과

실습 코드는 `04_experiment/src/run_experiment.py`에 작성했다. 실행 명령은 `python3 src/run_experiment.py --config configs/config.yaml`이며 결과는 `04_experiment/outputs/`에 저장했다.

| 조건 | Clean Accuracy | Robust Accuracy | Explanation Stability | Certified Rate | Fairness Gap | Verification Cost ms |
|---|---:|---:|---:|---:|---:|---:|
| Clean model | 0.818750 | 0.543750 | 0.927782 | 0.543750 | 0.039141 | 0.184215 |
| Adversarial input | 0.818750 | 0.543750 | 0.862321 | 0.340625 | 0.039141 | 0.176522 |
| Robust defense | 0.815625 | 0.543750 | 0.927152 | 0.543750 | 0.044823 | 0.151595 |
| XAI stability check | 0.815625 | 0.696875 | 0.976252 | 0.696875 | 0.044823 | 0.148367 |

이 결과는 synthetic toy 실험이다. certified rate는 선형 로지스틱 모델의 L-infinity bound proxy이며 실제 대규모 신경망의 formal verification 보증으로 일반화하지 않는다.

## 6. 발표자료 위치

| 파일 | 용도 |
|---|---|
| `09_presentation/presentation_report.md` | 발표용 보고서 |
| `09_presentation/presentation_report.html` | 브라우저용 발표 보고서 |
| `09_presentation/presentation_slides.md` | 슬라이드 원본 |
| `09_presentation/presentation_slides.html` | 브라우저 발표용 슬라이드 |
| `09_presentation/speaker_notes.md` | 발표자 대본 |
| `09_presentation/qna.md` | 예상 질문과 답변 |
| `09_presentation/one_page_handout.md` | 1페이지 배포자료 |

## 7. 기말논문 연결

추천 주제는 "강건성·설명안정성·공정성·재현성을 함께 보고하는 AI 보안 평가 프레임워크"이다. W12의 기여 후보는 verification/XAI/trade-off 문헌 비교표, multi-metric evaluation protocol, synthetic toy 실행 로그 기반 재현성 구조이다.

## 8. AI 활용 고지

Codex를 사용해 공통 지침 확인, W12 폴더 점검, toy 실험 코드 작성과 실행, 통합보고서·제출본·발표자료 작성을 수행했다. 정량값은 `04_experiment/outputs/run_log.md`, `metrics_summary.csv`, `results.json`과 일치하는 값만 사용했다. 상세 기록은 `05_ai_worklog/`에 있다.

## 9. 제출 전 점검표

| 점검 항목 | 상태 |
|---|---|
| 논문 요약 5편 | 완료 |
| 논문 비교표 | 완료 |
| AI 원리/보안 이슈 | 완료 |
| Research Track | 완료 |
| 실험 코드 | 완료 |
| 실험 결과 | 완료 |
| DOI/URL 검증표 | 부분 완료 |
| AI 활용 고지 | 완료 |
| 발표자료 | 완료 |
| 안전 범위 표시 | 완료 |
