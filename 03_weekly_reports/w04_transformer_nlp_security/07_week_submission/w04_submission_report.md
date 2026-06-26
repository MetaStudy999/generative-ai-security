# W04 제출용 단일 보고서

## Transformer 변형 & NLP 대적공격·프라이버시

## 0. 메타정보

| 항목 | 내용 |
|---|---|
| 주차 | W04 |
| 보고서 제목 | Transformer 변형 & NLP 대적공격·프라이버시 |
| 과목 범위 | AI 보안 |
| 작성자 | 박영세 |
| 학번 | 26200122 |
| 작성일 | 2026-06-26 |
| 문서 상태 | 주차별 단일 제출용 보고서 |
| 원본 관리 파일 | `03_weekly_reports/w04_transformer_nlp_security/07_week_submission/w04_submission_report.md` |
| Word/PDF 제출본 권장 위치 | `03_weekly_reports/w04_transformer_nlp_security/07_week_submission/exports/` |
| 관련 산출물 위치 | `03_weekly_reports/w04_transformer_nlp_security/` |
| 안전 범위 | 실제 개인정보, 실제 서비스 프롬프트, 무단 API 질의, 악용 가능한 공격 절차 제외 |
| PDF 검토 상태 | P01~P05 로컬 PDF blob 존재 확인. 제출 본문은 DOI/URL, `paper_list.md`, 논문별 summary, 실험 보고서 기준으로 작성 |
| 제출 전 주의 | P01/P02/P04/P05의 ACM Article 번호는 최종 제출 전 출판사 페이지에서 추가 확인 필요. P04의 강의자료 `N. Goyal` 표기는 실제 제1저자 `Shreya Goyal`과 달라 사람 검토 필요 |

---

## 초록

본 보고서는 W04 주차의 Transformer 변형, NLP 대적공격, 프롬프트 프라이버시를 하나의 제출용 보고서로 통합한다. Transformer는 query, key, value 기반 self-attention을 통해 토큰 간 관계를 학습하지만, 긴 입력 처리에서 계산 복잡도와 메모리 비용이 커진다. Efficient Transformer와 Faster/Lighter Transformer 연구는 sparse attention, low-rank approximation, kernelized attention, distillation, pruning, quantization 등을 통해 비용을 줄이려는 접근을 정리한다. 그러나 NLP 보안 관점에서는 단어 치환, 문장 재구성, paraphrase, prompt leakage, ICL leakage, log exposure가 새로운 공격면이 된다. 본 보고서는 W04 논문 5편을 바탕으로 Transformer 효율화와 NLP/prompt security를 연결하고, synthetic privacy-risk prompt와 keyword privacy-risk detector를 사용한 안전한 toy protocol로 clean score, attack success rate, privacy leakage, utility score, reproducibility evidence를 분리 기록하였다. 실험 결과는 실제 Transformer 또는 LLM의 강건성·프라이버시 성능이 아니라 평가 구조를 설명하는 안전한 예시로 한정한다.

**키워드:** Transformer, Efficient Transformer, NLP adversarial attack, prompt privacy, ICL leakage, clean score, ASR, privacy leakage, utility, 재현성

---

## 1. 한 문장 요약

W04는 Transformer의 효율화 구조와 NLP 대적공격·prompt privacy를 연결해, 프롬프트 기반 AI 시스템을 clean score, ASR, privacy leakage, utility score, reproducibility evidence로 분리 평가하는 주차다.

---

## 2. 학습 배경과 주차 목표

### 2.1 이번 주 주제의 위치

W04는 W03의 Vision Transformer와 robust evaluation을 NLP Transformer와 프롬프트 기반 보안 문제로 확장하는 주차다. W03에서 이미지를 patch token으로 다루었다면, W04는 텍스트 token, 긴 context, prompt, ICL example, output log가 보안 자산이 되는 환경을 다룬다. 이 주차는 이후 W07 LLM 보안, W08 RAG 프롬프트 인젝션, W11 차등프라이버시, W14 MLOps 로그 거버넌스와 연결된다.

### 2.2 강의계획서상 학습목표

- Self-attention과 Transformer block의 기본 원리를 이해한다.
- Efficient Transformer가 긴 입력의 계산 복잡도와 메모리 병목을 어떻게 완화하는지 정리한다.
- Faster/lighter Transformer의 distillation, pruning, quantization, compression 전략을 보안 평가 비용과 연결한다.
- NLP adversarial robustness에서 character/word/sentence/paraphrase attack과 defense metric을 구분한다.
- Prompt privacy와 ICL leakage를 입력, 출력, 로그, tool-call argument 관점에서 위협모형화한다.
- Synthetic toy 실험으로 clean score, ASR, privacy leakage, utility score를 분리 기록한다.

### 2.3 이번 주 핵심 질문

1. Self-attention의 계산 복잡도는 긴 prompt와 log 감사 비용에 어떤 영향을 주는가?
2. Efficient/faster/lighter Transformer는 보안 필터와 프라이버시 필터의 배포 가능성을 어떻게 바꾸는가?
3. NLP adversarial attack은 이미지 perturbation과 달리 semantic similarity와 utility를 왜 함께 봐야 하는가?
4. Prompt masking의 leakage 0.000000을 실제 개인정보보호 보증으로 해석하면 왜 위험한가?
5. W04의 synthetic toy protocol을 기말논문의 prompt privacy 평가 프레임워크로 확장하려면 어떤 지표가 필요한가?

---

## 3. 논문 5편의 서술형 종합 요약

### 3.1 P01. Efficient Transformers: A Survey

P01은 W04의 Transformer 효율화 핵심 문헌이다. 기존 self-attention은 입력 길이 $n$에 대해 token 간 모든 관계를 계산하므로 시간과 메모리 비용이 크게 증가한다. Efficient Transformer 연구는 sparse attention, low-rank attention, kernelized attention, memory-compressed attention, recurrence 등 다양한 구조를 통해 긴 문맥을 더 낮은 비용으로 처리하려고 한다.

보안 관점에서 긴 문맥 처리 비용은 단순 성능 문제가 아니다. 프롬프트 보안 필터, 로그 감사, RAG 문서 검증, 민감정보 탐지 시스템은 긴 입력을 처리해야 하므로 latency와 memory가 크면 실제 운영 경로에 방어를 넣기 어렵다. 따라서 P01은 W04에서 long-context security와 cost-aware defense의 배경이 된다.

### 3.2 P02. A Practical Survey on Faster and Lighter Transformers

P02는 Transformer를 더 빠르고 가볍게 만드는 실용적 기법을 정리한다. Distillation, pruning, quantization, parameter sharing, architecture simplification은 모델 크기와 추론 비용을 줄이는 데 사용된다. 이러한 접근은 모바일·엣지·실시간 서비스에서 Transformer 기반 모델을 운영하는 데 중요하다.

보안 관점에서는 경량화가 방어 기능의 배포 가능성을 높일 수 있다. 그러나 압축된 모델이 adversarial robustness, prompt filtering, privacy masking 성능을 유지하는지는 별도로 평가해야 한다. W04 보고서에서는 효율성을 utility-cost trade-off로 보고, latency와 memory뿐 아니라 보안 지표와 함께 기록해야 한다.

### 3.3 P03. A survey of transformers

P03은 Transformer 계열 구조와 응용을 전반적으로 정리한다. Transformer는 self-attention, feed-forward network, residual connection, layer normalization, positional encoding 등을 통해 sequence modeling의 기본 구조가 되었고, NLP뿐 아니라 vision, multimodal, speech, graph task로 확장되었다.

보안 관점에서 Transformer taxonomy는 공격면을 분리하는 데 중요하다. 입력 token, embedding, attention map, output, log, tool call, prompt template은 각각 다른 보호 자산이 될 수 있다. 따라서 W04에서는 Transformer를 단순 모델 구조가 아니라 입력·처리·출력·기록 단계가 연결된 보안 평가 대상으로 본다.

### 3.4 P04. A Survey of Adversarial Defenses and Robustness in NLP

P04는 NLP adversarial attack과 defense를 정리하는 핵심 보안 문헌이다. NLP 공격은 character-level typo, word substitution, paraphrase, syntax transformation, sentence-level perturbation 등으로 구성될 수 있다. 이미지 공격과 달리 NLP 공격은 의미 보존, 문법성, 자연스러움, semantic similarity를 함께 고려해야 한다.

보안 관점에서 P04는 clean score와 ASR을 분리해야 하는 근거가 된다. 정상 문장에서는 모델이 잘 작동하더라도, 의미가 크게 바뀌지 않은 단어 치환이나 재구성 문장에서 모델 판단이 바뀌면 NLP 시스템은 강건하지 않다. 따라서 ASR, robust accuracy, semantic similarity, utility preservation, false positive rate를 함께 보고해야 한다.

### 3.5 P05. Privacy Preserving Prompt Engineering: A Survey

P05는 prompt privacy와 privacy-preserving prompt engineering을 정리한다. Prompt에는 사용자 개인정보, 업무 기밀, API token, 지시문, ICL examples, RAG context, tool-call argument가 포함될 수 있다. 이러한 정보는 모델 입력, 출력, 로그, 제3자 API 전달 과정에서 노출될 수 있다.

보안 관점에서 P05는 W04의 prompt privacy 핵심 문헌이다. Prompt masking, rewriting, policy instruction, redaction, context minimization, logging control은 privacy leakage를 줄이는 데 활용될 수 있다. 다만 마스킹이 과도하면 utility가 떨어질 수 있으므로 privacy leakage와 utility score를 동시에 보고해야 한다.

---

## 4. 논문 간 연결 관계

W04 논문 5편은 다음 흐름으로 연결된다.

```text
Efficient Transformer와 long-context 비용
→ Faster/lighter Transformer와 배포 가능성
→ Transformer taxonomy와 입력·출력·로그 공격면
→ NLP adversarial robustness
→ prompt privacy와 ICL leakage 평가
```

P01과 P02는 Transformer의 비용과 효율화 문제를 다룬다. P03은 Transformer 전체 구조와 응용 지도를 제공한다. P04는 NLP 입력 교란과 robustness 평가를 다루고, P05는 prompt privacy와 leakage 방어를 다룬다. 이 다섯 문헌을 종합하면 W04의 핵심 메시지는 “Transformer 기반 AI 시스템 보안은 성능뿐 아니라 비용, 강건성, 프라이버시, 유용성, 재현성을 함께 평가해야 한다”는 것이다.

---

## 5. AI 원리 70% 정리

Transformer는 입력 token 간 관계를 attention으로 계산한다. 이 구조는 긴 문맥과 복잡한 의미 관계를 학습하는 데 강력하지만, 입력 길이가 길어질수록 attention cost가 커진다. Efficient Transformer는 attention 연산을 sparse, low-rank, kernelized 방식으로 근사하거나 제한해 비용을 낮추려 한다. Faster/lighter Transformer는 distillation, pruning, quantization 등을 통해 실서비스 배포 비용을 줄인다.

### 5.1 핵심 수식

Scaled dot-product attention은 query와 key의 유사도로 value를 가중합한다.

$$
Attention(Q,K,V)=\mathrm{softmax}\left(\frac{QK^T}{\sqrt{d}}\right)V
$$

| 기호 | 의미 |
|---|---|
| $Q$ | query matrix |
| $K$ | key matrix |
| $V$ | value matrix |
| $d$ | key/query dimension |

Full attention의 계산 복잡도는 입력 길이 $n$에 대해 대략 다음과 같이 증가한다.

$$
Cost_{full}=O(n^2d)
$$

Sparse attention은 일부 token 관계만 계산해 비용을 줄인다.

$$
Cost_{sparse}=O(nkd)
$$

| 기호 | 의미 |
|---|---|
| $n$ | sequence length |
| $k$ | 각 token이 참조하는 제한된 token 수 |
| $d$ | hidden dimension |

Transformer block은 attention과 feed-forward network를 residual 구조로 결합한다.

$$
h_{l+1}=h_l+\mathrm{MHA}(h_l)
$$

$$
z_{l+1}=h_{l+1}+\mathrm{FFN}(h_{l+1})
$$

NLP adversarial evaluation에서는 attack success rate를 별도로 기록한다.

$$
ASR=\frac{N_{atk}}{N_{adv}}
$$

Prompt privacy 평가에서는 민감정보 누출 비율을 분리한다.

$$
LeakageRate=\frac{N_{leak}}{N_{risk}}
$$

| 기호 | 의미 |
|---|---|
| $N_{adv}$ | 공격 조건 평가 입력 수 |
| $N_{atk}$ | 공격 성공 입력 수 |
| $N_{risk}$ | 민감정보 위험이 있는 입력 수 |
| $N_{leak}$ | 마스킹 이후에도 민감정보가 남은 입력 수 |

### 5.2 핵심 개념과 보안 연결

| 핵심 개념 | AI 원리 | 보안 연결 |
|---|---|---|
| Self-attention | 토큰 간 관계를 Q/K/V로 계산 | 긴 프롬프트와 로그 처리 비용 증가 |
| Efficient Transformer | sparse, low-rank, kernelized attention | 보안 필터 latency와 감사 비용에 영향 |
| Faster/lighter Transformer | distillation, pruning, quantization | 방어 기능의 배포 가능성과 성능 유지 평가 |
| Transformer taxonomy | 구조와 응용 분류 | 입력·출력·로그별 공격면 분리 |
| NLP adversarial robustness | 단어·문장 수준 교란 | ASR과 semantic utility 분리 필요 |
| Prompt privacy | prompt/ICL/log 민감정보 보호 | leakage와 utility 동시 평가 필요 |

---

## 6. 보안 이슈 30% 정리

NLP 대적공격은 의미를 크게 유지하면서 모델 판단을 바꾸는 단어 치환, 문장 재구성, paraphrase, transfer attack을 다룬다. Prompt privacy는 프롬프트 입력과 ICL 예시에서 민감정보가 노출될 수 있음을 지적한다. 보호 자산은 prompt input, ICL examples, model output, logs, tool-call arguments, user intent이다.

| 보안 속성 | W04에서의 의미 | 대표 위협 | 평가 지표 |
|---|---|---|---|
| Confidentiality | prompt, ICL, log, tool-call argument의 민감정보 노출 | prompt leakage, ICL leakage | leakage rate |
| Integrity | 의미 유지 교란으로 모델 판단 변경 | word substitution, paraphrase attack | ASR, robust score |
| Availability | 보안 필터·마스킹 비용으로 응답 지연 증가 | long-context overhead | latency, cost |
| Privacy | 민감정보 마스킹과 utility의 상충관계 | over-masking, under-masking | privacy-utility score |
| Accountability | prompt, output, log, policy decision 기록 필요 | 감사 불가능성 | reproducibility evidence |

---

## 7. Research Track 분석

### 7.1 연구문제

- RQ1. 프롬프트 기반 AI 시스템의 민감정보 보호를 어떤 최소 지표로 평가할 것인가?
- RQ2. Word substitution은 clean score와 attack success rate에 어떤 차이를 만드는가?
- RQ3. Prompt masking과 prompt wrapper는 privacy leakage와 utility score를 어떻게 바꾸는가?
- RQ4. Efficient Transformer와 경량화 기법은 보안 필터의 배포 가능성과 감사 비용에 어떤 영향을 주는가?

### 7.2 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | user prompt, ICL examples, RAG context, model output, logs, tool-call arguments, user intent |
| 공격자 목표 | 민감정보 유출, word substitution 우회, prompt privacy filter 회피, 로그 노출 유도 |
| 공격자 지식 | keyword detector 일부 지식, prompt pattern 관찰, output/log 접근 가능성 |
| 공격자 능력 | word substitution, paraphrase, 민감정보 포함 prompt 작성, masking 우회 표현 사용 |
| 공격 경로 | prompt 입력 → Transformer/NLP system → output/log/tool-call → privacy leakage 또는 오분류 |
| 방어자 능력 | masking, rewriting, policy instruction, logging control, privacy wrapper, reproducibility logging |
| 제외 범위 | 실제 서비스 침해, 실제 개인정보 사용, 무단 API 반복 질의, 악용 가능한 공격 절차 제공 |

### 7.3 평가축

| 평가축 | 질문 | 대표 지표 또는 증거 |
|---|---|---|
| Clean score | 정상 synthetic prompt를 올바르게 분류하는가 | clean score |
| Attack behavior | word substitution 후 우회가 발생하는가 | attack success rate |
| Privacy leakage | masking 후 민감정보가 남는가 | privacy leakage |
| Utility preservation | 마스킹 후 입력 의도가 유지되는가 | utility score |
| Reproducibility evidence | 동일 결과를 다시 만들 수 있는가 | seed, config, Docker, outputs, run log |

### 7.4 재현성

재현성을 위해 synthetic prompt dataset, seed, substitution rule, masking regex, privacy wrapper, config, Dockerfile, CSV/JSON/Markdown log를 보존한다. W04 실습은 실제 사용자 프롬프트나 개인정보를 사용하지 않는다.

---

## 8. 실습 보고서 및 그래프 수치 검증

본 실습은 실제 Transformer 또는 LLM 공격 재현이 아니라 W04의 핵심인 프롬프트 프라이버시 평가축을 안전하게 설명하기 위한 최소 toy protocol이다. Synthetic privacy-risk prompts와 keyword privacy-risk detector를 사용해 clean score, attack success rate, privacy leakage, utility score, reproducibility evidence를 분리하였다.

### 8.1 실습 설계

| 항목 | 내용 |
|---|---|
| Dataset | Synthetic privacy-risk prompts |
| Model/checker | Keyword privacy-risk detector |
| Baseline | Clean baseline |
| Attack scenario | Word substitution |
| Defense/check | Regex masking and privacy-preserving prompt wrapper |
| Metrics | Clean score, attack success rate, privacy leakage, utility score |
| Seed | 42 |
| 결과 위치 | `04_experiment/outputs/` |

### 8.2 실습 결과 수치

| 조건 | Clean Score | Attack Success Rate | Privacy Leakage | Utility Score | 해석 |
|---|---:|---:|---:|---:|---|
| Clean baseline | 1.000000 | 해당 없음 | 해당 없음 | 1.000000 | 정상 입력에서 keyword detector가 synthetic 라벨을 모두 맞춤 |
| Word substitution | 0.625000 | 0.750000 | 해당 없음 | 1.000000 | 민감 키워드 우회로 일부 privacy-risk 입력이 benign으로 오분류 |
| Prompt masking | 해당 없음 | 해당 없음 | 0.000000 | 1.000000 | 정규식 마스킹 후 synthetic 민감값 노출 없음 |
| Privacy-preserving prompt | 해당 없음 | 해당 없음 | 0.000000 | 1.000000 | 마스킹과 정책 지시를 결합해 입력 의도만 유지 |

이 결과는 synthetic toy 실험의 평가 형식 검증용 수치이며, 실제 Transformer, LLM, 상용 NLP 시스템의 강건성 또는 프라이버시 보호 성능으로 일반화하지 않는다. Word substitution 결과는 실제 NLP adversarial robustness 수치가 아니며, Prompt masking leakage 0.000000은 synthetic regex check 결과일 뿐 실제 개인정보보호 보증이 아니다.

### 8.3 그래프 수치 검증

현재 제출 보고서의 그래프는 `assets/w04_metric_chart.png`를 참조한다. 확인 가능한 SVG 그래프에는 `clean_score`, `attack_success_rate`, `privacy_leakage`, `utility_score` 네 series가 표시되어 있다. 각 조건마다 측정되는 지표가 다르므로 보고서 표에서는 해당 없음 항목을 명시한다.

| 조건 | 그래프 Clean Score | 표 Clean Score | 그래프 ASR | 표 ASR | 그래프 Privacy Leakage | 표 Privacy Leakage | 그래프 Utility | 표 Utility | 확인 결과 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Clean baseline | 1.000000 | 1.000000 | 해당 없음 | 해당 없음 | 해당 없음 | 해당 없음 | 1.000000 | 1.000000 | 일치 |
| Word substitution | 0.625000 | 0.625000 | 0.750000 | 0.750000 | 해당 없음 | 해당 없음 | 1.000000 | 1.000000 | 일치 |
| Prompt masking | 해당 없음 | 해당 없음 | 해당 없음 | 해당 없음 | 0.000000 | 0.000000 | 1.000000 | 1.000000 | 일치 |
| Privacy-preserving prompt | 해당 없음 | 해당 없음 | 해당 없음 | 해당 없음 | 0.000000 | 0.000000 | 1.000000 | 1.000000 | 일치 |

<!-- submission-metric-chart:start -->
**그림 1. W04 metrics summary chart**

![W04 metrics summary chart](assets/w04_metric_chart.png)

출처: `04_experiment/outputs/metrics_summary.csv`. 이 그래프는 공개 toy/synthetic 산출물 기반이며 실제 공격 성능이나 운영 환경 성능으로 일반화하지 않는다. 현재 그래프는 clean_score, attack_success_rate, privacy_leakage, utility_score를 시각화한다.
<!-- submission-metric-chart:end -->

### 8.4 예측 요약

| ID | 정답 | Clean 예측 | 공격 후 예측 |
|---|---|---|---|
| B01 | benign | benign | benign |
| B02 | benign | benign | benign |
| B03 | benign | benign | benign |
| B04 | benign | benign | benign |
| R01 | privacy_risk | privacy_risk | benign |
| R02 | privacy_risk | privacy_risk | benign |
| R03 | privacy_risk | privacy_risk | benign |
| R04 | privacy_risk | privacy_risk | privacy_risk |

---

## 9. 기말논문 연결

W04는 기말논문에서 “프롬프트 기반 AI 시스템의 민감정보 보호 평가체계 연구”로 확장할 수 있다. W04는 관련연구, 위협모형, synthetic prompt toy protocol, clean/ASR/leakage/utility/reproducibility 평가축을 제공한다.

| 기말논문 장 | W04 반영 내용 |
|---|---|
| 1장 서론 | 프롬프트 기반 AI 시스템에서 민감정보 보호 평가 필요성 제시 |
| 2장 관련연구 | Efficient Transformer, faster/lighter Transformer, Transformer taxonomy, NLP robustness, prompt privacy 문헌 정리 |
| 3장 위협모형 | prompt, ICL example, log, tool-call argument, output leakage 공격면 정의 |
| 4장 연구방법 | clean score, ASR, privacy leakage, utility score, reproducibility evidence 설계 |
| 5장 분석 | word substitution과 masking/wrapper 결과 비교 |
| 6장 결론 | prompt privacy 평가는 leakage와 utility를 함께 보고해야 함 |

---

## 10. AI 도구 활용 기록

AI 도구는 문헌 요약, 코드 점검, 문장 구조화, 그래프 생성 보조에 사용하였다. 모든 DOI/URL, 실험 수치, 본문 인용, 결론은 작성자가 outputs 파일과 로컬 참고문헌 검증표를 대조하여 검증한다.

| 항목 | 내용 |
|---|---|
| 사용 도구명 | Codex, ChatGPT 계열 도구 |
| 사용 목적 | 문헌 요약 정리, 보고서 구조화, 안전한 toy/synthetic 실험 결과 표기 점검, 그래프 생성 보조, 제출 전 체크리스트 정리 |
| AI 산출물 반영 위치 | `07_week_submission/w04_submission_report.md`, `07_week_submission/assets/w04_metric_chart.png`, `05_ai_worklog/ai_disclosure_draft.md` |
| 본인 수정 내용 | 주차별 문헌 상태 확인, 실험 수치와 outputs 대조, 안전 범위와 한계 문장 확인, 최종 제출 전 미확정 문헌 분리 |
| 사실관계 검증 방법 | `01_papers/paper_list.md`, `01_papers/doi_check.md`, 강의계획서 문헌표 대조 |
| 실험결과 검증 방법 | `04_experiment/experiment_report.md`, `04_experiment/outputs/metrics_summary.csv`, `results.json`, `run_log.md`의 수치와 보고서 표기 대조 |
| 최종 책임 확인 | AI 산출물은 초안 보조이며 최종 제출자는 원고 내용, 인용, 실험결과, 연구윤리 책임을 확인한다. |

---

## 11. 제출 전 자기 점검표

| 점검 항목 | 상태 | 비고 |
|---|---|---|
| 메타정보 작성 | 완료 | 작성일 2026-06-26 반영 |
| 초록 및 키워드 작성 | 완료 |  |
| AI 원리 70% 정리 | 완료 | 핵심 수식 추가 |
| 보안 이슈 30% 정리 | 완료 |  |
| 논문 5편 서술형 요약 | 완료 |  |
| 논문 간 연결 관계 작성 | 완료 |  |
| Research Track 5요소 작성 | 완료 | 연구문제, 위협모형, 평가방법, 재현성, 한계 |
| P01~P05 PDF blob 확인 | 완료 | GitHub 파일 존재 확인. 원문 PDF 저작권/배포 정책 별도 검토 필요 |
| P01~P05 DOI/URL 검증 | 완료 | `paper_list.md` 기준 |
| P01/P02/P04/P05 Article 번호 | 확인 필요 | ACM Article 번호 출판사 페이지 최종 확인 필요 |
| P04 강의자료 저자 표기 | 확인 필요 | `N. Goyal` 표기와 실제 `Shreya Goyal` 차이 |
| 실험 outputs 파일 존재 확인 | 완료 | 실험 보고서 기준 CSV/JSON/run_log 존재 |
| 실험 결과와 보고서 수치 일치 | 완료 | 실험 보고서 수치 기준 반영 |
| 그래프 수치 확인 | 완료 | clean_score/ASR/privacy_leakage/utility_score series 기준 표와 일치 |
| AI 활용 고지 작성 | 완료 |  |
| DOCX/PDF 제출본 생성 | 필요 | `07_week_submission/exports/` 권장 |
| 최종 사람이 검토할 항목 표시 | 완료 | Article 번호, P04 저자 표기, Word/PDF 렌더링 |

---

## 12. 참고문헌 검증표

| 번호 | 참고문헌 | DOI/URL | 상태 | 비고 |
|---:|---|---|---|---|
| [1] | Yi Tay, Mostafa Dehghani, Dara Bahri, Donald Metzler, “Efficient Transformers: A Survey,” ACM Computing Surveys, 2022 | `https://doi.org/10.1145/3530811`; arXiv `https://arxiv.org/abs/2009.06732` | 출판 DOI 확인 | Article 번호 추가 확인 필요 |
| [2] | Quentin Fournier, Gaetan Marceau Caron, Daniel Aloise, “A Practical Survey on Faster and Lighter Transformers,” ACM Computing Surveys, 2023 | `https://doi.org/10.1145/3586074`; arXiv `https://arxiv.org/abs/2103.14636` | 출판 DOI 확인 | Article 번호 추가 확인 필요 |
| [3] | Tianyang Lin, Yuxin Wang, Xiangyang Liu, Xipeng Qiu, “A survey of transformers,” AI Open, 2022 | `https://doi.org/10.1016/j.aiopen.2022.10.001` | 출판 DOI/권호/쪽 확인 | AI Open Vol. 3, pp. 111-132 |
| [4] | Shreya Goyal et al., “A Survey of Adversarial Defenses and Robustness in NLP,” ACM Computing Surveys, 2023 | `https://doi.org/10.1145/3593042`; arXiv `https://arxiv.org/abs/2203.06414` | 출판 DOI 확인 | 강의자료 `N. Goyal` 표기와 실제 제1저자 차이 확인 필요 |
| [5] | Kennedy Edemacu, Xintao Wu, “Privacy Preserving Prompt Engineering: A Survey,” ACM Computing Surveys, 2025 | `https://doi.org/10.1145/3729219`; arXiv `https://arxiv.org/abs/2404.06001` | 출판 DOI 확인 | Article 번호 추가 확인 필요 |

---

## 13. 부록 A. KCI 논문 형식 전환 아이디어

### A.1 제목 후보

| 번호 | 국문 제목 후보 | 영문 제목 후보 | 대상 시스템 | 보안 위협 | 연구방법 | 예상 기여 |
|---:|---|---|---|---|---|---|
| 1 | 프롬프트 기반 AI 시스템의 민감정보 보호 평가체계 연구 | A Study on an Evaluation Framework for Sensitive Information Protection in Prompt-Based AI Systems | LLM 프롬프트 시스템 | Prompt privacy, ICL leakage | 문헌분석 + synthetic prompt 실험 | 민감정보 보호 평가표 |
| 2 | NLP 대적공격과 프롬프트 프라이버시 평가를 위한 다중지표 프레임워크 연구 | A Multi-Metric Framework for Evaluating NLP Adversarial Attacks and Prompt Privacy | Transformer 기반 NLP 시스템 | Word substitution, prompt leakage | toy 실험 + 위협모형 | clean/ASR/leakage/utility 분리 |
| 3 | Efficient Transformer 환경에서 프롬프트 민감정보 보호와 유용성의 상충관계 연구 | A Study on the Trade-off Between Prompt Privacy Protection and Utility in Efficient Transformer Settings | 긴 입력 NLP/LLM 시스템 | 긴 프롬프트 민감정보 노출 | 문헌분석 + 체크리스트 | 비용·보안·유용성 평가 |

추천 제목은 “프롬프트 기반 AI 시스템의 민감정보 보호 평가체계 연구”이다. 연구문제는 프롬프트 기반 AI 시스템에서 민감정보 보호를 평가하기 위한 최소 지표, 단어 치환 공격의 clean score와 ASR 영향, prompt masking과 prompt wrapper의 leakage/utility 영향으로 구성한다.

### A.2 연구문제

- RQ1. 프롬프트 기반 AI 시스템에서 민감정보 보호를 평가하기 위한 최소 지표는 무엇인가?
- RQ2. Word substitution은 clean score와 ASR에 어떤 영향을 주는가?
- RQ3. Prompt masking과 privacy wrapper는 leakage와 utility의 trade-off를 어떻게 만드는가?

---

## 14. 부록 B. SCI 논문 형식 전환 아이디어

SCI 제목 후보는 “A Multi-Metric Evaluation Framework for Prompt Privacy in Transformer-Based NLP Systems: Integrating Clean Score, Attack Success Rate, Privacy Leakage, Utility, and Reproducibility Evidence”이다.

Structured abstract는 Background, Problem, Method, Results, Contribution, Implications로 구성한다. 결과 문장은 W04 toy evaluation이 Clean Score 1.000000, Word substitution ASR 0.750000, synthetic leakage 0.000000 after masking/prompt wrapping을 기록했다는 수준으로 제한한다. 실제 LLM 강건성 또는 개인정보보호 보증으로 일반화하지 않는다.

| 연구축 | 대표 논문 | 역할 |
|---|---|---|
| Efficient Transformers | Tay et al. | attention 복잡도 완화와 X-former 분류 |
| Faster and lighter Transformers | Fournier et al. | 속도·메모리·경량화 전략 |
| Transformer taxonomy | Lin et al. | Transformer 구조와 응용 전체 지도 |
| NLP adversarial robustness | Goyal et al. | 단어 치환·문장 재구성·semantic-preserving attack |
| Prompt privacy | Edemacu and Wu | prompt privacy, ICL leakage, masking/policy control |

---

## 15. 부록 C. 제출 파일 위치와 변환 권장

| 파일 | 설명 |
|---|---|
| `07_week_submission/w04_submission_report.md` | 본 제출용 보고서 원본 |
| `07_week_submission/assets/w04_metric_chart.png` | 제출 보고서 그래프 |
| `04_experiment/experiment_report.md` | 실험 근거 보고서 |
| `04_experiment/outputs/` | 실험 결과 근거 파일 위치 |
| `05_ai_worklog/ai_disclosure_draft.md` | AI 활용 고지 근거 |

Word 제출본은 다음 위치에 생성해 관리한다.

```text
03_weekly_reports/w04_transformer_nlp_security/07_week_submission/exports/w04_submission_report.docx
```

PDF 제출본은 Word에서 최종 육안 검수 후 다음 위치에 저장한다.

```text
03_weekly_reports/w04_transformer_nlp_security/07_week_submission/exports/w04_submission_report.pdf
```

수식은 GitHub와 Word 변환을 모두 고려하여 Markdown 표 안에 넣지 않고, `$$...$$` block math로 유지한다.
