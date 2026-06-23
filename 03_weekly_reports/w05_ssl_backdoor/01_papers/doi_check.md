# W05 DOI/URL 검증표

## 1. 검증 결과

| ID | 논문 제목 | DOI/URL | 검증 근거 | 상태 | 남은 검토 사항 |
|---|---|---|---|---|---|
| P01 | A Survey on Self-Supervised Learning: Algorithms, Applications, and Future Trends | IEEE DOI `10.1109/TPAMI.2024.3415112`; arXiv DOI `10.48550/arXiv.2301.05712`; https://doi.org/10.1109/TPAMI.2024.3415112; https://arxiv.org/abs/2301.05712 | Crossref 제목 검색, 로컬 PDF 첫 페이지, arXiv ID | TPAMI DOI 확인 | 강의계획서의 `Yan Gui` 표기가 `Jie Gui`의 오기인지 사람 확인 필요 |
| P02 | A Comprehensive Survey on Self-Supervised Learning for Recommendation | `10.1145/3746280`; https://doi.org/10.1145/3746280 | Crossref DOI, 로컬 PDF metadata/첫 페이지 | DOI 확인, 대체 문헌 가능성 표시 | 강의계획서 지정 `A Comprehensive Survey on Self-Supervised Learning` 일반 SSL survey와 동일 여부 확인 필요 |
| P03 | Self-Supervised Learning for Videos: A Survey | `10.1145/3577925`; https://doi.org/10.1145/3577925; https://arxiv.org/abs/2207.00419 | Crossref DOI, 로컬 PDF metadata/첫 페이지, arXiv ID | DOI/URL 확인 | 강의계획서 제목 `Self-Supervised Learning of Video Representations: A Survey`와의 제목 차이 메모 유지. Article 번호는 Crossref에서 확인되지 않아 확인 필요 |
| P04 | Threats to Training: A Survey of Poisoning Attacks and Defenses on Machine Learning Systems | `10.1145/3538707`; https://doi.org/10.1145/3538707 | Crossref DOI, 로컬 PDF 첫 페이지 | DOI 확인, 제목 차이 표시 | 강의계획서 제목 및 `Y. Wang et al.` 표기와 동일 논문 여부 확인 필요 |
| P05 | A survey of backdoor attacks and defences: From deep neural networks to large language models | `10.1016/j.jnlest.2025.100326`; https://doi.org/10.1016/j.jnlest.2025.100326 | Crossref DOI, Elsevier/KeAi PDF metadata/첫 페이지 | DOI/URL 확인 | 강의계획서 `Z. Jin et al.` 표기와 출판사 첫 저자 `Ling-Xin Jin`의 대응 확인 필요 |

## 2. 출판 정보 메모

| ID | 권호/페이지/Article 정보 |
|---|---|
| P01 | IEEE Transactions on Pattern Analysis and Machine Intelligence, Vol. 46, No. 12, pp. 9052-9071, Dec. 2024 |
| P02 | ACM Computing Surveys, Vol. 58, No. 1, Article 22, 1-38 pages, online Sep. 2025, print Jan. 2026 |
| P03 | ACM Computing Surveys, Vol. 55, No. 13s, pp. 1-37, online Jul. 13, 2023, print Dec. 31, 2023. Article 번호 확인 필요 |
| P04 | ACM Computing Surveys, Vol. 55, No. 7, Article 134, 1-36 pages, online Dec. 15, 2022 |
| P05 | Journal of Electronic Science and Technology, Vol. 23, No. 3, Article 100326, 2025 |

## 3. 로컬 PDF 확인 메모

| ID | 확인 내용 |
|---|---|
| P01 | `pdfinfo` 기본 Title은 비어 있으나 첫 페이지 제목과 arXiv ID가 확인됨. 로컬 PDF는 arXiv v4 성격으로 보이며 TPAMI 최종판과 판본 차이 확인 필요 |
| P02 | `pdfinfo` Title, 첫 페이지, DOI가 `A Comprehensive Survey on Self-Supervised Learning for Recommendation`, `10.1145/3746280`로 일치함 |
| P03 | `pdfinfo` Title과 첫 페이지 제목은 arXiv판 `Self-Supervised Learning for Videos: A Survey`로 확인됨 |
| P04 | `pdfinfo` 기본 Title은 비어 있으나 첫 페이지 제목과 DOI가 `Threats to Training: A Survey of Poisoning Attacks and Defenses on Machine Learning Systems`, `10.1145/3538707`로 확인됨 |
| P05 | `pdfinfo` Title, Subject, XMP metadata에서 DOI `10.1016/j.jnlest.2025.100326` 확인됨 |

## 4. 검증 원칙

1. DOI는 추측해서 적지 않는다.
2. 프롬프트/강의계획서 제목과 로컬 PDF 제목이 다르면 정식 출판 제목을 우선하되, 동일 논문 여부가 불명확한 항목은 `확인 필요`로 남긴다.
3. 최종 제출 전 P02 대체 문헌 사용 여부, P03 Article 번호, P04 동일 논문 여부, P05 저자 표기를 사람이 다시 확인한다.

<!-- AUTO-RELATED-PAPER-REFLECTION:start -->
## 논문/관련 논문 최종 판정 반영표

아래 표는 공식 DOI/arXiv 재검색 결과를 반영한 최종 판정이다. `논문 / 확인`은 공식 서지 기준으로 논문 인용, `관련 논문 / 확인`은 주차 주제 보강용 관련 논문 인용을 뜻한다.

| ID | 구분 | 상태 | 공식 확인 기준 | 보고서 반영 |
|---|---|---|---|---|
| P01 | 논문 / 확인 | 공식 DOI 확인 | `https://doi.org/10.1109/TPAMI.2024.3415112`; A Survey on Self-Supervised Learning: Algorithms, Applications, and Future Trends; IEEE TPAMI; 2024 | 공식 서지 기준으로 논문 인용 |
| P02 | 관련 논문 / 확인 | 공식 DOI 확인 | `https://doi.org/10.1145/3746280`; A Comprehensive Survey on Self-Supervised Learning for Recommendation; ACM Computing Surveys; 2025 | 주차 주제 보강용 관련 논문으로 인용 |
| P04 | 관련 논문 / 확인 | 공식 DOI 확인 | `https://doi.org/10.1145/3538707`; Threats to Training: A Survey of Poisoning Attacks and Defenses on Machine Learning Systems; ACM Computing Surveys; 2022 | 주차 주제 보강용 관련 논문으로 인용 |
| P05 | 논문 / 확인 | 공식 DOI 확인 | `https://doi.org/10.1016/j.jnlest.2025.100326`; A survey of backdoor attacks and defences: From deep neural networks to large language models; Journal of Electronic Science and Technology; 2025 | 공식 서지 기준으로 논문 인용 |
<!-- AUTO-RELATED-PAPER-REFLECTION:end -->
