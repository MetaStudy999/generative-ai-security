# W10 논문 5편 비교표

| 논문 | 연구문제 | 핵심 방법 | 데이터/실험 | 보안 위협 | 평가 지표 | 한계 | 내 논문 활용 |
|---|---|---|---|---|---|---|---|
| P01 | Federated Learning, aggregation, personalization, robustness의 신뢰성 및 보증 문제 | 문헌조사와 분류체계 정리 | 문헌조사 중심, 세부 실험값 대조 필요 | Gradient leakage | 개념 분류, 위협 범위, 평가축 | 원문 세부 수치 확인 전 | 원리와 보안 보증 사이의 연결 |
| P02 | Gradient leakage, poisoning, backdoor, privacy attack와 관련된 위협 분류 | 문헌조사와 분류체계 정리 | 문헌조사 중심, 세부 실험값 대조 필요 | Gradient leakage | 개념 분류, 위협 범위, 평가축 | 원문 세부 수치 확인 전 | 공격-방어-평가 관점을 연결하는 보안 분석 틀 |
| P03 | Gradient leakage, poisoning, backdoor, privacy attack와 관련된 위협 분류 | 문헌조사와 분류체계 정리 | 문헌조사 중심, 세부 실험값 대조 필요 | Gradient leakage | 개념 분류, 위협 범위, 평가축 | 원문 세부 수치 확인 전 | 공격-방어-평가 관점을 연결하는 보안 분석 틀 |
| P04 | Gradient leakage, poisoning, backdoor, privacy attack와 관련된 위협 분류 | 문헌조사와 분류체계 정리 | 문헌조사 중심, 세부 실험값 대조 필요 | Gradient leakage | 개념 분류, 위협 범위, 평가축 | 원문 세부 수치 확인 전 | 공격-방어-평가 관점을 연결하는 보안 분석 틀 |
| P05 | Gradient leakage, poisoning, backdoor, privacy attack와 관련된 위협 분류 | 문헌조사와 분류체계 정리 | 문헌조사 중심, 세부 실험값 대조 필요 | Gradient leakage | 개념 분류, 위협 범위, 평가축 | 원문 세부 수치 확인 전 | 공격-방어-평가 관점을 연결하는 보안 분석 틀 |

## 종합 비교

### 1. 공통적으로 다루는 문제

다섯 편은 모두 연합학습(FL) 및 FL 위협/방어/정책를 이해하기 위한 핵심 원리, 적용 범위, 평가 기준을 제공한다. AI 원리 측면에서는 연합학습의 기본 구조, Client, server, aggregation의 역할, FedAvg의 기본 원리, Aggregation technique taxonomy가 반복적으로 등장하고, 보안 측면에서는 Gradient leakage, Membership inference in FL, Poisoning attack, Model poisoning가 공통 축으로 묶인다.

### 2. 논문 간 차이점

AI 원리 중심 논문은 모델 구조와 학습/평가 원리를 설명하는 데 강하고, 보안 중심 논문은 공격자 능력, 방어 방법, 실패 조건을 더 직접적으로 다룬다. 따라서 기말 논문에서는 두 축을 분리하지 않고 생명주기 기반 평가표로 통합하는 편이 적절하다.

### 3. 아직 해결되지 않은 문제

원문별 데이터셋, 실험 설정, DOI/URL 검증이 남아 있다. 또한 survey 문헌의 분류체계가 실제 재현 실험과 어떻게 연결되는지는 별도 프로토콜로 보완해야 한다.

### 4. 기말 논문 주제로 발전 가능한 연결부

W10는 연합학습(FL) 및 FL 위협/방어/정책를 대상으로 한 위협모형, 평가방법, 재현성 체크리스트를 만들기 위한 기반 주차로 활용할 수 있다.
