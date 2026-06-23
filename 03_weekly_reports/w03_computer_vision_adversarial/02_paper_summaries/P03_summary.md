# P03 Summary

## Multimodal Learning With Transformers: A Survey — Peng Xu, Xiatian Zhu, David A. Clifton, IEEE TPAMI, 2023

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W03 컴퓨터비전 표현학습 & 비전 대적공격 |
| 논문명 | Multimodal Learning With Transformers: A Survey |
| 저자 | Peng Xu, Xiatian Zhu, David A. Clifton |
| 학술지 | IEEE Transactions on Pattern Analysis and Machine Intelligence |
| 권호/쪽 | Vol. 45, No. 10, pp. 12113–12132 |
| 연도 | 2023 |
| DOI | https://doi.org/10.1109/TPAMI.2023.3275156 |
| 논문 유형 | Survey / Multimodal Transformer Review |
| 로컬 PDF | `01_papers/pdf/03_Xu_et_al_2023_Multimodal_Learning_Transformers_Survey.pdf` |
| 강의계획서 지정 논문과 일치 여부 | 일치. 강의계획서의 `Y. Xu et al.` 축약 표기는 실제 제1저자 `Peng Xu`와 대응 |
| 핵심 근거 사용 가능 여부 | 가능 |
| 검증 메모 | W03 `paper_list.md` 기준 Crossref/IEEE URL 및 로컬 PDF 제목 일치 확인 |

---

## 1. 한 문장 요약

이 논문은 Transformer 기반 멀티모달 학습을 **modality-specific tokenization, self-attention, cross-modal fusion, alignment, multimodal pretraining, missing/noisy modality, application taxonomy** 관점에서 정리하고, 이미지·텍스트·비디오·오디오·3D 입력이 결합될 때 보안 공격면과 평가 지표가 확장됨을 보여주는 survey 논문이다.

---

## 2. 연구문제

> 이미지, 텍스트, 비디오, 오디오, 3D/point cloud 등 서로 다른 modality를 Transformer 구조 안에서 어떻게 표현·정렬·융합하며, 이 구조가 멀티모달 AI 보안 평가에 어떤 새로운 공격면을 만드는가?

| 번호 | 연구질문 |
|---|---|
| RQ1 | Transformer는 서로 다른 modality를 token sequence로 어떻게 통합하는가? |
| RQ2 | Self-attention과 cross-attention은 modality 간 관계를 어떻게 모델링하는가? |
| RQ3 | Multimodal pretraining과 alignment는 image-text retrieval, VQA, grounding에 어떤 역할을 하는가? |
| RQ4 | Missing modality, noisy modality, modality mismatch는 보안 실패 조건으로 어떻게 해석되는가? |
| RQ5 | 멀티모달 시스템에서 이미지 교란, 텍스트 조작, retrieval 오염, prompt injection은 어떻게 결합될 수 있는가? |

---

## 3. 핵심 이론 및 수식

### 3.1 Scaled Dot-Product Attention

Transformer의 핵심 연산은 query, key, value 간의 attention이다.

$$
Attention(Q,K,V)=\operatorname{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V
$$

| 기호 | 의미 |
|---|---|
| $Q$ | query 행렬 |
| $K$ | key 행렬 |
| $V$ | value 행렬 |
| $d_k$ | key vector 차원 |

### 보안적 의미

Attention은 서로 다른 modality의 token 간 관계를 학습할 수 있게 하지만, 잘못된 modality token이나 오염된 문서·이미지 token도 출력에 영향을 줄 수 있다. 따라서 멀티모달 보안에서는 입력 하나만 보는 것이 아니라 modality 간 정렬과 융합 과정을 점검해야 한다.

---

### 3.2 Cross-Modal Fusion

이미지 token $H_I$와 텍스트 token $H_T$의 cross-modal attention은 다음처럼 표현할 수 있다.

$$
H_{I \leftarrow T}=\operatorname{softmax}\left(\frac{Q_IK_T^T}{\sqrt{d_k}}\right)V_T
$$

| 기호 | 의미 |
|---|---|
| $H_I$ | 이미지 modality 표현 |
| $H_T$ | 텍스트 modality 표현 |
| $Q_I$ | 이미지 query |
| $K_T,V_T$ | 텍스트 key/value |
| $H_{I \leftarrow T}$ | 텍스트 정보를 반영한 이미지 표현 |

### 보안적 의미

텍스트 prompt나 caption이 오염되면 이미지 이해 결과가 바뀔 수 있고, 반대로 이미지 patch가 텍스트 응답을 왜곡할 수 있다. 이는 멀티모달 LLM과 RAG에서 prompt-image injection, caption poisoning, retrieval contamination으로 확장된다.

---

### 3.3 Alignment Loss

멀티모달 표현학습은 서로 대응하는 modality 표현을 가깝게 만들고, 대응하지 않는 표현은 멀게 만드는 목표를 사용할 수 있다.

$$
\mathcal{L}_{align}=-\log\frac{\exp(sim(h_I,h_T)/\tau)}{\sum_{j}\exp(sim(h_I,h_{T_j})/\tau)}
$$

| 기호 | 의미 |
|---|---|
| $h_I$ | 이미지 표현 |
| $h_T$ | 대응 텍스트 표현 |
| $sim(\cdot)$ | 유사도 함수 |
| $\tau$ | temperature |

### 보안적 의미

Alignment가 오염되면 image-text retrieval, captioning, VQA, grounding이 잘못된 연결을 만들 수 있다. 따라서 멀티모달 보안은 classification accuracy만으로 평가할 수 없다.

---

## 4. AI 원리 관점 분석

| 항목 | 분석 |
|---|---|
| Tokenization | 이미지, 텍스트, 오디오, 비디오, 3D 입력을 token sequence로 변환한다. |
| Self-Attention | 같은 modality 또는 통합 token 간 관계를 학습한다. |
| Cross-Attention | 서로 다른 modality 간 참조와 융합을 수행한다. |
| Multimodal Pretraining | 대규모 modality pair를 이용해 공통 표현공간을 학습한다. |
| Fusion | early, middle, late fusion 구조에 따라 보안 실패 위치가 달라진다. |
| Alignment | modality 간 의미 대응이 모델 성능과 취약성의 핵심이 된다. |
| Missing/Noisy Modality | 입력 누락·노이즈·불일치가 모델 신뢰성을 낮출 수 있다. |

---

## 5. 보안 이슈 관점 분석

| 보안 항목 | 멀티모달 Transformer 관점 해석 |
|---|---|
| 무결성 | 한 modality의 조작이 다른 modality 기반 판단까지 왜곡할 수 있다. |
| 기밀성 | 이미지, 음성, 텍스트, 위치 정보가 결합되면 개인정보 위험이 커진다. |
| 가용성 | modality 누락이나 noise가 서비스 실패로 이어질 수 있다. |
| 프롬프트 보안 | 텍스트 prompt가 이미지·비디오 해석을 조작할 수 있다. |
| RAG/검색 보안 | 검색된 이미지·문서·caption이 오염되면 생성 결과가 왜곡된다. |
| 책임성 | modality별 입력, alignment 근거, retrieval source를 기록해야 한다. |

---

## 6. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 대상 | 이미지, 텍스트, 오디오, 비디오, 3D point, caption, embedding, retrieval result |
| 공격자 목표 | cross-modal mismatch, 잘못된 grounding, retrieval 왜곡, 생성 응답 조작 |
| 공격자 능력 | 이미지 patch, caption 조작, prompt 삽입, modality 누락, retrieval 문서 오염 |
| 공격 경로 | modality 입력 → tokenization → attention/fusion → alignment → task output |
| 제외 범위 | 실제 멀티모달 서비스 무단 공격, 개인정보 데이터 수집, 악성 prompt 유포 |

---

## 7. 평가방법 및 지표

| 지표 | 의미 | W03/P03에서의 활용 |
|---|---|---|
| Retrieval Recall | 올바른 cross-modal pair 검색 성능 | image-text 정합 평가 |
| Grounding Accuracy | 텍스트가 가리키는 시각 영역을 맞히는 정도 | 시각-언어 alignment 평가 |
| VQA Accuracy | 이미지 기반 질의응답 정확도 | 멀티모달 추론 평가 |
| Robust Accuracy | modality 교란 조건 성능 | 보안성 평가 |
| Modality Drop Performance | 특정 modality 누락 시 성능 | 가용성/견고성 평가 |
| Alignment Consistency | modality 간 의미 일관성 | 오염·불일치 탐지 |
| Source Traceability | 검색·입력 출처 기록 여부 | 감사 가능성 |

---

## 8. 재현성 점검

| 항목 | 점검 |
|---|---|
| 데이터셋 | image-text retrieval, VQA, captioning 공개 데이터셋 사용 가능 |
| 모델 | CLIP류, multimodal transformer, toy image-text embedding 가능 |
| 입력 관리 | modality별 원본, 전처리, tokenization, prompt/caption 기록 필요 |
| 평가 | retrieval recall, VQA accuracy, grounding, robust metric 분리 필요 |
| 오염 조건 | caption noise, image perturbation, missing modality 등 안전한 toy 설정만 사용 |
| 재현 가능성 판단 | toy image-text 실험은 가능. 대규모 multimodal pretraining 재현은 비용이 큼 |

---

## 9. 논문의 고유 기여

1. Transformer 기반 멀티모달 학습을 modality, fusion, alignment, pretraining 관점에서 체계화했다.
2. 이미지 중심 W03를 텍스트·비디오·오디오·3D 입력까지 확장하는 이론적 기반을 제공한다.
3. Cross-modal alignment와 fusion이 보안 평가의 별도 공격면이 될 수 있음을 시사한다.
4. W07/W08의 멀티모달 LLM, RAG, prompt injection 보안으로 연결되는 bridge 문헌이다.

---

## 10. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 보안 직접성 부족 | 공격·방어 전문 survey는 아니므로 adversarial metric은 별도 설계가 필요하다. | P05 및 W08 프롬프트 인젝션 문헌과 결합한다. |
| 대규모 재현 비용 | Multimodal pretraining 재현은 데이터와 GPU 비용이 크다. | toy image-text retrieval 평가로 제한한다. |
| LLM 최신성 | 멀티모달 LLM의 최신 공격면은 후속 문헌 보강 필요 | W07/W08 summary와 연결한다. |
| 지표 복잡성 | task별 지표가 달라 단일 점수로 요약하기 어렵다. | modality-task-metric 매트릭스를 작성한다. |

---

## 11. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 2장 관련연구 | 멀티모달 Transformer, fusion, alignment 정리 |
| 3장 위협모형 | modality별 보호 자산과 공격 경로 정의 |
| 4장 연구방법 | retrieval, grounding, robust metric 설계 |
| 6장 보안적 함의 | 멀티모달 개인정보·무결성·감사 가능성 해석 |

---

## 12. 기말논문 연결 3문장

1. 이 주차에서 기말논문에 반영할 개념: 멀티모달 Transformer는 서로 다른 입력 modality를 token과 attention으로 결합하므로 공격면도 modality 간 정렬과 융합 단계까지 확장된다.
2. 이 주차에서 기말논문에 반영할 표·그림·실험: modality별 보호 자산, cross-modal attention 수식, retrieval/grounding/robustness 지표 비교표를 반영한다.
3. 이 주차가 RAG 문서 오염/LLM 보안 감사 프레임워크와 연결되는 지점: 멀티모달 RAG에서는 이미지·문서·caption·embedding이 모두 검색·생성 컨텍스트가 되므로 P03의 alignment 평가를 W08의 문서 오염 평가로 확장한다.

---

## 13. 최종 판단

이 논문은 W03에서 단일 이미지 분류를 멀티모달 AI 보안으로 확장하는 bridge 문헌이다. 직접적인 대적공격 평가는 P05가 담당하고, P03은 modality alignment와 fusion 보안 평가의 이론적 배경으로 사용한다.

---

## 14. 변환 호환성 메모

```bash
pandoc P03_summary.md -o P03_summary.docx
pandoc P03_summary.md -o P03_summary.pdf --pdf-engine=xelatex
```
