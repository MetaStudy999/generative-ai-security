# W06 1페이지 핸드아웃

## 주제

확률생성모형(Diffusion/GAN) & 딥페이크 검출

## 핵심 메시지

딥페이크 탐지기는 in-domain accuracy만으로 신뢰할 수 없다. Cross-domain FPR/FNR, calibration, human review routing, 재현성 로그를 함께 기록해야 한다.

## AI 원리

| 개념 | 핵심 |
|---|---|
| Diffusion | forward noise process와 reverse denoising process |
| Score-based model | 데이터 분포의 score를 이용한 sampling |
| GAN | generator-discriminator 경쟁 학습 |
| 조건부 생성 | text/image/class 조건으로 synthetic media 생성 방향 제어 |

## 보안 이슈

| 위험 | 평가 연결 |
|---|---|
| 허위정보와 사칭 | 딥페이크 생성·유통 위협모형 |
| False positive | 진짜 미디어를 가짜로 판단하는 위험 |
| False negative | 실제 조작물을 놓치는 위험 |
| Domain shift | 압축, 재인코딩, 미지 생성기 조건 |
| 자동판정 과신 | review rate와 auto coverage 기록 |

## 실험 결과

| 조건 | Accuracy | F1 | FPR | FNR | 비고 |
|---|---:|---:|---:|---:|---|
| In-domain | 1.000000 | 1.000000 | 0.000000 | 0.000000 | 기준 score 분리 |
| Cross-domain | 0.816667 | 0.813559 | 0.166667 | 0.200000 | 신뢰성 저하 |
| Review-band | 0.909091 | 0.901408 | 0.050000 | 0.135135 | review rate 0.358333 |

## 기억할 점

1. 생성모형 품질 지표와 탐지기 신뢰성 지표는 다르다.
2. Accuracy만 보면 FPR/FNR trade-off가 숨겨진다.
3. 불확실 구간은 자동판정보다 human review로 넘기는 설계가 필요하다.
4. 이번 수치는 synthetic toy 결과이며 실제 포렌식 성능 주장이 아니다.
5. P02/P03은 ACM DOI가 확인되었지만 강의계획서 지정 문헌 표기와 로컬/출판사 메타데이터 차이를 최종 확인해야 한다.

<!-- formula-visual-handout:start -->
## 수식·그래프·그림 보강 요약

| 항목 | 반영 내용 |
|---|---|
| 핵심 수식 | Diffusion Forward Process와 Denoising Objective, GAN Min-Max와 FPR/FNR |
| 그래프 | `assets/charts/w06_metrics_chart.png` (`metrics_summary.csv` 기반) |
| 다이어그램 | `assets/diagrams/w06_pipeline_diagram.svg` (generated-media detection pipeline) |
| 기호 정의 | 통합보고서와 발표 슬라이드의 수식 블록에 포함 |
| 주의사항 | 생성 모델 수식은 표준 학습 목적 설명이며 deepfake 제작 절차를 안내하지 않는다. |
<!-- formula-visual-handout:end -->
