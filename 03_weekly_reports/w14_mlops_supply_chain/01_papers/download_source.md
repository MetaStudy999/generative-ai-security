# W14 다운로드 출처 기록

| ID | 로컬 파일명 | 로컬 PDF 첫 페이지/메타데이터 | 지정 논문과 동일 여부 | 비고 |
|---|---|---|---|---|
| P01 | `01_Eken_et_al_2025_MLOps_Practices_Multivocal_Review.pdf` | `A Multivocal Review of MLOps Practices, Challenges and Open Issues`, Beyza Eken et al. | 부분 동일 | DOI/arXiv와 대응되나 수업자료의 Bayram Eken/긴 제목 표기와 다름 |
| P02 | `02_Paleyes_Urma_Lawrence_2022_ML_Deployment_Challenges.pdf` | arXiv:2011.09926v3, `Challenges in Deploying Machine Learning: a Survey of Case Studies` | 동일 주제 | ACM DOI와 제목/저자군 대응. 로컬 파일은 arXiv판 |
| P03 | `03_SUBSTITUTE_Cheng_et_al_2023_AIOps_Cloud_Survey.pdf` | `AI for IT Operations (AIOps) on Cloud Platforms: Reviews, Opportunities and Challenges`, Qian Cheng et al., arXiv:2304.04661 | 불일치 | Cheng et al. AIOps 대체문헌. 지정 논문 원문 PDF 확보 필요 |
| P04 | `04_SUBSTITUTE_Zhou_et_al_2019_Edge_Intelligence_Survey.pdf` | `Edge Intelligence: Paving the Last Mile of Artificial Intelligence with Edge Computing`, Zhi Zhou et al., arXiv:1905.10083 | 불일치 | Zhou et al. Edge Intelligence 대체문헌. 지정 논문 원문 PDF 확보 필요 |
| P05 | `05_Yang_Xia_Lo_Grundy_2022_Deep_Learning_Software_Engineering.pdf` | `A Survey on Deep Learning for Software Engineering`, Yanming Yang, Xin Xia, David Lo, John Grundy, arXiv:2011.14597 | 수업자료 표기와 불일치 | DOI 10.1145/3505243과 대응되나 수업자료의 Xiang Chen 표기 확인 필요 |

## PDF 보관 정책 점검

- `git ls-files 03_weekly_reports/w14_mlops_supply_chain/01_papers/pdf` 기준 W14 PDF 5개는 이미 Git 추적 중이다.
- `.gitignore`에는 `03_weekly_reports/**/01_papers/pdf/*.pdf` 규칙이 이미 존재한다.
- public GitHub 저장소에는 ACM/IEEE 등 출판사 PDF 원문을 올리지 않는 것이 원칙이다. 현재 PDF는 삭제 필요 상태로 표시하되, 사용자 명시 승인 없이 삭제하지 않는다.
- 제출용 문서에는 DOI/URL, 서지정보, 요약, 로컬 PDF 불일치 상태만 남기는 방향을 권장한다.

## 관리 메모

- 최종 제출 전 P03, P04, P05의 공식 원문 PDF를 확보하거나 보고서에서 대체문헌임을 유지한다.
- 현재 W14 보고서는 수업자료 DOI와 로컬 PDF 상태를 분리해 기록한다.
- 원문 세부 주장과 정량값은 PDF 첫 페이지·초록 수준 확인을 넘어서는 경우 `원문 세부 대조 필요`로 둔다.
