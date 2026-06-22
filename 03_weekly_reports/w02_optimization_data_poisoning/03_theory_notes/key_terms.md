# 핵심 용어

| 용어 | 정의 | W02에서의 의미 |
|---|---|---|
| Large-scale optimization | 대규모 데이터와 파라미터에서 손실함수를 최소화하는 절차 | 모델 학습의 기본 원리 |
| Empirical risk | 학습 데이터 평균 손실 | 데이터가 오염되면 최적화 대상 자체가 바뀜 |
| Stochastic gradient | 일부 샘플로 계산한 gradient 추정치 | mini-batch에 오염 샘플이 들어가면 업데이트가 왜곡될 수 있음 |
| Generalization | 학습 데이터 밖에서 성능이 유지되는 성질 | clean test 성능과 공격 조건 성능을 분리해야 함 |
| Model compression | 모델 크기와 연산량을 줄이는 기법 | 방어 비용과 backdoor 제거 가능성에 영향 |
| Data poisoning | 학습 데이터를 조작해 모델을 오염시키는 공격 | W02 핵심 보안 위협 |
| Label flipping | 라벨을 다른 클래스로 바꾸는 poisoning | 안전한 toy 실습에서 구현 가능한 범위 |
| Backdoor | 특정 trigger에서만 공격자 목표 행동을 하는 은닉 공격 | clean accuracy와 ASR 동시 평가 필요 |
| Attack Success Rate | trigger 조건에서 목표 오분류가 발생한 비율 | backdoor 핵심 지표 |
| Stealthiness | 공격이 정상 검증에서 드러나지 않는 정도 | clean accuracy 유지율로 근사 가능 |
| Detection rate | 오염 또는 backdoor를 찾아내는 비율 | 방어 평가 지표 |
| Provenance | 데이터 출처와 처리 이력 | accountability와 재현성의 핵심 |
