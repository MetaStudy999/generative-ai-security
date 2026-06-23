# W02 100점형 통합 Summary

## 대규모 최적화 & 데이터 오염 위협

## 0. 문서 목적

이 문서는 W02 개별 논문 summary 5개를 기말논문 작성용 연구 노트로 통합한 100점형 요약본이다. 기존 `integrated_report_final.md`는 제출용 통합보고서이고, 본 문서는 개별 PDF summary 보강 결과를 반영한 **논문 작성용 압축본**으로 사용한다.

| 항목 | 내용 |
|---|---|
| 주차 | W02 |
| 주제 | 대규모 최적화 & 데이터 오염 위협 |
| 주요 문헌 | P01–P05 |
| 핵심 프레임 | 최적화 원리 + 효율성 평가 + poisoning taxonomy + training data poisoning + backdoor 평가 |
| 수식 작성 방식 | GitHub / Word / PDF 변환 호환을 위해 LaTeX block math 사용 |
| 주의사항 | P04는 강의계획서 지정 제목과 현재 로컬 PDF 제목 차이가 있으므로 최종 제출 전 동일성 확인 필요 |

---

## 1. 한 문장 통합 요약

W02는 머신러닝 학습을 **데이터 기반 최적화 과정**으로 보고, 학습 데이터와 라벨이 오염되면 경험위험, gradient 추정량, 결정경계, 조건부 trigger 반응이 바뀔 수 있으므로 clean accuracy, poisoning impact, ASR, stealthiness, efficiency cost, reproducibility evidence를 분리해 평가해야 함을 정리하는 주차다.

---

## 2. W02 핵심 연구질문

| 번호 | 연구질문 |
|---|---|
| RQ1 | 대규모 머신러닝에서 SGD와 mini-batch gradient는 왜 데이터 품질과 오염에 민감한가? |
| RQ2 | 데이터 오염은 경험위험과 gradient 추정량을 어떻게 왜곡하는가? |
| RQ3 | Efficient DL 관점에서 방어 모델은 accuracy뿐 아니라 어떤 비용 지표를 함께 보고해야 하는가? |
| RQ4 | Poisoning attack은 availability, integrity, backdoor 관점에서 어떻게 구분되는가? |
| RQ5 | Clean accuracy가 높아도 ASR이 높으면 왜 보안적으로 실패한 모델인가? |
| RQ6 | W02의 데이터 오염 평가축을 RAG 문서 오염, LLM fine-tuning, MLOps 데이터 공급망 보안으로 어떻게 확장할 수 있는가? |

---

## 3. 문헌 5편 통합 매트릭스

| ID | 논문 | 핵심 역할 | 주요 수식/지표 | 기말논문 반영 위치 |
|---|---|---|---|---|
| P01 | Bottou et al., *Optimization Methods for Large-Scale Machine Learning* | ERM, SGD, mini-batch gradient, regularization 원리 | expected risk, empirical risk, SGD, poisoned ERM | 2장 이론, 3장 위협모형, 4장 연구방법 |
| P02 | Menghani, *Efficient Deep Learning* | 모델 효율성, 압축, latency, memory, cost 평가 | compression ratio, utility-cost score, security-efficiency score | 4장 평가지표, 5장 실험/분석 |
| P03 | Tian et al., *Poisoning Attacks and Countermeasures* | poisoning taxonomy와 countermeasure | poison rate, bilevel objective, ASR, detection rate | 2장 관련연구, 3장 위협모형 |
| P04 | Cina et al., *Wild Patterns Reloaded* | training data poisoning, data provenance, defense taxonomy | targeted objective, stealthiness, defense FPR | 3장 위협모형, 4장 연구방법 |
| P05 | Jin et al., *Backdoor Attacks and Defences* | backdoor trigger, clean accuracy-ASR 분리, DNN-to-LLM 확장 | trigger function, backdoor loss, ASR, utility drop | 4장 평가방법, 6장 보안적 함의 |

---

## 4. AI 원리 70% 통합 정리

### 4.1 기대위험과 경험위험

머신러닝의 이상적 목표는 실제 데이터 분포에서 기대 손실을 최소화하는 것이다.

$$
\min_{\theta \in \Theta} R(\theta)
= \mathbb{E}_{(x,y)\sim P}\left[\ell(f_{\theta}(x), y)\right]
$$

실제 학습에서는 유한한 학습 데이터셋의 평균 손실을 최소화한다.

$$
\min_{\theta \in \Theta} \hat{R}_n(\theta)
= \frac{1}{n}\sum_{i=1}^{n} \ell(f_{\theta}(x_i), y_i)
$$

| 기호 | 의미 |
|---|---|
| $R(\theta)$ | 기대위험 |
| $\hat{R}_n(\theta)$ | 경험위험 |
| $P$ | 실제 데이터 분포 |
| $D_n$ | 유한 학습 데이터셋 |
| $\ell(\cdot)$ | 손실함수 |

**보안 해석:** 데이터 오염은 경험위험을 구성하는 데이터 자체를 바꾼다. 따라서 모델은 정상 목적함수가 아니라 공격자가 왜곡한 목적함수를 최소화할 수 있다.

---

### 4.2 SGD와 mini-batch gradient

대규모 데이터에서는 mini-batch gradient를 사용한다.

$$
g_t = \frac{1}{|B_t|}\sum_{i \in B_t} \nabla_{\theta}\ell(f_{\theta_t}(x_i), y_i)
$$

$$
\theta_{t+1} = \theta_t - \eta_t g_t
$$

| 항목 | 의미 | 보안 연결 |
|---|---|---|
| $B_t$ | mini-batch | 오염 샘플 포함 여부가 update 방향에 영향 |
| $g_t$ | gradient 추정량 | poisoning은 gradient를 왜곡 가능 |
| $\eta_t$ | learning rate | 오염 영향의 누적 정도와 연결 |
| $\theta_t$ | 현재 모델 파라미터 | 반복 update로 결정경계가 형성됨 |

---

### 4.3 효율성 평가

Efficient DL은 성능과 비용을 함께 고려한다.

$$
Score = Utility - \lambda_1 Latency - \lambda_2 Size - \lambda_3 Energy - \lambda_4 Memory
$$

**보안 해석:** 방어 모델이 정확하더라도 너무 느리거나 무거우면 운영 시스템에 배포되기 어렵다. 따라서 poisoning/backdoor 방어는 accuracy와 ASR 외에 latency, memory, retraining cost, audit cost를 함께 보고해야 한다.

---

## 5. 보안 이슈 30% 통합 정리

| 보안 축 | 관련 논문 | 핵심 문제 | 주요 지표/증거 |
|---|---|---|---|
| 학습 데이터 무결성 | P01, P03, P04 | 데이터와 라벨 오염이 목적함수를 왜곡 | poison rate, poison index, data lineage |
| 효율성·운영성 | P02 | 방어와 검증의 비용·속도·배포 가능성 | latency, size, FLOPs, audit cost |
| Poisoning taxonomy | P03 | availability/integrity/backdoor 공격 구분 | accuracy drop, ASR, detection rate |
| Training data provenance | P04 | 데이터 출처·변경 이력·라벨 검증 누락 | provenance coverage, defense FPR |
| Backdoor hidden behavior | P05 | 정상 성능 유지 + trigger 조건 악성 행동 | clean accuracy, ASR, utility drop |

---

## 6. W02 통합 위협모형

### 6.1 보호 자산

| 보호 자산 | 설명 |
|---|---|
| 원천 데이터 | 수집된 원본 데이터와 메타데이터 |
| 라벨 | 사람 또는 자동화 시스템이 부여한 정답 정보 |
| 전처리 결과 | feature, embedding, augmentation 결과 |
| 학습 과정 | optimizer, batch order, learning rate, seed, checkpoint |
| 모델 파라미터 | 오염된 update가 반영될 수 있는 가중치 |
| 검증 데이터 | clean test set, trigger test set, hidden validation set |
| 운영 로그 | data version, model version, config, metric, incident log |

### 6.2 공격자 능력

| 공격자 유형 | 가능 행위 | 대표 지표 |
|---|---|---|
| Label-flip attacker | 일부 라벨을 다른 클래스로 변경 | accuracy drop, F1 변화 |
| Clean-label attacker | 라벨 변경 없이 feature를 조작 | targeted error, detection difficulty |
| Backdoor attacker | trigger와 target behavior를 삽입 | ASR, utility drop |
| Data-supply attacker | 외부 데이터셋·크롤링·라벨링 과정 오염 | provenance coverage |
| Model supplier attacker | backdoor checkpoint 또는 adapter 제공 | hidden behavior test |
| Resource attacker | 방어 비용을 높여 검증을 회피 | latency, audit cost |

### 6.3 공격 경로

```text
데이터 수집/라벨링
→ 일부 데이터·라벨·trigger 오염
→ mini-batch gradient 왜곡
→ 모델 파라미터와 결정경계 변화
→ 정상 테스트는 통과 가능
→ trigger/target 조건에서 ASR 증가 또는 성능 저하 발생
→ 로그·provenance 부족 시 원인 추적 실패
```

---

## 7. 통합 평가 지표

| 평가축 | 대표 지표 | 해석 | 관련 논문 |
|---|---|---|---|
| Clean Performance | clean accuracy, macro F1 | 정상 조건 성능 | P01, P03, P05 |
| Poisoning Impact | accuracy drop, target error | 오염으로 인한 성능 저하 | P03, P04 |
| Backdoor Success | ASR, trigger coverage | 조건부 공격 성공 여부 | P04, P05 |
| Stealthiness | utility drop, clean accuracy 유지율 | 공격 은닉성 | P04, P05 |
| Defense Quality | detection rate, FPR, removal effectiveness | 방어 성능과 부작용 | P03–P05 |
| Efficiency Cost | latency, size, FLOPs, retraining cost | 배포 가능성 | P02 |
| Reproducibility Evidence | seed, config, poison index, metric log | 재현성과 감사 가능성 | P01, P04 |

---

## 8. 핵심 수식 묶음

### 8.1 Poisoned ERM

$$
\min_{\theta}
\frac{1}{|D_{clean} \cup D_{poison}|}
\sum_{(x,y) \in D_{clean} \cup D_{poison}}
\ell(f_{\theta}(x), y)
$$

### 8.2 Poison Rate

$$
PoisonRate = \frac{|D_{poison}|}{|D_{clean} \cup D_{poison}|}
$$

### 8.3 Targeted Poisoning

$$
\max_{D_{poison} \in \mathcal{C}} \; \Pr[f_{\theta^*}(x^{target}) = y^{adv}]
$$

$$
\theta^* = \arg\min_{\theta}
\sum_{(x,y) \in D_{clean} \cup D_{poison}}
\ell(f_{\theta}(x), y)
$$

### 8.4 Backdoor Trigger와 ASR

$$
x^{trigger} = T(x; \tau)
$$

$$
ASR = \frac{1}{N_{trigger}}
\sum_{j=1}^{N_{trigger}}
\mathbf{1}[f_{\theta}(x_j^{trigger}) = y^{target}]
$$

### 8.5 Utility Drop

$$
UtilityDrop = CleanAcc_{baseline} - CleanAcc_{backdoored}
$$

---

## 9. 재현성 체크리스트

| 항목 | 필수 기록 | W02 적용 |
|---|---|---|
| 문헌 | DOI, URL, 로컬 PDF명, 검증 상태 | P01–P05 summary에 반영 |
| 데이터 | 출처, 버전, split, 라벨 기준 | public/toy data 기준 |
| 오염 설정 | poison rate, poison index, label flip rule, trigger pattern | 필수 기록 |
| 모델 | architecture, optimizer, learning rate, seed | config로 저장 |
| 평가 | clean accuracy, macro F1, ASR, detection rate, FPR | CSV/JSON 저장 |
| 효율성 | latency, model size, retraining cost | 가능한 범위에서 기록 |
| 한계 | toy/public data 일반화 제한 | 실제 운영 성능으로 해석 금지 |
| AI 활용 | 사용 도구, 목적, 검증 방식 | AI 활용 고지 필요 |

---

## 10. 기말논문 반영 구조

| 기말논문 장 | W02 반영 내용 |
|---|---|
| 1장 서론 | 학습 데이터 오염은 모델 학습 과정 자체를 왜곡하는 핵심 AI 보안 위협임을 제시 |
| 2장 관련연구 | 최적화, 효율적 딥러닝, poisoning, training data poisoning, backdoor 문헌 정리 |
| 3장 위협모형 | 공격자 목표, 오염 위치, 오염률, trigger, 데이터 provenance 정의 |
| 4장 연구방법 | clean accuracy, macro F1, ASR, poison rate, stealthiness, latency 기반 평가 설계 |
| 5장 실험/분석 | toy label-flip/backdoor 실험 또는 문헌 기반 비교표 제시 |
| 6장 보안적 함의 | 데이터 무결성, 모델 무결성, 가용성, 공급망 보안, 감사 가능성 해석 |
| 7장 결론 | AI 보안은 추론 방어뿐 아니라 데이터·학습·검증 증거를 포함해야 함을 제시 |

---

## 11. W02 기말논문 연결 3문장

1. W02에서 기말논문에 반영할 개념: 데이터 오염과 backdoor는 학습 데이터와 라벨의 무결성을 훼손해 모델의 경험위험, gradient, 결정경계, 조건부 행동을 바꾸는 학습 단계 공격이다.
2. W02에서 기말논문에 반영할 표·그림·실험: ERM/SGD 수식, poison rate 수식, clean accuracy-ASR 비교표, poisoning taxonomy, backdoor trigger 개념도, provenance checklist를 반영한다.
3. W02가 RAG 문서 오염/LLM 보안 감사 프레임워크와 연결되는 지점: RAG 검색 문서, embedding corpus, LLM fine-tuning data, adapter, prompt dataset도 데이터 파이프라인 자산이므로 W02의 poisoning/backdoor 평가축을 W08/W14의 문서 오염 및 MLOps 감사로 확장한다.

---

## 12. 최종 판단

W02의 5개 문헌은 다음 역할로 정리한다.

| 문헌 | 최종 판단 |
|---|---|
| P01 | 최적화 원리 문헌. 데이터 오염이 목적함수와 gradient를 바꾸는 이유 설명 |
| P02 | 효율성 평가 문헌. 방어 비용·지연시간·모델 크기·배포 가능성 평가에 사용 |
| P03 | Poisoning taxonomy 핵심 문헌. 위협모형과 평가 지표의 중심 근거 |
| P04 | Training data poisoning 관련 핵심 문헌. 단, 강의계획서 지정 제목과 동일성 확인 필요 |
| P05 | Backdoor 핵심 문헌. Clean accuracy와 ASR 분리 평가의 근거 |

W02는 후속 W05 self-supervised/backdoor, W08 RAG prompt injection, W10 federated learning poisoning, W14 MLOps supply-chain security로 확장된다. 특히 기말논문에서는 “오염 데이터가 학습·검색·생성 파이프라인에 들어올 때 어떤 지표와 증거로 보안성을 검토할 것인가”라는 문제로 발전시키는 것이 적절하다.

---

## 13. 변환 호환성 메모

- 모든 핵심 수식은 Markdown 표 밖에 LaTeX block math로 작성했다.
- 변수 설명은 표로 분리했다.
- GitHub Markdown, MS Word, PDF 변환을 모두 고려했다.
- DOCX/PDF 변환 시 다음 명령을 권장한다.

```bash
pandoc w02_integrated_summary_100point.md -o w02_integrated_summary_100point.docx
pandoc w02_integrated_summary_100point.md -o w02_integrated_summary_100point.pdf --pdf-engine=xelatex
```
