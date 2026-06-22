# AI 활용 고지서

| 항목 | 작성 내용 |
|---|---|
| 사용한 AI 도구명 | Codex, ChatGPT |
| 사용 일자 | 2026-06-22, 2026-06-23 |
| 사용 목적 | 논문 요약 보강, DOI/URL 검증 보조, SUBSTITUTE PDF 표시, synthetic robustness/XAI 실험 코드 작성, 발표자료 작성, KCI/SCI 섹션 보완 |
| 주요 프롬프트 1 | W12 보고서 최종 보완 지시 |
| 주요 프롬프트 2 | P01~P05 공식 DOI와 대체 PDF 검증 요청 |
| 주요 프롬프트 3 | KCI/SCI 논문 형식 전환 섹션 작성 요청 |
| AI 산출물 반영 위치 | W12 하위 Markdown, Python, HTML, 실험 보고서 파일 |
| 본인 수정 내용 | DOI/URL 검증 상태 분리, 대체 PDF 명시, certified rate proxy 한계 표시, outputs 수치 대조 |
| 사실관계 검증 방법 | DOI/Crossref/출판사 페이지, 로컬 PDF 메타데이터와 첫 페이지, 실행 로그, 수업자료 대조 |
| 참고문헌 검증 방법 | 제목, 저자, 연도, 학술지, DOI/URL 대조 |
| 실험결과 처리 | `outputs/metrics_summary.csv`, `outputs/results.json`, `outputs/run_log.md`와 보고서·발표자료 수치 대조 |
| 아직 검토 필요한 항목 | P01 강의 표기와 공식 DOI 메타데이터 충돌, P02 Sen/Shuai Zhou 및 로컬 Ren PDF 동일 여부, P03 공식 published title 차이, P04/P05 지정 저자·제목 DOI, 국내 참고문헌, PDF 저작권 상태 |
| 최종 책임 확인 | 최종 제출자는 원고의 내용, 인용, 실험결과, 연구윤리 책임을 확인해야 한다. |

## 추가 고지

AI가 생성한 문장은 초안으로만 취급한다. DOI, 저자명, 학술지명, Article 번호, 실험 수치, PDF 저작권 상태는 사람이 공식 자료와 재확인한 뒤 최종 제출한다.
