# STRUCTURE_REPAIR_REPORT

## 1. 작업 요약

루트에 생성된 비번호형 폴더의 유효 산출물을 기존 번호형 구조의 `04_final_paper/` 하위 폴더로 이동·병합하였다. 실제 제출용 복사본은 `06_submission/2026-06-13_JKAIS_mock_submission/`에 별도로 정리하였다.

## 2. 구조 원칙

- 작업 원본: `04_final_paper/`
- 최종 제출 복사본: `06_submission/2026-06-13_JKAIS_mock_submission/`
- 루트 비번호형 폴더 사용 금지

## 3. 이동 완료 파일

| 기존 경로 | 새 경로 | 처리 방식 |
|---|---|---|
| `paper/JKAIS_paper_draft.md` | `04_final_paper/05_draft/JKAIS_paper_draft.md` | `git mv` |
| `paper/JKAIS_paper_draft.docx` | `04_final_paper/05_draft/JKAIS_paper_draft.docx` | `git mv` |
| `paper/JKAIS_paper_draft.pdf` | `04_final_paper/05_draft/JKAIS_paper_draft.pdf` | `git mv` |
| `paper/build_docx.sh` | `04_final_paper/05_draft/build_docx.sh` | `git mv` |
| `paper/build_docx_pdf.py` | `04_final_paper/05_draft/build_docx_pdf.py` | `git mv` |
| `paper/paper_metadata.yaml` | `04_final_paper/01_planning/paper_metadata.yaml` | `git mv` |
| `paper/title_candidates.md` | `04_final_paper/01_planning/title_candidates.md` | `git mv` |
| `paper/figures/*` | `04_final_paper/05_draft/figures/` | `git mv` |
| `data/*` | `04_final_paper/04_methodology_experiment/data/` | `git mv` |
| `experiments/*.py` | `04_final_paper/04_methodology_experiment/scripts/` | `git mv` |
| `outputs/*` | `04_final_paper/04_methodology_experiment/outputs/` | `git mv` |
| `references/domestic_kci_references.md` | `04_final_paper/03_related_work/domestic_kci_references.md` | `git mv` |
| `references/international_references.md` | `04_final_paper/03_related_work/international_references.md` | `git mv` |
| `references/reference_verification.md` | `04_final_paper/06_appendices/reference_verification.md` | `git mv` |
| `submission/journal_template/*` | `04_final_paper/00_journal_format/journal_template/` | `git mv` |
| `submission/journal_policy/*` | `04_final_paper/00_journal_format/journal_policy/` | `git mv` |
| `submission/journal_format_source.md` | `04_final_paper/00_journal_format/journal_format_source.md` | `git mv` |
| `submission/*.md` | `04_final_paper/02_weekly_reflection/`, `04_final_paper/06_appendices/`, `04_final_paper/07_final_submission/` | `git mv` |
| `ethics/*` | `04_final_paper/06_appendices/` | `git mv` |
| `reports/presentation_visual_audit.md` | `04_final_paper/06_appendices/presentation_visual_audit.md` | `git mv` |

## 4. 병합 또는 검토 필요 파일

충돌 파일은 사용자 승인에 따라 루트 비번호형 폴더의 최근 산출물을 최종본으로 채택하고, 기존 `04_final_paper/` 대상 파일은 `_migration_review/`에 보존하였다.

| 최종 파일 | 보존한 기존 파일 |
|---|---|
| `04_final_paper/04_methodology_experiment/outputs/metrics_summary.csv` | `04_final_paper/06_appendices/_migration_review/04_final_paper_04_methodology_experiment_outputs_metrics_summary.csv` |
| `04_final_paper/04_methodology_experiment/outputs/run_log.md` | `04_final_paper/06_appendices/_migration_review/04_final_paper_04_methodology_experiment_outputs_run_log.md` |
| `04_final_paper/06_appendices/reference_verification.md` | `04_final_paper/06_appendices/_migration_review/04_final_paper_06_appendices_reference_verification.md` |
| `04_final_paper/06_appendices/ai_disclosure.md` | `04_final_paper/06_appendices/_migration_review/04_final_paper_06_appendices_ai_disclosure.md` |
| `04_final_paper/00_journal_format/journal_format_source.md` | `04_final_paper/06_appendices/_migration_review/04_final_paper_00_journal_format_journal_format_source.md` |

`experiments/__pycache__/common.cpython-312.pyc`는 Git 추적 파일이 아니며, 삭제하지 않고 `04_final_paper/06_appendices/_migration_review/__pycache__/experiments_common.cpython-312.pyc`에 보존하였다.

## 5. 제거된 비번호형 폴더

- `paper`
- `data`
- `experiments`
- `outputs`
- `references`
- `submission`
- `ethics`
- `reports`

## 6. 남은 비번호형 폴더

없음.

## 7. README 수정 내역

핵심 산출물 경로를 번호형 구조 기준으로 수정하였다. 또한 기말논문 작업 원본은 `04_final_paper/`, 제출 복사본은 `06_submission/2026-06-13_JKAIS_mock_submission/`에 둔다는 구조 원칙을 추가하였다.

## 8. AGENTS.md 수정 내역

`AGENTS.md`를 새로 생성하고, Codex가 루트 비번호형 폴더를 다시 만들지 않도록 구조 규칙을 추가하였다.

## 9. 제출 복사본 생성 결과

| 파일 | 상태 |
|---|---|
| 기말논문 DOCX | READY |
| 기말논문 PDF | READY |
| AI 활용 고지서 | READY |
| 참고문헌 검증표 | READY |
| 주차별 보고서 반영표 | READY |
| 학회지 양식 출처표 | READY |

## 10. 실험 재실행 결과

| 명령 | 성공 여부 |
|---|---|
| `python3 04_final_paper/04_methodology_experiment/scripts/run_baseline_no_filter.py` | 성공 |
| `python3 04_final_paper/04_methodology_experiment/scripts/run_baseline_keyword.py` | 성공 |
| `python3 04_final_paper/04_methodology_experiment/scripts/run_baseline_regex.py` | 성공 |
| `python3 04_final_paper/04_methodology_experiment/scripts/run_proposed_framework.py` | 성공 |
| `python3 04_final_paper/04_methodology_experiment/scripts/evaluate_metrics.py` | 성공 |
| `bash 04_final_paper/05_draft/build_docx.sh` | 성공 |

## 11. 최종 git status

```text
13 A
 3 D
11 M
46 R
```

`git status --short` 기준으로 모든 변경은 staged 상태다. 주요 항목은 다음과 같다.

- `paper/`, `data/`, `experiments/`, `outputs/`, `references/`, `submission/`, `ethics/`, `reports/` 산출물이 번호형 구조로 이동됨
- `AGENTS.md`, `STRUCTURE_REPAIR_PLAN.md`, `STRUCTURE_REPAIR_REPORT.md` 추가됨
- `06_submission/2026-06-13_JKAIS_mock_submission/` 제출 복사본 추가됨
- 제출 PDF는 `.gitignore`의 `*.pdf` 규칙 때문에 `git add -f`로 명시 추가됨

## 12. 주의사항

- 실험 결과와 참고문헌은 최종 제출 전 사람이 다시 검증해야 한다.
- `04_final_paper/04_methodology_experiment/outputs/results.json`은 기존 정적 감사 산출물로 보존되어 있다.
- 제출 복사본 파일명의 `성명_학번`은 실제 제출 전 사용자가 수정해야 한다.
