# W07 LLM 보안과 프라이버시

Research Question: LLM 보안과 프라이버시에서 성능 지표와 보안 지표를 어떻게 분리해 평가할 수 있는가?

---

## Core Formula

### Language Modeling Objective와 Perplexity

$$
\mathcal{L}_{LM}=-\sum_{t=1}^{T}\log p_\theta(x_t|x_{<t}),
\qquad
PPL=\exp\left(\frac{1}{T}\mathcal{L}_{LM}\right)
$$

| 기호 | 의미 |
|---|---|
| `x_t` | t번째 토큰 |
| `x_{<t}` | 이전 토큰 문맥 |
| `p_\theta` | 언어모델 확률 |
| `PPL` | perplexity |

- 직관적 의미: 언어모델은 이전 문맥을 보고 다음 토큰 확률을 높이는 방향으로 학습된다. Perplexity는 언어모델링 품질을 보는 표준 지표다.
- 보안적 의미: 보안 평가에서는 품질 지표와 privacy leakage, unsafe completion을 분리해야 한다.
- 평가 지표 연결: utility, answer_rate, privacy_leakage_rate, code_vulnerability_rate와 연결한다.
- 한계: 실습 수치는 toy prompt set 기준 proxy이며 실제 서비스 위험률이 아니다.

---

## Threat Model

- Diagram: LLM privacy/safety evaluation flow
- Stages: Prompt, LM, Safety Policy, Leakage Audit, Report
- 안전 범위: public, synthetic, toy, local evaluation

![W07 pipeline diagram](assets/diagrams/w07_pipeline_diagram.svg)

---

## Evaluation Protocol

- Metrics: utility, attack_success_rate, privacy_leakage_rate, code_vulnerability_rate
- 데이터 출처: `04_experiment/outputs/metrics_summary.csv`

| condition | utility | attack_success_rate | privacy_leakage_rate | code_vulnerability_rate | notes |
| --- | --- | --- | --- | --- | --- |
| Clean prompts | 0.867 | 0 | 0 | 0 | 정상 질의에서 유용성과 과차단 여부를 확인 |
| Prompt attack simulation | 0.401 | 0.15 | 0 | 0 | 공격 절차 재현 없이 방어 평가용 추상 카테고리만 사용 |
| Privacy-risk prompts | 0.393 | 0.1 | 0.025 | 0 | 실제 개인정보 없이 민감정보 노출 평가 구조만 점검 |
| Code security prompts | 0.678 | 0 | 0 | 0.2 | 취약 코드 생성을 직접 제시하지 않고 체크리스트 판정만 모의 |

---

## Figure-first Result

![W07 metrics chart](assets/charts/w07_metrics_chart.svg)

그래프는 LLM 평가의 utility, attack_success_rate, privacy_leakage_rate, code_vulnerability_rate를 비교한다. 유용성 향상과 안전성 저하가 동시에 나타날 수 있으므로 refusal quality와 leakage를 분리해서 해석해야 한다. 수치는 기존 output CSV 기반이다.

---

## Paper Map

| ID | 논문 역할 | 발표에서 쓰는 위치 | 기말논문 연결 |
|---|---|---|---|
| P01 | 핵심 이론 | Background / Core Formula | LLM 보안과 프라이버시의 관련연구 뼈대 |
| P02 | 위협 분류 | Threat Model | 공격자·방어자·보호자산 정의 |
| P03 | 평가 지표 | Evaluation Protocol | 정량 지표와 로그 근거 연결 |
| P04 | 공격·방어 사례 | Security Implication | 보안적 함의와 방어 한계 |
| P05 | 재현성·정책 근거 | Limitation | 확인 필요 항목과 제출 전 검증 |

---

## Limitation

- privacy leakage는 toy/proxy metric이며 실제 개인정보 추출 실험으로 해석하지 않는다.
- 원문 DOI/URL과 formal guarantee는 최종 제출 전 확인 필요.
- 실제 운영 시스템 악용 절차나 무단 API 질의 절차는 포함하지 않음.

---

## Final Takeaway

W07의 핵심은 `utility, attack_success_rate, privacy_leakage_rate, code_vulnerability_rate`를 성능·보안·재현성 근거로 분리해 기말논문의 평가방법에 연결하는 것이다.
