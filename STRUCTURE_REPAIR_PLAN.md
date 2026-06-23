# STRUCTURE_REPAIR_PLAN

## 1. 현재 문제

루트에 기존 번호형 구조와 새 비번호형 구조가 혼재되어 있다.

현재 확인된 비번호형 루트 폴더는 다음과 같다.

- `paper`
- `data`
- `experiments`
- `outputs`
- `references`
- `submission`
- `ethics`
- `reports`

## 2. 유지할 표준 루트 구조

- `00_class_materials`
- `01_codex_prompts`
- `02_report_templates`
- `03_weekly_reports`
- `04_final_paper`
- `05_references`
- `06_submission`
- `scripts`
- `assets`

## 3. 구조 원칙

- 기말논문 작업 원본은 `04_final_paper/`에 둔다.
- 실제 제출 복사본만 `06_submission/2026-06-13_JKAIS_mock_submission/`에 둔다.
- 루트 비번호형 폴더는 최종 구조가 아니다.
- 기존 파일은 삭제하지 않고 이동, 병합, 또는 `_migration_review/`에 보존한다.
- 이동은 가능하면 `git mv`를 사용한다.
- 충돌 파일은 루트 비번호형 폴더에 있는 최근 생성 산출물을 최종본으로 채택하고, 기존 `04_final_paper/` 대상 파일은 `_migration_review/`에 보존한다.
- 논문 내용의 대폭 수정은 하지 않고, 구조 복구와 경로 정리만 수행한다.

## 4. 이동 대상 비번호형 폴더

- `paper`
- `data`
- `experiments`
- `outputs`
- `references`
- `submission`
- `ethics`
- `reports`

## 5. 이동 매핑표

| 현재 경로 | 목표 경로 | 처리 |
|---|---|---|
| `paper/JKAIS_paper_draft.md` | `04_final_paper/05_draft/JKAIS_paper_draft.md` | 이동 |
| `paper/JKAIS_paper_draft.docx` | `04_final_paper/05_draft/JKAIS_paper_draft.docx` | 이동 |
| `paper/JKAIS_paper_draft.pdf` | `04_final_paper/05_draft/JKAIS_paper_draft.pdf` | 이동 |
| `paper/build_docx.sh` | `04_final_paper/05_draft/build_docx.sh` | 이동 |
| `paper/build_docx_pdf.py` | `04_final_paper/05_draft/build_docx_pdf.py` | 이동 |
| `paper/paper_metadata.yaml` | `04_final_paper/01_planning/paper_metadata.yaml` | 이동 |
| `paper/title_candidates.md` | `04_final_paper/01_planning/title_candidates.md` | 이동 |
| `paper/figures/*` | `04_final_paper/05_draft/figures/` | 이동 |
| `data/*` | `04_final_paper/04_methodology_experiment/data/` | 이동 |
| `experiments/*.py` | `04_final_paper/04_methodology_experiment/scripts/` | 이동 |
| `experiments/__pycache__/common.cpython-312.pyc` | `04_final_paper/06_appendices/_migration_review/__pycache__/experiments_common.cpython-312.pyc` | 보존 |
| `outputs/metrics_summary.csv` | `04_final_paper/04_methodology_experiment/outputs/metrics_summary.csv` | 루트 산출물을 최종본으로 채택, 기존 대상은 보존 |
| `outputs/run_log.md` | `04_final_paper/04_methodology_experiment/outputs/run_log.md` | 루트 산출물을 최종본으로 채택, 기존 대상은 보존 |
| `outputs/failure_cases.md` | `04_final_paper/04_methodology_experiment/outputs/failure_cases.md` | 이동 |
| `outputs/*_predictions.csv` | `04_final_paper/04_methodology_experiment/outputs/` | 이동 |
| `outputs/confusion_matrix.csv` | `04_final_paper/04_methodology_experiment/outputs/confusion_matrix.csv` | 이동 |
| `references/domestic_kci_references.md` | `04_final_paper/03_related_work/domestic_kci_references.md` | 이동 |
| `references/international_references.md` | `04_final_paper/03_related_work/international_references.md` | 이동 |
| `references/reference_verification.md` | `04_final_paper/06_appendices/reference_verification.md` | 루트 산출물을 최종본으로 채택, 기존 대상은 보존 |
| `submission/journal_template/*` | `04_final_paper/00_journal_format/journal_template/` | 이동 |
| `submission/journal_policy/*` | `04_final_paper/00_journal_format/journal_policy/` | 이동 |
| `submission/journal_format_source.md` | `04_final_paper/00_journal_format/journal_format_source.md` | 루트 산출물을 최종본으로 채택, 기존 대상은 보존 |
| `submission/submission_checklist.md` | `04_final_paper/07_final_submission/submission_checklist.md` | 이동 |
| `submission/file_name_rules.md` | `04_final_paper/07_final_submission/file_name_rules.md` | 이동 |
| `submission/weekly_report_mapping.md` | `04_final_paper/02_weekly_reflection/weekly_report_mapping.md` | 이동 |
| `submission/conversion_TODO.md` | `04_final_paper/07_final_submission/conversion_TODO.md` | 이동 |
| `submission/ai_disclosure.md` | `04_final_paper/06_appendices/ai_disclosure.md` | 루트 산출물을 최종본으로 채택, 기존 대상은 보존 |
| `submission/reference_verification.md` | `04_final_paper/06_appendices/reference_verification_submission.md` | 이동 |
| `ethics/ai_disclosure.md` | `04_final_paper/06_appendices/ai_disclosure_from_ethics.md` | 이동 |
| `ethics/copyright_check.md` | `04_final_paper/06_appendices/copyright_check.md` | 이동 |
| `ethics/privacy_check.md` | `04_final_paper/06_appendices/privacy_check.md` | 이동 |
| `reports/presentation_visual_audit.md` | `04_final_paper/06_appendices/presentation_visual_audit.md` | 이동 |

## 6. 충돌 예상 파일

| 현재 경로 | 목표 경로 | 처리 원칙 |
|---|---|---|
| `outputs/metrics_summary.csv` | `04_final_paper/04_methodology_experiment/outputs/metrics_summary.csv` | 루트 파일 최종본, 기존 대상 보존 |
| `outputs/run_log.md` | `04_final_paper/04_methodology_experiment/outputs/run_log.md` | 루트 파일 최종본, 기존 대상 보존 |
| `references/reference_verification.md` | `04_final_paper/06_appendices/reference_verification.md` | 루트 파일 최종본, 기존 대상 보존 |
| `submission/ai_disclosure.md` | `04_final_paper/06_appendices/ai_disclosure.md` | 루트 파일 최종본, 기존 대상 보존 |
| `submission/journal_format_source.md` | `04_final_paper/00_journal_format/journal_format_source.md` | 루트 파일 최종본, 기존 대상 보존 |

## 7. 삭제 금지 파일

다음 파일은 절대 삭제하지 않는다.

- 논문 초안
- DOCX/PDF 초안
- 학회 양식
- 학회 양식 다운로드 기록
- 데이터셋
- 실험 코드
- 실험 결과
- AI 활용 고지서
- 참고문헌 검증표
- 주차별 보고서 반영표
- 제출 체크리스트
