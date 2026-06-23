# P01 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 논문 제목 | I Know What You Trained Last Summer: A Survey on Stealing Machine Learning Models and Defences |
| 저자 | Daryna Oliynyk, Rudolf Mayer, Andreas Rauber |
| 학술지 | ACM Computing Surveys |
| 공식 출판정보 | Vol. 55, Issue 14s, pp. 1-41, online 2023-07-17, print 2023-12-31 |
| DOI/URL | `10.1145/3595292`, `https://dl.acm.org/doi/10.1145/3595292`, `https://arxiv.org/abs/2206.08451` |
| 제목 표기 | 공식 제목은 `Defences` 표기. `Defenses`로 바꾸지 않는다. |
| 검증 상태 | 공식 DOI/출판정보 확인 완료. 로컬 PDF의 ACM reference placeholder보다 공식 ACM/Crossref 메타데이터를 우선한다. |

## 2. 한 문장 요약

이 논문은 MLaaS 환경의 모델 도난과 모델 추출 공격을 공격 목표, 공격 방법, 대상 모델, 방어 전략별로 체계화하며, query-response 기반 평가에서 fidelity, query cost, 공격 목표, 방어 적용 범위를 함께 보아야 함을 제시한다[1].

## 3. 연구문제

공개 API 또는 black-box 접근만으로도 모델 행동, 파라미터, 하이퍼파라미터, 결정경계가 어느 정도 복제될 수 있는가를 묻는다. 또한 공격 탐지와 예방 방어가 어떤 공격 목표와 자원 조건에서 약해지는지 분류한다.

## 4. 핵심 개념

| 개념 | 설명 | W13 연결 |
|---|---|---|
| Model stealing | 타깃 모델의 지식 또는 행동을 외부에서 복제하는 공격군 | W13 위협모형의 중심 |
| Model extraction | 질의-응답 쌍으로 모델 행동 또는 속성을 추정하는 절차 | toy substitute model 설계 |
| Fidelity | victim과 substitute의 출력 일치도 | 실험 핵심 지표 |
| Query budget | 공격자가 사용할 수 있는 질의 수 | 위험 노출과 비용 지표 |
| Defense selection | 탐지/예방 방어를 공격 목표와 접근 수준에 맞추는 기준 | 기말논문 평가표 |

## 5. 방법론

문헌조사와 taxonomy 기반 systematization을 수행한다. 공격은 목표, 지식 수준, 대상 모델, 질의 방식, 성능 지표로 비교하고, 방어는 탐지와 예방 관점으로 정리한다.

## 6. W13 활용

P01은 W13의 query budget, extraction fidelity, substitute accuracy 지표를 정당화하는 직접 배경이다. 다만 이 보고서는 실제 API 공격 절차를 재현하지 않고 synthetic binary classification 기반 안전 toy 실험으로 평가 형식만 축소한다.

## 7. 한계와 검토 필요

Survey 문헌이므로 최신 LLM 워터마킹과 생성모형 방어는 P02/P04/P05 및 후속 문헌으로 보완해야 한다. 공식 DOI는 확인됐지만, 공개 저장소에 PDF 원문을 커밋하는 것은 별도의 저작권 검토가 필요하다.
