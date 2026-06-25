# P03 Summary

## Self-Supervised Learning for Videos: A Survey — Madeline C. Schiappa, Yogesh S. Rawat, Mubarak Shah, ACM Computing Surveys, 2023

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W05 자기지도학습·파운데이션 모델 & Poisoning/Backdoor |
| 강의계획서 표기 | Self-Supervised Learning of Video Representations: A Survey |
| 정식 제목 | Self-Supervised Learning for Videos: A Survey |
| 저자 | Madeline C. Schiappa, Yogesh S. Rawat, Mubarak Shah |
| 공식 출판 정보 | ACM Computing Surveys, Vol. 55, No. 13s, pp. 1–37, 2023 |
| DOI | https://doi.org/10.1145/3577925 |
| 보조 URL | https://arxiv.org/abs/2207.00419 |
| 로컬 PDF | `01_papers/pdf/03_Schiappa_Rawat_Shah_2023_Self_Supervised_Learning_Videos.pdf` |
| 검증 상태 | W05 `paper_list.md`와 `download_source.md` 기준 DOI/URL 확인. 강의계획서 제목은 의미상 축약/변형 가능성이 있으나 참고문헌에는 출판사 기준 정식 제목을 사용 |
| PDF 확인 메모 | repo의 PDF 폴더에 P03 관련 PDF blob이 존재함을 확인했다. 요약은 로컬 PDF 경로와 W05 `paper_list.md`, `download_source.md`의 공식 DOI/arXiv 메타데이터 기준으로 보완했다. |
| 수식 호환성 | GitHub 수식 렌더링 오류 방지를 위해 `\operatorname`을 사용하지 않고, `\mathrm{sim}`과 짧은 변수명을 사용했다. `v_{<t}` 같은 표현은 쓰지 않고 `v_{1:t-1}` 형식을 사용한다. |
| 핵심 근거 사용 가능 여부 | 가능. W05에서 비디오 SSL, temporal representation, motion, cross-modal agreement, temporal poisoning/backdoor 공격면을 설명하는 핵심 문헌으로 사용 |

---

## 1. 한 문장 요약

이 논문은 비디오 자기지도학습을 **temporal order, motion representation, frame sampling, clip augmentation, temporal contrastive learning, future prediction, masked video modeling, video-audio-text cross-modal agreement, action recognition, video retrieval, downstream transfer** 관점에서 정리하며, W05에서는 시간축과 멀티모달 신호가 representation 학습을 강화하는 동시에 **frame-level poisoning, temporal trigger, sampling manipulation, modality mismatch**라는 보안 공격면을 확장함을 보여주는 survey 문헌이다.

---

## 2. 핵심 연구문제

> 비디오 SSL은 이미지 SSL과 달리 시간축, 움직임, clip 순서, frame 간 관계, audio-text alignment를 활용한다. 이 강점은 action recognition과 video retrieval 성능을 높이지만, temporal trigger나 frame sampling 조작이 downstream behavior를 왜곡할 수 있는 새로운 공격면을 만든다.

| 번호 | 연구질문 |
|---|---|
| RQ1 | 비디오 SSL은 이미지 SSL과 달리 시간축과 motion 정보를 어떻게 활용하는가? |
| RQ2 | Temporal contrastive learning, order prediction, future prediction, masked video modeling은 어떤 역할을 하는가? |
| RQ3 | Video-audio-text cross-modal agreement는 representation 학습에 어떤 이점을 주는가? |
| RQ4 | Temporal trigger, frame-level poisoning, sampling manipulation, modality mismatch는 downstream behavior를 어떻게 왜곡할 수 있는가? |
| RQ5 | 비디오 SSL 보안 평가는 action recognition accuracy 외에 어떤 robust/safety/reproducibility 지표가 필요한가? |

---

## 3. 논문의 핵심 기여

| 기여 | 설명 | W05 연결 |
|---|---|---|
| Video SSL taxonomy | temporal order, motion, contrastive, generative, predictive, cross-modal 방법 정리 | W05 P03 핵심 |
| Temporal representation 강조 | frame 순서, motion, clip sampling이 비디오 표현학습의 핵심임을 설명 | temporal trigger 위협모형 근거 |
| Cross-modal SSL 정리 | video-audio-text agreement와 multimodal signal을 이용하는 방법 정리 | W07/W08 멀티모달 보안 연결 |
| Downstream 평가 구조 | action recognition, video retrieval, localization, transfer evaluation 정리 | clean/attack 성능 분리 평가 |
| 보안 확장 가능성 | 보안 전문 문헌은 아니지만 frame poisoning, sampling manipulation, temporal backdoor 평가축 도출 가능 | P04/P05 poisoning/backdoor 문헌과 결합 |

---

## 4. 목차별 핵심 개괄

| 목차 | 핵심 내용 | 비전공자용 이해 |
|---|---|---|
| 1. Introduction | 비디오 데이터의 라벨 부족과 시간축 표현 학습 필요성을 설명한다. | 영상은 라벨 붙이기 어렵기 때문에 스스로 시간적 패턴을 배운다. |
| 2. Background | video representation, clip, frame, motion, downstream task를 정리한다. | 영상은 여러 장의 이미지와 움직임이 결합된 데이터다. |
| 3. Pretext Tasks | temporal order, future prediction, speed prediction, frame/clip reconstruction 등을 다룬다. | 순서 맞히기, 다음 장면 예측 같은 과제로 배운다. |
| 4. Contrastive Learning | 같은 video의 다른 view를 positive로, 다른 video를 negative로 두어 표현공간을 학습한다. | 같은 영상의 다른 조각은 가깝게 배운다. |
| 5. Generative/Masked Modeling | frame이나 clip 일부를 가리고 복원한다. | 가려진 장면을 맞히면서 영상 구조를 배운다. |
| 6. Cross-modal Learning | audio, text, optical flow 등 다른 modality와의 정합성을 학습한다. | 소리와 영상, 자막과 영상을 함께 맞춘다. |
| 7. Evaluation | action recognition, retrieval, downstream transfer, robustness를 평가한다. | 배운 표현이 실제 영상 이해에 도움이 되는지 본다. |
| 8. Challenges | 데이터 규모, temporal bias, augmentation, privacy, generalization, multimodal noise가 과제로 남는다. | 영상 데이터는 크고 민감하며, 시간축 조작에 취약하다. |

---

## 5. 핵심 이론 및 수식

> 아래 수식은 video SSL 원리와 W05 보안 평가를 설명하기 위한 표준화된 표현이다. GitHub 호환성을 위해 `\operatorname`은 사용하지 않고, 수식은 Markdown 표 밖의 LaTeX block math로 작성한다.

### 5.1 Temporal Contrastive Objective

같은 비디오 내 인접하거나 의미적으로 관련 있는 시점 표현을 positive pair로 둘 수 있다.

$$
\mathcal{L}_{temp}=-\log\frac{\exp(\mathrm{sim}(z_t,z_{t+d})/\tau)}{\sum_{j=1}^{K}\exp(\mathrm{sim}(z_t,z_j)/\tau)}
$$

| 기호 | 의미 |
|---|---|
| $z_t$ | 시점 $t$의 비디오 representation |
| $z_{t+d}$ | 같은 비디오의 인접 또는 관련 시점 representation |
| $z_j$ | 비교 후보 representation |
| $d$ | 시간 간격 |
| $\mathrm{sim}$ | 유사도 함수 |
| $\tau$ | temperature |

### 보안적 의미

공격자가 특정 frame, frame order, temporal segment를 조작하면 temporal positive relation이 왜곡될 수 있다. 이는 downstream action recognition이나 retrieval 결과를 바꿀 수 있다.

---

### 5.2 Temporal Consistency Loss

비디오 SSL은 시간적으로 인접한 표현이 일관되도록 학습할 수 있다.

$$
\mathcal{L}_{cons}=\sum_{t=1}^{T-d}\left\|h_{\theta}(v_t)-h_{\theta}(v_{t+d})\right\|_2^2
$$

| 기호 | 의미 |
|---|---|
| $v_t$ | 시점 $t$의 frame 또는 clip |
| $h_{\theta}$ | 비디오 encoder |
| $d$ | 시간 간격 |
| $T$ | clip 길이 |

### 보안적 의미

Temporal consistency는 안정적 표현을 만들지만, 특정 trigger가 여러 frame에 반복되면 모델이 해당 패턴을 강한 시계열 신호로 학습할 수 있다.

---

### 5.3 Masked Video Modeling

Frame 또는 patch 일부를 가리고 복원하도록 학습한다.

$$
\mathcal{L}_{mvm}=\sum_{i\in\mathcal{M}}\ell(\hat{r}_i,r_i)
$$

| 기호 | 의미 |
|---|---|
| $\mathcal{M}$ | mask된 frame/patch/clip 위치 집합 |
| $r_i$ | 원래 video representation 또는 token |
| $\hat{r}_i$ | 모델이 복원한 representation 또는 token |
| $\ell$ | 복원 손실 |

### 보안적 의미

Masked video modeling은 비디오 corpus의 시각·시간 패턴을 학습한다. corpus에 민감 장면, 편향, 반복 trigger가 포함되면 downstream behavior에 영향을 줄 수 있다.

---

### 5.4 Cross-modal Consistency

비디오와 오디오·텍스트 representation이 같은 의미를 가리키는지 평가한다.

$$
CrossModalConsistency=\frac{1}{N}\sum_{i=1}^{N}\mathrm{sim}(h_v^{(i)},h_m^{(i)})
$$

| 기호 | 의미 |
|---|---|
| $h_v^{(i)}$ | $i$번째 video representation |
| $h_m^{(i)}$ | $i$번째 audio/text 등 다른 modality representation |
| $\mathrm{sim}$ | 유사도 함수 |

### 보안적 의미

Audio-text-video가 서로 맞지 않으면 모델은 잘못된 action, event, identity 판단을 할 수 있다. 멀티모달 RAG와 MLLM에서는 modality mismatch가 보안 실패로 이어진다.

---

### 5.5 Downstream Transfer Evaluation

비디오 SSL 표현은 action recognition이나 retrieval로 평가된다.

$$
\hat{y}=g_{\phi}(h_{\theta}(v_{1:T}))
$$

| 기호 | 의미 |
|---|---|
| $v_{1:T}$ | 길이 $T$의 video clip |
| $h_{\theta}$ | self-supervised video encoder |
| $g_{\phi}$ | downstream classifier 또는 retrieval head |
| $\hat{y}$ | downstream prediction |

### 보안적 의미

비디오 encoder가 오염되면 downstream classifier를 깨끗하게 학습해도 trigger condition에서 오작동할 수 있다.

---

### 5.6 Temporal Backdoor ASR

Trigger frame이나 특정 temporal pattern 조건에서 공격 목표 behavior가 나타나는 비율이다.

$$
ASR_{temp}=\frac{N_{atk}}{N_{trig}}
$$

| 기호 | 의미 |
|---|---|
| $N_{trig}$ | temporal trigger가 포함된 평가 clip 수 |
| $N_{atk}$ | 공격 목표 behavior가 발생한 clip 수 |

### 보안적 의미

Video SSL backdoor는 단일 frame trigger뿐 아니라 frame 순서, 반복 패턴, 특정 motion cue로도 나타날 수 있다.

---

### 5.7 Temporal Robustness

Frame drop, reorder, noise 조건에서 성능이 얼마나 유지되는지 측정한다.

$$
TemporalRobustness=Acc_{clean}-\lambda_1DropLoss-\lambda_2ReorderLoss-\lambda_3NoiseLoss
$$

### 보안적 의미

영상 시스템은 압축, frame drop, sampling 차이, temporal jitter에 노출된다. 보안 평가는 clean accuracy만으로 충분하지 않다.

---

### 5.8 Video SSL Risk

비디오 SSL pipeline의 위험을 sampling, augmentation, temporal trigger, cross-modal mismatch, privacy 위험으로 요약한다.

$$
VideoSSLRisk=SamplingRisk+AugRisk+TriggerRisk+MismatchRisk+PrivacyRisk-MonitoringCoverage
$$

### 보안적 의미

비디오 SSL 보안은 모델만 검사해서는 부족하다. sampling rule, frame order, augmentation, modality alignment, dataset source를 함께 관리해야 한다.

---

## 6. AI 원리 70% 관점 분석

| 원리 항목 | 설명 | W05/P03에서의 의미 |
|---|---|---|
| Temporal Order | frame 순서와 시간적 연속성이 핵심 신호 | temporal trigger 공격면 |
| Motion | optical flow, frame difference, dynamic pattern 활용 | action recognition 근거 |
| Contrastive Video SSL | 같은 video/clip의 view를 positive로 사용 | temporal pair poisoning 가능 |
| Generative Video SSL | masked frame/clip reconstruction 수행 | corpus pattern memorization |
| Predictive SSL | future frame, speed, order, context 예측 | sequence manipulation 연결 |
| Cross-modal Agreement | video-audio-text alignment 학습 | modality mismatch와 MLLM 연결 |
| Downstream Transfer | action recognition, retrieval, localization으로 평가 | clean/attack 분리 필요 |
| Video Foundation | 대규모 비디오 pretraining은 video foundation model의 기반 | W07/W08 멀티모달 보안 연결 |

---

## 7. 보안 이슈 30% 관점 분석

| 보안 항목 | 비디오 SSL 관점 해석 | 대표 평가 지표 |
|---|---|---|
| 무결성 | frame sampling, temporal order, trigger frame 조작이 표현을 왜곡 | ASR_temp, RepShift |
| 안전성 | 행동 인식·감시·로봇 비전에서 오분류가 실제 피해로 이어질 수 있음 | robust accuracy, human review |
| 기밀성 | 비디오에는 얼굴, 위치, 행동, 음성 등 민감정보가 포함될 수 있음 | privacy leakage, re-identification risk |
| 가용성 | 노이즈, frame drop, modality missing이 서비스 품질 저하 | TemporalRobustness |
| 프라이버시 | video-audio-text 결합은 재식별 가능성을 높임 | cross-modal privacy risk |
| 책임성 | clip sampling, augmentation, modality alignment, dataset source를 기록해야 함 | data lineage, audit completeness |

---

## 8. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 대상 | video frames, clip sampling rule, audio/text modality, temporal representation, encoder checkpoint, downstream output |
| 공격자 목표 | action misclassification, retrieval mismatch, temporal trigger activation, modality mismatch 유도, 특정 event/class bias 삽입 |
| 공격자 능력 | frame insertion/deletion, temporal reorder, trigger frame 삽입, sampling rule 조작, audio-text mismatch 유도 |
| 공격 경로 | video sequence → sampling/augmentation → SSL encoder → downstream task → action/retrieval output |
| 방어자 능력 | frame provenance, sampling audit, trigger test, cross-modal consistency check, checkpoint verification, human review |
| 제외 범위 | 실제 감시·로봇 시스템 공격, 개인 영상 사용, 무단 데이터 수집, 공격 trigger 제작 절차 제공 |

---

## 9. 평가방법 및 지표

| 평가축 | 지표 | 의미 | W05/P03 활용 |
|---|---|---|---|
| Clean transfer | Action Recognition Accuracy | downstream 행동 인식 성능 | clean utility |
| Retrieval | Video Retrieval Recall | 비디오 표현 검색 성능 | representation quality |
| Temporal robustness | TemporalRobustness | frame drop/reorder/noise 조건 성능 | 시간축 견고성 |
| Backdoor | ASR_temp | trigger frame 조건 공격 성공률 | hidden behavior 평가 |
| Cross-modal | CrossModalConsistency | video-audio-text 정합성 | modality mismatch 탐지 |
| Representation | RepShift | 오염 전후 encoder 표현 차이 | poisoning 영향 |
| Privacy | re-identification risk | 얼굴·행동·장소 정보 노출 가능성 | 기밀성 평가 |
| Audit | Sampling provenance | frame rate, stride, clip source 기록 | 책임성 |

---

## 10. 재현성 체크리스트

| 항목 | 기록해야 할 내용 |
|---|---|
| Bibliographic status | DOI, ACM CSUR 출판정보, arXiv URL, 로컬 PDF 상태 |
| Data | UCF101/Kinetics subset 또는 toy video clips 사용, 개인정보·실제 민감 영상 제외 |
| Sampling | frame rate, clip length, temporal stride, frame order, seed |
| Augmentation | crop, temporal jitter, frame masking, speed change, audio/text pairing |
| SSL objective | temporal contrastive, masked video modeling, predictive task, cross-modal agreement 중 선택 |
| Model | video encoder, projection head, checkpoint hash, downstream head |
| Evaluation | action accuracy, retrieval recall, TemporalRobustness, ASR_temp, CrossModalConsistency, RepShift |
| Evidence | data source, clip hash, sampling log, augmentation log, metric CSV/JSON, script commit |
| Limitation | toy video 실험을 실제 감시/자율 시스템 안전성으로 일반화하지 않음 |
| GitHub math | `\operatorname` 사용 금지, `\mathrm{sim}`과 짧은 변수명 사용, `v_{<t}` 대신 `v_{1:t-1}` 사용 |

---

## 11. 논문의 고유 기여

1. 비디오 SSL의 pretext task와 representation learning 흐름을 체계화했다.
2. 이미지 SSL과 달리 temporal order, motion, cross-modal signal의 중요성을 보여준다.
3. W05에서 temporal trigger, frame-level poisoning, sampling manipulation, modality mismatch 위험을 논의하는 배경 문헌이 된다.
4. 후속 W07/W08의 멀티모달 LLM, video-RAG, OCR/video context 보안으로 확장 가능하다.
5. 비디오 representation 평가를 action accuracy뿐 아니라 temporal robustness, cross-modal consistency, provenance evidence로 확장하는 근거를 제공한다.

---

## 12. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 보안 직접성 부족 | poisoning/backdoor 전문 문헌은 아니다. | W05 P04/P05와 결합 |
| 재현 비용 | 비디오 SSL pretraining은 데이터와 GPU 비용이 크다. | toy clips와 문헌 기반 비교로 제한 |
| 개인정보 위험 | 비디오 데이터는 얼굴, 위치, 행동, 음성 등 민감정보를 포함할 수 있다. | 공개 데이터 또는 synthetic/toy data만 사용 |
| LLM/Video foundation 확장 필요 | 최신 video foundation model과 MLLM은 추가 문헌 필요 | W07/W08로 연결 |
| 평가 복잡성 | temporal robustness, retrieval, action recognition, cross-modal alignment를 모두 봐야 한다. | 지표를 분리 보고 |
| 악용 위험 | 실제 감시·로봇 시스템 공격 시나리오를 상세화하면 부적절하다. | 원리·평가·방어 중심으로 제한 |

---

## 13. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | SSL이 이미지·텍스트뿐 아니라 비디오 foundation representation으로 확장된다는 문제의식 |
| 2장 관련연구 | 비디오 SSL, temporal representation, cross-modal agreement 정리 |
| 3장 위협모형 | temporal trigger, frame poisoning, sampling manipulation, modality mismatch 정의 |
| 4장 연구방법 | temporal contrastive loss, temporal consistency, masked video modeling, ASR_temp, TemporalRobustness 지표 설계 |
| 5장 분석 | video SSL pipeline과 temporal attack surface matrix 제시 |
| 6장 보안적 함의 | 영상 데이터 프라이버시, 안전성, action misclassification, 책임성 해석 |
| 부록 | clip sampling rule, frame hash, augmentation config, model checkpoint, metric CSV 수록 |

---

## 14. 기말논문 연결 3문장

1. W05에서 기말논문에 반영할 개념: 비디오 SSL은 frame sequence와 temporal consistency를 이용하므로 frame-level poisoning과 temporal trigger가 representation을 왜곡할 수 있다.
2. W05에서 기말논문에 반영할 표·그림·실험: temporal contrastive objective, temporal consistency loss, masked video modeling, ASR_temp, TemporalRobustness, VideoSSLRisk 수식표와 video SSL pipeline 도식을 반영한다.
3. W05가 W07/W08/W14와 연결되는 지점: video-RAG와 멀티모달 LLM은 frame/text/audio context를 함께 사용하므로 temporal/cross-modal provenance와 sampling log를 evidence chain으로 남겨야 한다.

---

## 15. 최종 판단

P03은 W05에서 비디오 SSL과 temporal representation을 설명하는 핵심 문헌이다. 직접 보안 문헌은 아니지만, 시간축 학습이 poisoning/backdoor 공격면을 어떻게 확장하는지 설명하는 데 중요하다. 따라서 기말논문에서는 P03을 **video SSL, temporal representation, frame-level poisoning, temporal trigger, cross-modal consistency, video foundation security의 배경 문헌**으로 사용하는 것이 적절하다.

---

## 16. GitHub 수식 호환성 메모

이 파일에서는 GitHub 수식 렌더링 오류 방지를 위해 `\operatorname`을 사용하지 않는다.

| 피해야 할 표현 | 권장 표현 |
|---|---|
| `\operatorname{sim}` | `\mathrm{sim}` |
| `v_{<t}` | `v_{1:t-1}` |
| `N_{trigger\ success}` | `N_{atk}`처럼 짧은 변수명 사용 후 표에서 의미 설명 |
| `N_{trigger\ clips}` | `N_{trig}`처럼 짧은 변수명 사용 후 표에서 의미 설명 |
| 긴 영문 subscript | 짧은 변수명 사용 후 표에서 의미 설명 |

```bash
pandoc P03_summary.md -o P03_summary.docx
pandoc P03_summary.md -o P03_summary.pdf --pdf-engine=xelatex
```
