# P04 논문 요약

## 1. 서지와 검증 상태

| 항목 | 내용 |
|---|---|
| 강의 지정 제목 | Adversarial Robustness of Neural Networks from Lipschitz Regularization: A Survey |
| 강의 지정 저자 | Inaki Pérez et al. |
| 공식 DOI 후보 | 확인 필요 |
| 유사 공식 후보 | `10.1145/3648351`, "Adversarial Robustness of Neural Networks from the Perspective of Lipschitz Calculus: A Survey" |
| 유사 후보 메타데이터 | Monty-Maximilian Zühlke and Daniel Kudenko, ACM Computing Surveys, Vol. 57, Issue 6, pp. 1-41, published 2025-02-10 |
| 강의 표기와 차이 | 저자, 제목, 연도가 지정 P04와 일치하지 않아 DOI 확정 금지 |
| 로컬 PDF | `04_SUBSTITUTE_Finlay_et_al_2018_Lipschitz_Adversarial_Robustness.pdf` |
| 로컬 PDF 상태 | Finlay et al. 2018/2019 Lipschitz regularized DNN paper. 지정 논문 원문 아님 |

주의: W12의 P04는 지정 논문과 로컬 PDF가 불일치한다. 현재 로컬 PDF는 Finlay et al. 2018 Lipschitz robustness 관련 대체 문헌이므로, 최종 제출 전 Inaki Pérez et al. 지정 논문 원문 PDF 또는 공식 출판 페이지를 확보해야 한다.

## 2. 핵심 연구문제

P04는 Lipschitz regularization이 adversarial robustness를 어떻게 설명하는지 다루는 문헌 축이다[4]. 핵심은 입력 변화가 출력 변화로 얼마나 증폭될 수 있는지 bound로 제한하고, margin, certified radius, robust accuracy를 함께 해석하는 것이다.

## 3. W12에서의 역할

| 관점 | 요약 |
|---|---|
| AI 원리 | Lipschitz constant, margin, regularization, certified radius |
| 보안 연결 | perturbation amplification, robustness overclaim |
| 평가 지표 | robust accuracy, Lipschitz bound, certified rate |
| 한계 | 지정 P04 공식 DOI는 확인 필요. 로컬 PDF는 Finlay 대체 문헌 |
| 내 논문 활용 | toy certified rate proxy의 이론적 배경과 한계 설명 |

## 4. 실습 연결

W12의 `certified_rate`는 `signed_margin - epsilon * ||w||_1 > 0` 형태의 선형 모델 bound proxy다. 이 값은 formal verifier가 발급한 DNN certificate가 아니며, Lipschitz/regularization 개념을 교육용으로 연결하기 위한 최소 지표다.

## 5. 최종 제출 전 확인 항목

- Inaki Pérez et al. 지정 논문 공식 DOI를 재검색한다.
- 유사 후보 DOI `10.1145/3648351`을 P04로 확정하지 않는다.
- Finlay PDF는 대체 문헌으로만 관리한다.
