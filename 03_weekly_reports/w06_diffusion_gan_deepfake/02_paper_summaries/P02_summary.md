# 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 논문 제목 | A Survey on Video Diffusion Models |
| 저자 | Zhen Xing, Qijun Feng, Haoran Chen, Qi Dai, Han Hu, Hang Xu, Zuxuan Wu, Yu-Gang Jiang |
| 학술지/학회 | ACM Computing Surveys |
| 출판 정보 | Vol. 57, No. 2, pages 1-42, online 2024-11-07, print issue 2025-02-28, Article 번호 확인 필요 |
| 연도 | 2024 online / 2025 print issue |
| DOI/URL | https://doi.org/10.1145/3696415, https://doi.org/10.48550/arXiv.2310.10647, https://arxiv.org/abs/2310.10647 |
| PDF 파일명 | 02_Xing_et_al_2024_Video_Diffusion_Models_Survey.pdf |
| 검증 상태 | ACM/arXiv DOI 확인, 강의계획서 지정 P02 동일 여부와 Article 번호 확인 필요 |

## 2. 한 문장 요약

> 이 논문은 video diffusion model의 생성, 편집, 이해 과제를 diffusion 원리와 application taxonomy로 정리하며, 비디오 딥페이크 탐지에서 temporal consistency와 cross-domain generalization이 왜 중요한지 설명한다.

## 3. 연구문제

이미지 diffusion과 달리 video diffusion은 프레임 간 시간 일관성, motion modeling, 긴 sequence sampling 비용, text-video alignment를 함께 다뤄야 한다. 이 논문은 video domain에서 diffusion model이 어떤 과제로 확장되고, 어떤 평가·응용 문제가 남는지 정리한다.

## 4. 핵심 개념

| 개념 | 설명 | 기말 논문 연결 |
|---|---|---|
| Video generation | 시간축을 포함한 영상 생성 | 비디오 딥페이크 생성 배경 |
| Video editing | 기존 영상의 내용·스타일·동작 조작 | 합성미디어 조작면 |
| Temporal consistency | 프레임 간 자연스러운 motion 유지 | 탐지 우회와 포렌식 단서 |
| Text-to-video | 자연어 조건으로 영상 생성 | 조건부 생성 위험 |
| Evaluation gap | 영상 품질과 신뢰성 지표의 표기 차이 | W06 신뢰성 평가 설계 |

## 5. 방법론

비디오 diffusion 연구를 generation, editing, video understanding 등으로 나누어 survey한다. 본 보고서에서는 실제 비디오 생성 실험을 수행하지 않고, 탐지 신뢰성의 핵심 위험인 domain shift와 uncertainty routing만 synthetic score 실험으로 재현했다.

### 5.1 핵심 수식 또는 알고리즘 설명

| 항목 | 내용 |
|---|---|
| 수식/알고리즘 이름 | Conditional Video Diffusion 개념식 |
| 원문 위치 | 논문 세부 절/쪽/그림/알고리즘 번호 확인 필요. 로컬 DOI/URL 점검표로 문헌 대응만 확인. |
| 작성 형식 | Markdown + LaTeX math |
| 검산 도구 | 사용 안 함 |
| 수식 또는 절차 | 표준 정의식 / 원문 직접 인용 아님.<br>$$p_\theta(x_{0:T}\mid c)=\prod_t p_\theta(x_{t-1}\mid x_t,c)$$ |
| 기호·입력·출력 | \(x_{0:T}\): video frame 또는 latent sequence, \(c\): 조건, \(p_\theta\): reverse model |
| 직관적 의미 | Conditional Video Diffusion 개념식는 Diffusion/GAN·Deepfake 평가에서 핵심 원리나 평가 지표를 정량적으로 해석하기 위한 표준식이다. |
| 보안 관점 해석 | Diffusion/GAN·Deepfake 평가에서는 정상 성능과 보안 실패 조건을 분리해 보아야 한다. 이 항목은 공격·방어 원리 또는 운영 통제의 평가 기준을 명시하되, 실제 공격 절차나 무단 적용 단계는 포함하지 않는다. |
| 평가 지표와 연결 | temporal consistency, FPR/FNR, detection accuracy |
| 한계와 가정 | 표준 정의식 / 원문 직접 인용 아님. 논문별 변형, 정확한 수식 번호, 실험 설정은 원문 PDF에서 확인 필요다. |
| 기말 논문 반영 여부 | 참고만 |

## 6. 주요 결과

Video diffusion은 이미지 생성보다 더 큰 계산 비용과 temporal coherence 문제를 갖는다. 생성 품질이 높아질수록 탐지기는 단일 이미지 artifact보다 frame-level, sequence-level, compression robustness까지 함께 평가해야 한다.

## 7. 보안 관점 분석

비디오 딥페이크는 압축, 재인코딩, 플랫폼별 후처리, 프레임 샘플링에 의해 탐지 score 분포가 흔들릴 수 있다. 따라서 W06 실험의 cross-domain reliability stress는 P02의 temporal/video domain 논의를 안전한 toy 형태로 축소한 것이다.

## 8. 한계와 오픈문제

ACM DOI `10.1145/3696415`는 확인되었지만, 강의계획서 지정 P02는 `Ananya Högele et al., "Video Diffusion Models: A Survey"`로 되어 있어 현재 로컬 PDF와 제목·저자 표기가 다르다. 동일 논문인지 확인되지 않으면 현재 P02는 관련 보조 문헌으로 보아야 한다. 또한 survey는 실제 forensic detector의 법적 신뢰성을 직접 보장하지 않는다.

주의: W06의 P02는 강의계획서 지정 논문인 Ananya Högele et al., "Video Diffusion Models: A Survey"와 현재 로컬 PDF "A Survey on Video Diffusion Models"의 동일 여부를 최종 확인해야 한다. 동일하지 않다면 현재 P02는 관련 보조 문헌으로 사용한 것이며, 최종 제출 전 교수자 확인이 필요하다.

## 9. 기말 논문에 반영할 부분

기말 논문에서는 video diffusion을 비디오 합성미디어 위협의 배경으로 쓰고, temporal consistency와 platform shift를 탐지 신뢰성 평가 항목에 포함한다.
