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
| PDF 확인 메모 | repo의 PDF 폴더에 P02 관련 PDF blob이 존재함을 확인했다. 요약은 로컬 PDF 경로와 W06 `paper_list.md`의 공식 DOI/arXiv 메타데이터 기준으로 보완했다. |
| 수식 호환성 | GitHub 수식 렌더링 오류 방지를 위해 `\operatorname`을 사용하지 않고, 긴 영문 subscript 대신 짧은 변수명과 표 설명을 사용했다. `v_{<t}` 같은 표현은 쓰지 않고 `v_{1:t-1}` 형식으로 작성했다. |
| 핵심 근거 사용 가능 여부 | 가능. W06에서 image diffusion을 video generation, temporal consistency, video deepfake threat model, 영상 provenance, 시간축 검출 신뢰성으로 확장하는 핵심 문헌으로 사용 |

---

## 1. 한 문장 요약

이 논문은 video diffusion model을 **video generation, video editing, text-to-video, image-to-video, video prediction, video understanding, spatiotemporal denoising, temporal attention, latent video diffusion, controllable generation, temporal consistency, video benchmark, long video generation** 관점에서 정리하며, W06에서는 생성 영상·비디오 딥페이크·영상 provenance·temporal artifact 검출·identity consistency 평가를 이해하기 위한 핵심 survey 문헌이다.

---

## 2. 핵심 연구문제

> 이미지 diffusion을 비디오 영역으로 확장하면 frame 품질뿐 아니라 시간축 일관성, 움직임 자연성, 정체성 유지, 조건부 제어, 긴 영상 생성, 계산 비용, 압축·편집 후 검출 신뢰성까지 함께 평가해야 한다.

| 번호 | 연구질문 |
|---|---|
| RQ1 | Image diffusion을 video diffusion으로 확장할 때 frame 간 temporal consistency는 어떻게 유지되는가? |
| RQ2 | Video diffusion model은 text-to-video, image-to-video, video editing, video prediction, video understanding task에서 어떻게 활용되는가? |
| RQ3 | 2D U-Net, 3D U-Net, temporal attention, spatiotemporal transformer, latent video diffusion 구조는 생성 품질과 비용에 어떤 영향을 주는가? |
| RQ4 | Video diffusion 평가는 single-frame quality뿐 아니라 motion coherence, identity consistency, temporal artifact, audio-visual consistency를 어떻게 측정해야 하는가? |
| RQ5 | 생성 영상은 딥페이크, 허위 증거, 음성·영상 불일치, 인물 정체성 조작, provenance 위조 측면에서 어떤 보안 위험을 만드는가? |

---

## 3. 논문의 핵심 기여

| 기여 | 설명 | W06 연결 |
|---|---|---|
| Video diffusion survey | image diffusion 중심 기존 survey의 한계를 보완하고 video domain 중심으로 정리 | W06의 video deepfake 배경 |
| Task taxonomy | video generation, video editing, video understanding, prediction, controllable generation으로 흐름 분류 | 생성 영상 공격면 분류 |
| Architecture taxonomy | spatiotemporal module, temporal attention, transformer, latent video diffusion 등 구조 정리 | temporal consistency 평가 연결 |
| Evaluation challenge 정리 | 긴 영상, motion consistency, computation cost, dataset/bias, identity consistency 문제 제시 | deepfake reliability 평가 연결 |
| Future direction 제시 | long video, controllability, efficiency, multimodal conditioning, practical deployment 과제 제시 | W14/W15 운영·재현성 연결 |
| 보안 확장 가능성 | 논문 자체는 보안 전문 survey는 아니지만 video deepfake, provenance, detector generalization 문제와 직접 연결 가능 | W06 P04/P05와 결합 |

---

## 4. 목차별 핵심 개괄

| 목차 | 핵심 내용 | 비전공자용 이해 |
|---|---|---|
| 1. Introduction | Video diffusion의 등장 배경, image diffusion 대비 난점, 응용 가능성을 제시한다. | 이미지를 넘어서 움직이는 영상을 생성하는 AI다. |
| 2. Background | Diffusion model, video representation, spatiotemporal modeling, conditioning의 기본 개념을 설명한다. | 영상은 여러 장의 이미지와 시간 정보가 함께 있는 데이터다. |
| 3. Video Generation | text-to-video, image-to-video, unconditional video generation을 정리한다. | 글이나 이미지 조건으로 짧은 영상을 만든다. |
| 4. Video Editing | 기존 영상의 일부를 바꾸거나 motion/style/content를 조정하는 방법을 다룬다. | 원본 영상 일부를 자연스럽게 바꿀 수 있다. |
| 5. Video Understanding | diffusion을 representation learning, prediction, understanding task와 연결한다. | 생성뿐 아니라 영상 이해에도 사용될 수 있다. |
| 6. Architecture | 2D/3D U-Net, temporal layer, attention, transformer, latent diffusion 구조를 정리한다. | 공간과 시간 정보를 함께 처리하는 구조가 필요하다. |
| 7. Evaluation | FVD, frame quality, temporal consistency, motion realism, human evaluation 등을 정리한다. | 영상이 자연스러운지, 시간축으로 흔들리지 않는지 평가한다. |
| 8. Challenges | 긴 영상 생성, 정체성 유지, 계산 비용, 데이터 편향, 안전성, provenance가 과제로 남는다. | 잘 만든 영상일수록 검증과 책임 기록이 중요하다. |

---

## 5. 핵심 이론 및 수식

> 아래 수식은 video diffusion model을 W06 보고서에서 설명하기 위해 표준화한 표현이다. 원문 수식의 직접 전사가 아니라, video diffusion의 구조·평가·보안 연결을 설명하기 위한 보고서용 정식화다. GitHub 호환성을 위해 `\operatorname`은 사용하지 않는다.

### 5.1 Video Forward Diffusion

비디오 $v_0$는 frame sequence 또는 latent tensor로 볼 수 있다. Forward process는 비디오 전체에 noise를 추가한다.

$$
q(v_t\mid v_{t-1})=\mathcal{N}\left(v_t;\sqrt{1-\beta_t}v_{t-1},\beta_t I\right)
$$

| 기호 | 의미 |
|---|---|
| $v_0$ | 원본 video clip 또는 latent video representation |
| $v_t$ | $t$단계 noise가 추가된 video tensor |
| $\beta_t$ | noise schedule |
| $I$ | 단위 공분산 행렬 |

### 보안적 의미

비디오 생성은 단일 이미지보다 더 많은 신원·행동·상황 정보를 포함한다. 따라서 얼굴, 행동, 장소, 음성-입술 정합성 등 복합 개인정보와 신뢰성 위험이 커진다.

---

### 5.2 Video Denoising Objective

Video diffusion은 noisy video에서 noise를 예측하도록 학습한다.

$$
\mathcal{L}_{video}=\mathbb{E}_{t,v_0,\epsilon}\left[\left\|\epsilon-\epsilon_{\theta}(v_t,t,c)\right\|_2^2\right]
$$

| 기호 | 의미 |
|---|---|
| $\epsilon$ | 실제 주입된 noise |
| $\epsilon_{\theta}$ | video diffusion model이 예측한 noise |
| $c$ | text, image, pose, motion, audio 등 condition |

### 보안적 의미

Condition $c$가 text prompt, reference image, pose, audio 등으로 주어질수록 공격자는 특정 인물·행동·상황을 더 세밀하게 유도할 수 있다. 따라서 생성 로그에는 prompt, reference media, seed, model version, sampler를 함께 기록해야 한다.

---

### 5.3 Temporal Consistency Loss

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

### 5.4 Text-to-Video Conditional Generation

Text-to-video generation은 텍스트 조건을 기반으로 비디오를 생성한다.

$$
v_{1:T}\sim p_{\theta}(v_{1:T}\mid z)
$$

| 기호 | 의미 |
|---|---|
| $v_{1:T}$ | 생성된 video frame sequence |
| $z$ | text prompt 또는 기타 생성 조건 |

### 보안적 의미

Text prompt만으로 특정 사건, 인물, 장소, 행동을 영상화할 수 있으면 허위 영상 증거, 정치·사회적 조작, 사회공학 공격 위험이 커진다. W06에서는 실제 인물 대상 생성 대신 synthetic/toy scenario와 문헌 기반 분석으로 제한해야 한다.

---

### 5.5 Video-level Fake Score

생성 영상 검출은 frame-level prediction과 video-level aggregation을 함께 고려한다.

$$
Score_{video}=\mathrm{Agg}\left(\{s_i=f_{\psi}(\hat{v}_i)\}_{i=1}^{T}\right)
$$

| 기호 | 의미 |
|---|---|
| $s_i$ | $i$번째 frame의 fake score |
| $\mathrm{Agg}$ | 평균, 최대값, temporal model 등 aggregation 방식 |
| $Score_{video}$ | video-level fake score |

### 보안적 의미

Frame 하나만 보고 판정하면 압축·편집·flicker·scene change에 취약할 수 있다. Video deepfake 검출은 temporal artifact와 video-level consistency를 함께 봐야 한다.

---

### 5.6 Temporal Artifact Score

생성 영상의 시간축 흔들림과 정체성 drift를 단순화해 측정한다.

$$
TempArtifact=\frac{1}{T-1}\sum_{i=1}^{T-1}\left\|\Phi(\hat{v}_{i+1})-\Phi(\hat{v}_{i})\right\|_2
$$

### 보안적 의미

Temporal artifact가 높으면 생성 영상일 가능성이 높아질 수 있다. 그러나 최신 video diffusion은 artifact를 줄이는 방향으로 발전하므로 detector는 지속적으로 cross-model 검증이 필요하다.

---

### 5.7 Identity Consistency

인물 영상에서는 frame 간 identity representation이 얼마나 유지되는지 평가해야 한다.

$$
IDConsistency=1-\frac{1}{T-1}\sum_{i=1}^{T-1}\left\|g(\hat{v}_{i+1})-g(\hat{v}_{i})\right\|_2
$$

| 기호 | 의미 |
|---|---|
| $g$ | identity feature extractor |
| $\hat{v}_i$ | 생성된 $i$번째 frame |

### 보안적 의미

Identity consistency가 높으면 영상이 더 자연스러워 보이지만, 신원 사칭 딥페이크의 설득력도 높아질 수 있다.

---

### 5.8 Video Provenance Coverage

생성 영상의 출처·워터마크·metadata가 얼마나 남아 있는지 측정한다.

$$
VideoProvCoverage=\frac{N_{vp}}{N_{video}}
$$

| 기호 | 의미 |
|---|---|
| $N_{video}$ | 평가 대상 생성 영상 수 |
| $N_{vp}$ | provenance 또는 watermark가 정상 확인된 영상 수 |

### 보안적 의미

Video provenance가 없으면 허위 증거, 합성 뉴스, 정치·사회적 조작, 저작권 분쟁에서 검증이 어렵다.

---

## 6. AI 원리 70% 관점 분석

| 원리 항목 | 설명 | W06/P02에서의 의미 |
|---|---|---|
| Video as tensor | 비디오를 시간축을 가진 이미지 sequence 또는 latent tensor로 표현 | image diffusion을 video domain으로 확장 |
| Spatiotemporal denoising | 공간 정보와 시간 정보를 동시에 복원 | frame 품질과 motion coherence 동시 처리 |
| Temporal attention | frame 간 관계를 attention으로 모델링 | 긴 영상·정체성 유지에 필요 |
| Conditional generation | text, image, pose, motion, audio를 조건으로 사용 | controllable video generation과 misuse 가능성 |
| Latent video diffusion | 고차원 video를 latent space에서 처리 | 비용 절감과 고해상도 생성 가능성 |
| Video editing | 기존 영상의 일부를 조건에 맞게 수정 | 증거 조작·부분 합성 위험 |
| Video understanding | 생성뿐 아니라 representation/understanding task에도 diffusion 활용 | 보안 분석·검출 모델과 연결 |
| Long video generation | 긴 시간축의 일관성을 유지하는 생성 | 검출·감사·저장 비용 증가 |

---

## 7. 보안 이슈 30% 관점 분석

| 보안 항목 | Video Diffusion 관점 해석 | 대표 평가 지표 |
|---|---|---|
| 기밀성 | 얼굴, 행동, 장소, 음성-입술 정보가 복합적으로 노출될 수 있음 | re-identification risk, leakage score |
| 무결성 | 허위 영상 증거, 사건 재현 조작, 신원 사칭이 가능 | detection AUC, temporal artifact score |
| 가용성 | 대량 합성 영상으로 검토·포렌식 시스템 부담 증가 | review cost, latency, throughput |
| 프라이버시 | reference image/video 기반 생성이 개인 특징을 재현할 수 있음 | identity similarity, memorization risk |
| 안전성 | 의료·법률·정치·재난 영상에서 잘못된 판단 유도 가능 | high-stakes review flag |
| 책임성 | prompt, reference media, seed, model, sampler, output hash 기록 필요 | provenance coverage, audit completeness |

---

## 8. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | 얼굴 영상, 음성-영상 정합성, identity, reference image/video, text prompt, model checkpoint, watermark, provenance metadata |
| 공격자 목표 | video deepfake 생성, 신원 사칭, 허위 사건 영상 제작, 검출 회피, provenance 제거 |
| 공격자 능력 | text-to-video prompt, image-to-video reference, pose/motion control, post-processing, compression, frame editing |
| 공격 경로 | reference/text condition → video diffusion model → generated video → editing/compression → distribution |
| 방어자 능력 | video deepfake detector, watermark, provenance log, temporal consistency analysis, human review, output hashing |
| 제외 범위 | 실제 인물 사칭 영상 제작, 유해·불법 영상 생성, 무단 개인정보 영상 사용, 실제 서비스 공격, 탐지 우회 절차 제공 |

---

## 9. 평가방법 및 지표

| 평가축 | 지표 | 의미 | W06/P02 활용 |
|---|---|---|---|
| Video quality | FVD, IS, CLIPScore | 생성 품질과 prompt 정합성 | 품질 baseline |
| Temporal consistency | TempArtifact, motion coherence | frame 간 자연스러움 | deepfake 검출 단서 |
| Identity | IDConsistency | 인물 정체성 유지 정도 | 신원 사칭 위험 |
| Detection | AUC, recall, FPR | 생성 영상 검출 성능 | detector 평가 |
| Provenance | VideoProvCoverage | watermark/metadata 확인 | 출처 확인 |
| Privacy | re-identification risk | 개인 특징 재현 가능성 | 프라이버시 평가 |
| Robustness | compression/editing robustness | 압축·편집 후 검출 유지 | 실전 신뢰성 |
| Reproducibility | prompt, seed, model, sampler, output hash | 재현 가능성 | W15 evidence chain |

---

## 10. 재현성 체크리스트

| 항목 | 기록해야 할 내용 |
|---|---|
| Bibliographic status | DOI, ACM CSUR 출판정보, arXiv 판본, 강의계획서 표기 차이, 로컬 PDF 상태 |
| Model | video diffusion model 이름, checkpoint, license, version |
| Sampling config | sampler, step 수, seed, guidance scale, frame 수, FPS, resolution, scheduler |
| Condition | text prompt, reference image/video, pose, motion, audio condition, preprocessing |
| Data | 공개 toy video 또는 synthetic sample만 사용, 개인정보·실제 인물 영상 제외 |
| Output | video hash, frame hash, watermark 여부, provenance metadata, post-processing 여부 |
| Evaluation | FVD/CLIPScore 등 품질 지표와 TempArtifact, IDConsistency, Detection AUC, FPR 분리 |
| Security controls | watermark, detector, content policy, human review, safe logging |
| Evidence | config file, prompt log, output hash, metric CSV/JSON, script commit |
| GitHub math | `\operatorname` 사용 금지, `v_{<t}` 대신 `v_{1:t-1}` 형식 사용, 긴 영문 subscript는 짧은 변수명과 표 설명 사용 |

---

## 11. 논문의 고유 기여

1. Video diffusion model 연구를 task, architecture, evaluation, application 관점에서 체계적으로 정리한다.
2. Image diffusion에서 video diffusion으로 넘어갈 때 temporal consistency와 motion coherence가 핵심 문제가 됨을 보여준다.
3. Video deepfake와 합성 영상 검출에서 frame-level 품질뿐 아니라 video-level consistency 평가가 필요하다는 근거를 제공한다.
4. Text-to-video와 image-to-video 조건부 생성이 허위 영상 증거, 신원 사칭, privacy leakage, provenance 위조 문제로 확장될 수 있음을 설명한다.
5. W14/W15에서 영상 생성 로그, output hash, watermark, provenance metadata를 evidence chain으로 남겨야 하는 근거가 된다.

---

## 12. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 강의계획서 표기 차이 | 강의계획서 지정 P02와 로컬/공식 확인 논문의 제목·저자 표기가 다르다. | DOI 기준 인용, 최종 제출 전 교수자 확인 |
| 보안 직접성 부족 | video diffusion survey 자체는 딥페이크 검출 전문 문헌이 아니다. | W06 P04/P05 deepfake detection 문헌과 결합 |
| 재현 비용 | video diffusion은 GPU, storage, 시간 비용이 크다. | toy video와 공개 예시 기준으로 제한 |
| 평가 복잡성 | temporal consistency, identity, motion, compression robustness를 모두 평가해야 한다. | 지표를 분리 보고 |
| privacy 위험 | 실제 인물 reference video 사용은 윤리·법적 문제가 있다. | synthetic/reference-free toy scenario 사용 |
| 악용 위험 | 실제 딥페이크 생성 절차를 상세화하면 부적절하다. | 원리·평가·방어 중심으로 제한 |

---

## 13. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | 생성형 AI가 이미지에서 영상으로 확장되며 temporal consistency와 video provenance 문제가 중요해진다는 문제의식 |
| 2장 관련연구 | video diffusion model taxonomy와 architecture 정리 |
| 3장 위협모형 | reference media, text prompt, pose/motion condition, output video, watermark, provenance metadata 보호 자산 정의 |
| 4장 연구방법 | video forward diffusion, denoising loss, temporal consistency, video-level fake score, IDConsistency, VideoProvCoverage 지표 설계 |
| 5장 분석 | video diffusion pipeline과 video deepfake security risk matrix 제시 |
| 6장 보안적 함의 | 허위 영상 증거, 신원 사칭, temporal artifact, detector generalization, provenance 필요성 해석 |
| 부록 | prompt, seed, model version, sampler, frame/FPS/resolution, output hash, watermark/provenance log 수록 |

---

## 14. 기말논문 연결 3문장

1. W06에서 기말논문에 반영할 개념: Video diffusion은 image diffusion을 시간축으로 확장한 생성모형이며, frame 품질뿐 아니라 temporal consistency와 identity consistency가 영상 신뢰성의 핵심이 된다.
2. W06에서 기말논문에 반영할 표·그림·실험: video forward diffusion, denoising objective, temporal consistency, Score_video, TempArtifact, IDConsistency, VideoProvCoverage 수식표와 video generation-provenance-detection pipeline을 반영한다.
3. W06이 W14/W15와 연결되는 지점: 생성 영상은 prompt, reference media, seed, sampler, frame hash, video hash, watermark, provenance metadata를 evidence chain으로 남겨야 재현성과 책임성을 확보할 수 있다.

---

## 15. 최종 판단

P02는 W06의 video diffusion 확장 핵심 문헌이다. 직접적인 딥페이크 검출 논문은 아니지만, 고품질 생성 영상이 어떻게 만들어지고 왜 temporal consistency·identity consistency·provenance가 중요한지 설명한다. 따라서 기말논문에서는 P02를 **video diffusion generation pipeline, temporal consistency, video deepfake threat model, video-level detection, identity/provenance 평가의 배경 문헌**으로 사용하는 것이 적절하다.

---

## 16. GitHub 수식 호환성 메모

이 파일에서는 GitHub 수식 렌더링 오류 방지를 위해 `\operatorname`을 사용하지 않는다.

| 피해야 할 표현 | 권장 표현 |
|---|---|
| `\operatorname{Agg}` | `\mathrm{Agg}` |
| `v_{<t}` | `v_{1:t-1}` |
| `c_{text}` | `z` 또는 표에서 설명한 짧은 변수명 |
| `N_{provenance\ detected}` | `N_{vp}`처럼 짧은 변수명 사용 후 표에서 의미 설명 |
| 긴 영문 subscript | 짧은 변수명 사용 후 표에서 의미 설명 |

```bash
pandoc P02_summary.md -o P02_summary.docx
pandoc P02_summary.md -o P02_summary.pdf --pdf-engine=xelatex
```
