# W06 주차 연구 발표 요약

## Research Question

이 주차에서 성능 지표와 보안 지표를 어떻게 분리해 평가할 수 있는가?

## Key Formula

**Diffusion Forward Process와 Denoising Objective**

$$
q(x_t|x_{t-1})=\mathcal{N}\left(\sqrt{1-\beta_t}x_{t-1},\beta_t I\right),
\qquad
\mathcal{L}_{simple}=\mathbb{E}_{t,x_0,\epsilon}\left[\lVert \epsilon-\epsilon_\theta(x_t,t)\rVert_2^2\right]
$$

- 기호와 의미는 슬라이드의 표를 기준으로 설명한다.
- 보안적 의미: 보안 발표에서는 생성 원리보다 탐지와 검증 지표를 중심에 둔다.

## Threat Model

generated-media detection pipeline 기준으로 공격자, 방어자, 보호 자산, 성공 조건을 분리한다.

## Main Figure

- Diagram: `assets/diagrams/w06_pipeline_diagram.svg`
- Chart: `assets/charts/w06_metrics_chart.svg`

## Evaluation Metrics

accuracy, f1, false_positive_rate, false_negative_rate, auroc. 실제 수치는 `04_experiment/outputs/metrics_summary.csv` 기준이다.

## Security Implication

Clean 성능과 보안 지표는 서로 다른 실패 모드를 설명하므로 같은 결론으로 합치지 않는다.

## Limitation

생성 모델 수식은 표준 학습 목적 설명이며 deepfake 제작 절차를 안내하지 않는다. toy/synthetic 범위와 formal guarantee 여부를 구분해야 한다.

## Final Paper Link

기말논문에서는 관련연구, 위협모형, 평가방법, 한계 절에 이 주차의 수식·표·그래프·다이어그램을 연결한다.
