# W13 제출용 보고서

## 표지

| 항목 | 내용 |
|---|---|
| 주차 | W13 |
| 보고서 제목 | 모델 지식재산(IP)·모델 도난·모델 추출 위협 |
| 과목 범위 | AI 보안 |
| 작성일 | 2026-06-22 |
| 문서 상태 | 제출용 통합본 |
| 관련 산출물 위치 | `03_weekly_reports/w13_model_stealing_watermarking/` |
| 실험 근거 | `04_experiment/outputs/run_log.md` |

## 초록

본 보고서는 모델 지식재산, 모델 도난, 모델 추출, 워터마킹, 핑거프린팅을 AI 원리와 보안 이슈로 나누어 정리한다. 문헌 5편은 model stealing taxonomy, DNN/LLM watermarking, ModelShield, GAN privacy/security를 담당한다. 실습은 실제 API나 개인정보 없이 synthetic toy classifier로 수행했으며, query budget 100/500/1000에서 extraction fidelity 0.864000/0.920000/0.902000, watermark detection 0.700000/1.000000/1.000000을 기록했다. 다만 false positive proxy가 0.600000으로 높아, 본 실습은 소유권 검증의 필요성과 한계를 함께 보여주는 교육용 결과로 해석한다.

**키워드:** model stealing, model extraction, model watermarking, fingerprinting, query-response, extraction fidelity, false positive, reproducibility

## 1. AI 원리 70%

모델 IP는 파라미터와 구조뿐 아니라 학습 데이터, 출력 행동, 생성물 출처까지 포함한다. 모델 추출은 공개 API의 query-response 정보를 이용해 대체 모델을 학습하거나 원 모델 행동을 근사하는 과정이다. 워터마킹과 핑거프린팅은 추출 이후에도 소유권 또는 출처를 검증하기 위한 기술이지만, utility와 false positive를 함께 관리해야 한다.

## 2. 보안 이슈 30%

| 관점 | 관련 위협 | W13 평가 연결 |
|---|---|---|
| Confidentiality | model behavior leakage | extraction fidelity |
| Integrity | watermark removal/forgery | watermark detection |
| Availability | API query abuse | query budget |
| Privacy | stolen model based inference | 개인정보 제외 및 한계 표시 |
| Safety | misuse of stolen generative model | 생성모형 보조 문헌 |
| Accountability | ownership verification failure | false positive rate |

## 3. 문헌 요약

| ID | 문헌 | DOI/URL 상태 | 활용 |
|---|---|---|---|
| P01 | I Know What You Trained Last Summer | PDF DOI 표기 확인, 공식 대조 필요 | model stealing/extraction taxonomy |
| P02 | Watermarking Techniques for Large Language Models: A Survey | 대체 PDF, arXiv 표기 확인 | LLM watermarking 보조 배경 |
| P03 | A Survey of Deep Neural Network Watermarking Techniques | DOI/URL 확인 필요 | DNN watermarking trade-off |
| P04 | ModelShield | arXiv 표기 확인, 출판 정보 대조 필요 | extraction 이후 ownership check |
| P05 | Generative Adversarial Networks: A Survey Towards Private and Secure Applications | 대체 PDF, DOI/URL 확인 필요 | 생성모형 privacy/security 보조 배경 |

## 4. Research Track

| 항목 | 내용 |
|---|---|
| 연구문제 | query-response 기반 모델 추출 위험과 워터마크 기반 소유권 검증 신뢰성을 어떻게 함께 평가할 것인가 |
| 대상 시스템 | 공개 API 또는 제한 인터페이스로 제공되는 ML/LLM/생성모형 서비스 |
| 보호 자산 | 모델 파라미터, 출력 행동, 결정경계, 워터마크, fingerprint, 생성물 출처, API 로그 |
| 위협 | model stealing, model extraction, query abuse, watermark removal/forgery |
| 평가 지표 | extraction fidelity, substitute accuracy, query budget, watermark detection, false positive, utility accuracy |
| 재현성 | seed 42, config, script, CSV/JSON/run log 보존 |
| 제외 범위 | 실제 상용 API 공격, 무단 대량 질의, 실제 모델 탈취, 개인정보 기반 평가 |

## 5. 실습/실험 결과

실습 코드는 `04_experiment/src/run_experiment.py`에 작성했다. 실행 명령은 `python3 src/run_experiment.py --config configs/config.yaml`이며 결과는 `04_experiment/outputs/`에 저장했다.

| 조건 | Query Budget | Extraction Fidelity | Substitute Accuracy | Watermark Detection | False Positive Rate | Utility Accuracy |
|---|---:|---:|---:|---:|---:|---:|
| Baseline victim model | 0 | 1.000000 | 0.868000 | 1.000000 | 0.600000 | 0.868000 |
| Substitute query 100 | 100 | 0.864000 | 0.812000 | 0.700000 | 0.600000 |  |
| Substitute query 500 | 500 | 0.920000 | 0.840000 | 1.000000 | 0.600000 |  |
| Substitute query 1000 | 1000 | 0.902000 | 0.822000 | 1.000000 | 0.600000 |  |
| Watermarked ownership check | 0 | 1.000000 | 0.868000 | 1.000000 | 0.600000 | 0.868000 |

이 결과는 synthetic toy 실험이다. false positive proxy가 0.600000으로 높아, trigger-set detection만으로 소유권을 확정할 수 없으며 더 많은 대조군과 통계 검증이 필요하다.

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

추천 주제는 “모델 추출 이후 소유권 검증을 위한 다중지표 평가 프레임워크”이다. W13의 기여 후보는 query budget, extraction fidelity, watermark detection, false positive, utility accuracy를 같은 표에서 보고하는 절차다.

## 8. AI 활용 고지

Codex를 사용해 공통 지침 확인, 문헌 요약 보완, toy 실험 코드 작성·실행, 통합보고서·제출본·발표자료 작성을 수행했다. 상세 기록은 `05_ai_worklog/`에 있다. 정량값은 `04_experiment/outputs/run_log.md`, `metrics_summary.csv`, `results.json`과 일치하는 값만 사용했다.

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
| 대체 PDF 표시 | 완료 |
