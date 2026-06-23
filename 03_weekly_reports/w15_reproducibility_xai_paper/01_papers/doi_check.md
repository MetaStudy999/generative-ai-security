# W15 DOI/URL 검증표

> 최종 판정 우선: 이 문서의 현재 상태는 `논문/관련 논문 최종 반영표`를 우선한다. 상단의 제목·저자·로컬 PDF 차이 메모는 오류 판정이 아니라 검증 이력이며, `관련 논문 / 확인`은 주차 주제에 맞는 공식 확인 논문으로 사용한다.
>
> 2026-06-24 기준: `02_paper_summaries/P01_summary.md` ~ `P05_summary.md`는 100점형 구조로 보완 완료했다. 수식은 GitHub, MS Word, PDF 변환 호환성을 위해 Markdown 표 밖의 LaTeX block math로 작성했다.

| ID | 논문 제목 | DOI/URL | 검증 근거 | 상태 | 비고 |
|---|---|---|---|---|---|
| P01 | A Survey on Evaluation of Large Language Models | `https://doi.org/10.1145/3641289` | 로컬 PDF 첫 페이지, DOI/Crossref metadata | 확인 / 100점형 summary 보완 완료 | ACM Transactions on Intelligent Systems and Technology 15(3), Article 39. 원 프롬프트의 ACM Computing Surveys 표기와 다름 |
| P02 | Assuring the Machine Learning Lifecycle: Desiderata, Methods, and Challenges | `https://doi.org/10.1145/3453444` | White Rose accepted version 표지, DOI/Crossref metadata | 확인 / 100점형 summary 보완 완료 | ACM Computing Surveys 54(5), Article 111. 로컬 PDF는 accepted version |
| P03 | Explainable AI: Core Ideas, Techniques, and Solutions | `https://doi.org/10.1145/3561048` | Crossref metadata에서 ACM Computing Surveys 55(9), Article 131 확인. 로컬 PDF는 Mersha et al. 관련 보조 문헌 | 공식 DOI 확인 / PDF 차이 기록 / 100점형 summary 보완 완료 | 공식 metadata의 제1저자는 Rudresh Dwivedi로 확인된다. 원 프롬프트의 Vivek Dwivedi 표기와 로컬 PDF 차이는 최종 반영표 기준 공식 출판정보로 정리 |
| P04 | Explainable Artificial Intelligence (XAI): Concepts, Taxonomies, Opportunities and Challenges toward Responsible AI | `https://doi.org/10.1016/j.inffus.2019.12.012` | ScienceDirect article page 및 로컬 arXiv preprint 대조 | 확인 / 100점형 summary 보완 완료 | Information Fusion 58, 82-115 |
| P05 | Concept-based Explainable Artificial Intelligence: A Survey | `https://doi.org/10.1145/3774643`, `https://arxiv.org/abs/2312.12936` | arXiv API와 Crossref metadata에서 동일 제목·저자 및 최종 ACM DOI 확인 | 확인 / 100점형 summary 보완 완료 | ACM Computing Surveys, online publication 2025-11-08, Article 3774643. 권호/issue는 최종 제출 전 ACM 페이지에서 재확인 |

## 허위 인용 방지 원칙

- DOI가 확인되지 않은 항목은 참고문헌 본문에 확정 DOI처럼 쓰지 않는다.
- 관련 논문 PDF 항목은 지정 논문과 실제 PDF가 다름을 본문, 제출본, 발표자료에 함께 표시한다.
- 최종 기말논문에는 공식 출판사 페이지, DOI, 로컬 PDF가 서로 일치하는 문헌만 확정 참고문헌으로 반영한다.

## 2026-06-23 재검증 메모

- P03은 `Explainable AI (XAI): Core Ideas, Techniques, and Solutions`라는 ACM Computing Surveys 논문의 DOI `10.1145/3561048`이 확인되었으나, 로컬 PDF는 `Mersha et al., Explainable Artificial Intelligence: A Survey of Needs, Techniques, Applications, and Future Direction`이므로 강의자료 표기 원문으로 취급하지 않는다.
- P05는 arXiv `2312.12936` metadata가 DOI `10.1145/3774643`을 포함하고, Crossref metadata도 동일 제목과 저자, ACM Computing Surveys online publication을 반환하므로 DOI 확인 상태로 갱신한다.
- ACM 원문 페이지는 네트워크 환경에서 Cloudflare challenge로 직접 열람이 제한될 수 있으므로, 최종 제출 전 브라우저에서 DOI landing page와 PDF 권한을 사람이 재확인한다.

<!-- AUTO-RELATED-PAPER-REFLECTION:start -->
## 논문/관련 논문 최종 판정 반영표

아래 표는 공식 DOI/arXiv 재검색 결과를 반영한 최종 판정이다. `논문 / 확인`은 공식 서지 기준으로 논문 인용, `관련 논문 / 확인`은 주차 주제 보강용 관련 논문 인용을 뜻한다.

| ID | 구분 | 상태 | 공식 확인 기준 | 보고서 반영 |
|---|---|---|---|---|
| P01 | 논문 / 확인 | 공식 DOI 확인 | `https://doi.org/10.1145/3641289`; A Survey on Evaluation of Large Language Models; ACM Transactions on Intelligent Systems and Technology; 2024 | 공식 서지 기준으로 논문 인용 |
| P02 | 논문 / 확인 | 공식 DOI 확인 | `https://doi.org/10.1145/3453444`; Assuring the Machine Learning Lifecycle: Desiderata, Methods, and Challenges; ACM Computing Surveys 54(5), Article 111, pp. 1-39; 2021/2022 | 공식 서지 기준으로 논문 인용 |
| P03 | 논문 / 확인 | 공식 DOI 확인 | `https://doi.org/10.1145/3561048`; Explainable AI (XAI): Core Ideas, Techniques, and Solutions; ACM Computing Surveys; 2023 | 공식 서지 기준으로 논문 인용 |
| P04 | 논문 / 확인 | 공식 DOI 확인 | `https://doi.org/10.1016/j.inffus.2019.12.012`; Explainable Artificial Intelligence (XAI): Concepts, taxonomies, opportunities and challenges toward responsible AI; Information Fusion 58, pp. 82-115; 2020 | 공식 서지 기준으로 논문 인용 |
| P05 | 논문 / 확인 | 공식 DOI 확인 / 권호 추가 확인 | `https://doi.org/10.1145/3774643`; Concept-based Explainable Artificial Intelligence: A Survey; ACM Computing Surveys, Article 3774643, online 2025-11-08 | 공식 서지 기준으로 논문 인용. 최종 제출 전 ACM 권호/issue 표기만 재확인 |
<!-- AUTO-RELATED-PAPER-REFLECTION:end -->
