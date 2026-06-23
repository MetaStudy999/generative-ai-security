# W05 주차 연구 발표 요약

## Research Question

이 주차에서 성능 지표와 보안 지표를 어떻게 분리해 평가할 수 있는가?

## Key Formula

**Contrastive Loss와 Representation Shift**

$$
\mathcal{L}_{NCE}=-\log
\frac{\exp(sim(z_i,z_i^+)/\tau)}
{\sum_{j}\exp(sim(z_i,z_j)/\tau)},
\qquad
\Delta_z=\lVert \mu_{clean}-\mu_{trigger}\rVert_2
$$

- 기호와 의미는 슬라이드의 표를 기준으로 설명한다.
- 보안적 의미: 은닉 trigger가 representation에 남으면 downstream classifier에서 조건부 실패가 생길 수 있다.

## Threat Model

SSL backdoor evaluation flow 기준으로 공격자, 방어자, 보호 자산, 성공 조건을 분리한다.

## Main Figure

- Diagram: `assets/diagrams/w05_pipeline_diagram.svg`
- Chart: `assets/charts/w05_metrics_chart.svg`

## Evaluation Metrics

clean_accuracy, attack_success_rate, attack_after_defense, representation_shift, trigger_detection_rate. 실제 수치는 `04_experiment/outputs/metrics_summary.csv` 기준이다.

## Security Implication

Clean 성능과 보안 지표는 서로 다른 실패 모드를 설명하므로 같은 결론으로 합치지 않는다.

## Limitation

trigger 관련 설명은 공개 toy/synthetic 범위이며 실제 악용 가능한 절차를 제공하지 않는다. toy/synthetic 범위와 formal guarantee 여부를 구분해야 한다.

## Final Paper Link

기말논문에서는 관련연구, 위협모형, 평가방법, 한계 절에 이 주차의 수식·표·그래프·다이어그램을 연결한다.
