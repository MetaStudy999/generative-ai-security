# 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 논문 제목 | I Know What You Trained Last Summer: A Survey on Stealing Machine Learning Models and Defences |
| 저자 | Daryna Oliynyk, Rudolf Mayer, Andreas Rauber |
| 학술지/학회 | ACM Computing Surveys |
| 연도 | 2023 |
| DOI/URL | PDF 표기 DOI: 10.1145/3595292, 공식 페이지 최종 대조 필요 |
| PDF 파일명 | 01_Oliynyk_Mayer_Rauber_2023_Model_Stealing_Survey.pdf |
| 검증 상태 | 로컬 PDF 제목/초록 확인, 세부 표와 수치는 원문 대조 필요 |

## 2. 한 문장 요약

> 이 논문은 MLaaS 환경의 모델 도난과 모델 추출 공격을 공격 목표, 공격 방법, 대상 모델, 방어 전략별로 체계화하며, query-response 기반 평가에서 fidelity, query cost, 방어 우회 가능성을 함께 보아야 함을 제시한다.

## 3. 연구문제

공개 API 또는 black-box 접근만으로도 모델 행동, 파라미터, 하이퍼파라미터, 결정경계가 어느 정도 복제될 수 있는가를 묻는다. 또한 공격을 탐지하거나 예방하는 방어가 어떤 공격 목표와 자원 조건에서 효과가 약해지는지 분류한다.

## 4. 핵심 개념

| 개념 | 설명 | 기말 논문 연결 |
|---|---|---|
| Model stealing | 타깃 모델의 지식 또는 행동을 외부에서 복제하는 공격군 | 위협모형의 중심 사례 |
| Model extraction | 질의-응답 쌍을 이용해 모델 행동 또는 파라미터를 추정하는 절차 | toy 실험의 substitute model 설계 |
| Fidelity | 원 모델과 대체 모델의 출력 일치도 | W13 실험의 핵심 지표 |
| Attack prevention/detection | 질의 제한, 모니터링, 출력 변형, 워터마킹 등 | 방어 평가표 |

## 5. 방법론

문헌조사와 taxonomy 기반 systematization을 수행한다. 논문은 모델 도난 공격을 목표, 지식 수준, 대상 모델, 질의 방식, 성능 지표별로 비교하고, 방어는 탐지와 예방 관점으로 나누어 설명한다.

## 6. 주요 결과

모델 도난은 단순한 파라미터 탈취가 아니라 행동 복제, architecture/hyperparameter 추정, decision boundary 모방 등 여러 목표를 갖는다. 방어도 단일 기법만으로 충분하지 않으며, 공격자의 query budget과 출력 접근 수준에 따라 효과가 달라진다.

## 7. 보안 관점 분석

Confidentiality는 모델 행동과 학습된 지식의 유출로 흔들리고, accountability는 도난 모델의 출처를 입증하지 못할 때 약해진다. W13 실습에서는 실제 API를 사용하지 않고 이 논문의 fidelity/query budget 관점을 synthetic query-response 평가로 축소한다.

## 8. 한계와 오픈문제

Survey 문헌이므로 개별 공격의 최신 구현 성능을 그대로 일반화할 수 없다. 방어가 공격 조합이나 adaptive attacker에 대해 얼마나 유지되는지는 별도 실험 또는 최신 문헌 대조가 필요하다.

## 9. 기말 논문에 반영할 부분

모델 추출 위협모형, query budget, extraction fidelity, 방어 선택 기준을 관련연구와 평가방법 장에 반영한다.
