# 보안 이슈 30% 정리

W02의 보안 이슈는 데이터 오염, 훈련데이터 조작, poisoning, backdoor이다. 핵심은 공격 절차를 자세히 재현하는 것이 아니라, 어떤 자산이 보호 대상이고 어떤 평가 지표로 위험을 확인할지 명확히 하는 것이다.

## 1. 주요 보안 이슈

| 이슈 | 설명 | 대표 평가 |
|---|---|---|
| Data poisoning | 학습 데이터 일부를 조작해 모델 학습 결과를 바꾸는 공격 | 오염률별 accuracy drop |
| Label-flipping poisoning | 학습 라벨을 다른 클래스로 바꾸는 단순하지만 강력한 오염 | clean accuracy, macro F1 |
| Clean-label poisoning | 라벨은 유지하면서 입력 특징을 조작하는 공격 | 탐지 난이도, stealthiness |
| Backdoor attack | trigger가 있을 때만 공격자 목표로 오분류되는 조건부 공격 | ASR, clean accuracy 유지율 |
| Training data manipulation | 수집, 라벨링, 증강, 필터링 단계에서 데이터가 오염되는 문제 | provenance, 검수 로그 |
| Defense and detection | 데이터 정제, anomaly detection, robust training, pruning, retraining | detection rate, false positive, cost |

## 2. CIA 관점 분석

| 관점 | 관련 위협 | 설명 |
|---|---|---|
| Confidentiality | Poisoned data source leakage | 오염 데이터의 출처나 민감 정보가 분석 과정에서 노출될 수 있음 |
| Integrity | Data poisoning / Backdoor | 모델의 학습 결과와 예측 무결성이 조작됨 |
| Availability | Model degradation | 오염 데이터로 전체 성능이 저하되어 서비스 품질이 하락함 |
| Privacy | Training data inference | 오염 탐지 과정에서 데이터 구성원이 드러날 위험 |
| Safety | Trigger-based misclassification | 특정 trigger 조건에서 안전하지 않은 예측이 발생 |
| Accountability | Poisoning provenance tracking | 데이터 출처, 라벨러, 학습 로그가 없으면 책임 추적 불가 |

## 3. Clean Accuracy와 ASR의 차이

Clean accuracy는 정상 입력에서 모델이 얼마나 잘 맞는지를 보여준다. ASR은 trigger가 들어간 공격 조건에서 모델이 공격자 목표로 얼마나 자주 오분류되는지를 보여준다. Backdoor 평가에서는 clean accuracy가 높아도 ASR이 높으면 보안적으로 실패한 모델로 보아야 한다.

| 조건 | Clean Accuracy | ASR | 해석 |
|---|---:|---:|---|
| 정상 모델 | 높음 | 낮음 | 정상 동작 |
| 전체 성능 저하형 poisoning | 낮음 | 상황별 | availability/integrity 손상 |
| 은닉형 backdoor | 높음 | 높음 | 정상 성능으로 위협이 가려짐 |
| 강한 방어 후 모델 | 적정 수준 | 낮음 | 유틸리티와 보안성 균형 필요 |

## 4. 공격자 비용모형

| 항목 | 낮은 비용 공격 | 높은 비용 공격 |
|---|---|---|
| 데이터 접근 | 공개 데이터 일부 업로드 | 내부 학습 파이프라인 접근 |
| 라벨 조작 | 소수 라벨 flip | 대규모 clean-label poisoning |
| 모델 지식 | black-box 추정 | white-box gradient 활용 |
| 은닉성 | 단순 오염, 탐지 쉬움 | 정상 성능 유지, 탐지 어려움 |
| 방어 우회 | 기본 검수 통과 | 통계 탐지/재학습까지 고려 |

## 5. 방어 및 탐지 방법

| 방어 위치 | 방법 | 장점 | 한계 |
|---|---|---|---|
| 데이터 수집 전 | 출처 검증, 신뢰도 점수 | 오염 유입 감소 | 비용과 운영 부담 |
| 라벨링 단계 | 다중 라벨러, 라벨 일관성 검사 | label-flip 탐지에 유리 | clean-label 공격에는 제한 |
| 학습 전 | 이상치 탐지, 중복/trigger 검사 | 위험 샘플 사전 제거 | 오탐 가능 |
| 학습 중 | robust training, loss monitoring | 모델 업데이트 이상 감지 | 구현 복잡도 |
| 학습 후 | trigger 테스트, pruning, retraining | backdoor 완화 가능 | 보편적 해결책 아님 |

## 6. W02 안전 범위

본 주차 실습은 공개 digits 데이터 또는 Docker 환경에서 실행되는 toy evaluation만 다룬다. 실제 서비스 침해, 실제 개인정보, 무단 데이터 수집, 악성코드 실행, 운영 시스템 대상 공격은 포함하지 않는다.
