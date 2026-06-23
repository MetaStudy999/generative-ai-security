# W13 1페이지 요약

## 핵심 메시지

모델 추출 위험은 victim/substitute 출력 일치율인 fidelity로 보고, 워터마크 기반 소유권 검증은 detection rate와 false positive rate를 함께 봐야 한다.

## 문헌 상태

| ID | 역할 | 상태 |
|---|---|---|
| P01 | model stealing taxonomy | DOI 확인 |
| P02 | watermarking/fingerprinting | SUBSTITUTE, 원문 확보 필요 |
| P03 | DNN watermarking trade-off | DOI 확인, 표기 차이 |
| P04 | ModelShield | IEEE TIFS DOI 확인 |
| P05 | GAN attack/defense | SUBSTITUTE, 지정 후보 DOI 확인 |

## 실험 결과

| 조건 | Query Budget | Fidelity | Detection | FPR |
|---|---:|---:|---:|---:|
| Substitute query 100 | 100 | 0.864000 | 0.700000 | 0.600000 |
| Substitute query 500 | 500 | 0.920000 | 1.000000 | 0.600000 |
| Substitute query 1000 | 1000 | 0.902000 | 1.000000 | 0.600000 |

Baseline victim utility accuracy는 0.868000이다. 실험은 synthetic toy 환경에서만 수행했으며 실제 API, 실제 LLM, 개인정보, 무단 질의는 포함하지 않는다.

## False Positive 해석

FPR 0.600000은 trigger-set detection만으로 소유권을 강하게 주장하기 어렵다는 신호다. clean control, unrelated model, random trigger control, multiple seeds, statistical testing이 필요하다.

## 기말논문 연결

“모델 추출 이후 소유권 검증을 위한 다중지표 평가 프레임워크”로 발전시킬 수 있다. 핵심 지표는 fidelity, query cost, detection, false positive, utility, reproducibility다.

<!-- formula-visual-handout:start -->
## 수식·그래프·그림 보강 요약

| 항목 | 반영 내용 |
|---|---|
| 핵심 수식 | Model Extraction Query Objective, Watermark Detection Rate, FPR/FNR, Utility Loss |
| 그래프 | `assets/charts/w13_metrics_chart.png` (`metrics_summary.csv` 기반) |
| 다이어그램 | `assets/diagrams/w13_pipeline_diagram.svg` (model extraction and watermark audit flow) |
| 기호 정의 | 통합보고서와 발표 슬라이드의 수식 블록에 포함 |
| 주의사항 | model extraction은 방어 평가 관점의 toy query objective로만 설명한다. |
<!-- formula-visual-handout:end -->
