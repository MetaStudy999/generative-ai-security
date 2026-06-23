# W03 컴퓨터 비전 대적 공격

Research Question: 컴퓨터 비전 대적 공격에서 성능 지표와 보안 지표를 어떻게 분리해 평가할 수 있는가?

---

## Core Formula

### Adversarial Perturbation Constraint

$$
x' = x+\delta,
\qquad
\lVert \delta \rVert_p \le \epsilon
$$

| 기호 | 의미 |
|---|---|
| `x` | 원본 입력 |
| `x'` | 교란된 입력 |
| `\delta` | 입력 교란 |
| `\epsilon` | 허용 교란 반경 |

- 직관적 의미: 대적 예시는 작은 입력 교란이 예측을 바꿀 수 있는지를 보는 평가 개념이다. 핵심은 교란 크기와 모델 실패 여부를 함께 기록하는 것이다.
- 보안적 의미: 보안 관점에서는 입력 검증, 강건성 평가, defense 비용이 연결된다.
- 평가 지표 연결: robust accuracy, attack_success_rate, robust_drop, defense 여부와 연결한다.
- 한계: toy image setting이며 실제 운영 비전 시스템을 우회하는 절차가 아니다.

---

## Threat Model

- Diagram: adversarial evaluation flow
- Stages: Clean Image, Perturbation Set, Model, Defense, Robust Metrics
- 안전 범위: public, synthetic, toy, local evaluation

![W03 pipeline diagram](assets/diagrams/w03_pipeline_diagram.svg)

---

## Evaluation Protocol

- Metrics: accuracy, attack_success_rate, robust_drop
- 데이터 출처: `04_experiment/outputs/metrics_summary.csv`

| condition | accuracy | attack_success_rate | robust_drop |
| --- | --- | --- | --- |
| clean_baseline | 1 |  | 0 |
| centroid_direction_linf | 1 | 0 | 0 |
| centroid_direction_linf | 1 | 0 | 0 |
| centroid_direction_linf | 1 | 0 | 0 |
| centroid_direction_linf | 0 | 1 | 1 |

---

## Figure-first Result

![W03 metrics chart](assets/charts/w03_metrics_chart.svg)

그래프는 condition별 accuracy, attack_success_rate, robust_drop을 `metrics_summary.csv`에서 읽어 시각화한다. epsilon 또는 defense 조건별 변화는 robust accuracy를 clean accuracy와 분리해 보아야 함을 보여준다. 이미 존재하는 output 수치만 사용했다.

---

## Paper Map

| ID | 논문 역할 | 발표에서 쓰는 위치 | 기말논문 연결 |
|---|---|---|---|
| P01 | 핵심 이론 | Background / Core Formula | 컴퓨터 비전 대적 공격의 관련연구 뼈대 |
| P02 | 위협 분류 | Threat Model | 공격자·방어자·보호자산 정의 |
| P03 | 평가 지표 | Evaluation Protocol | 정량 지표와 로그 근거 연결 |
| P04 | 공격·방어 사례 | Security Implication | 보안적 함의와 방어 한계 |
| P05 | 재현성·정책 근거 | Limitation | 확인 필요 항목과 제출 전 검증 |

---

## Limitation

- 대적 교란은 toy evaluation 범위로 설명하며 실제 시스템 우회 절차로 쓰지 않는다.
- 원문 DOI/URL과 formal guarantee는 최종 제출 전 확인 필요.
- 실제 운영 시스템 악용 절차나 무단 API 질의 절차는 포함하지 않음.

---

## Final Takeaway

W03의 핵심은 `accuracy, attack_success_rate, robust_drop`를 성능·보안·재현성 근거로 분리해 기말논문의 평가방법에 연결하는 것이다.
