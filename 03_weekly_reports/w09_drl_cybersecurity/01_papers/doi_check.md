# W09 DOI/URL 검증표

> 검증일: 2026-06-23. 검증 근거는 로컬 PDF 첫 페이지, DOI/Crossref 메타데이터, 실행 로그다. 공식 출판사 페이지에서 전문 접근권과 PDF 재배포 가능 여부는 별도 확인이 필요하다.

| ID | 공식 제목 | DOI | 공식 출판정보 | 로컬 PDF 상태 | 상태 | 비고 |
|---|---|---|---|---|---|---|
| P01 | Deep Reinforcement Learning: A Brief Survey | https://doi.org/10.1109/MSP.2017.2743240 | IEEE Signal Processing Magazine, 34(6), 26-38, Nov. 2017 | arXiv extended version, 제목은 `A Brief Survey of Deep Reinforcement Learning` | 부분 검증 | 동일 저자·동일 주제의 확장본으로 판단하되, 참고문헌은 공식 출판판 제목/권호/쪽수 사용 |
| P02 | Deep Reinforcement Learning for Autonomous Driving: A Survey | https://doi.org/10.1109/TITS.2021.3054625 | IEEE Transactions on Intelligent Transportation Systems, 23(6), 4909-4926, Jun. 2022 | arXiv v2, 2021-01-23 | 부분 검증 | DOI 등록/early access는 2021, 최종 출판판은 2022 |
| P03 | Deep Reinforcement Learning for Cyber Security | https://doi.org/10.1109/TNNLS.2021.3121870 | IEEE Transactions on Neural Networks and Learning Systems, 34(8), 3779-3795, Aug. 2023 | IEEE early access/arXiv v4 표기 | 확인 필요 | DOI/PDF 저자 `Thanh Thi Nguyen; Vijay Janapa Reddi`와 강의계획서 `Ngoc-Tinh Nguyen et al.` 불일치 |
| P04 | Cyber-security and reinforcement learning -- A brief survey | https://doi.org/10.1016/j.engappai.2022.105116 | Engineering Applications of Artificial Intelligence, 114, Article 105116, Sep. 2022 | Elsevier 출판판 PDF | 확인 필요 | DOI/PDF 저자 `Amrin Maria Khan Adawadkar; Nilima Kulkarni`와 강의계획서 `Aditya Adawadkar et al.` 불일치. 제목은 공식 메타데이터에서 em dash 사용 |
| P05 | Deep Reinforcement Learning Verification: A Survey | https://doi.org/10.1145/3596444 | ACM Computing Surveys, 55(14s), Article 330, 31 pages, Jul. 2023 | ACM 출판판 PDF | 확인 필요 | DOI/PDF 저자 `Matthew Landers; Afsaneh Doryab`와 강의계획서 `H. Yan et al.` 불일치 |

## 강의계획서 패킷 대조

| ID | 동일 여부 판단 | 남은 확인 |
|---|---|---|
| P01 | 부분 검증: 공식 제목과 로컬 arXiv 제목은 다르지만 동일 저자·동일 DOI 연결 문헌으로 처리 가능 | arXiv extended version과 출판판의 세부 차이(그림/쪽수/부록)는 최종 제출 전 확인 필요 |
| P02 | 부분 검증: 로컬 arXiv v2와 IEEE TITS 출판판은 같은 제목/저자 흐름이나 출판판 정보가 우선 | arXiv v2와 최종 IEEE판의 세부 차이 확인 필요 |
| P03 | 확인 필요: 제목·학술지·연도는 강의계획서와 맞지만 첫 저자명이 다름 | `Ngoc-Tinh Nguyen` 표기가 오기인지 대체 문헌인지 교수자/강의자료 원본 확인 필요 |
| P04 | 확인 필요: 제목·학술지는 맞지만 첫 저자명이 다름 | `Aditya Adawadkar` 표기가 오기인지 대체 문헌인지 확인 필요 |
| P05 | 확인 필요: 제목·학술지는 맞지만 저자명이 완전히 다름 | `H. Yan et al.` 지정 논문과 Landers/Doryab 문헌의 동일 여부 확인 필요 |

주의: W09의 P05는 강의계획서 지정 저자명 `H. Yan et al.`과 현재 로컬 PDF 기준 `Matthew Landers; Afsaneh Doryab`가 다르므로, 동일 논문 여부와 최종 ACM 출판정보를 확인 필요 상태로 유지한다.

## PDF 보관 정책 점검

- `01_papers/pdf/` 아래 PDF 5개는 현재 `git ls-files` 기준 Git 추적 대상이다.
- `.gitignore`에는 `03_weekly_reports/**/01_papers/pdf/*.pdf` 규칙이 이미 존재하지만, 기존 추적 파일에는 적용되지 않는다.
- public GitHub 저장소에는 IEEE/ACM/Elsevier PDF 원문을 그대로 포함하지 않는 것이 안전하다.
- 사용자 명시 승인 없이 PDF를 삭제하지 않았다. public 배포 전 `git rm --cached` 또는 별도 비공개 보관 전환이 필요하다.

## 검증 원칙

1. DOI/URL은 임의 생성하지 않는다.
2. 로컬 PDF와 DOI 메타데이터가 다르면 공식 출판판 메타데이터를 우선하되, 로컬 PDF 차이를 비고에 남긴다.
3. 강의계획서 저자명과 DOI/PDF 저자명이 충돌하는 항목은 `확인 필요`로 유지한다.
4. 참고문헌 번호는 [1] P01, [2] P02, [3] P03, [4] P04, [5] P05에 대응시킨다.
