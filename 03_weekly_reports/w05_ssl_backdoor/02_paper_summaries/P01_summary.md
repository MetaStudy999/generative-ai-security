# P01 Summary

## A Survey on Self-Supervised Learning: Algorithms, Applications, and Future Trends — Jie Gui et al., IEEE TPAMI, 2024

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W05 자기지도학습·파운데이션 모델 & Poisoning/Backdoor |
| 논문명 | A Survey on Self-Supervised Learning: Algorithms, Applications, and Future Trends |
| 저자 | Jie Gui, Tuo Chen, Jing Zhang, Qiong Cao, Zhenan Sun, Hao Luo, Dacheng Tao |
| 학술지 | IEEE Transactions on Pattern Analysis and Machine Intelligence |
| 권호/쪽 | Vol. 46, No. 12, pp. 9052–9071 |
| 연도 | 2024 |
| DOI | https://doi.org/10.1109/TPAMI.2024.3415112 |
| 보조 URL | https://arxiv.org/abs/2301.05712 |
| 논문 유형 | Survey / Self-Supervised Learning Review |
| 로컬 PDF | `01_papers/pdf/01_Gui_et_al_2024_Self_Supervised_Learning_Survey.pdf` |
| 강의계획서 지정 논문과 일치 여부 | 제목·주제는 일치. 강의계획서의 `Yan Gui` 표기는 출판사 기준 `Jie Gui`와 달라 확인 필요 |
| 핵심 근거 사용 가능 여부 | 가능 |
| 검증 메모 | W05 `paper_list.md` 기준 TPAMI DOI와 arXiv DOI 확인. 로컬 PDF는 arXiv판일 수 있으므로 최종 페이지·그림 번호는 원문 대조 필요 |

---

## 1. 한 문장 요약

이 논문은 라벨 없이 표현을 학습하는 자기지도학습을 **contrastive learning, generative/masked modeling, predictive learning, clustering, multimodal SSL, downstream transfer** 관점에서 체계화하고, W05에서 pretraining representation이 보안 자산이자 poisoning/backdoor 공격면이 될 수 있음을 설명하는 핵심 배경 survey 논문이다.

---

## 2. 연구문제

> 라벨 없이 생성한 pretext task와 augmentation이 어떻게 유용한 representation을 만들며, 그 representation이 downstream task와 foundation model 보안성에 어떤 영향을 주는가?

| 번호 | 연구질문 |
|---|---|
| RQ1 | SSL은 contrastive, generative, predictive 계열로 어떻게 분류되는가? |
| RQ2 | Positive/negative pair, augmentation, masking, context prediction은 representation 학습에 어떤 역할을 하는가? |
| RQ3 | SSL pretraining representation은 downstream transfer에서 어떤 방식으로 평가되는가? |
| RQ4 | 라벨이 없는 pretraining 단계에서도 poisoning/backdoor 공격면이 생기는 이유는 무엇인가? |
| RQ5 | 기말논문에서 SSL 기반 모델을 clean transfer performance와 attack-condition performance로 어떻게 분리 평가할 수 있는가? |

---

## 3. 핵심 이론 및 수식

### 3.1 InfoNCE 대조학습 손실

Contrastive SSL은 anchor 표현 $z$와 positive 표현 $z^+$를 가깝게, negative 표현 $z_j^-$를 멀게 학습한다.

$$
\mathcal{L}_{InfoNCE}
=-\log\frac{\exp(sim(z,z^+)/\tau)}
{\exp(sim(z,z^+)/\tau)+\sum_{j=1}^{K}\exp(sim(z,z_j^-)/\tau)}
$$

| 기호 | 의미 |
|---|---|
| $z$ | anchor 표현 |
| $z^+$ | 같은 샘플 또는 관련 샘플에서 나온 positive 표현 |
| $z_j^-$ | negative 표현 |
| $sim(\cdot)$ | 유사도 함수 |
| $\tau$ | temperature |

### 보안적 의미

공격자가 augmentation, positive pair, negative sampling, pretraining corpus를 조작하면 representation space가 왜곡될 수 있다. 라벨이 없어도 self-supervised objective 자체가 공격면이 된다.

---

### 3.2 Masked Reconstruction Objective

Generative SSL은 입력 일부를 가리고 원래 값을 복원하도록 학습할 수 있다.

$$
\mathcal{L}_{mask}=\sum_{i\in\mathcal{M}}\ell(\hat{x}_i,x_i)
$$

| 기호 | 의미 |
|---|---|
| $\mathcal{M}$ | mask 위치 집합 |
| $x_i$ | 원래 입력 조각 |
| $\hat{x}_i$ | 모델이 복원한 값 |
| $\ell$ | 복원 손실 |

### 보안적 의미

Masked reconstruction은 corpus의 통계적 패턴을 모델에 저장한다. 민감정보, 편향, 악성 패턴, trigger가 pretraining corpus에 포함되면 downstream behavior에 영향을 줄 수 있다.

---

### 3.3 Linear Probe와 Transfer 성능

SSL 표현은 보통 representation을 고정하고 간단한 classifier를 붙여 평가한다.

$$
\hat{y}=g_{\phi}(h_{\theta}(x))
$$

| 기호 | 의미 |
|---|---|
| $h_{\theta}$ | self-supervised encoder |
| $g_{\phi}$ | downstream linear probe 또는 classifier |
| $\hat{y}$ | downstream 예측 |

### 보안적 의미

Clean transfer accuracy가 높더라도 특정 trigger, 특정 domain shift, 특정 class에서 ASR이 높으면 representation이 보안적으로 취약할 수 있다.

---

## 4. AI 원리 관점 분석

| 항목 | 분석 |
|---|---|
| Contrastive Learning | positive/negative pair를 이용해 표현공간을 구성한다. |
| Generative SSL | masking, reconstruction, denoising으로 입력 구조를 학습한다. |
| Predictive SSL | context나 future token/frame을 예측한다. |
| Augmentation | 같은 의미를 유지하는 변환을 positive signal로 사용한다. |
| Transfer Learning | pretraining representation을 downstream task에 전이한다. |
| Foundation Model | 대규모 self-supervised pretraining은 foundation model의 핵심 기반이다. |

---

## 5. 보안 이슈 관점 분석

| 보안 항목 | SSL 관점 해석 |
|---|---|
| 데이터 무결성 | pretraining corpus와 augmentation pipeline이 오염되면 representation이 왜곡된다. |
| 모델 무결성 | downstream classifier가 정상이어도 encoder representation이 backdoor를 포함할 수 있다. |
| 기밀성 | self-supervised corpus가 민감정보를 포함하면 memorization/leakage 위험이 있다. |
| 가용성 | 오염 representation은 downstream 성능 저하를 만들 수 있다. |
| 책임성 | pretraining data, augmentation, seed, checkpoint 출처 기록이 필요하다. |

---

## 6. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 대상 | pretraining corpus, augmentation rule, positive/negative pairs, encoder, checkpoint, downstream task |
| 공격자 목표 | representation shift, downstream 성능 저하, trigger 조건 target behavior 유도 |
| 공격자 능력 | corpus 오염, augmentation 조작, false positive/negative pair 삽입, checkpoint 공급망 조작 |
| 공격 경로 | corpus/augmentation → SSL objective → encoder representation → downstream model |
| 제외 범위 | 실제 대규모 corpus 오염, 무단 모델 공격, 개인정보 포함 데이터 사용 |

---

## 7. 평가방법 및 지표

| 지표 | 의미 | W05/P01에서의 활용 |
|---|---|---|
| Linear Probe Accuracy | encoder 표현의 downstream 분류 성능 | clean transfer 평가 |
| Fine-tuning Accuracy | end-to-end downstream 성능 | 실사용 성능 |
| Retrieval Recall | 표현공간 검색 성능 | representation quality |
| Representation Distance | clean/poisoned 표현 차이 | poisoning 영향 평가 |
| ASR | trigger 조건 공격 성공률 | backdoor 평가 |
| Transfer Robustness | 다른 downstream task로 전이된 안정성 | foundation model 위험 평가 |
| Data Lineage | pretraining data 출처 기록 | 감사 가능성 |

---

## 8. 재현성 점검

| 항목 | 점검 |
|---|---|
| 데이터 | 공개 image/text/video toy corpus 사용 가능 |
| SSL objective | contrastive, masked reconstruction, predictive task 중 하나 선택 |
| Augmentation | crop, mask, noise, temporal sampling 등 명시 |
| 모델 | encoder architecture, projection head, downstream classifier 기록 |
| 평가 | linear probe, clean accuracy, ASR, representation shift 분리 |
| 한계 | 소규모 toy SSL 결과를 foundation model 보안성으로 일반화하지 않음 |

---

## 9. 논문의 고유 기여

1. SSL 알고리즘과 응용을 폭넓은 taxonomy로 정리한다.
2. Contrastive/generative/predictive SSL의 공통 원리와 차이를 설명한다.
3. Pretraining representation과 downstream transfer 평가의 기본 구조를 제공한다.
4. W05에서 self-supervised pretraining 단계의 데이터 오염·backdoor 위험을 설명하는 배경 근거가 된다.

---

## 10. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 보안 직접성 부족 | poisoning/backdoor를 중심으로 다루는 논문은 아니다. | P04/P05와 결합한다. |
| 대규모 재현 비용 | foundation-scale SSL 재현은 비용이 크다. | toy encoder/linear probe로 제한한다. |
| 저자명 검증 | 강의계획서의 `Yan Gui` 표기와 출판사 기준 `Jie Gui`가 다르다. | paper_list에 검증 메모 유지 |
| 원문 수치 전사 제한 | survey 수치를 임의 전사하지 않는다. | 평가 프레임 중심으로 사용한다. |

---

## 11. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | foundation model과 SSL pretraining의 보안 중요성 제시 |
| 2장 관련연구 | SSL taxonomy, contrastive/generative/predictive learning 정리 |
| 3장 위협모형 | corpus, augmentation, encoder, downstream transfer 공격면 정의 |
| 4장 연구방법 | linear probe, ASR, representation shift 평가 설계 |
| 6장 보안적 함의 | 데이터 무결성, 모델 공급망, 책임성 해석 |

---

## 12. 기말논문 연결 3문장

1. 이 주차에서 기말논문에 반영할 개념: SSL은 라벨 없이 representation을 학습하지만, pretraining corpus와 augmentation이 오염되면 downstream 모델 전체의 보안성이 흔들릴 수 있다.
2. 이 주차에서 기말논문에 반영할 표·그림·실험: InfoNCE 수식, masked reconstruction 수식, SSL pipeline 도식, clean transfer-ASR 비교표를 반영한다.
3. 이 주차가 RAG 문서 오염/LLM 보안 감사 프레임워크와 연결되는 지점: RAG embedding과 LLM pretraining/fine-tuning도 self-supervised representation에 의존하므로 P01의 corpus/augmentation/representation 평가축을 W08/W14로 확장한다.

---

## 13. 최종 판단

P01은 W05의 AI 원리 핵심 문헌이다. 직접 보안 문헌은 아니지만 SSL pretraining representation이 왜 보안 자산이 되는지를 설명하는 이론적 출발점으로 사용한다.

---

## 14. 변환 호환성 메모

```bash
pandoc P01_summary.md -o P01_summary.docx
pandoc P01_summary.md -o P01_summary.pdf --pdf-engine=xelatex
```
