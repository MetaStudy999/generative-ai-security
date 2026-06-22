# AI 활용 기록

| 일자 | 도구 | 사용 목적 | 주요 입력 | 산출물 | 본인 검토 | 검증 방법 |
|---|---|---|---|---|---|---|
| 2026-06-22 | Codex | W03 보고서 구조 보완 및 초안 작성 | `W03` 프롬프트와 로컬 파일 상태 | 논문 요약, 이론노트, 보안노트, 실험 설계, 통합보고서 초안 | 원문/DOI/수치 검증 항목은 별도 표시 | PDF 파일명, 프롬프트 논문 목록, 최종 원문 대조 |
| 2026-06-22 | Codex | W03 실험 결과 완성 및 문서 갱신 | 로컬 W03 실험 폴더와 사용자 요청 | `src/run_experiment.py`, `outputs/` 결과, 관련 Markdown 업데이트 | synthetic toy 범위와 실행 로그 기준 수치 확인 | `python3 src/run_experiment.py --config configs/config.yaml`, `outputs/run_log.md` |
| 2026-06-22 | Codex | W03 발표용 보고서 작성 | W03 최종 통합보고서와 실험 로그 | `09_presentation/presentation_report.md` | 발표 수치와 한계 표현 확인 | `04_experiment/outputs/run_log.md`, `06_report/final/integrated_report_final.md` |
| 2026-06-22 | Codex | W03 제출용 보고서와 HTML 작성 | W03 통합보고서, 발표보고서, 실험 로그 | `w03_submission_report.md/html`, `presentation_report.html` | 제출 수치, DOI 미검증 표시, toy 한계 확인 | `04_experiment/outputs/run_log.md`, `01_papers/doi_check.md` |
| 2026-06-22 | Codex | W03 발표용 슬라이드 작성 | W03 발표용 보고서와 실험 로그 | `presentation_slides.md`, `presentation_slides.html` | 슬라이드 수치와 한계 표현 확인 | `04_experiment/outputs/run_log.md` |
| 2026-06-22 | Codex | W03 발표 보조자료 작성 | W03 발표 슬라이드와 실험 로그 | `speaker_notes.md`, `qna.md`, `one_page_handout.md` | 발화 대본, 예상 질문, 배포 요약의 수치와 한계 표현 확인 | `presentation_slides.md`, `04_experiment/outputs/run_log.md` |
| 2026-06-22 | Codex | W03 완성도 점검 및 보완 | 공통 README, 템플릿 원칙, W03 프롬프트, 로컬 산출물 | 상태표 보완, 보조 README 추가, 실험 결과 재실행 및 보존 범위 확인 | DOI/URL은 임의 확정하지 않고 보류 상태 유지, 수치는 `outputs/` 로그와 대조 | `python3 src/run_experiment.py --config configs/config.yaml`, `git check-ignore -v`, `outputs/run_log.md` |

## 사용 원칙

- AI 산출물은 초안이며 최종 책임은 작성자에게 있다.
- DOI, URL, 정량 결과는 임의 생성하지 않는다.
- 원문 세부 내용은 최종 제출 전 사람이 대조한다.
