# W01-W15 주차별 자동 점검 상태

생성일: 2026-06-24 01:38:39 KST

## 점검 범위

- 대상: `03_weekly_reports/w01`부터 `w15`까지의 주차별 보고서 폴더
- 제외: 참고문헌 진위 확인, 논문 질 평가, PDF 육안 확인, 기말논문 원고 편집
- 방식: 파일/폴더 존재, 문서 특징, 로컬 상대경로 링크, 0바이트 파일, config/output 일치, 로컬 문서 기반 수치·참고문헌 상태만 자동 점검

## 주차별 자동 점수

| 주차 | 폴더 | 점수 | 구조 | 보고서 | 발표 | 표/그림/수식 | 실험 | AI 고지 | 무결성 | 깨진 링크 | 0바이트 |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| W01 | `w01_deep_learning_ml_security` | 100 | 20 | 20 | 15 | 15 | 10 | 10 | 10 | 0 | 0 |
| W02 | `w02_optimization_data_poisoning` | 100 | 20 | 20 | 15 | 15 | 10 | 10 | 10 | 0 | 0 |
| W03 | `w03_computer_vision_adversarial` | 100 | 20 | 20 | 15 | 15 | 10 | 10 | 10 | 0 | 0 |
| W04 | `w04_transformer_nlp_security` | 100 | 20 | 20 | 15 | 15 | 10 | 10 | 10 | 0 | 0 |
| W05 | `w05_ssl_backdoor` | 100 | 20 | 20 | 15 | 15 | 10 | 10 | 10 | 0 | 0 |
| W06 | `w06_diffusion_gan_deepfake` | 100 | 20 | 20 | 15 | 15 | 10 | 10 | 10 | 0 | 0 |
| W07 | `w07_llm_security_privacy` | 100 | 20 | 20 | 15 | 15 | 10 | 10 | 10 | 0 | 0 |
| W08 | `w08_rag_prompt_injection` | 100 | 20 | 20 | 15 | 15 | 10 | 10 | 10 | 0 | 0 |
| W09 | `w09_drl_cybersecurity` | 100 | 20 | 20 | 15 | 15 | 10 | 10 | 10 | 0 | 0 |
| W10 | `w10_federated_learning_security` | 100 | 20 | 20 | 15 | 15 | 10 | 10 | 10 | 0 | 0 |
| W11 | `w11_differential_privacy_mi` | 100 | 20 | 20 | 15 | 15 | 10 | 10 | 10 | 0 | 0 |
| W12 | `w12_nn_verification_xai` | 100 | 20 | 20 | 15 | 15 | 10 | 10 | 10 | 0 | 0 |
| W13 | `w13_model_stealing_watermarking` | 100 | 20 | 20 | 15 | 15 | 10 | 10 | 10 | 0 | 0 |
| W14 | `w14_mlops_supply_chain` | 100 | 20 | 20 | 15 | 15 | 10 | 10 | 10 | 0 | 0 |
| W15 | `w15_reproducibility_xai_paper` | 100 | 20 | 20 | 15 | 15 | 10 | 10 | 10 | 0 | 0 |

## 구조 점수와 검증 점수 분리

| 주차 | 구조 자동 점수 | 수치 대조 점수 | 참고문헌 검증 점수 | 사람이 확인해야 할 항목 |
|---|---:|---:|---:|---|
| W01 | 100 | 100 | 100 | 자동 구조 점검 기준 주요 감점 없음 |
| W02 | 100 | 11 | 100 | 수치 대조: 확인 필요 |
| W03 | 100 | 100 | 100 | 자동 구조 점검 기준 주요 감점 없음 |
| W04 | 100 | 100 | 100 | 자동 구조 점검 기준 주요 감점 없음 |
| W05 | 100 | 100 | 100 | 자동 구조 점검 기준 주요 감점 없음 |
| W06 | 100 | 52 | 100 | 수치 대조: 확인 필요 |
| W07 | 100 | 100 | 100 | 자동 구조 점검 기준 주요 감점 없음 |
| W08 | 100 | 100 | 100 | 자동 구조 점검 기준 주요 감점 없음 |
| W09 | 100 | 48 | 100 | 수치 대조: 부분 대조 완료 |
| W10 | 100 | 100 | 100 | 자동 구조 점검 기준 주요 감점 없음 |
| W11 | 100 | 47 | 100 | 수치 대조: 확인 필요 |
| W12 | 100 | 100 | 100 | 자동 구조 점검 기준 주요 감점 없음 |
| W13 | 100 | 82 | 100 | 수치 대조: 부분 대조 완료 |
| W14 | 100 | 100 | 100 | 자동 구조 점검 기준 주요 감점 없음 |
| W15 | 100 | 100 | 100 | 자동 구조 점검 기준 주요 감점 없음 |

## 실험 상태와 outputs 일치 점검

| 주차 | config status | metrics | results | run_log | 그래프 | 상태 메모 |
|---|---|---:|---:|---:|---:|---|
| W01 | `source_ready_results_recorded` | O | O | O | O | executed 상태와 outputs 일치 |
| W02 | `executed` | O | O | O | O | executed 상태와 outputs 일치 |
| W03 | `executed` | O | O | O | O | executed 상태와 outputs 일치 |
| W04 | `executed_toy_experiment` | O | O | O | O | executed 상태와 outputs 일치 |
| W05 | `executed_toy_experiment` | O | O | O | O | executed 상태와 outputs 일치 |
| W06 | `executed_toy` | O | O | O | O | executed 상태와 outputs 일치 |
| W07 | `safe_synthetic_run` | O | O | O | O | executed 상태와 outputs 일치 |
| W08 | `executed` | O | O | O | O | executed 상태와 outputs 일치 |
| W09 | `executed` | O | O | O | O | executed 상태와 outputs 일치 |
| W10 | `executed` | O | O | O | O | executed 상태와 outputs 일치 |
| W11 | `executed` | O | O | O | O | executed 상태와 outputs 일치 |
| W12 | `executed` | O | O | O | O | executed 상태와 outputs 일치 |
| W13 | `executed` | O | O | O | O | executed 상태와 outputs 일치 |
| W14 | `executed` | O | O | O | O | executed 상태와 outputs 일치 |
| W15 | `executed` | O | O | O | O | executed 상태와 outputs 일치 |

## 우선순위 주차 수치 대조 결과

| 주차 | 상태 | 기준 원천 | 세부 메모 |
|---|---|---|---|
| W02 | 확인 필요 | `03_weekly_reports/w02_optimization_data_poisoning/04_experiment/outputs/metrics_summary.csv` | experiment_report.md 3/27 부분 대조: 사람이 세부 수치 확인 필요; w02_submission_report.md 4/27 부분 대조: 사람이 세부 수치 확인 필요; w02_submission_report.html 5/27 부분 대조: 사람이 세부 수치 확인 필요; presentation_slides.html 0/27 확인 필요: 기준 수치 토큰 미탐지 |
| W06 | 확인 필요 | `03_weekly_reports/w06_diffusion_gan_deepfake/04_experiment/outputs/metrics_summary.csv` | experiment_report.md 18/25 부분 대조: 사람이 세부 수치 확인 필요; w06_submission_report.md 17/25 부분 대조: 사람이 세부 수치 확인 필요; w06_submission_report.html 17/25 부분 대조: 사람이 세부 수치 확인 필요; presentation_slides.html 0/25 확인 필요: 기준 수치 토큰 미탐지 |
| W09 | 부분 대조 완료 | `03_weekly_reports/w09_drl_cybersecurity/04_experiment/outputs/metrics_summary.csv` | experiment_report.md 15/31 부분 대조: 사람이 세부 수치 확인 필요; w09_submission_report.md 20/31 부분 대조: 사람이 세부 수치 확인 필요; w09_submission_report.html 20/31 부분 대조: 사람이 세부 수치 확인 필요; presentation_slides.html 4/31 부분 대조: 사람이 세부 수치 확인 필요 |
| W11 | 확인 필요 | `03_weekly_reports/w11_differential_privacy_mi/04_experiment/outputs/metrics_summary.csv` | experiment_report.md 19/27 부분 대조: 사람이 세부 수치 확인 필요; w11_submission_report.md 16/27 부분 대조: 사람이 세부 수치 확인 필요; w11_submission_report.html 16/27 부분 대조: 사람이 세부 수치 확인 필요; presentation_slides.html 0/27 확인 필요: 기준 수치 토큰 미탐지 |
| W13 | 부분 대조 완료 | `03_weekly_reports/w13_model_stealing_watermarking/04_experiment/outputs/metrics_summary.csv` | experiment_report.md 15/15 자동 대조 완료; w13_submission_report.md 15/15 자동 대조 완료; w13_submission_report.html 15/15 자동 대조 완료; presentation_slides.html 4/15 부분 대조: 사람이 세부 수치 확인 필요 |
| W15 | 자동 대조 완료 | `03_weekly_reports/w15_reproducibility_xai_paper/04_experiment/outputs/metrics_summary.csv` | experiment_report.md 7/7 자동 대조 완료; w15_submission_report.md 7/7 자동 대조 완료; w15_submission_report.html 7/7 자동 대조 완료; presentation_slides.html 7/7 자동 대조 완료 |

## 참고문헌 검증 상태

| 주차 | 확인 완료(로컬 기록) | 확인 필요 | 부분 검증 | DOI/제목 불일치 후보 | 대체 문헌 후보 | 로컬 PDF 없음 | 검증 점수 |
|---|---:|---:|---:|---:|---:|---:|---:|
| W01 | 5 | 0 | 0 | 0 | 0 | 0 | 100 |
| W02 | 5 | 0 | 0 | 0 | 0 | 0 | 100 |
| W03 | 5 | 0 | 0 | 0 | 0 | 0 | 100 |
| W04 | 5 | 0 | 0 | 0 | 0 | 0 | 100 |
| W05 | 5 | 0 | 0 | 0 | 0 | 0 | 100 |
| W06 | 5 | 0 | 0 | 0 | 0 | 0 | 100 |
| W07 | 5 | 0 | 0 | 0 | 0 | 0 | 100 |
| W08 | 5 | 0 | 0 | 0 | 0 | 0 | 100 |
| W09 | 5 | 0 | 0 | 0 | 0 | 0 | 100 |
| W10 | 5 | 0 | 0 | 0 | 0 | 0 | 100 |
| W11 | 5 | 0 | 0 | 0 | 0 | 0 | 100 |
| W12 | 5 | 0 | 0 | 0 | 0 | 0 | 100 |
| W13 | 5 | 0 | 0 | 0 | 0 | 0 | 100 |
| W14 | 5 | 0 | 0 | 0 | 0 | 0 | 100 |
| W15 | 5 | 0 | 0 | 0 | 0 | 0 | 100 |

## 생성 또는 갱신된 상태 파일

- `03_weekly_reports/WEEKLY_STATUS.md`
- `03_weekly_reports/WEEKLY_STATUS.csv`
- `03_weekly_reports/WEEKLY_STATUS.json`
- `03_weekly_reports/WEEKLY_REFERENCE_VERIFICATION_AUDIT.md`
- `03_weekly_reports/WEEKLY_NUMERIC_CROSSCHECK_AUDIT.md`
- `03_weekly_reports/w15_reproducibility_xai_paper/00_management/W15_NUMERIC_AUDIT.md`

## 주차별 README 변경

- 갱신: `03_weekly_reports/w11_differential_privacy_mi/README.md`

## 주차별 README 존재 상태

- W01-W15 주차별 루트 `README.md`가 모두 존재함

## 누락 보완한 폴더

- 없음

## 자동 보완한 bridge/AI 고지/보고서 문장

- 없음


## 깨진 상대경로 링크

- 없음

## 0바이트 파일

- 없음

## 사람이 직접 확인해야 할 항목

- 참고문헌 DOI/URL/출판사 페이지의 실제 존재와 강의 지정문헌 일치 여부
- 논문 선정 품질, 요약의 학술적 타당성, 비판적 해석의 적절성
- PDF 원문 파일의 열람 가능성, 페이지 깨짐, 서식 및 그림 가독성
- 실험 수치의 과학적 의미, 재현성, 데이터/코드 실행 결과의 타당성
- AI 활용 고지 내용의 사실관계와 최종 제출 전 연구윤리 책임 확인
