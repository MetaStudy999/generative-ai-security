# AI 활용 고지서

| 항목 | 작성 내용 |
|---|---|
| 사용한 AI 도구명 | Codex, ChatGPT 등 실제 사용 도구 |
| 사용 일자 | 2026-06-22 |
| 사용 목적 | 논문 요약 보강, DOI/URL 검증 보조, 개념 설명, 문장 구조화, synthetic prompt 실험 코드 작성, 발표자료 작성, KCI/SCI 섹션 보완 |
| 주요 프롬프트 1 | W04 보고서 최종 보완 지시 |
| 주요 프롬프트 2 | P01/P04/P05 출판판 및 DOI 검증 요청 |
| 주요 프롬프트 3 | KCI/SCI 논문 형식 전환 섹션 작성 요청 |
| AI 산출물 반영 위치 | `03_weekly_reports/w04_transformer_nlp_security/` 하위 Markdown, Python, HTML, 실험 보고서 파일 |
| 본인 수정 내용 | DOI/URL 검증 상태 분리, 실험 범위 제한, outputs 수치 대조, 실제 개인정보 제외, PDF 저작권 위험 표시 |
| 사실관계 검증 방법 | Crossref DOI API, DOI BibTeX, arXiv API, ScienceDirect/AI Open 페이지, 로컬 PDF 메타데이터, 실행 로그, 수업자료 대조 |
| 참고문헌 검증 방법 | 제목, 저자, 연도, 학술지, DOI/URL, 권호, 쪽 정보 대조 |
| 실험결과 처리 | `outputs/metrics_summary.csv`, `outputs/results.json`, `outputs/run_log.md`와 보고서·발표자료 수치 대조 |
| 아직 검토 필요한 항목 | ACM Article 번호, P04 강의자료의 `N. Goyal` 표기, 국내 참고문헌, PDF 원문 공개 저장소 보관 여부 |
| 최종 책임 확인 | 최종 제출자는 원고의 내용, 인용, 실험결과, 연구윤리 책임을 확인해야 한다. |
