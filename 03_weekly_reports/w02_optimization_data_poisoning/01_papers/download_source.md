# W02 PDF/URL 출처 기록

| ID | 논문 제목 | 로컬 PDF | 공식 DOI/URL | 보관 메모 |
|---|---|---|---|---|
| P01 | Optimization Methods for Large-Scale Machine Learning | `pdf/01_Bottou_Curtis_Nocedal_2018_Optimization_Methods_Large_Scale_ML.pdf` | `https://doi.org/10.1137/16M1080173` | SIAM Review 최종판 서지 확인 |
| P02 | Efficient Deep Learning: A Survey on Making Deep Learning Models Smaller, Faster, and Better | `pdf/02_Menghani_2023_Efficient_Deep_Learning_Survey.pdf` | `https://doi.org/10.1145/3578938`; arXiv `https://arxiv.org/abs/2106.08962` | ACM Computing Surveys 최종판을 우선 인용. Article 번호는 확인 필요 |
| P03 | A Comprehensive Survey on Poisoning Attacks and Countermeasures in Machine Learning | `pdf/03_Tian_Cui_Liang_Yu_2023_Comprehensive_Poisoning_Survey.pdf` | `https://doi.org/10.1145/3551636` | 출판 정보 기준 저자명 `Zhiyi Tian` |
| P04 | Wild Patterns Reloaded: A Survey of Machine Learning Security against Training Data Poisoning | `pdf/04_Cina_et_al_2023_Wild_Patterns_Reloaded_Poisoning_Survey.pdf` | `https://doi.org/10.1145/3585385`; arXiv `https://arxiv.org/abs/2205.01992` | 강의계획서 P04 제목과 동일 논문/이전 제목 여부 확인 필요 |
| P05 | A survey of backdoor attacks and defences: From deep neural networks to large language models | `pdf/05_Jin_et_al_2025_Backdoor_Attacks_and_Defences_Survey.pdf` | `https://doi.org/10.1016/j.jnlest.2025.100326` | Journal of Electronic Science and Technology 최종판 확인 |

## 공개 저장소 보관 정책

- 현재 `01_papers/pdf/` 아래 PDF 원문 5개가 Git 추적 대상이다.
- `.gitignore`에는 `03_weekly_reports/**/01_papers/pdf/*.pdf`가 이미 있으나, 과거에 추가된 추적 파일에는 소급 적용되지 않는다.
- public GitHub 저장소에는 출판사 PDF 원문 대신 DOI/URL, 서지정보, 개인 요약, 검증 메모만 남기는 것이 안전하다.
- 본 작업에서는 사용자 승인 없이 PDF를 삭제하지 않는다. 최종 제출 전 공개 저장소 배포 여부에 따라 `git rm --cached` 등 추적 제거를 사람이 승인해야 한다.
