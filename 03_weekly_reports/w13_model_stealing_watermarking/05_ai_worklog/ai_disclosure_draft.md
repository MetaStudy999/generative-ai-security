# AI 활용 고지서

| 항목 | 작성 내용 |
|---|---|
| 사용한 AI 도구명 | Codex, ChatGPT 계열 대화형 AI |
| 사용 일자 | 2026-06-22, 2026-06-23 |
| 사용 목적 | 논문 요약 보강, DOI/URL 검증 보조, SUBSTITUTE PDF 표시, synthetic model extraction/watermarking 실험 코드 작성·점검, 발표자료 작성, KCI/SCI 섹션 보완 |
| 주요 프롬프트 1 | W13 보고서 최종 보완 지시 |
| 주요 프롬프트 2 | P01~P05 공식 DOI와 대체 PDF 검증 요청 |
| 주요 프롬프트 3 | KCI/SCI 논문 형식 전환 섹션 작성 요청 |
| AI 산출물 반영 위치 | W13 하위 Markdown, Python, HTML, 실험 보고서 파일 |
| 본인 수정 내용 | DOI/URL 검증 상태 분리, 대체 PDF 명시, false positive 해석 보완, outputs 수치 대조, 실제 API 공격 제외 |
| 사실관계 검증 방법 | DOI/arXiv/출판사 페이지, Crossref 메타데이터, 로컬 PDF 첫 페이지/메타데이터, 실행 로그, 수업자료 대조 |
| 참고문헌 검증 방법 | 제목, 저자, 연도, 학술지, DOI/URL 대조 |
| 실험결과 처리 | `outputs/metrics_summary.csv`, `outputs/results.json`, `outputs/run_log.md` 수치 대조 |
| 아직 검토 필요한 항목 | P02 지정 논문 원문 PDF, P03 강의계획서 저자명·제목 차이, P05 강의계획서 저자명 표기, 국내 참고문헌, PDF 저작권 상태 |
| 최종 책임 확인 | 최종 제출자는 원고의 내용, 인용, 실험결과, 연구윤리 책임을 확인해야 한다. |

## AI 활용 한계

AI가 생성한 문장은 초안으로만 취급한다. DOI와 출판정보는 확인된 공식 메타데이터만 확정값으로 반영했고, 확인하지 못한 지정 논문 원문은 `확인 필요` 또는 `대체 PDF 상태`로 남겼다. 실험 결과는 실행된 outputs 파일과 일치하는 값만 사용했다.
