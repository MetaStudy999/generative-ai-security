# P01 Summary

## Efficient Transformers: A Survey — Yi Tay, Mostafa Dehghani, Dara Bahri, Donald Metzler, ACM Computing Surveys, 2022

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W04 Transformer 변형 & NLP 대적공격·프라이버시 |
| 논문명 | Efficient Transformers: A Survey |
| 저자 | Yi Tay, Mostafa Dehghani, Dara Bahri, Donald Metzler |
| 학술지 | ACM Computing Surveys |
| 권호/쪽 | Vol. 55, No. 6, pp. 1–28 |
| 연도 | 2022 |
| DOI | https://doi.org/10.1145/3530811 |
| 보조 URL | https://arxiv.org/abs/2009.06732 |
| 논문 유형 | Survey / Efficient Attention and X-former Review |
| 로컬 PDF | `01_papers/pdf/01_Tay_et_al_2022_Efficient_Transformers_Survey.pdf` |
| 강의계획서 지정 논문과 일치 여부 | 일치 |
| 핵심 근거 사용 가능 여부 | 가능 |
| 검증 메모 | W04 `paper_list.md` 기준 ACM CSUR 출판 DOI 확인. Article 번호는 추가 확인 메모 |

---

## 1. 한 문장 요약

이 논문은 Transformer self-attention의 $O(n^2)$ 시간·메모리 병목을 줄이기 위해 제안된 **sparse attention, low-rank approximation, kernelized attention, recurrence/memory, locality-sensitive hashing, compressed context** 계열 Efficient Transformer를 체계화하고, 긴 입력 기반 LLM/RAG/NLP 보안 평가에서 latency·memory·context coverage를 별도 지표로 관리해야 함을 보여주는 survey 논문이다.

---

## 2. 연구문제

> 긴 시퀀스에서 full self-attention의 계산량과 메모리를 줄이면서 task utility, long-context reasoning, approximation quality, 배포 가능성을 어느 수준까지 유지할 수 있는가?

| 번호 | 연구질문 |
|---|---|
| RQ1 | Full self-attention의 quadratic complexity 병목은 어떤 수식으로 설명되는가? |
| RQ2 | Sparse, low-rank, kernelized, recurrence/memory attention은 각각 어떤 방식으로 비용을 줄이는가? |
| RQ3 | 효율화된 attention은 긴 프롬프트, 긴 로그, RAG 문맥 처리에서 어떤 장점과 위험을 만드는가? |
| RQ4 | 보안 필터·프라이버시 마스킹·감사 로그 분석을 붙일 때 latency와 memory overhead를 어떻게 측정해야 하는가? |
| RQ5 | Efficient Transformer의 근사 오류가 보안 탐지 누락이나 context coverage 손실로 이어질 가능성은 어떻게 평가할 수 있는가? |

---

## 3. 핵심 이론 및 수식

> 수식은 GitHub, MS Word, PDF 변환 호환성을 위해 표 밖의 LaTeX block math로 작성한다.

### 3.1 Full Attention Complexity

Transformer self-attention은 길이 $n$의 sequence에서 모든 token pair를 비교한다.

$$
Attention(Q,K,V)=\operatorname{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V
$$

$$
Cost_{full}=O(n^2d)
$$

| 기호 | 의미 |
|---|---|
| $n$ | sequence length |
| $d$ | hidden dimension |
| $Q,K,V$ | query, key, value 행렬 |
| $d_k$ | key dimension |

### 보안적 의미

긴 입력을 처리할수록 비용이 $n^2$로 증가한다. 프롬프트 보안, 로그 감사, RAG 문서 검증처럼 긴 context를 다루는 작업에서는 보안 모듈이 계산 비용 때문에 생략될 수 있다.

---

### 3.2 Sparse Attention

Sparse attention은 각 token이 전체 token이 아니라 제한된 $k$개 token만 참조하도록 한다.

$$
Cost_{sparse}\approx O(nkd), \qquad k \ll n
$$

| 기호 | 의미 |
|---|---|
| $k$ | 각 token이 참조하는 제한된 key 수 |
| $Cost_{sparse}$ | sparse attention 계산 비용 |

### 보안적 의미

Sparse attention은 긴 입력 처리 비용을 줄이지만, 중요 보안 단서가 attention pattern 밖에 있으면 민감정보 탐지나 간접 인젝션 탐지가 누락될 수 있다. 따라서 context coverage와 detection recall을 함께 기록해야 한다.

---

### 3.3 Kernelized Attention

Softmax attention은 feature map $\phi(\cdot)$를 이용해 선형화할 수 있다.

$$
\operatorname{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V
\approx \phi(Q)\left(\phi(K)^TV\right)
$$

| 기호 | 의미 |
|---|---|
| $\phi(\cdot)$ | kernel 또는 random feature map |
| $Q,K,V$ | attention 입력 |

### 보안적 의미

Kernelized attention은 throughput을 높일 수 있지만, 근사 품질이 낮으면 long-context에서 중요한 정책 문장, 민감정보, 악성 지시문을 약하게 반영할 수 있다.

---

## 4. AI 원리 관점 분석

| 항목 | 분석 |
|---|---|
| Full Attention | 모든 token pair를 비교하여 전역 관계를 학습한다. 비용은 높지만 표현력은 강하다. |
| Sparse Attention | 선택된 token 연결만 계산해 비용을 줄인다. context coverage 관리가 중요하다. |
| Low-rank Approximation | attention matrix를 낮은 rank 구조로 근사한다. 근사 오류 평가가 필요하다. |
| Kernelized Attention | softmax attention을 선형 시간에 가깝게 계산하려는 접근이다. |
| Memory/Recurrence | 이전 문맥을 압축·재사용해 긴 입력 처리를 가능하게 한다. |
| Long-context Modeling | 긴 로그, 긴 문서, 긴 프롬프트를 처리할 수 있지만 보안 감사 비용이 커진다. |

---

## 5. 보안 이슈 관점 분석

| 보안 항목 | Efficient Transformer 관점 해석 |
|---|---|
| 기밀성 | 긴 prompt/log에 민감정보가 포함될수록 leakage surface가 증가한다. |
| 무결성 | 긴 context 안의 악성 지시문이나 오염 문서가 attention에 포함될 수 있다. |
| 가용성 | full attention 비용은 보안 필터와 감사 모듈의 운영 적용을 어렵게 만든다. |
| 책임성 | context truncation, attention pattern, memory reuse 정책을 기록해야 한다. |
| 운영 리스크 | 효율화 근사가 탐지 누락, context loss, long-context hallucination을 만들 수 있다. |

---

## 6. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 대상 | 긴 프롬프트, 로그, RAG 문서, system prompt, memory cache, attention context |
| 공격자 목표 | 긴 context 내부의 악성 지시문 은닉, 민감정보 유출, 감사 우회 |
| 공격자 능력 | 긴 입력 삽입, 문서 위치 조작, low-salience injection, context flooding |
| 공격 경로 | long input → efficient attention/truncation/memory → model output |
| 제외 범위 | 실제 서비스 무단 prompt injection, 개인정보 포함 로그 사용 |

---

## 7. 평가방법 및 지표

| 지표 | 의미 | W04/P01에서의 활용 |
|---|---|---|
| Latency | 입력 길이별 응답 지연 | 보안 필터 운영 가능성 |
| Memory Usage | attention 계산 메모리 | long-context 적용 가능성 |
| Context Coverage | 보안 관련 token이 처리 범위에 포함되는지 | 탐지 누락 방지 |
| Utility | downstream task 성능 | 효율화 후 품질 유지 |
| Detection Recall | 악성/민감 token 탐지율 | 보안 모듈 성능 |
| Leakage Rate | 민감정보 노출 비율 | 프라이버시 평가 |
| Approximation Error | full attention 대비 근사 차이 | 효율화 한계 평가 |

---

## 8. 재현성 점검

| 항목 | 점검 |
|---|---|
| 데이터 | 긴 synthetic prompt, 긴 로그, 긴 문서 toy corpus 사용 가능 |
| 모델 | full attention baseline과 efficient attention variant 비교 가능 |
| 설정 | sequence length, attention pattern, memory size, truncation rule 기록 |
| 평가 | latency, memory, utility, detection recall, leakage rate 분리 |
| 결과 파일 | 길이별 metric CSV/JSON, config, seed, runtime log 저장 |
| 한계 | toy long-context 결과를 실제 LLM 보안성으로 일반화하지 않는다 |

---

## 9. 논문의 고유 기여

1. Efficient Transformer를 구조별 taxonomy로 정리했다.
2. Attention complexity 병목과 이를 줄이는 주요 접근을 비교할 수 있게 했다.
3. Long-context NLP/RAG 보안 평가에서 latency, memory, context coverage가 독립 평가축이 되어야 함을 뒷받침한다.
4. 보안 직접 문헌은 아니지만 W04의 비용·확장성·운영성 평가 근거가 된다.

---

## 10. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 보안 직접성 부족 | NLP 공격·프롬프트 프라이버시를 직접 평가하지 않는다. | P04/P05와 결합한다. |
| 근사 품질 해석 복잡 | 효율화가 항상 보안성을 높이거나 낮추는 것은 아니다. | context coverage와 detection recall을 추가한다. |
| 최신 LLM serving 미반영 | 최신 KV-cache, speculative decoding, long-context LLM은 추가 문헌 필요 | W07/W08/W14로 확장한다. |
| 실험 재현 비용 | 대규모 모델 long-context 실험은 비용이 크다. | toy corpus와 작은 모델 기준으로 제한한다. |

---

## 11. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 2장 관련연구 | Efficient Transformer taxonomy와 attention complexity |
| 3장 위협모형 | 긴 prompt/log/context 기반 공격면 정의 |
| 4장 연구방법 | latency, memory, context coverage, leakage rate 평가 설계 |
| 5장 분석 | 입력 길이별 비용·탐지율 비교표 |
| 6장 보안적 함의 | 보안 모듈의 운영 비용과 감사 가능성 해석 |

---

## 12. 기말논문 연결 3문장

1. 이 주차에서 기말논문에 반영할 개념: 긴 프롬프트와 긴 로그를 다루는 Transformer 보안 평가는 정확도뿐 아니라 attention 비용, memory, latency, context coverage를 함께 봐야 한다.
2. 이 주차에서 기말논문에 반영할 표·그림·실험: full/sparse/kernel attention complexity 표, 입력 길이별 latency-memory 그래프, context coverage 평가표를 반영한다.
3. 이 주차가 RAG 문서 오염/LLM 보안 감사 프레임워크와 연결되는 지점: RAG는 긴 문서 context를 다루므로 Efficient Transformer의 비용·coverage 관점을 W08 문서 오염 탐지와 W14 운영 감사로 확장한다.

---

## 13. 최종 판단

P01은 W04의 AI 원리와 운영 비용 평가를 담당하는 핵심 배경 문헌이다. 직접 보안 문헌은 아니지만 P04/P05의 NLP robustness와 prompt privacy 평가를 실제 배포 가능한 수준으로 해석하게 해준다.

---

## 14. 변환 호환성 메모

```bash
pandoc P01_summary.md -o P01_summary.docx
pandoc P01_summary.md -o P01_summary.pdf --pdf-engine=xelatex
```
