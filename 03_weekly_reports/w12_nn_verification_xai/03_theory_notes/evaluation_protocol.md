# 평가방법

| 평가 항목 | 지표 | 측정 방법 | 필요한 데이터 | 비고 |
|---|---|---|---|---|
| Clean Performance | Accuracy/F1/Task score | 정상 조건에서 기준 모델 평가 | 공개 또는 synthetic 데이터 | 기본 성능 |
| Attack Impact | Attack Success Rate/Risk score | 대적공격과 대적방어, Certified robustness 조건을 모의 | 변형 입력 또는 시나리오 | 악용 절차는 제외 |
| Robust Performance | Robust score | 공격 또는 교란 조건에서 성능 비교 | 교란 데이터 | 강건성 |
| Privacy/Leakage | Leakage score | 민감정보 노출 가능성 점검 | synthetic shadow data | 실제 개인정보 금지 |
| Reproducibility | Seed/config/log completeness | seed, config, Docker, 결과표 보존 여부 점검 | 실행 로그 | 결과값은 실제 실행 후 기록 |
| Human Review | 검토 완료 여부 | 원문, DOI, 수치, 인용을 사람이 재검토 | 체크리스트 | 최종 책임 |

## 실행 전제

실험 결과는 실제 실행 전까지 비워 두거나 `실행 전`으로 표시한다. 본 파일은 평가 설계서이며, 정량 수치는 `04_experiment/outputs/run_log.md`, `metrics_summary.csv`, `results.json`이 생긴 뒤에만 채운다.
