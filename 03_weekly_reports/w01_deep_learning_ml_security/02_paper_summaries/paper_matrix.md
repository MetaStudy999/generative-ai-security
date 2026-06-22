# W01 논문 5편 비교표

| 논문 | 연구문제 | 핵심 방법 | 데이터/실험 | 보안 위협 | 평가 지표 | 한계 | 내 논문 활용 |
|---|---|---|---|---|---|---|---|
| P01 | 딥러닝이 어떻게 계층적 표현을 학습하는가 | 다층 신경망, 역전파, CNN/RNN 사례 정리 | 리뷰 논문, 분야별 사례 중심 | 직접 보안 논문은 아니나 gradient·표현 취약성의 배경 | 일반화 성능, 표현 품질 | 보안 위협모형 부재 | AI 원리와 모델 취약성 설명 |
| P02 | ML 시스템 안전성을 어떤 생명주기 증거로 보증할 것인가 | lifecycle 단계화, desiderata, 보증 방법 분류 | 문헌조사 | 데이터/모델/배포 단계의 보증 실패 | traceability, verification evidence, lifecycle coverage | 공격별 정량 프로토콜은 별도 필요 | 위협모형과 재현성 프레임 |
| P03 | 침입탐지에 어떤 ML/데이터마이닝 방법이 적합한가 | 알고리즘·데이터·평가지표 survey | IDS 공개 데이터와 선행 연구 비교 | 오탐, 미탐, 데이터 drift, 라벨 품질 | detection rate, false alarm rate, precision/recall/F1 | 공개 데이터셋과 실제망 격차 | 보안 평가 지표 설계 |
| P04 | 대적 공격과 방어를 어떻게 분류하고 검증할 것인가 | attack/defense taxonomy, 방어 한계 분석 | survey 및 문헌 기반 비교 | evasion, physical attack, gradient masking, transfer attack | attack success rate, robust accuracy, clean accuracy | arXiv 대체 논문 기준. 강의계획서 지정 IEEE COMST 논문 동일 여부 확인 필요 | adversarial robustness 장 |
| P05 | ML 프라이버시 공격은 어떤 지식과 자산을 노리는가 | privacy attack taxonomy, threat model, defense survey | 40편 이상 문헌 분석 | membership inference, model inversion, property inference | leakage risk, attack advantage, utility/privacy trade-off | 단일 지표로 privacy risk 요약 어려움 | privacy leakage 평가축 |

## 종합 비교

### 1. 공통적으로 다루는 문제

다섯 편은 모두 “모델 성능만으로 ML 시스템의 신뢰성을 설명할 수 없다”는 결론으로 모인다. P01은 성능이 나오는 AI 원리를 제공하고, P02는 그 모델이 시스템 안에서 안전하게 운영되려면 어떤 생명주기 증거가 필요한지 보여준다. P03-P05는 보안 영역에서 성능, 무결성, 기밀성 평가가 어떻게 달라지는지 구체화한다.

### 2. 논문 간 차이점

P01은 원리 중심, P02는 프로세스 중심, P03은 보안 탐지 응용 중심, P04는 무결성 공격 중심, P05는 기밀성 공격 중심이다. 따라서 W01 보고서에서는 이들을 하나의 선형 서사로 읽기보다 “원리-생명주기-탐지-대적공격-프라이버시”의 다섯 축으로 배치한다.

### 3. 아직 해결되지 않은 문제

1. Clean accuracy와 security robustness를 동시에 만족시키는 평가 설계가 어렵다.
2. 공개 데이터셋 기반 결과가 실제 운영 환경으로 얼마나 일반화되는지 불확실하다.
3. Privacy defense는 유틸리티 손실과 보호 수준 사이의 trade-off를 낳는다.
4. Survey taxonomy를 실제 재현 실험으로 연결하려면 최소한의 안전한 toy protocol이 필요하다.
5. P04는 현재 arXiv 논문 기준이므로 강의계획서 지정 IEEE Communications Surveys & Tutorials 논문과 동일 여부를 확인해야 한다.

### 4. 기말 논문 주제로 발전 가능한 연결부

W01의 기말논문 연결부는 “ML 생명주기 기반 AI 보안 평가 프레임워크”이다. 각 주차의 공격/방어 문헌을 데이터 관리, 모델 학습, 모델 검증, 배포·운영 단계에 매핑하고, 성능·강건성·프라이버시·재현성을 함께 평가하는 체크리스트로 발전시킬 수 있다.
