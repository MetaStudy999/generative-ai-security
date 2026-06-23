# 연구 프로젝트 상태표

## 1. 저장소 기본 정보

| 항목 | 내용 |
|---|---|
| 저장소명 | generative-ai-security |
| 연구 주제 | AI 보안 기말 모의투고 논문 |
| 주요 대상 폴더 | `03_weekly_reports`, `04_final_paper`, `06_submission` |
| 상태 기준일 | 2026-06-24 KST |

## 2. 현재 연구 진행 현황

| 구분 | 상태 | 근거 파일 | 비고 |
|---|---|---|---|
| W01-W15 제출보고서 | 보완 완료 | `03_weekly_reports/*/07_week_submission/` | Markdown/HTML/체크리스트 갱신 |
| W01-W15 그래프 | 생성 완료 | `07_week_submission/assets/wXX_metric_chart.png` | 각 주차 `metrics_summary.csv` 기반 |
| AI 활용 고지 | PASS | `04_final_paper/06_appendices/ai_disclosure.md` | 주차별 고지도 갱신 |
| 참고문헌 검증 | PASS | `03_weekly_reports/WEEKLY_REFERENCE_VERIFICATION_AUDIT.md`, `04_final_paper/06_appendices/reference_verification.md` | 주차별 논문/관련 논문 구분 반영, 최종논문 최소 편수 충족 |
| DOCX 제출본 | 생성 | `06_submission/final_paper_submission/` | Markdown 초안 변환본 |
| PDF 제출본 | 보류(pandoc/libreoffice 없음) | `06_submission/final_paper_submission/` | pandoc/libreoffice 필요 |
| PDF Git 추적 | 해제 완료 | `05_references/PDF_POLICY.md` | 로컬 파일 삭제 아님 |
| 전체 감사표 | 작성 완료 | `AUDIT_REPORT_WEEKLY_SUBMISSIONS.md`, `03_weekly_reports/WEEKLY_STATUS.md` | 구조 점수와 수치/참고문헌 검증 점수를 분리 |

## 3. 미해결 이슈

| 번호 | 이슈 | 우선순위 | 상태 | 조치 |
|---:|---|---|---|---|
| 1 | 국내 논문 공식 DB 재확인 | 상 | 수동 확인 필요 | RISS/KCI/DBpia 상세 페이지에서 최종 제출 전 권호·쪽·URL 재확인 |
| 2 | 주차별 관련 논문/보조 문헌 구분 | 상 | 반영 | `03_weekly_reports/WEEKLY_REFERENCE_VERIFICATION_AUDIT.md` 및 각 주차 `doi_check.md` 기준으로 `논문 / 확인` 또는 `관련 논문 / 확인` 표시 |
| 3 | 최종 학회지 양식 확정 | 상 | 확인 필요 | 학회명, 논문지명, 투고규정 URL 최종 확인 |
| 4 | 최종 PDF 변환 | 중 | 확인 필요 | pandoc/libreoffice 사용 가능 환경에서 변환 |
| 5 | HTML/PDF 시각 검수 | 중 | 수동 확인 필요 | 자동 점검은 렌더링 깨짐을 보증하지 않음 |

## 4. 자동 점검 실행 결과

| 명령 | 결과 | 비고 |
|---|---|---|
| `python3 scripts/weekly_audit.py` | PASS | 종료코드 0, W01-W15 구조 100/100, W15 수치 대조 100/100 |
| `python3 scripts/check_references.py` | PASS/WARN | 종료코드 0, 최종논문 국내 6/해외 8 확인 완료(로컬 기록 기준), 주차별 수동 확인 WARN |
| `python3 scripts/check_ai_disclosure.py` | PASS | 종료코드 0 |
| `python3 scripts/check_submission.py` | PASS | 종료코드 0 |
| `make weekly-audit` | PASS | 종료코드 0, 상태표/감사표 재생성 |
| `make check` | PASS/WARN | 종료코드 0, 참고문헌 WARN 출력 유지 |

## 5. 다음 작업

- [ ] RISS/KCI/DBpia/출판사 페이지에서 최종 참고문헌 권호·쪽·URL 재확인
- [ ] 강의계획서 지정 논문과 주차별 P01-P05 최종 대조
- [ ] W02/W06/W09/W11/W13 발표자료 수치 표기 필요 여부 수동 판단
- [ ] 학회지 양식에 맞춘 DOCX 서식 정리
- [ ] PDF 변환 및 최종 육안 검수
