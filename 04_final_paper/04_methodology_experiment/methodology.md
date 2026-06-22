# 연구방법

## 1. 연구방법 개요

본 연구는 다음 방식을 결합한 문헌분석 기반 프레임워크 설계 연구이다.

- 문헌분석
- 사례분석
- 모의실험 설계
- 체크리스트 설계
- 프레임워크 설계

W07, W08, W11, W14, W15 보고서를 중심으로 LLM/RAG 보안 위협과 재현성 평가 항목을 통합한다.

## 2. 분석 대상

| 항목 | 내용 |
|---|---|
| 대상 시스템 | LLM/RAG 기반 AI 응용 및 연구용 toy evaluation 파이프라인 |
| 보안 위협 | 프롬프트 인젝션, RAG 문서 오염, benchmark contamination, privacy leakage, 재현성 실패 |
| 분석 자료 | W07, W08, W11, W14, W15 주차 보고서, 논문 비교표, 이론노트, AI 활용기록 |
| 실험 데이터 | 공개 데이터 또는 synthetic context 기반 toy evaluation 설계 |
| 평가 지표 | Utility, Attack Success Rate, Privacy Leakage, Robustness, Reproducibility, Cost, Auditability |

## 3. 연구 절차

1. 관련연구 수집
2. 선행연구 비교표 작성
3. 위협모형 정의
4. 평가방법 설계
5. 모의실험 또는 사례분석 수행
6. 보안적 함의 도출
7. 한계와 후속 연구 정리

## 4. 방법론의 한계

정량 실험은 실제 실행 전까지 결과를 작성하지 않는다. 실행한 경우에는 `outputs/run_log.md`, `metrics_summary.csv`, `results.json`을 근거로 결과표를 채우고, 사용한 config와 seed를 함께 보존한다. DOI/URL과 국내 문헌은 최종 검증 후 확정한다.
