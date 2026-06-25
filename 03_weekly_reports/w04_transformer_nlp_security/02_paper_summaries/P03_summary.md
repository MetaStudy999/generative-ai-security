# P03 Summary

## A Survey of Transformers — Tianyang Lin, Yuxin Wang, Xiangyang Liu, Xipeng Qiu, AI Open, 2022

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W04 Transformer 변형 & NLP 대적공격·프라이버시 |
| 논문명 | A survey of transformers |
| 저자 | Tianyang Lin, Yuxin Wang, Xiangyang Liu, Xipeng Qiu |
| 공식 출판 정보 | AI Open, Vol. 3, pp. 111–132, 2022 |
| DOI | https://doi.org/10.1016/j.aiopen.2022.10.001 |
| 공식 URL | https://www.sciencedirect.com/science/article/pii/S2666651022000146 |
| 논문 유형 | Survey / General Transformer Taxonomy Review |
| 로컬 PDF | `01_papers/pdf/03_Lin_et_al_2022_Survey_of_Transformers.pdf` |
| 검증 상태 | W04 `paper_list.md` 기준 AI Open 출판 DOI, 권호, 쪽수 확인. 강의계획서 지정 논문과 일치 |
| PDF 확인 메모 | repo의 PDF 폴더에 P03 관련 PDF blob이 존재함을 확인했다. 요약은 로컬 PDF 경로와 W04 `paper_list.md`의 공식 DOI 메타데이터 기준으로 보완했다. |
| 수식 호환성 | GitHub 수식 렌더링 오류 방지를 위해 `\operatorname`을 사용하지 않고 `\mathrm{...}` 형태로 작성했다. |
| 핵심 근거 사용 가능 여부 | 가능. W04에서 vanilla Transformer, self-attention, positional encoding, Transformer block, pretraining/fine-tuning, NLP/CV/audio/multimodal applications, input-token-attention-output-log 위협모형의 기본 taxonomy 문헌으로 사용 |

---

## 1. 한 문장 요약

이 논문은 Transformer 계열 모델을 **self-attention, multi-head attention, positional encoding, encoder-decoder structure, architectural modification, pretraining, fine-tuning, NLP/CV/audio/multimodal applications** 관점에서 폭넓게 정리하며, W04에서는 NLP/LLM 보안 위협모형을 **입력 token, attention context, hidden representation, output distribution, prompt/context log, external application action** 단계로 분해하는 기본 구조 문헌으로 사용된다.

---

## 2. 핵심 연구문제

> Vanilla Transformer 이후 다양한 구조와 응용은 어떤 taxonomy로 분류할 수 있으며, 이러한 구조적 차이는 NLP/멀티모달 보안에서 보호 자산과 공격면을 어떻게 바꾸는가?

| 번호 | 연구질문 |
|---|---|
| RQ1 | Transformer의 핵심 구성요소인 self-attention, multi-head attention, positional encoding, FFN, residual connection은 어떻게 결합되는가? |
| RQ2 | Attention, position encoding, depth, recurrence, memory, architecture modification은 어떤 방향으로 발전했는가? |
| RQ3 | Pretraining과 downstream fine-tuning은 Transformer 응용 성능과 보안 위험에 어떤 영향을 주는가? |
| RQ4 | NLP, CV, audio, multimodal Transformer는 보안 위협모형에서 각각 어떤 보호 자산과 공격면을 갖는가? |
| RQ5 | 프롬프트 보안 평가에서 input-token-attention-output-log-tool 단계의 evidence chain을 어떻게 설계해야 하는가? |

---

## 3. 논문의 핵심 기여

| 기여 | 설명 | W04 연결 |
|---|---|---|
| Transformer taxonomy 정리 | Transformer의 기본 구조와 다양한 변형을 큰 분류체계로 정리 | W04 대상 시스템 정의 |
| Attention 중심 설명 | self-attention과 multi-head attention의 핵심 원리를 설명 | NLP 공격면의 구조적 기반 |
| 구조 변형 정리 | position encoding, memory, recurrence, efficient architecture 등 변형 방향 소개 | P01/P02 efficient transformer와 연결 |
| 응용 범위 확장 | NLP뿐 아니라 CV, speech/audio, multimodal application까지 확장 | W03/W07/W08 bridge |
| 보안 위협모형 기반 제공 | 직접 보안 문헌은 아니지만 input-token-attention-output-log 단계 구분에 유용 | P04/P05 보안 문헌 연결 |

---

## 4. 목차별 핵심 개괄

| 목차 | 핵심 내용 | 비전공자용 이해 |
|---|---|---|
| 1. Introduction | Transformer는 sequence modeling에서 RNN/CNN 한계를 줄이고 attention 기반 병렬 처리를 가능하게 했다. | 문장 안 단어들이 서로를 직접 참고하는 구조다. |
| 2. Vanilla Transformer | encoder, decoder, self-attention, multi-head attention, FFN, residual connection을 설명한다. | Transformer의 기본 블록을 이해하는 부분이다. |
| 3. Attention Mechanisms | scaled dot-product attention, multi-head attention, attention variants를 정리한다. | 어떤 단어가 어떤 단어를 얼마나 참조하는지 계산한다. |
| 4. Positional Encoding | 순서 정보가 없는 attention에 위치 정보를 추가하는 방법을 설명한다. | 단어 순서를 모델이 알 수 있게 해준다. |
| 5. Architectural Variants | efficient, sparse, memory-augmented, recurrence, depth/width 변경 구조를 다룬다. | Transformer를 더 빠르거나 깊거나 길게 처리하도록 바꾼다. |
| 6. Pretraining and Fine-tuning | 대규모 corpus에서 사전학습하고 task에 맞게 조정하는 과정을 설명한다. | 먼저 많이 읽고, 나중에 특정 일을 배우는 방식이다. |
| 7. Applications | NLP, CV, audio, multimodal, reinforcement learning 등 응용을 정리한다. | Transformer가 언어를 넘어 여러 분야로 확장되었다. |
| 8. Challenges | 계산 비용, 긴 context, 데이터 편향, 해석 가능성, robustness, privacy 문제가 남는다. | 성능은 좋지만 비용과 안전 문제가 있다. |
| 보안 연결 | 입력, context, attention, output, log, tool action이 모두 보안 자산이 된다. | 프롬프트와 출력뿐 아니라 내부 처리 경로도 관리해야 한다. |

---

## 5. 핵심 이론 및 수식

> 수식은 GitHub Markdown/KaTeX 호환성을 우선한다. `\operatorname` 매크로는 사용하지 않고 `\mathrm{...}` 형태로 작성한다.

### 5.1 Scaled Dot-Product Attention

Transformer의 핵심 연산은 token 간 관계를 attention weight로 계산하는 것이다.

$$
Attention(Q,K,V)=\mathrm{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V
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

### 5.2 Multi-Head Attention

여러 attention head는 서로 다른 representation subspace에서 token 관계를 학습한다.

$$
\mathrm{MHA}(Q,K,V)=\mathrm{Concat}(head_1,\ldots,head_h)W^O
$$

$$
head_i=Attention(QW_i^Q,KW_i^K,VW_i^V)
$$

### 보안적 의미

특정 head가 안전 정책, 민감정보, 문맥 단서, 특정 syntax 패턴에 민감할 수 있다. Head pruning이나 attention 분석을 할 때 보안 관련 head가 제거되거나 약화되지 않는지 확인해야 한다.

---

### 5.3 Transformer Block

Transformer block은 attention과 feed-forward network를 잔차 연결과 정규화로 반복한다.

$$
H'=\mathrm{LayerNorm}(H+\mathrm{MHA}(H))
$$

$$
H^{out}=\mathrm{LayerNorm}(H'+\mathrm{FFN}(H'))
$$

| 기호 | 의미 |
|---|---|
| $H$ | 입력 hidden states |
| $\mathrm{MHA}$ | multi-head attention |
| $\mathrm{FFN}$ | feed-forward network |
| $H^{out}$ | block 출력 |

### 보안적 의미

입력 token의 교란은 여러 layer를 거치며 증폭되거나 완화될 수 있다. 따라서 NLP 공격은 입력 표면형뿐 아니라 내부 representation, layer별 attention, output confidence까지 평가해야 한다.

---

### 5.4 Positional Encoding

순서 정보가 없는 attention에 위치 정보를 더해 token 순서를 반영한다.

$$
H_0=E_{token}+E_{pos}
$$

| 기호 | 의미 |
|---|---|
| $E_{token}$ | token embedding |
| $E_{pos}$ | positional embedding 또는 positional encoding |
| $H_0$ | 위치 정보가 반영된 초기 hidden representation |

### 보안적 의미

Prompt injection은 단순 단어 존재뿐 아니라 위치, 순서, system/user/context 구분에 민감하다. 위치 encoding과 truncation rule은 보안 평가의 기록 대상이다.

---

### 5.5 Pretraining / Fine-tuning Objective

언어모델의 기본 학습은 다음 token 또는 masked token을 예측하는 형태로 볼 수 있다.

$$
\mathcal{L}_{LM}=-\sum_{t=1}^{T}\log p_{\theta}(x_t\mid x_{<t})
$$

### 보안적 의미

Pretraining/fine-tuning data에 민감정보나 악성 패턴이 포함되면 모델 출력, memorization, prompt behavior, downstream task에 영향을 줄 수 있다.

---

### 5.6 Attack Success Rate

NLP 또는 prompt 공격의 목표 성공률을 평가한다.

$$
ASR=\frac{N_{attack\ success}}{N_{attack\ trials}}
$$

### 보안적 의미

Transformer taxonomy를 위협모형으로 확장하려면 정상 성능뿐 아니라 공격 성공률을 별도 지표로 기록해야 한다.

---

### 5.7 Leakage Rate

모델 출력에서 민감정보가 노출되는 비율이다.

$$
LeakageRate=\frac{N_{leaked\ outputs}}{N_{total\ outputs}}
$$

### 보안적 의미

Prompt, context, fine-tuning data, log가 민감정보를 포함하면 출력과 로그를 통해 leakage가 발생할 수 있다.

---

### 5.8 Transformer Security Risk

Transformer 기반 NLP 시스템의 보안 위험을 입력, attention, 학습 데이터, 출력, 로그 위험으로 분해한다.

$$
TransformerRisk=InputRisk+AttentionRisk+DataRisk+OutputRisk+LogRisk-MonitoringCoverage
$$

### 보안적 의미

Transformer 보안은 입력만 막는 문제가 아니다. attention context, pretraining/fine-tuning data, output distribution, logging, tool call까지 함께 관리해야 한다.

---

## 6. AI 원리 70% 관점 분석

| 원리 항목 | 설명 | W04/P03에서의 의미 |
|---|---|---|
| Vanilla Transformer | self-attention, positional encoding, FFN, residual connection으로 구성 | 기본 대상 구조 |
| Self-Attention | token 간 전역 관계를 학습 | prompt/context 영향 분석 |
| Multi-Head Attention | 여러 subspace에서 관계 학습 | head별 기능과 취약성 |
| Positional Encoding | token 순서 정보 반영 | prompt 순서·truncation 평가 |
| Pretraining | 대규모 corpus에서 일반 표현 학습 | data risk와 memorization |
| Fine-tuning | task 또는 instruction에 맞게 모델 조정 | downstream policy 변화 |
| Applications | NLP, CV, audio, multimodal tasks로 확장 | 위협모형 범위 확장 |
| Taxonomy | 구조별·응용별 차이를 분류 | 보안 평가 프레임의 뼈대 |

---

## 7. 보안 이슈 30% 관점 분석

| 보안 항목 | Transformer taxonomy 관점 해석 | 대표 평가 지표 |
|---|---|---|
| 기밀성 | pretraining/fine-tuning data, prompt, context, log에 민감정보가 포함될 수 있음 | LeakageRate, PII finding |
| 무결성 | 입력 token, prompt, retrieved context가 출력 결정을 왜곡할 수 있음 | ASR, robust accuracy |
| 가용성 | 긴 입력과 복잡한 모델은 latency와 비용 문제를 만듦 | latency, memory |
| 프라이버시 | context, ICL examples, output probability가 정보 누출 경로가 됨 | MI signal, confidence leakage |
| 안전성 | 공격 prompt와 unsafe context가 모델 행동을 바꿀 수 있음 | unsafe response rate |
| 책임성 | 모델 구조, 데이터, prompt, output, tool call log를 기록해야 함 | auditability, trace coverage |

---

## 8. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 대상 | prompt, token sequence, attention context, positional context, model weights, pretraining/fine-tuning data, output, log, external tool call |
| 공격자 목표 | 입력 의미 왜곡, 정책 우회, 민감정보 유출, 출력 조작, tool action 오용 |
| 공격자 능력 | adversarial text, paraphrase, typo, prompt injection, context stuffing, output probing, poisoned context 제공 |
| 공격 경로 | input tokens → embedding/position → attention layers → output distribution → application action/log |
| 방어자 능력 | prompt validation, context filtering, retrieval source checking, output monitoring, logging, human review, tool permission control |
| 제외 범위 | 실제 서비스 무단 공격, 민감정보 포함 prompt 사용, 악성코드 실행, 공격 prompt 제작 지원 |

---

## 9. 평가방법 및 지표

| 평가축 | 지표 | 의미 | W04/P03 활용 |
|---|---|---|---|
| 정상 성능 | task utility, accuracy, F1 | clean performance | baseline |
| 언어모델 품질 | perplexity, loss | 예측 품질 | LM 평가 |
| 강건성 | robust accuracy, ASR | 교란 텍스트 조건 성능 | NLP robustness |
| 프라이버시 | LeakageRate, PII detection | 민감정보 노출 | prompt privacy |
| 운영성 | latency, memory, max length | long-context 운영 가능성 | W04 P01/P02 연결 |
| 감사성 | auditability, trace coverage | 입력·출력·로그 추적 가능성 | W15 연결 |
| 도구 안전성 | unsafe tool call rate | application action 위험 | agent/RAG 연결 |
| 재현성 | model/config/prompt/output log | 결과 재현 가능성 | W15 evidence chain |

---

## 10. 재현성 체크리스트

| 항목 | 기록해야 할 내용 |
|---|---|
| Bibliographic status | DOI, AI Open 출판정보, 로컬 PDF 판본 상태 |
| Model | Transformer variant, tokenizer, model version, checkpoint/hash |
| Input | prompt, context, adversarial text, privacy-risk prompt, retrieval source |
| Position/context | max length, truncation rule, context order, system/user/context 구분 |
| Decoding | temperature, top-p, max tokens, seed, stop sequence |
| Evaluation | utility, ASR, robust accuracy, LeakageRate, latency, memory |
| Logs | raw input, raw output, prompt template, tool call log, refusal text |
| Security | prompt injection setting, paraphrase/typo condition, PII scan, unsafe output check |
| Evidence | config file, model card, data card, metric CSV/JSON, script commit |
| GitHub math | `\operatorname` 사용 금지, `\mathrm{softmax}`·`\mathrm{MHA}`·`\mathrm{FFN}` 형태 사용 |

---

## 11. 논문의 고유 기여

1. Transformer 계열 구조와 응용을 큰 taxonomy로 정리했다.
2. W04에서 NLP/LLM 시스템의 기본 대상 구조를 정의하는 배경 문헌이다.
3. 입력·attention·pretraining·application 단계별 보안 위협모형을 나눌 수 있게 한다.
4. P04/P05의 NLP adversarial robustness와 prompt privacy 문헌을 연결하는 구조적 기반을 제공한다.
5. W07 LLM, W08 RAG, W14 MLOps, W15 reproducibility로 확장되는 input-model-output-log evidence chain의 기초가 된다.

---

## 12. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 보안 직접성 부족 | 공격·방어·프라이버시 지표를 직접 중심으로 다루지 않는다. | W04 P04/P05와 결합 |
| 최신 LLM 한계 | 2022년 survey라 instruction tuning, RAG, tool use, agent 최신 논의는 별도 보완 필요 | W07/W08/W14와 연결 |
| 실험 부재 | taxonomy survey이므로 재현 실험은 별도 설계 필요 | toy prompt/adversarial text protocol 사용 |
| 수식 세부 부족 | survey 특성상 수식보다 taxonomy 중심이다. | W04 보고서에서 수식과 평가 지표 보완 |
| 구현 의존성 | Transformer variant별 구현 차이가 크다. | tokenizer/model/config를 명확히 기록 |
| 저작권 관리 | PDF 원문을 public repo에 유지하면 권리 조건 검토가 필요하다. | DOI/서지/summary 중심 공개 검토 |

---

## 13. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | Transformer 기반 NLP/LLM 보안에서 input-token-attention-output-log 단계가 모두 보안 자산이라는 문제의식 |
| 2장 관련연구 | Transformer 구조와 응용 taxonomy 정리 |
| 3장 위협모형 | input-token-attention-output-log-tool 단계 정의 |
| 4장 연구방법 | attention, Transformer block, LM objective, ASR, LeakageRate, TransformerRisk 지표 설계 |
| 5장 분석 | Transformer pipeline과 보안 공격면 연결표 제시 |
| 6장 보안적 함의 | 입력·출력·로그·도구 호출 보안 해석 |
| 부록 | prompt, context, decoding config, raw output, tool call log 수록 |

---

## 14. 기말논문 연결 3문장

1. W04에서 기말논문에 반영할 개념: Transformer 기반 NLP 시스템은 입력 token, attention context, pretraining/fine-tuning data, output distribution, log가 모두 보안 자산이 된다.
2. W04에서 기말논문에 반영할 표·그림·실험: scaled attention, Transformer block, LM objective, ASR, LeakageRate, TransformerRisk 수식표와 input-model-output-log pipeline을 반영한다.
3. W04가 W15 최종 제출과 연결되는 지점: Transformer 평가 결과는 model version, tokenizer, prompt/context, decoding config, raw output, refusal text, tool call log를 evidence chain으로 남겨야 재현성과 신뢰성을 확보할 수 있다.

---

## 15. 최종 판단

P03은 W04의 대상 시스템을 정의하는 기본 구조 문헌이다. 직접 보안 문헌은 아니지만, Transformer 기반 NLP/LLM 시스템의 보호 자산과 공격면을 input-token-attention-output-log-tool 단계로 나누는 데 필수적이다. 따라서 기말논문에서는 P03을 **Transformer taxonomy, self-attention, pretraining/fine-tuning, NLP/LLM 보안 위협모형의 구조적 배경 문헌**으로 사용하고, 실제 robust/privacy 평가는 W04 P04/P05 및 W07/W08 문헌과 결합하는 것이 적절하다.

---

## 16. GitHub 수식 호환성 메모

이 파일에서는 GitHub 수식 렌더링 오류 방지를 위해 `\operatorname`을 사용하지 않는다.

| 피해야 할 표현 | 권장 표현 |
|---|---|
| `\operatorname{softmax}` | `\mathrm{softmax}` |
| `\operatorname{LayerNorm}` | `\mathrm{LayerNorm}` |
| `\operatorname{MHA}` | `\mathrm{MHA}` |
| `\operatorname{FFN}` | `\mathrm{FFN}` |
| `\operatorname{argmax}` | `\mathrm{argmax}` 또는 `\arg\max` |

```bash
pandoc P03_summary.md -o P03_summary.docx
pandoc P03_summary.md -o P03_summary.pdf --pdf-engine=xelatex
```
