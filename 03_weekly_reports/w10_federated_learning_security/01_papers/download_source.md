# W10 다운로드 출처 기록

| ID | 논문 제목 | 확보 방식 | 파일명 | 공식 URL/DOI | 비고 |
|---|---|---|---|---|---|
| P01 | Federated Learning Survey: A Multi-Level Taxonomy of Aggregation Techniques, Experimental Insights, and Future Frontiers | 로컬 PDF | 01_Arbaoui_et_al_2024_FL_Aggregation_Taxonomy.pdf | https://doi.org/10.1145/3678182 | 로컬 PDF는 AAM/arXiv 성격. 수업자료의 CSUR 표기와 TIST DOI 메타데이터 차이 있음 |
| P02 | A survey on security and privacy of federated learning | 로컬 PDF | 02_Mothukuri_et_al_2021_FL_Security_Privacy_Survey.pdf | https://doi.org/10.1016/j.future.2020.10.007 | Elsevier/FGCS 출판본 기준 |
| P03 | Survey on federated learning threats: Concepts, taxonomy on attacks and defences, experimental study and challenges | 로컬 PDF | 03_Rodriguez_Barroso_et_al_2023_FL_Threats_Survey.pdf | https://doi.org/10.1016/j.inffus.2022.09.011; https://arxiv.org/abs/2201.08135 | arXiv preprint와 Information Fusion 출판본 모두 확인 |
| P04 | The Federation Strikes Back: A Survey of Federated Learning Privacy Attacks, Defenses, Applications, and Policy Landscape | 로컬 PDF | 04_Zhao_et_al_2025_Federation_Strikes_Back.pdf | https://doi.org/10.1145/3724113 | 로컬 PDF는 AAM/프리프린트 성격. 최종 DOI 메타데이터는 ACM Computing Surveys 57(9), pp. 1-37 |
| P05 | Backdoor attacks and defenses in federated learning: Survey, challenges and future research directions | 로컬 PDF | 05_Nguyen_et_al_2024_FL_Backdoor_Attacks_Defenses.pdf | https://doi.org/10.1016/j.engappai.2023.107166; https://arxiv.org/abs/2303.02213 | arXiv preprint와 EAAI 출판본 모두 확인 |

## PDF 보관 정책 점검

- `01_papers/pdf/` 아래 PDF 5개는 `git ls-files` 기준 현재 저장소 추적 대상이다.
- `.gitignore`에는 이미 `03_weekly_reports/**/01_papers/pdf/*.pdf` 규칙이 존재하지만, 이미 추적 중인 파일에는 소급 적용되지 않는다.
- public GitHub 저장소에 출판사 PDF 원문이 올라가면 저작권 위험이 있다. 공개 저장소에는 원칙적으로 PDF 원문 대신 DOI/URL, 서지정보, 요약 파일만 남기는 편이 안전하다.
- 본 작업에서는 사용자 승인 없이 PDF 파일을 삭제하지 않았다. 공개 저장소 운영 전 PDF 추적 해제와 원문 삭제 여부는 사람이 최종 결정해야 한다.
