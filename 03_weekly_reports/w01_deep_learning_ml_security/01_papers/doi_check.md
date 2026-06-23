# W01 DOI/URL 검증표

> 최종 판정 우선: 이 문서의 현재 상태는 `논문/관련 논문 최종 반영표`를 우선한다. 상단의 제목·저자·로컬 PDF 차이 메모는 오류 판정이 아니라 검증 이력이며, `관련 논문 / 확인`은 주차 주제에 맞는 공식 확인 논문으로 사용한다.


| ID | 논문 제목 | DOI | URL | 상태 | 검증 근거 |
|---|---|---|---|---|---|
| P01 | Deep learning | 10.1038/nature14539 | https://doi.org/10.1038/nature14539 | 확인 | Nature DOI 랜딩 페이지에서 제목, 저자, 권호, 페이지 확인 |
| P02 | Assuring the Machine Learning Lifecycle: Desiderata, Methods, and Challenges | 10.1145/3453444 | https://doi.org/10.1145/3453444 | 공식 DOI 확인 | 로컬 accepted version PDF 내부 DOI 확인. 최종 제출 전 출판사 landing page에서 권호/쪽 표기만 재확인 |
| P03 | A Survey of Data Mining and Machine Learning Methods for Cyber Security Intrusion Detection | 10.1109/COMST.2015.2494502 | https://doi.org/10.1109/COMST.2015.2494502 | 확인 | 로컬 PDF XMP 메타데이터에 IEEE COMST, 18(2), 1153-1176 및 DOI 확인 |
| P04 | Adversarial Attacks and Defenses in Machine Learning-Powered Networks: A Contemporary Survey | 10.48550/arXiv.2303.06302 | https://arxiv.org/abs/2303.06302 | arXiv 확인, 강의계획서 지정 논문 동일 여부 추가 확인 메모 | arXiv 제목, 저자, 제출일, arXiv DOI 확인. IEEE COMST 25(4), 2245-2298 논문과 동일 여부는 최종 DOI 보류 |
| P05 | A Survey of Privacy Attacks in Machine Learning | 10.1145/3624010 | https://doi.org/10.1145/3624010 | 공식 DOI 확인 | 로컬 arXiv v3/ACM 양식 PDF 확인. 최종 제출 전 출판사 landing page에서 권호/쪽 표기만 재확인 |

## 검증 원칙

1. DOI는 출판사 페이지, arXiv DOI, 또는 로컬 PDF 메타데이터로 확인되는 경우에만 적는다.
2. 프롬프트 제목과 원문 제목이 다를 경우 원문 제목을 우선하고, 차이는 검수 메모에 남긴다.
3. 실험값, 데이터셋별 수치, 인용 횟수는 이번 주차 보고서에서 새로 만들지 않는다.
4. 최종 논문 작성 시에는 참고문헌 형식을 학과 또는 제출 저널 양식에 맞춰 다시 정리한다.
5. 공개 GitHub 저장소에는 출판사 PDF 원문 대신 DOI/URL, 서지정보, 요약을 남기는 것을 원칙으로 한다.

## P04 동일 여부 검증 메모

- 강의계획서 지정 정보: Y. Wang et al., "Adversarial Attacks and Defenses in Machine Learning: A Survey", IEEE Communications Surveys & Tutorials, 25(4), 2023, pp. 2245-2298.
- 현재 W01 P04 정보: Yulong Wang et al., "Adversarial Attacks and Defenses in Machine Learning-Powered Networks: A Contemporary Survey", arXiv:2303.06302, DOI 10.48550/arXiv.2303.06302.
- 로컬 P04 PDF 첫 페이지와 arXiv 페이지는 현재 W01 P04 제목, 저자, arXiv 번호를 확인시켜 준다.
- IEEE COMST 최종 출판 정보, DOI, 권호, 페이지는 현재 로컬 PDF와 접근 가능한 공개 페이지에서 확인하지 못했으므로 `추가 확인 메모`로 남긴다.

<!-- AUTO-RELATED-PAPER-REFLECTION:start -->
## 논문/관련 논문 최종 판정 반영표

아래 표는 공식 DOI/arXiv 재검색 결과를 반영한 최종 판정이다. `논문 / 확인`은 공식 서지 기준으로 논문 인용, `관련 논문 / 확인`은 주차 주제 보강용 관련 논문 인용을 뜻한다.

| ID | 구분 | 상태 | 공식 확인 기준 | 보고서 반영 |
|---|---|---|---|---|
| P02 | 논문 / 확인 | 공식 DOI 확인 | `https://doi.org/10.1145/3453444`; Assuring the Machine Learning Lifecycle: Desiderata, Methods, and Challenges; ACM Computing Surveys; 2021 | 공식 서지 기준으로 논문 인용 |
| P04 | 관련 논문 / 확인 | 공식 arXiv 확인 | `https://arxiv.org/abs/2303.06302`; Adversarial Attacks and Defenses in Machine Learning-Powered Networks: A Contemporary Survey; arXiv; 2023 | 주차 주제 보강용 관련 논문으로 인용 |
| P05 | 논문 / 확인 | 공식 DOI 확인 | `https://doi.org/10.1145/3624010`; A Survey of Privacy Attacks in Machine Learning; ACM Computing Surveys; 2023 | 공식 서지 기준으로 논문 인용 |
<!-- AUTO-RELATED-PAPER-REFLECTION:end -->
