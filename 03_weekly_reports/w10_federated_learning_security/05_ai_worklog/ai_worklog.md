# AI 활용 기록

| 일자 | 도구 | 사용 목적 | 주요 입력 | 산출물 | 본인 검토 | 검증 방법 |
|---|---|---|---|---|---|---|
| 2026-06-22 | Codex | 공통 지침과 W10 프롬프트 확인 | `README.md`, `03_weekly_reports/README.md`, `01_codex_prompts/W10_federated_learning_security.md` | 작업 범위 정리 | 실험 결과는 실행 로그 기준으로만 반영 | 로컬 파일 대조 |
| 2026-06-22 | Codex | 로컬 PDF 메타데이터 대조 | W10 PDF 첫 페이지 텍스트 | DOI/URL 검증표 보정 | 당시 P03/P05는 출판 DOI 확인 필요로 유지 | `pdftotext`, 로컬 PDF |
| 2026-06-22 | Codex | synthetic FL toy 실험 코드 작성 | W10 실험 지시, 보안 범위 | `src/run_experiment.py`, `configs/config.yaml` | 실제 개인정보·외부 서비스 사용 없음 확인 | 코드 검토 |
| 2026-06-22 | Codex | 실험 실행과 결과 반영 | seed 42, synthetic data, 10 clients | `outputs/run_log.md`, CSV, JSON | 수치가 보고서와 일치하는지 확인 | CSV/JSON/run log 대조 |
| 2026-06-22 | Codex | 제출본·발표본 작성 | 최종 통합보고서와 실행 로그 | 제출용 보고서, 발표자료 | 확인 필요 항목 유지 | `rg`와 파일 목록 점검 |
| 2026-06-23 | Codex | W10 최종 보완 | DOI/Crossref/arXiv 대조, outputs 수치 대조, 최종 보완 지시 | 16장 보고서, KCI/SCI 섹션, AI 고지, PDF 위험 메모 | P03/P05 출판 DOI 반영, P01/P04 남은 확인 표시 | DOI 메타데이터, arXiv, CSV/JSON/run log 대조 |

## 사용 원칙

- AI 산출물은 초안이며 최종 책임은 작성자에게 있다.
- DOI, URL, 정량 결과는 확인된 자료가 있을 때만 확정한다.
- 실험은 synthetic toy 환경으로 제한하고 실제 개인정보, 운영 서비스, 무단 공격 절차는 포함하지 않는다.
