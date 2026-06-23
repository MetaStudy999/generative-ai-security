# W12 통합보고서 초안

이 초안은 최종본 `../final/integrated_report_final.md`와 같은 구조를 따른다. 2026-06-22 실행 결과를 반영했으며, 정량값은 `04_experiment/outputs/`의 CSV/JSON/로그와 일치해야 한다.

## 핵심 요약

W12는 신경망 검증과 정형방법을 바탕으로 대적 강건성, XAI 설명 안정성, 정확도, 공정성 trade-off를 다중지표로 보고하는 주차다. toy 실험에서는 clean accuracy 0.818750, robust accuracy 0.543750, explanation stability 0.927782를 기준값으로 기록했다.

## 초안 점검 항목

| 항목 | 상태 | 메모 |
|---|---|---|
| 문헌 요약 | 작성 | DOI/원문 세부 대조 필요 |
| AI 원리 | 작성 | verification, abstraction, certificate 중심 |
| 보안 이슈 | 작성 | adversarial/XAI/trade-off 중심 |
| 실험 | 실행 | synthetic toy 결과만 사용 |
| 제출본 | 작성 | `07_week_submission/w12_submission_report.md` |
| 발표본 | 작성 | `09_presentation/` |

## 초안 한계

로컬 PDF 중 `RELATED`가 포함된 파일은 프롬프트 지정 문헌과 실제 확보 문헌의 차이를 최종 확인해야 한다. 실험 결과는 교육용 proxy이며 실제 DNN formal verification 결과가 아니다.
