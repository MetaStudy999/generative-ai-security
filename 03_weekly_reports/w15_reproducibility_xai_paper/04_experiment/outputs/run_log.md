# W15 재현성·제출 준비 감사 실행 로그

- 실행 시각(UTC): 2026-06-23T01:54:55.937212+00:00
- 실행 명령: `python src/run_experiment.py --config configs/config.yaml`
- 실험 성격: 모델 성능 실험이 아니라 로컬 산출물 감사
- 개인정보 사용: 없음
- 실제 공격 수행: 없음
- benchmark 성능 주장: 없음

## 결과 요약

| 항목 | 값 | 상태 | 근거 |
|---|---:|---|---|
| w15_required_files | 47/47 | complete | `03_weekly_reports/w15_reproducibility_xai_paper` |
| final_paper_link_files | 9/9 | complete | `04_final_paper` |
| local_pdf_count | 5 | complete | `01_papers/pdf` |
| doi_confirmed | 4 | complete | `01_papers/doi_check.md` |
| doi_partial | 1 | partial | `01_papers/doi_check.md` |
| doi_unverified | 0 | complete | `01_papers/doi_check.md` |
| weighted_reference_verification_rate | 0.90 | partial | `01_papers/doi_check.md` |
| ai_disclosure_completeness | 11/11 | complete | `05_ai_worklog/ai_disclosure_draft.md` |
| config_present | 1 | complete | `configs/config.yaml` |
| seed_recorded | 42 | complete | `configs/config.yaml` |

## 해석

W15 필수 산출물과 기말논문 연결 파일의 존재 여부, DOI/URL 검증 상태, AI 활용 고지 완성도를 점검했다.
P03은 공식 DOI 메타데이터를 확인했지만 로컬 PDF가 Mersha et al. 대체 문헌이므로 부분 확인으로 유지한다.
P05는 arXiv와 최종 ACM DOI가 연결되어 DOI 확인 상태로 갱신했다.
