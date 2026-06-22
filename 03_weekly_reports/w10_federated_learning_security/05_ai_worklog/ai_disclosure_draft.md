# AI 활용 고지서

| 항목 | 작성 내용 |
|---|---|
| 사용한 AI 도구명 | Codex, ChatGPT 등 실제 사용 도구 |
| 사용 일자 | 2026-06-22, 2026-06-23 |
| 사용 목적 | 논문 요약 보강, DOI/URL 검증 보조, 개념 설명, 문장 구조화, synthetic FL 실험 코드 작성, 발표자료 작성, KCI/SCI 섹션 보완 |
| 주요 프롬프트 1 | W10 보고서 최종 보완 지시 |
| 주요 프롬프트 2 | P03/P05 출판 DOI 검증 요청 |
| 주요 프롬프트 3 | KCI/SCI 논문 형식 전환 섹션 작성 요청 |
| AI 산출물 반영 위치 | `03_weekly_reports/w10_federated_learning_security/` 하위 Markdown, Python, HTML, 실험 보고서 파일 |
| 본인 수정 내용 | DOI/URL 검증 상태 분리, 실험 범위 제한, outputs 수치 대조, 실제 개인정보/서비스 공격 제외, PDF 보관 위험 표시 |
| 사실관계 검증 방법 | DOI/arXiv/출판사 DOI 메타데이터, 로컬 PDF 메타데이터, 실행 로그, 수업자료 대조 |
| 참고문헌 검증 방법 | 제목, 저자, 연도, 학술지, 권호, 페이지/Article ID, DOI/URL 대조 |
| 실험결과 처리 | `outputs/metrics_summary.csv`, `outputs/results.json`, `outputs/run_log.md` 수치 대조 |
| 아직 검토 필요한 항목 | P01 수업자료 표기 차이 최종 확인, P04 Article 번호, 국내 참고문헌, public GitHub PDF 저작권 상태, HTML 렌더링 육안 확인 |
| 최종 책임 확인 | 최종 제출자는 원고의 내용, 인용, 실험결과, 연구윤리 책임을 확인해야 한다. |

## 사용 범위 제한

- AI가 생성한 문장은 제출 전 사람이 최종 검토해야 하는 초안으로 취급한다.
- AI는 실제 개인정보, 실제 FL 서비스, 무단 클라이언트 접속, 실제 공격 payload, 실제 gradient inversion, 실제 membership inference 공격 절차를 작성하거나 실행하지 않았다.
- 실험 수치는 실행된 `outputs/` 파일과 일치하는 항목만 본문에 반영했다.
