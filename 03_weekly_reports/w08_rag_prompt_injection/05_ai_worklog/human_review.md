# 사람 검토 기록

| 검토 항목 | 검토 내용 | 상태 |
|---|---|---|
| 서지정보 | PDF 첫 페이지와 DOI/arXiv 식별자 대조 | 완료 |
| DOI 임의 생성 방지 | P01은 placeholder DOI라 미확정 처리 | 완료 |
| 실험 안전 범위 | 실제 개인정보, 외부 API, live tool 호출 없음 | 완료 |
| 실험 수치 | `metrics_summary.csv`, `results.json`, `run_log.md` 값 대조 | 완료 |
| 보고서 일관성 | 실험보고서, 통합보고서, 제출본, 발표자료 같은 수치 사용 | 완료 |
| 한계 표현 | toy evaluator이며 실제 LLM 성능으로 일반화하지 않음 | 완료 |
| 강의계획서와 로컬 PDF 차이 | P01/P02/P04/P05 표기 차이를 확인 필요로 유지 | 완료 / 확인 필요 |
| PDF 보관 정책 | PDF 5개가 git 추적 중임을 확인하고 삭제 필요 가능성 표시 | 완료 / 확인 필요 |

## 추가 확인 필요

1. P01의 공식 출판 DOI가 이후 확정되었는지 최종 제출 전 확인한다.
2. P01이 강의계획서의 Shiyu Chen et al. / ACM Computing Surveys 2025 표기와 동일 논문인지 확인한다.
3. P02의 Jianxiang Li et al. 표기와 DOI 기준 Zulun Zhu et al. 논문이 동일한지 확인한다.
4. P04의 Tianlei/Tongcheng Geng 표기 차이를 확인한다.
5. P05의 강의계획서 지정 제목과 DOI 기준 제목이 동일 논문인지 확인한다.
6. public GitHub 저장소에 PDF 원문을 유지해도 되는지 저작권·라이선스 관점에서 확인한다.
