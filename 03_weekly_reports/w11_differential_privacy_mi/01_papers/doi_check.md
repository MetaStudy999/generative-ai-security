# W11 DOI/URL 검증표

| ID | 문헌 | DOI/URL | 상태 | 남은 검토 사항 |
|---|---|---|---|---|
| P01 | A Critical Review on the Use (and Misuse) of Differential Privacy in Machine Learning | DOI `10.1145/3547139`; ACM primary URL `https://dl.acm.org/doi/10.1145/3547139`; arXiv `https://arxiv.org/abs/2206.04621` | DOI 확인 | 로컬 PDF는 arXiv v2이므로 ACM 최종본과 세부 문구 차이 검토 필요 |
| P02 | Recent Advances of Differential Privacy in Centralized Deep Learning: A Systematic Survey | DOI `10.1145/3712000`; ACM primary URL `https://dl.acm.org/doi/10.1145/3712000`; arXiv `https://arxiv.org/abs/2309.16398` | DOI 확인, 표기 불일치 있음 | 강의자료의 `Jonathan Demelius`, `57(9), Article 202` 표기는 Crossref 기준 `Lea Demelius`, `57(6), pp. 1-28`과 다르므로 최종 대조 필요 |
| P03 | Differential privacy in deep learning: A literature survey | DOI `10.1016/j.neucom.2024.127663`; Elsevier primary URL `https://linkinghub.elsevier.com/retrieve/pii/S092523122400434X` | DOI 확인, 로컬 PDF 불일치 | 공식 메타데이터는 `Ke Pan et al.`로 확인됨. 강의자료의 `Zizheng Pan et al.` 표기와 지정 원문 PDF 확보 필요 |
| P04 | Membership Inference Attacks on Machine Learning: A Survey | DOI `10.1145/3523273`; ACM primary URL `https://dl.acm.org/doi/10.1145/3523273`; arXiv `https://arxiv.org/abs/2103.07853` | DOI 확인 | 로컬 PDF는 arXiv/ACM preprint 판이므로 ACM 최종본과 세부 표기 검토 필요 |
| P05 | Defenses to Membership Inference Attacks: A Survey | DOI `10.1145/3620667`; ACM primary URL `https://dl.acm.org/doi/10.1145/3620667` | DOI 확인, 로컬 PDF 불일치, 표기 불일치 있음 | 공식 메타데이터는 `Li Hu et al.`, ACM CSUR 56(4), pp. 1-34로 확인됨. 강의자료의 `Hongsheng Hu et al.` 표기와 지정 원문 PDF 확보 필요 |

## 검증 근거

- 2026-06-23 Crossref API에서 DOI, publisher, venue, volume, issue, page, published-online/print, primary URL을 확인했다.
- P01, P02, P04는 로컬 PDF 첫 페이지와 arXiv 식별자를 함께 확인했다.
- P03 로컬 PDF는 `Differentially Private Federated Learning: A Systematic Review`로, 지정 Neurocomputing 논문과 다르다.
- P05 로컬 PDF는 `Membership Inference Attacks and Defenses in Federated Learning: A Survey`로, 지정 ACM Computing Surveys 논문과 다르다.

## 최종 제출 전 확인 순서

1. 강의계획서 원본의 P02, P03, P05 저자명/권호 표기를 교수자 자료와 다시 대조한다.
2. P03 Neurocomputing 지정 논문 원문 또는 공식 출판 페이지를 확보한다.
3. P05 ACM Computing Surveys 지정 논문 원문 또는 공식 출판 페이지를 확보한다.
4. public GitHub 저장소에는 PDF 원문 대신 DOI/URL, 서지정보, 요약만 남기는 방향을 검토한다.
