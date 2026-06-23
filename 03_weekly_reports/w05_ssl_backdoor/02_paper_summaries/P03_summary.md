# P03 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 강의계획서 표기 | Self-Supervised Learning of Video Representations: A Survey |
| 정식 제목 | Self-Supervised Learning for Videos: A Survey |
| 저자 | Madeline C. Schiappa, Yogesh S. Rawat, Mubarak Shah |
| 출판 정보 | ACM Computing Surveys, 55(13s), 1-37, 2023 |
| DOI/URL | `10.1145/3577925`; https://doi.org/10.1145/3577925; https://arxiv.org/abs/2207.00419 |
| 로컬 PDF | `03_Schiappa_Rawat_Shah_2023_Self_Supervised_Learning_Videos.pdf` |
| 검증 상태 | DOI/URL 확인. Article 번호는 Crossref에서 확인되지 않아 확인 필요 |

## 2. 제목 차이 메모

강의계획서 제목은 `Self-Supervised Learning of Video Representations: A Survey`이고, ACM/Crossref 및 로컬 PDF 기준 제목은 `Self-Supervised Learning for Videos: A Survey`다. 저자와 주제는 대응되지만 최종 참고문헌에는 출판사 기준 정식 제목을 사용한다.

## 3. 한 문장 요약

이 논문은 비디오 표현학습에서 pretext task, generative learning, contrastive learning, cross-modal agreement를 정리하며, W05에서 temporal representation과 video SSL 평가 구조를 설명한다[3].

## 4. 핵심 기여

| 구분 | 내용 |
|---|---|
| Video-specific SSL | 이미지 SSL과 달리 시간축, motion, temporal consistency를 핵심 변수로 다룬다 |
| Cross-modal signal | video-audio-text 신호를 이용한 multimodal/self-supervised representation을 포함한다 |
| 평가 구조 | action recognition, retrieval, downstream transfer 평가를 연결한다 |

## 5. 보안 관점

비디오 SSL은 시간적 순서, 프레임 sampling, augmentation, cross-modal alignment에 의존한다. 따라서 temporal trigger, frame-level poisoning, modality mismatch, augmentation poisoning이 representation shift를 만들 수 있다. W05에서는 실제 공격 재현이 아니라 평가 지표와 위협면 도출에 활용한다.

### 5.1 핵심 수식 또는 알고리즘 설명

| 항목 | 내용 |
|---|---|
| 수식/알고리즘 이름 | Temporal Contrastive Objective |
| 원문 위치 | 논문 세부 절/쪽/그림/알고리즘 번호 확인 필요. 로컬 DOI/URL 점검표로 문헌 대응만 확인. |
| 작성 형식 | Markdown + LaTeX math |
| 검산 도구 | 사용 안 함 |
| 수식 또는 절차 | 표준 정의식 / 원문 직접 인용 아님.<br>$$\mathcal{L}_{temp}=-\log\frac{\exp(sim(z_t,z_{t+\Delta})/\tau)}{\sum_j\exp(sim(z_t,z_j)/\tau)}$$ |
| 기호·입력·출력 | \(z_t\): 시점 t 표현, \(z_{t+\Delta}\): 같은 영상의 인접 표현, \(z_j\): 비교 후보 |
| 직관적 의미 | Temporal Contrastive Objective는 자기지도학습·Backdoor 평가에서 핵심 원리나 평가 지표를 정량적으로 해석하기 위한 표준식이다. |
| 보안 관점 해석 | 자기지도학습·Backdoor 평가에서는 정상 성능과 보안 실패 조건을 분리해 보아야 한다. 이 항목은 공격·방어 원리 또는 운영 통제의 평가 기준을 명시하되, 실제 공격 절차나 무단 적용 단계는 포함하지 않는다. |
| 평가 지표와 연결 | video retrieval, action recognition transfer, trigger ASR |
| 한계와 가정 | 표준 정의식 / 원문 직접 인용 아님. 논문별 변형, 정확한 수식 번호, 실험 설정은 원문 PDF에서 확인 필요다. |
| 기말 논문 반영 여부 | 참고만 |

## 6. 한계와 확인 필요

- 로컬 PDF는 arXiv판이며 ACM 최종 PDF의 Article 번호는 확인 필요다.
- 직접 보안 논문은 아니므로 poisoning/backdoor 성능 주장을 이 문헌에서 끌어오지 않는다.

## 7. 기말 논문 활용

비디오 SSL 확장 장에서 temporal representation, cross-modal agreement, downstream transfer가 보안 평가축과 어떻게 연결되는지 설명하는 근거로 활용한다.
