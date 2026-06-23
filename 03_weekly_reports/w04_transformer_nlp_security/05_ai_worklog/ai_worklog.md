# AI 활용 기록

| 일자 | 도구 | 사용 목적 | 주요 입력 | 산출물 | 본인 검토 | 검증 방법 |
|---|---|---|---|---|---|---|
| 2026-06-22 | Codex | W04 보고서 구조 보완 및 초안 작성 | `W04` 프롬프트와 로컬 파일 상태 | 논문 요약, 이론노트, 보안노트, 실험 설계, 통합보고서 초안 | 원문/DOI/수치 검증 항목은 별도 표시 | PDF 파일명, 프롬프트 논문 목록, 최종 원문 대조 |
| 2026-06-22 | Codex | DOI/URL 검증 보조 | 공개 arXiv, ACM DOI, ScienceDirect 페이지 | `doi_check.md`, `paper_list.md`, 논문 요약 서지정보 갱신 | 출판 DOI와 arXiv DOI를 구분해 반영 | 공개 페이지 URL, 로컬 PDF 링크 문자열 대조 |
| 2026-06-22 | Codex | synthetic NLP 보안 실험 작성 및 실행 | W04 실습 요구사항, `configs/config.yaml` | `src/run_experiment.py`, `outputs/metrics_summary.csv`, `outputs/results.json`, `outputs/run_log.md` | 실제 개인정보 없음, toy 결과 한계 표시 | 스크립트 재실행, CSV/JSON/run_log 값 일치 확인 |
| 2026-06-22 | Codex | 제출/발표 산출물 작성 | 최종 통합보고서, 실험 로그, AI 고지서 | 제출용 보고서, 발표 보고서, 슬라이드, 대본, Q&A, 핸드아웃 | 실험 수치와 DOI 상태 일관성 확인 | `rg` 기반 미완성 표현 검색 |

## 사용 원칙

- AI 산출물의 최종 책임은 작성자에게 있다.
- DOI, URL, 정량 결과는 임의 생성하지 않고 근거가 있는 항목만 확정한다.
- synthetic toy 실험 결과는 실제 Transformer 또는 LLM 성능 주장으로 일반화하지 않는다.
- 원문 세부 내용은 최종 제출 전 사람이 대조한다.

# AI 활용 기록: 수식·알고리즘 보강

| 항목 | 기록 내용 |
|---|---|
| 사용 목적 | 수식 설명 / LaTeX 변환 / 기호 정의 / 검산 보조 |
| 반영 위치 | `02_paper_summaries/P01_summary.md`-`P05_summary.md`의 `### 5.1 핵심 수식 또는 알고리즘 설명`, `02_paper_summaries/formula_audit.md`, `00_class_materials/formula_audit_index.md` |
| 검증 방식 | 로컬 `README.md`, `math_formula_toolchain.md`, `paper_summary_template.md`, 각 주차 `paper_list.md`와 `doi_check.md`를 확인했다. 대표 표준식은 공식 arXiv/DOI landing page로 문헌 존재를 일부 대조했으나, 개별 원문 절/쪽/그림/알고리즘 번호는 `확인 필요`로 유지했다. |
| 주의사항 | 검증 전 수식·정량값은 확정값으로 쓰지 않고, 표준식은 `표준 정의식 / 원문 직접 인용 아님`으로 표시했다. 실제 공격 절차나 무단 침투 단계는 작성하지 않았다. |
