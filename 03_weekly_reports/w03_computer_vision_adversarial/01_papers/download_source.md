# W03 다운로드 출처 및 보관 정책 기록

| ID | 논문 제목 | 확보 방식 | 파일명 | 공식 DOI/URL | 보관 정책 메모 |
|---|---|---|---|---|---|
| P01 | Gradient-Based Learning Applied to Document Recognition | 로컬 PDF 확인 | `01_LeCun_et_al_1998_Gradient_Based_Learning_Document_Recognition.pdf` | https://doi.org/10.1109/5.726791 | IEEE 문헌 원문 PDF는 public 저장소 보관 위험 있음 |
| P02 | Deep Learning for Computer Vision: A Brief Review | 로컬 PDF 확인 | `02_Voulodimos_et_al_2018_Deep_Learning_Computer_Vision_Review.pdf` | https://doi.org/10.1155/2018/7068349 | OA 문헌이지만 라이선스/출처 표시 필요 |
| P03 | Multimodal Learning With Transformers: A Survey | 로컬 PDF 확인 | `03_Xu_et_al_2023_Multimodal_Learning_Transformers_Survey.pdf` | https://doi.org/10.1109/TPAMI.2023.3275156 | 로컬 PDF는 arXiv 버전으로 보임; 출판사 PDF 대체 여부 확인 필요 |
| P04 | Transformers in Vision: A Survey | 로컬 PDF 확인 | `04_Khan_et_al_2022_Transformers_in_Vision_Survey.pdf` | https://doi.org/10.1145/3505244 | 로컬 PDF는 arXiv 버전으로 보임; ACM 최종 PDF 보관 금지 권고 |
| P05 | A Survey of Robustness and Safety of 2D and 3D Deep Learning Models against Adversarial Attacks | 로컬 PDF 확인 | `05_Li_et_al_2024_Robustness_Safety_2D_3D_Adversarial_Attacks.pdf` | https://doi.org/10.1145/3636551 | 로컬 PDF는 submitted manuscript/arXiv 버전으로 보임; ACM 최종 PDF 보관 금지 권고 |

## public GitHub 보관 위험

- 원격 저장소 `MetaStudy999/generative-ai-security`는 GitHub API 기준 public 저장소로 확인되었다.
- `git ls-files` 기준 W03 PDF 5개가 이미 git 추적 대상이다.
- `.gitignore`에는 `03_weekly_reports/**/01_papers/pdf/*.pdf` 규칙이 이미 존재하지만, 과거에 커밋된 PDF는 계속 추적된다.
- 사용자의 명시 승인 없이는 PDF를 삭제하지 않는다. 최종 제출 전에는 PDF 원문 삭제 또는 Git LFS/비공개 저장소/공식 URL 대체 방안을 사람이 결정해야 한다.
