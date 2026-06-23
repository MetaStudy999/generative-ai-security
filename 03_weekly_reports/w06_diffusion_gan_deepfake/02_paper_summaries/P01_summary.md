# P01 Summary

## Diffusion Models: A Comprehensive Survey of Methods and Applications — Ling Yang et al., ACM Computing Surveys, 2024

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W06 확률생성모형(Diffusion/GAN) & 딥페이크 검출 |
| 논문명 | Diffusion Models: A Comprehensive Survey of Methods and Applications |
| 저자 | Ling Yang, Zhilong Zhang, Yang Song, Shenda Hong, Runsheng Xu, Yue Zhao, Wentao Zhang, Bin Cui, Ming-Hsuan Yang |
| 공식 출판 정보 | ACM Computing Surveys, Vol. 56, No. 4, Article 105, online 2023-11-09, print issue 2024-04-30 |
| DOI | https://doi.org/10.1145/3626235 |
| 보조 URL | https://arxiv.org/abs/2209.00796 |
| 로컬 PDF | `01_papers/pdf/01_Yang_et_al_2023_Diffusion_Models_Comprehensive_Survey.pdf` |
| 검증 상태 | W06 `paper_list.md` 기준 DOI/URL 확인. 최종 참고문헌은 공식 DOI 메타데이터 기준 사용 |
| 강의계획서 연결 | W06 학습목표 중 diffusion 수학적 정식화와 샘플링 알고리즘 비교, 딥페이크 검출 신뢰성 평가의 AI 원리 배경 |
| 핵심 근거 사용 가능 여부 | 가능. W06의 확률생성모형 원리 핵심 문헌으로 사용 |

---

## 1. 한 문장 요약

이 논문은 diffusion model을 **forward noising, reverse denoising, score-based modeling, stochastic differential equation, sampler, conditioning, latent diffusion, 응용 분야** 관점에서 체계화하며, W06에서 합성 이미지·비디오·딥페이크·watermark·provenance 평가를 이해하기 위한 확률생성모형의 핵심 이론 기반을 제공한다.

---

## 2. 핵심 연구문제

> Diffusion model은 데이터를 점진적으로 noise화한 뒤 reverse denoising으로 복원하는 확률 과정을 어떻게 학습하며, 이 생성 원리가 합성미디어 보안·딥페이크 검출·provenance 평가에 어떤 위험과 평가 기준을 만드는가?

| 번호 | 연구질문 |
|---|---|
| RQ1 | Diffusion model은 forward process와 reverse process를 통해 데이터 분포를 어떻게 근사하는가? |
| RQ2 | DDPM, score-based generative model, SDE 기반 diffusion, latent diffusion은 어떤 공통 원리와 차이를 갖는가? |
| RQ3 | Noise schedule, denoising objective, sampler step 수, guidance scale은 생성 품질·속도·신뢰성에 어떤 영향을 주는가? |
| RQ4 | Text/class/image conditioning은 생성물 통제성을 높이는 동시에 어떤 misuse와 provenance 문제를 만드는가? |
| RQ5 | Diffusion 기반 합성물이 딥페이크, 저작권, 개인정보, 워터마킹, 멀티모달 RAG 근거 오염 문제와 어떻게 연결되는가? |

---

## 3. 논문의 핵심 기여

| 기여 | 설명 | W06 연결 |
|---|---|---|
| Diffusion family taxonomy | DDPM, score-based model, SDE, latent diffusion, guided generation을 포괄적으로 정리 | 확률생성모형의 공통 언어 제공 |
| Forward/reverse process 설명 | 데이터에 noise를 추가하고 다시 복원하는 생성 원리를 체계화 | W06 AI 원리 70% 핵심 |
| Sampling 방법 정리 | DDPM/DDIM 계열, sampling step, 속도·품질 trade-off 논의 | 생성 품질과 운영 비용 평가 |
| Conditioning과 guidance 분석 | class/text/image condition이 생성 방향을 제어하는 방식 설명 | 딥페이크·합성 이미지 prompt 통제와 misuse 연결 |
| 응용 및 한계 정리 | image, video, audio, text, medical, scientific application 정리 | 보안 적용·고위험 도메인 한계 연결 |

---

## 4. 핵심 이론 및 수식

> 작성 원칙: 아래 수식은 diffusion model을 W06 보고서에서 설명하기 위한 표준 정의식이다. GitHub, MS Word, PDF 변환 호환성을 위해 수식은 Markdown 표 밖의 LaTeX block math로 작성한다.

### 4.1 Forward Diffusion Process

Forward process는 원본 데이터 $x_0$에 작은 Gaussian noise를 단계적으로 추가해 $x_T$가 거의 순수 noise가 되도록 만든다.

$$
q(x_t\mid x_{t-1})=\mathcal{N}\left(x_t;\sqrt{1-\beta_t}x_{t-1},\beta_t I\right)
$$

| 기호 | 의미 |
|---|---|
| $x_0$ | 원본 데이터 |
| $x_t$ | $t$번째 noise 단계 데이터 |
| $\beta_t$ | noise schedule |
| $I$ | 단위 공분산 행렬 |

### 보안적 의미

Forward process는 학습 데이터 분포를 점진적 noise 변환으로 다룬다. 학습 데이터에 얼굴, 저작권 이미지, 의료 이미지, 개인정보가 포함되면 reverse generation에서 민감한 패턴이 재현될 가능성을 평가해야 한다.

---

### 4.2 Closed-form Noising

여러 단계의 noising은 다음처럼 원본 데이터에서 직접 샘플링하는 형태로 표현할 수 있다.

$$
q(x_t\mid x_0)=\mathcal{N}\left(x_t;\sqrt{\bar{\alpha}_t}x_0,(1-\bar{\alpha}_t)I\right)
$$

$$
\alpha_t=1-\beta_t, \qquad \bar{\alpha}_t=\prod_{s=1}^{t}\alpha_s
$$

| 기호 | 의미 |
|---|---|
| $\alpha_t$ | noise를 제외하고 남는 signal 비율 |
| $\bar{\alpha}_t$ | $t$단계까지 누적 signal 비율 |

### 보안적 의미

Noise schedule은 생성물 품질과 학습 안정성에 영향을 준다. 생성물 검출 연구에서는 모델·sampler·noise schedule 차이가 검출기의 cross-model generalization에 영향을 줄 수 있다.

---

### 4.3 Reverse Denoising Process

Reverse process는 noise에서 데이터 방향으로 복원하는 조건부 분포를 학습한다.

$$
p_\theta(x_{t-1}\mid x_t)=\mathcal{N}\left(x_{t-1};\mu_\theta(x_t,t),\Sigma_\theta(x_t,t)\right)
$$

| 기호 | 의미 |
|---|---|
| $p_\theta$ | 학습된 reverse denoising model |
| $\mu_\theta$ | 예측된 평균 |
| $\Sigma_\theta$ | 예측 또는 고정된 공분산 |

### 보안적 의미

Reverse denoising이 정교할수록 고품질 합성물이 생성된다. 이는 창작·시뮬레이션에는 장점이지만, 딥페이크·허위 증거·신원 사칭에는 위험 요인이 된다.

---

### 4.4 Denoising Objective

DDPM 계열 학습에서는 모델이 주어진 noisy sample에서 추가된 noise를 예측하도록 학습한다.

$$
\mathcal{L}_{simple}=\mathbb{E}_{t,x_0,\epsilon}\left[\left\|\epsilon-\epsilon_\theta(x_t,t)\right\|_2^2\right]
$$

| 기호 | 의미 |
|---|---|
| $\epsilon$ | 실제 주입된 Gaussian noise |
| $\epsilon_\theta$ | 모델이 예측한 noise |
| $\mathcal{L}_{simple}$ | noise prediction 손실 |

### 보안적 의미

Denoising loss가 낮아질수록 생성 품질이 좋아질 수 있지만, 보안 평가는 품질만 보면 안 된다. 학습 데이터 memorization, 생성물 provenance, watermark robustness, detector generalization을 함께 확인해야 한다.

---

### 4.5 Score-based Modeling

Score-based generative modeling은 데이터 분포의 log-density gradient를 추정하는 관점으로 diffusion을 설명한다.

$$
s_\theta(x_t,t)\approx \nabla_{x_t}\log p_t(x_t)
$$

| 기호 | 의미 |
|---|---|
| $s_\theta$ | score network |
| $p_t(x_t)$ | $t$시점 noisy data distribution |

### 보안적 의미

Score는 데이터 분포 방향으로 샘플을 이동시키는 역할을 한다. 이 관점은 생성물이 실제 데이터 분포의 어떤 특징을 따라가는지, 민감 패턴이나 특정 인물 특징이 얼마나 재현될 수 있는지 평가할 때 중요하다.

---

### 4.6 Conditional Generation과 Classifier-free Guidance

Text-to-image, image-to-image, class-conditional generation은 condition $c$를 통해 생성 방향을 제어한다.

$$
\epsilon_\theta(x_t,t,c)
$$

Classifier-free guidance는 조건부 예측과 무조건 예측의 차이를 이용해 조건 정합성을 강화한다.

$$
\hat{\epsilon}_\theta = \epsilon_\theta(x_t,t,\varnothing)+s\left(\epsilon_\theta(x_t,t,c)-\epsilon_\theta(x_t,t,\varnothing)\right)
$$

| 기호 | 의미 |
|---|---|
| $c$ | text, class, image 등 condition |
| $\varnothing$ | condition이 없는 상태 |
| $s$ | guidance scale |

### 보안적 의미

Guidance scale이 높으면 prompt alignment가 강해질 수 있지만 artifact, 편향, 안전성 위반, 특정 인물·스타일 모방 위험도 커질 수 있다. 따라서 prompt, seed, guidance scale, model version을 생성 로그에 남겨야 한다.

---

## 5. AI 원리 70% 관점 분석

| 원리 항목 | 설명 | W06/P01에서의 의미 |
|---|---|---|
| 확률생성모형 | 데이터 분포에서 새로운 샘플을 생성하는 모델 | 합성미디어 생성 원리 |
| Forward process | 데이터를 점진적으로 noise화 | 학습 과정의 수학적 정식화 |
| Reverse process | noise에서 데이터로 복원 | 생성 과정의 핵심 |
| Denoising objective | noise 예측 손실로 학습 | 학습 안정성과 품질 결정 |
| Score modeling | log-density gradient 추정 | SDE/score-based diffusion 연결 |
| Sampling | reverse trajectory를 따라 샘플 생성 | 품질·속도·비용 trade-off |
| Conditioning | text/class/image condition으로 생성 제어 | 딥페이크·저작권·prompt misuse 연결 |
| Latent diffusion | latent space에서 diffusion 수행 | 대규모 생성모델 비용 절감 |

---

## 6. 보안 이슈 30% 관점 분석

| 보안 항목 | Diffusion 관점 해석 | 대표 평가 지표 |
|---|---|---|
| 기밀성 | 학습 데이터 memorization, 민감 이미지 재생성, 개인정보 패턴 복원 위험 | leakage risk, nearest-neighbor similarity |
| 무결성 | 합성 이미지가 증거·인증·여론·문서 신뢰성을 훼손할 수 있음 | detection AUC, forensic consistency |
| 가용성 | 대량 합성물과 고품질 deepfake가 검출·검토 시스템 부담을 증가시킴 | review cost, latency, detector throughput |
| 프라이버시 | 특정 얼굴·의료·위치 정보가 생성물에 암시될 수 있음 | re-identification risk, memorization score |
| 저작권/IP | 학습 데이터 스타일·저작물 모방과 생성물 권리 문제가 발생 | provenance coverage, content similarity |
| 책임성 | 생성 모델, prompt, seed, sampler, watermark, output hash 기록 필요 | audit completeness, watermark robustness |

---

## 7. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | 학습 데이터, 얼굴·신원, 저작물, prompt, seed, model checkpoint, sampler config, watermark key, provenance log |
| 공격자 목표 | 합성 이미지 생성, 신원 사칭, 허위 시각 증거 생성, 검출 회피, watermark 제거, 출처 위조 |
| 공격자 능력 | text prompt 조작, image editing, fine-tuning, LoRA/adaptation, sampler 변경, post-processing, compression |
| 공격 경로 | training data → diffusion pretraining/fine-tuning → conditioned generation → post-processing → synthetic media distribution |
| 방어자 능력 | watermark, provenance metadata, detector, hash logging, human review, prompt/output audit, dataset governance |
| 제외 범위 | 실제 인물 사칭물 제작, 유해 딥페이크 생성, 무단 개인정보 사용, 저작권 침해 목적 생성 |

---

## 8. 평가방법 및 지표

| 평가축 | 지표 | 의미 | W06/P01 활용 |
|---|---|---|---|
| 생성 품질 | FID, KID | 생성 이미지 분포가 실제 데이터와 유사한지 | 생성 성능 배경 |
| 조건 정합성 | CLIP Score, text-image alignment | prompt와 생성물의 의미 일치 | conditional generation 평가 |
| 다양성 | diversity score, mode coverage | 동일 prompt/seed 변화에서 다양성 | mode collapse/편향 확인 |
| 검출 가능성 | Detection AUC, F1, FPR/FNR | 합성물 검출 성능 | P04/P05 deepfake detector와 연결 |
| 일반화 | cross-generator AUC | 다른 모델·sampler 생성물에도 검출되는지 | detector overfitting 방지 |
| 워터마크 | watermark detection rate, FPR/FNR | 생성물 provenance 확인 | W13 watermark와 연결 |
| 프라이버시 | memorization score, nearest-neighbor similarity | 학습 데이터 재현 위험 | W11 privacy와 연결 |
| 운영 비용 | sampling latency, GPU cost, step count | 실제 서비스 가능성 | W14 MLOps와 연결 |
| 감사 가능성 | prompt/seed/model/output hash completeness | 사후 검증 가능성 | W15 evidence chain |

---

## 9. 재현성 체크리스트

| 항목 | 기록해야 할 내용 |
|---|---|
| 모델 | diffusion variant, checkpoint, model card, license |
| 데이터 | 학습/평가 데이터셋 출처, 공개 여부, 개인정보 포함 여부 |
| Sampler | DDPM/DDIM/solver 종류, sampling step 수, scheduler |
| Conditioning | prompt, negative prompt, class label, image condition, guidance scale |
| Randomness | seed, batch size, random generator 정보 |
| 출력 | 생성 이미지 hash, metadata, output path, 실패 사례 |
| 보안 평가 | detector version, watermark detector, nearest-neighbor 검색 설정 |
| 로그 | prompt-output-model-sampler-watermark-provenance log |
| 한계 | toy generation 또는 문헌 기반 분석을 실제 딥페이크 탐지 보증으로 일반화하지 않음 |

---

## 10. 논문의 고유 기여

1. Diffusion model 계열을 DDPM, score-based model, SDE, latent diffusion, conditional generation까지 폭넓게 정리한다.
2. Forward noising과 reverse denoising을 공통 수학적 틀로 이해하게 한다.
3. Sampling, guidance, application taxonomy를 통해 생성 품질과 비용의 trade-off를 설명한다.
4. W06의 딥페이크·합성미디어 검출 문헌(P04/P05)을 이해하기 위한 생성모형 원리 기반을 제공한다.
5. W08 멀티모달 RAG, W13 watermarking, W14 MLOps provenance, W15 evidence chain으로 연결 가능한 보안 평가축을 제공한다.

---

## 11. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 직접 보안 문헌은 아님 | P01은 생성모형 survey이며 deepfake detection 자체가 주제는 아니다. | P04/P05와 결합해 보안 평가로 확장 |
| 빠른 기술 변화 | diffusion sampler, latent diffusion, text-to-video 모델이 빠르게 바뀐다. | 모델명·버전·평가일 명시 |
| 생성 품질과 안전성 분리 필요 | FID/CLIP이 좋아도 안전하다는 뜻은 아니다. | detector AUC, watermark, provenance, leakage를 별도 평가 |
| 데이터 provenance 한계 | 학습 데이터 출처가 불명확하면 memorization·저작권 위험을 평가하기 어렵다. | dataset governance와 output similarity audit 반영 |
| 실제 딥페이크 실험 제한 | 실제 인물 사칭물 생성은 윤리·법적 위험이 있다. | synthetic/toy data와 문헌 기반 분석으로 제한 |

---

## 12. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | 생성형 AI 보안은 고품질 생성 자체보다 생성물 신뢰성·출처·검출 가능성이 문제라는 문제의식 |
| 2장 관련연구 | diffusion model 원리, DDPM/score/SDE/latent diffusion taxonomy |
| 3장 위협모형 | 합성 이미지, prompt, checkpoint, sampler, watermark, provenance log 보호 자산 정의 |
| 4장 연구방법 | FID/KID, CLIP, detection AUC, watermark robustness, memorization risk, audit completeness 지표 설계 |
| 5장 분석 | toy/synthetic generation 또는 문헌 기반 생성-검출 평가표 제시 |
| 6장 보안적 함의 | 딥페이크, 저작권, 프라이버시, 책임성, human review 필요성 해석 |
| 7장 결론 | diffusion 기반 생성물 보안 평가는 생성 품질·검출·provenance·프라이버시를 함께 봐야 함을 요약 |

---

## 13. 기말논문 연결 3문장

1. W06에서 기말논문에 반영할 개념: diffusion model은 고품질 합성물을 생성하는 핵심 확률생성모형이므로, 생성 품질만이 아니라 provenance, watermark, detector generalization, privacy leakage를 함께 평가해야 한다.
2. W06에서 기말논문에 반영할 표·그림·실험: forward/reverse diffusion 수식, denoising objective, classifier-free guidance, 생성-검출-provenance pipeline, detection AUC·watermark·memorization 평가표를 반영한다.
3. W06이 RAG/LLM 보안 감사 프레임워크와 연결되는 지점: 이미지·비디오 생성물은 W08 멀티모달 RAG의 근거 자료로 들어갈 수 있으므로, 생성물 출처와 prompt-output 로그를 W14/W15의 evidence chain으로 관리해야 한다.

---

## 14. 최종 판단

P01은 W06의 확률생성모형 원리 핵심 문헌이다. 직접적인 딥페이크 검출과 reliability 평가는 P04/P05가 담당하지만, P01 없이는 deepfake 생성 원리, prompt-conditioned generation, watermark/provenance 평가의 기술적 배경을 설명하기 어렵다.

---

## 15. 변환 호환성 메모

```bash
pandoc P01_summary.md -o P01_summary.docx
pandoc P01_summary.md -o P01_summary.pdf --pdf-engine=xelatex
```
