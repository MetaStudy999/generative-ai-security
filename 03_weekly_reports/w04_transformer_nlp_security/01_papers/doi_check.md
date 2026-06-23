# W04 DOI/URL 검증표

검증일: 2026-06-22
검증 근거: Crossref DOI API, DOI BibTeX content negotiation, arXiv API, ScienceDirect/AI Open 페이지

| ID | 논문 제목 | DOI/URL | 상태 | 남은 검토 사항 |
|---|---|---|---|---|
| P01 | Efficient Transformers: A Survey | ACM DOI `10.1145/3530811`; arXiv DOI `10.48550/arXiv.2009.06732`; https://doi.org/10.1145/3530811; https://arxiv.org/abs/2009.06732 | ACM CSUR 출판 DOI 확인 | ACM Article 번호는 Crossref/BibTeX에 미제공. 필요 시 ACM 페이지에서 사람 확인 |
| P02 | A Practical Survey on Faster and Lighter Transformers | ACM DOI `10.1145/3586074`; https://doi.org/10.1145/3586074; https://arxiv.org/abs/2103.14636 | ACM CSUR 출판 DOI 확인 | ACM Article 번호는 Crossref/BibTeX에 미제공. 필요 시 ACM 페이지에서 사람 확인 |
| P03 | A survey of transformers | DOI `10.1016/j.aiopen.2022.10.001`; https://www.sciencedirect.com/science/article/pii/S2666651022000146 | AI Open DOI/URL/권호/쪽 확인 | 없음. 최종 제출 전 저널 스타일에 맞춰 대소문자만 재점검 |
| P04 | A Survey of Adversarial Defenses and Robustness in NLP | ACM DOI `10.1145/3593042`; arXiv DOI `10.48550/arXiv.2203.06414`; https://doi.org/10.1145/3593042; https://arxiv.org/abs/2203.06414 | ACM CSUR 출판 DOI 확인 | `Defences`/`Defenses`, `of`/`on`, `N. Goyal` 표기는 강의자료와 원문 간 차이로 사람 검토 필요 |
| P05 | Privacy Preserving Prompt Engineering: A Survey | ACM DOI `10.1145/3729219`; arXiv DOI `10.48550/arXiv.2404.06001`; https://doi.org/10.1145/3729219; https://arxiv.org/abs/2404.06001 | ACM CSUR 2025 출판 DOI 확인 | ACM Article 번호는 Crossref/BibTeX에 미제공. 필요 시 ACM 페이지에서 사람 확인 |

## 세부 검증 메모

- P01 Crossref: ACM Computing Surveys, Vol. 55, No. 6, online published 2022-12-07, pp. 1-28.
- P02 Crossref: ACM Computing Surveys, Vol. 55, No. 14s, online published 2023-07-17, pp. 1-40.
- P03 ScienceDirect/Crossref: AI Open, Vol. 3, 2022, pp. 111-132.
- P04 Crossref: ACM Computing Surveys, Vol. 55, No. 14s, online published 2023-07-17, pp. 1-39.
- P05 Crossref: ACM Computing Surveys, Vol. 57, No. 10, online published 2025-05-06, pp. 1-36.

## 검증 원칙

1. DOI는 추측해서 적지 않고, 출판 DOI와 arXiv DOI를 구분한다.
2. ACM Article 번호처럼 확인되지 않은 필드는 `확인 필요`로 남긴다.
3. 최종 제출 전 사람 검토자가 제목 표기, 저자명, 권호, 쪽, DOI 링크를 한 번 더 대조한다.
4. 로컬 PDF는 인용 근거가 아니라 독해 편의 자료이며, 공개 저장소 배포 가능성은 별도로 판단한다.

<!-- AUTO-RELATED-PAPER-REFLECTION:start -->
## 논문/관련 논문 최종 판정 반영표

아래 표는 공식 DOI/arXiv 재검색 결과를 반영한 최종 판정이다. `논문 / 확인`은 공식 서지 기준으로 논문 인용, `관련 논문 / 확인`은 주차 주제 보강용 관련 논문 인용을 뜻한다.

| ID | 구분 | 상태 | 공식 확인 기준 | 보고서 반영 |
|---|---|---|---|---|
| P01 | 논문 / 확인 | 공식 DOI 확인 | `https://doi.org/10.1145/3530811`; Efficient Transformers: A Survey; ACM Computing Surveys; 2022 | 공식 서지 기준으로 논문 인용 |
| P02 | 논문 / 확인 | 공식 DOI 확인 | `https://doi.org/10.1145/3586074`; A Practical Survey on Faster and Lighter Transformers; ACM Computing Surveys; 2023 | 공식 서지 기준으로 논문 인용 |
| P04 | 논문 / 확인 | 공식 DOI 확인 | `https://doi.org/10.1145/3593042`; A Survey of Adversarial Defenses and Robustness in NLP; ACM Computing Surveys; 2023 | 공식 서지 기준으로 논문 인용 |
| P05 | 논문 / 확인 | 공식 DOI 확인 | `https://doi.org/10.1145/3729219`; Privacy Preserving Prompt Engineering: A Survey; ACM Computing Surveys; 2025 | 공식 서지 기준으로 논문 인용 |
<!-- AUTO-RELATED-PAPER-REFLECTION:end -->
