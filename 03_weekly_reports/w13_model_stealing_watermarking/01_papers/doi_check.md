# W13 DOI/URL 검증표

| ID | 논문 제목 | DOI/URL | 상태 | 공식 확인 메모 | 남은 검토 사항 |
|---|---|---|---|---|---|
| P01 | I Know What You Trained Last Summer: A Survey on Stealing Machine Learning Models and Defences | `https://doi.org/10.1145/3595292`, ACM: `https://dl.acm.org/doi/10.1145/3595292`, arXiv: `https://arxiv.org/abs/2206.08451` | 확인 완료 | ACM/Crossref 기준 ACM Computing Surveys 55(14s), 1-41, online 2023-07-17, print 2023-12-31. 제목은 `Defences` | 로컬 PDF의 ACM reference placeholder와 공식 권호/쪽 차이는 최종 원고에서 공식 메타데이터 우선 |
| P02 | 지정: A Survey of Watermarking and Fingerprinting Techniques for Deep Learning Models / 로컬: Watermarking Techniques for Large Language Models: A Survey | 로컬 PDF: `https://arxiv.org/abs/2409.00089`; 지정 후보 확인 필요 | 대체 PDF | 로컬 PDF는 Yuqing Liang et al. arXiv:2409.00089v1. 지정 제목/저자/연도와 동일하지 않음 | Y. Ye et al. 지정 논문 원문 또는 공식 페이지 확보 필요. Peigen Ye et al. ACM CSUR 2026 DOI `10.1145/3773028`은 후보일 뿐 지정 문헌으로 확정 금지 |
| P03 | A survey of Deep Neural Network watermarking techniques | `https://doi.org/10.1016/j.neucom.2021.07.051`, Elsevier linking page: `https://linkinghub.elsevier.com/retrieve/pii/S092523122101095X`, arXiv: `https://arxiv.org/abs/2103.09274` | 확인 완료 / 강의계획서 표기 차이 | Elsevier/Crossref 기준 Neurocomputing 461, 171-193, 2021, Yue Li, Hongxia Wang, Mauro Barni | 강의계획서의 `Feng Li et al.` 및 `Techniques and challenges` 표기가 동일 논문 오기인지 사람 검토 필요 |
| P04 | ModelShield: Adaptive and Robust Watermark Against Model Extraction Attack | `https://doi.org/10.1109/TIFS.2025.3530691`, IEEE: `https://ieeexplore.ieee.org/document/10843740/`, arXiv: `https://arxiv.org/abs/2405.02365` | 확인 완료 | IEEE TIFS Vol. 20, 1767-1782, 2025. arXiv v4는 2025-01-12, 제목·저자 일치 | 최종 제출 시 IEEE DOI를 우선 인용하고 arXiv는 preprint로 병기 |
| P05 | 지정 후보: Generative Adversarial Networks: A Survey on Attack and Defense Perspective / 로컬: Generative Adversarial Networks: A Survey Towards Private and Secure Applications | 지정 후보 DOI `https://doi.org/10.1145/3615336`, ACM: `https://dl.acm.org/doi/10.1145/3615336`, 로컬 arXiv: `https://arxiv.org/abs/2106.03785` | 지정 후보 확인 / 로컬 대체 PDF | Chenhan Zhang et al. 공식 ACM 논문은 ACM CSUR 56(4), 1-35, online 2023-11-10, print 2024-04-30. 로컬 PDF는 Zhipeng Cai et al.로 불일치 | 강의계획서의 `Cheng Zhang` 표기와 공식 `Chenhan Zhang` 차이 확인 필요. 로컬 Cai et al. PDF를 지정 논문처럼 인용 금지 |

## 검증 원칙

1. DOI는 추측해서 적지 않는다.
2. P02/P05의 `SUBSTITUTE` PDF는 지정 논문 원문처럼 인용하지 않는다.
3. P01/P03/P04/P05의 공식 DOI는 보고서 본문과 참고문헌에 반영하되, 강의계획서 표기 차이는 `확인 필요`로 남긴다.
4. 공개 GitHub 저장소에는 PDF 원문 대신 DOI/URL과 요약을 남기는 방식을 권장한다.

<!-- AUTO-RELATED-PAPER-REFLECTION:start -->
## 논문/관련 논문 최종 판정 반영표

아래 표는 공식 DOI/arXiv 재검색 결과를 반영한 최종 판정이다. `논문 / 확인`은 공식 서지 기준으로 논문 인용, `관련 논문 / 확인`은 주차 주제 보강용 관련 논문 인용을 뜻한다.

| ID | 구분 | 상태 | 공식 확인 기준 | 보고서 반영 |
|---|---|---|---|---|
| P02 | 관련 논문 / 확인 | 공식 DOI 확인 | `https://doi.org/10.1145/3773028`; Securing Large Language Models: A Survey of Watermarking and Fingerprinting Techniques; ACM Computing Surveys; 2026 | 주차 주제 보강용 관련 논문으로 인용 |
| P03 | 논문 / 확인 | 공식 DOI 확인 | `https://doi.org/10.1016/j.neucom.2021.07.051`; A survey of Deep Neural Network watermarking techniques; Neurocomputing; 2021 | 공식 서지 기준으로 논문 인용 |
| P05 | 논문 / 확인 | 공식 DOI 확인 | `https://doi.org/10.1145/3615336`; Generative Adversarial Networks: A Survey on Attack and Defense Perspective; ACM Computing Surveys; 2023 | 공식 서지 기준으로 논문 인용 |
<!-- AUTO-RELATED-PAPER-REFLECTION:end -->
