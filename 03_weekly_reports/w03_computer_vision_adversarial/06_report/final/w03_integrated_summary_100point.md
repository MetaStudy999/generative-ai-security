# W03 100점형 통합 Summary

## 컴퓨터비전 표현학습 & 비전 대적공격

## 0. 문서 목적

이 문서는 W03 개별 논문 summary 5개를 기말논문 작성용 연구 노트로 통합한 100점형 요약본이다. 기존 `integrated_report_final.md`는 제출용 통합보고서이고, 본 문서는 개별 PDF summary 보강 결과를 반영한 **논문 작성용 압축본**으로 사용한다.

| 항목 | 내용 |
|---|---|
| 주차 | W03 |
| 주제 | 컴퓨터비전 표현학습 & 비전 대적공격 |
| 주요 문헌 | P01–P05 |
| 핵심 프레임 | CNN 표현학습 + CV task 지표 + 멀티모달 Transformer + Vision Transformer + 2D/3D adversarial robustness |
| 수식 작성 방식 | GitHub / Word / PDF 변환 호환을 위해 LaTeX block math 사용 |
| 주의사항 | 원문 수치를 임의 전사하지 않고, 문헌별 구조·수식·위협모형·평가지표 중심으로 정리 |

---

## 1. 한 문장 통합 요약

W03은 컴퓨터비전 모델을 **CNN의 지역 표현학습, CV task별 평가 구조, 멀티모달 Transformer의 alignment, ViT의 patch-token attention, 2D/3D 대적공격과 물리 안전성**으로 확장하여, 비전 AI 보안 평가는 clean performance와 robust/safety performance를 분리해야 함을 정리하는 주차다.

---

## 2. W03 핵심 연구질문

| 번호 | 연구질문 |
|---|---|
| RQ1 | CNN의 convolution, pooling, gradient-based learning은 비전 표현학습의 어떤 귀납편향을 제공하는가? |
| RQ2 | Classification, detection, recognition, pose estimation 등 CV task별 실패 조건과 보안 지표는 어떻게 다른가? |
| RQ3 | 멀티모달 Transformer는 modality alignment와 fusion 과정에서 어떤 새로운 공격면을 만드는가? |
| RQ4 | Vision Transformer의 patch-token 구조는 CNN과 다른 취약성을 어떻게 만드는가? |
| RQ5 | 2D/3D adversarial attack과 physical-world attack은 어떤 threat model과 평가 지표로 분리해야 하는가? |
| RQ6 | W03의 비전 보안 평가축을 멀티모달 LLM, RAG 문서/이미지 입력, MLOps 감사로 어떻게 확장할 수 있는가? |

---

## 3. 문헌 5편 통합 매트릭스

| ID | 논문 | 핵심 역할 | 주요 수식/지표 | 기말논문 반영 위치 |
|---|---|---|---|---|
| P01 | LeCun et al., *Gradient-Based Learning Applied to Document Recognition* | CNN, convolution, pooling, end-to-end gradient learning | 2D convolution, pooling, gradient update | 2장 관련연구, 3장 입력 위협모형 |
| P02 | Voulodimos et al., *Deep Learning for Computer Vision* | CV task taxonomy와 task별 평가 지표 | softmax, cross-entropy, task metrics | 2장 관련연구, 4장 평가방법 |
| P03 | Xu et al., *Multimodal Learning With Transformers* | modality tokenization, cross-modal attention, alignment | attention, cross-modal fusion, alignment loss | 3장 멀티모달 위협모형 |
| P04 | Khan et al., *Transformers in Vision* | ViT, patch embedding, self-attention, CNN-ViT 차이 | patch embedding, MSA, robust drop | 2장 관련연구, 4장 평가방법 |
| P05 | Li et al., *2D and 3D Robustness and Safety* | 2D/3D adversarial robustness와 safety 평가 | adversarial perturbation, FGSM, robust accuracy, ASR | 3장 위협모형, 5장 분석/실험 |

---

## 4. AI 원리 70% 통합 정리

### 4.1 2D Convolution

CNN은 입력 이미지의 국소 영역에 같은 kernel을 반복 적용해 공간 패턴을 학습한다.

$$
Y_{i,j,k}=b_k+\sum_{u,v,c}W_{u,v,c,k}X_{i+u,j+v,c}
$$

| 기호 | 의미 |
|---|---|
| $X$ | 입력 이미지 또는 특징맵 |
| $Y$ | 출력 특징맵 |
| $W$ | convolution kernel |
| $b_k$ | bias |

**보안 해석:** 지역 패턴을 학습하는 CNN은 patch, noise, local perturbation에 영향을 받을 수 있다. Local feature가 전체 decision에 과도한 영향을 주면 adversarial patch나 localized corruption이 위험해진다.

---

### 4.2 Softmax와 Cross-Entropy

분류 모델은 logit을 class 확률로 변환하고 cross-entropy를 최소화한다.

$$
p_k=\frac{e^{z_k}}{\sum_{j=1}^{K} e^{z_j}}
$$

$$
CE(y,p)=-\sum_{k=1}^{K}y_k\log p_k
$$

**보안 해석:** Softmax confidence와 margin은 공격자가 예측 변화, membership leakage, calibration failure를 분석하는 단서가 될 수 있다.

---

### 4.3 Attention과 Multimodal Fusion

Transformer는 token 간 관계를 attention으로 모델링한다.

$$
Attention(Q,K,V)=\operatorname{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V
$$

이미지와 텍스트 간 cross-modal fusion은 다음처럼 표현할 수 있다.

$$
H_{I \leftarrow T}=\operatorname{softmax}\left(\frac{Q_IK_T^T}{\sqrt{d_k}}\right)V_T
$$

**보안 해석:** 한 modality의 오염이 다른 modality의 판단을 바꿀 수 있다. 이미지 patch, caption 조작, prompt injection, retrieval contamination은 멀티모달 attention/fusion 단계에서 결합될 수 있다.

---

### 4.4 Vision Transformer Patch Embedding

ViT는 이미지를 patch token sequence로 변환한다.

$$
Z_0=[x_{cls};x_p^1E;x_p^2E;\cdots;x_p^NE]+E_{pos}
$$

**보안 해석:** ViT에서는 pixel 단위뿐 아니라 patch token, position embedding, attention map이 공격면이 된다.

---

## 5. 보안 이슈 30% 통합 정리

| 보안 축 | 관련 논문 | 핵심 문제 | 주요 지표/증거 |
|---|---|---|---|
| CNN 입력 무결성 | P01 | local perturbation, patch, OCR 오인식 | clean accuracy, robust accuracy |
| CV task 안전성 | P02 | task별 실패 비용 차이 | mAP, FAR/FRR, keypoint error, robust metric |
| 멀티모달 alignment | P03 | modality mismatch, caption/prompt 오염 | retrieval recall, grounding accuracy, alignment consistency |
| ViT patch 취약성 | P04 | patch corruption, attention perturbation | patch robustness, attention stability, robust drop |
| 2D/3D adversarial safety | P05 | digital/physical attack, LiDAR/point cloud 취약성 | ASR, robust accuracy, safety impact |

---

## 6. W03 통합 위협모형

### 6.1 보호 자산

| 보호 자산 | 설명 |
|---|---|
| 2D 이미지 | 분류·탐지·인식 모델 입력 |
| 3D point cloud / LiDAR | 자율주행·로봇·공간 인식 입력 |
| Patch token | ViT 입력 단위 |
| Caption / Text prompt | 멀티모달 모델의 텍스트 modality |
| Embedding / Attention | 내부 표현과 cross-modal alignment |
| Output decision | class, detection box, segmentation, caption, VQA answer |
| Evaluation log | clean/robust/safety metric과 실패 사례 |

### 6.2 공격자 능력

| 공격자 유형 | 가능 행위 | 대표 지표 |
|---|---|---|
| Pixel perturbation attacker | 작은 norm 제한 교란 삽입 | robust accuracy, robust drop |
| Patch attacker | 국소 patch 또는 sticker 삽입 | ASR, missed detection |
| Physical attacker | 조명, 각도, 인쇄물, 3D object 조작 | physical realizability, safety impact |
| Multimodal attacker | caption, prompt, image-text pair 조작 | alignment consistency, retrieval error |
| Data attacker | pretraining/fine-tuning data 또는 annotation 오염 | data lineage, clean/robust metric |

### 6.3 공격 경로

```text
이미지/비디오/3D/텍스트 입력
→ 전처리 및 tokenization
→ CNN feature 또는 Transformer attention
→ task head 또는 multimodal fusion
→ output decision
→ 공격자가 pixel/patch/modality/alignment/physical condition을 조작
→ 오분류, 미탐, 잘못된 grounding, safety failure 발생
```

---

## 7. 통합 평가 지표

| 평가축 | 대표 지표 | 해석 | 관련 논문 |
|---|---|---|---|
| Clean Performance | accuracy, F1, mAP, PCK | 정상 조건 성능 | P01, P02 |
| Robust Performance | robust accuracy, robust drop | 교란 조건 성능 | P04, P05 |
| Attack Success | ASR, targeted success | 공격 목표 달성 여부 | P05 |
| Physical Safety | safety impact, physical realizability | 실제 환경 위험 | P05 |
| Multimodal Alignment | retrieval recall, grounding accuracy, alignment consistency | modality 정합성 | P03 |
| Patch/Attention Stability | patch corruption robustness, attention stability | ViT 특화 안정성 | P04 |
| Reproducibility | seed, config, dataset, perturbation setting, failure cases | 재현성과 감사 가능성 | P01–P05 |

---

## 8. 핵심 수식 묶음

### 8.1 대적 교란

$$
x^{adv}=x+\delta, \qquad \lVert\delta\rVert_p \leq \epsilon
$$

### 8.2 FGSM 개념식

$$
x^{adv}=x+\epsilon\cdot\operatorname{sign}\left(\nabla_x\ell(f_{\theta}(x),y)\right)
$$

### 8.3 Robust Accuracy와 Robust Drop

$$
RobustAcc=\frac{1}{n}\sum_{i=1}^{n}\mathbf{1}[f_{\theta}(x_i^{adv})=y_i]
$$

$$
RobustDrop=CleanAcc-RobustAcc
$$

### 8.4 Patch Embedding

$$
Z_0=[x_{cls};x_p^1E;x_p^2E;\cdots;x_p^NE]+E_{pos}
$$

### 8.5 Cross-Modal Attention

$$
H_{I \leftarrow T}=\operatorname{softmax}\left(\frac{Q_IK_T^T}{\sqrt{d_k}}\right)V_T
$$

---

## 9. 재현성 체크리스트

| 항목 | 필수 기록 | W03 적용 |
|---|---|---|
| 문헌 | DOI, URL, 로컬 PDF명, 검증 상태 | P01–P05 summary에 반영 |
| 데이터 | dataset, split, preprocessing, augmentation | toy image 또는 공개 dataset 기준 |
| 모델 | CNN, ViT, multimodal model, baseline | 모델 구조와 version 기록 |
| 공격 조건 | epsilon, norm, patch size, physical assumption | 안전한 toy perturbation만 사용 |
| 평가 | clean accuracy, robust accuracy, ASR, robust drop | CSV/JSON 저장 |
| 실패 사례 | 오분류 이미지, confusion matrix, attention/failure note | 보고서 부록화 |
| 한계 | toy 결과의 실제 2D/3D 안전성 일반화 금지 | 명시 필요 |
| AI 활용 | 사용 도구, 목적, 검증 방식 | AI 활용 고지 필요 |

---

## 10. 기말논문 반영 구조

| 기말논문 장 | W03 반영 내용 |
|---|---|
| 1장 서론 | 비전 AI의 입력 취약성, physical attack, 안전성 문제 제시 |
| 2장 관련연구 | CNN, CV task, multimodal transformer, ViT, 2D/3D robustness 정리 |
| 3장 위협모형 | pixel, patch, modality, attention, physical attack 경로 정의 |
| 4장 연구방법 | clean/robust/ASR/safety/alignment 지표 설계 |
| 5장 실험/분석 | toy perturbation 또는 문헌 기반 2D/3D 비교표 제시 |
| 6장 보안적 함의 | 무결성, 안전성, 프라이버시, 책임성 해석 |
| 7장 결론 | 비전 AI 보안은 모델 구조별·modality별·환경별 평가가 필요함을 제시 |

---

## 11. W03 기말논문 연결 3문장

1. W03에서 기말논문에 반영할 개념: 비전 AI 보안은 CNN/ViT/멀티모달 구조에 따라 공격면이 달라지므로 clean accuracy와 robust/safety metric을 분리해야 한다.
2. W03에서 기말논문에 반영할 표·그림·실험: CNN convolution 수식, ViT patch embedding 수식, FGSM/robust accuracy 수식, 2D/3D threat model 표, clean-robust 비교표를 반영한다.
3. W03이 RAG 문서 오염/LLM 보안 감사 프레임워크와 연결되는 지점: 멀티모달 RAG와 LLM은 이미지·문서·caption·embedding을 함께 처리하므로 W03의 modality/attention/robustness 평가축을 W07/W08/W14로 확장한다.

---

## 12. 최종 판단

W03의 5개 문헌은 다음 역할로 정리한다.

| 문헌 | 최종 판단 |
|---|---|
| P01 | CNN과 gradient-based visual representation의 고전 핵심 문헌 |
| P02 | CV task별 평가와 보안 영향 범위를 넓히는 배경 문헌 |
| P03 | 멀티모달 Transformer와 alignment 보안으로 확장하는 bridge 문헌 |
| P04 | ViT patch/token/attention 구조와 CNN 차이를 설명하는 핵심 문헌 |
| P05 | 2D/3D adversarial robustness와 safety 평가의 핵심 보안 문헌 |

W03은 후속 W07 멀티모달 LLM, W08 RAG/프롬프트 인젝션, W14 MLOps 운영 보안과 연결된다. 특히 기말논문에서는 “멀티모달 입력이 모델 컨텍스트에 들어갈 때 어떤 robust/safety evidence를 남겨야 하는가”라는 문제로 발전시킬 수 있다.

---

## 13. 변환 호환성 메모

```bash
pandoc w03_integrated_summary_100point.md -o w03_integrated_summary_100point.docx
pandoc w03_integrated_summary_100point.md -o w03_integrated_summary_100point.pdf --pdf-engine=xelatex
```
