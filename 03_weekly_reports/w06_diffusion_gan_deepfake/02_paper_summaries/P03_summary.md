# 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 논문 제목 | Generative Adversarial Networks in Computer Vision: A Survey and Taxonomy |
| 저자 | Zhengwei Wang, Qi She, Tomas E. Ward |
| 학술지/학회 | ACM Computing Surveys |
| 출판 정보 | Vol. 54, No. 2, Article 37, published 2021-02-09, print issue 2022-03-31 |
| 연도 | 2021 online / 2022 print issue |
| DOI/URL | https://doi.org/10.1145/3439723, https://doi.org/10.48550/arXiv.1906.01529, https://arxiv.org/abs/1906.01529 |
| PDF 파일명 | 03_Wang_She_Ward_2021_GANs_Computer_Vision_Survey.pdf |
| 검증 상태 | ACM/arXiv DOI 확인, 강의계획서 저자명 차이 확인 필요 |

## 2. 한 문장 요약

> 이 논문은 computer vision에서 GAN 변형과 loss taxonomy를 정리하며, 고품질·다양성·학습 안정성 문제가 합성미디어와 딥페이크 탐지의 기초 위험으로 이어짐을 보여준다.

## 3. 연구문제

GAN은 generator와 discriminator의 경쟁 구조로 사실적인 데이터를 생성하지만 mode collapse, training instability, evaluation ambiguity가 반복적으로 나타난다. 이 논문은 GAN 연구를 architecture variant와 loss variant로 분류하고 computer vision application에서 어떤 문제가 남는지 묻는다.

## 4. 핵심 개념

| 개념 | 설명 | 기말 논문 연결 |
|---|---|---|
| Generator | latent vector 또는 condition에서 synthetic sample 생성 | 딥페이크 생성 원리 |
| Discriminator | real/fake 구분을 학습하는 판별자 | 탐지기와 유사한 평가 관점 |
| Minimax training | generator와 discriminator의 경쟁 학습 | 학습 안정성 문제 |
| Mode collapse | 다양성이 줄고 일부 mode만 생성되는 현상 | 데이터 다양성 평가 |
| FID/IS 한계 | 생성 품질 지표가 보안 신뢰성을 직접 보장하지 않음 | 탐지 신뢰성 지표 필요 |

## 5. 방법론

GAN 연구를 architecture-variant와 loss-variant 중심으로 taxonomy화하고, computer vision application에서 품질·다양성·안정성을 비교한다. W06에서는 이 taxonomy를 diffusion과 비교하며 “생성 모델 평가”와 “포렌식 탐지 평가”를 구분한다.

## 6. 주요 결과

GAN은 image synthesis, image-to-image translation, attribute manipulation 등에서 큰 성과를 냈지만 stable training과 diversity 보장은 계속 어려운 문제다. 이러한 특성은 딥페이크 생성의 발전과 탐지기의 artifact 의존성을 함께 설명한다.

## 7. 보안 관점 분석

GAN discriminator는 탐지기처럼 보이지만 연구 목적의 discriminator와 forensic detector는 다르다. 실제 보안 평가는 FID나 visual quality가 아니라 FPR, FNR, cross-dataset generalization, human review routing까지 포함해야 한다.

## 8. 한계와 오픈문제

ACM DOI `10.1145/3439723`와 Article 37은 확인되었다. 다만 강의계획서에는 `Tianqi Wang et al.`로 표기되어 있고, 로컬 PDF/arXiv/ACM 출판 정보는 `Zhengwei Wang, Qi She, Tomas E. Ward`로 되어 있어 표기 차이를 최종 확인해야 한다. 또한 GAN survey만으로 최신 diffusion 기반 딥페이크를 설명하기에는 부족하므로 P01/P02와 함께 읽어야 한다.

주의: W06의 P03은 강의계획서 지정 저자명과 현재 로컬 PDF/arXiv 저자명이 다르므로, 동일 논문 여부와 강의계획서 표기 오류 가능성을 확인 필요 상태로 유지한다.

## 9. 기말 논문에 반영할 부분

GAN의 generator-discriminator 구조, mode collapse, training stability, 생성 품질 지표의 한계를 관련연구와 평가방법 장에 반영한다.
