# 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 논문 제목 | A Survey on Video Diffusion Models |
| 저자 | Zhen Xing, Qijun Feng, Haoran Chen, Qi Dai, Han Hu, Hang Xu, Zuxuan Wu, Yu-Gang Jiang |
| 학술지/학회 | arXiv preprint / ACM-formatted preprint |
| 연도 | 2024 |
| DOI/URL | https://doi.org/10.48550/arXiv.2310.10647, https://arxiv.org/abs/2310.10647 |
| PDF 파일명 | 02_Xing_et_al_2024_Video_Diffusion_Models_Survey.pdf |
| 검증 상태 | arXiv DOI 확인, ACM DOI 미확인 |

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
| Evaluation gap | 영상 품질과 신뢰성 지표의 불일치 | W06 신뢰성 평가 설계 |

## 5. 방법론

비디오 diffusion 연구를 generation, editing, video understanding 등으로 나누어 survey한다. 본 보고서에서는 실제 비디오 생성 실험을 수행하지 않고, 탐지 신뢰성의 핵심 위험인 domain shift와 uncertainty routing만 synthetic score 실험으로 재현했다.

## 6. 주요 결과

Video diffusion은 이미지 생성보다 더 큰 계산 비용과 temporal coherence 문제를 갖는다. 생성 품질이 높아질수록 탐지기는 단일 이미지 artifact보다 frame-level, sequence-level, compression robustness까지 함께 평가해야 한다.

## 7. 보안 관점 분석

비디오 딥페이크는 압축, 재인코딩, 플랫폼별 후처리, 프레임 샘플링에 의해 탐지 score 분포가 흔들릴 수 있다. 따라서 W06 실험의 cross-domain reliability stress는 P02의 temporal/video domain 논의를 안전한 toy 형태로 축소한 것이다.

## 8. 한계와 오픈문제

로컬 PDF의 ACM DOI 필드는 임시값으로 남아 있어 최종 ACM DOI는 확인하지 못했다. 또한 survey는 실제 forensic detector의 법적 신뢰성을 직접 보장하지 않는다.

## 9. 기말 논문에 반영할 부분

기말 논문에서는 video diffusion을 비디오 합성미디어 위협의 배경으로 쓰고, temporal consistency와 platform shift를 탐지 신뢰성 평가 항목에 포함한다.
