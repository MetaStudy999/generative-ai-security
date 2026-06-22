# W11 제출용 보고서

## 표지

| 항목 | 내용 |
|---|---|
| 주차 | W11 |
| 보고서 제목 | 차등프라이버시(DP) & 멤버십 추론 공격·방어 |
| 과목 범위 | AI 보안 |
| 작성일 | 2026-06-22 |
| 문서 상태 | 제출용 통합본 |
| 관련 산출물 위치 | `03_weekly_reports/w11_differential_privacy_mi/` |
| 실험 근거 | `04_experiment/outputs/run_log.md` |

## 초록

본 보고서는 차등프라이버시의 정의, privacy budget, DP-SGD, privacy accounting을 AI 원리 관점에서 정리하고, membership inference와 privacy leakage를 보안 평가 관점에서 분석한다. 문헌 5편은 DP misuse, DP-DL auditing, deep learning/FL DP, MI attack taxonomy, MI defense taxonomy를 담당한다. 실습은 실제 개인정보 없이 synthetic binary classification으로 수행했고, Non-DP baseline accuracy 0.956250, DP-like noise high accuracy 0.950000, MI attack accuracy 범위 0.512500-0.521875, privacy leakage score 범위 0.011769-0.016482를 기록했다. 단, `epsilon_proxy`는 정식 DP accountant 산출값이 아니므로 실제 DP 보장으로 해석하지 않는다.

**키워드:** differential privacy, DP-SGD, membership inference, privacy leakage, utility-privacy trade-off, privacy accounting, reproducibility

## 1. AI 원리 70%

DP는 인접 데이터셋의 출력 분포 차이를 제한해 개별 레코드 포함 여부가 모델 출력에서 과도하게 드러나지 않도록 한다. DP-SGD는 gradient clipping, noise injection, privacy accounting이 함께 있어야 의미가 있으며, 단순 noise addition만으로는 DP 보장을 주장할 수 없다.

## 2. 보안 이슈 30%

| 관점 | 관련 위협 | W11 평가 연결 |
|---|---|---|
| Confidentiality | membership inference, training data leakage | MI Attack Accuracy |
| Privacy | individual record exposure | Privacy Leakage Score |
| Integrity | DP misuse, missing accounting | DOI/config/log 검증 |
| Availability | utility degradation from noise | Accuracy, Utility Drop |
| Accountability | unverified privacy claim | AI 활용기록, outputs 보존 |

## 3. 문헌 요약

| ID | 문헌 | DOI/URL 상태 | 활용 |
|---|---|---|---|
| P01 | A Critical Review on the Use (and Misuse) of Differential Privacy in Machine Learning | arXiv `2206.04621`, ACM DOI 공식 확인 필요 | DP misuse와 reporting 책임 |
| P02 | Recent Advances of Differential Privacy in Centralized Deep Learning | arXiv `2309.16398`, ACM 최종본 대조 필요 | DP-DL auditing과 privacy-utility 개선 |
| P03 | Differential Privacy in Deep Learning: A Literature Survey | DOI 후보 `10.1016/j.neucom.2024.127663`; 로컬 PDF는 Fu et al. 대체 문헌 | DP deep learning/FL 보호 대상 비교 |
| P04 | Membership Inference Attacks on Machine Learning | arXiv `2103.07853`, ACM DOI 공식 확인 필요 | MI attack taxonomy |
| P05 | Defenses to Membership Inference Attacks | DOI 후보 `10.1145/3620667`; 로컬 PDF는 Bai et al. 대체 문헌 | MI defense와 trade-off |

## 4. Research Track

| 항목 | 내용 |
|---|---|
| 연구문제 | DP claim 검증을 위해 utility, MI risk, leakage, accounting, reproducibility를 어떻게 함께 보고할 것인가 |
| 대상 시스템 | 개인정보가 포함될 수 있는 ML/DL 학습 시스템 |
| 보호 자산 | 학습 데이터 포함 여부, confidence score, model output, evaluation log |
| 위협 | membership inference, training data leakage, DP misuse |
| 평가 지표 | Accuracy, MI Attack Accuracy, Privacy Leakage Score, Utility Drop, epsilon/accounting |
| 재현성 | seed 42, config, script, CSV/JSON/run log 보존 |
| 제외 범위 | 실제 개인정보, 실제 개인 대상 추론, 운영 모델/API 무단 질의 |

## 5. 실습/실험 결과

실습 코드는 `04_experiment/src/run_experiment.py`에 작성했다. 실행 명령은 `python3 src/run_experiment.py --config configs/config.yaml`이며 결과는 `04_experiment/outputs/`에 저장했다.

| 조건 | Accuracy | Train Accuracy | MI Attack Accuracy | Epsilon Proxy | Utility Drop | Privacy Leakage Score |
|---|---:|---:|---:|---:|---:|---:|
| Non-DP baseline | 0.956250 | 0.965625 | 0.515625 | 해당 없음 | 0.000000 | 0.014833 |
| DP-like noise low | 0.956250 | 0.965625 | 0.515625 | 8.000000 | 0.000000 | 0.014494 |
| DP-like noise medium | 0.962500 | 0.965625 | 0.512500 | 3.000000 | 0.000000 | 0.011769 |
| DP-like noise high | 0.950000 | 0.962500 | 0.521875 | 1.000000 | 0.006250 | 0.016482 |

이 결과는 synthetic toy 실험이다. `epsilon_proxy`는 정식 privacy accountant로 계산한 보장이 아니며, 실제 개인정보 보호 수준이나 운영 모델의 membership inference 위험으로 일반화하지 않는다.

## 6. 발표자료 위치

| 파일 | 용도 |
|---|---|
| `09_presentation/presentation_report.md` | 발표용 보고서 |
| `09_presentation/presentation_slides.md` | 슬라이드 원본 |
| `09_presentation/presentation_slides.html` | 브라우저 발표용 슬라이드 |
| `09_presentation/speaker_notes.md` | 발표자 대본 |
| `09_presentation/qna.md` | 예상 질문과 답변 |
| `09_presentation/one_page_handout.md` | 1페이지 배포자료 |

## 7. 기말논문 연결

추천 주제는 “AI 보안 연구에서 privacy claim을 검증하기 위한 다중지표 평가 프레임워크”이다. W11의 기여 후보는 DP reporting checklist, membership inference threat model, utility-privacy trade-off 실험표, seed/config/output 기반 재현성 구조이다.

## 8. AI 활용 고지

Codex를 사용해 로컬 파일 점검, 문헌 요약 구조화, 대체 PDF 표시, synthetic 실험 코드 작성과 실행, 제출용 보고서 및 발표자료 작성을 수행했다. 정량값은 `04_experiment/outputs/run_log.md`, `metrics_summary.csv`, `results.json`과 일치하는 값만 사용했다. 상세 기록은 `05_ai_worklog/`에 있다.

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
