# 평가방법

| 평가 항목 | 지표 | 측정 방법 | 필요한 데이터 | 비고 |
|---|---|---|---|---|
| Clean Performance | Clean score | 정상 synthetic 입력에서 keyword detector 평가 | synthetic privacy-risk prompts | 실제 Transformer 성능 아님 |
| Attack Impact | Attack Success Rate | word substitution 후 privacy-risk 입력이 benign으로 오분류되는 비율 | 변형 입력 | 악용 절차 상세화 제외 |
| Robust Performance | Robust score | 공격 조건에서 clean score와 비교 | synthetic attacked prompts | 의미 유사도는 후속 과제 |
| Privacy/Leakage | Privacy leakage | regex 기반 원시 민감값 잔존 여부 점검 | masked/protected prompts | 실제 privacy guarantee 아님 |
| Utility | Utility score | 작업 의도 marker 유지 여부 확인 | masked/protected prompts | 과도한 마스킹 영향 점검 |
| Reproducibility | Seed/config/log completeness | seed, config, Docker, CSV, JSON, run_log 보존 여부 점검 | 실행 로그 | W04 outputs 생성 완료 |
| Human Review | 검토 완료 여부 | DOI, Article 번호, PDF 저작권, 인용 대응을 사람이 재검토 | 체크리스트 | 최종 책임 |

## 실행 근거

W04 정량 수치는 `04_experiment/outputs/run_log.md`, `metrics_summary.csv`, `results.json` 기준이다.

| 조건 | Clean Score | Attack Success Rate | Privacy Leakage | Utility Score |
|---|---:|---:|---:|---:|
| Clean baseline | 1.000000 | 해당 없음 | 해당 없음 | 1.000000 |
| Word substitution | 0.625000 | 0.750000 | 해당 없음 | 1.000000 |
| Prompt masking | 해당 없음 | 해당 없음 | 0.000000 | 1.000000 |
| Privacy-preserving prompt | 해당 없음 | 해당 없음 | 0.000000 | 1.000000 |

이 결과는 synthetic toy 실험의 평가 형식 검증용 수치이며, 실제 Transformer, LLM, 상용 NLP 시스템의 강건성 또는 프라이버시 보호 성능으로 일반화하지 않는다.
