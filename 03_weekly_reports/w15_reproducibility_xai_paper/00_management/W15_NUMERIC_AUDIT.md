# W15 수치 대조 감사

생성일: 2026-06-24 00:18:52 KST

## 1. 기준 원천

- 기준 원천: `03_weekly_reports/w15_reproducibility_xai_paper/04_experiment/outputs/metrics_summary.csv`
- 기준 우선순위: `metrics_summary.csv`를 1차 원천으로 사용
- 실험 성격: 로컬 산출물 존재와 제출 준비 상태 감사이며, 모델 성능 실험이 아님

## 2. 대조한 파일 목록

- `03_weekly_reports/w15_reproducibility_xai_paper/04_experiment/experiment_report.md`
- `03_weekly_reports/w15_reproducibility_xai_paper/07_week_submission/w15_submission_report.md`
- `03_weekly_reports/w15_reproducibility_xai_paper/07_week_submission/w15_submission_report.html`
- `03_weekly_reports/w15_reproducibility_xai_paper/09_presentation/presentation_slides.html`

## 3. 기준 원천 수치

| category | metric | value | status | evidence |
|---|---|---:|---|---|
| artifact | w15_required_files | 47/47 | complete | `03_weekly_reports/w15_reproducibility_xai_paper` |
| artifact | final_paper_link_files | 9/9 | complete | `04_final_paper` |
| paper | local_pdf_count | 5 | complete | `01_papers/pdf` |
| reference | doi_confirmed | 4 | complete | `01_papers/doi_check.md` |
| reference | doi_partial | 1 | partial | `01_papers/doi_check.md` |
| reference | doi_unverified | 0 | complete | `01_papers/doi_check.md` |
| reference | weighted_reference_verification_rate | 0.90 | partial | `01_papers/doi_check.md` |
| ai_disclosure | ai_disclosure_completeness | 11/11 | complete | `05_ai_worklog/ai_disclosure_draft.md` |
| reproducibility | config_present | 1 | complete | `configs/config.yaml` |
| reproducibility | seed_recorded | 42 | complete | `configs/config.yaml` |

## 4. 일치한 수치

- 자동 토큰 대조 점수: 100/100
- `metrics_summary.csv`의 핵심 값 `47/47`, `9/9`, `5`, `4`, `1`, `0`, `0.90`, `11/11`, `42`를 기준으로 확인했다.

## 5. 수정한 수치

- 원문에 없는 실험 결과를 새로 만들지 않았다.
- 자동 대조표를 생성해 기준 원천과 대조 대상의 확인 필요 상태를 명시했다.

## 6. 확인 필요 수치

| 대조 대상 | 자동 대조 결과 | 확인 필요 |
|---|---|---|
| `03_weekly_reports/w15_reproducibility_xai_paper/04_experiment/experiment_report.md` | 7/7 / 자동 대조 완료 | 아니오 |
| `03_weekly_reports/w15_reproducibility_xai_paper/07_week_submission/w15_submission_report.md` | 7/7 / 자동 대조 완료 | 아니오 |
| `03_weekly_reports/w15_reproducibility_xai_paper/07_week_submission/w15_submission_report.html` | 7/7 / 자동 대조 완료 | 아니오 |
| `03_weekly_reports/w15_reproducibility_xai_paper/09_presentation/presentation_slides.html` | 7/7 / 자동 대조 완료 | 아니오 |

## 7. 사람이 봐야 할 항목

- `weekly_submission.html`과 `presentation_slides.html`의 렌더링에서 표와 캡션이 깨지지 않는지 확인
- P03 대체 PDF 상태와 W15 참고문헌 검증률 `0.90` 산정 방식 확인
- `47/47`, `9/9`, `11/11`은 completeness proxy이며 실제 모델 성능으로 해석하지 않도록 최종 원고 문구 확인
- `seed_recorded=42`와 `config_present=1`이 config/run_log와 계속 일치하는지 제출 직전 재확인
