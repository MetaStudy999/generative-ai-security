# AI 활용 기록

| 일자 | 도구 | 사용 목적 | 주요 입력 | 산출물 | 본인 검토 | 검증 방법 |
|---|---|---|---|---|---|---|
| 2026-06-22 | Codex | W06 보고서 구조 보완 및 초안 작성 | `W06` 프롬프트와 로컬 파일 상태 | 논문 요약, 이론노트, 보안노트, 실험 설계, 통합보고서 초안 | 원문/DOI/수치 검증 항목은 별도 표시 | PDF 파일명, 프롬프트 논문 목록, 최종 원문 대조 |
| 2026-06-22 | Codex | W06 실험 코드 작성 및 실행 | synthetic detector score 신뢰성 평가 설계 | `src/run_experiment.py`, `outputs/` 결과, 실험보고서 갱신 | 실제 딥페이크 생성 없이 toy 범위 확인 | `python3 src/run_experiment.py --config configs/config.yaml`, `outputs/run_log.md` |
| 2026-06-22 | Codex | 제출본과 발표자료 작성 | 최종 통합보고서와 실행 로그 | `w06_submission_report.*`, `09_presentation/` | 수치와 DOI 상태 일치 확인 | `metrics_summary.csv`, `doi_check.md` |

## 사용 원칙

- AI 산출물은 초안이며 최종 책임은 작성자에게 있다.
- DOI, URL, 정량 결과는 임의 생성하지 않는다.
- 원문 세부 내용은 최종 제출 전 사람이 대조한다.
