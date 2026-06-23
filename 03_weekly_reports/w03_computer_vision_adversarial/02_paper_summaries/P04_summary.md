# P04 Summary

## Transformers in Vision: A Survey — Salman Khan et al., ACM Computing Surveys, 2022

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W03 컴퓨터비전 표현학습 & 비전 대적공격 |
| 논문명 | Transformers in Vision: A Survey |
| 저자 | Salman Khan, Muzammal Naseer, Munawar Hayat, Syed Waqas Zamir, Fahad Shahbaz Khan, Mubarak Shah |
| 학술지 | ACM Computing Surveys |
| 권호/쪽 | Vol. 54, No. 10s, pp. 1–41 |
| 연도 | 2022 |
| DOI | https://doi.org/10.1145/3505244 |
| 논문 유형 | Survey / Vision Transformer Review |
| 로컬 PDF | `01_papers/pdf/04_Khan_et_al_2022_Transformers_in_Vision_Survey.pdf` |
| 강의계획서 지정 논문과 일치 여부 | 일치 |
| 핵심 근거 사용 가능 여부 | 가능 |
| 검증 메모 | W03 `paper_list.md` 기준 Crossref/ACM URL 및 로컬 PDF 제목 일치 확인 |

---

## 1. 한 문장 요약

이 논문은 Transformer가 컴퓨터비전에서 **patch embedding, self-attention, positional encoding, pretraining/fine-tuning, classification/detection/segmentation/generation/3D task**로 확장된 흐름을 정리하고, CNN과 ViT의 inductive bias 차이가 비전 보안 평가와 취약성 분석에 영향을 준다는 점을 보여주는 survey 논문이다.

---

## 2. 연구문제

> NLP에서 성공한 Transformer 구조가 이미지와 비디오 등 시각 데이터에 어떻게 적용되며, CNN과 다른 표현 구조가 비전 모델의 성능·효율성·강건성·취약성에 어떤 차이를 만드는가?

| 번호 | 연구질문 |
|---|---|
| RQ1 | 이미지는 patch token sequence로 어떻게 변환되는가? |
| RQ2 | Vision Transformer의 self-attention은 CNN의 local convolution과 어떤 구조적 차이를 갖는가? |
| RQ3 | Pretraining과 fine-tuning은 ViT 성능과 재현성에 어떤 영향을 주는가? |
| RQ4 | Patch corruption, attention perturbation, data bias는 ViT 보안 평가에 어떤 의미가 있는가? |
| RQ5 | CNN과 ViT를 비교할 때 clean accuracy와 robust accuracy를 왜 분리해야 하는가? |

---

## 3. 핵심 이론 및 수식

### 3.1 Patch Embedding

Vision Transformer는 이미지를 고정 크기 patch로 나누고 각 patch를 token embedding으로 변환한다.

$$
Z_0=[x_{cls};x_p^1E;x_p^2E;\cdots;x_p^NE]+E_{pos}
$$

| 기호 | 의미 |
|---|---|
| $x_{cls}$ | classification token |
| $x_p^i$ | $i$번째 image patch |
| $E$ | patch embedding matrix |
| $E_{pos}$ | positional embedding |
| $N$ | patch token 수 |
| $Z_0$ | Transformer 입력 token sequence |

### 보안적 의미

이미지를 patch token으로 처리하면 patch 단위 corruption, patch masking, adversarial patch, attention hijacking이 별도 공격면이 된다. CNN의 pixel-local filter 취약성과 ViT의 token-attention 취약성은 같은 방식으로 평가할 수 없다.

---

### 3.2 Multi-Head Self-Attention

ViT는 patch token 간 관계를 self-attention으로 계산한다.

$$
Attention(Q,K,V)=\operatorname{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V
$$

$$
MSA(Z)=\operatorname{Concat}(head_1,\ldots,head_h)W^O
$$

| 기호 | 의미 |
|---|---|
| $Q,K,V$ | query, key, value 행렬 |
| $d_k$ | key 차원 |
| $head_i$ | $i$번째 attention head |
| $W^O$ | output projection |

### 보안적 의미

Attention은 장거리 의존성을 학습할 수 있지만, 특정 patch token 또는 position embedding이 전체 출력을 크게 바꿀 수 있다. 따라서 attention stability, patch robustness, token attribution을 보안 평가에 포함할 수 있다.

---

### 3.3 Robust Drop

구조별 취약성을 비교하려면 정상 성능과 교란 조건 성능의 차이를 본다.

$$
RobustDrop = CleanAcc - RobustAcc
$$

| 기호 | 의미 |
|---|---|
| $CleanAcc$ | 정상 입력 정확도 |
| $RobustAcc$ | 교란 또는 공격 조건 정확도 |
| $RobustDrop$ | 공격 조건에서의 성능 저하 |

### 보안적 의미

CNN과 ViT가 같은 clean accuracy를 보이더라도 robust drop이 다르면 보안성은 다르다. 모델 구조별 취약성은 별도 평가해야 한다.

---

## 4. AI 원리 관점 분석

| 항목 | 분석 |
|---|---|
| Patch Tokenization | 이미지를 patch sequence로 바꾸어 Transformer 입력으로 사용한다. |
| Positional Encoding | patch의 공간 위치 정보를 token에 더한다. |
| Self-Attention | 전역 patch 관계를 직접 모델링한다. |
| Inductive Bias | CNN보다 지역성 가정이 약하고 데이터 규모와 pretraining에 더 민감할 수 있다. |
| Pretraining/Fine-tuning | 대규모 데이터에서 표현을 학습한 뒤 task별로 조정한다. |
| Task Extension | classification, detection, segmentation, video, 3D, generation으로 확장된다. |
| Efficiency | attention complexity와 patch resolution이 비용에 영향을 준다. |

---

## 5. 보안 이슈 관점 분석

| 보안 항목 | Vision Transformer 관점 해석 |
|---|---|
| 무결성 | patch token 조작이나 attention 교란이 예측을 바꿀 수 있다. |
| 가용성 | 고해상도 입력과 attention 비용이 운영 지연을 만들 수 있다. |
| 안전성 | detection/segmentation 실패는 자율주행·의료·로봇 안전과 연결된다. |
| 데이터 공급망 | pretraining dataset과 fine-tuning data 오염이 취약점으로 이어질 수 있다. |
| 책임성 | 모델 구조, pretraining source, patch size, fine-tuning 설정을 기록해야 한다. |

---

## 6. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 대상 | image patch, position embedding, attention map, class token, pretrained weights |
| 공격자 목표 | 오분류, detection/segmentation 실패, attention 왜곡, patch-level evasion |
| 공격자 능력 | patch 교란, masking, image corruption, pretraining/fine-tuning data 오염 |
| 공격 경로 | image → patch embedding → attention layers → task head → output |
| 제외 범위 | 실제 서비스 공격, 무단 pretraining data 조작, 악성 모델 배포 |

---

## 7. 평가방법 및 지표

| 지표 | 의미 | W03/P04에서의 활용 |
|---|---|---|
| Clean Accuracy | 정상 이미지 정확도 | 기본 성능 |
| Robust Accuracy | 교란 이미지 정확도 | 공격 조건 성능 |
| Robust Drop | clean과 robust 차이 | 구조별 취약성 비교 |
| Patch Corruption Robustness | patch masking/noise 조건 성능 | ViT 특화 평가 |
| Attention Stability | 입력 변화에 따른 attention 변화 | 설명·안정성 평가 |
| Transferability | CNN↔ViT 공격 이전성 | 모델 구조별 위험 비교 |
| Compute Cost | attention 연산 비용 | 운영 가능성 평가 |

---

## 8. 재현성 점검

| 항목 | 점검 |
|---|---|
| 데이터셋 | CIFAR-10, ImageNet subset, toy patch dataset 가능 |
| 모델 | CNN baseline과 ViT 또는 tiny ViT 비교 가능 |
| 전처리 | image size, patch size, augmentation, normalization 기록 필요 |
| 학습 | pretraining 여부, fine-tuning setting, seed 기록 필요 |
| 교란 조건 | patch corruption, noise, masking 등 안전한 toy 설정만 사용 |
| 결과 파일 | clean/robust accuracy, robust drop, attention map, config 저장 |
| 재현 가능성 판단 | 소형 ViT 실험은 가능. 대규모 pretraining 재현은 비용이 큼 |

---

## 9. 논문의 고유 기여

1. Vision Transformer 계열 모델을 task와 구조 관점에서 체계화했다.
2. CNN과 ViT의 inductive bias 차이를 설명하는 주요 참고문헌이다.
3. Patch/token/attention 구조가 비전 보안 평가의 새로운 분석 단위가 될 수 있음을 시사한다.
4. W03에서 CNN 기반 평가와 ViT 기반 평가를 구분해야 하는 근거를 제공한다.

---

## 10. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 보안 직접성 부족 | ViT 구조 survey이며 adversarial robustness가 중심은 아니다. | P05 robustness/safety survey와 결합한다. |
| 대규모 재현 비용 | ViT 성능은 pretraining 규모에 영향을 크게 받는다. | toy patch/소형 모델 실험으로 제한한다. |
| 최신 모델 추가 필요 | 최신 foundation vision model과 multimodal LLM은 후속 문헌 필요 | P03 및 W07/W08과 연결한다. |
| 지표 복잡성 | task별 ViT 성능 지표가 다르다. | clean/robust/task별 metric matrix를 작성한다. |

---

## 11. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 2장 관련연구 | ViT 구조, patch embedding, attention, CNN과의 차이 |
| 3장 위협모형 | patch/token/attention/pretraining data 공격면 정의 |
| 4장 연구방법 | patch corruption robustness, robust drop, attention stability 지표 설계 |
| 5장 분석 | CNN과 ViT 취약성 비교표 |
| 6장 보안적 함의 | 구조별 공격면과 운영 비용 해석 |

---

## 12. 기말논문 연결 3문장

1. 이 주차에서 기말논문에 반영할 개념: Vision Transformer는 이미지를 patch token과 attention으로 처리하므로 CNN과 다른 공격면과 평가 지표가 필요하다.
2. 이 주차에서 기말논문에 반영할 표·그림·실험: patch embedding 수식, CNN-ViT 구조 비교표, clean/robust/patch corruption 지표표를 반영한다.
3. 이 주차가 RAG 문서 오염/LLM 보안 감사 프레임워크와 연결되는 지점: ViT의 token-attention 구조는 LLM/RAG의 token-context 처리와 유사하게 입력 token 오염과 attention 왜곡을 감사해야 한다는 논리로 확장된다.

---

## 13. 최종 판단

이 논문은 W03에서 CNN 이후의 비전 Transformer 구조를 설명하는 핵심 문헌이다. 직접적인 공격 평가 근거는 P05가 제공하지만, P04는 patch/token/attention 기반 위협모형을 구성하는 데 필수적이다.

---

## 14. 변환 호환성 메모

```bash
pandoc P04_summary.md -o P04_summary.docx
pandoc P04_summary.md -o P04_summary.pdf --pdf-engine=xelatex
```
