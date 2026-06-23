# W10 논문 목록

> 최종 판정 우선: 이 문서의 현재 상태는 `논문/관련 논문 최종 반영표`를 우선한다. 상단의 제목·저자·로컬 PDF 차이 메모는 오류 판정이 아니라 검증 이력이며, `관련 논문 / 확인`은 주차 주제에 맞는 공식 확인 논문으로 사용한다.
>
> 2026-06-24 기준: `02_paper_summaries/P01_summary.md` ~ `P05_summary.md`는 100점형 구조로 보완 완료했다. 수식은 GitHub, MS Word, PDF 변환 호환성을 위해 Markdown 표 밖의 LaTeX block math로 작성했다.

| ID | 논문 제목 | 저자 | 연도 | 공식 출판 정보 | 로컬 PDF | 검증 상태 |
|---|---|---|---|---|---|---|
| P01 | Federated Learning Survey: A Multi-Level Taxonomy of Aggregation Techniques, Experimental Insights, and Future Frontiers | Meriem Arbaoui, Mohamed-el-Amine Brahmia, Abdellatif Rahmoun, Mourad Zghal | 2024 | ACM Transactions on Intelligent Systems and Technology, 15(6), pp. 1-69 | 01_Arbaoui_et_al_2024_FL_Aggregation_Taxonomy.pdf | DOI 10.1145/3678182 확인. 100점형 summary 보완 완료. 수업자료/프롬프트의 ACM Computing Surveys 57(2) 표기와 공식 DOI 메타데이터/TIST 표기 차이 있음 |
| P02 | A survey on security and privacy of federated learning | Viraaji Mothukuri, Reza M. Parizi, Seyedamin Pouriyeh, Yan Huang, Ali Dehghantanha, Gautam Srivastava | 2021 | Future Generation Computer Systems, 115, pp. 619-640 | 02_Mothukuri_et_al_2021_FL_Security_Privacy_Survey.pdf | DOI 10.1016/j.future.2020.10.007 확인. 100점형 summary 보완 완료 |
| P03 | Survey on federated learning threats: Concepts, taxonomy on attacks and defences, experimental study and challenges | Nuria Rodriguez-Barroso, Daniel Jimenez-Lopez, M. Victoria Luzon, Francisco Herrera, Eugenio Martinez-Camara | 2023 | Information Fusion, 90, pp. 148-173 | 03_Rodriguez_Barroso_et_al_2023_FL_Threats_Survey.pdf | arXiv:2201.08135 및 출판 DOI 10.1016/j.inffus.2022.09.011 확인. 100점형 summary 보완 완료 |
| P04 | The Federation Strikes Back: A Survey of Federated Learning Privacy Attacks, Defenses, Applications, and Policy Landscape | Joshua C. Zhao et al. | 2025 | ACM Computing Surveys, 57(9), pp. 1-37 | 04_Zhao_et_al_2025_Federation_Strikes_Back.pdf | DOI 10.1145/3724113 확인. 100점형 summary 보완 완료. 수업자료 제목은 `The Federation Strikes Back` 부제가 빠진 축약 표기 |
| P05 | Backdoor attacks and defenses in federated learning: Survey, challenges and future research directions | Thuy Dung Nguyen, Tuan Nguyen, Phi Le Nguyen, Hieu H. Pham, Khoa D. Doan, Kok-Seng Wong | 2024 | Engineering Applications of Artificial Intelligence, 127, Article 107166 | 05_Nguyen_et_al_2024_FL_Backdoor_Attacks_Defenses.pdf | arXiv:2303.02213 및 출판 DOI 10.1016/j.engappai.2023.107166 확인. 100점형 summary 보완 완료 |

## 100점형 summary 반영 상태

| ID | 보완 상태 | 추가된 핵심 요소 |
|---|---|---|
| P01 | 완료 / 검증 메모 유지 | FedAvg, aggregation taxonomy, update provenance, non-IID/client drift 평가 |
| P02 | 완료 | FL security/privacy, leakage risk, utility drop, secure aggregation/DP trade-off |
| P03 | 완료 | Byzantine rate, robust aggregation, FL attack/defense taxonomy, malicious client index |
| P04 | 완료 | privacy risk score, MI/GI/PI, defense coverage, policy/compliance 평가 |
| P05 | 완료 | FL backdoor ASR, malicious client rate, model replacement, trigger/provenance 평가 |

## 검수 메모

- 위 목록은 `00_class_materials/AI 보안 박사과정 논문지도 세미나.md`, `00_class_materials/강의논문.md`, `01_codex_prompts/W10_federated_learning_security.md`, 로컬 PDF 첫 페이지, DOI 등록 메타데이터를 대조했다.
- P01은 수업자료와 W10 프롬프트에서 `ACM Computing Surveys, 57(2), 2024`로 적혀 있으나, DOI 10.1145/3678182의 공식 메타데이터와 로컬 AAM PDF 표기는 `ACM Transactions on Intelligent Systems and Technology`다. 참고문헌에는 공식 DOI 메타데이터 기준 TIST 표기를 우선 사용한다.
- P03은 arXiv 제출본과 Information Fusion 출판본 제목이 실질적으로 동일하며, 출판본은 DOI 10.1016/j.inffus.2022.09.011, volume 90, pp. 148-173으로 확인했다.
- P05는 arXiv 제출본과 Engineering Applications of Artificial Intelligence 출판본 제목이 실질적으로 동일하며, 출판본은 DOI 10.1016/j.engappai.2023.107166, volume 127, Article 107166으로 확인했다.
- P01/P04의 Article 번호는 DOI 등록 메타데이터에서 별도 `article-number` 필드로 확인되지 않았다. 수업자료의 P04 `Article 230` 표기는 공식 DOI 메타데이터와 추가 대조가 필요하다.

<!-- AUTO-RELATED-PAPER-REFLECTION:start -->
## 논문/관련 논문 최종 반영표

아래 표는 공식 DOI/arXiv 재검색 결과를 주차 보고서에 반영하기 위한 최종 판정이다. 기존 대조 기록은 보존하고, 보고서 본문과 참고문헌에서는 이 표의 `구분`과 `검증 상태`를 우선 사용한다.

| ID | 구분 | 논문 제목 | 논문 | 저자 | 연도 | 학술지/학회 | 학술지/출처 | DOI/URL | 검증 상태 | 보고서 반영 |
|---|---|---|---|---|---:|---|---|---|---|---|
| P01 | 논문 / 확인 | Federated Learning Survey: A Multi-Level Taxonomy of Aggregation Techniques, Experimental Insights, and Future Frontiers | Federated Learning Survey: A Multi-Level Taxonomy of Aggregation Techniques, Experimental Insights, and Future Frontiers | Meriem Arbaoui et al. | 2024 | ACM TIST | ACM Transactions on Intelligent Systems and Technology | `https://doi.org/10.1145/3678182` | 공식 DOI 확인 | 공식 서지 기준으로 논문 인용 |
| P02 | 논문 / 확인 | A survey on security and privacy of federated learning | A survey on security and privacy of federated learning | Viraaji Mothukuri et al. | 2021 | Future Generation Computer Systems | Future Generation Computer Systems | `https://doi.org/10.1016/j.future.2020.10.007` | 공식 DOI 확인 | 공식 서지 기준으로 논문 인용 |
| P03 | 논문 / 확인 | Survey on federated learning threats: Concepts, taxonomy on attacks and defences, experimental study and challenges | Survey on federated learning threats: Concepts, taxonomy on attacks and defences, experimental study and challenges | Nuria Rodriguez-Barroso et al. | 2023 | Information Fusion | Information Fusion | `https://doi.org/10.1016/j.inffus.2022.09.011` | 공식 DOI 확인 | 공식 서지 기준으로 논문 인용 |
| P04 | 논문 / 확인 | The Federation Strikes Back: A Survey of Federated Learning Privacy Attacks, Defenses, Applications, and Policy Landscape | The Federation Strikes Back: A Survey of Federated Learning Privacy Attacks, Defenses, Applications, and Policy Landscape | Joshua C. Zhao et al. | 2025 | ACM Computing Surveys | ACM Computing Surveys | `https://doi.org/10.1145/3724113` | 공식 DOI 확인 | 공식 서지 기준으로 논문 인용 |
| P05 | 논문 / 확인 | Backdoor attacks and defenses in federated learning: Survey, challenges and future research directions | Backdoor attacks and defenses in federated learning: Survey, challenges and future research directions | Thuy Dung Nguyen et al. | 2024 | Engineering Applications of Artificial Intelligence | Engineering Applications of Artificial Intelligence | `https://doi.org/10.1016/j.engappai.2023.107166` | 공식 DOI 확인 | 공식 서지 기준으로 논문 인용 |
<!-- AUTO-RELATED-PAPER-REFLECTION:end -->
