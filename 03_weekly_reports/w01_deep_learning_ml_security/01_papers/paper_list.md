# W01 논문 목록

> 최종 판정 우선: 이 문서의 현재 상태는 `논문/관련 논문 최종 반영표`를 우선한다. 상단의 제목·저자·로컬 PDF 차이 메모는 오류 판정이 아니라 검증 이력이며, `관련 논문 / 확인`은 주차 주제에 맞는 공식 확인 논문으로 사용한다.


| ID | 논문 제목 | 저자 | 연도 | 학술지/학회 | DOI/URL | 로컬 PDF | 검증 상태 |
|---|---|---:|---:|---|---|---|---|
| P01 | Deep learning | Yann LeCun, Yoshua Bengio, Geoffrey Hinton | 2015 | Nature | https://doi.org/10.1038/nature14539 | 01_LeCun_Bengio_Hinton_2015_Deep_Learning.pdf | DOI/출판정보 확인 |
| P02 | Assuring the Machine Learning Lifecycle: Desiderata, Methods, and Challenges | Rob Ashmore, Radu Calinescu, Colin Paterson | 2021 | ACM Computing Surveys | https://doi.org/10.1145/3453444 | 02_Ashmore_Calinescu_Paterson_2021_Assuring_ML_Lifecycle.pdf | DOI는 PDF 메타데이터와 DOI 링크로 확인 |
| P03 | A Survey of Data Mining and Machine Learning Methods for Cyber Security Intrusion Detection | Anna L. Buczak, Erhan Guven | 2016 | IEEE Communications Surveys & Tutorials | https://doi.org/10.1109/COMST.2015.2494502 | 03_Buczak_Guven_2016_ML_Methods_for_Cyber_Security_Intrusion_Detection.pdf | DOI는 PDF 메타데이터로 확인 |
| P04 | Adversarial Attacks and Defenses in Machine Learning-Powered Networks: A Contemporary Survey | Yulong Wang, Tong Sun, Shenghong Li, Xin Yuan, Wei Ni, Ekram Hossain, H. Vincent Poor | 2023 | arXiv preprint | https://doi.org/10.48550/arXiv.2303.06302 | 04_Wang_et_al_2023_Adversarial_Attacks_and_Defenses.pdf | arXiv DOI 확인. 강의계획서 지정 IEEE COMST 논문과 동일 여부 추가 확인 메모 |
| P05 | A Survey of Privacy Attacks in Machine Learning | Maria Rigaki, Sebastian Garcia | 2023 | ACM Computing Surveys | https://doi.org/10.1145/3624010 | 05_Rigaki_Garcia_2023_Survey_of_Privacy_Attacks_in_ML.pdf | arXiv와 관련 DOI 확인 |

## 논문 패킷 역할

| ID | W01에서의 역할 | 기말논문 연결 |
|---|---|---|
| P01 | 딥러닝의 표현학습, 역전파, CNN/RNN 계열의 기본 원리를 제공한다. | AI 원리와 보안 취약성의 기술적 배경 |
| P02 | ML 생명주기를 데이터 관리, 모델 학습, 검증, 배포 단계로 나누고 보증 증거를 정리한다. | 위협모형과 평가 프로토콜의 뼈대 |
| P03 | 침입탐지에서 ML/데이터마이닝 기법이 어떻게 적용되는지 분류한다. | 보안 데이터셋, 탐지 성능, 오탐/미탐 지표 |
| P04 | 대적 공격과 방어를 공격 원리, 방어 방식, 한계 관점에서 정리한다. | robustness 평가와 공격-방어 분류체계 |
| P05 | ML 프라이버시 공격을 공격자 지식, 공격 대상 자산, 방어책으로 분류한다. | membership/property/model leakage 평가축 |

## 검수 메모

- P04는 프롬프트의 축약 제목과 로컬 파일명이 실제 arXiv 제목보다 짧다. 본 보고서에서는 arXiv 제목을 기준으로 정리했다.
- 주의: 본 W01 보고서의 P04는 강의계획서 지정 IEEE Communications Surveys & Tutorials 논문과 동일 여부를 최종 확인하지 못했거나, 대체 arXiv 논문으로 정리되었다. 최종 제출 전 강의계획서 지정 논문으로 교체하거나, 대체 논문 사용 사유를 교수자에게 설명해야 한다.
- DOI/URL은 확인 가능한 범위에서만 입력했다. 출판사 페이지 접근이 제한된 항목은 로컬 PDF 메타데이터 또는 arXiv의 DOI 정보를 검증 근거로 남겼다.
- `RELATED`가 포함된 PDF는 W01 폴더에는 없다.
- PDF 원문 5개가 Git 추적 대상에 포함되어 있어 공개 저장소에서는 저작권 위험이 있다. 공개 제출 전 DOI/URL과 서지정보만 남기고 PDF 삭제 또는 비공개 보관을 검토해야 한다.

<!-- AUTO-RELATED-PAPER-REFLECTION:start -->
## 논문/관련 논문 최종 반영표

아래 표는 공식 DOI/arXiv 재검색 결과를 주차 보고서에 반영하기 위한 최종 판정이다. 기존 대조 기록은 보존하고, 보고서 본문과 참고문헌에서는 이 표의 `구분`과 `검증 상태`를 우선 사용한다.

| ID | 구분 | 논문 제목 | 논문 | 저자 | 연도 | 학술지/학회 | 학술지/출처 | DOI/URL | 검증 상태 | 보고서 반영 |
|---|---|---|---|---|---:|---|---|---|---|---|
| P02 | 논문 / 확인 | Assuring the Machine Learning Lifecycle: Desiderata, Methods, and Challenges | Assuring the Machine Learning Lifecycle: Desiderata, Methods, and Challenges | Rob Ashmore, Radu Calinescu, Colin Paterson | 2021 | ACM Computing Surveys | ACM Computing Surveys | `https://doi.org/10.1145/3453444` | 공식 DOI 확인 | 공식 서지 기준으로 논문 인용 |
| P04 | 관련 논문 / 확인 | Adversarial Attacks and Defenses in Machine Learning-Powered Networks: A Contemporary Survey | Adversarial Attacks and Defenses in Machine Learning-Powered Networks: A Contemporary Survey | Yulong Wang et al. | 2023 | arXiv | arXiv | `https://arxiv.org/abs/2303.06302` | 공식 arXiv 확인 | 주차 주제 보강용 관련 논문으로 인용 |
| P05 | 논문 / 확인 | A Survey of Privacy Attacks in Machine Learning | A Survey of Privacy Attacks in Machine Learning | Maria Rigaki, Sebastian Garcia | 2023 | ACM Computing Surveys | ACM Computing Surveys | `https://doi.org/10.1145/3624010` | 공식 DOI 확인 | 공식 서지 기준으로 논문 인용 |
<!-- AUTO-RELATED-PAPER-REFLECTION:end -->
