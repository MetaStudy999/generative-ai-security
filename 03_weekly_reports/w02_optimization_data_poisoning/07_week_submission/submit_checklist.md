# W02 제출 체크리스트

## 최종 자기 점검표

| 점검 항목 | 상태 | 비고 |
|---|---|---|
| 1장 한 문장 요약 작성 | 완료 | `w02_submission_report.md` |
| 2장 학습 배경과 주차 목표 작성 | 완료 | `w02_submission_report.md`, `integrated_report_final.md` |
| AI 원리 70% 정리 | 완료 | P01/P02 기반 |
| 보안 이슈 30% 정리 | 완료 | P03/P04/P05 기반 |
| 논문 5편 요약 | 완료 | `02_paper_summaries/` |
| 논문 5편 비교표 | 완료 | `02_paper_summaries/paper_matrix.md` |
| Research Track 5요소 작성 | 완료 | 연구문제, 위협모형, 평가방법, 재현성, 오픈문제 |
| P02 최종 출판판 검증 | 완료 | ACM DOI `10.1145/3578938`; Article 번호 확인 필요 |
| P04 최종 출판판 검증 | 확인 필요 | DOI `10.1145/3585385`는 확인. 강의계획서 제목과 동일 여부 확인 필요 |
| 실험 outputs 파일 존재 확인 | 완료 | `metrics_summary.csv`, `results.json`, `run_log.md` 존재 |
| 실험 결과와 보고서 수치 일치 | 완료 | outputs 기준으로 보고서 반영 |
| KCI 논문 형식 전환 작성 | 완료 | 12장 |
| SCI 논문 형식 전환 작성 | 완료 | 13장 |
| 본문 인용과 참고문헌 대응 | 완료 | [1]-[5] 대응 |
| 표·그림 번호 정리 | 완료 | 제출용 보고서 표 0-7, 그림 1 |
| AI 활용 고지 작성 | 완료 | `05_ai_worklog/ai_disclosure_draft.md` |
| PDF 저작권 위험 점검 | 완료 | PDF 5개 Git 추적 중, 사용자 승인 없이 삭제하지 않음 |
| 최종 사람이 검토할 항목 표시 | 완료 | P04, Article 번호, PDF 보관 정책, 국내 참고문헌 |

## outputs 파일 확인

| 파일 | 존재 여부 | 비고 |
|---|---|---|
| `04_experiment/outputs/metrics_summary.csv` | 존재 | 수치 정합성 기준 |
| `04_experiment/outputs/results.json` | 존재 | metadata와 row별 결과 |
| `04_experiment/outputs/run_log.md` | 존재 | 보고서 표기값 기준 로그 |

## PDF 보관 정책 메모

- `01_papers/pdf/` 아래 PDF 원문 5개는 `git ls-files` 기준 Git 추적 대상이다.
- `.gitignore`에는 PDF 무시 규칙이 있으나 이미 추적된 파일에는 소급 적용되지 않는다.
- public GitHub 저장소 공개 전 사용자 승인 아래 PDF 추적 제거 또는 비공개 전환이 필요하다.
- 본 작업에서는 PDF 삭제를 수행하지 않았다.

## 제출 메모

- W02는 문헌 기반 보고서, 실습 코드, outputs 수치, 발표자료, KCI/SCI 전환 섹션까지 제출용 최종 초안으로 보완했다.
- 최종 제출 확정은 하지 않았으며, 사람이 위 검토 필요 항목을 확인한 뒤 제출 여부를 결정한다.
