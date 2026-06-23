# W02 발표자 노트

## 발표 개요

- 권장 시간: 8-10분
- 발표 톤: AI 원리 70%, 보안 이슈 30%
- 핵심 문장: “데이터 오염은 입력 하나의 문제가 아니라 학습 목적함수와 gradient를 바꾸는 훈련 단계 위협입니다.”

## Slide 1. 제목

오늘 발표는 2주차 주제인 대규모 최적화와 데이터 오염 위협입니다. 핵심은 모델 학습을 최적화 문제로 이해하고, 그 최적화가 데이터와 라벨에 얼마나 의존하는지를 보는 것입니다. 이 관점에서 poisoning과 backdoor를 clean accuracy와 ASR로 분리해 설명하겠습니다.

## Slide 2. 왜 W02가 중요한가

1주차가 ML 보안 평가의 공통 언어였다면, 2주차는 학습 단계 위협을 다룹니다. 모델은 학습 데이터로부터 gradient를 얻고, 이 gradient를 반복적으로 적용해 파라미터를 바꿉니다. 그래서 데이터 일부가 잘못되거나 악의적으로 설계되면 모델이 배우는 기준 자체가 바뀔 수 있습니다.

## Slide 3. 발표 로드맵

발표는 여섯 부분으로 진행하겠습니다. 먼저 대규모 최적화와 효율적 학습을 설명하고, 이어서 데이터 오염과 backdoor를 정리합니다. 그 다음 논문 5편이 어떤 역할을 하는지 보여드리고, 마지막으로 위협모형, 평가방법, 실습 설계, 기말논문 연결로 마무리합니다.

## Slide 4. AI 원리 70%: 최적화

대규모 머신러닝은 손실함수를 최소화하는 파라미터를 찾는 문제입니다. 전체 데이터의 gradient를 매번 계산하는 것은 비용이 크기 때문에, 실제 학습에서는 SGD와 mini-batch 학습이 많이 사용됩니다. 중요한 점은 데이터가 오염되면 이 gradient 추정도 바뀐다는 것입니다. 그래서 poisoning은 테스트 시점 입력 공격이 아니라 학습 목적함수를 바꾸는 공격으로 볼 수 있습니다.

## Slide 5. AI 원리 70%: 효율성

효율적 딥러닝은 모델 압축, 경량화, 빠른 학습, 낮은 latency 같은 비용 지표를 함께 다룹니다. 보안 관점에서는 이 효율성이 방어 평가와 연결됩니다. 방어 기법이 아무리 좋아도 학습 비용이나 탐지 지연이 너무 크면 실제 운영 환경에 적용하기 어렵습니다.

## Slide 6. 보안 이슈 30%

W02의 보안 이슈는 label-flipping, data poisoning, backdoor, provenance failure입니다. Label-flipping은 라벨을 바꾸는 비교적 단순한 오염이고, backdoor는 정상 입력에서는 잘 동작하다가 trigger 조건에서만 공격자 목표로 오분류되는 공격입니다. 그래서 정상 성능만 보면 위험을 놓칠 수 있습니다.

## Slide 7. Clean Accuracy와 ASR

Backdoor 평가에서 가장 중요한 구분은 clean accuracy와 ASR입니다. Clean accuracy는 정상 테스트셋 성능이고, ASR은 trigger 입력에서 공격자 목표로 예측되는 비율입니다. 은닉형 backdoor는 clean accuracy가 높으면서 ASR도 높은 조건이므로 가장 조심해야 합니다.

## Slide 8. 논문 5편의 역할

P01은 최적화, P02는 효율적 딥러닝, P03은 poisoning taxonomy, P04는 training data poisoning threat model, P05는 backdoor survey입니다. 이 다섯 편을 연결하면, 학습 원리와 보안 위협을 따로 읽는 것이 아니라 “데이터가 학습을 어떻게 움직이고, 공격자가 그 데이터를 어떻게 흔드는가”로 볼 수 있습니다.

## Slide 9. 위협모형

위협은 데이터 수집, 라벨링, 전처리, 학습, 검증 단계에서 발생할 수 있습니다. 보호 자산은 데이터, 라벨, 모델 파라미터, 검증셋, 로그입니다. 공격자는 데이터 제공자나 악의적 라벨러, 내부 접근자로 볼 수 있습니다. 성공 조건은 전체 성능 저하 또는 trigger 조건부 목표 오분류입니다.

## Slide 10. 평가 프로토콜

평가 프로토콜은 clean performance, poisoning impact, backdoor effect, stealthiness, reproducibility, efficiency를 나누어 기록합니다. 단일 accuracy 표로는 poisoning과 backdoor를 설명하기 어렵습니다. 특히 재현성을 위해 seed, config, Docker, outputs 로그를 같이 남겨야 합니다.

## Slide 11. 실습 설계

실습은 scikit-learn digits 공개 데이터셋을 사용했습니다. clean baseline, label flip 5%, 10%, 20%, 안전한 toy backdoor 5% 조건을 비교했고, Docker 실행으로 CSV, JSON, Markdown 로그를 생성했습니다.

## Slide 12. 결과 기록 방식

이 슬라이드는 실제 실행 결과를 보여줍니다. clean baseline accuracy는 0.981481, macro F1은 0.981443입니다. label-flip 오염률이 5%, 10%, 20%로 증가할수록 accuracy는 0.918519, 0.877778, 0.818519로 낮아졌고 macro F1은 0.918457, 0.877582, 0.818134로 낮아졌습니다. 안전한 toy backdoor 조건은 clean accuracy 0.970370, macro F1 0.970359를 유지하면서 ASR 0.987654를 보였습니다.

## Slide 13. 한계와 기말논문 연결

Digits toy experiment는 실제 대규모 모델을 대표하지 않습니다. Label-flip도 clean-label poisoning이나 공급망 공격의 은닉성을 충분히 설명하지 못합니다. 하지만 평가 지표를 분리하고 재현성 패키지를 만드는 훈련으로는 적합합니다. 기말논문은 학습 데이터 오염과 backdoor 평가를 위한 다중지표 프레임워크로 발전시키는 것이 좋습니다.

## Slide 14. 결론

마지막 결론입니다. 최적화는 데이터로 움직이고, 데이터 오염은 그 최적화 경로를 바꿉니다. Backdoor 평가는 clean accuracy와 ASR을 분리해야 하며, 안전한 실습은 Docker, config, seed, outputs를 남겨야 합니다. W02는 실습 코드, 실행 결과, 제출 문서까지 정리된 상태입니다.

<!-- formula-visual-speaker-notes:start -->
## 수식·그래프·그림 발표자 노트

- 핵심 수식: ERM, Poisoned Empirical Risk, SGD Update, Accuracy Drop와 ASR. 수식은 표준 정의식이며, 원문 위치나 formal guarantee가 확인되지 않은 부분은 확인 필요로 말한다.
- 기호 정의표는 청중이 식을 해석할 수 있도록 먼저 읽고, 이후 보안 지표와 연결한다.
- 그래프 설명: 그래프는 `metrics_summary.csv`의 clean accuracy, macro F1, ASR을 조건별로 그린 것이다. Label-flip 조건에서는 오염률 증가와 함께 clean 성능 저하를 비교할 수 있고, toy backdoor 조건은 clean 성능과 ASR을 분리해 보아야 함을 보여준다. 표에 없는 실험 조건이나 수치는 추가하지 않았다.
- 다이어그램 설명: `training-data poisoning evaluation flow`는 threat model 또는 평가 pipeline을 한 장으로 보여주는 보조 그림이다.
- 한계 고지: toy backdoor는 공개 toy 데이터 기반 안전 실습이며 실제 시스템 악용 절차로 일반화하지 않는다.
<!-- formula-visual-speaker-notes:end -->
