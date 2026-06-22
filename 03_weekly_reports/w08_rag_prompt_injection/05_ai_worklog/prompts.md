# 주요 프롬프트 기록

| 구분 | 프롬프트 요지 | 사용 목적 | 반영 위치 |
|---|---|---|---|
| 공통 지침 확인 | 공통 지침 확인 후 W08 완성 | 작업 범위 설정 | 전체 산출물 |
| 서지 검증 | W08 PDF 첫 페이지와 DOI/URL 상태 확인 | 논문 목록 보정 | `01_papers/`, `02_paper_summaries/` |
| 실험 설계 | RAG prompt injection을 synthetic document 기반으로 안전하게 평가 | toy evaluator 작성 | `04_experiment/src/run_experiment.py` |
| 보고서 작성 | 실행 outputs 기준으로 통합보고서, 제출본, 발표자료 작성 | 제출 가능한 산출물 작성 | `06_report/`, `07_week_submission/`, `09_presentation/` |
| 안전성 점검 | 실제 공격 payload, 개인정보, 외부 시스템 공격 절차 제외 | 연구윤리 확인 | 모든 보고서의 한계/제외 범위 |

## 비고

프롬프트 기록은 작업 목적과 검증 경로를 남기기 위한 요약이며, 민감정보나 실제 공격 payload는 포함하지 않는다.
