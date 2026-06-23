# W11 Differential Privacy & Membership Inference

Research Question: Differential Privacy & Membership Inference에서 성능 지표와 보안 지표를 어떻게 분리해 평가할 수 있는가?

---

## Core Formula

### Differential Privacy Definition

$$
\Pr[M(D)\in S]\le e^{\varepsilon}\Pr[M(D')\in S]+\delta
$$

| 기호 | 의미 |
|---|---|
| `M` | 무작위 알고리즘 또는 학습 절차 |
| `D,D'` | 한 레코드만 다른 adjacent datasets |
| `S` | 가능한 출력 사건 |
| `\varepsilon,\delta` | DP privacy parameters |

- 직관적 의미: DP는 한 개인 레코드의 포함 여부가 출력 분포를 크게 바꾸지 않도록 제한하는 표준 정의다.
- 보안적 의미: Membership inference 위험을 줄이려는 privacy claim은 이 정의와 accountant 근거가 있어야 한다.
- 평가 지표 연결: epsilon, delta, privacy_leakage_score, mi_attack_accuracy와 연결한다.
- 한계: 현재 CSV의 `epsilon_proxy`는 formal accountant 결과가 아니므로 보증값으로 쓰지 않는다.

---

## Threat Model

- Diagram: DP-SGD and MI audit flow
- Stages: Dataset, Clip Gradients, Add Noise, Model, MI Audit
- 안전 범위: public, synthetic, toy, local evaluation

![W11 pipeline diagram](assets/diagrams/w11_pipeline_diagram.svg)

---

## Evaluation Protocol

- Metrics: accuracy, mi_attack_accuracy, epsilon_proxy, privacy_leakage_score, utility_drop
- 데이터 출처: `04_experiment/outputs/metrics_summary.csv`

| condition | accuracy | mi_attack_accuracy | epsilon_proxy | privacy_leakage_score | utility_drop |
| --- | --- | --- | --- | --- | --- |
| Non-DP baseline | 0.956 | 0.516 | not_applicable | 0.015 | 0 |
| DP-like noise low | 0.956 | 0.516 | 8 | 0.014 | 0 |
| DP-like noise medium | 0.963 | 0.512 | 3 | 0.012 | 0 |
| DP-like noise high | 0.95 | 0.522 | 1 | 0.016 | 0.006 |

---

## Figure-first Result

![W11 metrics chart](assets/charts/w11_metrics_chart.svg)

그래프는 accuracy, MI attack accuracy, epsilon_proxy, leakage score, utility_drop, noise_multiplier를 조건별로 비교한다. `epsilon_proxy`는 formal DP accountant 결과가 아니므로 privacy guarantee로 읽으면 안 된다. 수치는 W11 outputs의 toy 결과 그대로다.

---

## Paper Map

| ID | 논문 역할 | 발표에서 쓰는 위치 | 기말논문 연결 |
|---|---|---|---|
| P01 | 핵심 이론 | Background / Core Formula | Differential Privacy & Membership Inference의 관련연구 뼈대 |
| P02 | 위협 분류 | Threat Model | 공격자·방어자·보호자산 정의 |
| P03 | 평가 지표 | Evaluation Protocol | 정량 지표와 로그 근거 연결 |
| P04 | 공격·방어 사례 | Security Implication | 보안적 함의와 방어 한계 |
| P05 | 재현성·정책 근거 | Limitation | 확인 필요 항목과 제출 전 검증 |

---

## Limitation

- `epsilon_proxy`는 formal DP accountant 값이 아니며 formal DP guarantee로 쓰지 않는다.
- 원문 DOI/URL과 formal guarantee는 최종 제출 전 확인 필요.
- 실제 운영 시스템 악용 절차나 무단 API 질의 절차는 포함하지 않음.

---

## Final Takeaway

W11의 핵심은 `accuracy, mi_attack_accuracy, epsilon_proxy, privacy_leakage_score, utility_drop`를 성능·보안·재현성 근거로 분리해 기말논문의 평가방법에 연결하는 것이다.
