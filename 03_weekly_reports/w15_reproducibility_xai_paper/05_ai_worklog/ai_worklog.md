# AI 활용 기록

| 일자 | 도구 | 사용 목적 | 주요 입력 | 산출물 | 본인 검토 | 검증 방법 |
|---|---|---|---|---|---|---|
| 2026-06-22 | Codex | W15 보고서 구조 보완 및 초안 작성 | `W15` 프롬프트, 공통 README, 로컬 W15 파일 상태 | 논문 요약, 이론노트, 보안노트, 통합보고서 보완 | 대체 PDF와 미검증 DOI를 별도 표시 | 로컬 PDF 첫 페이지, DOI 표, 출판사/아카이브 페이지 대조 |
| 2026-06-22 | Codex | 로컬 재현성·제출 준비 감사 스크립트 작성 | W15 필수 산출물 목록, `04_final_paper` 연결 파일 목록 | `04_experiment/src/run_experiment.py`, `outputs/metrics_summary.csv`, `results.json`, `run_log.md` | 실제 공격·개인정보·모델 성능 주장 없음 확인 | 실행 로그와 CSV/JSON 값 대조 |
| 2026-06-22 | Codex | 제출본·발표자료 작성 | 통합보고서, 실험보고서, DOI 검증표, 감사 결과 | `07_week_submission/w15_submission_report.*`, `09_presentation/` | Markdown/HTML 상태값 일치 확인 | `outputs/run_log.md` 기준 수치 확인 |

## 사용 원칙

- AI 산출물은 초안이며 최종 책임은 작성자에게 있다.
- DOI, URL, 정량 결과는 임의 생성하지 않는다.
- 실행 로그가 없는 모델 성능 수치는 작성하지 않는다.
- P03 지정 논문 원문, P05 최종 DOI, 국내 문헌은 최종 제출 전 사람이 재검증한다.
