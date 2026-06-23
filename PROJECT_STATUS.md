# 연구 프로젝트 상태표

## 1. 저장소 기본 정보

| 항목 | 내용 |
|---|---|
| 저장소명 | generative-ai-security |
| 연구 주제 | AI 보안 기말 모의투고 논문 |
| 주요 대상 폴더 | `03_weekly_reports`, `04_final_paper`, `06_submission` |
| 상태 기준일 | 2026-06-23 |

## 2. 현재 연구 진행 현황

| 구분 | 상태 | 근거 파일 | 비고 |
|---|---|---|---|
| W01-W15 제출보고서 | 보완 완료 | `03_weekly_reports/*/07_week_submission/` | Markdown/HTML/체크리스트 갱신 |
| W01-W15 그래프 | 생성 완료 | `07_week_submission/assets/wXX_metric_chart.png` | 각 주차 `metrics_summary.csv` 기반 |
| AI 활용 고지 | PASS | `04_final_paper/06_appendices/ai_disclosure.md` | 주차별 고지도 갱신 |
| 참고문헌 검증 | 미충족 | `04_final_paper/06_appendices/reference_verification.md` | 국내 문헌과 일부 해외 문헌 확인 필요 |
| DOCX 제출본 | 생성 | `06_submission/final_paper_submission/` | Markdown 초안 변환본 |
| PDF 제출본 | 보류(pandoc/libreoffice 없음) | `06_submission/final_paper_submission/` | pandoc/libreoffice 필요 |
| PDF Git 추적 | 해제 완료 | `05_references/PDF_POLICY.md` | 로컬 파일 삭제 아님 |
| 전체 감사표 | 작성 완료 | `AUDIT_REPORT_WEEKLY_SUBMISSIONS.md` | 교수 제출 전 잔여 항목 확인용 |

## 3. 미해결 이슈

| 번호 | 이슈 | 우선순위 | 상태 | 조치 |
|---:|---|---|---|---|
| 1 | 국내 논문 3편 공식 검증 | 상 | 확인 필요 | KCI, DBpia, RISS, Google Scholar, 출판사 페이지 확인 |
| 2 | 일부 주차 지정 논문/로컬 문헌 불일치 후보 | 상 | 부분 확인 | 각 주차 `doi_check.md` 기준으로 교체 또는 대체 문헌 표시 |
| 3 | 최종 학회지 양식 확정 | 상 | 확인 필요 | 학회명, 논문지명, 투고규정 URL 최종 확인 |
| 4 | 최종 PDF 변환 | 중 | 확인 필요 | pandoc/libreoffice 사용 가능 환경에서 변환 |
| 5 | Git 히스토리 내 과거 PDF 제거 | 중 | 별도 작업 | 현재 추적 해제와 정책 문서화만 수행 |

## 4. 자동 점검 실행 결과

| 명령 | 결과 | 비고 |
|---|---|---|
| `python3 scripts/check_references.py` | FAIL/WARN | 종료코드 1 |
| `python3 scripts/check_ai_disclosure.py` | PASS | 종료코드 0 |
| `python3 scripts/check_submission.py` | PASS | 종료코드 0 |
| `make check` | FAIL/WARN | 종료코드 2 |

## 5. 다음 작업

- [ ] 국내 문헌 3편 공식 검증 및 참고문헌 표 확정
- [ ] 강의계획서 지정 논문과 주차별 P01-P05 최종 대조
- [ ] 학회지 양식에 맞춘 DOCX 서식 정리
- [ ] PDF 변환 및 최종 육안 검수
