# W09 논문 목록

> 검증 기준: 로컬 PDF 첫 페이지, `pdftotext` 추출 결과, DOI/Crossref 메타데이터를 함께 대조했다. 강의계획서 표기와 충돌하는 저자명은 임의로 확정하지 않고 `확인 필요`로 남긴다.

| ID | 강의계획서 지정 | 현재 로컬 PDF/DOI 기준 문헌 | 공식 출판정보 | DOI/URL | 로컬 PDF | 검증 상태 |
|---|---|---|---|---|---|---|
| P01 | Kai Arulkumaran et al., "Deep Reinforcement Learning: A Brief Survey", IEEE Signal Processing Magazine, 2017 | Kai Arulkumaran; Marc Peter Deisenroth; Miles Brundage; Anil Anthony Bharath, "A Brief Survey of Deep Reinforcement Learning" | IEEE Signal Processing Magazine, Vol. 34, No. 6, pp. 26-38, Nov. 2017 | https://doi.org/10.1109/MSP.2017.2743240 | `01_Arulkumaran_et_al_2017_Deep_Reinforcement_Learning_Survey.pdf` | 부분 검증: 공식 출판판 제목은 `Deep Reinforcement Learning: A Brief Survey`, 로컬 PDF는 arXiv extended version 제목 `A Brief Survey of Deep Reinforcement Learning` |
| P02 | B. R. Kiran et al., "Deep Reinforcement Learning for Autonomous Driving: A Survey", IEEE TITS, 2022 | B. Ravi Kiran; Ibrahim Sobh; Victor Talpaert; Patrick Mannion; Ahmad A. Al Sallab; Senthil Yogamani; Patrick Perez | IEEE Transactions on Intelligent Transportation Systems, Vol. 23, No. 6, pp. 4909-4926, Jun. 2022 | https://doi.org/10.1109/TITS.2021.3054625 | `02_Kiran_et_al_2022_DRL_Autonomous_Driving_Survey.pdf` | 부분 검증: DOI는 2021년에 등록/early access, 출판판은 2022년; 로컬 PDF는 arXiv v2 |
| P03 | Ngoc-Tinh Nguyen et al., "Deep Reinforcement Learning for Cyber Security", IEEE TNNLS, 2023 | Thanh Thi Nguyen; Vijay Janapa Reddi, "Deep Reinforcement Learning for Cyber Security" | IEEE Transactions on Neural Networks and Learning Systems, Vol. 34, No. 8, pp. 3779-3795, Aug. 2023 | https://doi.org/10.1109/TNNLS.2021.3121870 | `03_Nguyen_Reddi_2023_DRL_for_Cyber_Security.pdf` | 확인 필요: 제목/학술지/연도는 일치하지만 강의계획서 저자명 `Ngoc-Tinh Nguyen`과 DOI/PDF 저자명 `Thanh Thi Nguyen`이 다름 |
| P04 | Aditya Adawadkar et al., "Cyber-security and reinforcement learning -- A brief survey", Engineering Applications of Artificial Intelligence, 2022 | Amrin Maria Khan Adawadkar; Nilima Kulkarni, "Cyber-security and reinforcement learning - A brief survey" | Engineering Applications of Artificial Intelligence, Vol. 114, Article 105116, Sep. 2022 | https://doi.org/10.1016/j.engappai.2022.105116 | `04_Adawadkar_Kulkarni_2022_Cybersecurity_RL_Survey.pdf` | 확인 필요: DOI/PDF 저자명은 `Amrin Maria Khan Adawadkar`; 강의계획서 `Aditya Adawadkar` 표기와 다름. 공식 제목은 em dash 표기 |
| P05 | H. Yan et al., "Deep Reinforcement Learning Verification: A Survey", ACM Computing Surveys, 2023 | Matthew Landers; Afsaneh Doryab, "Deep Reinforcement Learning Verification: A Survey" | ACM Computing Surveys, Vol. 55, No. 14s, Article 330, 31 pages, Jul. 2023 | https://doi.org/10.1145/3596444 | `05_Landers_Doryab_2023_DRL_Verification_Survey.pdf` | 확인 필요: 제목/학술지는 유사하나 강의계획서 저자명 `H. Yan et al.`과 DOI/PDF 저자명이 다름. 동일 논문 여부 미확정 |

## 검수 메모

- P01은 공식 DOI 메타데이터의 출판판 제목이 `Deep Reinforcement Learning: A Brief Survey`이고, 로컬 PDF 첫 페이지는 `IEEE Signal Processing Magazine ... (arXiv extended version)` 및 `A Brief Survey of Deep Reinforcement Learning`로 표시된다. 제출 참고문헌에는 공식 출판판 제목과 DOI를 우선 사용한다.
- P02는 로컬 PDF가 `arXiv:2002.00444v2 [cs.LG] 23 Jan 2021`로 표시되며, 공식 출판판은 IEEE TITS 23(6), 4909-4926, 2022이다. DOI 문자열의 `2021`은 등록/early access 시점으로 보며 최종 출판연도는 2022로 기록한다.
- P03은 DOI/PDF 기준 저자가 `Thanh Thi Nguyen; Vijay Janapa Reddi`이다. 강의계획서의 `Ngoc-Tinh Nguyen et al.` 표기는 확인 필요다.
- P04는 DOI/PDF 기준 저자가 `Amrin Maria Khan Adawadkar; Nilima Kulkarni`이다. 강의계획서의 `Aditya Adawadkar et al.` 표기는 확인 필요다.
- P05는 DOI/PDF 기준 저자가 `Matthew Landers; Afsaneh Doryab`이다. 강의계획서 지정 `H. Yan et al.`과 동일 논문인지 확인되지 않았으므로, 현재 문헌은 대체 문헌 가능성을 열어 둔다.
- 실험 수치는 문헌의 실험 결과가 아니라 W09 synthetic toy cyber-defense state/action/reward simulation에서 생성된 별도 결과다.
