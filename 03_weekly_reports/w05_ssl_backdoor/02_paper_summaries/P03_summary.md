# P03 Summary

## Self-Supervised Learning for Videos: A Survey — Madeline C. Schiappa, Yogesh S. Rawat, Mubarak Shah, ACM Computing Surveys, 2023

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W05 자기지도학습·파운데이션 모델 & Poisoning/Backdoor |
| 강의계획서 표기 | Self-Supervised Learning of Video Representations: A Survey |
| 정식 제목 | Self-Supervised Learning for Videos: A Survey |
| 저자 | Madeline C. Schiappa, Yogesh S. Rawat, Mubarak Shah |
| 학술지 | ACM Computing Surveys |
| 권호/쪽 | Vol. 55, No. 13s, pp. 1–37 |
| 연도 | 2023 |
| DOI | https://doi.org/10.1145/3577925 |
| 보조 URL | https://arxiv.org/abs/2207.00419 |
| 논문 유형 | Survey / Video Self-Supervised Learning Review |
| 로컬 PDF | `01_papers/pdf/03_Schiappa_Rawat_Shah_2023_Self_Supervised_Learning_Videos.pdf` |
| 강의계획서 지정 논문과 일치 여부 | 의미상 일치. 제목은 출판사 기준 정식 제목으로 사용 |
| 핵심 근거 사용 가능 여부 | 가능 |
| 검증 메모 | W05 `paper_list.md` 기준 DOI/URL 확인. 로컬 PDF는 arXiv판일 수 있어 ACM 최종 Article 번호와 페이지는 추가 확인 필요 |

---

## 1. 한 문장 요약

이 논문은 비디오 self-supervised learning을 **temporal order, motion, frame sampling, contrastive learning, generative learning, cross-modal agreement, action recognition, video retrieval, downstream transfer** 관점에서 정리하고, W05에서 시간축과 멀티모달 신호가 representation과 backdoor/poisoning 공격면을 확장함을 설명하는 survey 논문이다.

---

## 2. 연구문제

> 비디오 데이터에서 라벨 없이 시간적·공간적·멀티모달 표현을 학습하기 위해 어떤 pretext task가 사용되며, 이러한 temporal representation은 downstream task와 보안 평가에서 어떤 취약성을 만드는가?

| 번호 | 연구질문 |
|---|---|
| RQ1 | 비디오 SSL은 이미지 SSL과 달리 시간축과 motion 정보를 어떻게 활용하는가? |
| RQ2 | Temporal contrastive learning, order prediction, future prediction, masked video modeling은 어떤 역할을 하는가? |
| RQ3 | Video-audio-text cross-modal agreement는 representation 학습에 어떤 이점을 주는가? |
| RQ4 | Temporal trigger, frame-level poisoning, sampling manipulation은 downstream behavior를 어떻게 왜곡할 수 있는가? |
| RQ5 | 비디오 SSL 보안 평가는 action recognition accuracy 외에 어떤 robust/safety 지표가 필요한가? |

---

## 3. 핵심 이론 및 수식

### 3.1 Temporal Contrastive Objective

같은 비디오 내 인접하거나 관련 있는 시점 표현을 positive pair로 둘 수 있다.

$$
\mathcal{L}_{temp}=-\log\frac{\exp(sim(z_t,z_{t+\Delta})/\tau)}{\sum_j\exp(sim(z_t,z_j)/\tau)}
$$

| 기호 | 의미 |
|---|---|
| $z_t$ | 시점 $t$의 비디오 표현 |
| $z_{t+\Delta}$ | 같은 비디오의 인접 또는 관련 시점 표현 |
| $z_j$ | 비교 후보 표현 |
| $\tau$ | temperature |

### 보안적 의미

공격자가 특정 frame, frame order, temporal segment를 조작하면 temporal positive relation이 왜곡될 수 있다. 이는 downstream action recognition이나 retrieval 결과를 바꿀 수 있다.

---

### 3.2 Temporal Consistency Loss

비디오 SSL은 시간적으로 인접한 표현이 일관되도록 학습할 수 있다.

$$
\mathcal{L}_{cons}=\sum_{t}\left\|h_{\theta}(v_t)-h_{\theta}(v_{t+\Delta})\right\|_2^2
$$

| 기호 | 의미 |
|---|---|
| $v_t$ | 시점 $t$의 frame 또는 clip |
| $h_{\theta}$ | 비디오 encoder |
| $\Delta$ | 시간 간격 |

### 보안적 의미

Temporal consistency는 안정적 표현을 만들지만, 특정 trigger가 여러 frame에 반복되면 모델이 해당 패턴을 강한 시계열 신호로 학습할 수 있다.

---

### 3.3 Downstream Transfer Evaluation

비디오 SSL 표현은 action recognition이나 retrieval로 평가된다.

$$
\hat{y}=g_{\phi}(h_{\theta}(v_{1:T}))
$$

| 기호 | 의미 |
|---|---|
| $v_{1:T}$ | 길이 $T$의 비디오 clip |
| $h_{\theta}$ | self-supervised video encoder |
| $g_{\phi}$ | downstream classifier 또는 retrieval head |

### 보안적 의미

비디오 encoder가 오염되면 downstream classifier를 깨끗하게 학습해도 trigger condition에서 오작동할 수 있다.

---

## 4. AI 원리 관점 분석

| 항목 | 분석 |
|---|---|
| Temporal Order | frame 순서와 시간적 연속성이 핵심 신호다. |
| Motion | optical flow, frame difference, dynamic pattern을 활용한다. |
| Contrastive Video SSL | 같은 video/clip의 view를 positive로 사용한다. |
| Generative Video SSL | masked frame/clip reconstruction을 수행한다. |
| Cross-modal Agreement | video-audio-text alignment를 학습한다. |
| Downstream Transfer | action recognition, retrieval, localization으로 평가된다. |

---

## 5. 보안 이슈 관점 분석

| 보안 항목 | 비디오 SSL 관점 해석 |
|---|---|
| 무결성 | frame sampling, temporal order, trigger frame 조작이 표현을 왜곡한다. |
| 안전성 | 행동 인식·감시·로봇 비전에서 오분류가 실제 피해로 이어질 수 있다. |
| 기밀성 | 비디오에는 얼굴, 위치, 행동, 음성 등 민감정보가 포함될 수 있다. |
| 가용성 | 노이즈, frame drop, modality missing이 서비스 품질을 낮춘다. |
| 책임성 | clip sampling, augmentation, modality alignment, dataset source를 기록해야 한다. |

---

## 6. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 대상 | video frames, clip sampling, audio/text modality, temporal representation, downstream output |
| 공격자 목표 | action misclassification, retrieval mismatch, temporal trigger activation |
| 공격자 능력 | frame insertion/deletion, temporal reorder, trigger frame 삽입, modality mismatch 유도 |
| 공격 경로 | video sequence → sampling/augmentation → SSL encoder → downstream task |
| 제외 범위 | 실제 감시·로봇 시스템 공격, 개인 영상 사용, 무단 데이터 수집 |

---

## 7. 평가방법 및 지표

| 지표 | 의미 | W05/P03에서의 활용 |
|---|---|---|
| Action Recognition Accuracy | downstream 행동 인식 성능 | clean transfer 평가 |
| Video Retrieval Recall | 비디오 표현 검색 성능 | representation quality |
| Temporal Robustness | frame drop/reorder/noise 조건 성능 | 시간축 견고성 |
| ASR | trigger frame 조건 공격 성공률 | backdoor 평가 |
| Cross-modal Consistency | video-audio-text 정합성 | modality mismatch 탐지 |
| Representation Shift | 오염 전후 encoder 표현 차이 | poisoning 영향 |

---

## 8. 재현성 점검

| 항목 | 점검 |
|---|---|
| 데이터 | UCF101/Kinetics subset 또는 toy video clips 사용 가능 |
| Sampling | frame rate, clip length, temporal stride 기록 필요 |
| Augmentation | crop, temporal jitter, frame masking, audio/text pairing 기록 |
| 평가 | action accuracy, retrieval recall, temporal robustness, ASR 분리 |
| 한계 | toy video 실험을 실제 감시/자율 시스템 안전성으로 일반화하지 않음 |

---

## 9. 논문의 고유 기여

1. 비디오 SSL의 pretext task와 representation learning 흐름을 체계화했다.
2. 이미지 SSL과 달리 temporal order, motion, cross-modal signal의 중요성을 보여준다.
3. W05에서 temporal trigger, frame-level poisoning, modality mismatch 위험을 논의하는 배경 문헌이 된다.
4. 후속 W07/W08의 멀티모달 LLM과 video-RAG 보안으로 확장 가능하다.

---

## 10. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 보안 직접성 부족 | poisoning/backdoor 전문 문헌은 아니다. | P04/P05와 결합한다. |
| 재현 비용 | 비디오 SSL pretraining은 데이터와 GPU 비용이 크다. | toy clips와 문헌 기반 비교로 제한한다. |
| 개인정보 위험 | 비디오 데이터는 민감정보를 포함할 수 있다. | 공개 데이터 또는 synthetic/toy data만 사용한다. |
| LLM/Video foundation 확장 필요 | 최신 video foundation model은 추가 문헌 필요 | W07/W08로 연결한다. |

---

## 11. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 2장 관련연구 | 비디오 SSL, temporal representation, cross-modal agreement 정리 |
| 3장 위협모형 | temporal trigger, frame poisoning, modality mismatch 정의 |
| 4장 연구방법 | temporal robustness, retrieval recall, ASR 지표 설계 |
| 6장 보안적 함의 | 영상 데이터 프라이버시, 안전성, 책임성 해석 |

---

## 12. 기말논문 연결 3문장

1. 이 주차에서 기말논문에 반영할 개념: 비디오 SSL은 frame sequence와 temporal consistency를 이용하므로 frame-level poisoning과 temporal trigger가 representation을 왜곡할 수 있다.
2. 이 주차에서 기말논문에 반영할 표·그림·실험: temporal contrastive objective, video SSL pipeline, temporal threat model, action accuracy-ASR 비교표를 반영한다.
3. 이 주차가 RAG 문서 오염/LLM 보안 감사 프레임워크와 연결되는 지점: video-RAG와 멀티모달 LLM은 frame/text/audio context를 함께 사용하므로 P03의 temporal/cross-modal provenance를 W08/W14로 확장한다.

---

## 13. 최종 판단

P03은 W05에서 비디오 SSL과 temporal representation을 설명하는 핵심 문헌이다. 직접 보안 문헌은 아니지만 temporal poisoning/backdoor 평가축을 도출하는 데 유용하다.

---

## 14. 변환 호환성 메모

```bash
pandoc P03_summary.md -o P03_summary.docx
pandoc P03_summary.md -o P03_summary.pdf --pdf-engine=xelatex
```
