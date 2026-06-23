# P03 Summary

## Generative Adversarial Networks in Computer Vision: A Survey and Taxonomy — Zhengwei Wang, Qi She, Tomas E. Ward, ACM Computing Surveys, 2021

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W06 확률생성모형(Diffusion/GAN) & 딥페이크 검출 |
| 논문명 | Generative Adversarial Networks in Computer Vision: A Survey and Taxonomy |
| 저자 | Zhengwei Wang, Qi She, Tomas E. Ward |
| 학술지 | ACM Computing Surveys |
| 권호/쪽 | Vol. 54, No. 2, Article 37 |
| 연도 | online 2021 / print 2022 |
| DOI | https://doi.org/10.1145/3439723 |
| 보조 URL | https://arxiv.org/abs/1906.01529 |
| 로컬 PDF | `01_papers/pdf/03_Wang_She_Ward_2021_GANs_Computer_Vision_Survey.pdf` |
| 검증 상태 | W06 `paper_list.md` 기준 출판 DOI 확인. 강의계획서 저자명 차이 메모 유지 |

---

## 1. 한 문장 요약

이 논문은 GAN을 **generator-discriminator minimax game, image synthesis, image-to-image translation, super-resolution, domain adaptation, evaluation** 관점에서 정리하고, W06에서 딥페이크 생성과 검출의 고전적 생성모형 배경을 제공한다.

---

## 2. 핵심 연구질문

| 번호 | 연구질문 |
|---|---|
| RQ1 | GAN은 generator와 discriminator의 경쟁 학습으로 어떻게 데이터 분포를 학습하는가? |
| RQ2 | GAN 변형은 컴퓨터비전 생성 task에 어떻게 확장되었는가? |
| RQ3 | GAN 기반 생성물은 딥페이크·이미지 조작·검출 회피 문제와 어떻게 연결되는가? |
| RQ4 | GAN 생성물 검출은 어떤 artifact와 평가 지표를 사용해야 하는가? |

---

## 3. 핵심 수식

### 3.1 GAN Minimax Objective

$$
\min_G \max_D V(D,G)=\mathbb{E}_{x\sim p_{data}}[\log D(x)] + \mathbb{E}_{z\sim p_z}[\log(1-D(G(z)))]
$$

| 기호 | 의미 |
|---|---|
| $G$ | generator |
| $D$ | discriminator |
| $z$ | latent noise |
| $p_{data}$ | 실제 데이터 분포 |

**보안 해석:** Discriminator가 진짜/가짜를 구분하도록 학습되는 구조는 딥페이크 검출기와 개념적으로 연결된다. 그러나 생성기가 발전하면 검출기도 계속 재학습해야 한다.

### 3.2 생성물 검출 위험

$$
DetectionRate=\frac{TP_{fake}}{TP_{fake}+FN_{fake}}
$$

$$
FPR=\frac{FP_{real}}{FP_{real}+TN_{real}}
$$

---

## 4. AI 원리·보안 분석

| 항목 | 분석 |
|---|---|
| Adversarial training | 생성기와 판별기가 경쟁하며 학습한다. |
| Mode collapse | 생성 다양성 부족이 발생할 수 있다. |
| Image translation | 얼굴·스타일·도메인 변환에 활용된다. |
| Deepfake risk | 얼굴 합성·속성 조작·신원 사칭에 악용될 수 있다. |
| Detector arms race | 생성기 품질이 오르면 검출기 성능이 낮아질 수 있다. |

---

## 5. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 대상 | 얼굴 이미지, 신원, 원본성, 생성물 provenance, 검출기 |
| 공격자 목표 | 합성 이미지 생성, 판별기 회피, 허위 시각 증거 생성 |
| 공격자 능력 | GAN 학습/사용, post-processing, 압축, style/identity transfer |
| 제외 범위 | 실제 인물 사칭물 제작, 무단 얼굴 데이터 사용 |

---

## 6. 평가방법 및 지표

| 지표 | 의미 |
|---|---|
| FID/IS | 생성 이미지 품질 평가 |
| Detection AUC/F1 | GAN 생성물 검출 성능 |
| Cross-dataset Generalization | 다른 생성기/데이터셋에서 검출 유지 여부 |
| Robustness | 압축·크롭·재인코딩 후 검출 유지 |
| Artifact Analysis | 주파수·텍스처·얼굴 경계 artifact 확인 |

---

## 7. 재현성·기말논문 연결

| 항목 | 반영 내용 |
|---|---|
| 재현성 | 생성기 종류, latent seed, training data, post-processing, detector version 기록 |
| 한계 | GAN survey이므로 최신 diffusion deepfake를 모두 대표하지 않음 |
| 기말논문 | GAN 생성-검출 arms race, deepfake detector generalization 지표로 반영 |

---

## 8. 최종 판단

P03은 W06에서 GAN 기반 생성과 딥페이크 검출의 역사적·기술적 배경을 제공한다. 최신 diffusion 기반 생성물은 P01/P02와 함께 비교한다.
