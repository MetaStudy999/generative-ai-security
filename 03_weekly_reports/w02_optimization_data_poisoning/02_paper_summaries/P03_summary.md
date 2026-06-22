# P03 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 논문 제목 | A Comprehensive Survey on Poisoning Attacks and Countermeasures in Machine Learning |
| 저자 | Zhiyi Tian et al. |
| 학술지/학회 | ACM Computing Surveys |
| 연도 | 2022/2023 |
| DOI/URL | DOI: `10.1145/3551636` |
| PDF 파일명 | `03_Tian_Cui_Liang_Yu_2023_Comprehensive_Poisoning_Survey.pdf` |
| 검증 상태 | 로컬 PDF XMP 메타데이터에서 DOI 확인 |

## 2. 한 문장 요약

> 이 논문은 머신러닝 poisoning 공격과 대응책을 공격 목표, 공격 지식, 오염 위치, 방어 전략으로 분류하며, W02의 위협모형과 평가방법을 구성하는 핵심 보안 문헌이다.

## 3. 연구문제

학습 단계에서 데이터가 조작되면 모델은 정상 검증에서는 그럴듯하게 보이면서도 특정 조건에서 성능이 저하되거나 공격자 의도대로 오분류될 수 있다. 이 논문은 poisoning 공격의 유형, 공격자 능력, 방어 방법, 평가 기준을 체계적으로 묶어 연구 지형을 정리한다.

## 4. 핵심 개념

| 개념 | 설명 | W02 연결 |
|---|---|---|
| Poisoning attack | 학습 데이터 또는 라벨을 조작해 학습 결과를 바꾸는 공격 | W02 보안 이슈의 중심 |
| Availability attack | 전체 성능 저하를 목표로 하는 오염 | accuracy drop 평가 |
| Integrity attack | 특정 입력 또는 클래스에 대한 조건부 오분류 목표 | ASR과 targeted error 평가 |
| Backdoor | trigger가 있을 때만 공격자 목표로 동작하는 은닉 공격 | clean accuracy와 ASR의 괴리 |
| Countermeasure | 데이터 정제, robust training, anomaly detection 등 | 방어 평가 프레임 |

## 5. 방법론

Survey 방식으로 공격 및 방어 문헌을 분류한다. 본 보고서에서는 P03의 taxonomy를 이용해 공격자 지식, 공격자 능력, 오염률, 공격 성공 조건, 방어 관측 가능성을 위협모형 표로 재구성한다.

## 6. 주요 결과

Poisoning은 단일 공격 기법이 아니라 학습 데이터, 라벨, feature, 모델 업데이트, federated setting 등 다양한 위치에서 발생할 수 있는 학습 단계 위협이다. 따라서 방어도 단일 accuracy 확인이 아니라 데이터 검증, 학습 로그, 오염률별 민감도, 탐지율, 재현성 기록을 함께 요구한다.

## 7. 보안 관점 분석

P03은 W02에서 “보안 이슈 30%”를 구성하는 중심 문헌이다. 특히 label-flipping, clean-label poisoning, backdoor, federated poisoning을 구분하면 실습과 기말 연구의 안전 범위를 명확히 할 수 있다. 본 주차 실습은 실제 공격 절차가 아니라 공개 digits 데이터에서 라벨 플립과 단순 trigger를 시뮬레이션하는 범위로 제한한다.

## 8. 한계와 오픈문제

Survey 문헌이므로 특정 실험 환경의 재현 코드를 직접 제공하지 않는다. 또한 공격과 방어가 빠르게 발전하므로 최신 LLM, foundation model, 데이터 공급망 환경에서는 별도 문헌 보강이 필요하다.

## 9. 기말 논문에 반영할 부분

기말 논문에서는 P03을 poisoning taxonomy와 위협모형의 핵심 근거로 쓴다. 연구문제는 “오염률, 공격 유형, 방어 관측 가능성에 따라 clean accuracy와 ASR이 어떻게 달라지는가”로 발전시킬 수 있다.
