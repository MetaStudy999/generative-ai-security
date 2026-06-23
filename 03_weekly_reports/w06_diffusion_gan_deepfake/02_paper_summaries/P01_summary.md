# 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 논문 제목 | Diffusion Models: A Comprehensive Survey of Methods and Applications |
| 저자 | Ling Yang, Zhilong Zhang, Yang Song, Shenda Hong, Runsheng Xu, Yue Zhao, Wentao Zhang, Bin Cui, Ming-Hsuan Yang |
| 학술지/학회 | ACM Computing Surveys |
| 출판 정보 | Vol. 56, No. 4, Article 105, online 2023-11-09, print issue 2024-04-30 |
| 연도 | 2023 online / 2024 print issue |
| DOI/URL | https://doi.org/10.1145/3626235, https://arxiv.org/abs/2209.00796 |
| PDF 파일명 | 01_Yang_et_al_2023_Diffusion_Models_Comprehensive_Survey.pdf |
| 검증 상태 | DOI/URL 확인 |

## 2. 한 문장 요약

> 이 논문은 diffusion model의 학습 원리, sampling 개선, likelihood 추정, 구조화 데이터 적용 문제를 survey와 taxonomy로 정리하며, 생성모형 평가와 딥페이크 탐지 신뢰성 논의를 위한 배경 이론을 제공한다.

## 3. 연구문제

Diffusion model은 노이즈를 점진적으로 추가하는 forward process와 노이즈를 제거하며 데이터를 복원하는 reverse process를 통해 복잡한 데이터 분포를 학습한다. 이 논문은 다양한 diffusion 계열 방법을 어떻게 분류하고, sampling 비용과 생성 품질, likelihood 추정, 특수 데이터 구조 처리 문제를 어떻게 이해할 것인지 묻는다.

## 4. 핵심 개념

| 개념 | 설명 | 기말 논문 연결 |
|---|---|---|
| Forward process | 데이터에 노이즈를 점진적으로 추가하는 고정 또는 학습된 확률 과정 | 생성모형 원리 설명 |
| Reverse process | 노이즈 상태에서 원 데이터 분포로 되돌리는 denoising 생성 과정 | synthetic media 생성 경로 이해 |
| Score-based model | 데이터 분포의 score를 추정해 sampling하는 관점 | diffusion과 확률적 생성 연결 |
| Sampling cost | 고품질 생성을 위해 많은 step이 필요한 문제 | 실제 보안 평가 비용과 연결 |
| Conditional generation | class, text, image condition으로 생성 방향을 제어 | 딥페이크와 합성미디어 위험 분석 |

## 5. 방법론

이 논문은 diffusion 연구를 sampling, likelihood, special data structure, application 관점으로 분류한다. 개별 모델 성능 경쟁보다 방법군의 구조와 연구 흐름을 정리하는 survey이므로, W06에서는 정량 수치보다 평가축과 한계를 가져온다.

### 5.1 핵심 수식 또는 알고리즘 설명

| 항목 | 내용 |
|---|---|
| 수식/알고리즘 이름 | DDPM Forward Process |
| 원문 위치 | 논문 세부 절/쪽/그림/알고리즘 번호 확인 필요. 로컬 DOI/URL 점검표로 문헌 대응만 확인. |
| 작성 형식 | Markdown + LaTeX math |
| 검산 도구 | 사용 안 함 |
| 수식 또는 절차 | 표준 정의식 / 원문 직접 인용 아님.<br>$$q(x_t\mid x_{t-1})=\mathcal{N}(x_t;\sqrt{1-\beta_t}x_{t-1},\beta_t I)$$ |
| 기호·입력·출력 | \(x_t\): timestep t의 noisy sample, \(\beta_t\): noise schedule, \(I\): identity covariance |
| 직관적 의미 | DDPM Forward Process는 Diffusion/GAN·Deepfake 평가에서 핵심 원리나 평가 지표를 정량적으로 해석하기 위한 표준식이다. |
| 보안 관점 해석 | Diffusion/GAN·Deepfake 평가에서는 정상 성능과 보안 실패 조건을 분리해 보아야 한다. 이 항목은 공격·방어 원리 또는 운영 통제의 평가 기준을 명시하되, 실제 공격 절차나 무단 적용 단계는 포함하지 않는다. |
| 평가 지표와 연결 | FID, detection accuracy, FPR/FNR, provenance score |
| 한계와 가정 | 표준 정의식 / 원문 직접 인용 아님. 논문별 변형, 정확한 수식 번호, 실험 설정은 원문 PDF에서 확인 필요다. |
| 기말 논문 반영 여부 | 반영 |

## 6. 주요 결과

Diffusion model은 이미지 생성뿐 아니라 video, text, temporal data, scientific data 등으로 확장된다. 그러나 sampling 비용, 평가 지표의 한계, 조건부 생성 통제, 데이터 구조별 일반화 문제는 여전히 중요한 연구 공백으로 남는다.

## 7. 보안 관점 분석

Diffusion model은 고품질 합성미디어 생성 능력을 높이는 동시에 딥페이크 탐지의 난도를 높인다. 따라서 보안 평가는 “생성이 가능한가”보다 “탐지기가 새로운 생성 방식, 압축, 편집, 도메인 이동에서도 신뢰할 수 있는가”로 이동해야 한다.

## 8. 한계와 오픈문제

Survey 문헌이므로 특정 딥페이크 탐지 모델의 성능을 직접 증명하지 않는다. 또한 생성 품질 지표와 포렌식 신뢰성 지표 사이에는 간극이 있어, W06 toy 실험에서는 이를 cross-domain reliability와 FPR/FNR 기록으로 보완했다.

arXiv판과 ACM판이 모두 확인되며, 제출용 참고문헌에는 ACM DOI와 Article 105 정보를 우선 사용한다. 세부 수식이나 그림을 직접 인용할 때는 ACM판의 절·쪽수 기준으로 재확인한다.

## 9. 기말 논문에 반영할 부분

기말 논문의 관련연구와 배경 이론 장에서 diffusion model의 forward/reverse process, score-based 관점, sampling 비용, 조건부 생성 개념을 정리하는 근거로 활용한다.
