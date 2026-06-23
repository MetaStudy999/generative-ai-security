# W13 논문 목록

> 상태 기준: DOI/출판정보는 ACM, IEEE, Elsevier, arXiv, Crossref 등 공식 메타데이터로 확인된 경우만 확정했다. `SUBSTITUTE` PDF는 지정 논문 원문처럼 인용하지 않는다.

| ID | 강의계획서 지정 문헌 | 현재 로컬 PDF | 공식 확인 결과 | 검증 상태 | 제출 전 조치 |
|---|---|---|---|---|---|
| P01 | Daryna/Daria Oliynyk et al., "I Know What You Trained Last Summer: A Survey on Stealing Machine Learning Models and Defences", ACM Computing Surveys, 2023 | 동일 제목의 arXiv/ACM accepted manuscript PDF | DOI `10.1145/3595292`, ACM Computing Surveys, Vol. 55, Issue 14s, pp. 1-41, online 2023-07-17, print 2023-12-31. 제목은 `Defences` 표기 | 공식 DOI 확인 완료, 로컬 PDF는 VOR가 아닌 accepted/arXiv 계열 메타데이터 포함 | 최종 인용은 DOI/ACM 메타데이터 기준으로 정리 |
| P02 | Y. Ye et al., "A Survey of Watermarking and Fingerprinting Techniques for Deep Learning Models", ACM Computing Surveys, 2024 | `02_SUBSTITUTE_Liang_et_al_2024_LLM_Watermarking_Survey.pdf`: Yuqing Liang et al., "Watermarking Techniques for Large Language Models: A Survey", arXiv:2409.00089v1 | 지정 제목과 일치하는 2024 ACM CSUR 문헌은 현재 확인하지 못함. 제목/저자 유사 후보로 Peigen Ye et al., "Securing Large Language Models: A Survey of Watermarking and Fingerprinting Techniques", DOI `10.1145/3773028`, ACM CSUR 2026이 확인되나 지정 문헌과 동일하다고 확정할 수 없음 | 대체 PDF, 지정 논문 원문 확보 필요 | 지정 P02 원문 또는 공식 페이지 확보 전까지 로컬 PDF는 보조 배경으로만 사용 |
| P03 | Feng Li et al., "Deep neural network watermarking: Techniques and challenges", Neurocomputing, 2021 | Yue Li, Hongxia Wang, Mauro Barni, "A Survey of Deep Neural Network Watermarking Techniques" | DOI `10.1016/j.neucom.2021.07.051`, Neurocomputing, Vol. 461, pp. 171-193, 2021 | 로컬 PDF 공식 DOI 확인 완료, 단 강의계획서의 저자명·제목 표기와 불일치 | 강의계획서 표기가 오기인지 사람 검토 필요 |
| P04 | Kaiyi Pang et al., "ModelShield: Adaptive and Robust Watermark Against Model Extraction Attack", IEEE TIFS, 2025 | arXiv:2405.02365v4 PDF | DOI `10.1109/TIFS.2025.3530691`, IEEE Transactions on Information Forensics and Security, Vol. 20, pp. 1767-1782, 2025 | arXiv판과 IEEE TIFS 출판판 제목·저자 일치 확인, 권호/쪽/DOI 확인 완료 | 최종 인용은 IEEE DOI 기준, arXiv v4는 사전판으로 병기 |
| P05 | Cheng/Chenhan Zhang et al., "Generative Adversarial Networks: A Survey on Attack and Defense", ACM Computing Surveys, 2023 | `05_SUBSTITUTE_Cai_et_al_2021_GAN_Private_Secure_Applications.pdf`: Zhipeng Cai et al., "Generative Adversarial Networks: A Survey Towards Private and Secure Applications", arXiv:2106.03785v1 | 지정 제목과 매우 유사한 ACM 논문은 Chenhan Zhang et al., "Generative Adversarial Networks: A Survey on Attack and Defense Perspective", DOI `10.1145/3615336`, ACM CSUR Vol. 56, Issue 4, pp. 1-35, online 2023-11-10, print 2024-04-30 | 대체 PDF, 지정 문헌 저자명·제목 표기 차이 확인 필요 | 지정 P05 원문 확보 전까지 로컬 PDF는 보조 배경으로만 사용 |

## SUBSTITUTE 경고

주의: W13의 P02는 지정 논문과 로컬 PDF가 불일치한다. 현재 로컬 PDF는 Yuqing Liang et al.의 LLM watermarking survey이므로, 최종 제출 전 Y. Ye et al.의 deep learning model watermarking/fingerprinting 지정 논문 원문 또는 공식 출판 페이지를 확보해야 한다.

주의: W13의 P05는 지정 논문과 로컬 PDF가 불일치한다. 현재 로컬 PDF는 Zhipeng Cai et al.의 GAN privacy/security application survey이므로, 최종 제출 전 Cheng/Chenhan Zhang et al.의 GAN attack/defense 지정 논문 원문 또는 공식 출판 페이지를 확보해야 한다.

## PDF 보관 위험

`01_papers/pdf/`의 PDF 5개는 이미 git 추적 대상이다. 공개 GitHub 저장소에는 원칙적으로 출판사 PDF 원문 대신 DOI/URL, 서지정보, 요약만 남기는 것이 안전하다. 사용자 승인 없이 PDF를 삭제하지 않았으며, 최종 공개 전 삭제 또는 비공개 저장소 이전 검토가 필요하다.
