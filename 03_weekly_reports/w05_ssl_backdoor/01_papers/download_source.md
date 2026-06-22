# W05 다운로드 출처 및 PDF 보관 정책

## 1. 출처 기록

| ID | 논문 제목 | 확보 방식 | 파일명 | 공식 접근 경로 |
|---|---|---|---|---|
| P01 | A Survey on Self-Supervised Learning: Algorithms, Applications, and Future Trends | 로컬 PDF, arXiv, Crossref/IEEE DOI 확인 | `01_Gui_et_al_2024_Self_Supervised_Learning_Survey.pdf` | https://doi.org/10.1109/TPAMI.2024.3415112; https://arxiv.org/abs/2301.05712 |
| P02 | A Comprehensive Survey on Self-Supervised Learning for Recommendation | 로컬 PDF, Crossref/ACM DOI 확인 | `02_Ren_et_al_2025_Self_Supervised_Learning_for_Recommendation.pdf` | https://doi.org/10.1145/3746280 |
| P03 | Self-Supervised Learning for Videos: A Survey | 로컬 PDF, Crossref/ACM DOI, arXiv URL 확인 | `03_Schiappa_Rawat_Shah_2023_Self_Supervised_Learning_Videos.pdf` | https://doi.org/10.1145/3577925; https://arxiv.org/abs/2207.00419 |
| P04 | Threats to Training: A Survey of Poisoning Attacks and Defenses on Machine Learning Systems | 로컬 PDF, Crossref/ACM DOI 확인 | `04_Wang_et_al_2022_Threats_to_Training_Poisoning_Survey.pdf` | https://doi.org/10.1145/3538707 |
| P05 | A survey of backdoor attacks and defences: From deep neural networks to large language models | 로컬 PDF, Crossref/Elsevier DOI 확인 | `05_Jin_et_al_2025_Backdoor_Attacks_and_Defences_Survey.pdf` | https://doi.org/10.1016/j.jnlest.2025.100326 |

## 2. PDF 보관 정책 점검

| 점검 항목 | 결과 |
|---|---|
| `01_papers/pdf/` PDF 존재 여부 | PDF 5개 존재 |
| Git 추적 여부 | `git ls-files 03_weekly_reports/w05_ssl_backdoor/01_papers/pdf` 기준 5개 모두 추적 중 |
| `.gitignore` 규칙 | `03_weekly_reports/**/01_papers/pdf/*.pdf` 규칙 존재 |
| public GitHub 저작권 위험 | 높음. IEEE/ACM/Elsevier/KeAi PDF 원문은 공개 저장소 배포에 부적절할 수 있음 |
| 조치 상태 | 사용자 승인 없이 삭제하지 않음 |
| 제출 전 권고 | public 저장소에서는 PDF 원문을 제거하거나 추적 해제하고 DOI/URL, 서지정보, 요약만 남긴다 |

## 3. 남은 확인

- 저장소가 public인지 private인지 확인한다.
- 이미 커밋된 PDF는 필요 시 `git rm --cached 03_weekly_reports/w05_ssl_backdoor/01_papers/pdf/*.pdf` 후 별도 비공개 보관소로 이동한다.
- 저작권 정책은 출판사별 self-archiving 조건을 사람이 최종 확인한다.
