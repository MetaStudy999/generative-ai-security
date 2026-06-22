# AI 활용 기록

| 일자 | 도구 | 사용 목적 | 주요 입력 | 산출물 | 본인 검토 | 검증 방법 |
|---|---|---|---|---|---|---|
| 2026-06-22 | Codex | 공통 지침 및 W13 산출물 구조 확인 | `03_weekly_reports/README.md`, W13 프롬프트, 기존 W13 파일 | 누락 파일 목록과 보완 범위 도출 | 실행 전 수치 금지, DOI 임의 생성 금지 확인 | 공통 README와 W13 지시서 대조 |
| 2026-06-22 | Codex | 문헌 요약 보완 | W13 로컬 PDF 메타데이터/첫 페이지, 기존 summary | P01~P05 요약 및 paper matrix 보완 | P02/P05 대체 PDF 상태 표시 | `pdfinfo`, `pdftotext`, 로컬 파일명 대조 |
| 2026-06-22 | Codex | toy 실험 코드 작성 및 실행 | synthetic data, query budget, trigger-set ownership check | `src/run_experiment.py`, outputs 3종 | 실제 API/개인정보/무단 질의 제외 확인 | `py_compile`, 실행 로그, CSV/JSON 대조 |
| 2026-06-22 | Codex | 최종보고서·제출본·발표자료 작성 | 실행 결과와 W13 평가표 | 통합보고서, 제출용 보고서, 발표자료 세트 | false positive 한계와 대체 PDF 상태 명시 | `outputs/run_log.md` 수치 일치 확인 |

## 사용 원칙

- AI 산출물은 초안 작성과 구조화에 사용했으며 최종 책임은 작성자에게 있다.
- DOI, URL, 원문 세부 수치는 임의 생성하지 않는다.
- 실험 수치는 `04_experiment/outputs/metrics_summary.csv`, `results.json`, `run_log.md`와 일치하는 값만 사용한다.
- 실제 상용 API 대상 모델 추출, 무단 대량 질의, 실제 모델 탈취 절차는 작성하지 않는다.
