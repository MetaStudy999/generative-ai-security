# W12 주차 연구 발표 요약

## Research Question

이 주차에서 성능 지표와 보안 지표를 어떻게 분리해 평가할 수 있는가?

## Key Formula

**Robustness Objective와 Certified Radius**

$$
\min_\theta \mathbb{E}_{(x,y)}\left[\max_{\lVert \delta\rVert\le \epsilon}\ell(f_\theta(x+\delta),y)\right],
\qquad
\forall \delta:\lVert\delta\rVert\le r,\ f(x+\delta)=f(x)
$$

- 기호와 의미는 슬라이드의 표를 기준으로 설명한다.
- 보안적 의미: 보안 주장에는 empirical robustness와 formal certificate를 구분해야 한다.

## Threat Model

verification-XAI robustness flow 기준으로 공격자, 방어자, 보호 자산, 성공 조건을 분리한다.

## Main Figure

- Diagram: `assets/diagrams/w12_pipeline_diagram.svg`
- Chart: `assets/charts/w12_metrics_chart.svg`

## Evaluation Metrics

clean_accuracy, robust_accuracy, explanation_stability, certified_rate, fairness_gap. 실제 수치는 `04_experiment/outputs/metrics_summary.csv` 기준이다.

## Security Implication

Clean 성능과 보안 지표는 서로 다른 실패 모드를 설명하므로 같은 결론으로 합치지 않는다.

## Limitation

`certified_rate`는 toy proxy 또는 제한 실험인지 formal verification인지 최종 원문 확인이 필요하다. toy/synthetic 범위와 formal guarantee 여부를 구분해야 한다.

## Final Paper Link

기말논문에서는 관련연구, 위협모형, 평가방법, 한계 절에 이 주차의 수식·표·그래프·다이어그램을 연결한다.
