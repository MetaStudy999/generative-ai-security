# W12 신경망 검증·XAI·강건성 Trade-off

안전한 AI 평가는 정확도 하나로 끝나지 않는다.

---

## 오늘의 질문

- 모델이 clean test에서 잘 맞으면 충분한가?
- 작은 입력 변화에도 예측과 설명이 안정적인가?
- 검증 비용과 공정성 영향까지 같이 보고했는가?

---

## 문헌 5편의 역할

| 문헌 | 발표 역할 |
|---|---|
| P01 | verification abstraction |
| P02 | adversarial attack/defense |
| P03 | adversarial XAI |
| P04 | Lipschitz robustness |
| P05 | robustness-accuracy-fairness trade-off |

---

## AI 원리 70%

- Neural network verification
- Abstraction and reachability
- Formal robustness certificate
- Lipschitz regularization
- XAI explanation stability

---

## 보안 이슈 30%

- Adversarial input은 예측 무결성을 흔든다.
- Explanation manipulation은 검토자 판단을 흔든다.
- Verification scalability failure는 검증 생략으로 이어진다.
- Robustness, accuracy, fairness는 trade-off를 만들 수 있다.

---

## Toy 실험 설계

| 항목 | 설정 |
|---|---|
| 데이터 | synthetic binary classification |
| 모델 | toy logistic classifier |
| Seed | 42 |
| Perturbation | L-infinity epsilon 0.35 proxy |
| 제외 | 실제 시스템 공격, 개인정보 |

---

## 실험 결과

| 조건 | Clean Acc. | Robust Acc. | XAI Stability | Certified |
|---|---:|---:|---:|---:|
| Clean model | 0.818750 | 0.543750 | 0.927782 | 0.543750 |
| Adversarial input | 0.818750 | 0.543750 | 0.862321 | 0.340625 |
| Robust defense | 0.815625 | 0.543750 | 0.927152 | 0.543750 |
| XAI stability check | 0.815625 | 0.696875 | 0.976252 | 0.696875 |

---

## 해석

Clean accuracy가 높아도 robust accuracy는 낮아질 수 있다.

Certified rate와 explanation stability는 보증의 일부만 보여준다.

---

## 기말논문 연결

- 성능·강건성·설명안정성·공정성·재현성 통합 평가표
- 위협모형과 평가 프로토콜의 연결
- 실행 로그 기반 연구윤리와 재현성 관리

---

## 결론

W12의 핵심은 "정확도 중심 보고"에서 "보증 가능한 다중지표 보고"로 관점을 바꾸는 것이다.
