# AI 활용 기록

| 일자 | 도구 | 사용 목적 | 주요 입력 | 산출물 | 본인 검토 | 검증 방법 |
|---|---|---|---|---|---|---|
| 2026-06-22 | Codex | 공통 지침과 W14 프롬프트 확인 | `README.md`, `03_weekly_reports/README.md`, `01_codex_prompts/W14_mlops_supply_chain.md` | 작업 범위 정리 | 실험 수치는 outputs 기준으로만 반영 | 로컬 파일 대조 |
| 2026-06-22 | Codex | 로컬 PDF 메타데이터 대조 | W14 PDF 첫 페이지, 수업 검수보고서 | P01 제목 보정, P03/P04/P05 대체 PDF 상태 기록 | DOI와 원문 불일치 항목 분리 | PDF first page, 수업자료 대조 |
| 2026-06-22 | Codex | Synthetic toy MLOps pipeline 작성 및 실행 | config.yaml, 공통 실험 산출물 규칙 | run_experiment.py, outputs 6개 파일 | 실제 개인정보/운영 서비스 사용 없음 확인 | run_log, CSV, JSON 대조 |
| 2026-06-22 | Codex | 보고서·제출본·발표자료 작성 | 실행 결과와 W14 문헌요약 | 통합보고서, 제출본, 발표 패키지 | 수치 일관성 확인 | `rg`와 파일별 표 대조 |

## 사용 원칙

- AI 산출물은 초안이며 최종 책임은 작성자에게 있다.
- DOI, URL, 정량 결과는 근거 파일이 있을 때만 적는다.
- P03/P04/P05의 공식 원문 PDF는 최종 제출 전 사람이 재확인한다.
