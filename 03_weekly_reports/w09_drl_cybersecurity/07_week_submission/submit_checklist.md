# W09 제출 체크리스트

| 점검 항목 | 상태 | 근거/비고 |
|---|---|---|
| 논문 목록/DOI 정리 | 완료 / 확인 필요 | `01_papers/paper_list.md`, `doi_check.md`; P03/P04/P05 저자명 차이 |
| 논문 요약 5편 | 완료 / 확인 필요 | `02_paper_summaries/P01_summary.md` - `P05_summary.md` |
| 논문 비교표 | 완료 | `02_paper_summaries/paper_matrix.md` |
| AI 원리/보안 이슈 | 완료 | `03_theory_notes/` |
| Research Track | 완료 | threat model, evaluation protocol, open problems |
| 실험 코드 | 완료 | `04_experiment/src/run_experiment.py` |
| 실험 결과 | 완료 | `04_experiment/outputs/` |
| 통합보고서 | 완료 | `06_report/final/integrated_report_final.md` |
| 제출용 Markdown | 완료 | `07_week_submission/w09_submission_report.md` |
| 제출용 HTML | 완료 | Markdown 최신본의 핵심 구조와 수치 동기화 |
| 발표자료 | 완료 | 수치가 outputs 기준과 일치 |
| AI 활용 고지 | 완료 | `05_ai_worklog/ai_disclosure_draft.md` |
| 악용 가능한 절차 제외 | 완료 | toy simulation만 포함 |
| Docker build/run | 완료 | 2026-06-23 `docker compose build`, compose run 성공 |
| PDF 보관 정책 | 확인 필요 | PDF 5개가 Git 추적 대상, public 배포 전 삭제/비공개 전환 필요 |

## 최종 자기 점검표

| 점검 항목 | 상태 | 비고 |
|---|---|---|
| 1장 한 문장 요약 작성 | 완료 |  |
| 2장 학습 배경과 주차 목표 작성 | 완료 |  |
| AI 원리 70% 정리 | 완료 |  |
| 보안 이슈 30% 정리 | 완료 |  |
| 논문 5편 요약 | 완료 |  |
| 논문 5편 비교표 보완 | 완료 / 확인 필요 | P05 동일 여부 반영 |
| Research Track 5요소 작성 | 완료 | 연구문제, 위협모형, 평가방법, 재현성, 오픈문제 |
| P01 DOI/URL 검증 | 완료 | arXiv extended version 메모 |
| P02 DOI/URL 검증 | 완료 | arXiv v2/출판판 차이 메모 |
| P03 DOI/URL 검증 | 완료 / 확인 필요 | 저자명 표기 차이 확인 |
| P04 DOI/URL 검증 | 완료 / 확인 필요 | 저자명 표기 차이 확인 |
| P05 지정 논문 동일 여부 검증 | 확인 필요 | H. Yan et al. vs Landers/Doryab |
| 실험 outputs 파일 존재 확인 | 완료 | `metrics_summary.csv`, `results.json`, `run_log.md` |
| 실험 결과와 보고서 수치 일치 | 완료 | Python/Docker 재실행 확인 |
| KCI 논문 형식 전환 작성 | 완료 |  |
| SCI 논문 형식 전환 작성 | 완료 |  |
| 본문 인용과 참고문헌 대응 | 완료 / 확인 필요 | P03/P04/P05 표기 차이 |
| 표·그림 번호 정리 | 완료 | 표 1-7, 그림 1 |
| AI 활용 고지 작성 | 완료 |  |
| PDF 저작권 위험 점검 | 완료 / 확인 필요 | PDF 원문 추적 중, 삭제 필요 |
| 최종 사람이 검토할 항목 표시 | 완료 | 제출 확정 아님 |

## 제출 전 최종 확인

- P03/P04/P05의 강의계획서 저자명 차이를 교수자 또는 원 강의자료에서 확인한다.
- public GitHub 제출 전 `01_papers/pdf/*.pdf` 원문을 제거하거나 비공개 보관으로 전환한다.
- HTML 제출본은 Markdown 최신본의 핵심 구조와 수치를 반영했지만, 최종 제출 전 렌더링을 육안 확인한다.
- 실험 수치는 `outputs/run_log.md`, `metrics_summary.csv`, `results.json`과 다른 값을 쓰지 않는다.
