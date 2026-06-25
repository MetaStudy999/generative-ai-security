# P01 Summary

## Efficient Transformers: A Survey — Yi Tay, Mostafa Dehghani, Dara Bahri, Donald Metzler, ACM Computing Surveys, 2022

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W04 Transformer 변형 & NLP 대적공격·프라이버시 |
| 논문명 | Efficient Transformers: A Survey |
| 저자 | Yi Tay, Mostafa Dehghani, Dara Bahri, Donald Metzler |
| 공식 출판 정보 | ACM Computing Surveys, Vol. 55, No. 6, pp. 1–28, 2022 |
| DOI | https://doi.org/10.1145/3530811 |
| 보조 URL | https://arxiv.org/abs/2009.06732 |
| 논문 유형 | Survey / Efficient Attention and X-former Review |
| 로컬 PDF | `01_papers/pdf/01_Tay_et_al_2022_Efficient_Transformers_Survey.pdf` |
| 검증 상태 | W04 `paper_list.md` 기준 ACM CSUR 출판 DOI 확인. arXiv 최초 공개 2020년, arXiv v3 2022년 갱신판, ACM CSUR 판은 같은 제목과 저자 기준으로 정리 |
| PDF 확인 메모 | repo의 PDF 폴더에 P01 관련 PDF blob이 존재함을 확인했다. 요약은 로컬 PDF 경로와 W04 `paper_list.md`의 공식 DOI 메타데이터 기준으로 보완했다. |
| 수식 호환성 | GitHub 수식 렌더링 오류 방지를 위해 `\operatorname`을 사용하지 않고 `\mathrm{...}` 형태로 작성했다. |
| 핵심 근거 사용 가능 여부 | 가능. W04에서 full attention complexity, sparse attention, low-rank attention, kernelized attention, memory/recurrence, long-context 처리, LLM/RAG 보안 비용·문맥 커버리지 평가의 핵심 문헌으로 사용 |

---

## 1. 한 문장 요약

이 논문은 Transformer self-attention의 $O(n^2)$ 시간·메모리 병목을 완화하기 위해 제안된 **sparse attention, local attention, low-rank approximation, kernelized attention, locality-sensitive hashing, recurrence/memory, compressed context, routing, efficient positional mechanism** 계열 Efficient Transformer를 체계화하며, W04에서는 긴 prompt·긴 로그·RAG 문서·보안 감사 context를 다룰 때 **latency, memory, context coverage, approximation error, detection recall, privacy leakage**를 별도 지표로 평가해야 함을 보여주는 핵심 survey 문헌이다.

---

## 2. 핵심 연구문제

> Transformer는 모든 token pair를 비교하는 full self-attention 때문에 sequence length가 길어질수록 계산량과 메모리가 급증한다. Efficient Transformer 연구의 핵심은 비용을 줄이면서도 long-context utility와 attention 품질을 유지하는 것이다. 보안 관점에서는 효율화 자체보다, 효율화 과정에서 어떤 token이 누락되고 어떤 보안 단서가 약화되는지를 평가해야 한다.

| 번호 | 연구질문 |
|---|---|
| RQ1 | Full self-attention의 quadratic complexity 병목은 어떤 수식과 비용 구조로 설명되는가? |
| RQ2 | Sparse, local, low-rank, kernelized, memory/recurrence attention은 각각 어떤 방식으로 시간·메모리 비용을 줄이는가? |
| RQ3 | Efficient attention은 긴 prompt, 긴 보안 로그, RAG 문서, 장문 정책 문서 처리에서 어떤 장점과 위험을 만드는가? |
| RQ4 | Sparse 또는 approximate attention이 악성 지시문, 민감정보, policy violation token을 놓칠 가능성은 어떻게 평가해야 하는가? |
| RQ5 | 기말논문에서 Transformer 기반 보안 시스템을 평가할 때 latency, memory, context coverage, detection recall, leakage rate를 어떻게 evidence chain에 포함할 것인가? |

---

## 3. 논문의 핵심 기여

| 기여 | 설명 | W04 연결 |
|---|---|---|
| Efficient Transformer taxonomy | attention 효율화 기법을 구조별로 체계화 | W04 P01 핵심 |
| Complexity bottleneck 정리 | full attention의 $O(n^2d)$ 비용 문제를 명확화 | long-context 평가 근거 |
| 효율화 계열 비교 | sparse, low-rank, kernelized, memory/recurrence, routing 등 접근 비교 | 수식·표 정리 |
| Long-context 처리 논의 | 긴 sequence를 다루는 구조적 trade-off 설명 | RAG/log/prompt 보안 연결 |
| Utility-cost 관점 제공 | 정확도뿐 아니라 latency, memory, throughput, approximation quality가 중요함을 제시 | 운영 보안 평가축 |

---

## 4. 목차별 핵심 개괄

| 목차 | 핵심 내용 | 비전공자용 이해 |
|---|---|---|
| 1. Introduction | Transformer의 강점과 full self-attention의 비용 병목을 제시한다. | 문장이 길어지면 모든 단어끼리 비교하므로 계산량이 폭증한다. |
| 2. Background | self-attention, multi-head attention, Transformer block, sequence length와 complexity를 설명한다. | Transformer가 토큰 사이 관계를 계산하는 기본 원리다. |
| 3. Taxonomy | Efficient Transformer를 sparse, low-rank, kernelized, memory, recurrence, routing 등으로 분류한다. | 비용을 줄이는 방법에는 여러 계열이 있다. |
| 4. Sparse Attention | 모든 token을 보지 않고 일부 token만 선택적으로 참조한다. | 중요한 위치만 보도록 하여 계산량을 줄인다. |
| 5. Low-rank Methods | attention matrix를 낮은 rank 구조로 근사한다. | 큰 행렬을 더 작은 구조로 압축한다. |
| 6. Kernelized Attention | softmax attention을 feature map 기반 선형 계산으로 근사한다. | 모든 쌍을 직접 비교하지 않고 빠르게 계산한다. |
| 7. Recurrence/Memory | 이전 context를 memory로 저장하거나 압축해 긴 문맥을 처리한다. | 긴 문서를 한 번에 다 보지 않고 요약 기억을 활용한다. |
| 8. Evaluation | 효율화는 task utility, speed, memory, long-range dependency 유지 여부로 평가해야 한다. | 빠르기만 하면 부족하고 정답 품질도 유지해야 한다. |
| 9. Challenges | 근사 오류, context loss, hardware efficiency, benchmark 차이, long-context 일반화가 문제다. | 빠르게 하면서 중요한 내용을 놓치지 않는 것이 어렵다. |
| 보안 연결 | 긴 context 보안에서는 attention 축약이 악성 지시문·민감정보·정책 위반 단서를 누락시킬 수 있다. | 효율화가 보안 탐지 누락을 만들 수 있다. |

---

## 5. 핵심 이론 및 수식

> 수식은 GitHub Markdown/KaTeX 호환성을 우선한다. `\operatorname` 매크로는 사용하지 않고 `\mathrm{...}` 형태로 작성한다.

### 5.1 Full Self-Attention

Transformer self-attention은 모든 token pair를 비교해 attention weight를 계산한다.

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

Full attention은 전역 context를 잘 반영하지만 비용이 크다. 보안 로그, 장문 prompt, RAG 문서 검증처럼 긴 입력을 처리할 때 full attention 비용이 커지면 보안 필터나 감사 모듈이 생략될 위험이 있다.

---

### 5.2 Full Attention Complexity

길이 $n$, hidden dimension $d$인 sequence에서 full attention의 주요 비용은 다음과 같이 근사된다.

$$
Cost_{full}=O(n^2d)
$$

### 보안적 의미

입력 길이가 2배가 되면 attention 비용은 대략 4배로 증가한다. 장문 prompt 기반 공격, context flooding, indirect prompt injection 방어에서는 비용 증가가 보안 운영의 병목이 된다.

---

### 5.3 Sparse Attention Complexity

Sparse attention은 각 token이 전체가 아니라 제한된 $k$개 token만 참조하도록 한다.

$$
Cost_{sparse}\approx O(nkd),\qquad k\ll n
$$

| 기호 | 의미 |
|---|---|
| $k$ | 각 token이 참조하는 제한된 key 수 |
| $n$ | sequence length |
| $d$ | hidden dimension |

### 보안적 의미

Sparse attention은 긴 입력 처리 비용을 줄이지만, 중요 보안 단서가 attention pattern 밖에 있으면 민감정보 탐지나 간접 인젝션 탐지가 누락될 수 있다.

---

### 5.4 Kernelized Attention

Softmax attention은 feature map $\phi$를 이용해 선형화할 수 있다.

$$
\mathrm{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V\approx \phi(Q)\left(\phi(K)^TV\right)
$$

| 기호 | 의미 |
|---|---|
| $\phi$ | kernel 또는 random feature map |
| $Q,K,V$ | attention 입력 |

### 보안적 의미

Kernelized attention은 throughput을 높일 수 있지만, 근사 품질이 낮으면 long-context에서 중요한 정책 문장, 민감정보, 악성 지시문을 약하게 반영할 수 있다.

---

### 5.5 Context Coverage

보안 관련 token이 attention 또는 retrieval 처리 범위에 얼마나 포함되는지 평가한다.

$$
ContextCoverage=\frac{|Tokens_{security\ covered}|}{|Tokens_{security\ relevant}|}
$$

### 보안적 의미

긴 문서에서 보안 관련 문장이 처리 범위 밖으로 밀려나면 모델은 안전하지 않은 결론을 낼 수 있다. RAG와 prompt filtering에서는 context coverage를 별도로 기록해야 한다.

---

### 5.6 Approximation Error

Efficient attention이 full attention과 얼마나 다른지 측정한다.

$$
ApproxError=\frac{\|A_{full}-A_{eff}\|_F}{\|A_{full}\|_F+\epsilon}
$$

| 기호 | 의미 |
|---|---|
| $A_{full}$ | full attention matrix |
| $A_{eff}$ | efficient attention이 근사한 attention matrix |
| $\epsilon$ | 0 나눗셈 방지 상수 |

### 보안적 의미

근사 오류가 크면 모델이 봐야 할 long-range dependency나 정책 조건을 놓칠 수 있다.

---

### 5.7 Detection Recall Under Efficient Attention

효율화된 attention 조건에서 악성·민감 token 탐지율을 측정한다.

$$
Recall_{detect}=\frac{TP}{TP+FN}
$$

### 보안적 의미

Latency와 memory가 줄어도 detection recall이 낮아지면 보안 모듈로 적합하지 않다.

---

### 5.8 Utility-Cost Score

효율화 모델의 성능과 비용을 함께 평가한다.

$$
UtilityCostScore=Utility-\lambda Latency-\mu Memory-\gamma ApproxError
$$

### 보안적 의미

운영 가능한 보안 시스템은 좋은 성능뿐 아니라 낮은 지연, 낮은 메모리, 낮은 근사 오류를 함께 만족해야 한다.

---

### 5.9 Long-Context Security Risk

긴 context 기반 Transformer 보안 위험을 요약한다.

$$
LongContextRisk=ContextLoss+ApproxError+LeakageRisk+DetectionMiss-MonitoringCoverage
$$

### 보안적 의미

Efficient Transformer는 긴 context 처리를 가능하게 하지만, context 손실·근사 오류·민감정보 노출·탐지 누락을 함께 관리해야 한다.

---

## 6. AI 원리 70% 관점 분석

| 원리 항목 | 설명 | W04/P01에서의 의미 |
|---|---|---|
| Full Attention | 모든 token pair를 비교해 전역 관계를 학습 | 표현력은 강하지만 비용이 큼 |
| Sparse Attention | 선택된 token 연결만 계산 | 비용 절감, coverage 관리 필요 |
| Low-rank Approximation | attention matrix를 낮은 rank로 근사 | memory 절감, 근사 오류 평가 필요 |
| Kernelized Attention | softmax attention을 feature map으로 선형화 | 긴 sequence 처리 효율화 |
| Local Attention | 주변 token 중심 attention | locality 활용, long-range 누락 위험 |
| Memory/Recurrence | 이전 context를 압축·재사용 | 긴 문서 처리와 memory risk |
| Long-context Modeling | 긴 로그, 긴 문서, 긴 prompt 처리 | RAG·보안 감사 연결 |
| Utility-Cost Trade-off | 성능과 latency/memory 균형 | 운영 보안 평가 핵심 |

---

## 7. 보안 이슈 30% 관점 분석

| 보안 항목 | Efficient Transformer 관점 해석 | 대표 평가 지표 |
|---|---|---|
| 기밀성 | 긴 prompt/log/RAG context에 민감정보가 포함될수록 leakage surface 증가 | leakage rate, redaction coverage |
| 무결성 | 긴 context 안의 악성 지시문이나 오염 문서가 attention/fusion에 포함될 수 있음 | detection recall, ASR |
| 가용성 | full attention 비용은 보안 필터와 감사 모듈의 운영 적용을 어렵게 만듦 | latency, memory, throughput |
| 프라이버시 | memory cache와 long-context log가 개인정보를 보존할 수 있음 | retention policy, memory leakage |
| 안전성 | context truncation 또는 approximation error로 정책 조건을 놓칠 수 있음 | ContextCoverage, ApproxError |
| 책임성 | attention pattern, truncation rule, memory reuse 정책을 기록해야 감사 가능 | config log, source traceability |

---

## 8. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 대상 | 긴 프롬프트, 보안 로그, RAG 문서, system prompt, memory cache, attention context, truncation rule, detection result |
| 공격자 목표 | 긴 context 내부의 악성 지시문 은닉, 민감정보 유출, 감사 우회, context flooding, low-salience injection |
| 공격자 능력 | 긴 입력 삽입, 문서 위치 조작, 악성 지시문을 낮은 attention 위치에 배치, retrieval 문서 오염, context window 소모 |
| 공격 경로 | long input → tokenization → efficient attention/truncation/memory → detection miss 또는 unsafe output |
| 방어자 능력 | context coverage 측정, source tracing, retrieval filtering, chunk prioritization, sensitive token scan, monitoring, audit log |
| 제외 범위 | 실제 서비스 무단 prompt injection, 개인정보 포함 로그 사용, 공격 prompt 제작 지원, 운영 시스템 침해 |

---

## 9. 평가방법 및 지표

| 평가축 | 지표 | 의미 | W04/P01 활용 |
|---|---|---|---|
| 비용 | latency, memory usage, throughput | 운영 가능성 | long-context serving 평가 |
| 성능 | utility, task accuracy, perplexity | 효율화 후 품질 유지 | baseline 비교 |
| 문맥 커버리지 | ContextCoverage | 보안 관련 token 포함 여부 | 탐지 누락 방지 |
| 근사 품질 | ApproxError | full attention 대비 차이 | 효율화 한계 평가 |
| 보안 탐지 | Recall_detect, FPR, FNR | 민감/악성 token 탐지 | 보안 필터 평가 |
| 프라이버시 | leakage rate, redaction miss | 민감정보 노출 | prompt/log 보안 |
| 운영성 | GPU memory, batch size, sequence length limit | 배포 가능성 | W14 연결 |
| 재현성 | model/config/data/prompt log | 결과 재현 가능성 | W15 연결 |

---

## 10. 재현성 체크리스트

| 항목 | 기록해야 할 내용 |
|---|---|
| Bibliographic status | DOI, ACM CSUR 출판정보, arXiv 판본 상태 |
| Data | 긴 synthetic prompt, 긴 로그, 긴 문서 toy corpus, train/test split |
| Model | full attention baseline, sparse/kernel/low-rank variant, checkpoint/hash |
| Attention config | sequence length, attention pattern, kernel feature map, memory size, truncation rule |
| Security input | 악성 지시문 위치, 민감정보 위치, retrieval source, chunk order |
| Evaluation | latency, memory, utility, ContextCoverage, ApproxError, Recall_detect, leakage rate |
| Environment | GPU/CPU, Python/framework version, dependency lock, seed |
| Evidence | config, raw prompt, output log, metric CSV/JSON, script commit |
| Limitation | toy long-context 결과를 실제 LLM 보안성으로 과장하지 않음 |
| GitHub math | `\operatorname` 사용 금지, `\mathrm{softmax}`·`\mathrm{sim}` 형태 사용 |

---

## 11. 논문의 고유 기여

1. Efficient Transformer를 sparse, low-rank, kernelized, recurrence/memory 등 구조별 taxonomy로 정리했다.
2. Full attention의 quadratic complexity 병목과 이를 줄이는 주요 접근을 비교할 수 있게 했다.
3. Long-context NLP/RAG 보안 평가에서 latency, memory, context coverage가 독립 평가축이 되어야 함을 뒷받침한다.
4. 보안 직접 문헌은 아니지만, 긴 prompt·로그·RAG 문서 보안의 비용-효용 trade-off를 분석하는 근거가 된다.
5. W04 P04/P05의 NLP adversarial/privacy 논의와 W08 RAG prompt injection, W14 MLOps 운영성, W15 재현성 evidence chain으로 연결된다.

---

## 12. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 보안 직접성 부족 | NLP 공격·프롬프트 프라이버시를 직접 평가하지 않는다. | W04 P04/P05, W08 prompt injection 문헌과 결합 |
| 근사 품질 해석 복잡 | 효율화가 항상 보안성을 높이거나 낮추는 것은 아니다. | ContextCoverage, ApproxError, Recall_detect 병기 |
| 최신 LLM serving 미반영 | 최신 KV-cache, speculative decoding, long-context LLM serving은 추가 문헌 필요 | W07/W08/W14로 확장 |
| 실험 재현 비용 | 대규모 모델 long-context 실험은 비용이 크다. | toy corpus와 작은 모델 기준으로 제한 |
| Hardware dependency | 실제 latency/memory는 GPU, batch, kernel implementation에 의존 | 환경·hardware log 기록 |
| 저작권 관리 | PDF 원문을 public repo에 유지하면 권리 조건 검토가 필요하다. | DOI/서지/summary 중심 공개 검토 |

---

## 13. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | 긴 prompt와 긴 로그를 다루는 LLM/RAG 보안에서 비용과 문맥 커버리지가 중요하다는 문제의식 |
| 2장 관련연구 | Efficient Transformer taxonomy와 attention complexity 정리 |
| 3장 위협모형 | long prompt, log, RAG context, memory cache, truncation rule 보호 자산 정의 |
| 4장 연구방법 | full/sparse/kernel attention, ContextCoverage, ApproxError, Recall_detect, UtilityCostScore, LongContextRisk 지표 설계 |
| 5장 분석 | 입력 길이별 latency-memory-detection recall 비교표와 context coverage matrix 제시 |
| 6장 보안적 함의 | 보안 모듈의 운영 비용, 탐지 누락, 문맥 손실, 감사 가능성 해석 |
| 부록 | attention config, sequence length, raw prompt, output log, metric CSV/JSON 수록 |

---

## 14. 기말논문 연결 3문장

1. W04에서 기말논문에 반영할 개념: 긴 프롬프트와 긴 로그를 다루는 Transformer 보안 평가는 정확도뿐 아니라 attention 비용, memory, latency, context coverage를 함께 봐야 한다.
2. W04에서 기말논문에 반영할 표·그림·실험: full/sparse/kernel attention complexity 표, 입력 길이별 latency-memory 그래프, ContextCoverage와 Recall_detect 평가표를 반영한다.
3. W04가 W15 최종 제출과 연결되는 지점: Efficient Transformer 실험은 sequence length, attention pattern, truncation rule, model config, raw prompt/output, metric CSV를 evidence chain으로 남겨야 재현성과 신뢰성을 확보할 수 있다.

---

## 15. 최종 판단

P01은 W04의 Efficient Transformer 핵심 문헌이다. 이 논문은 보안 직접 문헌은 아니지만, 긴 입력을 처리해야 하는 LLM/RAG/NLP 보안 시스템에서 attention 비용과 문맥 커버리지 문제가 왜 중요한지 설명한다. 따라서 기말논문에서는 P01을 **long-context Transformer, attention efficiency, latency-memory-cost 평가, context coverage, RAG/prompt 보안 운영성의 근거 문헌**으로 사용하는 것이 적절하다.

---

## 16. GitHub 수식 호환성 메모

이 파일에서는 GitHub 수식 렌더링 오류 방지를 위해 `\operatorname`을 사용하지 않는다.

| 피해야 할 표현 | 권장 표현 |
|---|---|
| `\operatorname{softmax}` | `\mathrm{softmax}` |
| `\operatorname{sim}` | `\mathrm{sim}` |
| `\operatorname{argmax}` | `\mathrm{argmax}` 또는 `\arg\max` |

```bash
pandoc P01_summary.md -o P01_summary.docx
pandoc P01_summary.md -o P01_summary.pdf --pdf-engine=xelatex
```
