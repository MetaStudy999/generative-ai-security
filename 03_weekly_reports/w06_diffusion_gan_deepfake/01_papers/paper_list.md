# W06 논문 목록

> 최종 판정 우선: 이 문서의 현재 상태는 `논문/관련 논문 최종 반영표`를 우선한다. 상단의 제목·저자·로컬 PDF 차이 메모는 오류 판정이 아니라 검증 이력이며, `관련 논문 / 확인`은 주차 주제에 맞는 공식 확인 논문으로 사용한다.


| ID | 논문 제목 | 저자 | 출판 정보 | DOI/URL | 로컬 PDF | 검증 상태 |
|---|---|---|---|---|---|---|
| P01 | Diffusion Models: A Comprehensive Survey of Methods and Applications | Ling Yang, Zhilong Zhang, Yang Song, Shenda Hong, Runsheng Xu, Yue Zhao, Wentao Zhang, Bin Cui, Ming-Hsuan Yang | ACM Computing Surveys, Vol. 56, No. 4, Article 105, online 2023-11-09, print issue 2024-04-30 | DOI `10.1145/3626235`, arXiv `2209.00796` | `01_Yang_et_al_2023_Diffusion_Models_Comprehensive_Survey.pdf` | DOI/URL 확인 |
| P02 | A Survey on Video Diffusion Models | Zhen Xing, Qijun Feng, Haoran Chen, Qi Dai, Han Hu, Hang Xu, Zuxuan Wu, Yu-Gang Jiang | ACM Computing Surveys, Vol. 57, No. 2, pages 1-42, online 2024-11-07, print issue 2025-02-28 | DOI `10.1145/3696415`, arXiv `2310.10647` | `02_Xing_et_al_2024_Video_Diffusion_Models_Survey.pdf` | 출판 DOI 확인, 강의계획서 지정 P02 동일 여부와 Article 번호 추가 확인 메모 |
| P03 | Generative Adversarial Networks in Computer Vision: A Survey and Taxonomy | Zhengwei Wang, Qi She, Tomas E. Ward | ACM Computing Surveys, Vol. 54, No. 2, Article 37, published 2021-02-09, print issue 2022-03-31 | DOI `10.1145/3439723`, arXiv `1906.01529` | `03_Wang_She_Ward_2021_GANs_Computer_Vision_Survey.pdf` | 출판 DOI 확인, 강의계획서 저자명과 차이 추가 확인 메모 |
| P04 | The Creation and Detection of Deepfakes: A Survey | Yisroel Mirsky, Wenke Lee | ACM Computing Surveys, Vol. 54, No. 1, pages 1-41, online 2021-01-02, print issue 2022-01-31 | DOI `10.1145/3425780`, arXiv `2004.11138` | `04_Mirsky_Lee_2021_Creation_Detection_Deepfakes.pdf` | DOI/URL 확인, Article 번호 추가 확인 메모 |
| P05 | Deepfake Detection: A Comprehensive Survey from the Reliability Perspective | Tianyi Wang, Xin Liao, Kam Pui Chow, Xiaodong Lin, Yinglong Wang | ACM Computing Surveys, Vol. 57, No. 3, pages 1-35, online 2024-11-11, print issue 2025-03-31 | DOI `10.1145/3699710`, arXiv `2211.10881` | `05_Wang_et_al_2024_Deepfake_Detection_Reliability_Survey.pdf` | DOI/URL 확인, Article 번호 추가 확인 메모 |

## 검수 메모

- P01은 로컬 PDF 첫 페이지에서 ACM Computing Surveys Vol. 56, No. 4, Article 105와 DOI `10.1145/3626235`를 확인했다.
- P02는 로컬 PDF/arXiv 제목과 저자가 `Zhen Xing et al., A Survey on Video Diffusion Models`이며, Crossref 기준 ACM DOI `10.1145/3696415`가 확인된다. 다만 Article 번호는 확인하지 못했고, 강의계획서 지정 항목 `Ananya Högele et al., "Video Diffusion Models: A Survey"`와 제목·저자 표기가 달라 최종 제출 전 교수자 확인이 필요하다.
- P03은 로컬 PDF/arXiv/ACM DOI 페이지 기준 `Zhengwei Wang, Qi She, Tomas E. Ward` 논문이며 ACM DOI `10.1145/3439723`, Article 37이 확인된다. 강의계획서의 `Tianqi Wang et al.` 표기와 달라 동일성 검토 메모를 유지한다.
- P04는 DOI `10.1145/3425780`이 확인되지만 로컬 PDF는 arXiv/ACM 양식 preprint로 DOI placeholder가 남아 있다. 참고문헌에는 ACM DOI를 우선 사용한다.
- P05는 출판사 기준 저자명이 `Tianyi Wang et al.`이며 강의계획서의 `J. Wang et al.` 표기는 축약 또는 오기 가능성이 있어 추가 확인 메모로 남긴다.
- `01_papers/pdf/` 아래 PDF 원문 5개는 git 추적 대상이다. public GitHub 저장소에서는 저작권 위험이 있으므로 DOI/URL과 요약만 남기고 PDF 원문 삭제를 사람이 별도 검토해야 한다.

<!-- AUTO-RELATED-PAPER-REFLECTION:start -->
## 논문/관련 논문 최종 반영표

아래 표는 공식 DOI/arXiv 재검색 결과를 주차 보고서에 반영하기 위한 최종 판정이다. 기존 대조 기록은 보존하고, 보고서 본문과 참고문헌에서는 이 표의 `구분`과 `검증 상태`를 우선 사용한다.

| ID | 구분 | 논문 제목 | 논문 | 저자 | 연도 | 학술지/학회 | 학술지/출처 | DOI/URL | 검증 상태 | 보고서 반영 |
|---|---|---|---|---|---:|---|---|---|---|---|
| P02 | 논문 / 확인 | A Survey on Video Diffusion Models | A Survey on Video Diffusion Models | Zhen Xing et al. | 2024 | ACM Computing Surveys | ACM Computing Surveys | `https://doi.org/10.1145/3696415` | 공식 DOI 확인 | 공식 서지 기준으로 논문 인용 |
| P03 | 논문 / 확인 | Generative Adversarial Networks in Computer Vision | Generative Adversarial Networks in Computer Vision | Zhengwei Wang, Qi She, Tomas E. Ward | 2021 | ACM Computing Surveys | ACM Computing Surveys | `https://doi.org/10.1145/3439723` | 공식 DOI 확인 | 공식 서지 기준으로 논문 인용 |
| P04 | 논문 / 확인 | The Creation and Detection of Deepfakes | The Creation and Detection of Deepfakes | Yisroel Mirsky, Wenke Lee | 2021 | ACM Computing Surveys | ACM Computing Surveys | `https://doi.org/10.1145/3425780` | 공식 DOI 확인 | 공식 서지 기준으로 논문 인용 |
| P05 | 논문 / 확인 | Deepfake Detection: A Comprehensive Survey from the Reliability Perspective | Deepfake Detection: A Comprehensive Survey from the Reliability Perspective | Tianyi Wang et al. | 2024 | ACM Computing Surveys | ACM Computing Surveys | `https://doi.org/10.1145/3699710` | 공식 DOI 확인 | 공식 서지 기준으로 논문 인용 |
<!-- AUTO-RELATED-PAPER-REFLECTION:end -->
