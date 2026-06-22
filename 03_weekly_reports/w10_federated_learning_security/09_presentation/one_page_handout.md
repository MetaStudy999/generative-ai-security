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

| 조건 | Accuracy | ASR |
|---|---:|---:|
| Clean FL | 0.960000 | 0.136076 |
| Poisoned FL 10% | 0.953333 | 0.297468 |
| Poisoned FL 20% | 0.950000 | 0.496835 |
| Robust aggregation 20% | 0.955000 | 0.237342 |

## 해석

- 20% poisoned FedAvg는 clean accuracy가 0.950000으로 비교적 높지만 ASR은 0.496835다.
- Coordinate median은 같은 20% 조건에서 ASR을 0.237342로 낮췄다.
- Robust aggregation은 유용하지만 단독 충분조건은 아니다.
- Privacy Leakage Proxy는 실제 privacy attack 성공률이 아니라 update 노출 위험 대용 지표다.

## 기말논문 연결

W10는 utility, attack success, privacy exposure, reproducibility를 함께 기록하는 AI 보안 평가표의 근거가 된다.
