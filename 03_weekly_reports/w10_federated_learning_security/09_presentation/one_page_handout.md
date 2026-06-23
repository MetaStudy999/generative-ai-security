# W10 주차 연구 발표 요약

## Research Question

이 주차에서 성능 지표와 보안 지표를 어떻게 분리해 평가할 수 있는가?

## Key Formula

**FedAvg Aggregation과 Client Update**

$$
\theta_{t+1}^{(k)}=\theta_t-\eta\nabla \mathcal{L}_k(\theta_t),
\qquad
\theta_{t+1}=\sum_{k=1}^{K}\frac{n_k}{n}\theta_{t+1}^{(k)}
$$

- 기호와 의미는 슬라이드의 표를 기준으로 설명한다.
- 보안적 의미: 악성 client update가 aggregation에 들어오면 global model과 backdoor 성능이 바뀔 수 있다.

## Threat Model

FL aggregation structure 기준으로 공격자, 방어자, 보호 자산, 성공 조건을 분리한다.

## Main Figure

- Diagram: `assets/diagrams/w10_pipeline_diagram.svg`
- Chart: `assets/charts/w10_metrics_chart.svg`

## Evaluation Metrics

global_accuracy, global_f1, attack_success_rate, privacy_leakage_proxy, mean_update_norm. 실제 수치는 `04_experiment/outputs/metrics_summary.csv` 기준이다.

## Security Implication

Clean 성능과 보안 지표는 서로 다른 실패 모드를 설명하므로 같은 결론으로 합치지 않는다.

## Limitation

privacy_leakage_proxy는 실제 gradient inversion 성공률이 아니며 proxy로만 해석한다. toy/synthetic 범위와 formal guarantee 여부를 구분해야 한다.

## Final Paper Link

기말논문에서는 관련연구, 위협모형, 평가방법, 한계 절에 이 주차의 수식·표·그래프·다이어그램을 연결한다.
