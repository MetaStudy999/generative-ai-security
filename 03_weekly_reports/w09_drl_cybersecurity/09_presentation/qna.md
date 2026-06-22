# W09 예상 Q&A

## Q1. 왜 deep neural network 기반 DRL이 아니라 tabular Q-learning을 사용했나?

목적이 고성능 DRL 모델 개발이 아니라 reward manipulation의 효과를 안전하고 재현 가능하게 보여주는 것이기 때문이다. tabular Q-learning은 상태·행동·보상 관계가 투명해 발표와 보고서에서 설명하기 쉽다.

## Q2. Robust reward design이 Average Reward는 normal reward보다 낮은데 더 안전하다고 볼 수 있나?

더 안전하다고 볼 수 있는 축이 있다. Safety Violation Rate가 0.000000으로 낮아졌기 때문이다. 다만 false positive 비용 때문에 Detection F1과 Average Reward가 일부 낮아져 utility-safety trade-off가 생긴다.

## Q3. Manipulated reward에서 observed reward와 true reward를 왜 나눴나?

공격자 또는 잘못된 설계가 학습 reward를 왜곡하면 agent가 보는 점수와 실제 보안 목표가 달라질 수 있다. 이 차이를 보려면 학습에 쓰인 observed reward와 평가용 true reward를 분리해야 한다.

## Q4. 실제 네트워크 보안 시스템에 바로 적용할 수 있나?

아니다. 본 실험은 synthetic toy simulation이다. 실제 적용 전에는 공개 benchmark, 익명화된 운영 로그, 정책 검증, human override 설계를 추가해야 한다.

## Q5. 기말논문에는 어떤 부분을 가져가면 좋은가?

reward integrity 위협모형, Detection F1/Safety Violation/Policy Robustness 평가표, seed/config/output 기반 재현성 패키지를 가져가면 좋다.
