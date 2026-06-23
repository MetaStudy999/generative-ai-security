# P02 Summary

## A Practical Survey on Faster and Lighter Transformers — Quentin Fournier, Gaetan Marceau Caron, Daniel Aloise, ACM Computing Surveys, 2023

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W04 Transformer 변형 & NLP 대적공격·프라이버시 |
| 논문명 | A Practical Survey on Faster and Lighter Transformers |
| 저자 | Quentin Fournier, Gaetan Marceau Caron, Daniel Aloise |
| 학술지 | ACM Computing Surveys |
| 권호/쪽 | Vol. 55, No. 14s, pp. 1–40 |
| 연도 | 2023 |
| DOI | https://doi.org/10.1145/3586074 |
| 보조 URL | https://arxiv.org/abs/2103.14636 |
| 논문 유형 | Practical Survey / Faster and Lighter Transformers Review |
| 로컬 PDF | `01_papers/pdf/02_Fournier_et_al_2023_Faster_Lighter_Transformers_Survey.pdf` |
| 강의계획서 지정 논문과 일치 여부 | 일치 |
| 핵심 근거 사용 가능 여부 | 가능 |
| 검증 메모 | W04 `paper_list.md` 기준 ACM CSUR 출판 DOI 확인. Article 번호는 추가 확인 메모 |

---

## 1. 한 문장 요약

이 논문은 Transformer를 실제 배포 환경에서 더 빠르고 가볍게 만들기 위한 **distillation, pruning, quantization, low-rank/kernel approximation, efficient architecture, caching, early exit, inference optimization** 전략을 실용적으로 정리하고, NLP 보안 방어가 utility와 latency/cost trade-off 안에서 평가되어야 함을 보여주는 survey 논문이다.

---

## 2. 연구문제

> Transformer의 task utility를 크게 훼손하지 않으면서 parameter count, memory footprint, inference latency, energy cost를 어떻게 줄일 수 있으며, 이 효율화가 보안 필터·프라이버시 보호·로그 감사의 운영 가능성에 어떤 영향을 주는가?

| 번호 | 연구질문 |
|---|---|
| RQ1 | Faster/lighter Transformer를 만드는 대표 기법은 무엇인가? |
| RQ2 | Distillation, pruning, quantization은 utility와 cost를 어떻게 바꾸는가? |
| RQ3 | Efficient architecture와 inference optimization은 실시간 NLP 시스템에 어떤 이점을 주는가? |
| RQ4 | 보안 방어 모듈이 너무 무겁거나 느릴 때 어떤 운영 리스크가 발생하는가? |
| RQ5 | 경량화가 robustness, privacy leakage, over-refusal, auditability에 미치는 영향은 어떻게 평가할 수 있는가? |

---

## 3. 핵심 이론 및 수식

### 3.1 Utility-Cost Objective

경량 Transformer는 성능과 비용을 함께 최적화해야 한다.

$$
Score = Utility - \lambda_1 Latency - \lambda_2 Memory - \lambda_3 Size - \lambda_4 Energy
$$

| 기호 | 의미 |
|---|---|
| $Utility$ | accuracy, F1, BLEU, ROUGE, task success 등 품질 지표 |
| $Latency$ | 추론 지연시간 |
| $Memory$ | 추론 또는 학습 메모리 사용량 |
| $Size$ | 모델 크기 또는 파라미터 수 |
| $Energy$ | 에너지 비용 |
| $\lambda_i$ | 비용 항목의 가중치 |

### 보안적 의미

프롬프트 마스킹, 민감정보 탐지, NLP adversarial defense, 로그 감사 모듈은 비용이 크면 실제 운영 경로에서 빠질 수 있다. 따라서 보안성 평가는 utility와 함께 latency/cost evidence를 포함해야 한다.

---

### 3.2 Compression Ratio

모델 경량화의 효과는 원본 대비 모델 크기 축소로 표현할 수 있다.

$$
CompressionRatio=\frac{Size_{original}}{Size_{compressed}}
$$

| 기호 | 의미 |
|---|---|
| $Size_{original}$ | 압축 전 모델 크기 |
| $Size_{compressed}$ | 압축 후 모델 크기 |

### 보안적 의미

Compression ratio가 높아도 robustness나 privacy safety가 유지된다는 보장은 없다. pruning이나 quantization이 rare token, 민감정보 탐지, adversarial input 대응에 영향을 줄 수 있기 때문이다.

---

### 3.3 Knowledge Distillation

Teacher 모델의 출력 분포를 student 모델이 모방하도록 학습할 수 있다.

$$
\mathcal{L}_{KD}=T^2 \cdot KL\left(\operatorname{softmax}(z_T/T)\;\|\;\operatorname{softmax}(z_S/T)\right)
$$

| 기호 | 의미 |
|---|---|
| $z_T$ | teacher model logits |
| $z_S$ | student model logits |
| $T$ | temperature |
| $KL(\cdot\|\cdot)$ | Kullback-Leibler divergence |

### 보안적 의미

Student 모델이 teacher의 취약성, 편향, 민감정보 처리 습관까지 모방할 수 있다. 따라서 distillation 후에는 clean utility뿐 아니라 adversarial robustness와 privacy leakage도 다시 평가해야 한다.

---

## 4. AI 원리 관점 분석

| 항목 | 분석 |
|---|---|
| Distillation | 큰 모델의 지식을 작은 모델로 이전한다. |
| Pruning | 중요도가 낮은 weight, head, layer를 제거한다. |
| Quantization | 낮은 정밀도 연산으로 메모리와 계산량을 줄인다. |
| Low-rank/Kernel | attention 또는 layer를 근사하여 비용을 줄인다. |
| Early Exit | 쉬운 입력은 중간 layer에서 조기 종료한다. |
| Caching | 반복 계산을 줄여 추론 효율을 높인다. |
| Deployment | edge, mobile, API server, cloud inference 환경 제약을 고려한다. |

---

## 5. 보안 이슈 관점 분석

| 보안 항목 | Faster/Lighter Transformer 관점 해석 |
|---|---|
| 무결성 | 경량화 후 adversarial input에 대한 robust 성능이 변할 수 있다. |
| 기밀성 | 압축 모델이 민감정보 탐지 성능을 잃으면 leakage가 증가할 수 있다. |
| 가용성 | 경량화는 서비스 지연을 줄여 방어 모듈 적용 가능성을 높인다. |
| 책임성 | 모델 압축 설정, quantization bit, pruning ratio, distillation data를 기록해야 한다. |
| 운영 리스크 | 경량화로 비용은 줄지만 보안 탐지율·정책 준수율이 떨어질 수 있다. |

---

## 6. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 대상 | 경량 Transformer, 보안 필터, prompt privacy wrapper, inference pipeline |
| 공격자 목표 | 경량 모델의 탐지 약점 이용, 우회 표현 삽입, 민감정보 노출 유도 |
| 공격자 능력 | adversarial text 입력, 긴 prompt 삽입, rare token 이용, 반복 질의 |
| 공격 경로 | user text → lightweight model/filter → policy/output decision |
| 제외 범위 | 실제 운영 API 무단 공격, 개인정보 포함 prompt 사용 |

---

## 7. 평가방법 및 지표

| 지표 | 의미 | W04/P02에서의 활용 |
|---|---|---|
| Utility | task 성능 | 경량화 후 성능 유지 |
| Latency | 응답 지연 | 실시간 prompt 검사 가능성 |
| Throughput | 단위 시간 처리량 | 대량 로그 감사 가능성 |
| Memory | 메모리 사용량 | 온디바이스/저비용 배포 |
| Model Size | 모델 파일 크기 | 배포·운영 비용 |
| Robust Accuracy | 공격 조건 성능 | NLP 방어 성능 |
| Leakage Rate | 민감정보 노출률 | prompt privacy 평가 |
| Over-refusal | 정상 요청 과차단 | utility 손실 평가 |

---

## 8. 재현성 점검

| 항목 | 점검 |
|---|---|
| 모델 | original, distilled, pruned, quantized variant 구분 |
| 설정 | pruning ratio, quantization bit, distillation temperature 기록 |
| 데이터 | clean task data, adversarial text set, privacy-risk prompt set 분리 |
| 평가 | utility, latency, memory, robust accuracy, leakage rate 함께 측정 |
| 환경 | CPU/GPU, batch size, library version 기록 |
| 한계 | toy/small model 결과를 대규모 LLM serving 성능으로 일반화하지 않음 |

---

## 9. 논문의 고유 기여

1. Transformer 효율화 기법을 실제 배포 관점에서 실용적으로 정리했다.
2. 모델 크기, 속도, 메모리, 비용을 task utility와 함께 비교할 수 있는 관점을 제공한다.
3. W04에서 보안 방어가 실제 운영 경로에 들어갈 수 있는지 판단하는 비용 평가 근거가 된다.
4. Prompt privacy와 NLP robustness 평가에 latency/cost/audit overhead 지표를 추가하는 근거를 제공한다.

---

## 10. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 보안 직접성 부족 | NLP adversarial attack이나 prompt privacy가 중심은 아니다. | P04/P05와 결합한다. |
| 경량화-보안 관계 미확정 | 압축이 보안성을 항상 높이거나 낮추지는 않는다. | robust/leakage 재평가를 의무화한다. |
| LLM 최신 serving 미반영 | 최신 quantized LLM, KV-cache, speculative decoding은 추가 문헌 필요 | W07/W14와 연결한다. |
| 하드웨어 의존성 | latency와 memory는 환경에 따라 달라진다. | 실험환경을 표준화해 기록한다. |

---

## 11. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 2장 관련연구 | Transformer 경량화·압축·배포 최적화 정리 |
| 3장 위협모형 | lightweight filter 우회, deployment constraint 공격면 정의 |
| 4장 연구방법 | utility-latency-memory-leakage 다중지표 평가 설계 |
| 5장 분석 | 경량 보안 필터의 utility/cost trade-off 표 |
| 6장 보안적 함의 | 방어 비용과 운영 적용 가능성 해석 |

---

## 12. 기말논문 연결 3문장

1. 이 주차에서 기말논문에 반영할 개념: Transformer 보안 방어는 정확도뿐 아니라 latency, memory, model size, audit cost까지 포함해 평가해야 한다.
2. 이 주차에서 기말논문에 반영할 표·그림·실험: utility-cost score, compression ratio, distillation loss, utility-latency-leakage 비교표를 반영한다.
3. 이 주차가 RAG 문서 오염/LLM 보안 감사 프레임워크와 연결되는 지점: RAG/LLM 운영환경에서는 prompt 검사, 문서 필터링, 로그 감사가 비용을 만들기 때문에 P02의 practical efficiency 지표를 W08/W14의 운영 평가로 확장한다.

---

## 13. 최종 판단

P02는 W04에서 보안 방어의 실용성 평가를 담당한다. P01이 attention 구조 비용을 설명한다면, P02는 실제 배포에서 pruning, quantization, distillation, inference optimization이 보안 평가에 어떻게 들어와야 하는지 설명한다.

---

## 14. 변환 호환성 메모

```bash
pandoc P02_summary.md -o P02_summary.docx
pandoc P02_summary.md -o P02_summary.pdf --pdf-engine=xelatex
```
