# P01 Summary

## Diffusion Models: A Comprehensive Survey of Methods and Applications — Ling Yang et al., ACM Computing Surveys, 2024

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W06 확률생성모형(Diffusion/GAN) & 딥페이크 검출 |
| 논문명 | Diffusion Models: A Comprehensive Survey of Methods and Applications |
| 저자 | Ling Yang et al. |
| 학술지 | ACM Computing Surveys |
| 권호/쪽 | Vol. 56, No. 4, Article 105 |
| 연도 | online 2023 / print 2024 |
| DOI | https://doi.org/10.1145/3626235 |
| 보조 URL | https://arxiv.org/abs/2209.00796 |
| 로컬 PDF | `01_papers/pdf/01_Yang_et_al_2023_Diffusion_Models_Comprehensive_Survey.pdf` |
| 검증 상태 | W06 `paper_list.md` 기준 DOI/URL 확인 |

---

## 1. 한 문장 요약

이 논문은 diffusion model을 **forward noising, reverse denoising, score-based modeling, sampling, conditioning, applications** 관점에서 체계화하고, W06에서 생성형 AI의 합성 이미지·딥페이크·watermark·검출 문제를 이해하기 위한 핵심 확률생성모형 배경을 제공한다.

---

## 2. 연구문제

| 번호 | 연구질문 |
|---|---|
| RQ1 | Diffusion model은 데이터를 점진적으로 noise화하고 다시 복원하는 과정을 어떻게 학습하는가? |
| RQ2 | DDPM, score-based model, latent diffusion은 어떤 공통 원리와 차이를 갖는가? |
| RQ3 | Conditioning과 guidance는 text-to-image, image editing, video generation에 어떤 역할을 하는가? |
| RQ4 | Diffusion 기반 생성물이 딥페이크·저작권·개인정보·워터마킹 평가에 어떤 보안 문제를 만드는가? |

---

## 3. 핵심 이론 및 수식

### 3.1 Forward Diffusion

$$
q(x_t\mid x_{t-1})=\mathcal{N}\left(x_t;\sqrt{1-\beta_t}x_{t-1},\beta_t I\right)
$$

| 기호 | 의미 |
|---|---|
| $x_0$ | 원본 데이터 |
| $x_t$ | $t$번째 noise 단계 데이터 |
| $\beta_t$ | noise schedule |

**보안 해석:** 생성모형은 학습 데이터 분포를 근사한다. 학습 데이터에 얼굴·저작물·민감정보가 포함되면 생성 결과와 프라이버시·저작권 이슈로 이어질 수 있다.

### 3.2 Reverse Denoising

$$
p_\theta(x_{t-1}\mid x_t)=\mathcal{N}\left(x_{t-1};\mu_\theta(x_t,t),\Sigma_\theta(x_t,t)\right)
$$

### 3.3 Denoising Loss

$$
\mathcal{L}_{simple}=\mathbb{E}_{t,x_0,\epsilon}\left[\left\|\epsilon-\epsilon_\theta(x_t,t)\right\|_2^2\right]
$$

**보안 해석:** 생성 품질 향상은 합성 이미지 탐지 난이도를 높인다. 따라서 W06에서는 생성 품질, 탐지 성능, 워터마크, provenance evidence를 분리해 평가해야 한다.

---

## 4. AI 원리 관점 분석

| 항목 | 분석 |
|---|---|
| Forward process | 원본 데이터를 Gaussian noise로 점진적으로 변환한다. |
| Reverse process | noise에서 data sample을 복원하도록 학습한다. |
| Score/Denoising | noise 예측 또는 score 추정이 핵심 학습 목표가 된다. |
| Sampling | 생성 품질과 속도는 sampler와 step 수에 영향을 받는다. |
| Conditioning | text, class, image condition이 생성 방향을 제어한다. |
| Latent Diffusion | latent space에서 diffusion을 수행해 비용을 줄인다. |

---

## 5. 보안 이슈 관점 분석

| 보안 항목 | Diffusion 관점 해석 |
|---|---|
| 기밀성 | 학습 데이터 memorization과 민감 이미지 재생성 위험이 있다. |
| 무결성 | 합성 이미지가 증거·인증·여론 조작에 사용될 수 있다. |
| 가용성 | 고품질 합성물 증가로 검출 시스템 부하가 커진다. |
| 저작권 | 학습 데이터와 생성물의 권리 문제가 발생할 수 있다. |
| 책임성 | 생성 모델, prompt, seed, watermark, provenance 기록이 필요하다. |

---

## 6. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 대상 | 얼굴 이미지, 신원, 저작물, 생성 prompt, model checkpoint, provenance log |
| 공격자 목표 | 합성 이미지 생성, 신원 사칭, 허위 시각 증거 생성, 검출 회피 |
| 공격자 능력 | text prompt 조작, image editing, model fine-tuning, watermark 제거 시도 |
| 공격 경로 | training data → diffusion model → conditioned generation → synthetic media distribution |
| 제외 범위 | 실제 인물 사칭물 제작, 무단 개인정보 사용, 유해 딥페이크 생성 |

---

## 7. 평가방법 및 지표

| 지표 | 의미 | W06/P01에서의 활용 |
|---|---|---|
| FID/KID | 생성 이미지 품질·분포 유사성 | 생성 품질 배경 |
| CLIP Score | text-image alignment | prompt-conditioned generation 평가 |
| Detection AUC | 합성물 검출 성능 | 딥페이크 검출 연결 |
| Watermark Robustness | watermark 유지율 | provenance 평가 |
| Leakage Risk | 학습 데이터 재현 위험 | 프라이버시 평가 |
| Latency/Cost | sampling 비용 | 운영 가능성 |

---

## 8. 재현성 점검

| 항목 | 점검 |
|---|---|
| 모델 | diffusion variant, sampler, step 수, guidance scale 기록 |
| 데이터 | 공개 데이터셋 또는 synthetic toy data 사용 |
| 생성 로그 | prompt, seed, model version, output hash 기록 |
| 보안 평가 | detection AUC, watermark, provenance, failure case 저장 |
| 한계 | toy generation 결과를 실제 딥페이크 탐지 성능으로 일반화하지 않음 |

---

## 9. 기말논문 반영 위치

| 장 | 반영 내용 |
|---|---|
| 2장 관련연구 | diffusion model 원리와 응용 정리 |
| 3장 위협모형 | 합성 이미지·prompt·checkpoint·provenance 공격면 정의 |
| 4장 연구방법 | 생성품질, 검출성능, provenance, watermark 지표 설계 |
| 6장 보안적 함의 | 딥페이크, 저작권, 프라이버시, 책임성 해석 |

---

## 10. 기말논문 연결 3문장

1. W06에서 기말논문에 반영할 개념: Diffusion model은 고품질 합성물을 생성할 수 있으므로 생성물 신뢰성, provenance, 검출 가능성을 함께 평가해야 한다.
2. 반영할 표·그림·실험: forward/reverse diffusion 수식, 생성 pipeline, detection AUC·watermark·provenance 평가표를 반영한다.
3. RAG/LLM 보안 연결: 이미지·비디오 생성물도 멀티모달 RAG의 입력 또는 근거 자료가 될 수 있으므로 provenance와 생성 로그 감사가 필요하다.

---

## 11. 최종 판단

P01은 W06의 확률생성모형 원리 핵심 문헌이다. 직접 딥페이크 탐지 문헌은 P04/P05가 담당하고, P01은 생성물 보안 평가의 모델 원리를 제공한다.
