# W13 논문 목록

> 최종 판정 우선: 이 문서의 현재 상태는 `논문/관련 논문 최종 반영표`를 우선한다. 상단의 제목·저자·로컬 PDF 차이 메모는 오류 판정이 아니라 검증 이력이며, `관련 논문 / 확인`은 주차 주제에 맞는 공식 확인 논문으로 사용한다.
>
> 2026-06-24 기준: `02_paper_summaries/P01_summary.md` ~ `P05_summary.md`는 100점형 구조로 보완 완료했다. 수식은 GitHub, MS Word, PDF 변환 호환성을 위해 Markdown 표 밖의 LaTeX block math로 작성했다.

> 상태 기준: DOI/출판정보는 ACM, IEEE, Elsevier, arXiv, Crossref 등 공식 메타데이터로 확인된 경우만 확정했다. 관련 논문 PDF는 최종 반영표 기준으로 관련 논문 여부를 구분한다.

| ID | 강의계획서 강의자료 표기 문헌 | 현재 로컬 PDF | 공식 확인 결과 | 검증 상태 | 제출 전 조치 |
|---|---|---|---|---|---|
| P01 | Daryna/Daria Oliynyk et al., "I Know What You Trained Last Summer: A Survey on Stealing Machine Learning Models and Defences", ACM Computing Surveys, 2023 | 동일 제목의 arXiv/ACM accepted manuscript PDF | DOI `10.1145/3595292`, ACM Computing Surveys, Vol. 55, Issue 14s, pp. 1-41, online 2023-07-17, print 2023-12-31. 제목은 `Defences` 표기 | 공식 DOI 확인 완료. 100점형 summary 보완 완료. 로컬 PDF는 VOR가 아닌 accepted/arXiv 계열 메타데이터 포함 | 최종 인용은 DOI/ACM 메타데이터 기준으로 정리 |
| P02 | Y. Ye et al., "A Survey of Watermarking and Fingerprinting Techniques for Deep Learning Models", ACM Computing Surveys, 2024 | `02_RELATED_Liang_et_al_2024_LLM_Watermarking_Survey.pdf`: Yuqing Liang et al., "Watermarking Techniques for Large Language Models: A Survey", arXiv:2409.00089v1 | 지정 제목과 일치하는 2024 ACM CSUR 문헌은 현재 확인하지 못함. 제목/저자 유사 후보로 Peigen Ye et al., "Securing Large Language Models: A Survey of Watermarking and Fingerprinting Techniques", DOI `10.1145/3773028`, ACM CSUR 2026이 확인되나 강의자료 표기 문헌과 동일하다고 관련 논문으로 별도 분류함 | 관련 논문 PDF, 강의자료 표기 원문 최종 반영표 기준 정리. 100점형 summary 보완 완료 | 지정 P02 원문 표기와 별개로 로컬 PDF는 보조 배경으로만 사용 |
| P03 | Feng Li et al., "Deep neural network watermarking: Techniques and challenges", Neurocomputing, 2021 | Yue Li, Hongxia Wang, Mauro Barni, "A Survey of Deep Neural Network Watermarking Techniques" | DOI `10.1016/j.neucom.2021.07.051`, Neurocomputing, Vol. 461, pp. 171-193, 2021 | 로컬 PDF 공식 DOI 확인 완료. 100점형 summary 보완 완료. 단 강의계획서의 저자명·제목 표기와 차이 | 강의계획서 표기가 오기인지 사람 검토 필요 |
| P04 | Kaiyi Pang et al., "ModelShield: Adaptive and Robust Watermark Against Model Extraction Attack", IEEE TIFS, 2025 | arXiv:2405.02365v4 PDF | DOI `10.1109/TIFS.2025.3530691`, IEEE Transactions on Information Forensics and Security, Vol. 20, pp. 1767-1782, 2025 | arXiv판과 IEEE TIFS 출판판 제목·저자 일치 확인, 권호/쪽/DOI 확인 완료. 100점형 summary 보완 완료 | 최종 인용은 IEEE DOI 기준, arXiv v4는 사전판으로 병기 |
| P05 | Cheng/Chenhan Zhang et al., "Generative Adversarial Networks: A Survey on Attack and Defense", ACM Computing Surveys, 2023 | `05_RELATED_Cai_et_al_2021_GAN_Private_Secure_Applications.pdf`: Zhipeng Cai et al., "Generative Adversarial Networks: A Survey Towards Private and Secure Applications", arXiv:2106.03785v1 | 지정 제목과 매우 유사한 ACM 논문은 Chenhan Zhang et al., "Generative Adversarial Networks: A Survey on Attack and Defense Perspective", DOI `10.1145/3615336`, ACM CSUR Vol. 56, Issue 4, pp. 1-35, online 2023-11-10, print 2024-04-30 | 관련 논문 PDF, 강의자료 표기 문헌 저자명·제목 표기 차이 추가 확인 메모. 100점형 summary 보완 완료 | 지정 P05 원문 표기와 별개로 로컬 PDF는 보조 배경으로만 사용 |

## 100점형 summary 반영 상태

| ID | 보완 상태 | 추가된 핵심 요소 |
|---|---|---|
| P01 | 완료 | model stealing, fidelity, query budget, extraction cost, API monitoring |
| P02 | 완료 / 관련 논문 | LLM watermark/fingerprint, detection score, FPR/FNR, paraphrase robustness |
| P03 | 완료 | DNN watermark verification, trigger set, watermark robustness, ownership proof |
| P04 | 완료 | ModelShield, watermark accuracy, extraction fidelity, utility drop |
| P05 | 완료 / 관련 논문 | GAN attack/defense, generated artifact risk, provenance coverage |

## 관련 보조 문헌 이력

주의: W13의 P02는 강의자료 표기와 로컬 PDF에 차이가 있다. 현재 로컬 PDF는 Yuqing Liang et al.의 LLM watermarking survey이므로, 최종 제출 전 Y. Ye et al.의 deep learning model watermarking/fingerprinting 강의자료 표기 원문 또는 공식 출판정보를 참고한다.

주의: W13의 P05는 강의자료 표기와 로컬 PDF에 차이가 있다. 현재 로컬 PDF는 Zhipeng Cai et al.의 GAN privacy/security application survey이므로, 최종 제출 전 Cheng/Chenhan Zhang et al.의 GAN attack/defense 강의자료 표기 원문 또는 공식 출판정보를 참고한다.

## PDF 보관 위험

`01_papers/pdf/`의 PDF 5개는 이미 git 추적 대상이다. 공개 GitHub 저장소에는 원칙적으로 출판사 PDF 원문 대신 DOI/URL, 서지정보, 요약만 남기는 것이 안전하다. 사용자 승인 없이 PDF를 삭제하지 않았으며, 최종 공개 전 삭제 또는 비공개 저장소 이전 검토가 필요하다.

<!-- AUTO-RELATED-PAPER-REFLECTION:start -->
## 논문/관련 논문 최종 반영표

아래 표는 공식 DOI/arXiv 재검색 결과를 주차 보고서에 반영하기 위한 최종 판정이다. 기존 대조 기록은 보존하고, 보고서 본문과 참고문헌에서는 이 표의 `구분`과 `검증 상태`를 우선 사용한다.

| ID | 구분 | 논문 제목 | 논문 | 저자 | 연도 | 학술지/학회 | 학술지/출처 | DOI/URL | 검증 상태 | 보고서 반영 |
|---|---|---|---|---|---:|---|---|---|---|---|
| P01 | 논문 / 확인 | I Know What You Trained Last Summer: A Survey on Stealing Machine Learning Models and Defences | I Know What You Trained Last Summer: A Survey on Stealing Machine Learning Models and Defences | Daria/Daryna Oliynyk et al. | 2023 | ACM Computing Surveys | ACM Computing Surveys | `https://doi.org/10.1145/3595292` | 공식 DOI 확인 | 공식 서지 기준으로 논문 인용 |
| P02 | 관련 논문 / 확인 | Securing Large Language Models: A Survey of Watermarking and Fingerprinting Techniques | Securing Large Language Models: A Survey of Watermarking and Fingerprinting Techniques | Peigen Ye et al. | 2026 | ACM Computing Surveys | ACM Computing Surveys | `https://doi.org/10.1145/3773028` | 공식 DOI 확인 | 주차 주제 보강용 관련 논문으로 인용 |
| P03 | 논문 / 확인 | A survey of Deep Neural Network watermarking techniques | A survey of Deep Neural Network watermarking techniques | Yue Li, Hongxia Wang, Mauro Barni | 2021 | Neurocomputing | Neurocomputing | `https://doi.org/10.1016/j.neucom.2021.07.051` | 공식 DOI 확인 | 공식 서지 기준으로 논문 인용 |
| P04 | 논문 / 확인 | ModelShield: Adaptive and Robust Watermark Against Model Extraction Attack | ModelShield: Adaptive and Robust Watermark Against Model Extraction Attack | Kaiyi Pang et al. | 2025 | IEEE TIFS | IEEE Transactions on Information Forensics and Security | `https://doi.org/10.1109/TIFS.2025.3530691` | 공식 DOI 확인 | 공식 서지 기준으로 논문 인용 |
| P05 | 논문 / 확인 | Generative Adversarial Networks: A Survey on Attack and Defense Perspective | Generative Adversarial Networks: A Survey on Attack and Defense Perspective | Chenhan Zhang et al. | 2023 | ACM Computing Surveys | ACM Computing Surveys | `https://doi.org/10.1145/3615336` | 공식 DOI 확인 | 공식 서지 기준으로 논문 인용 |
<!-- AUTO-RELATED-PAPER-REFLECTION:end -->
