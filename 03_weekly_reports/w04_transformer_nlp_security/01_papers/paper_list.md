# W04 논문 목록

> 최종 판정 우선: 이 문서의 현재 상태는 `논문/관련 논문 최종 반영표`를 우선한다. 상단의 제목·저자·로컬 PDF 차이 메모는 오류 판정이 아니라 검증 이력이며, `관련 논문 / 확인`은 주차 주제에 맞는 공식 확인 논문으로 사용한다.


## 강의계획서 W04 논문 패킷 대조

| ID | 논문 제목 | 저자 | 출판 정보 | DOI/URL | 검증 상태 |
|---|---|---|---|---|---|
| P01 | Efficient Transformers: A Survey | Yi Tay, Mostafa Dehghani, Dara Bahri, Donald Metzler | ACM Computing Surveys, Vol. 55, No. 6, 2022, pp. 1-28 | ACM DOI `10.1145/3530811`; arXiv DOI `10.48550/arXiv.2009.06732`; https://arxiv.org/abs/2009.06732 | ACM CSUR 출판 DOI 확인. Article 번호는 Crossref/BibTeX 응답에 미제공되어 추가 확인 메모 |
| P02 | A Practical Survey on Faster and Lighter Transformers | Quentin Fournier, Gaetan Marceau Caron, Daniel Aloise | ACM Computing Surveys, Vol. 55, No. 14s, 2023, pp. 1-40 | ACM DOI `10.1145/3586074`; https://arxiv.org/abs/2103.14636 | ACM CSUR 출판 DOI 확인. Article 번호는 Crossref/BibTeX 응답에 미제공되어 추가 확인 메모 |
| P03 | A survey of transformers | Tianyang Lin, Yuxin Wang, Xiangyang Liu, Xipeng Qiu | AI Open, Vol. 3, 2022, pp. 111-132 | DOI `10.1016/j.aiopen.2022.10.001`; https://www.sciencedirect.com/science/article/pii/S2666651022000146 | AI Open 출판 DOI/권호/쪽 확인 |
| P04 | A Survey of Adversarial Defenses and Robustness in NLP | Shreya Goyal, Sumanth Doddapaneni, Mitesh M. Khapra, Balaraman Ravindran | ACM Computing Surveys, Vol. 55, No. 14s, 2023, pp. 1-39 | ACM DOI `10.1145/3593042`; arXiv DOI `10.48550/arXiv.2203.06414`; https://arxiv.org/abs/2203.06414 | ACM CSUR 출판 DOI 확인. Article 번호는 Crossref/BibTeX 응답에 미제공되어 추가 확인 메모 |
| P05 | Privacy Preserving Prompt Engineering: A Survey | Kennedy Edemacu, Xintao Wu | ACM Computing Surveys, Vol. 57, No. 10, 2025, pp. 1-36 | ACM DOI `10.1145/3729219`; arXiv DOI `10.48550/arXiv.2404.06001`; https://arxiv.org/abs/2404.06001 | ACM CSUR 2025 출판 DOI 확인. Article 번호는 Crossref/BibTeX 응답에 미제공되어 추가 확인 메모 |

## 판본 차이 메모

- P01은 arXiv 최초 공개가 2020년이고 arXiv v3는 2022년 갱신판이다. ACM CSUR 판은 같은 제목과 저자이며 2022년 12월 온라인 출판, 2023년 6월 print issue로 기록된다.
- P02는 arXiv 최초 공개가 2021년이고 arXiv v2에 ACM DOI가 연결되어 있다. 최종 제출 참고문헌은 ACM CSUR 판을 우선 사용한다.
- P03은 ScienceDirect/AI Open 기준 Vol. 3, 2022, pp. 111-132와 DOI가 확인되었다.
- P04는 arXiv 제목이 `A Survey of Adversarial Defences and Robustness in NLP`이고 ACM/Crossref 제목은 `A Survey of Adversarial Defenses and Robustness in NLP`이다. 강의계획서의 `N. Goyal et al.` 표기는 Crossref/arXiv의 첫 저자 `Shreya Goyal`과 일치하지 않으므로 사람 검토가 필요하다.
- P05는 arXiv 기준 2024년 공개판이고 ACM CSUR 판은 2025년 온라인 출판판으로 확인되었다. 제목과 저자는 동일하게 확인된다.

## 로컬 PDF 및 저작권 메모

`01_papers/pdf/` 아래 PDF 5개가 Git 추적 대상으로 확인되었다. 공개 GitHub 저장소에서는 출판사 PDF 원문 대신 DOI/URL, 서지정보, 요약만 남기는 것이 안전하다. 사용자의 명시 승인 없이 PDF를 삭제하지 않았으며, 이미 추적 중인 PDF는 제출 전 삭제 또는 비공개 저장소 전환 검토가 필요하다.

<!-- AUTO-RELATED-PAPER-REFLECTION:start -->
## 논문/관련 논문 최종 반영표

아래 표는 공식 DOI/arXiv 재검색 결과를 주차 보고서에 반영하기 위한 최종 판정이다. 기존 대조 기록은 보존하고, 보고서 본문과 참고문헌에서는 이 표의 `구분`과 `검증 상태`를 우선 사용한다.

| ID | 구분 | 논문 제목 | 논문 | 저자 | 연도 | 학술지/학회 | 학술지/출처 | DOI/URL | 검증 상태 | 보고서 반영 |
|---|---|---|---|---|---:|---|---|---|---|---|
| P01 | 논문 / 확인 | Efficient Transformers: A Survey | Efficient Transformers: A Survey | Yi Tay, Mostafa Dehghani, Dara Bahri, Donald Metzler | 2022 | ACM Computing Surveys | ACM Computing Surveys | `https://doi.org/10.1145/3530811` | 공식 DOI 확인 | 공식 서지 기준으로 논문 인용 |
| P02 | 논문 / 확인 | A Practical Survey on Faster and Lighter Transformers | A Practical Survey on Faster and Lighter Transformers | Quentin Fournier, Gaetan Marceau Caron, Daniel Aloise | 2023 | ACM Computing Surveys | ACM Computing Surveys | `https://doi.org/10.1145/3586074` | 공식 DOI 확인 | 공식 서지 기준으로 논문 인용 |
| P04 | 논문 / 확인 | A Survey of Adversarial Defenses and Robustness in NLP | A Survey of Adversarial Defenses and Robustness in NLP | Shreya Goyal et al. | 2023 | ACM Computing Surveys | ACM Computing Surveys | `https://doi.org/10.1145/3593042` | 공식 DOI 확인 | 공식 서지 기준으로 논문 인용 |
| P05 | 논문 / 확인 | Privacy Preserving Prompt Engineering: A Survey | Privacy Preserving Prompt Engineering: A Survey | Kennedy Edemacu, Xintao Wu | 2025 | ACM Computing Surveys | ACM Computing Surveys | `https://doi.org/10.1145/3729219` | 공식 DOI 확인 | 공식 서지 기준으로 논문 인용 |
<!-- AUTO-RELATED-PAPER-REFLECTION:end -->
