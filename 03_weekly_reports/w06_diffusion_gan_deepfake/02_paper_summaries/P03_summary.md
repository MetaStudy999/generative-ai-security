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
| PDF 확인 메모 | repo의 PDF 폴더에 해당 PDF blob이 존재함을 확인했다. 요약은 로컬 PDF 경로와 공식 DOI/arXiv 메타데이터 기준으로 보완했다. |
| 핵심 근거 사용 가능 여부 | 가능. W06에서 diffusion model과 대비되는 GAN 기반 생성 원리, computer vision 응용, 딥페이크 생성·검출 arms race 배경 문헌으로 사용 |

---

## 1. 한 문장 요약

이 논문은 GAN을 **generator-discriminator minimax game, adversarial training, objective variants, architecture variants, image synthesis, image-to-image translation, super-resolution, domain adaptation, evaluation, open challenges** 관점에서 분류한 computer vision 중심 survey이며, W06에서 딥페이크 생성 원리와 생성-검출 arms race를 설명하는 핵심 배경 문헌이다.

---

## 2. 핵심 연구문제

> GAN은 생성기와 판별기의 경쟁 학습을 통해 시각 데이터 분포를 어떻게 학습하며, computer vision 응용에서 생성 품질·다양성·안정성·평가 한계가 어떤 방식으로 보안 위협과 연결되는가?

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

---

## 4. 핵심 이론 및 수식

> 아래 수식은 GAN 원리와 W06 보안 평가를 설명하기 위한 표준화된 표현이다. 수식은 GitHub, MS Word, PDF 변환 호환성을 위해 Markdown 표 밖의 LaTeX block math로 작성한다.

### 4.1 GAN Minimax Objective

GAN은 생성기 $G$와 판별기 $D$가 경쟁하는 minimax 문제로 정식화된다.

$$
\min_G \max_D V(D,G)=\mathbb{E}_{x\sim p_{data}}[\log D(x)] + \mathbb{E}_{z\sim p_z}[\log(1-D(G(z)))]
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

### 4.2 Conditional GAN

조건부 GAN은 class label, text, image, semantic map 등 조건 $c$를 사용해 생성 방향을 제어한다.

$$
\min_G \max_D V(D,G)=\mathbb{E}_{x\sim p_{data}}[\log D(x\mid c)] + \mathbb{E}_{z\sim p_z}[\log(1-D(G(z\mid c)\mid c))]
$$

| 기호 | 의미 |
|---|---|
| $c$ | class, text, image, mask, domain 등 condition |
| $G(z\mid c)$ | 조건 $c$에 맞게 생성된 sample |
| $D(x\mid c)$ | 조건과 sample의 정합성을 판별하는 discriminator |

### 보안적 의미

조건부 생성은 특정 얼굴, 속성, 도메인, 장면을 제어하는 데 쓰일 수 있다. 이는 창작·복원에는 유용하지만 신원 사칭, 속성 조작, 허위 이미지 생성 위험을 높인다.

---

### 4.3 Wasserstein GAN 관점

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

### 4.4 Mode Collapse와 다양성 평가

GAN은 생성 다양성이 낮아지는 mode collapse 문제가 발생할 수 있다.

$$
Diversity(G)=\mathbb{E}_{z_i,z_j}\left[d(G(z_i),G(z_j))\right]
$$

| 기호 | 의미 |
|---|---|
| $Diversity(G)$ | 생성물 간 평균 거리 기반 다양성 지표 |
| $d(\cdot,\cdot)$ | feature space 또는 perceptual distance |

### 보안적 의미

Mode collapse가 있으면 생성물 패턴이 반복되어 검출 단서가 될 수 있다. 반대로 생성 다양성이 높아질수록 detector는 더 넓은 fake distribution을 처리해야 한다.

---

### 4.5 GAN 생성물 검출 지표

생성물 검출은 fake를 fake로 탐지하는 능력과 real을 오탐하지 않는 능력을 함께 봐야 한다.

$$
DetectionRate=\frac{TP_{fake}}{TP_{fake}+FN_{fake}}
$$

$$
FPR=\frac{FP_{real}}{FP_{real}+TN_{real}}
$$

| 기호 | 의미 |
|---|---|
| $TP_{fake}$ | fake를 fake로 올바르게 탐지 |
| $FN_{fake}$ | fake를 real로 놓침 |
| $FP_{real}$ | real을 fake로 오탐 |
| $TN_{real}$ | real을 real로 올바르게 분류 |

### 보안적 의미

딥페이크 검출에서는 fake를 놓치는 미탐과 real을 fake로 오탐하는 문제가 모두 크다. 따라서 accuracy 하나로 평가하면 부족하다.

---

## 5. AI 원리 70% 관점 분석

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

## 6. 보안 이슈 30% 관점 분석

| 보안 항목 | GAN 관점 해석 | 대표 평가 지표 |
|---|---|---|
| 기밀성 | 학습 데이터의 얼굴·스타일·민감 패턴이 생성물에 재현될 수 있음 | memorization risk, nearest-neighbor similarity |
| 무결성 | 얼굴 합성, 속성 조작, image translation으로 시각 증거를 왜곡할 수 있음 | detection AUC, manipulation localization |
| 가용성 | 대량 synthetic content가 검토·탐지 시스템을 압박할 수 있음 | review cost, detector throughput |
| 프라이버시 | 특정 인물의 얼굴·속성·도메인 특징이 재현될 수 있음 | identity similarity, re-identification risk |
| 저작권/IP | 학습 데이터 스타일과 저작물 모방 문제가 발생 | content similarity, provenance coverage |
| 책임성 | 생성 모델, latent seed, training dataset, post-processing log 기록 필요 | audit completeness, watermark robustness |

---

## 7. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | 얼굴 이미지, 신원, 시각 증거, 학습 데이터, generator checkpoint, latent seed, watermark, provenance log |
| 공격자 목표 | 합성 이미지 생성, 얼굴 교체, 속성 조작, 허위 증거 생성, 검출 우회, 출처 위조 |
| 공격자 능력 | GAN 모델 사용·학습, latent manipulation, image-to-image translation, post-processing, compression, fine-tuning |
| 공격 경로 | training data → GAN training/fine-tuning → synthetic image generation → editing/compression → distribution |
| 방어자 능력 | GAN artifact detector, frequency analysis, provenance metadata, watermark, human review, cross-generator evaluation |
| 제외 범위 | 실제 인물 사칭물 제작, 무단 얼굴 데이터 수집, 유해 합성물 생성, 실제 서비스 공격 |

---

## 8. 평가방법 및 지표

| 평가축 | 지표 | 의미 | W06/P03 활용 |
|---|---|---|---|
| 생성 품질 | FID, IS, KID | 실제 이미지 분포와 생성물 분포 유사성 | 생성 성능 배경 |
| 다양성 | LPIPS diversity, mode coverage | mode collapse 여부 | 생성 분포 평가 |
| 조건 정합성 | classification accuracy, conditional consistency | 조건부 생성이 의도와 맞는지 | 속성 조작·translation 평가 |
| 검출 성능 | AUC, F1, FPR/FNR | GAN 생성물 탐지 성능 | 딥페이크 검출 연결 |
| 일반화 | cross-generator AUC | 보지 못한 GAN 변형에도 검출되는지 | detector overfitting 방지 |
| 강건성 | compression/crop/noise robustness | 플랫폼 업로드 후 탐지 유지 | 운영 평가 |
| 포렌식 단서 | frequency artifact, texture artifact | GAN 생성물의 특징적 artifact | detector feature 분석 |
| 감사 가능성 | seed/model/output hash/provenance log | 사후 검증 가능성 | W14/W15 evidence chain |

---

## 9. 재현성 체크리스트

| 항목 | 기록해야 할 내용 |
|---|---|
| 모델 | GAN variant, generator/discriminator architecture, checkpoint, license |
| 데이터 | dataset source, preprocessing, train/test split, face/person data 포함 여부 |
| 학습 설정 | loss function, optimizer, batch size, epoch, seed, augmentation |
| 생성 설정 | latent seed, condition, truncation, output resolution, post-processing |
| 평가 | FID/KID/IS, detection AUC/F1, cross-generator test, artifact analysis |
| 보안 로그 | model version, generated output hash, watermark/provenance metadata |
| 한계 | toy/synthetic generation 결과를 실제 딥페이크 탐지 보증으로 일반화하지 않음 |

---

## 10. 논문의 고유 기여

1. GAN 연구를 computer vision task와 taxonomy 중심으로 체계화한다.
2. Generator-discriminator 경쟁 학습이 image synthesis와 image manipulation에 어떻게 활용되는지 설명한다.
3. GAN의 강점뿐 아니라 mode collapse, training instability, evaluation difficulty 같은 한계를 정리한다.
4. W06에서 diffusion model(P01/P02)과 비교할 수 있는 고전적 생성모형 기준축을 제공한다.
5. Deepfake creation/detection 문헌(P04/P05)을 이해하기 위한 GAN 기반 생성 원리와 artifact 평가 배경을 제공한다.

---

## 11. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 최신 diffusion 중심 환경과 차이 | 현재 고품질 생성은 diffusion 계열이 강하지만 GAN도 여전히 중요한 생성 배경이다. | P01/P02 diffusion 문헌과 비교 |
| 직접 딥페이크 검출 논문은 아님 | GAN survey이며 deepfake detector reliability를 직접 다루지는 않는다. | P04/P05와 결합 |
| 평가 지표 한계 | FID/IS는 인간 지각과 보안 위험을 완전히 설명하지 못한다. | detector AUC, provenance, human review 병기 |
| Artifact 변화 | GAN 변형과 post-processing에 따라 artifact가 달라진다. | cross-generator, compression robustness 평가 추가 |
| 강의계획서 표기 차이 | 강의계획서의 `Tianqi Wang et al.` 표기와 공식 확인 저자 `Zhengwei Wang et al.` 차이 존재 | 최종 제출 전 교수자 확인 메모 유지 |

---

## 12. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | 합성미디어 보안은 GAN과 diffusion 같은 생성모형 발전에 따라 탐지·책임성 문제가 커진다는 문제의식 |
| 2장 관련연구 | GAN minimax objective, CV application taxonomy, image synthesis/translation 연구 흐름 |
| 3장 위협모형 | generator, latent seed, image translation, post-processing, provenance log 보호 자산 정의 |
| 4장 연구방법 | FID/KID, diversity, detection AUC, cross-generator robustness, FPR/FNR 지표 설계 |
| 5장 분석 | GAN 생성-검출 arms race와 diffusion 생성물 비교표 |
| 6장 보안적 함의 | 딥페이크, 시각 증거 조작, 저작권, 프라이버시, human review 필요성 해석 |

---

## 13. 기말논문 연결 3문장

1. W06에서 기말논문에 반영할 개념: GAN은 generator와 discriminator의 경쟁 학습을 통해 고품질 합성 이미지를 만들 수 있으며, 이는 딥페이크 생성과 검출기의 arms race를 설명하는 기본 모델이다.
2. W06에서 기말논문에 반영할 표·그림·실험: GAN minimax 수식, generator-discriminator 구조도, FID/KID와 detection AUC/FPR/FNR 비교표, GAN-vs-diffusion 생성물 평가표를 반영한다.
3. W06이 RAG/LLM 보안 감사 프레임워크와 연결되는 지점: GAN 기반 합성 이미지도 멀티모달 RAG의 근거 자료로 유입될 수 있으므로, 이미지 출처·생성 로그·artifact 분석·provenance를 W14/W15 evidence chain에 포함해야 한다.

---

## 14. 최종 판단

P03은 W06에서 GAN 기반 생성모형의 핵심 문헌이다. P01/P02가 diffusion 기반 생성 원리를 제공한다면, P03은 GAN의 경쟁 학습 구조와 computer vision 응용을 통해 딥페이크와 이미지 조작의 고전적 기반을 제공한다. 따라서 W06의 생성형 AI 보안 프레임워크에서는 P03을 **GAN 생성-검출 arms race와 시각 조작 위협모형의 근거 문헌**으로 사용하는 것이 적절하다.

---

## 15. 변환 호환성 메모

```bash
pandoc P03_summary.md -o P03_summary.docx
pandoc P03_summary.md -o P03_summary.pdf --pdf-engine=xelatex
```
