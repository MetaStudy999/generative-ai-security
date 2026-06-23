# W04 100점형 통합 Summary

## Transformer 변형 & NLP 대적공격·프라이버시

## 0. 문서 목적

이 문서는 W04 개별 논문 summary 5개를 기말논문 작성용 연구 노트로 통합한 100점형 요약본이다. 기존 `integrated_report_final.md`는 제출용 통합보고서이고, 본 문서는 개별 PDF summary 보강 결과를 반영한 **논문 작성용 압축본**으로 사용한다.

| 항목 | 내용 |
|---|---|
| 주차 | W04 |
| 주제 | Transformer 변형 & NLP 대적공격·프라이버시 |
| 주요 문헌 | P01–P05 |
| 핵심 프레임 | Efficient attention + practical lightweight Transformer + Transformer taxonomy + NLP robustness + prompt privacy |
| 수식 작성 방식 | GitHub / Word / PDF 변환 호환을 위해 LaTeX block math 사용 |
| 주의사항 | toy word substitution과 regex masking 결과를 실제 LLM 보안 보증으로 해석하지 않는다 |

---

## 1. 한 문장 통합 요약

W04는 Transformer 기반 NLP 시스템을 **attention 비용, 경량화·배포 제약, Transformer 구조 taxonomy, 텍스트 대적공격, 프롬프트 프라이버시** 관점에서 분석하고, 보안 평가는 task utility뿐 아니라 robust accuracy, ASR, leakage rate, over-refusal, latency, auditability를 분리해야 함을 정리하는 주차다.

---

## 2. W04 핵심 연구질문

| 번호 | 연구질문 |
|---|---|
| RQ1 | Transformer self-attention의 비용 병목은 긴 prompt/log/RAG context 보안 평가에 어떤 영향을 주는가? |
| RQ2 | Faster/lighter Transformer 기법은 prompt filter, privacy wrapper, audit module의 운영 가능성을 어떻게 바꾸는가? |
| RQ3 | Transformer taxonomy는 NLP 시스템의 입력·모델·출력·로그·도구 호출 공격면을 어떻게 분리하게 해주는가? |
| RQ4 | NLP adversarial attack은 의미 보존 텍스트 변형에서 clean accuracy와 robust accuracy를 어떻게 분리하게 만드는가? |
| RQ5 | Prompt privacy는 leakage rate, utility, over-refusal, auditability를 어떻게 함께 평가해야 하는가? |
| RQ6 | W04의 평가축을 W08 RAG prompt injection과 W14 MLOps 감사 프레임워크로 어떻게 확장할 수 있는가? |

---

## 3. 문헌 5편 통합 매트릭스

| ID | 논문 | 핵심 역할 | 주요 수식/지표 | 기말논문 반영 위치 |
|---|---|---|---|---|
| P01 | Tay et al., *Efficient Transformers* | attention complexity와 efficient attention taxonomy | full/sparse/kernel attention cost | 2장 관련연구, 4장 운영비용 평가 |
| P02 | Fournier et al., *Faster and Lighter Transformers* | distillation/pruning/quantization/inference optimization | utility-cost score, compression ratio, KD loss | 4장 다중지표 평가 |
| P03 | Lin et al., *A Survey of Transformers* | Transformer 구조와 응용 taxonomy | scaled attention, transformer block, LM objective | 2장 기본 구조, 3장 위협모형 |
| P04 | Goyal et al., *NLP Adversarial Defenses and Robustness* | NLP 대적공격·방어 taxonomy | adversarial risk, ASR, semantic similarity | 3장 위협모형, 4장 robustness 평가 |
| P05 | Edemacu & Wu, *Privacy Preserving Prompt Engineering* | prompt privacy와 leakage/utility 평가 | leakage rate, masking function, privacy-utility score | 4장 privacy 평가, 6장 보안적 함의 |

---

## 4. AI 원리 70% 통합 정리

### 4.1 Scaled Dot-Product Attention

$$
Attention(Q,K,V)=\operatorname{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V
$$

Full attention의 비용은 sequence length $n$에 대해 대략 다음과 같다.

$$
Cost_{full}=O(n^2d)
$$

**보안 해석:** 긴 prompt, 긴 로그, 긴 RAG 문서가 들어오면 비용과 latency가 커지고, 보안 필터·감사 모듈이 생략될 위험이 있다.

---

### 4.2 Efficient Attention

Sparse attention은 제한된 $k$개 token만 참조한다.

$$
Cost_{sparse}\approx O(nkd), \qquad k \ll n
$$

Kernelized attention은 softmax attention을 feature map으로 근사한다.

$$
\operatorname{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V
\approx \phi(Q)\left(\phi(K)^TV\right)
$$

**보안 해석:** 효율화는 운영성을 높이지만 중요한 민감정보, 악성 지시문, policy token이 attention/truncation/coverage 밖으로 밀려날 수 있다.

---

### 4.3 Transformer Block과 LM Objective

$$
H' = \operatorname{LayerNorm}(H + \operatorname{MHA}(H))
$$

$$
H^{out}=\operatorname{LayerNorm}(H' + \operatorname{FFN}(H'))
$$

언어모델 학습 목적은 다음처럼 표현할 수 있다.

$$
\mathcal{L}_{LM}=-\sum_{t=1}^{T}\log p_{\theta}(x_t \mid x_{<t})
$$

**보안 해석:** 입력 token, attention, hidden representation, output distribution이 모두 공격·프라이버시 평가 대상이다.

---

## 5. 보안 이슈 30% 통합 정리

| 보안 축 | 관련 논문 | 핵심 문제 | 주요 지표/증거 |
|---|---|---|---|
| Long-context 비용 | P01 | 긴 prompt/log/RAG context 처리 비용 | latency, memory, context coverage |
| 경량화와 운영성 | P02 | 보안 필터 배포 가능성 | model size, throughput, utility-cost |
| Transformer attack surface | P03 | input-token-attention-output-log 단계 | auditability, leakage, ASR |
| NLP robustness | P04 | word/character/paraphrase attack | robust accuracy, ASR, semantic similarity |
| Prompt privacy | P05 | prompt/context/output/log leakage | leakage rate, masking recall, over-refusal |

---

## 6. W04 통합 위협모형

### 6.1 보호 자산

| 보호 자산 | 설명 |
|---|---|
| Prompt | 사용자 입력과 작업 지시 |
| ICL examples | few-shot 예시와 포함된 민감정보 |
| Context window | RAG 문서, 로그, 대화 기록 |
| Token/Attention state | 모델 내부 참조 경로 |
| Output | 생성 응답, 분류 결과, tool call argument |
| Logs | prompt/output/tool/audit log |
| Lightweight defense | prompt filter, privacy wrapper, detector |

### 6.2 공격자 능력

| 공격자 유형 | 가능 행위 | 대표 지표 |
|---|---|---|
| Text adversary | typo, word substitution, paraphrase | ASR, robust accuracy |
| Privacy attacker | 민감정보 유도, indirect identifier 포함 | leakage rate |
| Context attacker | 긴 context flooding, policy token dilution | context coverage |
| Prompt attacker | policy bypass, masking 우회 | attack success, over-refusal |
| Resource attacker | 비용 높은 입력으로 방어 모듈 우회 | latency, memory |

### 6.3 공격 경로

```text
user prompt / retrieved context / ICL examples
→ tokenizer
→ attention / efficient attention / truncation / memory
→ Transformer output distribution
→ response / tool call / log
→ adversarial failure, privacy leakage, over-refusal, audit gap 발생
```

---

## 7. 통합 평가 지표

| 평가축 | 대표 지표 | 해석 | 관련 논문 |
|---|---|---|---|
| Utility | accuracy, F1, task success, ROUGE | 정상 작업 품질 | P02, P03 |
| Robustness | robust accuracy, ASR, transferability | 텍스트 교란 대응 | P04 |
| Semantic Validity | semantic similarity, fluency | 공격 입력 타당성 | P04 |
| Privacy | leakage rate, masking precision/recall | 민감정보 보호 | P05 |
| Over-refusal | 정상 요청 거절률 | 과차단 부작용 | P05 |
| Efficiency | latency, memory, throughput, size | 운영 가능성 | P01, P02 |
| Auditability | prompt/output/tool/log trace | 사후 검증 가능성 | P03, P05 |

---

## 8. 핵심 수식 묶음

### 8.1 Utility-Cost Score

$$
Score = Utility - \lambda_1 Latency - \lambda_2 Memory - \lambda_3 Size - \lambda_4 Energy
$$

### 8.2 NLP Adversarial Risk

$$
R_{adv}=\mathbb{E}_{(x,y)}\left[\max_{x_{alt}\in\mathcal{N}(x)}\ell(f_{\theta}(x_{alt}),y)\right]
$$

### 8.3 Attack Success Rate

$$
ASR=\frac{1}{m}\sum_{j=1}^{m}\mathbf{1}[f_{\theta}(x_j^{adv})\neq y_j]
$$

### 8.4 Privacy Leakage Rate

$$
LeakageRate=\frac{N_{sensitive\_output}}{N_{privacy\_risk\_prompts}}
$$

### 8.5 Privacy-Utility Score

$$
PrivacyUtilityScore = Utility - \lambda LeakageRate - \mu OverRefusal
$$

---

## 9. 재현성 체크리스트

| 항목 | 필수 기록 | W04 적용 |
|---|---|---|
| 문헌 | DOI, URL, 로컬 PDF명, 검증 상태 | P01–P05 summary에 반영 |
| 모델 | tokenizer, Transformer variant, model version | 필수 기록 |
| 입력 | clean prompt, adversarial text, privacy-risk prompt | 분리 저장 |
| 방어 | masking, rewriting, detector, filter, policy wrapper | 조건 기록 |
| 설정 | max length, truncation, decoding, seed, latency setting | config 저장 |
| 평가 | utility, ASR, leakage, over-refusal, latency | CSV/JSON 저장 |
| 한계 | toy 결과를 실제 LLM guarantee로 일반화 금지 | 명시 필요 |
| AI 활용 | 요약·수식 설명·표 구조화 사용 내역 | AI 활용 고지 필요 |

---

## 10. 기말논문 반영 구조

| 기말논문 장 | W04 반영 내용 |
|---|---|
| 1장 서론 | Transformer/LLM 입력 보안과 프롬프트 프라이버시 문제 제시 |
| 2장 관련연구 | Efficient Transformer, Transformer taxonomy, NLP robustness, prompt privacy 정리 |
| 3장 위협모형 | input-token-attention-output-log-tool call 공격 경로 정의 |
| 4장 연구방법 | ASR, robust accuracy, semantic similarity, leakage rate, over-refusal, latency 지표 설계 |
| 5장 실험/분석 | toy word substitution과 synthetic prompt masking 결과를 제한적으로 제시 |
| 6장 보안적 함의 | 기밀성, 무결성, 가용성, 프라이버시, 책임성 해석 |
| 7장 결론 | LLM/RAG 보안 평가는 utility, robustness, privacy, cost, auditability를 함께 봐야 함을 제시 |

---

## 11. W04 기말논문 연결 3문장

1. W04에서 기말논문에 반영할 개념: Transformer 기반 NLP 보안은 입력 문장만이 아니라 attention context, 프롬프트, ICL 예시, 출력, 도구 호출, 로그까지 포함하는 end-to-end 평가가 필요하다.
2. W04에서 기말논문에 반영할 표·그림·실험: attention complexity, NLP adversarial risk, ASR, leakage rate, privacy-utility score, prompt pipeline threat model을 반영한다.
3. W04가 RAG 문서 오염/LLM 보안 감사 프레임워크와 연결되는 지점: RAG/LLM 시스템은 긴 context와 prompt privacy 위험을 동시에 갖기 때문에 W04의 robustness/privacy/latency/auditability 지표를 W08/W14로 확장한다.

---

## 12. 최종 판단

W04의 5개 문헌은 다음 역할로 정리한다.

| 문헌 | 최종 판단 |
|---|---|
| P01 | Efficient attention과 long-context 비용 평가의 핵심 문헌 |
| P02 | Faster/lighter Transformer의 practical deployment 평가 문헌 |
| P03 | Transformer 구조와 응용 taxonomy의 기본 문헌 |
| P04 | NLP adversarial robustness의 핵심 보안 문헌 |
| P05 | Prompt privacy와 privacy-utility 평가의 핵심 문헌 |

W04는 후속 W07 LLM security, W08 RAG/prompt injection, W11 DP/privacy, W14 MLOps auditing으로 확장된다. 특히 기말논문에서는 “프롬프트 기반 AI 시스템의 민감정보 보호와 우회 공격 평가체계”로 발전시키기 적합하다.

---

## 13. 변환 호환성 메모

```bash
pandoc w04_integrated_summary_100point.md -o w04_integrated_summary_100point.docx
pandoc w04_integrated_summary_100point.md -o w04_integrated_summary_100point.pdf --pdf-engine=xelatex
```
