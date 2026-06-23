# P01 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 논문 제목 | A Critical Review on the Use (and Misuse) of Differential Privacy in Machine Learning |
| 저자 | Alberto Blanco-Justicia, David Sanchez, Josep Domingo-Ferrer, Krishnamurty Muralidhar |
| 학술지/학회 | ACM Computing Surveys 55(8), pp. 1-16; online 2022-12-23, print 2023-08-31 |
| 연도 | 2022/2023 |
| DOI/URL | DOI `10.1145/3547139`; arXiv `2206.04621` |
| PDF 파일명 | `01_Blanco_Justicia_et_al_2022_Differential_Privacy_Critical_Review.pdf` |
| 검증 상태 | Crossref/ACM 등록 DOI 확인. 로컬 PDF는 arXiv v2이므로 ACM 최종본과 세부 차이 검토 필요 |

## 2. 한 문장 요약

> 이 논문은 ML에서 DP가 형식적 보장 없이 “noise addition” 수준으로 오용될 위험을 비판하고, DP 주장에는 privacy budget, utility, empirical privacy risk 평가가 함께 필요하다는 기준을 제시한다.

## 3. 연구문제

DP를 ML에 적용할 때 이론적 DP 보장과 실제 구현 사이에 어떤 간극이 생기며, 높은 epsilon이나 불충분한 accounting이 privacy claim을 어떻게 약화시키는가를 묻는다.

## 4. 핵심 개념

| 개념 | 설명 | 기말 논문 연결 |
|---|---|---|
| epsilon-DP | 한 레코드 포함 여부가 출력 분포에 미치는 영향을 제한하는 형식적 보장 | DP 정의와 오용 기준 |
| Privacy budget | 보호 강도를 나타내지만 값이 크면 실질 보호가 약해질 수 있음 | 해석 주의사항 |
| Ex ante guarantee | 실행 전 수학적으로 보장되는 privacy 조건 | DP claim 검증 기준 |
| Ex post evaluation | 실제 leakage나 re-identification risk를 실험적으로 평가 | 실험 평가표 |

## 5. 방법론

DP의 원래 가정과 ML 적용 사례를 비판적으로 검토하고, privacy-utility-efficiency trade-off가 단순히 “DP 사용 여부”로 해결되지 않음을 문헌과 실험적 논의로 정리한다.

### 5.1 핵심 수식 또는 알고리즘 설명

| 항목 | 내용 |
|---|---|
| 수식/알고리즘 이름 | (epsilon, delta)-Differential Privacy 정의 |
| 원문 위치 | 논문 세부 절/쪽/그림/알고리즘 번호 확인 필요. 로컬 DOI/URL 점검표로 문헌 대응만 확인. |
| 작성 형식 | Markdown + LaTeX math |
| 검산 도구 | 사용 안 함 |
| 수식 또는 절차 | 표준 정의식 / 원문 직접 인용 아님.<br>$$\Pr[M(D)\in S]\le e^{\varepsilon}\Pr[M(D_{adj})\in S]+\delta$$ |
| 기호·입력·출력 | \(D,D_{adj}\): 하나의 레코드만 다른 인접 데이터셋, \(M\): randomized mechanism, \(S\): 출력 집합 |
| 직관적 의미 | (epsilon, delta)-Differential Privacy 정의는 Differential Privacy·Membership Inference 평가에서 핵심 원리나 평가 지표를 정량적으로 해석하기 위한 표준식이다. |
| 보안 관점 해석 | Differential Privacy·Membership Inference 평가에서는 정상 성능과 보안 실패 조건을 분리해 보아야 한다. 이 항목은 공격·방어 원리 또는 운영 통제의 평가 기준을 명시하되, 실제 공격 절차나 무단 적용 단계는 포함하지 않는다. |
| 평가 지표와 연결 | epsilon, delta, utility drop, MI advantage |
| 한계와 가정 | 표준 정의식 / 원문 직접 인용 아님. 논문별 변형, 정확한 수식 번호, 실험 설정은 원문 PDF에서 확인 필요다. |
| 기말 논문 반영 여부 | 반영 |

## 6. 주요 결과

DP를 적용했다고 해서 자동으로 충분한 privacy guarantee가 생기지 않는다. 특히 느슨한 budget, composition/accounting 누락, utility 우선 구현은 DP의 핵심 약속을 약화시킬 수 있다.

## 7. 보안 관점 분석

P01은 W11의 accountability 축에 가장 강하게 연결된다. 보고서나 논문에서 DP를 주장할 때 epsilon, delta, accountant, threat model, utility drop, membership inference risk를 함께 제시해야 한다.

## 8. 한계와 오픈문제

로컬 PDF는 arXiv preprint이므로 ACM 최종본의 문구, pagination, article number 표기는 최종 제출 전 다시 대조해야 한다. 또한 비판 논문이므로 특정 DP-SGD 구현의 최신 개선까지 모두 포괄하지는 않는다.

## 9. 기말 논문에 반영할 부분

기말 논문에서는 “DP 적용 여부”가 아니라 “DP 보장의 검증 가능성”을 평가 항목으로 둔다. P01은 DP misuse, privacy budget 해석, reporting checklist의 근거로 사용한다.
