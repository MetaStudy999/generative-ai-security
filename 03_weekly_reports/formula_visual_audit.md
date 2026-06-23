# Formula & Visual Audit

- 생성 일자: 2026-06-23
- 기준 브랜치: `main` (`git pull --ff-only` 결과 최신 상태 확인)
- 점검 범위: `03_weekly_reports/w01_*` ~ `03_weekly_reports/w15_*`
- 원칙: CSV/JSON/log에 없는 실험 수치를 만들지 않았고, 수식은 표준 정의식 또는 검증 가능한 평가식으로 제한했다.
- 모든 다이어그램은 AI-assisted conceptual diagram이며, 사실 자료나 실험 결과로 해석하지 않는다.

| 주차 | 통합보고서 수식 블록 | 기호 정의표 | 보안 관점 해석 | 평가 지표 연결 | 발표 슬라이드 수식 | 그래프 파일 | 다이어그램 파일 | MathJax/KaTeX | speaker_notes 보강 | qna 보강 | KCI 그림 상태 | 확인 필요 |
| -- | ----------- | ------ | -------- | -------- | ---------- | ------ | -------- | ------------- | ---------------- | ------ | --------- | ----- |
| W01 | 완료 | 완료 | 완료 | 완료 | 완료 | 완료 (w01_metrics_chart.png) | 완료 (w01_pipeline_diagram.svg) | MathJax 완료 | 완료 | 완료 | 완료 | 원문 논문별 절·쪽·그림 번호와 formal guarantee 여부는 확인 필요. |
| W02 | 완료 | 완료 | 완료 | 완료 | 완료 | 완료 (w02_metrics_chart.png) | 완료 (w02_pipeline_diagram.svg) | MathJax 완료 | 완료 | 완료 | 완료 | toy backdoor는 공개 toy 데이터 기반 안전 실습이며 실제 시스템 악용 절차로 일반화하지 않는다. |
| W03 | 완료 | 완료 | 완료 | 완료 | 완료 | 완료 (w03_metrics_chart.png) | 완료 (w03_pipeline_diagram.svg) | MathJax 완료 | 완료 | 완료 | 완료 | 대적 교란은 toy evaluation 범위로 설명하며 실제 시스템 우회 절차로 쓰지 않는다. |
| W04 | 완료 | 완료 | 완료 | 완료 | 완료 | 완료 (w04_metrics_chart.png) | 완료 (w04_pipeline_diagram.svg) | MathJax 완료 | 완료 | 완료 | 완료 | efficient attention 복잡도는 구조별로 달라 표준 비교식으로만 제시한다. |
| W05 | 완료 | 완료 | 완료 | 완료 | 완료 | 완료 (w05_metrics_chart.png) | 완료 (w05_pipeline_diagram.svg) | MathJax 완료 | 완료 | 완료 | 완료 | trigger 관련 설명은 공개 toy/synthetic 범위이며 실제 악용 가능한 절차를 제공하지 않는다. |
| W06 | 완료 | 완료 | 완료 | 완료 | 완료 | 완료 (w06_metrics_chart.png) | 완료 (w06_pipeline_diagram.svg) | MathJax 완료 | 완료 | 완료 | 완료 | 생성 모델 수식은 표준 학습 목적 설명이며 deepfake 제작 절차를 안내하지 않는다. |
| W07 | 완료 | 완료 | 완료 | 완료 | 완료 | 완료 (w07_metrics_chart.png) | 완료 (w07_pipeline_diagram.svg) | MathJax 완료 | 완료 | 완료 | 완료 | privacy leakage는 toy/proxy metric이며 실제 개인정보 추출 실험으로 해석하지 않는다. |
| W08 | 완료 | 완료 | 완료 | 완료 | 완료 | 완료 (w08_metrics_chart.png) | 완료 (w08_pipeline_diagram.svg) | MathJax 완료 | 완료 | 완료 | 완료 | prompt injection은 방어 평가 관점으로만 설명하고 실제 우회 절차는 제공하지 않는다. |
| W09 | 완료 | 완료 | 완료 | 완료 | 완료 | 완료 (w09_metrics_chart.png) | 완료 (w09_pipeline_diagram.svg) | MathJax 완료 | 완료 | 완료 | 완료 | DRL 환경은 toy simulation이며 실제 네트워크 공격 자동화 절차를 제공하지 않는다. |
| W10 | 완료 | 완료 | 완료 | 완료 | 완료 | 완료 (w10_metrics_chart.png) | 완료 (w10_pipeline_diagram.svg) | MathJax 완료 | 완료 | 완료 | 완료 | privacy_leakage_proxy는 실제 gradient inversion 성공률이 아니며 proxy로만 해석한다. |
| W11 | 완료 | 완료 | 완료 | 완료 | 완료 | 완료 (w11_metrics_chart.png) | 완료 (w11_pipeline_diagram.svg) | MathJax 완료 | 완료 | 완료 | 완료 | `epsilon_proxy`는 formal DP accountant 값이 아니며 formal DP guarantee로 쓰지 않는다. |
| W12 | 완료 | 완료 | 완료 | 완료 | 완료 | 완료 (w12_metrics_chart.png) | 완료 (w12_pipeline_diagram.svg) | MathJax 완료 | 완료 | 완료 | 완료 | `certified_rate`는 toy proxy 또는 제한 실험인지 formal verification인지 최종 원문 확인이 필요하다. |
| W13 | 완료 | 완료 | 완료 | 완료 | 완료 | 완료 (w13_metrics_chart.png) | 완료 (w13_pipeline_diagram.svg) | MathJax 완료 | 완료 | 완료 | 완료 | model extraction은 방어 평가 관점의 toy query objective로만 설명한다. |
| W14 | 완료 | 완료 | 완료 | 완료 | 완료 | 완료 (w14_metrics_chart.png) | 완료 (w14_pipeline_diagram.svg) | MathJax 완료 | 완료 | 완료 | 완료 | hash/pass 항목은 시각화에서 제외했으며 원본 CSV와 artifact inventory를 함께 확인해야 한다. |
| W15 | 완료 | 완료 | 완료 | 완료 | 완료 | 완료 (w15_metrics_chart.png) | 완료 (w15_pipeline_diagram.svg) | MathJax 완료 | 완료 | 완료 | 완료 | 비율 변환 값은 local completeness proxy이며 학술적 품질 보증 점수가 아니다. |
