# W12 1페이지 요약

## 핵심 메시지

AI 모델 안전성 평가는 clean accuracy 하나로 충분하지 않다. 신경망 검증, XAI 설명 안정성, 대적 강건성, 공정성 영향, 검증 비용, 재현성 로그를 함께 보고해야 한다.

## AI 원리 70%

| 개념 | 의미 |
|---|---|
| Neural network verification | 입력 범위에서 모델 출력이 명세를 만족하는지 확인 |
| Abstraction | 복잡한 모델 계산을 검증 가능한 형태로 근사 |
| Robustness certificate | 일정 perturbation 범위에서 예측 안정성을 보증하려는 근거 |
| XAI stability | 입력 변화 전후 설명 결과의 일관성 |

## 보안 이슈 30%

| 이슈 | 평가 지표 |
|---|---|
| Adversarial input | Robust Accuracy |
| Explanation manipulation | Explanation Stability |
| Verification scalability | Verification Cost |
| Trade-off | Accuracy, Certified Rate, Fairness Gap |

## W12 toy 실험 결과

| 조건 | Clean Acc. | Robust Acc. | XAI Stability | Certified |
|---|---:|---:|---:|---:|
| Clean model | 0.818750 | 0.543750 | 0.927782 | 0.543750 |
| Adversarial input | 0.818750 | 0.543750 | 0.862321 | 0.340625 |
| Robust defense | 0.815625 | 0.543750 | 0.927152 | 0.543750 |
| XAI stability check | 0.815625 | 0.696875 | 0.976252 | 0.696875 |

## 주의

이 수치는 synthetic toy classification 결과다. Certified rate는 선형 모델 bound proxy이며 대규모 DNN formal verification 결과가 아니다. 실제 시스템 공격, 운영 모델 침해, 개인정보 기반 평가는 포함하지 않았다.

## 기말논문 연결

W12는 "성능·강건성·설명안정성·공정성·재현성 통합 평가 프레임워크"의 근거 주차로 활용할 수 있다.
