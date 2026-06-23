# 실험 설계

## 1. 실험 목적

LLM/RAG 보안 평가 프레임워크가 성능, 공격 영향, 프라이버시, 재현성 항목을 함께 기록할 수 있는지 점검한다.

## 2. 실험 대상

| 항목 | 내용 |
|---|---|
| 대상 시스템/모델 | 공개 또는 toy LLM/RAG 평가 파이프라인 |
| 데이터셋 | 공개 문서 또는 synthetic context |
| 비교 기준선 | 보안 통제 전 baseline |
| 공격/위협 시나리오 | 간단한 prompt injection, RAG 문서 오염, benchmark contamination 시나리오 |
| 방어/평가 방법 | 출처 검증, context filtering, human approval, 재현성 체크리스트 |

## 3. 실험 절차

| 단계 | 수행 내용 | 산출물 |
|---:|---|---|
| 1 | baseline 평가 설계 | 기준 성능표 |
| 2 | 안전한 위협 시나리오 정의 | 위협모형표 |
| 3 | 방어·검토 절차 적용 | 평가 체크리스트 |
| 4 | config, seed, `04_final_paper/04_methodology_experiment/outputs/` 기록 | 재현성 패키지 |

## 4. 결과 작성 원칙

- 실제 수행하지 않은 실험 결과는 결과처럼 작성하지 않는다.
- 실제 수행한 실험 결과는 `04_final_paper/04_methodology_experiment/outputs/run_log.md`, `metrics_summary.csv`, `results.json`과 대조 가능한 값만 작성한다.
- 재현 가능한 설정과 한계를 함께 기록한다.
