# 실험 및 분석 보고서

## 1. 목적

이 문서는 기말 모의투고 논문의 방법론 재현성을 점검하기 위한 synthetic toy case 기반 정적 분석 보고서다. 실제 LLM 호출, 실제 RAG 시스템 공격, 실제 개인정보 처리, 무단 API 호출은 수행하지 않는다.

## 2. 분석 범위

| 항목 | 내용 |
|---|---|
| 입력 데이터 | `data/synthetic_documents.csv` |
| 설정 파일 | `configs/config.yaml` |
| 실행 스크립트 | `src/run_analysis.py` |
| 결과 파일 | `outputs/results.json`, `outputs/metrics_summary.csv`, `outputs/run_log.md` |
| 지표 | ASR, DPR, Leakage, RC |

## 3. 데이터 설명

`synthetic_documents.csv`는 정상 문서, 간접 프롬프트 인젝션 예시, synthetic privacy 예시를 포함한다. 모든 행은 연구 윤리와 안전한 재현성 점검을 위한 가상 문서이며 실제 개인정보나 실제 서비스 공격 대상 정보를 포함하지 않는다.

## 4. 지표 해석

| 지표 | 의미 | 주의 |
|---|---|---|
| ASR | high risk 문서 중 차단 기대가 아닌 사례 비율 | 실제 공격 성공률이 아니다. |
| DPR | high risk 문서 중 차단 기대로 분류된 비율 | 실제 방어 시스템 성능이 아니다. |
| Leakage | synthetic privacy 문서 중 차단 기대가 아닌 사례 비율 | 실제 개인정보 누수 실험이 아니다. |
| RC | risk label과 expected control이 모두 채워진 문서 비율 | 연구 관리 완성도 점검 지표다. |

## 5. 실행 방법

```bash
python 04_final_paper/04_methodology_experiment/src/run_analysis.py
```

## 6. 결과 기록 원칙

정량 결과는 `outputs/results.json`, `outputs/metrics_summary.csv`, `outputs/run_log.md`에 기록된 값만 사용한다. 논문 본문에는 이 값을 실제 모델 성능, 실제 공격 성공률, 실제 서비스 보안성 평가처럼 서술하지 않는다.
