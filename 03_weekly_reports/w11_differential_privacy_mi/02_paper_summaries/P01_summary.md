# P01 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 논문 제목 | A Critical Review on the Use (and Misuse) of Differential Privacy in Machine Learning |
| 저자 | Alberto Blanco-Justicia, David Sanchez, Josep Domingo-Ferrer, Krishnamurty Muralidhar |
| 학술지/학회 | 강의자료: ACM Computing Surveys 55(8), Article 166; 로컬 PDF: arXiv preprint |
| 연도 | 2022 |
| DOI/URL | arXiv `2206.04621`; ACM DOI 공식 확인 필요 |
| PDF 파일명 | `01_Blanco_Justicia_et_al_2022_Differential_Privacy_Critical_Review.pdf` |
| 검증 상태 | 로컬 PDF 첫 페이지 확인, DOI 공식 대조 필요 |

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

## 6. 주요 결과

DP를 적용했다고 해서 자동으로 충분한 privacy guarantee가 생기지 않는다. 특히 느슨한 budget, composition/accounting 누락, utility 우선 구현은 DP의 핵심 약속을 약화시킬 수 있다.

## 7. 보안 관점 분석

P01은 W11의 accountability 축에 가장 강하게 연결된다. 보고서나 논문에서 DP를 주장할 때 epsilon, delta, accountant, threat model, utility drop, membership inference risk를 함께 제시해야 한다.

## 8. 한계와 오픈문제

로컬 PDF는 arXiv preprint이므로 최종 ACM DOI와 권호 정보를 공식 페이지에서 다시 확인해야 한다. 또한 비판 논문이므로 특정 DP-SGD 구현의 최신 개선까지 모두 포괄하지는 않는다.

## 9. 기말 논문에 반영할 부분

기말 논문에서는 “DP 적용 여부”가 아니라 “DP 보장의 검증 가능성”을 평가 항목으로 둔다. P01은 DP misuse, privacy budget 해석, reporting checklist의 근거로 사용한다.
