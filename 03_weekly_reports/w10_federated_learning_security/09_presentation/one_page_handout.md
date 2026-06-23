# W10 1페이지 배포자료

## 핵심 메시지

연합학습은 raw data를 중앙으로 모으지 않지만, model update와 aggregation 단계에서 privacy·integrity 위험이 남는다. 따라서 FL 보안 평가는 clean accuracy, ASR, privacy leakage, aggregation rule, 재현성 로그를 함께 봐야 한다.

## 논문 패킷 역할

| 논문 | 역할 |
|---|---|
| P01 | FL aggregation taxonomy |
| P02 | FL security/privacy threat survey |
| P03 | attack-defense taxonomy |
| P04 | privacy attack, defense, policy |
| P05 | FL backdoor와 ASR 평가 |

## 실험 결과

| 조건 | Accuracy | F1 | ASR | Privacy Proxy |
|---|---:|---:|---:|---:|
| Clean FL | 0.960000 | 0.958042 | 0.136076 | 0.442597 |
| Poisoned FL 10% | 0.953333 | 0.951557 | 0.297468 | 0.428377 |
| Poisoned FL 20% | 0.950000 | 0.948630 | 0.496835 | 0.486591 |
| Robust aggregation 20% | 0.955000 | 0.953368 | 0.237342 | 0.439875 |

## 해석

- 20% poisoned FedAvg는 clean accuracy가 0.950000으로 비교적 높지만 ASR은 0.496835다.
- Coordinate median은 같은 20% 조건에서 ASR을 0.237342로 낮췄다.
- Robust aggregation은 유용하지만 단독 충분조건은 아니다.
- Privacy Leakage Proxy는 실제 privacy attack 성공률이 아니라 update 노출 위험 대용 지표다.

## 기말논문 연결

W10는 utility, attack success, privacy exposure, reproducibility를 함께 기록하는 AI 보안 평가표의 근거가 된다.

<!-- formula-visual-handout:start -->
## 수식·그래프·그림 보강 요약

| 항목 | 반영 내용 |
|---|---|
| 핵심 수식 | FedAvg Aggregation과 Client Update, Update Norm Leakage/Poisoning Proxy |
| 그래프 | `assets/charts/w10_metrics_chart.png` (`metrics_summary.csv` 기반) |
| 다이어그램 | `assets/diagrams/w10_pipeline_diagram.svg` (FL aggregation structure) |
| 기호 정의 | 통합보고서와 발표 슬라이드의 수식 블록에 포함 |
| 주의사항 | privacy_leakage_proxy는 실제 gradient inversion 성공률이 아니며 proxy로만 해석한다. |
<!-- formula-visual-handout:end -->
