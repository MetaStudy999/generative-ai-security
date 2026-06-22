# P02 논문 요약

## 1. 서지와 검증 상태

| 항목 | 내용 |
|---|---|
| 강의 지정 제목 | Adversarial Attacks and Defenses in Deep Learning |
| 강의 지정 저자 | Sen Zhou et al. |
| 공식 DOI 후보 | `10.1145/3547330` |
| 공식 URL | https://doi.org/10.1145/3547330 |
| 공식 후보 메타데이터 | Shuai Zhou et al., "Adversarial Attacks and Defenses in Deep Learning: From a Perspective of Cybersecurity", ACM Computing Surveys, Vol. 55, Issue 8, pp. 1-39, published 2022-12-23 |
| 강의 표기와 차이 | Sen/Shuai 저자 표기, 제목 subtitle, 권호/Article 정보 대조 필요 |
| 로컬 PDF | `02_Ren_et_al_2020_Adversarial_Attacks_Defenses_Deep_Learning.pdf` |
| 로컬 PDF 상태 | Kui Ren et al., Engineering 6, 2020, DOI `10.1016/j.eng.2019.12.012` |

주의: W12의 P02는 지정 논문명과 로컬 PDF 파일명·저자명이 다르므로, 동일 논문 여부와 최종 DOI를 확인 필요 상태로 유지한다.

## 2. 핵심 연구문제

P02는 deep learning 대적공격과 방어를 분류하고, 공격자 지식, 공격 시점, perturbation 제약, 방어 방식, 평가 지표를 taxonomy로 정리하는 문헌 축이다[2]. W12에서는 clean accuracy와 robust accuracy를 분리해서 보고해야 하는 이유를 설명하는 근거로 활용한다.

## 3. W12에서의 역할

| 관점 | 요약 |
|---|---|
| AI 원리 | adversarial example, perturbation budget, robust training, evaluation protocol |
| 보안 연결 | prediction integrity attack, adaptive attack, weak evaluation risk |
| 평가 지표 | clean accuracy, robust accuracy, attack success rate, defense success |
| 한계 | 로컬 PDF는 Kui Ren et al. 2020 Engineering 논문이므로 지정 Zhou 논문과 동일하게 인용하면 안 됨 |
| 내 논문 활용 | 공격·방어 평가축의 보안 근거와 threat model 분류 |

## 4. 실습 연결

W12의 `adversarial_features()`는 실제 FGSM/PGD가 아니라 선형 가중치 부호를 이용한 toy perturbation proxy다. 따라서 `Adversarial input` 조건은 실제 공격 절차 재현이 아니라 평가표를 안전하게 구성하기 위한 synthetic 조건이다.

## 5. 최종 제출 전 확인 항목

- 강의계획서의 `Sen Zhou` 표기가 `Shuai Zhou`의 오기인지 확인한다.
- ACM Computing Surveys article 번호와 권호를 공식 페이지에서 확인한다.
- 로컬 Kui Ren PDF를 P02 지정 논문 원문처럼 인용하지 않는다.
