# 연구 프로젝트 상태표

## 1. 저장소 기본 정보

| 항목 | 내용 |
|---|---|
| 저장소명 | generative-ai-security |
| 연구 주제 | AI 보안 기말 모의투고 논문 |
| 주요 대상 폴더 | 04_final_paper |
| 상태 기준일 | 2026-06-23 |

## 2. 현재 연구 진행 현황

| 구분 | 상태 | 근거 파일 | 비고 |
|---|---|---|---|
| 최종 주제 확정 | 파일 존재, 최종 확정 여부 확인 필요 | 04_final_paper/01_planning/final_topic.md | 선택 주제는 작성되어 있으나 제출 전 최종 확인 필요 |
| 연구질문 확정 | 파일 존재, 최종 확정 여부 확인 필요 | 04_final_paper/01_planning/research_question.md | RQ1-RQ3 작성됨 |
| 논문 초안 존재 | 파일 존재 | 04_final_paper/05_draft/paper_draft.md | 최종 제출 전 DOI/URL과 결과 표현 재검수 필요 |
| 국내 문헌 3편 검증 | 미충족 | 04_final_paper/06_appendices/reference_verification.md | 국내 3행 모두 `확인 필요` |
| 해외 문헌 5편 검증 | 미충족 | 04_final_paper/06_appendices/reference_verification.md | 해외 확인 완료 4편, 부분 확인 1편, 확인 필요 항목 존재 |
| 학회지 양식 출처 | 파일 존재, 선택 학회 확인 필요 | 04_final_paper/00_journal_format/journal_format_source.md | 학회명, 논문지명, URL 확인 필요 |
| AI 활용 고지 | 필수 항목 존재 | 04_final_paper/06_appendices/ai_disclosure.md | 자동 점검 PASS |
| 표 1개 이상 | 확인 | 04_final_paper/05_draft/paper_draft.md | `표 1` 및 Markdown 표 존재 |
| 그림 1개 이상 | 확인 | 04_final_paper/05_draft/paper_draft.md | `그림 1` 표기 존재, 최종 이미지 파일 여부는 확인 필요 |
| DOCX 제출본 | 없음 | 06_submission/final_paper_submission/ | 최종 변환 필요 |
| PDF 제출본 | 없음 | 06_submission/final_paper_submission/ | 최종 변환 필요 |

## 3. 미해결 이슈

| 번호 | 이슈 | 우선순위 | 상태 | 조치 |
|---:|---|---|---|---|
| 1 | 국내 논문 3편 검증 | 상 | 확인 필요 | KCI, DBpia, RISS, Google Scholar 확인 |
| 2 | 국내 학회지 양식 확정 | 상 | 확인 필요 | 학회명, 논문지명, 투고규정 URL 입력 |
| 3 | 최종 연구주제 범위 축소 | 상 | 확인 필요 | RAG 간접 프롬프트 인젝션 중심 검토 |
| 4 | 최종 DOCX/PDF 변환 | 중 | 확인 필요 | Pandoc 또는 학회지 양식 기반 변환 |
| 5 | 공개 PDF 저작권 리스크 | 중 | 확인 필요 | 삭제 전 정책 문서 작성 |

## 4. 다음 작업

- [ ] 국내 학회지 1개 선택
- [ ] 국내 문헌 3편 검증
- [ ] 연구질문 RQ1-RQ3 확정
- [x] 연구 추적성 매트릭스 작성
- [x] 참고문헌 자동 점검 스크립트 작성
- [x] 최종 제출 패키지 폴더 구성

## 5. 자동 점검 실행 결과

| 명령 | 결과 | 비고 |
|---|---|---|
| python 04_final_paper/04_methodology_experiment/src/run_analysis.py | PASS(대체 실행) | 현재 환경에 `python` 명령이 없어 `python3`로 실행. `outputs/results.json`, `outputs/metrics_summary.csv`, `outputs/run_log.md` 생성 |
| python scripts/check_references.py | FAIL(대체 실행) | 현재 환경에 `python` 명령이 없어 `python3`로 실행. 국내 확인 완료 0/3, 해외 확인 완료 4/5 |
| python scripts/check_ai_disclosure.py | PASS(대체 실행) | 현재 환경에 `python` 명령이 없어 `python3`로 실행. 필수 항목 모두 존재 |
| python scripts/check_submission.py | WARN(대체 실행) | 현재 환경에 `python` 명령이 없어 `python3`로 실행. 제출 폴더와 부속 문서는 존재하나 DOCX/PDF 없음 |
| make check | FAIL | 참고문헌 점검 실패로 `refs` 단계에서 종료 |
