# P01 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 논문 제목 | Optimization Methods for Large-Scale Machine Learning |
| 저자 | Léon Bottou, Frank E. Curtis, Jorge Nocedal |
| 학술지/학회 | SIAM Review |
| 연도 | 2018 |
| DOI/URL | DOI: `10.1137/16M1080173` |
| PDF 파일명 | `01_Bottou_Curtis_Nocedal_2018_Optimization_Methods_Large_Scale_ML.pdf` |
| 검증 상태 | 로컬 PDF와 SIAM 링크 기준으로 서지 확인, 세부 수식은 원문 대조 대상 |

## 2. 한 문장 요약

> 이 논문은 대규모 머신러닝에서 왜 stochastic gradient 계열 최적화가 중심이 되는지를 first-order, noise reduction, second-order 방법의 관점으로 정리하며, 성능과 일반화 및 재현성 평가의 이론적 배경을 제공한다.

## 3. 연구문제

대규모 데이터와 고차원 파라미터를 다루는 머신러닝에서 전통적인 batch optimization만으로는 계산 비용과 확장성을 감당하기 어렵다. 이 논문은 stochastic gradient 방법이 어떤 조건에서 유용하고, 단순 SGD 이후의 noise reduction, second-order approximation, regularized model optimization이 어떤 역할을 하는지를 묻는다.

## 4. 핵심 개념

| 개념 | 설명 | W02 연결 |
|---|---|---|
| Empirical risk minimization | 학습 데이터 평균 손실을 최소화하는 문제 설정 | poisoning은 학습 데이터가 바뀌면 목적함수 자체가 바뀐다는 점을 보여줌 |
| Stochastic gradient | 전체 데이터 대신 일부 샘플 또는 mini-batch로 gradient를 추정 | 대규모 학습의 기본 메커니즘 |
| Noise reduction | stochastic gradient의 분산을 줄여 안정적 수렴을 노리는 기법 | 오염 데이터가 gradient 방향에 주는 영향을 이해하는 배경 |
| Second-order methods | Hessian 또는 근사 곡률 정보를 활용하는 방법 | 계산 비용과 수렴 안정성의 trade-off |
| Generalization | 학습 데이터 밖의 성능 유지 | clean accuracy와 오염 조건 성능을 분리할 필요 |

## 5. 방법론

논문은 최적화 문제 설정, stochastic gradient 분석, noise reduction, second-order 방법, regularized model 방법을 문헌 리뷰와 이론 해설 방식으로 정리한다. 본 보고서에서는 이 논문을 데이터 오염 실험의 직접 공격 문헌이 아니라, 학습 절차와 평가 지표의 원리 배경으로 활용한다.

## 6. 주요 결과

대규모 학습에서는 한 번의 정확한 gradient 계산보다 많은 noisy update를 효율적으로 수행하는 전략이 실용적일 수 있다. 또한 단순 SGD만으로 모든 상황을 설명하기 어렵기 때문에 분산 감소, momentum, quasi-Newton, regularization 등 다양한 방법을 모델 규모와 데이터 조건에 맞춰 선택해야 한다.

## 7. 보안 관점 분석

Poisoning은 최적화 과정의 입력인 학습 데이터와 라벨을 조작한다. 따라서 공격 효과는 단순히 테스트 시점 오분류가 아니라 학습 목적함수, gradient 추정, decision boundary의 이동으로 해석해야 한다. P01은 “왜 작은 데이터 오염이 학습 결과 전체를 바꿀 수 있는가”를 설명하는 원리 문헌으로 쓸 수 있다.

## 8. 한계와 오픈문제

이 논문은 보안 공격 논문이 아니므로 poisoning 공격자의 지식, trigger 설계, 탐지율 같은 보안 지표는 직접 제공하지 않는다. 또한 현대 foundation model 규모의 학습에서는 분산 학습, 데이터 파이프라인, supply chain 위험까지 함께 고려해야 한다.

## 9. 기말 논문에 반영할 부분

기말 논문에서는 P01을 최적화 원리와 평가 재현성의 배경으로 반영한다. 특히 오염률별 accuracy drop, ASR, clean accuracy 유지율을 해석할 때 “학습 데이터 조작이 목적함수와 gradient를 바꾼다”는 설명을 이론적 연결부로 사용한다.
