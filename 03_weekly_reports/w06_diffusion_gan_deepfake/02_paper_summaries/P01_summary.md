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
| 검증 상태 | W06 `paper_list.md` 기준 DOI/URL 확인. 로컬 PDF 첫 페이지에서 ACM Computing Surveys Vol. 56, No. 4, Article 105와 DOI `10.1145/3626235` 확인 메모가 유지되어 있음 |
| PDF 확인 메모 | repo의 PDF 폴더에 P01 관련 PDF blob이 존재함을 확인했다. 요약은 로컬 PDF 경로와 W06 `paper_list.md`의 공식 DOI/arXiv 메타데이터 기준으로 보완했다. |
| 수식 호환성 | GitHub 수식 렌더링 오류 방지를 위해 `\operatorname`을 사용하지 않고, 긴 영문 subscript 대신 짧은 변수명과 표 설명을 사용했다. |
| 핵심 근거 사용 가능 여부 | 가능. W06의 diffusion 확률생성모형 원리, 합성미디어 provenance, watermark, 딥페이크 검출 신뢰성 평가의 핵심 이론 문헌으로 사용 |

---

## 1. 한 문장 요약

이 논문은 diffusion model을 **forward noising, reverse denoising, denoising score matching, stochastic differential equation, sampler, noise schedule, conditional generation, classifier-free guidance, latent diffusion, image/video/audio/text 응용** 관점에서 체계화하며, W06에서는 합성 이미지·비디오·딥페이크·워터마킹·provenance·검출기 일반화 문제를 이해하기 위한 확률생성모형의 핵심 이론 기반을 제공한다.

---

## 2. 핵심 연구문제

> Diffusion model은 데이터를 점진적으로 noise화한 뒤 reverse denoising으로 복원하는 확률 과정을 학습한다. 이 생성 원리는 고품질 합성미디어를 가능하게 하지만, 동시에 딥페이크·저작권·개인정보·워터마크 제거·합성물 검출 회피·provenance 불명확성 문제를 만든다.

| 번호 | 연구질문 |
|---|---|
| RQ1 | Diffusion model은 forward process와 reverse process를 통해 데이터 분포를 어떻게 근사하는가? |
| RQ2 | DDPM, score-based generative model, SDE 기반 diffusion, latent diffusion은 어떤 공통 원리와 차이를 갖는가? |
| RQ3 | Noise schedule, denoising objective, sampler step 수, guidance scale은 생성 품질·속도·신뢰성에 어떤 영향을 주는가? |
| RQ4 | Text/class/image conditioning은 생성물 통제성을 높이는 동시에 어떤 misuse와 provenance 문제를 만드는가? |
| RQ5 | Diffusion 기반 합성물이 딥페이크, 저작권, 개인정보, watermark, RAG 근거 오염, 디지털 증거 신뢰성 문제와 어떻게 연결되는가? |

---

## 3. 논문의 핵심 기여

| 기여 | 설명 | W06 연결 |
|---|---|---|
| Diffusion family taxonomy | DDPM, score-based model, SDE, guided diffusion, latent diffusion을 포괄적으로 정리 | 확률생성모형의 공통 언어 제공 |
| Forward/reverse process 설명 | 데이터에 noise를 추가하고 다시 복원하는 생성 원리를 체계화 | W06 AI 원리 70% 핵심 |
| Sampling 방법 정리 | DDPM/DDIM 계열, sampler step, 속도·품질 trade-off 논의 | 생성 품질과 운영 비용 평가 |
| Conditioning과 guidance 분석 | class/text/image condition이 생성 방향을 제어하는 방식 설명 | 딥페이크·합성 이미지 prompt 통제와 misuse 연결 |
| 응용 및 한계 정리 | image, video, audio, text, medical, scientific application 정리 | 보안 적용·고위험 도메인 한계 연결 |
| 보안 확장 가능성 | 논문 자체는 보안 전문 survey는 아니지만 synthetic media risk, provenance, watermark, detection 문제와 직접 연결 가능 | W06 딥페이크 검출 문헌의 이론 기반 |

---

## 4. 목차별 핵심 개괄

| 목차 | 핵심 내용 | 비전공자용 이해 |
|---|---|---|
| 1. Introduction | Diffusion model의 등장 배경과 GAN/VAE 대비 장점, 응용 확장을 설명한다. | 이미지를 조금씩 노이즈로 만들었다가 다시 복원하는 방식의 생성 AI다. |
| 2. Background | 확률모형, Markov chain, variational inference, score matching, SDE 배경을 정리한다. | 수학적으로 “노이즈에서 데이터로 돌아가는 길”을 배운다. |
| 3. DDPM 계열 | forward diffusion과 reverse denoising, noise prediction objective를 설명한다. | 원본에 넣은 노이즈를 맞히도록 학습한다. |
| 4. Score-based/SDE 계열 | score function과 연속시간 확률미분방정식 기반 해석을 다룬다. | 데이터가 있을 법한 방향으로 샘플을 이동시킨다. |
| 5. Sampling and Acceleration | DDIM, fast sampling, step 수 감소, 품질·속도 trade-off를 설명한다. | 더 적은 단계로 빠르게 이미지를 만드는 방법이다. |
| 6. Conditional Generation | class, text, image, layout 등 condition을 이용한 생성 제어를 정리한다. | “무엇을 만들지”를 prompt나 조건으로 제어한다. |
| 7. Latent Diffusion | pixel space 대신 latent space에서 diffusion을 수행해 비용을 낮춘다. | 압축된 공간에서 생성해 더 효율적으로 만든다. |
| 8. Applications | 이미지, 비디오, 오디오, 텍스트, 의료, 과학, 3D 등 응용을 정리한다. | 여러 형태의 데이터를 생성하거나 복원할 수 있다. |
| 9. Challenges | sampling 비용, controllability, safety, bias, privacy, provenance, evaluation 문제가 남는다. | 생성 품질뿐 아니라 안전성과 출처 확인이 중요하다. |

---

## 5. 핵심 이론 및 수식

> 아래 수식은 diffusion model을 W06 보고서에서 설명하기 위한 표준 정의식이다. GitHub 호환성을 위해 `\operatorname`은 사용하지 않고, 수식은 Markdown 표 밖의 LaTeX block math로 작성한다.

### 5.1 Forward Diffusion Process

Forward process는 원본 데이터 $x_0$에 작은 Gaussian noise를 단계적으로 추가해 $x_T$가 거의 순수 noise가 되도록 만든다.

$$
q(x_t \mid x_{t-1})=\mathcal{N}\left(x_t;\sqrt{1-\beta_t}x_{t-1},\beta_t I\right)
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

### 5.2 Closed-form Noising

여러 단계의 noising은 다음처럼 원본 데이터에서 직접 샘플링하는 형태로 표현할 수 있다.

$$
q(x_t \mid x_0)=\mathcal{N}\left(x_t;\sqrt{\bar{\alpha}_t}x_0,(1-\bar{\alpha}_t)I\right)
$$

$$
\alpha_t=1-\beta_t
$$

$$
\bar{\alpha}_t=\prod_{s=1}^{t}\alpha_s
$$

| 기호 | 의미 |
|---|---|
| $\alpha_t$ | noise를 제외하고 남는 signal 비율 |
| $\bar{\alpha}_t$ | $t$단계까지 누적 signal 비율 |

### 보안적 의미

Noise schedule은 생성물 품질과 학습 안정성에 영향을 준다. 생성물 검출 연구에서는 모델·sampler·noise schedule 차이가 detector의 cross-model generalization에 영향을 줄 수 있다.

---

### 5.3 Reverse Denoising Process

Reverse process는 noise에서 데이터 방향으로 복원하는 조건부 분포를 학습한다.

$$
p_{\theta}(x_{t-1}\mid x_t)=\mathcal{N}\left(x_{t-1};\mu_{\theta}(x_t,t),\Sigma_{\theta}(x_t,t)\right)
$$

| 기호 | 의미 |
|---|---|
| $p_{\theta}$ | 학습된 reverse denoising model |
| $\mu_{\theta}$ | 예측된 평균 |
| $\Sigma_{\theta}$ | 예측 또는 고정된 공분산 |

### 보안적 의미

Reverse denoising이 정교할수록 고품질 합성물이 생성된다. 이는 창작·시뮬레이션에는 장점이지만, 딥페이크·허위 증거·신원 사칭에는 위험 요인이 된다.

---

### 5.4 Denoising Objective

DDPM 계열 학습에서는 모델이 noisy sample에서 추가된 noise를 예측하도록 학습한다.

$$
\mathcal{L}_{denoise}=\mathbb{E}_{t,x_0,\epsilon}\left[\left\|\epsilon-\epsilon_{\theta}(x_t,t)\right\|_2^2\right]
$$

| 기호 | 의미 |
|---|---|
| $\epsilon$ | 실제 주입된 Gaussian noise |
| $\epsilon_{\theta}$ | 모델이 예측한 noise |
| $\mathcal{L}_{denoise}$ | noise prediction 손실 |

### 보안적 의미

Denoising loss가 낮아질수록 생성 품질이 좋아질 수 있지만, 보안 평가는 품질만 보면 안 된다. 학습 데이터 memorization, 생성물 provenance, watermark robustness, detector generalization을 함께 확인해야 한다.

---

### 5.5 Score-based Modeling

Score-based generative modeling은 데이터 분포의 log-density gradient를 추정하는 관점으로 diffusion을 설명한다.

$$
s_{\theta}(x_t,t)\approx \nabla_{x_t}\log p_t(x_t)
$$

| 기호 | 의미 |
|---|---|
| $s_{\theta}$ | score network |
| $p_t(x_t)$ | $t$시점 noisy data distribution |

### 보안적 의미

Score는 데이터 분포 방향으로 샘플을 이동시키는 역할을 한다. 이 관점은 생성물이 실제 데이터 분포의 어떤 특징을 따라가는지, 민감 패턴이나 특정 인물 특징이 얼마나 재현될 수 있는지 평가할 때 중요하다.

---

### 5.6 Conditional Generation과 Classifier-free Guidance

Text-to-image, image-to-image, class-conditional generation은 condition $c$를 통해 생성 방향을 제어한다.

$$
\epsilon_{\theta}(x_t,t,c)
$$

Classifier-free guidance는 조건부 예측과 무조건 예측의 차이를 이용해 조건 정합성을 강화한다.

$$
\hat{\epsilon}_{\theta}=\epsilon_{\theta}(x_t,t,0)+s\left(\epsilon_{\theta}(x_t,t,c)-\epsilon_{\theta}(x_t,t,0)\right)
$$

| 기호 | 의미 |
|---|---|
| $c$ | text, class, image 등 condition |
| $0$ | condition이 없는 상태를 나타내는 기호 |
| $s$ | guidance scale |

### 보안적 의미

Guidance scale이 높으면 prompt alignment가 강해질 수 있지만 artifact, 편향, 안전성 위반, 특정 인물·스타일 모방 위험도 커질 수 있다. 따라서 prompt, seed, guidance scale, model version을 생성 로그에 남겨야 한다.

---

### 5.7 Provenance Detection Rate

생성물의 출처 또는 watermark를 검출한 비율을 측정한다.

$$
ProvDetectRate=\frac{N_{pd}}{N_{gen}}
$$

| 기호 | 의미 |
|---|---|
| $N_{gen}$ | 평가 대상 생성물 수 |
| $N_{pd}$ | provenance 또는 watermark가 정상 검출된 생성물 수 |

### 보안적 의미

생성물의 출처가 확인되지 않으면 딥페이크, 허위 증거, 저작권 침해, RAG 근거 오염을 판별하기 어렵다.

---

### 5.8 Diffusion Security Risk

Diffusion 기반 합성미디어의 보안 위험을 요약한다.

$$
DiffusionRisk=MisuseRisk+PrivacyRisk+ProvenanceGap+DetectionEvasion-WatermarkCoverage
$$

### 보안적 의미

Diffusion model의 위험은 품질이 높아질수록 커질 수 있다. 따라서 생성 품질 평가와 별도로 misuse, privacy, provenance, watermark, detector robustness를 분리해야 한다.

---

## 6. AI 원리 70% 관점 분석

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

## 7. 보안 이슈 30% 관점 분석

| 보안 항목 | Diffusion 관점 해석 | 대표 평가 지표 |
|---|---|---|
| 기밀성 | 학습 데이터 memorization, 민감 이미지 재생성, 개인정보 패턴 복원 위험 | nearest-neighbor similarity, leakage test |
| 무결성 | 합성 이미지가 증거·인증·여론·문서 신뢰성을 왜곡 | deepfake detection rate, provenance check |
| 가용성 | 고품질 합성물 대량 생성이 탐지·검토 부담 증가 | review cost, detector throughput |
| 프라이버시 | 얼굴, 의료 이미지, 위치, 문서 이미지가 생성·복원될 수 있음 | privacy leakage, identity similarity |
| 저작권 | 특정 작가 스타일·저작물 특징 모방 가능 | style similarity, provenance evidence |
| 책임성 | 생성 prompt, seed, model version, sampler, watermark 정보를 기록해야 함 | audit completeness, generation log |

---

## 8. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | 학습 데이터, 얼굴·음성·의료·문서 이미지, 생성 prompt, model checkpoint, seed, sampler 설정, watermark, provenance log |
| 공격자 목표 | 딥페이크 생성, 허위 증거 생성, 저작권·스타일 모방, 개인정보 재현, detector 우회, watermark 제거 |
| 공격자 능력 | prompt 조작, condition 입력, seed 반복, sampler 변경, image-to-image 변환, post-processing |
| 공격 경로 | prompt/condition → diffusion sampling → synthetic media → distribution/log/provenance decision |
| 방어자 능력 | watermark, content provenance, detector, generation log, human review, dataset governance, safe release policy |
| 제외 범위 | 실제 인물 사칭 합성물 제작, 개인정보 이미지 사용, 불법·유해 이미지 생성, 탐지 우회 절차 제공 |

---

## 9. 평가방법 및 지표

| 지표 | 의미 | W06/P01 활용 |
|---|---|---|
| FID | 생성 이미지 분포와 실제 이미지 분포의 거리 | 생성 품질 평가 |
| IS | 생성 이미지의 class confidence와 다양성 | 품질 보조 지표 |
| CLIPScore | prompt와 이미지의 의미 정합성 | text-to-image alignment |
| Sampling Cost | step 수, latency, GPU memory | 운영 비용 평가 |
| ProvDetectRate | watermark/provenance 검출률 | 출처 확인 평가 |
| Detector Recall | 합성물 검출 성공률 | deepfake detector 평가 |
| FPR | 실제 이미지를 합성으로 오탐한 비율 | 탐지기 신뢰성 |
| Privacy Leakage | 민감 데이터 재현 가능성 | 프라이버시 평가 |
| AuditCompleteness | prompt, seed, model, sampler, output log 보존 정도 | W14/W15 evidence chain |

---

## 10. 재현성 체크리스트

| 항목 | 기록해야 할 내용 |
|---|---|
| Bibliographic status | DOI, ACM CSUR 출판정보, arXiv 판본, 로컬 PDF 상태 |
| Model | diffusion model 이름, checkpoint, license, version |
| Sampling config | sampler, step 수, seed, guidance scale, resolution, scheduler |
| Prompt/condition | text prompt, negative prompt, class/image condition, preprocessing |
| Data | 공개 toy image 또는 synthetic sample만 사용, 개인정보·실제 인물 이미지 제외 |
| Output | 생성물 hash, watermark 여부, provenance metadata, post-processing 여부 |
| Evaluation | FID/CLIPScore 등 품질 지표와 ProvDetectRate, Detector Recall, FPR, Privacy Leakage 분리 |
| Security controls | watermark, detector, content policy, human review, safe logging |
| Evidence | config file, prompt log, output hash, metric CSV/JSON, script commit |
| GitHub math | `\operatorname` 사용 금지, 긴 영문 subscript 대신 짧은 변수명과 표 설명 사용 |

---

## 11. 논문의 고유 기여

1. Diffusion model 계열을 DDPM, score-based, SDE, latent diffusion, guided generation 관점에서 포괄적으로 정리했다.
2. W06에서 GAN/deepfake 검출 논문을 이해하기 위한 확률생성모형의 이론 배경을 제공한다.
3. 생성 품질과 안전성·provenance·privacy를 분리해 평가해야 한다는 논리적 근거가 된다.
4. Text-to-image와 image-to-image conditioning이 misuse, identity similarity, style imitation, synthetic evidence 문제로 확장됨을 설명할 수 있게 한다.
5. W14/W15에서 생성 로그, watermark, output hash, model/sampler config를 evidence chain으로 남겨야 하는 근거가 된다.

---

## 12. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 보안 직접성 부족 | diffusion survey 자체는 보안·딥페이크 검출 전문 문헌이 아니다. | W06 P04/P05 deepfake detection 문헌과 결합 |
| 빠른 모델 변화 | text-to-image와 video diffusion 모델은 빠르게 변한다. | 모델 버전, 평가일, sampler config 명시 |
| 재현 비용 | 고품질 diffusion generation은 GPU와 시간이 필요하다. | toy sample과 공개 small model 기준으로 제한 |
| 프라이버시 평가 어려움 | 학습 데이터 memorization을 직접 확인하기 어렵다. | nearest-neighbor, synthetic privacy-risk test 한계 명시 |
| 탐지 일반화 한계 | 한 detector가 모든 diffusion model을 잘 잡는다고 볼 수 없다. | cross-model/cross-sampler 평가 필요성 명시 |
| 악용 위험 | 실제 딥페이크 생성 절차를 상세화하면 부적절하다. | 원리·평가·방어 중심으로 제한 |

---

## 13. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | 생성형 AI의 고품질 합성미디어가 provenance, privacy, trust 문제를 만든다는 문제의식 |
| 2장 관련연구 | diffusion model 원리와 생성모형 taxonomy 정리 |
| 3장 위협모형 | prompt, condition, seed, sampler, output, watermark, provenance log 보호 자산 정의 |
| 4장 연구방법 | forward/reverse process, denoising loss, guidance, ProvDetectRate, DiffusionRisk 지표 설계 |
| 5장 분석 | diffusion generation pipeline과 synthetic media security risk matrix 제시 |
| 6장 보안적 함의 | 딥페이크, 저작권, 개인정보, 탐지 일반화, 생성물 출처 확인 필요성 해석 |
| 부록 | prompt, seed, model version, sampler, output hash, watermark/provenance log 수록 |

---

## 14. 기말논문 연결 3문장

1. W06에서 기말논문에 반영할 개념: Diffusion model은 forward noising과 reverse denoising을 통해 고품질 합성미디어를 생성하며, 이 생성 원리는 딥페이크와 synthetic evidence risk의 기술적 기반이 된다.
2. W06에서 기말논문에 반영할 표·그림·실험: forward/reverse process, denoising objective, classifier-free guidance, ProvDetectRate, DiffusionRisk 수식표와 generation-provenance-evaluation pipeline을 반영한다.
3. W06이 W14/W15와 연결되는 지점: diffusion generation 결과는 prompt, seed, model checkpoint, sampler, watermark, output hash를 evidence chain으로 남겨야 재현성과 책임성을 확보할 수 있다.

---

## 15. 최종 판단

P01은 W06의 diffusion 이론 핵심 문헌이다. 직접적인 딥페이크 검출 논문은 아니지만, 고품질 합성 이미지와 비디오가 어떻게 생성되는지 설명하는 기반을 제공한다. 따라서 기말논문에서는 P01을 **확률생성모형 원리, diffusion generation pipeline, synthetic media risk, provenance/watermark 평가, 딥페이크 검출 일반화의 배경 문헌**으로 사용하는 것이 적절하다.

---

## 16. GitHub 수식 호환성 메모

이 파일에서는 GitHub 수식 렌더링 오류 방지를 위해 `\operatorname`을 사용하지 않는다.

| 피해야 할 표현 | 권장 표현 |
|---|---|
| `\operatorname{softmax}` | `\mathrm{softmax}` |
| `\operatorname{argmax}` | `\mathrm{argmax}` 또는 `\arg\max` |
| `N_{provenance\ detected}` | `N_{pd}`처럼 짧은 변수명 사용 후 표에서 의미 설명 |
| `N_{generated}` | `N_{gen}`처럼 짧은 변수명 사용 후 표에서 의미 설명 |
| 긴 영문 subscript | 짧은 변수명 사용 후 표에서 의미 설명 |

```bash
pandoc P01_summary.md -o P01_summary.docx
pandoc P01_summary.md -o P01_summary.pdf --pdf-engine=xelatex
```
