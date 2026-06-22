# AI 활용 고지서

| 항목 | 작성 내용 |
|---|---|
| 사용한 AI 도구명 | Codex, ChatGPT 등 실제 사용 도구 |
| 사용 일자 | 2026-06-22 및 2026-06-23 KST 작업분 |
| 사용 목적 | 논문 요약 보강, DOI/URL 검증 보조, 개념 설명, 문장 구조화, synthetic prompt score 실험 코드 작성, 발표자료 작성, KCI/SCI 섹션 보완 |
| 주요 프롬프트 1 | W07 보고서 최종 보완 지시 |
| 주요 프롬프트 2 | P02/P03/P04/P05 논문 동일 여부 및 DOI 검증 요청 |
| 주요 프롬프트 3 | KCI/SCI 논문 형식 전환 섹션 작성 요청 |
| AI 산출물 반영 위치 | `03_weekly_reports/w07_llm_security_privacy/` 하위 Markdown, Python, HTML, 실험 보고서 파일 |
| 본인 수정 내용 | DOI/URL 검증 상태 분리, 실험 범위 제한, outputs 수치 대조, 실제 jailbreak/개인정보/API 호출 제외 |
| 사실관계 검증 방법 | DOI/arXiv/출판사 페이지, Crossref 메타데이터, 로컬 PDF 메타데이터, 실행 로그, 수업자료 대조 |
| 참고문헌 검증 방법 | 제목, 저자, 연도, 학술지, 권호, 쪽수, DOI/URL 대조 |
| 실험결과 처리 | `outputs/metrics_summary.csv`, `outputs/results.json`, `outputs/run_log.md`와 보고서/발표자료 수치 대조 |
| 아직 검토 필요한 항목 | P01 강의계획서 저자 약식 표기, P02 Ankur Das 표기, P03 AI Open 지정 논문 동일 여부, P04 Yongtao Yin 표기, P05 Shujun Li 표기, 국내 참고문헌, PDF 저작권 상태 |
| 최종 책임 확인 | 최종 제출자는 원고의 내용, 인용, 실험결과, 연구윤리 책임을 확인해야 한다. |

## AI 사용 범위와 제한

- AI가 작성한 문장은 제출용 최종 초안으로만 사용하며, 최종 제출 전 사람이 원문·인용·수치·윤리 고지를 검토해야 한다.
- AI는 실제 LLM/API 호출, 실제 개인정보 추출, 실제 jailbreak 재현, 무단 서비스 질의, exploit instruction 생성을 수행하지 않았다.
- DOI/URL 검증은 확인 가능한 공식 메타데이터와 로컬 PDF 표지 기준으로만 반영했고, 확인되지 않은 항목은 `확인 필요`로 남겼다.
