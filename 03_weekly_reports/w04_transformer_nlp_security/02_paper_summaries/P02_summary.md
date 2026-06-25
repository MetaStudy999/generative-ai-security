# P02 Summary

## A Practical Survey on Faster and Lighter Transformers — Quentin Fournier, Gaetan Marceau Caron, Daniel Aloise, ACM Computing Surveys, 2023

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W04 Transformer 변형 & NLP 대적공격·프라이버시 |
| 논문명 | A Practical Survey on Faster and Lighter Transformers |
| 저자 | Quentin Fournier, Gaetan Marceau Caron, Daniel Aloise |
| 공식 출판 정보 | ACM Computing Surveys, Vol. 55, No. 14s, pp. 1–40, 2023 |
| DOI | https://doi.org/10.1145/3586074 |
| 보조 URL | https://arxiv.org/abs/2103.14636 |
| 논문 유형 | Practical Survey / Faster and Lighter Transformers Review |
| 로컬 PDF | `01_papers/pdf/02_Fournier_et_al_2023_Faster_Lighter_Transformers_Survey.pdf` |
| 검증 상태 | W04 `paper_list.md` 기준 ACM CSUR 출판 DOI 확인. `download_source.md` 기준 로컬 PDF 파일명과 DOI/arXiv 출처가 대응됨 |
| PDF 확인 메모 | repo의 PDF 폴더에 P02 관련 PDF blob이 존재함을 확인했다. 요약은 로컬 PDF 경로와 W04 `paper_list.md`, `download_source.md`의 공식 DOI/arXiv 메타데이터 기준으로 보완했다. |
| 수식 호환성 | GitHub 수식 렌더링 오류 방지를 위해 `\operatorname`을 사용하지 않고 `\mathrm{...}` 형태로 작성했다. |
| 핵심 근거 사용 가능 여부 | 가능. W04에서 transformer 경량화, distillation, pruning, quantization, low-rank/kernel approximation, early exit, caching, inference optimization, 보안 필터 운영 비용 평가의 핵심 문헌으로 사용 |

---

## 1. 한 문장 요약

이 논문은 Transformer를 실제 배포 환경에서 더 빠르고 가볍게 만들기 위한 **knowledge distillation, pruning, quantization, weight sharing, low-rank approximation, efficient architecture, early exit, caching, inference optimization, hardware-aware deployment** 전략을 실용적으로 정리하며, W04에서는 NLP 보안 방어와 prompt privacy 모듈을 **정확도뿐 아니라 latency, memory, model size, throughput, energy, robustness, leakage rate, auditability**까지 포함해 평가해야 함을 보여주는 핵심 survey 문헌이다.

---

## 2. 핵심 연구문제

> Transformer 기반 모델은 성능이 높지만, 큰 parameter 수와 높은 추론 비용 때문에 실제 서비스에 적용하기 어렵다. Faster and lighter Transformer 연구의 핵심은 task utility를 크게 훼손하지 않으면서도 latency, memory, model size, energy cost를 줄이는 것이다. 보안 관점에서는 경량화가 보안 필터의 운영 적용 가능성을 높일 수 있지만, 동시에 rare token 탐지, adversarial robustness, privacy leakage, over-refusal, auditability를 약화시킬 수 있다.

| 번호 | 연구질문 |
|---|---|
| RQ1 | Transformer를 더 빠르고 가볍게 만드는 대표 기법은 무엇이며, 각각 어떤 비용 항목을 줄이는가? |
| RQ2 | Distillation, pruning, quantization, low-rank approximation은 utility와 cost의 trade-off를 어떻게 바꾸는가? |
| RQ3 | 경량화된 Transformer는 실시간 NLP 보안 필터, prompt privacy wrapper, 로그 감사 시스템에 어떤 운영 이점을 주는가? |
| RQ4 | 경량화가 robustness, privacy leakage, rare token handling, over-refusal, auditability에 미치는 영향은 어떻게 평가해야 하는가? |
| RQ5 | 기말논문에서 lightweight security model을 사용할 경우 model variant, compression setting, evaluation metric, runtime log를 어떻게 evidence chain에 남겨야 하는가? |

---

## 3. 논문의 핵심 기여

| 기여 | 설명 | W04 연결 |
|---|---|---|
| Practical transformer efficiency taxonomy | 빠르고 가벼운 Transformer를 만드는 실용 기법들을 정리 | W04 P02 핵심 |
| Compression 관점 제공 | distillation, pruning, quantization, low-rank 등 모델 압축 기법 비교 | 운영 비용 절감 평가 |
| Inference optimization 강조 | early exit, caching, batching, hardware-aware inference 등 deployment 관점 포함 | MLOps/serving 연결 |
| Utility-cost trade-off 정리 | task utility와 latency, memory, size, energy를 함께 평가해야 함을 제시 | 기말논문 평가 지표 |
| 보안 확장 가능성 | 보안 필터와 privacy wrapper도 성능·비용·누락률을 함께 평가해야 함 | NLP 보안 운영성 |

---

## 4. 목차별 핵심 개괄

| 목차 | 핵심 내용 | 비전공자용 이해 |
|---|---|---|
| 1. Introduction | Transformer는 성능이 높지만 크고 느리며, 실제 배포에는 경량화가 필요하다. | 좋은 모델이어도 너무 느리면 서비스에 쓰기 어렵다. |
| 2. Background | Transformer 구조, self-attention, feed-forward layer, parameter/memory/latency 비용을 설명한다. | 모델이 커지는 이유와 느려지는 지점을 파악한다. |
| 3. Knowledge Distillation | 큰 teacher model의 지식을 작은 student model에 전달한다. | 큰 모델을 선생님으로 삼아 작은 모델을 학습시킨다. |
| 4. Pruning | 중요도가 낮은 weight, head, neuron, layer를 제거한다. | 덜 중요한 부분을 잘라 모델을 가볍게 만든다. |
| 5. Quantization | FP32보다 낮은 bit precision으로 연산과 저장 비용을 줄인다. | 숫자를 더 적은 비트로 표현해 빠르고 작게 만든다. |
| 6. Efficient Architectures | parameter sharing, low-rank, sparse/linear attention, compact layer 설계를 다룬다. | 처음부터 가볍게 설계하는 방법이다. |
| 7. Inference Optimization | caching, early exit, batching, hardware-specific optimization을 정리한다. | 같은 모델이라도 실행 방식을 바꾸면 빨라질 수 있다. |
| 8. Evaluation | accuracy, latency, memory, throughput, model size, energy, deployment constraint를 함께 평가한다. | 점수만 보지 말고 실제 운영 비용도 봐야 한다. |
| 9. Challenges | 압축 후 성능 저하, hardware dependency, task transfer, robustness, reproducibility 문제가 남는다. | 가볍게 만들수록 놓치는 것이 생길 수 있다. |
| 보안 연결 | 경량화는 보안 모듈 적용 가능성을 높이지만 탐지 누락과 leakage 증가를 만들 수 있다. | 빠른 보안 필터도 정확하고 안전해야 한다. |

---

## 5. 핵심 이론 및 수식

> 수식은 GitHub Markdown/KaTeX 호환성을 우선한다. `\operatorname` 매크로는 사용하지 않고 `\mathrm{...}` 형태로 작성한다.

### 5.1 Utility-Cost Objective

경량 Transformer는 성능과 비용을 함께 최적화해야 한다.

$$
Score=Utility-\lambda_1Latency-\lambda_2Memory-\lambda_3Size-\lambda_4Energy
$$

| 기호 | 의미 |
|---|---|
| $Utility$ | accuracy, F1, BLEU, ROUGE, task success 등 품질 지표 |
| $Latency$ | 추론 지연시간 |
| $Memory$ | 추론 또는 학습 메모리 사용량 |
| $Size$ | 모델 크기 또는 파라미터 수 |
| $Energy$ | 에너지 비용 |

### 보안적 의미

프롬프트 마스킹, 민감정보 탐지, NLP adversarial defense, 로그 감사 모듈은 비용이 크면 실제 운영 경로에서 빠질 수 있다. 따라서 보안성 평가는 utility와 함께 latency/cost evidence를 포함해야 한다.

---

### 5.2 Compression Ratio

모델 경량화의 효과는 원본 대비 모델 크기 축소로 표현할 수 있다.

$$
CompressionRatio=\frac{Size_{original}}{Size_{compressed}}
$$

### 보안적 의미

Compression ratio가 높아도 robustness나 privacy safety가 유지된다는 보장은 없다. pruning이나 quantization은 rare token, 민감정보 탐지, adversarial input 대응에 영향을 줄 수 있다.

---

### 5.3 Knowledge Distillation Loss

Teacher 모델의 출력 분포를 student 모델이 모방하도록 학습할 수 있다.

$$
\mathcal{L}_{KD}=T^2\cdot\mathrm{KL}\left(\mathrm{softmax}(z_T/T)\;\|\;\mathrm{softmax}(z_S/T)\right)
$$

| 기호 | 의미 |
|---|---|
| $z_T$ | teacher model logits |
| $z_S$ | student model logits |
| $T$ | temperature |
| $\mathrm{KL}$ | Kullback-Leibler divergence |

### 보안적 의미

Student 모델은 teacher의 지식뿐 아니라 취약성, 편향, 민감정보 처리 습관도 모방할 수 있다. Distillation 후에는 clean utility뿐 아니라 adversarial robustness와 privacy leakage도 다시 평가해야 한다.

---

### 5.4 Pruning Ratio

모델에서 제거한 parameter 또는 구조 비율이다.

$$
PruningRatio=1-\frac{Params_{pruned}}{Params_{original}}
$$

### 보안적 의미

Head 또는 layer pruning이 특정 보안 token, rare phrase, 정책 위반 패턴 탐지를 약화시킬 수 있다.

---

### 5.5 Quantization Error

낮은 정밀도 표현이 원래 weight와 얼마나 다른지 측정한다.

$$
QuantError=\frac{\|W-W_q\|_F}{\|W\|_F+\epsilon}
$$

| 기호 | 의미 |
|---|---|
| $W$ | 원래 weight |
| $W_q$ | quantized weight |
| $\epsilon$ | 0 나눗셈 방지 상수 |

### 보안적 의미

Quantization error가 크면 decision boundary가 변할 수 있고, 안전 필터의 정상/위험 판정 경계도 흔들릴 수 있다.

---

### 5.6 Security Utility Score

경량화된 보안 모델은 일반 성능, 보안 탐지율, privacy leakage, over-refusal을 함께 평가해야 한다.

$$
SecurityUtility=Utility+\alpha Recall_{detect}-\beta LeakageRate-\gamma OverRefusal
$$

### 보안적 의미

보안 필터는 단순히 작고 빠른 모델이면 충분하지 않다. 탐지율이 낮거나 민감정보 누출이 커지면 운영상 부적합하다.

---

### 5.7 Lightweight Deployment Score

경량 모델의 배포 적합성을 성능·보안·비용 측면에서 종합한다.

$$
DeployScore=SecurityUtility-\lambda Latency-\mu Memory-\nu ModelSize
$$

### 보안적 의미

최종 채택 모델은 정확도뿐 아니라 latency, memory, model size, detection recall, leakage rate를 함께 만족해야 한다.

---

### 5.8 Lightweight Security Risk

경량화로 인한 보안 위험을 요약한다.

$$
LightweightRisk=RobustDrop+LeakageIncrease+RareTokenMiss+AuditGap-DeploymentGain
$$

### 보안적 의미

경량화는 운영성을 높이지만, robustness 저하·leakage 증가·rare token 탐지 실패·감사 로그 부족을 초래할 수 있다.

---

## 6. AI 원리 70% 관점 분석

| 원리 항목 | 설명 | W04/P02에서의 의미 |
|---|---|---|
| Distillation | 큰 모델의 지식을 작은 모델로 이전 | 경량화 핵심 기법 |
| Pruning | 중요도가 낮은 weight, head, layer 제거 | model size 감소 |
| Quantization | 낮은 정밀도 연산으로 메모리와 계산량 절감 | edge/mobile 배포 |
| Low-rank/Kernel | attention 또는 layer를 근사해 비용 절감 | efficient architecture |
| Early Exit | 쉬운 입력은 중간 layer에서 조기 종료 | latency 감소 |
| Caching | 반복 계산을 줄여 추론 효율 향상 | serving 최적화 |
| Deployment Constraint | CPU/GPU/edge/cloud 환경 제약 고려 | 운영성 평가 |
| Utility-Cost Trade-off | 성능과 비용을 함께 최적화 | 보안 시스템 평가 기준 |

---

## 7. 보안 이슈 30% 관점 분석

| 보안 항목 | Faster/Lighter Transformer 관점 해석 | 대표 평가 지표 |
|---|---|---|
| 기밀성 | 경량 모델이 민감정보 탐지 성능을 잃으면 leakage 증가 | LeakageRate, redaction miss |
| 무결성 | 경량화 후 adversarial input에 대한 robust 성능이 달라질 수 있음 | RobustDrop, ASR |
| 가용성 | 경량화는 서비스 지연을 줄여 보안 필터 적용 가능성을 높임 | latency, throughput |
| 프라이버시 | distillation data와 model output이 privacy signal을 유지할 수 있음 | privacy leakage test |
| 안전성 | quantization/pruning으로 policy boundary가 불안정해질 수 있음 | unsafe response rate |
| 책임성 | 압축 설정, quantization bit, pruning ratio, distillation data를 기록해야 감사 가능 | config completeness |

---

## 8. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 대상 | 경량 Transformer, student model, compressed weights, quantized weights, security filter, prompt privacy wrapper, inference pipeline |
| 공격자 목표 | 경량 모델의 탐지 약점 이용, 우회 표현 삽입, rare token 악용, 민감정보 노출 유도, 과차단 유도 |
| 공격자 능력 | adversarial text 입력, 긴 prompt 삽입, rare token 사용, 반복 질의, paraphrase 우회, prompt privacy wrapper 우회 시도 |
| 공격 경로 | user text → lightweight model/filter → policy decision 또는 output decision → leakage/unsafe answer |
| 방어자 능력 | robust evaluation, privacy test, red-teaming, logging, fallback to larger model, human review, deployment monitoring |
| 제외 범위 | 실제 운영 API 무단 공격, 개인정보 포함 prompt 사용, 악성 prompt 제작 지원, 모델 우회 절차 제공 |

---

## 9. 평가방법 및 지표

| 평가축 | 지표 | 의미 | W04/P02 활용 |
|---|---|---|---|
| 일반 성능 | Utility, accuracy, F1 | 경량화 후 task 성능 | baseline 비교 |
| 속도 | latency, throughput | 실시간 prompt 검사 가능성 | 운영성 |
| 자원 | memory, model size, energy | 온디바이스/저비용 배포 | cost 평가 |
| 압축 품질 | CompressionRatio, PruningRatio, QuantError | 경량화 정도와 손실 | 방법 비교 |
| 보안 강건성 | robust accuracy, ASR, RobustDrop | 공격 조건 성능 | NLP defense 평가 |
| 프라이버시 | LeakageRate, redaction miss | 민감정보 노출률 | prompt privacy 평가 |
| 사용자 영향 | OverRefusal, false block rate | 정상 요청 과차단 | utility 손실 |
| 재현성 | config, model hash, quantization bit, pruning log | 결과 재현 가능성 | W15 연결 |

---

## 10. 재현성 체크리스트

| 항목 | 기록해야 할 내용 |
|---|---|
| Bibliographic status | DOI, ACM CSUR 출판정보, arXiv 판본 상태, 로컬 PDF 상태 |
| Model variants | original, distilled, pruned, quantized, early-exit variant 구분 |
| Compression config | pruning ratio, quantization bit, distillation temperature, teacher/student model |
| Data | clean task data, adversarial text set, privacy-risk prompt set, distillation data |
| Evaluation | utility, latency, throughput, memory, model size, RobustDrop, LeakageRate, OverRefusal |
| Environment | CPU/GPU, batch size, sequence length, runtime library, framework version |
| Security tests | rare token, paraphrase, adversarial text, privacy masking, prompt leakage test |
| Evidence | config file, model hash, runtime log, metric CSV/JSON, script commit |
| Limitation | toy/small model 결과를 대규모 LLM serving 성능으로 일반화하지 않음 |
| GitHub math | `\operatorname` 사용 금지, `\mathrm{softmax}`·`\mathrm{KL}` 형태 사용 |

---

## 11. 논문의 고유 기여

1. Transformer 효율화 기법을 실제 배포 관점에서 실용적으로 정리했다.
2. 모델 크기, 속도, 메모리, 에너지, latency를 task utility와 함께 비교할 수 있는 관점을 제공한다.
3. W04에서 보안 방어가 실제 운영 경로에 들어갈 수 있는지 판단하는 비용 평가 근거가 된다.
4. Prompt privacy와 NLP robustness 평가에 latency/cost/audit overhead 지표를 추가하는 근거를 제공한다.
5. W07 LLM, W08 RAG prompt injection, W14 MLOps deployment, W15 reproducibility와 연결되는 운영성 문헌이다.

---

## 12. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 보안 직접성 부족 | NLP adversarial attack이나 prompt privacy가 중심은 아니다. | W04 P04/P05와 결합 |
| 경량화-보안 관계 미확정 | 압축이 보안성을 항상 높이거나 낮추지는 않는다. | robust/leakage 재평가를 의무화 |
| LLM 최신 serving 미반영 | 최신 quantized LLM, KV-cache, speculative decoding은 추가 문헌 필요 | W07/W14와 연결 |
| 하드웨어 의존성 | latency와 memory는 CPU/GPU, batch size, kernel implementation에 따라 달라진다. | 실험환경을 표준화해 기록 |
| Distillation risk | teacher 취약성과 편향이 student에 전이될 수 있다. | teacher/student 비교와 red-team 평가 추가 |
| 저작권 관리 | PDF 원문을 public repo에 유지하면 권리 조건 검토가 필요하다. | DOI/서지/summary 중심 공개 검토 |

---

## 13. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | AI 보안 방어는 정확도뿐 아니라 비용과 배포 가능성까지 고려해야 한다는 문제의식 |
| 2장 관련연구 | Transformer 경량화·압축·배포 최적화 문헌으로 P02 정리 |
| 3장 위협모형 | lightweight filter 우회, compressed model leakage, deployment constraint 공격면 정의 |
| 4장 연구방법 | Utility-Cost, CompressionRatio, KD loss, PruningRatio, QuantError, SecurityUtility, DeployScore 지표 설계 |
| 5장 분석 | 경량 보안 필터의 utility-latency-memory-leakage 비교표 제시 |
| 6장 보안적 함의 | 방어 비용, 운영 적용 가능성, 경량화 후 탐지 누락·leakage 증가 위험 해석 |
| 부록 | compression config, model hash, latency/memory log, privacy/security test result 수록 |

---

## 14. 기말논문 연결 3문장

1. W04에서 기말논문에 반영할 개념: Transformer 보안 방어는 정확도뿐 아니라 latency, memory, model size, audit cost까지 포함해 평가해야 실제 운영 가능성을 판단할 수 있다.
2. W04에서 기말논문에 반영할 표·그림·실험: Utility-Cost score, CompressionRatio, KD loss, PruningRatio, QuantError, SecurityUtility, DeployScore 수식표와 utility-latency-leakage 비교표를 반영한다.
3. W04가 W15 최종 제출과 연결되는 지점: compressed model variant, pruning/quantization/distillation 설정, runtime environment, latency/memory 결과, leakage/robustness 평가를 evidence chain으로 남겨야 재현성과 신뢰성을 확보할 수 있다.

---

## 15. 최종 판단

P02는 W04의 faster/lighter Transformer 핵심 문헌이다. 이 논문은 보안 직접 문헌은 아니지만, 보안 필터와 prompt privacy wrapper가 실제 서비스에 들어가기 위해 필요한 속도·메모리·모델 크기·비용 평가의 근거를 제공한다. 따라서 기말논문에서는 P02를 **Transformer 경량화, 보안 필터 운영성, latency-memory-utility trade-off, 압축 후 robustness/privacy 재평가의 근거 문헌**으로 사용하는 것이 적절하다.

---

## 16. GitHub 수식 호환성 메모

이 파일에서는 GitHub 수식 렌더링 오류 방지를 위해 `\operatorname`을 사용하지 않는다.

| 피해야 할 표현 | 권장 표현 |
|---|---|
| `\operatorname{softmax}` | `\mathrm{softmax}` |
| `\operatorname{KL}` | `\mathrm{KL}` |
| `\operatorname{argmax}` | `\mathrm{argmax}` 또는 `\arg\max` |

```bash
pandoc P02_summary.md -o P02_summary.docx
pandoc P02_summary.md -o P02_summary.pdf --pdf-engine=xelatex
```
