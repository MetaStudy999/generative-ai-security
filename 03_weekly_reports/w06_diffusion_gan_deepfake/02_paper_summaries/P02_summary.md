# P02 Summary

## A Survey on Video Diffusion Models — Zhen Xing et al., ACM Computing Surveys, 2025

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W06 확률생성모형(Diffusion/GAN) & 딥페이크 검출 |
| 논문명 | A Survey on Video Diffusion Models |
| 저자 | Zhen Xing, Qijun Feng, Haoran Chen, Qi Dai, Han Hu, Hang Xu, Zuxuan Wu, Yu-Gang Jiang |
| 공식 출판 정보 | ACM Computing Surveys, Vol. 57, No. 2, pp. 1–42, online 2024-11-07, print issue 2025-02-28 |
| DOI | https://doi.org/10.1145/3696415 |
| 보조 URL | https://arxiv.org/abs/2310.10647 |
| 로컬 PDF | `01_papers/pdf/02_Xing_et_al_2024_Video_Diffusion_Models_Survey.pdf` |
| 검증 상태 | W06 `paper_list.md` 기준 DOI 확인. 강의계획서 지정 P02 `Ananya Högele et al., Video Diffusion Models: A Survey`와 제목·저자 표기가 달라 최종 제출 전 교수자 확인 필요 |
| PDF 확인 메모 | repo의 PDF 폴더에 해당 PDF blob이 존재함을 확인했다. 요약은 로컬 PDF 경로와 공식 DOI/arXiv 메타데이터 기준으로 보완했다. |
| 핵심 근거 사용 가능 여부 | 가능. W06에서 image diffusion을 video generation, temporal consistency, video deepfake threat model로 확장하는 핵심 문헌 |

---

## 1. 한 문장 요약

이 논문은 video diffusion model을 **video generation, video editing, video understanding, spatiotemporal denoising, temporal consistency, text-to-video generation, image-to-video generation, controllable generation, evaluation, future challenge** 관점에서 정리하며, W06에서 생성 영상·비디오 딥페이크·영상 provenance·temporal artifact 검출을 이해하기 위한 핵심 survey 문헌이다.

---

## 2. 핵심 연구문제

> 이미지 diffusion의 성공을 비디오 영역으로 확장할 때, 시간축 일관성·동작 표현·긴 영상 생성·조건부 제어·평가 지표·보안 위험을 어떻게 체계화할 수 있는가?

| 번호 | 연구질문 |
|---|---|
| RQ1 | Image diffusion을 video diffusion으로 확장할 때 frame 간 temporal consistency는 어떻게 유지되는가? |
| RQ2 | Video diffusion model은 text-to-video, image-to-video, video editing, video prediction, video understanding task에서 어떻게 활용되는가? |
| RQ3 | 2D U-Net, 3D U-Net, temporal attention, spatiotemporal transformer 등 architecture 선택은 생성 품질과 비용에 어떤 영향을 주는가? |
| RQ4 | Video diffusion의 평가에서는 single-frame quality뿐 아니라 motion coherence, identity consistency, temporal artifact를 어떻게 측정해야 하는가? |
| RQ5 | 생성 영상은 딥페이크, 허위 증거, 음성·영상 불일치, 인물 정체성 조작, provenance 위조 측면에서 어떤 보안 위험을 만드는가? |

---

## 3. 논문의 핵심 기여

| 기여 | 설명 | W06 연결 |
|---|---|---|
| Video diffusion survey | image diffusion 중심 기존 survey의 한계를 보완하고 video domain 중심으로 정리 | W06의 video deepfake 배경 |
| Task taxonomy | video generation, video editing, video understanding 등으로 연구 흐름 분류 | 생성 영상 공격면 분류 |
| Architecture taxonomy | spatiotemporal module, temporal attention, transformer, latent video diffusion 등 구조 정리 | temporal consistency 평가 연결 |
| Evaluation challenge 정리 | 긴 영상, motion consistency, computation cost, dataset/bias 문제 제시 | deepfake reliability 평가 연결 |
| Future direction 제시 | long video, controllability, efficiency, multimodal conditioning, practical deployment 과제 제시 | W14/W15 운영·재현성 연결 |

---

## 4. 핵심 이론 및 수식

> 아래 수식은 video diffusion model을 W06 보고서에서 설명하기 위해 표준화한 표현이다. 원문 수식을 직접 전사한 것이 아니라, video diffusion의 구조·평가·보안 연결을 설명하기 위한 보고서용 정식화다.

### 4.1 Video Forward Diffusion

비디오 $v_0$는 frame sequence 또는 latent tensor로 볼 수 있다. Forward process는 비디오 전체에 noise를 추가한다.

$$
q(v_t\mid v_{t-1})=\mathcal{N}\left(v_t;\sqrt{1-\beta_t}v_{t-1},\beta_t I\right)
$$

| 기호 | 의미 |
|---|---|
| $v_0$ | 원본 video clip 또는 latent video representation |
| $v_t$ | $t$단계 noise가 추가된 video tensor |
| $\beta_t$ | noise schedule |

### 보안적 의미

비디오 생성은 단일 이미지보다 더 많은 신원·행동·상황 정보를 포함한다. 따라서 얼굴, 행동, 장소, 음성-입술 정합성 등 복합 개인정보와 신뢰성 위험이 커진다.

---

### 4.2 Video Denoising Objective

Video diffusion은 noisy video에서 noise를 예측하도록 학습한다.

$$
\mathcal{L}_{video}=\mathbb{E}_{t,v_0,\epsilon}\left[\left\|\epsilon-\epsilon_\theta(v_t,t,c)\right\|_2^2\right]
$$

| 기호 | 의미 |
|---|---|
| $\epsilon$ | 실제 주입된 noise |
| $\epsilon_\theta$ | video diffusion model이 예측한 noise |
| $c$ | text, image, pose, motion, audio 등 condition |

### 보안적 의미

Condition $c$가 text prompt, reference image, pose, audio 등으로 주어질수록 공격자는 특정 인물·행동·상황을 더 세밀하게 유도할 수 있다. 따라서 생성 로그에는 prompt, reference media, seed, model version, sampler를 함께 기록해야 한다.

---

### 4.3 Temporal Consistency Loss

비디오 생성은 frame별 품질뿐 아니라 시간축 일관성이 중요하다.

$$
\mathcal{L}_{temp}=\sum_{i=1}^{T-1}\left\|\Phi(\hat{v}_i)-\Phi(\hat{v}_{i+1})\right\|_2^2
$$

| 기호 | 의미 |
|---|---|
| $\hat{v}_i$ | 생성된 $i$번째 frame |
| $\Phi$ | feature extractor 또는 temporal representation |
| $T$ | frame 수 |

### 보안적 의미

Frame flicker, identity drift, pose inconsistency, unnatural motion은 video deepfake 검출 단서가 될 수 있다. 반대로 모델이 temporal consistency를 잘 유지하면 검출 난이도는 높아진다.

---

### 4.4 Text-to-Video Conditional Generation

Text-to-video generation은 텍스트 조건을 기반으로 비디오를 생성한다.

$$
v_{1:T}\sim p_\theta(v_{1:T}\mid c_{text})
$$

| 기호 | 의미 |
|---|---|
| $v_{1:T}$ | 생성된 video frame sequence |
| $c_{text}$ | text prompt |

### 보안적 의미

Text prompt만으로 특정 사건, 인물, 장소, 행동을 영상화할 수 있으면 허위 영상 증거, 정치·사회적 조작, 사회공학 공격 위험이 커진다. W06에서는 실제 인물 대상 생성 대신 synthetic/toy scenario와 문헌 기반 분석으로 제한해야 한다.

---

### 4.5 Video Detection Risk

생성 영상 검출은 frame-level prediction과 video-level aggregation을 함께 고려한다.

$$
Score_{video}=Agg\left(\{s_i=f_\psi(\hat{v}_i)\}_{i=1}^{T}\right)
$$

| 기호 | 의미 |
|---|---|
| $s_i$ | $i$번째 frame의 fake score |
| $Agg$ | 평균, 최대값, temporal model 등 aggregation 방식 |
| $Score_{video}$ | video-level fake score |

### 보안적 의미

Frame 하나만 보고 판정하면 압축·편집·flicker·scene change에 취약할 수 있다. Video deepfake 검출은 temporal artifact와 video-level consistency를 함께 봐야 한다.

---

## 5. AI 원리 70% 관점 분석

| 원리 항목 | 설명 | W06/P02에서의 의미 |
|---|---|---|
| Video as tensor | 비디오를 시간축을 가진 이미지 sequence 또는 latent tensor로 표현 | image diffusion을 video domain으로 확장 |
| Spatiotemporal denoising | 공간 정보와 시간 정보를 동시에 복원 | frame 품질과 motion coherence 동시 처리 |
| Temporal attention | frame 간 관계를 attention으로 모델링 | 긴 영상·정체성 유지에 필요 |
| Conditional generation | text, image, pose, motion, audio를 조건으로 사용 | controllable video generation과 misuse 가능성 |
| Latent video diffusion | 고차원 video를 latent space에서 처리 | 비용 절감과 고해상도 생성 가능성 |
| Video editing | 기존 영상의 일부를 조건에 맞게 수정 | 증거 조작·부분 합성 위험 |
| Video understanding | 생성뿐 아니라 representation/understanding task에도 diffusion 활용 | 보안 분석·검출 모델과 연결 |

---

## 6. 보안 이슈 30% 관점 분석

| 보안 항목 | Video Diffusion 관점 해석 | 대표 평가 지표 |
|---|---|---|
| 기밀성 | 얼굴, 행동, 장소, 음성-입술 정보가 복합적으로 노출될 수 있음 | re-identification risk, leakage score |
| 무결성 | 허위 영상 증거, 사건 재현 조작, 신원 사칭이 가능 | detection AUC, temporal artifact score |
| 가용성 | 대량 합성 영상으로 검토·포렌식 시스템 부담 증가 | review cost, latency, throughput |
| 프라이버시 | reference image/video 기반 생성이 개인 특징을 재현할 수 있음 | identity similarity, memorization risk |
| 안전성 | 의료·법률·정치·재난 영상에서 잘못된 판단 유도 가능 | high-stakes review flag |
| 책임성 | prompt, reference media, seed, model, sampler, output hash 기록 필요 | provenance coverage, audit completeness |

---

## 7. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | 얼굴 영상, 음성-영상 정합성, identity, reference image/video, text prompt, model checkpoint, watermark, provenance metadata |
| 공격자 목표 | video deepfake 생성, 신원 사칭, 허위 사건 영상 제작, 검출 회피, provenance 제거 |
| 공격자 능력 | text-to-video prompt, image-to-video reference, pose/motion control, post-processing, compression, frame editing |
| 공격 경로 | reference/text condition → video diffusion model → generated video → editing/compression → distribution |
| 방어자 능력 | video deepfake detector, watermark, provenance log, temporal consistency analysis, human review |
| 제외 범위 | 실제 인물 사칭 영상 제작, 유해·불법 영상 생성, 무단 개인정보 영상 사용, 실제 서비스 공격 |

---

## 8. 평가방법 및 지표

| 평가축 | 지표 | 의미 | W06/P02 활용 |
|---|---|---|---|
| Video quality | FVD, FID, user preference | 생성 영상 품질 | 생성 성능 배경 |
| Text-video alignment | CLIP score, video-text retrieval score | prompt와 영상 내용 일치 | text-to-video 평가 |
| Temporal consistency | frame consistency, optical-flow consistency | flicker와 motion coherence 평가 | deepfake artifact 연결 |
| Identity consistency | face embedding similarity, identity drift | 인물 정체성 유지 여부 | 신원 사칭·검출 연결 |
| Detection performance | AUC, F1, FPR/FNR | 생성 영상 검출 성능 | P04/P05와 연결 |
| Robustness | compression robustness, crop/noise robustness | 플랫폼 업로드 후 검출 유지 | 운영 평가 |
| Provenance | watermark robustness, metadata preservation | 생성·편집 이력 추적 | W13/W14/W15 연결 |
| Cost | GPU memory, sampling latency, step count | 실제 서비스 가능성 | MLOps 연결 |

---

## 9. 재현성 체크리스트

| 항목 | 기록해야 할 내용 |
|---|---|
| 모델 | video diffusion model name, checkpoint, license, model card |
| 데이터 | video dataset, frame rate, resolution, clip length, preprocessing |
| 조건 | text prompt, reference image/video, pose/motion/audio condition |
| Sampler | sampler type, step count, scheduler, guidance scale |
| 출력 | video hash, frame count, codec, compression setting, output path |
| 평가 | FVD, temporal consistency, identity consistency, detection AUC, watermark score |
| 보안 로그 | prompt-reference-output-provenance log, human review record |
| 한계 | toy/synthetic video 결과를 실제 딥페이크 탐지 신뢰성으로 일반화하지 않음 |

---

## 10. 논문의 고유 기여

1. Video diffusion research를 generation, editing, understanding task로 체계적으로 분류한다.
2. Image diffusion을 video domain으로 확장할 때 생기는 temporal consistency, long video, computation cost 문제를 정리한다.
3. Text-to-video, image-to-video, controllable generation 등 AIGC 시대의 핵심 응용을 정리한다.
4. Video deepfake와 합성 영상 provenance 평가를 위한 모델 구조와 평가 지표 배경을 제공한다.
5. W06의 deepfake creation/detection 문헌(P04/P05)과 연결되는 생성 원리 측면의 기반을 제공한다.

---

## 11. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 직접 보안 문헌은 아님 | P02는 video diffusion survey이며 deepfake detector 전문 문헌은 아니다. | P04/P05와 결합해 보안 평가표 구성 |
| 긴 영상 생성 한계 | 긴 video에서 identity drift, temporal inconsistency, cost 문제가 커진다. | temporal consistency와 identity consistency를 별도 지표로 둔다. |
| 평가 지표 불완전 | FVD/CLIP 등은 안전성이나 진위성을 직접 보장하지 않는다. | detection AUC, provenance, watermark, human review를 병기한다. |
| 데이터 편향 | 학습 video dataset의 인물·문화·장면 편향이 생성물에 반영될 수 있다. | dataset provenance와 failure case를 기록한다. |
| 악용 가능성 | text-to-video와 video editing은 허위 영상 생성에 악용될 수 있다. | 실제 인물 대상 생성 없이 문헌·toy 평가로 제한한다. |

---

## 12. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | 생성형 AI 보안이 이미지에서 영상으로 확장되며, temporal consistency와 provenance가 중요해진다는 문제의식 |
| 2장 관련연구 | video diffusion taxonomy, text-to-video, image-to-video, video editing 연구 흐름 |
| 3장 위협모형 | text/reference/motion condition, generated video, compression, provenance log 보호 자산 정의 |
| 4장 연구방법 | FVD, temporal consistency, identity consistency, detection AUC, watermark robustness 지표 설계 |
| 5장 분석 | video generation-detection-provenance pipeline 표 또는 그림 제시 |
| 6장 보안적 함의 | 허위 영상 증거, 신원 사칭, human review, 법·윤리적 한계 논의 |

---

## 13. 기말논문 연결 3문장

1. W06에서 기말논문에 반영할 개념: video diffusion은 text/image/video condition을 통해 고품질 합성 영상을 생성할 수 있으므로, 생성 품질뿐 아니라 temporal consistency, identity consistency, provenance, 검출 신뢰성을 함께 평가해야 한다.
2. W06에서 기말논문에 반영할 표·그림·실험: video diffusion pipeline, text-to-video threat model, frame-level/video-level detection score, temporal artifact 평가표를 반영한다.
3. W06이 RAG/LLM 보안 감사 프레임워크와 연결되는 지점: 생성 영상은 멀티모달 RAG와 AI 에이전트의 입력 근거가 될 수 있으므로, 영상 출처·생성 로그·watermark·human review를 W14/W15 evidence chain에 포함해야 한다.

---

## 14. 최종 판단

P02는 W06에서 video diffusion의 핵심 문헌이다. P01이 diffusion의 일반 원리를 제공한다면, P02는 시간축이 포함된 생성 영상으로 확장하면서 생기는 temporal consistency, long video, controllability, video deepfake 위험을 설명한다. 따라서 W06 기말논문 연결에서는 P02를 **비디오 합성물 위협모형과 평가 지표 설계의 근거 문헌**으로 사용하는 것이 적절하다.

---

## 15. 변환 호환성 메모

```bash
pandoc P02_summary.md -o P02_summary.docx
pandoc P02_summary.md -o P02_summary.pdf --pdf-engine=xelatex
```
