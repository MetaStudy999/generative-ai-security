# W05 100점형 통합 Summary

## 자기지도학습·파운데이션 모델 & Poisoning/Backdoor

## 0. 문서 목적

이 문서는 W05 개별 논문 summary 5개를 기말논문 작성용 연구 노트로 통합한 100점형 요약본이다. 기존 제출용 통합보고서와 별도로, 본 문서는 **SSL/foundation model의 pretraining representation과 poisoning/backdoor 보안 평가축**을 압축 정리하는 용도로 사용한다.

| 항목 | 내용 |
|---|---|
| 주차 | W05 |
| 주제 | 자기지도학습·파운데이션 모델 & Poisoning/Backdoor |
| 주요 문헌 | P01–P05 |
| 핵심 프레임 | SSL taxonomy + domain-specific SSL + video SSL + poisoning defense + DNN-to-LLM backdoor |
| 수식 작성 방식 | GitHub / Word / PDF 변환 호환을 위해 LaTeX block math 사용 |
| 주의사항 | P02는 일반 SSL survey가 아니라 recommendation SSL 관련 보조 문헌이며, 지정 논문 동일성 확인 필요 |

---

## 1. 한 문장 통합 요약

W05는 self-supervised pretraining을 **라벨 없는 representation 학습**으로 이해하되, pretraining corpus, augmentation, positive/negative pair, temporal signal, user-item graph, checkpoint, adapter, fine-tuning data가 poisoning/backdoor 공격면이 될 수 있으므로 clean transfer performance, representation shift, ASR, detection rate, provenance evidence를 분리해 평가해야 함을 정리하는 주차다.

---

## 2. W05 핵심 연구질문

| 번호 | 연구질문 |
|---|---|
| RQ1 | SSL은 contrastive, generative, predictive learning으로 어떻게 분류되는가? |
| RQ2 | Pretraining corpus와 augmentation은 representation과 downstream behavior를 어떻게 결정하는가? |
| RQ3 | 추천 SSL과 비디오 SSL은 도메인별 데이터 구조와 공격면을 어떻게 확장하는가? |
| RQ4 | Poisoning 공격은 라벨이 없는 self-supervised pretraining에서도 어떻게 가능해지는가? |
| RQ5 | Backdoor는 clean performance를 유지하면서 trigger 조건에서 hidden behavior를 어떻게 유도하는가? |
| RQ6 | W05의 SSL/backdoor 평가축을 RAG 문서 오염, LLM fine-tuning, MLOps 공급망 감사로 어떻게 확장할 수 있는가? |

---

## 3. 문헌 5편 통합 매트릭스

| ID | 논문 | 핵심 역할 | 주요 수식/지표 | 기말논문 반영 위치 |
|---|---|---|---|---|
| P01 | Gui et al., *A Survey on Self-Supervised Learning* | SSL taxonomy와 foundation pretraining 원리 | InfoNCE, masked reconstruction, linear probe | 2장 관련연구, 3장 위협모형 |
| P02 | Ren et al., *SSL for Recommendation* | user-item graph와 domain-specific SSL | masked reconstruction, user-item contrastive loss | 2장 관련 보조문헌, 6장 보안 함의 |
| P03 | Schiappa et al., *SSL for Videos* | temporal representation과 cross-modal agreement | temporal contrastive objective, consistency loss | 3장 멀티모달/비디오 위협모형 |
| P04 | Wang et al., *Threats to Training* | poisoning attack/defense taxonomy | poisoned training objective, poison rate, detection rate/FPR | 3장 위협모형, 4장 평가방법 |
| P05 | Jin et al., *Backdoor Attacks and Defences* | DNN-to-LLM backdoor와 ASR 평가 | trigger function, backdoor objective, ASR, utility drop | 4장 평가방법, 6장 보안 함의 |

---

## 4. AI 원리 70% 통합 정리

### 4.1 InfoNCE 대조학습 손실

$$
\mathcal{L}_{InfoNCE}
=-\log\frac{\exp(sim(z,z^+)/\tau)}
{\exp(sim(z,z^+)/\tau)+\sum_{j=1}^{K}\exp(sim(z,z_j^-)/\tau)}
$$

| 기호 | 의미 |
|---|---|
| $z$ | anchor representation |
| $z^+$ | positive representation |
| $z_j^-$ | negative representation |
| $\tau$ | temperature |

**보안 해석:** positive/negative pair, augmentation, corpus curation이 오염되면 representation space가 왜곡될 수 있다.

---

### 4.2 Masked Reconstruction

$$
\mathcal{L}_{mask}=\sum_{i\in\mathcal{M}}\ell(\hat{x}_i,x_i)
$$

**보안 해석:** masked modeling은 corpus의 통계와 패턴을 학습하므로 민감정보, 편향, 악성 trigger가 pretraining representation에 반영될 수 있다.

---

### 4.3 Temporal Contrastive Learning

$$
\mathcal{L}_{temp}=-\log\frac{\exp(sim(z_t,z_{t+\Delta})/\tau)}{\sum_j\exp(sim(z_t,z_j)/\tau)}
$$

**보안 해석:** frame order, temporal trigger, video-audio-text mismatch가 temporal representation과 downstream action recognition을 왜곡할 수 있다.

---

## 5. 보안 이슈 30% 통합 정리

| 보안 축 | 관련 논문 | 핵심 문제 | 주요 지표/증거 |
|---|---|---|---|
| SSL corpus integrity | P01 | pretraining corpus와 augmentation 오염 | data lineage, representation shift |
| Recommendation SSL risk | P02 | fake interaction, graph poisoning, user embedding 왜곡 | Recall@K, NDCG, poison impact |
| Video SSL risk | P03 | frame-level poisoning, temporal trigger, modality mismatch | temporal robustness, ASR |
| Training-time poisoning | P04 | data/model poisoning, clean-label attack | poison rate, detection rate, FPR |
| Backdoor hidden behavior | P05 | clean performance 유지 + trigger condition 악성 행동 | clean accuracy, ASR, utility drop |

---

## 6. W05 통합 위협모형

### 6.1 보호 자산

| 보호 자산 | 설명 |
|---|---|
| Pretraining corpus | 이미지, 텍스트, 비디오, user-item log 등 SSL 데이터 |
| Augmentation rule | crop, mask, temporal sampling, graph augmentation |
| Positive/negative pairs | contrastive learning 관계 |
| Encoder representation | downstream task로 전이되는 표현 |
| Checkpoint/adapter | pretrained model, fine-tuned model, LoRA adapter |
| Trigger test set | hidden behavior 검증용 데이터 |
| Provenance evidence | 데이터 출처, 변경 이력, 학습 로그, 모델 버전 |

### 6.2 공격자 능력

| 공격자 유형 | 가능 행위 | 대표 지표 |
|---|---|---|
| Corpus poisoning attacker | pretraining corpus 일부 오염 | representation shift |
| Augmentation attacker | view generation 또는 masking rule 조작 | transfer performance drop |
| Graph/interaction attacker | fake user-item interaction 삽입 | poison impact, NDCG 변화 |
| Temporal attacker | trigger frame, frame reorder, modality mismatch 삽입 | temporal robustness, ASR |
| Backdoor attacker | trigger-target relation 학습 유도 | ASR, utility drop |
| Supply-chain attacker | checkpoint/adapter/fine-tuning data 조작 | auditability, hidden behavior test |

---

## 7. 통합 평가 지표

| 평가축 | 대표 지표 | 해석 | 관련 논문 |
|---|---|---|---|
| Clean Transfer | linear probe accuracy, fine-tuning accuracy | 정상 downstream 성능 | P01 |
| Representation Quality | retrieval recall, representation distance | 표현공간 품질 | P01, P03 |
| Domain Utility | Recall@K, NDCG@K | 추천/도메인 특화 성능 | P02 |
| Poisoning Impact | poison rate, accuracy drop, representation shift | 오염 영향 | P04 |
| Backdoor Success | ASR, trigger coverage | hidden behavior 평가 | P05 |
| Defense Quality | detection rate, FPR, ASRDrop | 방어 성능·부작용 | P04, P05 |
| Provenance | data lineage, checkpoint source, config/log | 감사 가능성 | P01–P05 |

---

## 8. 핵심 수식 묶음

### 8.1 Poisoned Training Objective

$$
\min_\theta\left[
\sum_{(x,y)\in D}\ell(f_\theta(x),y)
+\lambda\sum_{(\tilde{x},\tilde{y})\in D_p}\ell(f_\theta(\tilde{x}),\tilde{y})
\right]
$$

### 8.2 Poison Rate

$$
PoisonRate=\frac{|D_p|}{|D|+|D_p|}
$$

### 8.3 Backdoor Trigger와 ASR

$$
\tilde{x}=T(x;\tau)
$$

$$
ASR=\frac{1}{n}\sum_{i=1}^{n}\mathbf{1}\{f_\theta(T(x_i))=y_t\}
$$

### 8.4 Utility Drop와 ASRDrop

$$
UtilityDrop=CleanAcc_{baseline}-CleanAcc_{defended}
$$

$$
ASRDrop=ASR_{before}-ASR_{after}
$$

---

## 9. 재현성 체크리스트

| 항목 | 필수 기록 | W05 적용 |
|---|---|---|
| 문헌 | DOI, URL, 판본 차이, 검증 상태 | P01–P05 summary에 반영 |
| 데이터 | corpus/source, augmentation, split | public/toy data 기준 |
| SSL 설정 | objective, positive/negative pair, mask rule, temporal sampling | config 저장 |
| 오염 설정 | poison rate, poison index, trigger pattern, target behavior | 필수 기록 |
| 모델 | encoder, checkpoint, adapter, downstream head | version 기록 |
| 평가 | clean transfer, ASR, detection rate, FPR, representation shift | CSV/JSON 저장 |
| 한계 | toy 결과를 foundation model 보안성으로 일반화 금지 | 명시 필요 |
| AI 활용 | 요약·수식 설명·표 구조화 사용 내역 | AI 활용 고지 필요 |

---

## 10. 기말논문 반영 구조

| 기말논문 장 | W05 반영 내용 |
|---|---|
| 1장 서론 | SSL/foundation model pretraining이 데이터 무결성과 공급망 보안에 의존한다는 문제 제시 |
| 2장 관련연구 | SSL taxonomy, video SSL, recommendation SSL, poisoning, backdoor 문헌 정리 |
| 3장 위협모형 | corpus/augmentation/encoder/checkpoint/adapter/trigger 공격면 정의 |
| 4장 연구방법 | linear probe, ASR, representation shift, detection rate, provenance 지표 설계 |
| 5장 실험/분석 | toy SSL/backdoor 평가 또는 문헌 기반 비교표 제시 |
| 6장 보안적 함의 | 데이터 무결성, 모델 공급망, 프라이버시, 책임성 해석 |
| 7장 결론 | foundation model 보안은 pretraining부터 downstream까지 추적해야 함을 제시 |

---

## 11. W05 기말논문 연결 3문장

1. W05에서 기말논문에 반영할 개념: SSL과 foundation model은 라벨 없이 표현을 학습하지만, corpus·augmentation·checkpoint·fine-tuning data가 오염되면 downstream behavior와 hidden trigger response가 바뀔 수 있다.
2. W05에서 기말논문에 반영할 표·그림·실험: SSL pipeline 도식, InfoNCE/poison rate/ASR 수식, clean transfer-ASR 비교표, provenance checklist를 반영한다.
3. W05가 RAG 문서 오염/LLM 보안 감사 프레임워크와 연결되는 지점: RAG embedding corpus와 LLM fine-tuning data도 representation pipeline의 일부이므로 W05의 SSL/backdoor/provenance 지표를 W08/W14로 확장한다.

---

## 12. 최종 판단

W05의 5개 문헌은 다음 역할로 정리한다.

| 문헌 | 최종 판단 |
|---|---|
| P01 | SSL 원리와 foundation pretraining의 핵심 배경 문헌 |
| P02 | 추천 SSL 관련 보조 문헌. 지정 논문 동일성 확인 필요 |
| P03 | 비디오 SSL과 temporal/cross-modal representation 문헌 |
| P04 | 학습 단계 poisoning과 defense taxonomy 핵심 보안 문헌 |
| P05 | DNN-to-LLM backdoor와 ASR/hidden behavior 평가 핵심 문헌 |

W05는 후속 W07 LLM 보안, W08 RAG 문서 오염, W10 연합학습 poisoning, W14 MLOps 공급망 보안과 직접 연결된다.

---

## 13. 변환 호환성 메모

```bash
pandoc w05_integrated_summary_100point.md -o w05_integrated_summary_100point.docx
pandoc w05_integrated_summary_100point.md -o w05_integrated_summary_100point.pdf --pdf-engine=xelatex
```
