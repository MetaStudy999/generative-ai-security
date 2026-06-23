# 최종 제출 패키지

## 1. 현재 포함 파일

| 파일 | 상태 | 비고 |
|---|---|---|
| 최종 논문 DOCX | 생성 | `final_paper_draft.docx` |
| 최종 논문 PDF | 보류(pandoc/libreoffice 없음) | pandoc/libreoffice 미설치 환경에서는 변환 보류 |
| AI 활용 고지서 | 준비 | `04_final_paper/06_appendices/ai_disclosure.md` |
| 참고문헌 검증표 | 준비, 미확정 항목 있음 | `04_final_paper/06_appendices/reference_verification.md` |
| 학회지 양식 출처표 | 준비, 최종 학회 확인 필요 | `04_final_paper/00_journal_format/journal_format_source.md` |
| 주차별 보고서 반영표 | 준비 | `04_final_paper/02_weekly_reflection/weekly_reflection_table.md` |

## 2. 생성/변환 명령

현재 컨테이너에는 `pandoc`과 `libreoffice/soffice`가 없어 PDF 변환은 수행하지 않았다. 사용 가능한 환경에서는 아래 명령을 사용한다.

```bash
pandoc 04_final_paper/05_draft/paper_draft.md -o 06_submission/final_paper_submission/final_paper_draft.docx
libreoffice --headless --convert-to pdf --outdir 06_submission/final_paper_submission 06_submission/final_paper_submission/final_paper_draft.docx
```

## 3. 제출 전 최종 점검

- [ ] 선택한 국내 학회지 양식을 확정했다.
- [ ] 국내 논문 3편 이상을 공식 경로로 검증했다.
- [ ] `부분 확인` 또는 `확인 필요` 문헌이 본문 핵심 근거로 쓰이지 않는지 확인했다.
- [ ] PDF 변환 후 한글, 표, 그림, 참고문헌 번호 깨짐을 확인했다.
- [ ] public GitHub에는 논문 PDF 원문이 추적되지 않도록 유지했다.
