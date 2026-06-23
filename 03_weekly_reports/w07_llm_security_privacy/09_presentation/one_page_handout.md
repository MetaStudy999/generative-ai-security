# W07 주차 연구 발표 요약

## Research Question

이 주차에서 성능 지표와 보안 지표를 어떻게 분리해 평가할 수 있는가?

## Key Formula

**Language Modeling Objective와 Perplexity**

$$
\mathcal{L}_{LM}=-\sum_{t=1}^{T}\log p_\theta(x_t|x_{<t}),
\qquad
PPL=\exp\left(\frac{1}{T}\mathcal{L}_{LM}\right)
$$

- 기호와 의미는 슬라이드의 표를 기준으로 설명한다.
- 보안적 의미: 보안 평가에서는 품질 지표와 privacy leakage, unsafe completion을 분리해야 한다.

## Threat Model

LLM privacy/safety evaluation flow 기준으로 공격자, 방어자, 보호 자산, 성공 조건을 분리한다.

## Main Figure

- Diagram: `assets/diagrams/w07_pipeline_diagram.svg`
- Chart: `assets/charts/w07_metrics_chart.svg`

## Evaluation Metrics

utility, attack_success_rate, privacy_leakage_rate, code_vulnerability_rate. 실제 수치는 `04_experiment/outputs/metrics_summary.csv` 기준이다.

## Security Implication

Clean 성능과 보안 지표는 서로 다른 실패 모드를 설명하므로 같은 결론으로 합치지 않는다.

## Limitation

privacy leakage는 toy/proxy metric이며 실제 개인정보 추출 실험으로 해석하지 않는다. toy/synthetic 범위와 formal guarantee 여부를 구분해야 한다.

## Final Paper Link

기말논문에서는 관련연구, 위협모형, 평가방법, 한계 절에 이 주차의 수식·표·그래프·다이어그램을 연결한다.
