# 보안 이슈 30% 정리

## 1. 주요 보안 이슈

W10의 보안 이슈는 FL의 client-server-aggregation 구조에서 발생한다. 데이터가 중앙 서버로 이동하지 않아도 local update, global model, aggregation log는 여전히 공격과 추론의 대상이다.

- Gradient leakage: local update나 gradient에서 학습 데이터의 단서를 추론하는 위험
- Membership inference in FL: 특정 데이터가 client 학습에 사용됐는지 추론하는 위험
- Poisoning attack: 악성 client가 학습 데이터를 오염시키거나 update를 조작하는 위험
- Model poisoning: global model parameter를 의도적으로 왜곡하는 위험
- Backdoor attack in FL: 특정 trigger 조건에서만 global model이 목표 오동작을 하도록 만드는 위험
- Malicious client: 정상 참여자인 척 update를 제출하는 내부 공격자
- Byzantine client: 임의적·비정상 update를 제출해 학습을 불안정하게 만드는 client
- Secure aggregation: privacy 보호에는 유리하지만 update 검증과 충돌할 수 있는 방어
- Robust aggregation defense: 이상 update 영향을 줄이는 집계 기반 방어
- FL privacy policy landscape: 기술적 방어와 함께 책임성, 동의, 로그, 정책 준수가 필요한 영역

## 2. CIA 관점 분석

| 관점 | 관련 위협 | 설명 |
|---|---|---|
| Confidentiality | Gradient leakage, update inspection | 개별 client update가 local data 단서를 노출할 수 있다. |
| Integrity | Model poisoning, backdoor | 악성 update가 global model의 일반 성능 또는 특정 입력 행동을 바꿀 수 있다. |
| Availability | Byzantine client, communication bottleneck | 비정상 update나 통신 비용이 학습 라운드를 방해할 수 있다. |
| Privacy | Membership inference, privacy attack | 데이터 비공유 구조라도 학습 참여 여부와 민감 속성 노출 위험이 남는다. |
| Safety | Compromised global model behavior | clean 성능은 높아도 특정 trigger 조건에서 위험 행동이 나타날 수 있다. |
| Accountability | Malicious client attribution failure | secure aggregation과 privacy 보호가 강할수록 악성 client 식별은 어려워질 수 있다. |

## 3. 공격-방어-평가 분류

| 구분 | 내용 |
|---|---|
| 공격 자산 | local data, local update, global model, aggregation result, training log |
| 공격자 능력 | malicious client 참여, local label/backdoor 오염, update scaling, repeated participation |
| 방어 방법 | robust aggregation, update norm monitoring, client sampling, secure aggregation, DP, audit log |
| 평가 지표 | global accuracy, global F1, ASR, privacy leakage proxy, update norm, communication bytes |

## 4. W10 실험 해석

20% poisoned FedAvg는 clean accuracy 0.950000을 유지하면서 ASR 0.496835를 보였다. 이는 backdoor류 위협이 "일반 성능 저하"만으로 탐지되지 않을 수 있음을 보여준다. coordinate median은 같은 20% 조건에서 ASR 0.237342로 낮아졌지만 완전히 제거하지는 못했다. 따라서 robust aggregation은 필요하지만 단독 충분조건은 아니다.

## 5. 기말 논문 연결

이 보안 이슈는 기말 논문에서 "분산 AI 학습의 보안 평가는 utility, privacy, robustness, reproducibility를 함께 기록해야 한다"는 논지로 연결된다. 특히 FL은 privacy-preserving이라는 이름과 달리 update 수준의 privacy·integrity 평가가 별도로 필요하다.
