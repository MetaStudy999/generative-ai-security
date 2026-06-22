# AI 활용 기록

| 일자 | 도구 | 사용 목적 | 주요 입력 | 산출물 | 본인 검토 | 검증 방법 |
|---|---|---|---|---|---|---|
| 2026-06-22 | Codex | W11 보고서 구조 보완 및 초안 작성 | `W11` 프롬프트와 로컬 파일 상태 | 논문 요약, 이론노트, 보안노트, 실험 설계, 통합보고서 초안 | DOI/원문/수치 검증 항목 분리 | 로컬 PDF 파일명, 강의자료, DOI 검수보고서 |
| 2026-06-22 | Codex | synthetic toy 실험 코드 작성 및 실행 | `04_experiment/configs/config.yaml` | `src/run_experiment.py`, `outputs/metrics_summary.csv`, `results.json`, `run_log.md` | `epsilon_proxy` 한계 명시 | 실행 로그와 보고서 수치 대조 |
| 2026-06-22 | Codex | 제출용/발표용 산출물 작성 | 통합보고서와 outputs | `w11_submission_report.*`, `09_presentation/` | 수치 일치 여부와 대체 PDF 표시 확인 | `rg` placeholder 점검, 파일 목록 점검 |

## 사용 원칙

- AI 산출물은 초안이며 최종 책임은 작성자에게 있다.
- DOI, URL, 정량 결과는 근거가 있는 값만 적고 불확실한 항목은 확인 필요로 표시한다.
- 실험 수치는 `04_experiment/outputs/` 산출물과 일치하는 값만 사용한다.
