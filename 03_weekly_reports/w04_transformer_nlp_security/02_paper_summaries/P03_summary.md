# P03 Summary

## A Survey of Transformers — Tianyang Lin, Yuxin Wang, Xiangyang Liu, Xipeng Qiu, AI Open, 2022

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W04 Transformer 변형 & NLP 대적공격·프라이버시 |
| 논문명 | A survey of transformers |
| 저자 | Tianyang Lin, Yuxin Wang, Xiangyang Liu, Xipeng Qiu |
| 학술지 | AI Open |
| 권호/쪽 | Vol. 3, pp. 111–132 |
| 연도 | 2022 |
| DOI | https://doi.org/10.1016/j.aiopen.2022.10.001 |
| 공식 URL | https://www.sciencedirect.com/science/article/pii/S2666651022000146 |
| 논문 유형 | Survey / General Transformer Taxonomy Review |
| 로컬 PDF | `01_papers/pdf/03_Lin_et_al_2022_Survey_of_Transformers.pdf` |
| 강의계획서 지정 논문과 일치 여부 | 일치 |
| 핵심 근거 사용 가능 여부 | 가능 |
| 검증 메모 | W04 `paper_list.md` 기준 AI Open 출판 DOI/권호/쪽 확인 |

---

## 1. 한 문장 요약

이 논문은 Transformer의 기본 구조와 변형을 **self-attention, positional encoding, architectural modification, pre-training, NLP/CV/audio/multimodal applications** 관점에서 정리하고, W04의 NLP 보안 위협모형에서 입력·attention·출력·응용 단계별 공격면을 정의하는 기초 taxonomy를 제공하는 survey 논문이다.

---

## 2. 연구문제

> Vanilla Transformer 이후 다양한 구조와 응용은 어떤 taxonomy로 분류할 수 있으며, 이러한 구조적 차이는 NLP/멀티모달 보안에서 보호 자산과 공격면을 어떻게 바꾸는가?

| 번호 | 연구질문 |
|---|---|
| RQ1 | Transformer의 기본 구성요소는 무엇인가? |
| RQ2 | Attention, position encoding, depth, memory, architecture modification은 어떤 방향으로 발전했는가? |
| RQ3 | Pre-training과 downstream adaptation은 Transformer 응용에 어떤 역할을 하는가? |
| RQ4 | NLP, CV, audio, multimodal Transformer는 보안 위협모형에서 어떤 보호 자산을 갖는가? |
| RQ5 | 프롬프트 보안 평가에서 입력·모델·출력·로그·외부 도구 호출 단계를 어떻게 나눌 수 있는가? |

---

## 3. 핵심 이론 및 수식

### 3.1 Scaled Dot-Product Attention

Transformer의 핵심 연산은 token 간 관계를 attention weight로 계산하는 것이다.

$$
Attention(Q,K,V)=\operatorname{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V
$$

| 기호 | 의미 |
|---|---|
| $Q$ | query 행렬 |
| $K$ | key 행렬 |
| $V$ | value 행렬 |
| $d_k$ | scaling에 쓰이는 key 차원 |

### 보안적 의미

Attention은 모델이 입력의 어느 부분을 참조할지 결정한다. 악성 문장, 민감정보, 오염 문서, prompt injection 구문이 context 안에 포함되면 attention 경로를 통해 출력에 영향을 줄 수 있다.

---

### 3.2 Transformer Block

Transformer block은 attention과 feed-forward network를 잔차 연결과 정규화로 반복한다.

$$
H' = \operatorname{LayerNorm}(H + \operatorname{MHA}(H))
$$

$$
H^{out}=\operatorname{LayerNorm}(H' + \operatorname{FFN}(H'))
$$

| 기호 | 의미 |
|---|---|
| $H$ | 입력 hidden states |
| $\operatorname{MHA}$ | multi-head attention |
| $\operatorname{FFN}$ | feed-forward network |
| $H^{out}$ | block 출력 |

### 보안적 의미

입력 token의 교란은 여러 layer를 거치며 증폭되거나 완화될 수 있다. 따라서 NLP 공격은 입력 표면형뿐 아니라 내부 representation, layer별 attention, output confidence까지 평가해야 한다.

---

### 3.3 Pre-training / Fine-tuning Objective

언어모델의 기본 학습은 다음 token 또는 masked token을 예측하는 형태로 볼 수 있다.

$$
\mathcal{L}_{LM}=-\sum_{t=1}^{T}\log p_{\theta}(x_t \mid x_{<t})
$$

| 기호 | 의미 |
|---|---|
| $x_t$ | $t$번째 token |
| $x_{<t}$ | 이전 context |
| $p_{\theta}$ | 파라미터 $\theta$를 가진 언어모델 |

### 보안적 의미

Pretraining/fine-tuning data에 민감정보나 악성 패턴이 포함되면 모델 출력, memorization, prompt behavior, downstream task에 영향을 줄 수 있다.

---

## 4. AI 원리 관점 분석

| 항목 | 분석 |
|---|---|
| Vanilla Transformer | self-attention, positional encoding, FFN, residual connection으로 구성된다. |
| Architectural Modification | attention, position, depth, recurrence, memory 구조를 변경한다. |
| Pre-training | 대규모 corpus에서 일반 표현을 학습한다. |
| Fine-tuning | downstream task 또는 instruction에 맞게 모델을 조정한다. |
| Applications | NLP, CV, audio, multimodal tasks로 확장된다. |
| Taxonomy | 모델 구조별·응용별 차이를 위협모형 분리 기준으로 사용할 수 있다. |

---

## 5. 보안 이슈 관점 분석

| 보안 항목 | Transformer taxonomy 관점 해석 |
|---|---|
| 기밀성 | pretraining/fine-tuning data, prompt, 로그에 민감정보가 포함될 수 있다. |
| 무결성 | 입력 token, prompt, retrieved context가 출력 결정을 왜곡할 수 있다. |
| 가용성 | 긴 입력과 복잡한 모델은 latency와 비용 문제를 만든다. |
| 프라이버시 | context, ICL examples, output probability가 정보 누출 경로가 된다. |
| 책임성 | 모델 구조, 데이터, prompt, output, tool call log를 기록해야 한다. |

---

## 6. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 대상 | prompt, token sequence, attention context, model weights, output, log, external tool call |
| 공격자 목표 | 입력 의미 왜곡, 정책 우회, 민감정보 유출, 출력 조작 |
| 공격자 능력 | adversarial text, paraphrase, typo, prompt injection, context stuffing, output probing |
| 공격 경로 | input tokens → attention layers → output distribution → application action |
| 제외 범위 | 실제 서비스 무단 공격, 민감정보 포함 prompt 사용, 악성코드 실행 |

---

## 7. 평가방법 및 지표

| 지표 | 의미 | W04/P03에서의 활용 |
|---|---|---|
| Task Utility | 정상 task 성능 | clean performance |
| Perplexity | 언어모델 예측 품질 | 모델 품질 배경 지표 |
| Robust Accuracy | 교란 텍스트 조건 성능 | NLP robustness 평가 |
| ASR | 공격 목표 성공률 | prompt/NLP attack 평가 |
| Leakage Rate | 민감정보 노출률 | prompt privacy 평가 |
| Latency | 응답 지연 | long-context 운영성 |
| Auditability | 입력·출력·로그 추적 가능성 | MLOps 연결 |

---

## 8. 재현성 점검

| 항목 | 점검 |
|---|---|
| 모델 | Transformer variant, tokenizer, model version 기록 |
| 입력 | prompt, context, adversarial text, privacy-risk prompt 분리 |
| 설정 | max length, truncation, temperature, decoding, seed 기록 |
| 평가 | utility, ASR, robust accuracy, leakage rate, latency 저장 |
| 한계 | taxonomy survey이므로 특정 보안 실험 결과를 직접 제공하지 않음 |

---

## 9. 논문의 고유 기여

1. Transformer 계열 구조와 응용을 큰 taxonomy로 정리했다.
2. W04에서 NLP/LLM 시스템의 기본 대상 구조를 정의하는 배경 문헌이다.
3. 입력·attention·pretraining·application 단계별 보안 위협모형을 나눌 수 있게 한다.
4. P04/P05의 보안 문헌과 결합해 robust/privacy 평가 프레임을 구성할 수 있다.

---

## 10. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 보안 직접성 부족 | 공격·방어·프라이버시 지표를 직접 중심으로 다루지 않는다. | P04/P05와 결합한다. |
| 최신 LLM 한계 | 2022년 survey라 최신 instruction tuning, RAG, agent는 별도 보완 필요 | W07/W08/W14와 연결한다. |
| 실험 부재 | taxonomy survey이므로 재현 실험은 별도 설계 필요 | toy prompt/adversarial text protocol을 사용한다. |

---

## 11. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 2장 관련연구 | Transformer 구조와 응용 taxonomy |
| 3장 위협모형 | input-token-attention-output-log 단계 정의 |
| 4장 연구방법 | utility, ASR, leakage, latency 지표 설계 |
| 6장 보안적 함의 | 입력·출력·로그·도구 호출 보안 해석 |

---

## 12. 기말논문 연결 3문장

1. 이 주차에서 기말논문에 반영할 개념: Transformer 기반 NLP 시스템은 입력 token, attention context, pretraining/fine-tuning data, output log가 모두 보안 자산이 된다.
2. 이 주차에서 기말논문에 반영할 표·그림·실험: Transformer block 수식, input-model-output-log pipeline, 보안 평가 지표 매트릭스를 반영한다.
3. 이 주차가 RAG 문서 오염/LLM 보안 감사 프레임워크와 연결되는 지점: RAG/LLM 시스템도 Transformer 기반 context 처리 위에 구축되므로 P03의 taxonomy를 W08 문서 오염과 W14 MLOps 감사 구조로 확장한다.

---

## 13. 최종 판단

P03은 W04의 대상 시스템을 정의하는 기본 구조 문헌이다. 직접 보안 문헌은 아니므로 P04/P05와 결합해 NLP robustness와 prompt privacy 평가 프레임을 구성한다.

---

## 14. 변환 호환성 메모

```bash
pandoc P03_summary.md -o P03_summary.docx
pandoc P03_summary.md -o P03_summary.pdf --pdf-engine=xelatex
```
