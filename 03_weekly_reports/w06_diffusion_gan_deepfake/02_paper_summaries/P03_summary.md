# P03 Summary

## Generative Adversarial Networks in Computer Vision: A Survey and Taxonomy — Zhengwei Wang, Qi She, Tomas E. Ward, ACM Computing Surveys, 2021/2022

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W06 확률생성모형(Diffusion/GAN) & 딥페이크 검출 |
| 논문명 | Generative Adversarial Networks in Computer Vision: A Survey and Taxonomy |
| 저자 | Zhengwei Wang, Qi She, Tomas E. Ward |
| 공식 출판 정보 | ACM Computing Surveys, Vol. 54, No. 2, Article 37, online 2021-02-09, print issue 2022-03-31 |
| DOI | https://doi.org/10.1145/3439723 |
| 보조 URL | https://arxiv.org/abs/1906.01529 |
| 로컬 PDF | `01_papers/pdf/03_Wang_She_Ward_2021_GANs_Computer_Vision_Survey.pdf` |
| 검증 상태 | W06 `paper_list.md` 기준 출판 DOI 확인. 강의계획서의 `Tianqi Wang et al.` 표기와 달라 동일성 검토 메모 유지 |
| PDF 확인 메모 | repo의 PDF 폴더에 P03 관련 PDF blob이 존재함을 확인했다. 요약은 로컬 PDF 경로와 W06 `paper_list.md`의 공식 DOI/arXiv 메타데이터 기준으로 보완했다. |
| 수식 호환성 | GitHub 수식 렌더링 오류 방지를 위해 `\operatorname`을 사용하지 않고, 긴 영문 subscript 대신 짧은 변수명과 표 설명을 사용했다. |
| 핵심 근거 사용 가능 여부 | 가능. W06에서 diffusion model과 대비되는 GAN 생성 원리, computer vision 응용, 딥페이크 생성·검출 arms race 배경 문헌으로 사용 |

---

## 1. 한 문장 요약

이 논문은 GAN을 **generator-discriminator minimax game, adversarial training, objective variants, architecture variants, image synthesis, image-to-image translation, super-resolution, domain adaptation, style transfer, evaluation metrics, training instability, mode collapse, open challenges** 관점에서 분류한 computer vision 중심 survey이며, W06에서 딥페이크 생성 원리와 생성-검출 arms race를 설명하는 핵심 배경 문헌이다.

---

## 2. 핵심 연구문제

> GAN은 생성기와 판별기의 경쟁 학습을 통해 시각 데이터 분포를 근사한다. 이 구조는 고품질 이미지 생성과 변환을 가능하게 하지만, 동시에 얼굴 합성, 속성 조작, 시각 증거 조작, detector 회피, 저작권·프라이버시 문제를 만든다.

| 번호 | 연구질문 |
|---|---|
| RQ1 | GAN은 generator와 discriminator의 minimax game을 통해 실제 데이터 분포를 어떻게 근사하는가? |
| RQ2 | DCGAN, cGAN, WGAN, CycleGAN, StyleGAN 계열 등 주요 GAN 변형은 어떤 문제를 해결하기 위해 제안되었는가? |
| RQ3 | Image synthesis, image-to-image translation, super-resolution, style transfer, domain adaptation은 딥페이크·시각 증거 조작과 어떻게 연결되는가? |
| RQ4 | GAN 평가에서 image quality, diversity, training stability, mode collapse, human perceptual quality를 어떻게 측정해야 하는가? |
| RQ5 | GAN 기반 생성물과 diffusion 기반 생성물을 비교할 때 보안 평가 지표와 detector generalization은 어떻게 달라지는가? |

---

## 3. 논문의 핵심 기여

| 기여 | 설명 | W06 연결 |
|---|---|---|
| GAN taxonomy | loss/objective, architecture, training strategy, CV application별로 GAN 연구를 체계화 | GAN 생성모형의 공통 언어 제공 |
| Adversarial training 원리 정리 | generator와 discriminator의 경쟁 학습 구조 설명 | deepfake detector와 개념적으로 연결 |
| Computer vision 응용 분류 | image generation, translation, restoration, super-resolution, editing 등 응용 정리 | 이미지 조작·합성미디어 위협모형 연결 |
| 평가 지표와 한계 논의 | 생성 품질, 다양성, mode collapse, training instability 문제 제시 | 생성물 검출과 arms race 평가 |
| 향후 과제 정리 | 안정적 학습, 평가 신뢰성, 고품질 생성, 응용 확장 문제 제시 | W06 보안 평가와 W15 한계 서술 연결 |
| Diffusion 대비 근거 | diffusion 이전 세대의 핵심 생성모형으로 GAN artifact, detector, deepfake 생성 논의의 배경 제공 | W06 P01/P02와 비교 가능 |

---

## 4. 목차별 핵심 개괄

| 목차 | 핵심 내용 | 비전공자용 이해 |
|---|---|---|
| 1. Introduction | GAN의 등장 배경, computer vision에서의 영향, survey taxonomy를 제시한다. | 생성기와 판별기가 경쟁하며 이미지를 만든다. |
| 2. GAN Fundamentals | minimax objective, generator, discriminator, adversarial training 원리를 설명한다. | 위조범과 감별사가 서로 실력을 높이는 구조다. |
| 3. Objective Variants | vanilla GAN, cGAN, WGAN, LSGAN 등 loss 변형을 정리한다. | 학습을 더 안정적으로 만들기 위한 목적함수 변화다. |
| 4. Architecture Variants | DCGAN, progressive GAN, StyleGAN류 구조와 convolution/normalization 설계를 다룬다. | 더 선명하고 자연스러운 이미지를 만들기 위한 구조다. |
| 5. Applications | image synthesis, image translation, super-resolution, inpainting, restoration, domain adaptation을 정리한다. | 이미지를 새로 만들거나 다른 형태로 바꿀 수 있다. |
| 6. Evaluation | 생성 품질, 다양성, 안정성, mode collapse, FID/IS류 지표와 한계를 논의한다. | 이미지가 좋아 보이는지와 다양한지 평가한다. |
| 7. Challenges | 학습 불안정, mode collapse, 평가 신뢰성, 고해상도 생성, 데이터 편향 문제가 남는다. | 잘 만들기는 어렵고 평가도 쉽지 않다. |
| 보안 연결 | GAN 생성물은 딥페이크, 시각 증거 조작, detector arms race, 개인정보 재현 문제와 연결된다. | 합성 이미지가 현실 증거처럼 쓰일 수 있다. |

---

## 5. 핵심 이론 및 수식

> 아래 수식은 GAN 원리와 W06 보안 평가를 설명하기 위한 표준화된 표현이다. GitHub 호환성을 위해 `\operatorname`은 사용하지 않고, 수식은 Markdown 표 밖의 LaTeX block math로 작성한다.

### 5.1 GAN Minimax Objective

GAN은 생성기 $G$와 판별기 $D$가 경쟁하는 minimax 문제로 정식화된다.

$$
\min_G \max_D V(D,G)=\mathbb{E}_{x\sim p_{data}}[\log D(x)]+\mathbb{E}_{z\sim p_z}[\log(1-D(G(z)))]
$$

| 기호 | 의미 |
|---|---|
| $G$ | generator. latent noise에서 fake sample 생성 |
| $D$ | discriminator. real/fake 구분 |
| $z$ | latent noise vector |
| $p_{data}$ | 실제 데이터 분포 |
| $p_z$ | latent prior distribution |

### 보안적 의미

GAN의 discriminator는 생성물을 구분하는 구조이므로 딥페이크 검출기와 개념적으로 유사하다. 그러나 generator가 개선될수록 detector는 더 어려운 구분 문제를 풀어야 하며, 생성-검출 arms race가 발생한다.

---

### 5.2 Conditional GAN

조건부 GAN은 class label, text, image, semantic map 등 조건 $c$를 사용해 생성 방향을 제어한다.

$$
\min_G \max_D V(D,G,c)=\mathbb{E}_{x\sim p_{data}}[\log D(x,c)]+\mathbb{E}_{z\sim p_z}[\log(1-D(G(z,c),c))]
$$

| 기호 | 의미 |
|---|---|
| $c$ | class, text, image, mask, domain 등 condition |
| $G(z,c)$ | 조건 $c$에 맞게 생성된 sample |
| $D(x,c)$ | 조건과 sample의 정합성을 판별하는 discriminator |

### 보안적 의미

조건부 생성은 특정 얼굴, 속성, 도메인, 장면을 제어하는 데 쓰일 수 있다. 이는 창작·복원에는 유용하지만 신원 사칭, 속성 조작, 허위 이미지 생성 위험을 높인다.

---

### 5.3 Wasserstein GAN 관점

GAN 학습 안정성 개선을 위해 Wasserstein distance를 사용하는 변형도 중요하다.

$$
\min_G \max_{D\in \mathcal{D}} \mathbb{E}_{x\sim p_{data}}[D(x)]-\mathbb{E}_{z\sim p_z}[D(G(z))]
$$

| 기호 | 의미 |
|---|---|
| $\mathcal{D}$ | Lipschitz 제약을 만족하는 critic 함수 집합 |
| $D$ | 일반 GAN의 discriminator와 달리 real/fake 확률이 아닌 critic score를 출력 |

### 보안적 의미

학습 안정성이 좋아지면 더 자연스러운 합성물이 생성될 수 있다. 검출 측면에서는 더 낮은 artifact와 높은 현실감이 detector generalization을 어렵게 만든다.

---

### 5.4 Mode Collapse와 다양성 평가

GAN은 생성 다양성이 낮아지는 mode collapse 문제가 발생할 수 있다.

$$
Diversity(G)=\mathbb{E}_{z_i,z_j}\left[d(G(z_i),G(z_j))\right]
$$

| 기호 | 의미 |
|---|---|
| $Diversity(G)$ | 생성물 간 평균 거리 기반 다양성 지표 |
| $d$ | feature space 또는 perceptual distance |

### 보안적 의미

Mode collapse가 있으면 생성물 패턴이 반복되어 검출 단서가 될 수 있다. 반대로 생성 다양성이 높아질수록 detector는 더 넓은 fake distribution을 처리해야 한다.

---

### 5.5 GAN 생성물 검출 지표

생성물 검출은 fake를 fake로 탐지하는 능력과 real을 오탐하지 않는 능력을 함께 봐야 한다.

$$
DetectionRate=\frac{TP_f}{TP_f+FN_f}
$$

$$
FPR=\frac{FP_r}{FP_r+TN_r}
$$

| 기호 | 의미 |
|---|---|
| $TP_f$ | fake를 fake로 올바르게 탐지 |
| $FN_f$ | fake를 real로 놓침 |
| $FP_r$ | real을 fake로 오탐 |
| $TN_r$ | real을 real로 올바르게 분류 |

### 보안적 의미

딥페이크 검출에서는 fake를 놓치는 미탐과 real을 fake로 오탐하는 문제가 모두 크다. 따라서 accuracy 하나로 평가하면 부족하다.

---

### 5.6 GAN Security Risk

GAN 기반 합성미디어의 보안 위험을 생성 품질, 탐지 회피, 개인정보 재현, provenance gap으로 요약한다.

$$
GANRisk=RealismRisk+EvasionRisk+PrivacyRisk+ProvenanceGap-DetectorCoverage
$$

### 보안적 의미

생성 품질이 높아질수록 현실감과 설득력은 커지지만, 합성물 검출과 출처 확인이 더 어려워진다.

---

### 5.7 Generator-Detector Gap

생성기 품질 향상과 detector 성능 간 격차를 단순화해 볼 수 있다.

$$
GenDetectGap=RealismScore-DetectionRate
$$

### 보안적 의미

RealismScore가 높고 DetectionRate가 낮으면 합성물이 탐지 체계를 우회할 위험이 커진다.

---

### 5.8 Provenance Coverage

GAN 생성물에 watermark 또는 provenance metadata가 확인되는 비율이다.

$$
ProvCoverage=\frac{N_{pc}}{N_{gen}}
$$

| 기호 | 의미 |
|---|---|
| $N_{gen}$ | 평가 대상 생성물 수 |
| $N_{pc}$ | provenance 또는 watermark가 확인된 생성물 수 |

### 보안적 의미

출처가 확인되지 않는 합성 이미지는 딥페이크, 허위 증거, 저작권 침해, RAG 근거 오염의 위험을 키운다.

---

## 6. AI 원리 70% 관점 분석

| 원리 항목 | 설명 | W06/P03에서의 의미 |
|---|---|---|
| Adversarial training | generator와 discriminator가 경쟁하며 학습 | GAN의 핵심 학습 원리 |
| Latent representation | noise vector $z$가 이미지 manifold로 매핑 | 얼굴·장면·스타일 생성의 기초 |
| Conditional generation | class, domain, image, semantic condition으로 생성 제어 | 표적 속성 조작·image translation 연결 |
| Distribution matching | 생성 분포가 실제 데이터 분포를 닮도록 학습 | FID/KID 등 생성 품질 평가의 배경 |
| Mode collapse | 생성 다양성이 부족해지는 문제 | 검출 단서 또는 품질 한계 |
| Training instability | discriminator/generator 균형이 깨지는 문제 | 품질·artifact·재현성 한계 |
| Image-to-image translation | 한 domain 이미지를 다른 domain으로 변환 | 얼굴 교체·스타일 변환·증거 조작 연결 |
| Super-resolution/restoration | 저품질 이미지를 고품질로 복원 | 포렌식·증거 신뢰성 문제 연결 |

---

## 7. 보안 이슈 30% 관점 분석

| 보안 항목 | GAN 관점 해석 | 대표 평가 지표 |
|---|---|---|
| 기밀성 | 학습 데이터의 얼굴·스타일·민감 패턴이 생성물에 재현될 수 있음 | memorization risk, nearest-neighbor similarity |
| 무결성 | 얼굴 합성, 속성 조작, image translation으로 시각 증거를 왜곡할 수 있음 | detection AUC, manipulation localization |
| 가용성 | 대량 synthetic content가 검토·탐지 시스템을 압박할 수 있음 | review cost, detector throughput |
| 프라이버시 | 특정 인물의 얼굴·속성·도메인 특징이 재현될 수 있음 | identity similarity, re-identification risk |
| 저작권/IP | 학습 데이터 스타일과 저작물 모방 문제가 발생 | content similarity, ProvCoverage |
| 책임성 | 생성 모델, latent seed, training dataset, post-processing log 기록 필요 | audit completeness, watermark robustness |

---

## 8. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | 얼굴 이미지, 신원, 시각 증거, 학습 데이터, generator checkpoint, latent seed, watermark, provenance log |
| 공격자 목표 | 합성 이미지 생성, 얼굴 교체, 속성 조작, 허위 증거 생성, detector 회피, provenance 제거 |
| 공격자 능력 | latent sampling, conditional input 조작, image-to-image translation, post-processing, compression, style transfer |
| 공격 경로 | latent/condition 입력 → GAN generator → synthetic image → post-processing → distribution/provenance decision |
| 방어자 능력 | GAN/deepfake detector, watermark, provenance log, human review, dataset governance, output hashing |
| 제외 범위 | 실제 인물 사칭 합성물 제작, 개인정보 이미지 사용, 불법·유해 이미지 생성, 탐지 우회 절차 제공 |

---

## 9. 평가방법 및 지표

| 평가축 | 지표 | 의미 | W06/P03 활용 |
|---|---|---|---|
| 생성 품질 | FID, IS, KID | 생성 이미지 품질과 분포 유사도 | 품질 baseline |
| 다양성 | Diversity, mode collapse indicator | 생성물 다양성 | detector coverage 해석 |
| 안정성 | training stability, convergence | GAN 학습 안정성 | 재현성 한계 |
| 검출 성능 | DetectionRate, AUC, FPR | 합성물 검출 성능 | deepfake detector 평가 |
| 프라이버시 | nearest-neighbor similarity, identity similarity | 학습 데이터 재현 가능성 | privacy 평가 |
| 출처 확인 | ProvCoverage, watermark robustness | 생성물 provenance 확인 | W14/W15 연결 |
| 조작 위치 | manipulation localization | 합성·변환 위치 식별 | 포렌식 평가 |
| 재현성 | model, seed, checkpoint, post-processing log | 결과 재현 가능성 | evidence chain |

---

## 10. 재현성 체크리스트

| 항목 | 기록해야 할 내용 |
|---|---|
| Bibliographic status | DOI, ACM CSUR 출판정보, arXiv 판본, 강의계획서 표기 차이, 로컬 PDF 상태 |
| Model | GAN variant, generator/discriminator architecture, checkpoint, license |
| Data | 공개 toy image 또는 synthetic sample만 사용, 개인정보·실제 인물 이미지 제외 |
| Generation config | latent seed, condition, resolution, truncation/style setting, post-processing |
| Evaluation | FID/IS/KID, Diversity, DetectionRate, FPR, ProvCoverage, privacy risk 분리 |
| Detector | detector model, threshold, dataset split, compression/editing 조건 |
| Output | generated image hash, watermark 여부, provenance metadata, post-processing 여부 |
| Security controls | watermark, detector, human review, safe logging, dataset governance |
| Evidence | config file, seed log, output hash, metric CSV/JSON, script commit |
| GitHub math | `\operatorname` 사용 금지, 긴 영문 subscript 대신 짧은 변수명과 표 설명 사용 |

---

## 11. 논문의 고유 기여

1. GAN 계열을 objective, architecture, training strategy, computer vision application 관점에서 체계적으로 정리했다.
2. W06에서 diffusion model과 비교할 수 있는 핵심 생성모형 배경을 제공한다.
3. 딥페이크 생성과 검출을 generator-discriminator arms race로 설명할 수 있는 이론적 언어를 제공한다.
4. Image-to-image translation과 conditional generation이 신원 조작, 속성 조작, 시각 증거 왜곡으로 확장될 수 있음을 설명한다.
5. 생성 품질, 다양성, detection, provenance, privacy를 분리해 평가해야 한다는 근거가 된다.

---

## 12. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 강의계획서 표기 차이 | 강의계획서의 `Tianqi Wang et al.` 표기와 공식 저자 목록이 다르다. | DOI 기준 인용, 동일성 검토 메모 유지 |
| 보안 직접성 제한 | GAN survey 자체는 딥페이크 검출 전문 문헌이 아니다. | W06 P04/P05 deepfake detection 문헌과 결합 |
| 최신 diffusion 대비 | 2024 이후 생성형 모델은 diffusion/video model 중심으로 빠르게 변화했다. | P01/P02와 비교해 GAN 배경 문헌으로 사용 |
| 평가 지표 한계 | FID/IS는 실제 보안 위험을 직접 측정하지 않는다. | detection, provenance, privacy 지표 병기 |
| 재현성 문제 | GAN 학습은 seed, architecture, data, hyperparameter에 민감하다. | config와 seed 기록 강화 |
| 악용 위험 | 실제 얼굴 합성 절차를 상세화하면 부적절하다. | 원리·평가·방어 중심으로 제한 |

---

## 13. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | GAN 기반 합성 이미지와 딥페이크가 시각 정보 신뢰성을 약화한다는 문제의식 |
| 2장 관련연구 | GAN taxonomy와 diffusion 대비 생성모형 배경 정리 |
| 3장 위협모형 | latent seed, condition, generator checkpoint, synthetic image, watermark, provenance log 보호 자산 정의 |
| 4장 연구방법 | minimax objective, cGAN, WGAN, DetectionRate, FPR, GANRisk, ProvCoverage 지표 설계 |
| 5장 분석 | GAN generation-detection arms race와 synthetic media security risk matrix 제시 |
| 6장 보안적 함의 | 신원 사칭, 속성 조작, 시각 증거 조작, detector 일반화, provenance 필요성 해석 |
| 부록 | model/checkpoint, seed, condition, output hash, detector threshold, watermark/provenance log 수록 |

---

## 14. 기말논문 연결 3문장

1. W06에서 기말논문에 반영할 개념: GAN은 generator와 discriminator의 경쟁 학습을 통해 고품질 합성 이미지를 생성하며, 이는 딥페이크 생성과 검출 arms race의 이론적 기반이다.
2. W06에서 기말논문에 반영할 표·그림·실험: minimax objective, conditional GAN, WGAN, DetectionRate, FPR, GANRisk, ProvCoverage 수식표와 GAN generation-detection pipeline을 반영한다.
3. W06이 W14/W15와 연결되는 지점: GAN 생성 결과는 model/checkpoint, latent seed, condition, output hash, watermark, detector score를 evidence chain으로 남겨야 재현성과 책임성을 확보할 수 있다.

---

## 15. 최종 판단

P03은 W06의 GAN 생성모형 핵심 문헌이다. 직접적인 딥페이크 검출 논문은 아니지만, GAN이 어떻게 시각 합성물을 생성하고 왜 detector와 arms race를 형성하는지 설명한다. 따라서 기말논문에서는 P03을 **GAN taxonomy, adversarial training, synthetic image generation, image manipulation, detector arms race, provenance/watermark 평가의 배경 문헌**으로 사용하는 것이 적절하다.

---

## 16. GitHub 수식 호환성 메모

이 파일에서는 GitHub 수식 렌더링 오류 방지를 위해 `\operatorname`을 사용하지 않는다.

| 피해야 할 표현 | 권장 표현 |
|---|---|
| `\operatorname{softmax}` | `\mathrm{softmax}` |
| `\operatorname{argmax}` | `\mathrm{argmax}` 또는 `\arg\max` |
| `TP_{fake}` | `TP_f`처럼 짧은 변수명 사용 후 표에서 의미 설명 |
| `FP_{real}` | `FP_r`처럼 짧은 변수명 사용 후 표에서 의미 설명 |
| 긴 영문 subscript | 짧은 변수명 사용 후 표에서 의미 설명 |

```bash
pandoc P03_summary.md -o P03_summary.docx
pandoc P03_summary.md -o P03_summary.pdf --pdf-engine=xelatex
```
