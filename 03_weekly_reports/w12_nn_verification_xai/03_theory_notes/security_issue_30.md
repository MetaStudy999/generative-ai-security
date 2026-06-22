# 보안 이슈 30% 정리

## 1. 주요 보안 이슈

W12의 보안 이슈는 대적 입력에 의한 prediction integrity 훼손, XAI 설명 조작에 의한 accountability 훼손, 검증 비용 증가에 따른 availability 문제, robustness-accuracy-fairness trade-off 은폐 위험이다.

## 2. CIA+Safety 관점 분석

| 관점 | 관련 위협 | 설명 | W12 지표 |
|---|---|---|---|
| Confidentiality | explanation leakage | 설명이 민감 feature 의존성을 드러낼 수 있다 | human review, disclosure |
| Integrity | adversarial input | 작은 입력 변화가 예측을 바꿀 수 있다 | robust accuracy |
| Availability | verification scalability failure | 검증 비용이 커지면 검증이 생략될 수 있다 | verification cost |
| Safety | unverified robustness claim | empirical robustness를 formal guarantee처럼 과장할 수 있다 | certified rate proxy 경고 |
| Accountability | explanation manipulation | 예측은 유지되지만 설명이 바뀌어 검토자를 오도할 수 있다 | explanation stability |
| Fairness | robustness-fairness trade-off | 방어가 집단별 성능 차이를 키울 수 있다 | fairness gap |

## 3. 공격-방어-평가 분류

| 구분 | W12 정리 |
|---|---|
| 보호 자산 | model prediction, robustness certificate, explanation output, fairness metric, verification log |
| 공격자 능력 | input perturbation, explanation manipulation, evaluation setting manipulation |
| 공격 성공 조건 | prediction change, explanation change, robustness overclaim, fairness gap increase |
| 방어/점검 | robust training proxy, XAI stability check, bound proxy, fairness-gap reporting |
| 제외 범위 | 실제 안전중요 시스템 공격, 운영 모델 침해, 개인정보 기반 평가, 무단 probing |

## 4. 악용 방지 범위

본 보고서는 공격 절차를 재현 가능한 단계별 지침으로 제공하지 않는다. `Adversarial input` 조건은 실제 공격 코드가 아니라 synthetic toy perturbation proxy이며, 실제 운영 모델 침해나 무단 API 질의 실험은 수행하지 않는다.

## 5. 기말 논문 연결

기말논문에서는 W12를 "성능·강건성·설명안정성·공정성·재현성 통합 평가 프레임워크"의 관련연구와 위협모형 근거로 활용한다. 단일 accuracy 중심 주장을 피하고, 각 지표의 한계와 검증 범위를 함께 표시한다.
