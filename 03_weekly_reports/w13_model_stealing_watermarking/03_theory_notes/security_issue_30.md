# 보안 이슈 30% 정리

## 1. 주요 보안 이슈

W13의 보안 이슈는 모델 추출을 통한 지식재산 침해와, 그 이후 소유권을 입증하기 위한 watermarking/fingerprinting의 신뢰성이다. 공격 절차를 재현하는 것이 목표가 아니라, 공격자 능력과 방어 지표를 안전하게 평가표로 바꾸는 것이 목표다.

- Model stealing
- Model extraction
- API query abuse
- Substitute model training
- Watermark removal
- Watermark forgery
- Fingerprint collision
- Utility degradation
- False positive / false negative in watermark detection
- 생성모형 출력의 추적성과 오용 가능성

## 2. CIA 관점 분석

| 관점 | 관련 위협 | 설명 |
|---|---|---|
| Confidentiality | Model parameter / behavior leakage | 출력만 공개해도 모델 행동과 결정경계가 유출될 수 있다. |
| Integrity | Watermark removal / watermark forgery | 소유권 신호가 제거되거나 위조되면 검증 체계가 흔들린다. |
| Availability | Query abuse / API cost exhaustion | 반복 질의는 모델 추출뿐 아니라 비용 고갈과 서비스 부담을 만든다. |
| Privacy | Training data inference through stolen model | 도난 모델이 원 학습 데이터의 민감 패턴을 간접 노출할 수 있다. |
| Safety | Misuse of stolen generative model | 생성모형이 복제되면 오용과 책임 추적 실패가 커진다. |
| Accountability | Ownership verification failure | false positive/false negative가 높으면 소유권 주장의 신뢰도가 낮다. |

## 3. 공격-방어-평가 분류

| 구분 | 내용 |
|---|---|
| 공격 자산 | 모델 파라미터, 출력 행동, 학습된 결정경계, 워터마크, 생성물 |
| 공격자 능력 | 반복 질의, query-response 수집, 대체 모델 학습, 워터마크 제거·희석 시도 |
| 방어 방법 | query limit, 로그 감사, watermarking, fingerprinting, 이상 질의 탐지 |
| 평가 지표 | extraction fidelity, query cost, substitute accuracy, watermark detection, false positive, utility loss |
| 제외 범위 | 실제 상용 API 대상 질의, 무단 대량 수집, 실제 모델 탈취 절차 |

## 4. W13 toy 실험 해석

| 조건 | Query Budget | Extraction Fidelity | Watermark Detection | False Positive Proxy |
|---|---:|---:|---:|---:|
| Substitute query 100 | 100 | 0.864000 | 0.700000 | 0.600000 |
| Substitute query 500 | 500 | 0.920000 | 1.000000 | 0.600000 |
| Substitute query 1000 | 1000 | 0.902000 | 1.000000 | 0.600000 |

실험은 synthetic toy 데이터만 사용했다. watermark detection은 높아졌지만 false positive proxy도 높으므로, 이 trigger-set 설계는 소유권 검증의 필요성과 동시에 한계를 보여주는 예시로 해석한다.

## 5. 기말 논문 연결

W13의 기여 후보는 “모델 IP 보호 평가에서 fidelity와 detection만 보고하지 말고 false positive, utility loss, reproducibility를 함께 보고해야 한다”는 평가 프레임워크다.
