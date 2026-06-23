# P02 Summary

## A Comprehensive Survey on Self-Supervised Learning for Recommendation — Xubin Ren, Wei Wei, Lianghao Xia, Chao Huang, ACM Computing Surveys, 2025

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W05 자기지도학습·파운데이션 모델 & Poisoning/Backdoor |
| 강의계획서 표기 | H. Ren et al., "A Comprehensive Survey on Self-Supervised Learning", ACM Computing Surveys, 2025 |
| 현재 로컬 논문명 | A Comprehensive Survey on Self-Supervised Learning for Recommendation |
| 저자 | Xubin Ren, Wei Wei, Lianghao Xia, Chao Huang |
| 학술지 | ACM Computing Surveys |
| 권호/쪽 | Vol. 58, No. 1, Article 22, pp. 1–38 |
| 연도 | 2025 |
| DOI | https://doi.org/10.1145/3746280 |
| 논문 유형 | Domain-specific Survey / SSL for Recommendation |
| 로컬 PDF | `01_papers/pdf/02_Ren_et_al_2025_Self_Supervised_Learning_for_Recommendation.pdf` |
| 강의계획서 지정 논문과 일치 여부 | 확인 필요. 현재 로컬 PDF는 일반 SSL survey가 아니라 추천 시스템 SSL survey |
| 핵심 근거 사용 가능 여부 | 관련 보조 문헌으로 제한적 가능 |
| 검증 메모 | W05 `paper_list.md` 기준 DOI와 로컬 PDF 제목 확인. 최종 제출 전 지정 일반 SSL survey와 동일 여부 확인 필요 |

---

## 1. 한 문장 요약

이 논문은 추천 시스템에서 self-supervised learning을 **user-item interaction, sequential behavior, graph structure, contrastive/generative/adversarial SSL, data sparsity, recommendation robustness** 관점으로 정리하고, W05에서 domain-specific SSL이 사용자 표현·추천 편향·poisoned interaction 위험과 어떻게 연결되는지 설명하는 보조 survey 문헌이다.

---

## 2. 연구문제

> 추천 시스템에서 라벨이 부족하거나 상호작용 데이터가 희소한 상황에서 self-supervised signal을 어떻게 만들고, 그 표현이 추천 성능과 데이터 오염 위험에 어떤 영향을 주는가?

| 번호 | 연구질문 |
|---|---|
| RQ1 | 추천 시스템에서 SSL은 user-item interaction, sequence, graph, content feature를 어떻게 활용하는가? |
| RQ2 | Contrastive, generative, adversarial SSL은 추천 시나리오별로 어떻게 적용되는가? |
| RQ3 | User-item graph augmentation과 behavior sequence masking은 representation 학습에 어떤 역할을 하는가? |
| RQ4 | Fake interaction, poisoned behavior, graph manipulation은 추천 SSL representation을 어떻게 왜곡할 수 있는가? |
| RQ5 | 현재 P02를 일반 SSL 지정 논문이 아니라 관련 보조 문헌으로 사용할 때 어떤 제한을 명시해야 하는가? |

---

## 3. 핵심 이론 및 수식

### 3.1 Masked Reconstruction Loss

추천 SSL에서는 사용자의 interaction sequence 또는 item feature 일부를 mask하고 복원하도록 학습할 수 있다.

$$
\mathcal{L}_{mask}=\sum_{i\in\mathcal{M}}\ell(\hat{x}_i,x_i)
$$

| 기호 | 의미 |
|---|---|
| $\mathcal{M}$ | mask 위치 집합 |
| $x_i$ | 원래 interaction/item feature |
| $\hat{x}_i$ | 모델이 복원한 값 |
| $\ell$ | 복원 손실 |

### 보안적 의미

Masked reconstruction은 사용자 행동 패턴과 item 구조를 모델에 학습시킨다. 공격자가 interaction history나 item metadata를 조작하면 사용자 표현과 추천 결과가 왜곡될 수 있다.

---

### 3.2 User-Item Contrastive Loss

같은 사용자 또는 item의 다른 augmentation view를 positive pair로 두는 contrastive objective를 사용할 수 있다.

$$
\mathcal{L}_{rec-ssl}
=-\log\frac{\exp(sim(h_u^{(1)},h_u^{(2)})/\tau)}
{\sum_{v\in\mathcal{B}}\exp(sim(h_u^{(1)},h_v^{(2)})/\tau)}
$$

| 기호 | 의미 |
|---|---|
| $h_u^{(1)},h_u^{(2)}$ | 사용자 $u$의 두 augmentation view 표현 |
| $\mathcal{B}$ | batch 내 비교 대상 집합 |
| $sim(\cdot)$ | 유사도 함수 |
| $\tau$ | temperature |

### 보안적 의미

Graph augmentation이나 sequence augmentation이 공격자에 의해 조작되면 positive/negative 관계가 왜곡될 수 있다. 추천 결과가 특정 item으로 편향되거나 특정 사용자군에 불리하게 변할 수 있다.

---

### 3.3 Recommendation Utility와 보안 지표

추천 성능은 ranking utility와 보안 지표를 함께 봐야 한다.

$$
SecurityRecScore = Utility_{rank} - \lambda PoisonImpact - \mu BiasRisk
$$

| 기호 | 의미 |
|---|---|
| $Utility_{rank}$ | NDCG, Recall@K, HR@K 등 추천 성능 |
| $PoisonImpact$ | fake interaction 또는 graph poisoning에 의한 성능 변화 |
| $BiasRisk$ | 특정 item/user group으로의 편향 위험 |

### 보안적 의미

추천 SSL에서는 정확도뿐 아니라 조작된 상호작용이 ranking, fairness, exposure, user privacy에 미치는 영향을 평가해야 한다.

---

## 4. AI 원리 관점 분석

| 항목 | 분석 |
|---|---|
| Interaction SSL | 클릭, 구매, 평점, 시청 이력을 self-supervised signal로 사용한다. |
| Sequential SSL | 사용자 행동 순서를 mask/predict하여 representation을 학습한다. |
| Graph SSL | user-item graph augmentation과 contrastive learning을 사용한다. |
| Generative SSL | item 또는 behavior feature를 복원한다. |
| Adversarial SSL | representation을 강건하게 만들기 위해 perturbation을 사용할 수 있다. |
| Recommendation Transfer | SSL 표현은 downstream ranking이나 retrieval 성능에 영향을 준다. |

---

## 5. 보안 이슈 관점 분석

| 보안 항목 | 추천 SSL 관점 해석 |
|---|---|
| 데이터 무결성 | fake interaction, bot behavior, item metadata poisoning이 표현을 왜곡한다. |
| 기밀성 | 사용자 행동 데이터는 민감한 선호·위치·건강·정치 성향을 드러낼 수 있다. |
| 공정성 | 특정 item 또는 사용자군에 추천 노출이 편향될 수 있다. |
| 가용성 | 추천 품질 저하는 서비스 신뢰도를 낮춘다. |
| 책임성 | interaction log, augmentation rule, model version, ranking output 기록이 필요하다. |

---

## 6. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 대상 | user-item interaction, user embedding, item embedding, graph structure, ranking output |
| 공격자 목표 | 특정 item 노출 증가, 경쟁 item 노출 감소, 사용자 표현 왜곡, 추천 품질 저하 |
| 공격자 능력 | fake account, fake interaction, graph edge manipulation, item metadata 조작 |
| 공격 경로 | interaction log → SSL augmentation/objective → representation → ranking |
| 제외 범위 | 실제 플랫폼 조작, 개인정보 기반 추천 공격, 실사용자 데이터 사용 |

---

## 7. 평가방법 및 지표

| 지표 | 의미 | W05/P02에서의 활용 |
|---|---|---|
| Recall@K | 상위 K개 추천 중 관련 item 포함 비율 | 추천 utility |
| NDCG@K | ranking 품질 | 추천 성능 |
| Representation Shift | 오염 전후 user/item embedding 변화 | poisoning 영향 |
| Poison Impact | fake interaction 후 성능 변화 | 데이터 오염 위험 |
| Exposure Bias | 특정 item 노출 편향 | 공정성/조작 위험 |
| Privacy Risk | 사용자 행동 정보 노출 가능성 | 기밀성 평가 |
| Auditability | interaction provenance 기록 여부 | 책임성 |

---

## 8. 재현성 점검

| 항목 | 점검 |
|---|---|
| 데이터 | 공개 추천 데이터셋 또는 toy user-item matrix 사용 |
| SSL objective | contrastive, masked reconstruction, sequence prediction 중 선택 |
| 오염 조건 | fake interaction, edge perturbation 등 toy 조건만 사용 |
| 평가 | Recall@K, NDCG@K, representation shift, poison impact 분리 |
| 한계 | 추천 시스템 특화 문헌이므로 일반 SSL survey 대체로 과장하지 않음 |
| 검증 | 최종 제출 전 지정 P02 여부 확인 필요 |

---

## 9. 논문의 고유 기여

1. 추천 시스템 분야의 self-supervised learning을 체계화했다.
2. User-item graph, sequence, content signal을 SSL pretext task로 활용하는 방식을 정리했다.
3. W05에서 domain-specific SSL의 데이터 거버넌스·표현 오염·추천 편향 위험을 설명하는 보조 근거가 된다.
4. 일반 SSL 문헌과 달리 user behavior data의 민감성과 조작 가능성을 구체적으로 연결할 수 있다.

---

## 10. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 지정 논문 동일성 확인 필요 | 강의계획서 지정 일반 SSL survey와 로컬 PDF가 다를 수 있다. | 관련 보조 문헌으로 명시하고 paper_list 메모 유지 |
| 도메인 제한 | 추천 시스템에 특화되어 image/text/video SSL 일반론을 완전히 대체하지 못한다. | P01/P03으로 일반 SSL과 비디오 SSL 보완 |
| 보안 직접성 부족 | 추천 공격·방어 전문 문헌은 아니다. | poisoning/backdoor 문헌 P04/P05와 결합 |
| 실제 데이터 민감성 | 사용자 행동 데이터 사용은 개인정보 위험이 있다. | toy/public data와 집계 지표 중심으로 제한 |

---

## 11. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 2장 관련연구 | 도메인 특화 SSL 사례로 추천 시스템 SSL 정리 |
| 3장 위협모형 | user-item graph, fake interaction, behavior poisoning 공격면 정의 |
| 4장 연구방법 | ranking utility, representation shift, poison impact 평가 설계 |
| 6장 보안적 함의 | 사용자 데이터 기밀성, 추천 편향, 책임성 해석 |

---

## 12. 기말논문 연결 3문장

1. 이 주차에서 기말논문에 반영할 개념: 추천 SSL은 user-item interaction과 graph 구조를 self-supervised signal로 사용하므로 fake interaction과 graph poisoning이 representation을 왜곡할 수 있다.
2. 이 주차에서 기말논문에 반영할 표·그림·실험: masked reconstruction 수식, user-item contrastive loss, 추천 SSL 위협모형 표, ranking utility-poison impact 비교표를 반영한다.
3. 이 주차가 RAG 문서 오염/LLM 보안 감사 프레임워크와 연결되는 지점: 추천 SSL의 user-item graph 오염은 RAG의 document-query graph 오염과 유사하므로 P02의 graph/interaction provenance 관점을 W08/W14에 확장한다.

---

## 13. 최종 판단

P02는 W05에서 일반 SSL 지정 논문이 아니라 추천 시스템 SSL 관련 보조 문헌으로 제한해 사용하는 것이 안전하다. 지정 논문 동일성은 최종 제출 전 반드시 확인해야 한다.

---

## 14. 변환 호환성 메모

```bash
pandoc P02_summary.md -o P02_summary.docx
pandoc P02_summary.md -o P02_summary.pdf --pdf-engine=xelatex
```
