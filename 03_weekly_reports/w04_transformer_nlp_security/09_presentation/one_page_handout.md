# W04 주차 연구 발표 요약

## Research Question

이 주차에서 성능 지표와 보안 지표를 어떻게 분리해 평가할 수 있는가?

## Key Formula

**Scaled Dot-Product Attention**

$$
Attention(Q,K,V)=softmax\left(\frac{QK^\top}{\sqrt{d_k}}\right)V
$$

- 기호와 의미는 슬라이드의 표를 기준으로 설명한다.
- 보안적 의미: 입력 문맥이 길거나 오염되면 정보 흐름과 취약 응답이 달라질 수 있다.

## Threat Model

Transformer security evaluation flow 기준으로 공격자, 방어자, 보호 자산, 성공 조건을 분리한다.

## Main Figure

- Diagram: `assets/diagrams/w04_pipeline_diagram.svg`
- Chart: `assets/charts/w04_metrics_chart.svg`

## Evaluation Metrics

clean_score, attack_success_rate, privacy_leakage, utility_score. 실제 수치는 `04_experiment/outputs/metrics_summary.csv` 기준이다.

## Security Implication

Clean 성능과 보안 지표는 서로 다른 실패 모드를 설명하므로 같은 결론으로 합치지 않는다.

## Limitation

efficient attention 복잡도는 구조별로 달라 표준 비교식으로만 제시한다. toy/synthetic 범위와 formal guarantee 여부를 구분해야 한다.

## Final Paper Link

기말논문에서는 관련연구, 위협모형, 평가방법, 한계 절에 이 주차의 수식·표·그래프·다이어그램을 연결한다.
