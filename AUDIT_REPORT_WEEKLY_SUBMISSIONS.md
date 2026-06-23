# W01-W15 주차별 보고서 자동 감사 보고서

감사 기준일: 2026-06-24 00:18:52 KST

## 1. 자동 감사 원칙

- 대상은 `03_weekly_reports/` 아래 W01-W15 주차별 보고서 폴더로 제한했다.
- `04_final_paper/`, `06_submission/`, 논문 제출용 구조는 이동하거나 편집하지 않았다.
- 참고문헌 진위 확인, 논문 질 평가, PDF 육안 확인은 자동 정상 처리하지 않았다.
- 점수는 구조와 파일 존재, 문서 특징, 상대경로 링크, 0바이트 파일 여부를 중심으로 반영한다.
- 수치 대조는 로컬 `metrics_summary.csv`/`results.json`과 보고서 내 토큰 포함 여부를 비교하는 자동 보조 점검이며, 학술적 해석은 사람이 검토해야 한다.

## 2. 변경 전후 기록

- 기존 감사 보고서 백업: `AUDIT_REPORT_WEEKLY_SUBMISSIONS.backup.md (현재 감사 보고서로 갱신)`
- 상태 파일 생성/갱신: `03_weekly_reports/WEEKLY_STATUS.md`, `03_weekly_reports/WEEKLY_STATUS.csv`, `03_weekly_reports/WEEKLY_STATUS.json`
- 상세 검증표 생성/갱신: `03_weekly_reports/WEEKLY_REFERENCE_VERIFICATION_AUDIT.md`, `03_weekly_reports/WEEKLY_NUMERIC_CROSSCHECK_AUDIT.md`, `03_weekly_reports/w15_reproducibility_xai_paper/00_management/W15_NUMERIC_AUDIT.md`
- 주차별 README 변경:

- 없음

## 2-1. 자동 보완한 bridge/AI 고지/보고서 문장

- 없음


## 3. 주차별 README 존재 상태

- W01-W15 주차별 루트 `README.md`가 모두 존재함

## 4. 누락 보완한 폴더

- 없음

## 5. 주차별 자동 점수

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

## 5-1. 구조/검증 분리 감사표

| 주차 | 구조 | 보고서 | 발표자료 | 실험 outputs | 수치 대조 | 참고문헌 검증 | AI 고지 | bridge | 주요 감점 |
|---|---:|---:|---:|---:|---|---|---:|---|---|
| W01 | 20 | 20 | 15 | O | 기준 원천 존재 (100) | 88점 / 확인 필요 0, 불일치 1 | 10 | O | DOI/제목/저자 불일치 후보 1건 |
| W02 | 20 | 20 | 15 | O | 확인 필요 (11) | 46점 / 확인 필요 2, 불일치 0 | 10 | O | 참고문헌 확인 필요 2건; 대체 문헌 후보 1건; 수치 대조: 확인 필요 |
| W03 | 20 | 20 | 15 | O | 기준 원천 존재 (100) | 100점 / 확인 필요 0, 불일치 0 | 10 | O | 자동 구조 점검 기준 주요 감점 없음 |
| W04 | 20 | 20 | 15 | O | 기준 원천 존재 (100) | 20점 / 확인 필요 4, 불일치 0 | 10 | O | 참고문헌 확인 필요 4건 |
| W05 | 20 | 20 | 15 | O | 기준 원천 존재 (100) | 36점 / 확인 필요 2, 불일치 2 | 10 | O | 참고문헌 확인 필요 2건; DOI/제목/저자 불일치 후보 2건 |
| W06 | 20 | 20 | 15 | O | 확인 필요 (52) | 28점 / 확인 필요 3, 불일치 1 | 10 | O | 참고문헌 확인 필요 3건; DOI/제목/저자 불일치 후보 1건; 수치 대조: 확인 필요 |
| W07 | 20 | 20 | 15 | O | 기준 원천 존재 (100) | 42점 / 확인 필요 0, 불일치 3 | 10 | O | 부분 검증 문헌 1건; DOI/제목/저자 불일치 후보 3건; 대체 문헌 후보 1건 |
| W08 | 20 | 20 | 15 | O | 기준 원천 존재 (100) | 40점 / 확인 필요 2, 불일치 1 | 10 | O | 참고문헌 확인 필요 2건; 부분 검증 문헌 1건; DOI/제목/저자 불일치 후보 1건 |
| W09 | 20 | 20 | 15 | O | 부분 대조 완료 (48) | 32점 / 확인 필요 2, 불일치 1 | 10 | O | 참고문헌 확인 필요 2건; 부분 검증 문헌 2건; DOI/제목/저자 불일치 후보 1건; 수치 대조: 부분 대조 완료 |
| W10 | 20 | 20 | 15 | O | 기준 원천 존재 (100) | 100점 / 확인 필요 0, 불일치 0 | 10 | O | 자동 구조 점검 기준 주요 감점 없음 |
| W11 | 20 | 20 | 15 | O | 확인 필요 (47) | 32점 / 확인 필요 2, 불일치 0 | 10 | O | 참고문헌 확인 필요 2건; 대체 문헌 후보 2건; 수치 대조: 확인 필요 |
| W12 | 20 | 20 | 15 | O | 기준 원천 존재 (100) | 32점 / 확인 필요 0, 불일치 1 | 10 | O | DOI/제목/저자 불일치 후보 1건; 대체 문헌 후보 4건 |
| W13 | 20 | 20 | 15 | O | 부분 대조 완료 (82) | 60점 / 확인 필요 0, 불일치 1 | 10 | O | DOI/제목/저자 불일치 후보 1건; 대체 문헌 후보 2건; 수치 대조: 부분 대조 완료 |
| W14 | 20 | 20 | 15 | O | 기준 원천 존재 (100) | 32점 / 확인 필요 1, 불일치 1 | 10 | O | 참고문헌 확인 필요 1건; 부분 검증 문헌 1건; DOI/제목/저자 불일치 후보 1건; 대체 문헌 후보 2건 |
| W15 | 20 | 20 | 15 | O | 자동 대조 완료 (100) | 86점 / 확인 필요 0, 불일치 0 | 10 | O | 대체 문헌 후보 1건 |

## 6. 실험 상태와 outputs 일치 점검

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

## 7. 우선순위 주차 수치 대조 결과

| 주차 | 상태 | 기준 원천 | 세부 메모 |
|---|---|---|---|
| W02 | 확인 필요 | `03_weekly_reports/w02_optimization_data_poisoning/04_experiment/outputs/metrics_summary.csv` | experiment_report.md 3/27 부분 대조: 사람이 세부 수치 확인 필요; w02_submission_report.md 4/27 부분 대조: 사람이 세부 수치 확인 필요; w02_submission_report.html 5/27 부분 대조: 사람이 세부 수치 확인 필요; presentation_slides.html 0/27 확인 필요: 기준 수치 토큰 미탐지 |
| W06 | 확인 필요 | `03_weekly_reports/w06_diffusion_gan_deepfake/04_experiment/outputs/metrics_summary.csv` | experiment_report.md 18/25 부분 대조: 사람이 세부 수치 확인 필요; w06_submission_report.md 17/25 부분 대조: 사람이 세부 수치 확인 필요; w06_submission_report.html 17/25 부분 대조: 사람이 세부 수치 확인 필요; presentation_slides.html 0/25 확인 필요: 기준 수치 토큰 미탐지 |
| W09 | 부분 대조 완료 | `03_weekly_reports/w09_drl_cybersecurity/04_experiment/outputs/metrics_summary.csv` | experiment_report.md 15/31 부분 대조: 사람이 세부 수치 확인 필요; w09_submission_report.md 20/31 부분 대조: 사람이 세부 수치 확인 필요; w09_submission_report.html 20/31 부분 대조: 사람이 세부 수치 확인 필요; presentation_slides.html 4/31 부분 대조: 사람이 세부 수치 확인 필요 |
| W11 | 확인 필요 | `03_weekly_reports/w11_differential_privacy_mi/04_experiment/outputs/metrics_summary.csv` | experiment_report.md 19/27 부분 대조: 사람이 세부 수치 확인 필요; w11_submission_report.md 16/27 부분 대조: 사람이 세부 수치 확인 필요; w11_submission_report.html 16/27 부분 대조: 사람이 세부 수치 확인 필요; presentation_slides.html 0/27 확인 필요: 기준 수치 토큰 미탐지 |
| W13 | 부분 대조 완료 | `03_weekly_reports/w13_model_stealing_watermarking/04_experiment/outputs/metrics_summary.csv` | experiment_report.md 15/15 자동 대조 완료; w13_submission_report.md 15/15 자동 대조 완료; w13_submission_report.html 15/15 자동 대조 완료; presentation_slides.html 4/15 부분 대조: 사람이 세부 수치 확인 필요 |
| W15 | 자동 대조 완료 | `03_weekly_reports/w15_reproducibility_xai_paper/04_experiment/outputs/metrics_summary.csv` | experiment_report.md 7/7 자동 대조 완료; w15_submission_report.md 7/7 자동 대조 완료; w15_submission_report.html 7/7 자동 대조 완료; presentation_slides.html 7/7 자동 대조 완료 |

## 8. 참고문헌 검증 상태

| 주차 | 확인 완료(로컬 기록) | 확인 필요 | 부분 검증 | DOI/제목 불일치 후보 | 대체 문헌 후보 | 로컬 PDF 없음 | 검증 점수 |
|---|---:|---:|---:|---:|---:|---:|---:|
| W01 | 4 | 0 | 0 | 1 | 0 | 0 | 88 |
| W02 | 2 | 2 | 0 | 0 | 1 | 0 | 46 |
| W03 | 5 | 0 | 0 | 0 | 0 | 0 | 100 |
| W04 | 1 | 4 | 0 | 0 | 0 | 0 | 20 |
| W05 | 1 | 2 | 0 | 2 | 0 | 0 | 36 |
| W06 | 1 | 3 | 0 | 1 | 0 | 0 | 28 |
| W07 | 0 | 0 | 1 | 3 | 1 | 0 | 42 |
| W08 | 1 | 2 | 1 | 1 | 0 | 0 | 40 |
| W09 | 0 | 2 | 2 | 1 | 0 | 0 | 32 |
| W10 | 5 | 0 | 0 | 0 | 0 | 0 | 100 |
| W11 | 1 | 2 | 0 | 0 | 2 | 0 | 32 |
| W12 | 0 | 0 | 0 | 1 | 4 | 0 | 32 |
| W13 | 2 | 0 | 0 | 1 | 2 | 0 | 60 |
| W14 | 0 | 1 | 1 | 1 | 2 | 0 | 32 |
| W15 | 4 | 0 | 0 | 0 | 1 | 0 | 86 |

## 9. 깨진 상대경로 링크 목록

- 없음

## 10. 0바이트 파일 목록

- 없음

## 11. 자동 점검 상세 기준

| 항목 | 배점 | 자동 판정 |
|---|---:|---|
| 폴더 구조 완성도 | 20 | 필수 하위폴더 10개 존재 비율 |
| 보고서 파일 존재 | 20 | `06_report/` 또는 `07_week_submission/`의 보고서 후보 존재 |
| 발표자료 존재 | 15 | `09_presentation/`의 HTML 또는 Markdown 존재 |
| 표/그림/수식 포함 | 15 | 표 5점, 이미지 파일 5점, 수식 표현 5점 |
| 실험/산출물 존재 | 10 | `04_experiment/outputs/`와 주요 결과 파일 존재 |
| AI 활용 고지 존재 | 10 | `05_ai_worklog/`의 AI 고지/작업기록 후보 존재 |
| 링크/파일 무결성 | 10 | 깨진 상대경로 링크 5점, 0바이트 파일 5점 |

## 12. 사람이 직접 확인해야 할 항목

- 참고문헌이 실제 존재하는지, DOI/URL/출판사 페이지가 정확한지 확인
- 논문 품질과 주차 주제 적합성 평가
- PDF 파일의 시각적 깨짐, 누락 페이지, 서식 문제 확인
- 실험 결과의 학술적 해석, 재현 가능성, 데이터/코드 타당성 검토
- AI 활용 고지의 사실관계와 최종 책임 확인
