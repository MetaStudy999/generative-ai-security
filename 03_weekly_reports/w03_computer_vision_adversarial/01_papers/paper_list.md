# W03 논문 목록

> 최종 판정 우선: 이 문서의 현재 상태는 `논문/관련 논문 최종 반영표`를 우선한다. 상단의 제목·저자·로컬 PDF 차이 메모는 오류 판정이 아니라 검증 이력이며, `관련 논문 / 확인`은 주차 주제에 맞는 공식 확인 논문으로 사용한다.
>
> 2026-06-24 기준: `02_paper_summaries/P01_summary.md` ~ `P05_summary.md`는 100점형 구조로 보완 완료했다. 수식은 GitHub, MS Word, PDF 변환 호환성을 위해 Markdown 표 밖의 LaTeX block math로 작성했다.

강의계획서 W03 논문 패킷 5편을 Crossref/DOI 메타데이터와 로컬 PDF 첫 페이지 기준으로 재검증했다. 아래 목록은 제출용 최종 초안의 기준 목록이며, PDF 원문은 public GitHub 저장소 보관 시 저작권 위험이 있으므로 DOI/URL 중심 관리가 필요하다.

| ID | 논문 제목 | 저자 | 연도 | 학술지/권호/쪽 | DOI/공식 URL | 로컬 PDF | 검증 상태 |
|---|---|---|---:|---|---|---|---|
| P01 | Gradient-Based Learning Applied to Document Recognition | Yann LeCun, Leon Bottou, Yoshua Bengio, Patrick Haffner | 1998 | *Proceedings of the IEEE*, 86(11), 2278-2324 | https://doi.org/10.1109/5.726791 | `01_LeCun_et_al_1998_Gradient_Based_Learning_Document_Recognition.pdf` | 확인됨. 100점형 summary 보완 완료 |
| P02 | Deep Learning for Computer Vision: A Brief Review | Athanasios Voulodimos, Nikolaos Doulamis, Anastasios Doulamis, Eftychios Protopapadakis | 2018 | *Computational Intelligence and Neuroscience*, 2018, Article ID 7068349, 1-13 | https://doi.org/10.1155/2018/7068349 | `02_Voulodimos_et_al_2018_Deep_Learning_Computer_Vision_Review.pdf` | 확인됨. 100점형 summary 보완 완료 |
| P03 | Multimodal Learning With Transformers: A Survey | Peng Xu, Xiatian Zhu, David A. Clifton | 2023 | *IEEE Transactions on Pattern Analysis and Machine Intelligence*, 45(10), 12113-12132 | https://doi.org/10.1109/TPAMI.2023.3275156 | `03_Xu_et_al_2023_Multimodal_Learning_Transformers_Survey.pdf` | 확인됨. 100점형 summary 보완 완료 |
| P04 | Transformers in Vision: A Survey | Salman Khan, Muzammal Naseer, Munawar Hayat, Syed Waqas Zamir, Fahad Shahbaz Khan, Mubarak Shah | 2022 | *ACM Computing Surveys*, 54(10s), 1-41 | https://doi.org/10.1145/3505244 | `04_Khan_et_al_2022_Transformers_in_Vision_Survey.pdf` | 확인됨. 100점형 summary 보완 완료 |
| P05 | A Survey of Robustness and Safety of 2D and 3D Deep Learning Models against Adversarial Attacks | Yanjie Li, Bin Xie, Songtao Guo, Yuanyuan Yang, Bin Xiao | 2024 | *ACM Computing Surveys*, 56(6), 1-37 | https://doi.org/10.1145/3636551 | `05_Li_et_al_2024_Robustness_Safety_2D_3D_Adversarial_Attacks.pdf` | 확인됨. 100점형 summary 보완 완료 |

## 100점형 summary 반영 상태

| ID | 보완 상태 | 추가된 핵심 요소 |
|---|---|---|
| P01 | 완료 | 2D convolution, pooling, gradient-based learning, CNN/OCR 위협모형, clean/robust 지표 |
| P02 | 완료 | softmax, cross-entropy, CV task별 보안 지표, classification/detection/recognition 평가 분리 |
| P03 | 완료 | scaled dot-product attention, cross-modal fusion, alignment loss, 멀티모달 위협모형 |
| P04 | 완료 | patch embedding, multi-head self-attention, robust drop, ViT patch/token/attention 공격면 |
| P05 | 완료 | 대적 교란 일반식, FGSM, robust accuracy, 3D point cloud 교란, 2D/3D safety threat model |

## 검수 메모

- P02의 강의계획서/기존 목록 표기 `Apostolos Voulodimos`는 Crossref와 PDF 첫 페이지 기준 `Athanasios Voulodimos`로 정정했다.
- P03의 강의계획서 축약 표기 `Y. Xu et al.`은 실제 제1저자 `Peng Xu`와 대응한다.
- P05의 강의계획서 축약 표기 `Z. Li et al.`은 Crossref와 PDF 첫 페이지 기준 `Yanjie Li et al.`로 확인되었다. 최종 출판연도는 2024년이며, 로컬 PDF 파일명에 포함된 `2024`와 일치한다.
- P03-P05 로컬 PDF는 첫 페이지상 arXiv 또는 manuscript 버전으로 보인다. 출판사 최종 PDF가 아니더라도 public GitHub 저장소에 원문 PDF를 두는 것은 저작권/배포 정책 위험이 있으므로 삭제 검토가 필요하다.

## 논문/관련 논문 최종 반영표

| ID | 구분 | 논문 제목 | 저자 | 연도 | 학술지/출처 | DOI/URL | 검증 상태 | 보고서 반영 |
|---|---|---|---|---:|---|---|---|---|
| P01 | 논문 / 확인 | Gradient-Based Learning Applied to Document Recognition | Yann LeCun et al. | 1998 | Proceedings of the IEEE | `https://doi.org/10.1109/5.726791` | 공식 DOI 확인 | CNN/gradient-based learning 핵심 배경 |
| P02 | 논문 / 확인 | Deep Learning for Computer Vision: A Brief Review | Athanasios Voulodimos et al. | 2018 | Computational Intelligence and Neuroscience | `https://doi.org/10.1155/2018/7068349` | 공식 DOI 확인 | CV task별 평가 지표 배경 |
| P03 | 논문 / 확인 | Multimodal Learning With Transformers: A Survey | Peng Xu, Xiatian Zhu, David A. Clifton | 2023 | IEEE TPAMI | `https://doi.org/10.1109/TPAMI.2023.3275156` | 공식 DOI 확인 | 멀티모달/LLM/RAG 확장 bridge |
| P04 | 논문 / 확인 | Transformers in Vision: A Survey | Salman Khan et al. | 2022 | ACM Computing Surveys | `https://doi.org/10.1145/3505244` | 공식 DOI 확인 | ViT patch/token/attention 구조 분석 |
| P05 | 논문 / 확인 | A Survey of Robustness and Safety of 2D and 3D Deep Learning Models against Adversarial Attacks | Yanjie Li et al. | 2024 | ACM Computing Surveys | `https://doi.org/10.1145/3636551` | 공식 DOI 확인 | 2D/3D adversarial robustness 핵심 보안 문헌 |
