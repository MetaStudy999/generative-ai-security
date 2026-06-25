# P03 Summary

## Multimodal Learning With Transformers: A Survey — Peng Xu, Xiatian Zhu, David A. Clifton, IEEE TPAMI, 2023

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W03 컴퓨터비전 표현학습 & 비전 대적공격 |
| 논문명 | Multimodal Learning With Transformers: A Survey |
| 저자 | Peng Xu, Xiatian Zhu, David A. Clifton |
| 공식 출판 정보 | IEEE Transactions on Pattern Analysis and Machine Intelligence, Vol. 45, No. 10, pp. 12113–12132, 2023 |
| DOI | https://doi.org/10.1109/TPAMI.2023.3275156 |
| 논문 유형 | Survey / Multimodal Transformer Review |
| 로컬 PDF | `01_papers/pdf/03_Xu_et_al_2023_Multimodal_Learning_Transformers_Survey.pdf` |
| 검증 상태 | W03 `paper_list.md` 기준 공식 DOI와 IEEE TPAMI 출판정보 확인. 강의계획서의 `Y. Xu et al.` 축약 표기는 실제 제1저자 `Peng Xu`와 대응 |
| PDF 확인 메모 | repo의 PDF 폴더에 P03 관련 PDF blob이 존재함을 확인했다. 요약은 로컬 PDF 경로와 W03 `paper_list.md`의 공식 DOI 메타데이터 기준으로 보완했다. |
| 수식 호환성 | GitHub 수식 렌더링 오류 방지를 위해 `\operatorname`을 사용하지 않고 `\mathrm{...}` 형태로 작성했다. |
| 핵심 근거 사용 가능 여부 | 가능. W03에서 multimodal transformer, modality tokenization, self-attention, cross-attention, cross-modal fusion, alignment, retrieval, VQA, grounding, 멀티모달 보안 공격면의 bridge 문헌으로 사용 |

---

## 1. 한 문장 요약

이 논문은 Transformer 기반 멀티모달 학습을 **modality-specific tokenization, self-attention, cross-attention, cross-modal fusion, multimodal pretraining, image-text alignment, contrastive learning, VQA, retrieval, grounding, captioning, missing/noisy modality, multimodal robustness** 관점에서 정리하며, W03에서는 컴퓨터비전 보안 논의를 이미지 단일 입력에서 **이미지·텍스트·오디오·비디오·3D point cloud가 결합된 멀티모달 공격면**으로 확장하는 핵심 bridge 문헌이다.

---

## 2. 핵심 연구문제

> 이미지, 텍스트, 비디오, 오디오, 3D point cloud 등 서로 다른 modality를 Transformer 구조 안에서 어떻게 표현·정렬·융합할 수 있는가? 그리고 이 구조는 멀티모달 AI 보안에서 어떤 새로운 실패 조건과 공격면을 만드는가?

| 번호 | 연구질문 |
|---|---|
| RQ1 | Transformer는 서로 다른 modality를 token sequence로 변환하고 통합하는가? |
| RQ2 | Self-attention과 cross-attention은 동일 modality 내부 관계와 modality 간 관계를 어떻게 모델링하는가? |
| RQ3 | Multimodal pretraining과 contrastive alignment는 image-text retrieval, captioning, VQA, grounding 성능에 어떤 역할을 하는가? |
| RQ4 | Missing modality, noisy modality, modality mismatch, retrieval contamination은 멀티모달 시스템의 보안 실패 조건으로 어떻게 해석되는가? |
| RQ5 | 이미지 patch, caption poisoning, prompt injection, retrieval 오염이 결합되면 멀티모달 LLM/RAG 시스템에서 어떤 복합 공격면이 생기는가? |

---

## 3. 논문의 핵심 기여

| 기여 | 설명 | W03 연결 |
|---|---|---|
| Multimodal Transformer taxonomy | modality, fusion strategy, pretraining objective, downstream task별로 transformer 기반 멀티모달 학습을 체계화 | W03 P03 핵심 |
| Attention 기반 fusion 설명 | self-attention, cross-attention, co-attention을 통해 modality 간 관계를 모델링 | image-text 보안 공격면 이해 |
| Alignment objective 정리 | contrastive learning과 image-text matching을 통해 공통 representation space를 학습 | retrieval/RAG 오염 위험 분석 |
| 응용 task 정리 | retrieval, VQA, captioning, grounding, multimodal classification 등 주요 task 분류 | task별 평가 지표 설계 |
| 보안 확장 가능성 | 논문 자체는 보안 전문 survey는 아니지만, modality mismatch와 noisy modality 문제를 멀티모달 보안 평가로 확장 가능 | W07/W08/W15 연결 |

---

## 4. 목차별 핵심 개괄

| 목차 | 핵심 내용 | 비전공자용 이해 |
|---|---|---|
| 1. Introduction | 멀티모달 학습은 여러 종류의 데이터를 함께 사용해 더 풍부한 표현을 학습한다. | 이미지와 텍스트를 같이 보면 더 잘 이해할 수 있다. |
| 2. Transformer Background | Attention을 이용해 token 간 관계를 학습하고 긴 의존성을 처리한다. | 어떤 정보가 중요한지 서로 참조하며 판단한다. |
| 3. Modality Representation | 이미지, 텍스트, 오디오, 비디오, 3D 데이터를 token 또는 embedding으로 변환한다. | 서로 다른 데이터를 같은 계산 구조에 넣기 위해 숫자 표현으로 바꾼다. |
| 4. Fusion Strategy | early, middle, late fusion과 cross-attention 구조를 비교한다. | 언제, 어디서, 어떻게 서로 다른 정보를 합칠지 결정한다. |
| 5. Pretraining Objectives | masked modeling, contrastive learning, image-text matching, alignment loss 등을 정리한다. | 이미지와 설명문이 서로 맞는지 학습한다. |
| 6. Downstream Tasks | VQA, captioning, retrieval, grounding, multimodal classification 등 응용을 정리한다. | 그림을 보고 질문에 답하거나, 설명에 맞는 이미지를 찾는 작업이다. |
| 7. Challenges | missing/noisy modality, modality imbalance, alignment error, computational cost, dataset bias가 문제다. | 한쪽 정보가 틀리거나 빠지면 전체 판단이 흔들릴 수 있다. |
| 8. Future Directions | 효율적 fusion, robust multimodal learning, trustworthy multimodal AI, domain adaptation이 과제로 남는다. | 멀티모달 AI도 안전하고 재현 가능하게 평가해야 한다. |

---

## 5. 핵심 이론 및 수식

> 수식은 GitHub Markdown/KaTeX 호환성을 우선한다. `\operatorname` 매크로는 사용하지 않고 `\mathrm{...}` 형태로 작성한다.

### 5.1 Scaled Dot-Product Attention

Transformer의 핵심 연산은 query, key, value 간 attention이다.

$$
Attention(Q,K,V)=\mathrm{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V
$$

| 기호 | 의미 |
|---|---|
| $Q$ | query 행렬 |
| $K$ | key 행렬 |
| $V$ | value 행렬 |
| $d_k$ | key vector 차원 |

### 보안적 의미

Attention은 서로 다른 modality token 간 관계를 학습할 수 있게 하지만, 오염된 이미지 token, caption token, retrieval token도 출력에 영향을 줄 수 있다. 따라서 멀티모달 보안에서는 입력 하나만 보지 않고 attention/fusion 경로를 함께 점검해야 한다.

---

### 5.2 Cross-Modal Fusion

이미지 token $H_I$와 텍스트 token $H_T$의 cross-modal attention은 다음처럼 표현할 수 있다.

$$
H_{I \leftarrow T}=\mathrm{softmax}\left(\frac{Q_IK_T^T}{\sqrt{d_k}}\right)V_T
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

### 5.3 Alignment Loss

멀티모달 표현학습은 대응하는 modality 표현을 가깝게 만들고, 대응하지 않는 표현은 멀게 만드는 목표를 사용할 수 있다.

$$
\mathcal{L}_{align}=-\log\frac{\exp(\mathrm{sim}(h_I,h_T)/\tau)}{\sum_j\exp(\mathrm{sim}(h_I,h_{T_j})/\tau)}
$$

| 기호 | 의미 |
|---|---|
| $h_I$ | 이미지 표현 |
| $h_T$ | 대응 텍스트 표현 |
| $\mathrm{sim}$ | 유사도 함수 |
| $\tau$ | temperature |

### 보안적 의미

Alignment가 오염되면 image-text retrieval, captioning, VQA, grounding이 잘못된 연결을 만들 수 있다. 따라서 멀티모달 보안은 classification accuracy만으로 평가할 수 없다.

---

### 5.4 Multimodal Robust Accuracy

정상 멀티모달 입력과 교란된 멀티모달 입력에서의 성능을 분리해 측정한다.

$$
Acc_{MM}^{clean}=\frac{N_{correct}(x_I,x_T)}{N_{total}}
$$

$$
Acc_{MM}^{robust}=\frac{N_{correct}(x_I^{adv},x_T^{adv})}{N_{total}}
$$

### 보안적 의미

이미지만 교란하거나 텍스트만 조작하는 조건과 둘 다 조작하는 조건을 분리해야 한다.

---

### 5.5 Alignment Consistency

서로 다른 modality 표현이 의미적으로 얼마나 일관적인지 측정한다.

$$
AlignConsistency=\frac{1}{N}\sum_{i=1}^{N}\mathrm{sim}(h_I^{(i)},h_T^{(i)})
$$

### 보안적 의미

Alignment consistency가 낮으면 이미지와 텍스트가 서로 다른 의미를 가리키거나, retrieval source가 오염되었을 수 있다.

---

### 5.6 Modality Drop Robustness

특정 modality가 누락되었을 때 성능이 얼마나 유지되는지 평가한다.

$$
DropRobustness=\frac{Perf(M_{available})}{Perf(M_{all})}
$$

| 기호 | 의미 |
|---|---|
| $M_{all}$ | 모든 modality가 있는 조건 |
| $M_{available}$ | 일부 modality가 누락된 조건 |

### 보안적 의미

현장에서는 이미지가 흐리거나, caption이 누락되거나, 음성이 손상될 수 있다. 가용성 관점에서 modality drop 조건을 평가해야 한다.

---

### 5.7 Multimodal Attack Surface Score

멀티모달 시스템의 공격면을 modality별 위험과 fusion 위험으로 분해한다.

$$
MMRisk=ImageRisk+TextRisk+AudioRisk+RetrievalRisk+FusionRisk-MonitoringCoverage
$$

### 보안적 의미

멀티모달 시스템은 단일 입력 모델보다 공격 경로가 많다. image patch, prompt injection, retrieval poisoning, caption manipulation을 함께 관리해야 한다.

---

## 6. AI 원리 70% 관점 분석

| 원리 항목 | 설명 | W03/P03에서의 의미 |
|---|---|---|
| Modality Tokenization | 이미지, 텍스트, 오디오, 비디오, 3D 입력을 token sequence로 변환 | 멀티모달 Transformer 입력 구성 |
| Self-Attention | 같은 modality 또는 통합 token 간 관계 학습 | context modeling |
| Cross-Attention | 서로 다른 modality 간 참조와 융합 수행 | image-text fusion |
| Multimodal Pretraining | 대규모 modality pair를 이용해 공통 표현공간 학습 | CLIP류 학습 원리 |
| Fusion Strategy | early/middle/late fusion에 따라 정보 결합 위치 결정 | 보안 실패 위치 분석 |
| Alignment | modality 간 의미 대응이 성능과 취약성의 핵심 | retrieval·grounding 평가 |
| Missing/Noisy Modality | 입력 누락·노이즈·불일치가 모델 신뢰성 저하 | 가용성·강건성 평가 |
| Downstream Task | VQA, captioning, retrieval, grounding | task별 지표 분리 필요 |

---

## 7. 보안 이슈 30% 관점 분석

| 보안 항목 | 멀티모달 Transformer 관점 해석 | 대표 평가 지표 |
|---|---|---|
| 기밀성 | 이미지, 음성, 텍스트, 위치정보가 결합되면 개인정보 재식별 위험 증가 | PII leakage, modality linkage risk |
| 무결성 | 한 modality 조작이 다른 modality 기반 판단까지 왜곡 | robust accuracy, ASR |
| 가용성 | modality 누락, noisy modality, sensor failure가 서비스 실패로 연결 | DropRobustness, task failure rate |
| 프롬프트 보안 | 텍스트 prompt가 이미지·비디오 해석을 조작 | prompt-image injection success |
| RAG/검색 보안 | 검색된 이미지·문서·caption 오염이 생성 결과 왜곡 | retrieval contamination rate |
| 책임성 | modality별 입력, alignment 근거, retrieval source를 기록해야 감사 가능 | source traceability |

---

## 8. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 대상 | 이미지, 텍스트, 오디오, 비디오, 3D point, caption, embedding, retrieval result, attention/fusion output, generated response |
| 공격자 목표 | cross-modal mismatch, 잘못된 grounding, retrieval 왜곡, 생성 응답 조작, 특정 modality 기반 우회 |
| 공격자 능력 | 이미지 patch, caption 조작, prompt 삽입, modality 누락 유발, retrieval 문서 오염, noisy sensor 입력 |
| 공격 경로 | modality 입력 → tokenization → self/cross-attention → fusion/alignment → downstream task output |
| 방어자 능력 | modality validation, source tracing, retrieval filtering, alignment check, robust training, human review, monitoring |
| 제외 범위 | 실제 멀티모달 서비스 무단 공격, 개인정보 데이터 수집, 악성 prompt 유포, 운영 시스템 침해 지원 |

---

## 9. 평가방법 및 지표

| 평가축 | 지표 | 의미 | W03/P03 활용 |
|---|---|---|---|
| Retrieval | Recall@K, MRR | 올바른 cross-modal pair 검색 성능 | image-text 정합 평가 |
| Grounding | grounding accuracy, IoU | 텍스트가 가리키는 시각 영역을 맞히는 정도 | 시각-언어 alignment |
| VQA | VQA accuracy | 이미지 기반 질의응답 정확도 | 멀티모달 추론 |
| Robustness | robust accuracy, ASR, RobustDrop | modality 교란 조건 성능 | 보안성 평가 |
| Modality Drop | DropRobustness | modality 누락 시 성능 | 가용성 평가 |
| Alignment | AlignConsistency | modality 간 의미 일관성 | 오염·불일치 탐지 |
| Traceability | source traceability | 검색·입력 출처 기록 여부 | 감사 가능성 |
| 재현성 | model/config/data/prompt log | 결과 재현 가능성 | W15 연결 |

---

## 10. 재현성 체크리스트

| 항목 | 기록해야 할 내용 |
|---|---|
| Bibliographic status | DOI, IEEE TPAMI 출판정보, 로컬 PDF 판본 상태 |
| Dataset | image-text retrieval, VQA, captioning, grounding dataset, split |
| Modality input | 이미지/텍스트/오디오/비디오 원본, caption, prompt, 전처리 |
| Tokenization | patch size, text tokenizer, frame sampling, embedding model |
| Model | multimodal transformer 구조, fusion 방식, checkpoint/hash |
| Pretraining/Evaluation | alignment objective, downstream task, metric, seed |
| Perturbation | image noise/patch, caption noise, missing modality, retrieval contamination |
| Output | retrieval result, VQA answer, grounding box, generated response |
| Evidence | source documents, prompt/caption log, config, script commit, raw output |
| 한계 | 대규모 pretraining 성능을 toy 실험으로 과장하지 않고, task별 지표를 분리 보고 |

---

## 11. 논문의 고유 기여

1. Transformer 기반 멀티모달 학습을 modality, fusion, alignment, pretraining, task taxonomy 관점에서 체계화했다.
2. 이미지 중심 W03를 텍스트·비디오·오디오·3D 입력까지 확장하는 이론적 기반을 제공한다.
3. Cross-modal alignment와 fusion이 보안 평가의 별도 공격면이 될 수 있음을 시사한다.
4. W07/W08의 멀티모달 LLM, RAG, prompt injection 보안으로 연결되는 bridge 문헌이다.
5. 최종 기말논문에서 modality-task-metric matrix와 multimodal threat model을 설계하는 근거가 된다.

---

## 12. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 보안 직접성 부족 | 공격·방어 전문 survey는 아니므로 adversarial metric은 별도 설계가 필요하다. | W03 P05 및 W08 prompt injection 문헌과 결합 |
| 대규모 재현 비용 | Multimodal pretraining 재현은 데이터와 GPU 비용이 크다. | toy image-text retrieval 평가로 제한 |
| LLM 최신성 | 멀티모달 LLM의 최신 공격면은 후속 문헌 보강 필요 | W07/W08/W15 summary와 연결 |
| 지표 복잡성 | task별 지표가 달라 단일 점수로 요약하기 어렵다. | modality-task-metric matrix 작성 |
| 데이터 오염 위험 | 공개 image-text pair의 caption과 retrieval source가 오염될 수 있다. | source traceability와 contamination check 추가 |
| 설명가능성 부족 | attention weight만으로 설명을 단정하기 어렵다. | W15 XAI 문헌과 함께 해석 |

---

## 13. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | AI 보안 평가가 단일 이미지 모델에서 멀티모달 입력·retrieval·prompt까지 확장된다는 문제의식 |
| 2장 관련연구 | P03을 multimodal transformer와 cross-modal alignment 핵심 survey로 정리 |
| 3장 위협모형 | 이미지, 텍스트, caption, retrieval source, attention/fusion output 보호 자산 정의 |
| 4장 연구방법 | attention, cross-modal fusion, alignment loss, robust accuracy, DropRobustness, MMRisk 지표 설계 |
| 5장 분석 | modality-task-metric matrix와 multimodal attack surface table 제시 |
| 6장 보안적 함의 | prompt-image injection, caption poisoning, retrieval contamination, modality mismatch 위험 해석 |
| 부록 | prompt/caption/source log, model config, perturbation 조건, raw output 수록 |

---

## 14. 기말논문 연결 3문장

1. W03에서 기말논문에 반영할 개념: 멀티모달 Transformer는 서로 다른 입력 modality를 attention과 alignment로 결합하지만, 이 결합 과정이 새로운 공격면이 된다.
2. W03에서 기말논문에 반영할 표·그림·실험: scaled dot-product attention, cross-modal fusion, alignment loss, multimodal robust accuracy, DropRobustness, MMRisk 수식표와 modality-task-metric matrix를 반영한다.
3. W03이 W15 최종 제출과 연결되는 지점: 멀티모달 평가 결과는 modality별 입력, prompt/caption, retrieval source, model config, raw output, alignment metric을 evidence chain으로 남겨야 재현성과 신뢰성을 확보할 수 있다.

---

## 15. 최종 판단

P03은 W03의 멀티모달 확장 핵심 문헌이다. 이 논문은 컴퓨터비전 보안을 단일 이미지 분류 문제에서 image-text retrieval, VQA, grounding, captioning, multimodal LLM/RAG 보안으로 확장하는 bridge 역할을 한다. 따라서 기말논문에서는 P03을 **multimodal transformer, cross-modal fusion, alignment, retrieval contamination, prompt-image injection, modality-task-metric 설계의 근거 문헌**으로 사용하는 것이 적절하다.

---

## 16. GitHub 수식 호환성 메모

이 파일에서는 GitHub 수식 렌더링 오류 방지를 위해 `\operatorname`을 사용하지 않는다.

| 피해야 할 표현 | 권장 표현 |
|---|---|
| `\operatorname{softmax}` | `\mathrm{softmax}` |
| `\operatorname{sim}` | `\mathrm{sim}` |
| `\operatorname{argmax}` | `\mathrm{argmax}` 또는 `\arg\max` |

```bash
pandoc P03_summary.md -o P03_summary.docx
pandoc P03_summary.md -o P03_summary.pdf --pdf-engine=xelatex
```
