# AI 활용 고지서

| 항목 | 작성 내용 |
|---|---|
| 사용한 AI 도구명 | Codex, ChatGPT 등 실제 사용 도구 |
| 사용 일자 | 2026-06-22, 2026-06-23 |
| 사용 목적 | 논문 요약 보강, DOI/URL 검증 보조, 대체 PDF 표시, synthetic DP/MI 실험 코드 작성과 재현성 점검, 발표자료 작성, KCI/SCI 섹션 보완 |
| 주요 프롬프트 1 | W11 보고서 최종 보완 지시 |
| 주요 프롬프트 2 | P01~P05 공식 DOI와 대체 PDF 검증 요청 |
| 주요 프롬프트 3 | KCI/SCI 논문 형식 전환 섹션 작성 요청 |
| AI 산출물 반영 위치 | W11 하위 Markdown, Python, HTML, 실험 보고서 파일 |
| 본인 수정 내용 | DOI/URL 검증 상태 분리, P03/P05 대체 PDF 명시, 실험 범위 제한, outputs 수치 대조, `epsilon_proxy` 한계 표시, Docker 재현성 보완 |
| 사실관계 검증 방법 | DOI/Crossref/출판사 primary URL, arXiv, 로컬 PDF 메타데이터와 첫 페이지, 실행 로그, 강의자료 표기 대조 |
| 참고문헌 검증 방법 | 제목, 저자, 연도, 학술지, DOI/URL, 로컬 PDF 일치 여부 대조 |
| 실험결과 처리 | `outputs/metrics_summary.csv`, `outputs/results.json`, `outputs/run_log.md` 수치 대조 및 로컬/Docker 재실행 |
| 아직 검토 필요한 항목 | P02 강의자료 저자·권호 표기, P03 강의자료 저자명과 지정 원문 PDF, P05 강의자료 저자명과 지정 원문 PDF, 국내 참고문헌, PDF 저작권 상태 |
| 최종 책임 확인 | 최종 제출자는 원고의 내용, 인용, 실험결과, 연구윤리 책임을 확인해야 한다. |

## 추가 주의

- AI가 생성한 문장은 제출 전 사람이 직접 검토해야 한다.
- `epsilon_proxy`는 formal DP accountant 산출값이 아니며 실제 DP 보장으로 표현하면 안 된다.
- P03/P05의 대체 PDF를 지정 논문처럼 인용하면 안 된다.
- public GitHub 저장소에서는 출판사 PDF 원문 커밋 여부와 저작권 위험을 별도로 검토해야 한다.
