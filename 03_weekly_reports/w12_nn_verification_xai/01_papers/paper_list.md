# W12 논문 목록

## 1. 강의계획서 기준 W12 논문 패킷

| ID | 강의계획서 지정 논문 | 지정 저자 | 지정 연도/매체 | 로컬 PDF | 현재 판정 |
|---|---|---|---|---|---|
| P01 | A Review of Abstraction Methods Toward Verifying Neural Networks | Boudardara et al. | ACM Computing Surveys, 2024 | `01_SUBSTITUTE_Meng_et_al_2022_DNN_Robustness_Formal_Verification.pdf` | 지정 제목 DOI 후보는 확인했으나 매체 정보가 강의 표기와 다름. 로컬 PDF는 SUBSTITUTE |
| P02 | Adversarial Attacks and Defenses in Deep Learning | Sen Zhou et al. | ACM Computing Surveys, 2022 | `02_Ren_et_al_2020_Adversarial_Attacks_Defenses_Deep_Learning.pdf` | 로컬 PDF는 Kui Ren et al. 2020 Engineering 논문. 지정 논문 동일 여부 확인 필요 |
| P03 | Adversarial machine learning attacks against explainable artificial intelligence: A review | G. Vadillo et al. | WIREs Data Mining and Knowledge Discovery, 2025 | `03_SUBSTITUTE_Baniecki_Biecek_2023_Adversarial_XAI_Survey.pdf` | Vadillo 계열 공식 DOI 후보는 확인했으나 제목이 강의 표기와 다름. 로컬 PDF는 SUBSTITUTE |
| P04 | Adversarial Robustness of Neural Networks from Lipschitz Regularization: A Survey | Inaki Pérez et al. | ACM Computing Surveys, 2024 | `04_SUBSTITUTE_Finlay_et_al_2018_Lipschitz_Adversarial_Robustness.pdf` | 강의 표기와 완전 일치하는 공식 DOI 미확인. 로컬 PDF는 SUBSTITUTE |
| P05 | The Triangular Trade-off between Robustness, Accuracy, and Fairness | Chih-Hsiang Cheng et al. | ACM Computing Surveys, 2024 | `05_SUBSTITUTE_Singh_et_al_2021_Accuracy_Fairness_Robustness_Study.pdf` | 유사 ACM DOI 후보는 확인했으나 저자/제목/연도가 강의 표기와 다름. 로컬 PDF는 SUBSTITUTE |

## 2. 로컬 PDF 대조 결과

| ID | 로컬 PDF 첫 페이지/메타데이터 확인 | 지정 논문과 동일 여부 |
|---|---|---|
| P01 | Meng et al., "Adversarial Robustness of Deep Neural Networks: A Survey from a Formal Verification Perspective", arXiv:2206.12227, 2022 | 불일치. SUBSTITUTE |
| P02 | Kui Ren et al., "Adversarial Attacks and Defenses in Deep Learning", Engineering 6, 2020, DOI `10.1016/j.eng.2019.12.012` | 지정 저자/매체/연도와 불일치. 동일 여부 확인 필요 |
| P03 | Hubert Baniecki and Przemyslaw Biecek, "Adversarial attacks and defenses in explainable artificial intelligence: A survey", arXiv:2306.06123 | 불일치. SUBSTITUTE |
| P04 | Chris Finlay et al., "Lipschitz Regularized Deep Neural Networks Generalize and are Adversarially Robust", arXiv:1808.09540 | 불일치. SUBSTITUTE |
| P05 | Moninder Singh et al., "An Empirical Study of Accuracy, Fairness, Explainability, Distributional Robustness, and Adversarial Robustness", arXiv:2109.14653 | 불일치. SUBSTITUTE |

## 3. 필수 주의 문구

- 주의: W12의 P01은 지정 논문과 로컬 PDF가 불일치한다. 현재 로컬 PDF는 Meng et al. 2022 formal verification 관련 대체 문헌이므로, 최종 제출 전 Boudardara et al. 지정 논문 원문 PDF 또는 공식 출판 페이지를 확보해야 한다.
- 주의: W12의 P02는 지정 논문명과 로컬 PDF 파일명·저자명이 다르므로, 동일 논문 여부와 최종 DOI를 확인 필요 상태로 유지한다.
- 주의: W12의 P03은 지정 논문과 로컬 PDF가 불일치한다. 현재 로컬 PDF는 Baniecki/Biecek 2023 adversarial XAI 관련 대체 문헌이므로, 최종 제출 전 G. Vadillo et al. 지정 논문 원문 PDF 또는 공식 출판 페이지를 확보해야 한다.
- 주의: W12의 P04는 지정 논문과 로컬 PDF가 불일치한다. 현재 로컬 PDF는 Finlay et al. 2018 Lipschitz robustness 관련 대체 문헌이므로, 최종 제출 전 Inaki Pérez et al. 지정 논문 원문 PDF 또는 공식 출판 페이지를 확보해야 한다.
- 주의: W12의 P05는 지정 논문과 로컬 PDF가 불일치한다. 현재 로컬 PDF는 Singh et al. 2021 accuracy/fairness/robustness 관련 대체 문헌이므로, 최종 제출 전 Chih-Hsiang Cheng et al. 지정 논문 원문 PDF 또는 공식 출판 페이지를 확보해야 한다.

## 4. PDF 보관 정책

`01_papers/pdf/`의 PDF 5개는 `git ls-files` 기준 이미 저장소 추적 대상이다. `.gitignore`에는 `03_weekly_reports/**/01_papers/pdf/*.pdf` 규칙이 있으나, 이미 추적 중인 PDF에는 적용되지 않는다. public GitHub 저장소에서는 출판사 PDF 원문 대신 DOI/URL, 서지정보, 요약만 공개하는 편이 안전하다. 삭제는 사용자 승인 후 별도 작업으로 처리한다.
