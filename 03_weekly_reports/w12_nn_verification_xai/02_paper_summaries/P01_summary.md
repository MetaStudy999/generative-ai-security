# P01 논문 요약

## 1. 서지와 검증 상태

| 항목 | 내용 |
|---|---|
| 강의 지정 제목 | A Review of Abstraction Methods Toward Verifying Neural Networks |
| 강의 지정 저자 | Boudardara et al. |
| 공식 DOI 후보 | `10.1145/3617508` |
| 공식 URL | https://doi.org/10.1145/3617508 |
| 공식 메타데이터 확인 | title과 Boudardara et al.는 일치하나, Crossref 기준 매체는 ACM Transactions on Embedded Computing Systems, Vol. 23, Issue 4, pp. 1-19, 2024 |
| 강의 표기와 차이 | 강의자료의 ACM Computing Surveys 56(7), Article 151 표기와 충돌 |
| 로컬 PDF | `01_SUBSTITUTE_Meng_et_al_2022_DNN_Robustness_Formal_Verification.pdf` |
| 로컬 PDF 상태 | Meng et al. 2022 arXiv formal verification survey. 지정 논문 원문 아님 |

주의: W12의 P01은 지정 논문과 로컬 PDF가 불일치한다. 현재 로컬 PDF는 Meng et al. 2022 formal verification 관련 대체 문헌이므로, 최종 제출 전 Boudardara et al. 지정 논문 원문 PDF 또는 공식 출판 페이지를 확보해야 한다.

## 2. 핵심 연구문제

P01은 신경망 검증에서 abstraction method가 어떤 역할을 하는지 정리하는 문헌이다[1]. 신경망은 안전중요 시스템에서 점점 많이 쓰이지만, 네트워크 규모와 비선형성 때문에 모든 입력 영역을 직접 검증하기 어렵다. Abstraction은 세부 계산을 검증 가능한 추상 모델이나 bound로 바꾸어 reachability, specification satisfaction, verification cost를 다룰 수 있게 한다.

## 3. W12에서의 역할

| 관점 | 요약 |
|---|---|
| AI 원리 | abstraction, reachability, bound propagation, formal specification |
| 보안 연결 | 검증되지 않은 robustness claim, 안전중요 시스템 배치 전 보증 부족 |
| 평가 지표 | certified robustness, specification satisfaction, verification cost |
| 한계 | 현재 로컬 PDF가 지정 논문 원문이 아니므로 세부 taxonomy와 권호 정보는 최종 대조 필요 |
| 내 논문 활용 | empirical robust accuracy와 formal verification certificate의 차이를 설명하는 배경 |

## 4. 실습 연결

W12 실험의 `certified_rate`는 P01식 formal verification 결과가 아니다. 현재 실험은 toy logistic classifier의 선형 margin bound proxy를 계산한다. 따라서 `certified_rate`는 verification pipeline을 흉내 낸 보고 형식 검증용 지표로만 해석한다.

## 5. 최종 제출 전 확인 항목

- ACM/DOI 페이지에서 매체명, 권호, Article 번호, 페이지를 사람이 최종 확인한다.
- 강의계획서의 ACM Computing Surveys 표기가 맞는지 재확인한다.
- 로컬 SUBSTITUTE PDF를 지정 논문 원문처럼 인용하지 않는다.
