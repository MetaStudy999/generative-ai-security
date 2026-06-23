# W11 논문 목록

| ID | 구분 | 논문 제목 | 저자 | 공식 출판정보 | 로컬 PDF | DOI/URL 상태 |
|---|---|---|---|---|---|---|
| P01 | 지정 논문/로컬 PDF 주제 일치 | A Critical Review on the Use (and Misuse) of Differential Privacy in Machine Learning | Alberto Blanco-Justicia, David Sanchez, Josep Domingo-Ferrer, Krishnamurty Muralidhar | ACM Computing Surveys 55(8), pp. 1-16, online 2022-12-23, print 2023-08-31 | `01_Blanco_Justicia_et_al_2022_Differential_Privacy_Critical_Review.pdf`는 arXiv v2 | DOI `10.1145/3547139`; arXiv `2206.04621` |
| P02 | 지정 논문/로컬 PDF 제목 일치, 강의 표기 보정 필요 | Recent Advances of Differential Privacy in Centralized Deep Learning: A Systematic Survey | Lea Demelius, Roman Kern, Andreas Trugler | ACM Computing Surveys 57(6), pp. 1-28, online 2025-02-10, print 2025-06-30 | `02_Demelius_et_al_2025_Centralized_Deep_Learning_DP_Survey.pdf`는 arXiv v1 | DOI `10.1145/3712000`; arXiv `2309.16398`; `Jonathan Demelius` 표기 확인되지 않음 |
| P03 | 지정 논문과 로컬 PDF 불일치 | Differential privacy in deep learning: A literature survey | Crossref 기준 Ke Pan, Yew-Soon Ong, Maoguo Gong, Hui Li, A.K. Qin, Yuan Gao | Neurocomputing 589, Article 127663, 2024-07 | `03_SUBSTITUTE_Fu_et_al_2024_Differentially_Private_FL_Review.pdf`는 Fu et al.의 DP-FL systematic review | DOI `10.1016/j.neucom.2024.127663`; 지정 논문 원문 PDF 확보 필요; 강의자료의 `Zizheng Pan et al.` 표기 최종 확인 필요 |
| P04 | 지정 논문/로컬 PDF 주제 일치 | Membership Inference Attacks on Machine Learning: A Survey | Hongsheng Hu, Zoran Salcic, Lichao Sun, Gillian Dobbie, Philip S. Yu, Xuyun Zhang | ACM Computing Surveys 54(11s), pp. 1-37, print 2022-01-31, online 2022-09-09 | `04_Hu_et_al_2022_Membership_Inference_Attacks_Survey.pdf`는 arXiv/ACM preprint | DOI `10.1145/3523273`; arXiv `2103.07853` |
| P05 | 지정 논문과 로컬 PDF 불일치, 강의 표기 보정 필요 | Defenses to Membership Inference Attacks: A Survey | Crossref 기준 Li Hu, Anli Yan, Hongyang Yan, Jin Li, Teng Huang, Yingying Zhang, Changyu Dong, Chunsheng Yang | ACM Computing Surveys 56(4), pp. 1-34, online 2023-11-10, print 2024-04-30 | `05_SUBSTITUTE_Bai_et_al_2024_MIA_Attacks_Defenses_FL_Survey.pdf`는 Bai et al.의 FL-MIA survey | DOI `10.1145/3620667`; 지정 논문 원문 PDF 확보 필요; 강의자료의 `Hongsheng Hu et al.` 표기 최종 확인 필요 |

## 검증 메모

- DOI와 출판정보는 2026-06-23 Crossref 등록 메타데이터와 DOI URL 기준으로 확인했다. ACM Digital Library의 primary URL은 각 DOI의 `dl.acm.org/doi/...`로 등록되어 있다.
- P01, P02, P04의 로컬 PDF는 arXiv 또는 preprint 판이므로 ACM 최종본과 세부 pagination, article number 표기가 다를 수 있다.
- P02는 강의계획서 또는 기존 프롬프트의 `Jonathan Demelius et al.` 표기가 공식 메타데이터와 맞지 않는다. 현재 확인 가능한 공식 저자는 `Lea Demelius, Roman Kern, Andreas Trugler`이다.
- P03 DOI는 실제 Neurocomputing 논문과 연결되지만, 공식 메타데이터의 저자는 `Ke Pan et al.`이다. 강의자료의 `Zizheng Pan et al.` 표기는 최종 확인 필요 상태로 둔다.
- P03과 P05는 로컬 PDF가 지정 논문과 다르므로, 대체 PDF를 지정 논문처럼 인용하지 않는다.
- 공개 GitHub 저장소에 출판사 PDF 원문이 추적되어 있으면 저작권 위험이 있다. 현재 `.gitignore`에는 PDF 무시 규칙이 있으나 기존 PDF 5개는 이미 Git 추적 대상이다.

<!-- AUTO-RELATED-PAPER-REFLECTION:start -->
## 논문/관련 논문 최종 반영표

아래 표는 공식 DOI/arXiv 재검색 결과를 주차 보고서에 반영하기 위한 최종 판정이다. 기존 대조 기록은 보존하고, 보고서 본문과 참고문헌에서는 이 표의 `구분`과 `검증 상태`를 우선 사용한다.

| ID | 구분 | 논문 제목 | 논문 | 저자 | 연도 | 학술지/학회 | 학술지/출처 | DOI/URL | 검증 상태 | 보고서 반영 |
|---|---|---|---|---|---:|---|---|---|---|---|
| P01 | 논문 / 확인 | A Critical Review on the Use (and Misuse) of Differential Privacy in Machine Learning | A Critical Review on the Use (and Misuse) of Differential Privacy in Machine Learning | Alberto Blanco-Justicia et al. | 2022 | ACM Computing Surveys | ACM Computing Surveys | `https://doi.org/10.1145/3547139` | 공식 DOI 확인 | 공식 서지 기준으로 논문 인용 |
| P04 | 논문 / 확인 | Membership Inference Attacks on Machine Learning: A Survey | Membership Inference Attacks on Machine Learning: A Survey | Hongsheng Hu et al. | 2022 | ACM Computing Surveys | ACM Computing Surveys | `https://doi.org/10.1145/3523273` | 공식 DOI 확인 | 공식 서지 기준으로 논문 인용 |
| P02 | 논문 / 확인 | Recent Advances of Differential Privacy in Centralized Deep Learning: A Systematic Survey | Recent Advances of Differential Privacy in Centralized Deep Learning: A Systematic Survey | Lea Demelius, Roman Kern, Andreas Trugler | 2025 | ACM Computing Surveys | ACM Computing Surveys | `https://doi.org/10.1145/3712000` | 공식 DOI 확인 | 공식 서지 기준으로 논문 인용 |
| P03 | 논문 / 확인 | Differential privacy in deep learning: A literature survey | Differential privacy in deep learning: A literature survey | Ke Pan et al. | 2024 | Neurocomputing | Neurocomputing | `https://doi.org/10.1016/j.neucom.2024.127663` | 공식 DOI 확인 | 공식 서지 기준으로 논문 인용 |
| P05 | 논문 / 확인 | Defenses to Membership Inference Attacks: A Survey | Defenses to Membership Inference Attacks: A Survey | Li Hu et al. | 2023 | ACM Computing Surveys | ACM Computing Surveys | `https://doi.org/10.1145/3620667` | 공식 DOI 확인 | 공식 서지 기준으로 논문 인용 |
<!-- AUTO-RELATED-PAPER-REFLECTION:end -->
