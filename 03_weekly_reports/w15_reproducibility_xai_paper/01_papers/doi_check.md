# W15 DOI/URL 검증표

| ID | 논문 제목 | DOI/URL | 검증 근거 | 상태 | 비고 |
|---|---|---|---|---|---|
| P01 | A Survey on Evaluation of Large Language Models | `https://doi.org/10.1145/3641289` | 로컬 PDF 첫 페이지, DOI/Crossref metadata | 확인 | ACM Transactions on Intelligent Systems and Technology 15(3), Article 39. 원 프롬프트의 ACM Computing Surveys 표기와 다름 |
| P02 | Assuring the Machine Learning Lifecycle: Desiderata, Methods, and Challenges | `https://doi.org/10.1145/3453444` | White Rose accepted version 표지, DOI/Crossref metadata | 확인 | ACM Computing Surveys 54(5), Article 111. 로컬 PDF는 accepted version |
| P03 | Explainable AI: Core Ideas, Techniques, and Solutions | `https://doi.org/10.1145/3561048` | Crossref metadata에서 ACM Computing Surveys 55(9), Article 131 확인. 로컬 PDF는 Mersha et al. 대체 논문 | 부분 확인 | 공식 metadata의 제1저자는 Rudresh Dwivedi로 확인된다. 원 프롬프트의 Vivek Dwivedi 표기와 로컬 PDF가 모두 불일치하므로 지정 논문 원문 PDF 확보 필요 |
| P04 | Explainable Artificial Intelligence (XAI): Concepts, Taxonomies, Opportunities and Challenges toward Responsible AI | `https://doi.org/10.1016/j.inffus.2019.12.012` | ScienceDirect article page 및 로컬 arXiv preprint 대조 | 확인 | Information Fusion 58, 82-115 |
| P05 | Concept-based Explainable Artificial Intelligence: A Survey | `https://doi.org/10.1145/3774643`, `https://arxiv.org/abs/2312.12936` | arXiv API와 Crossref metadata에서 동일 제목·저자 및 최종 ACM DOI 확인 | 확인 | ACM Computing Surveys, online publication 2025-11-08, Article 3774643. 권호/issue는 최종 제출 전 ACM 페이지에서 재확인 |

## 허위 인용 방지 원칙

- DOI가 확인되지 않은 항목은 참고문헌 본문에 확정 DOI처럼 쓰지 않는다.
- 대체 PDF 항목은 지정 논문과 실제 PDF가 다름을 본문, 제출본, 발표자료에 함께 표시한다.
- 최종 기말논문에는 공식 출판사 페이지, DOI, 로컬 PDF가 서로 일치하는 문헌만 확정 참고문헌으로 반영한다.

## 2026-06-23 재검증 메모

- P03은 `Explainable AI (XAI): Core Ideas, Techniques, and Solutions`라는 ACM Computing Surveys 논문의 DOI `10.1145/3561048`이 확인되었으나, 로컬 PDF는 `Mersha et al., Explainable Artificial Intelligence: A Survey of Needs, Techniques, Applications, and Future Direction`이므로 지정 논문 원문으로 취급하지 않는다.
- P05는 arXiv `2312.12936` metadata가 DOI `10.1145/3774643`을 포함하고, Crossref metadata도 동일 제목과 저자, ACM Computing Surveys online publication을 반환하므로 DOI 확인 상태로 갱신한다.
- ACM 원문 페이지는 네트워크 환경에서 Cloudflare challenge로 직접 열람이 제한될 수 있으므로, 최종 제출 전 브라우저에서 DOI landing page와 PDF 권한을 사람이 재확인한다.
