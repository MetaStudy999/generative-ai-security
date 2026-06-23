# Run Log

## 1. 실행 개요

| 항목 | 내용 |
|---|---|
| 실행 일시 | 2026-06-23T11:56:15+09:00 |
| 입력 파일 | `data/synthetic_documents.csv` |
| 결과 파일 | `outputs/results.json`, `outputs/metrics_summary.csv` |
| 분석 유형 | synthetic toy document static audit |
| 실제 LLM 호출 | 수행하지 않음 |
| 외부 API 호출 | 수행하지 않음 |
| 실제 공격 자동화 | 수행하지 않음 |
| 실제 개인정보 사용 | 수행하지 않음 |

## 2. 집계 결과

| 항목 | 값 |
|---|---:|
| 전체 문서 수 | 5 |
| high risk 문서 수 | 3 |
| 차단 기대 사례 수 | 3 |
| 차단 성공으로 계산한 high risk 사례 수 | 3 |
| privacy 유형 문서 수 | 1 |

## 3. 정적 감사 지표

| 지표 | 값 | 해석 |
|---|---:|---|
| ASR | 0.0 | high risk 문서 중 차단 기대가 아닌 사례 비율 |
| DPR | 1.0 | high risk 문서 중 차단 기대로 분류된 비율 |
| Leakage | 0.0 | synthetic privacy 문서 중 차단 기대가 아닌 사례 비율 |
| RC | 1.0 | risk label과 expected control이 모두 채워진 문서 비율 |

## 4. 주의

이 로그는 실제 모델, 실제 RAG 시스템, 실제 서비스, 실제 공격 절차를 평가한 결과가 아니다. `synthetic_documents.csv`에 기록된 toy case의 정적 기대 통제값을 집계한 재현성 점검용 산출물이다.
