# P02 Summary

## A Comprehensive Survey on Self-Supervised Learning for Recommendation — Xubin Ren, Wei Wei, Lianghao Xia, Chao Huang, ACM Computing Surveys, 2025

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W05 자기지도학습·파운데이션 모델 & Poisoning/Backdoor |
| 강의계획서 표기 | H. Ren et al., `A Comprehensive Survey on Self-Supervised Learning`, ACM Computing Surveys, 2025 |
| 현재 로컬 논문명 | A Comprehensive Survey on Self-Supervised Learning for Recommendation |
| 저자 | Xubin Ren, Wei Wei, Lianghao Xia, Chao Huang |
| 공식 출판 정보 | ACM Computing Surveys, Vol. 58, No. 1, Article 22, pp. 1–38, 2025 |
| DOI | https://doi.org/10.1145/3746280 |
| 로컬 PDF | `01_papers/pdf/02_Ren_et_al_2025_Self_Supervised_Learning_for_Recommendation.pdf` |
| 검증 상태 | W05 `paper_list.md`와 `download_source.md` 기준 DOI와 로컬 PDF 제목 확인. 강의계획서 지정 일반 SSL survey와 동일 여부는 확인 필요 |
| PDF 확인 메모 | repo의 PDF 폴더에 P02 관련 PDF blob이 존재함을 확인했다. 요약은 로컬 PDF 경로와 W05 `paper_list.md`, `download_source.md`의 공식 DOI 메타데이터 기준으로 보완했다. |
| 수식 호환성 | GitHub 수식 렌더링 오류 방지를 위해 `\operatorname`을 사용하지 않고, `\mathrm{sim}`과 짧은 변수명 중심으로 작성했다. 긴 영문 subscript는 표 설명으로 분리했다. |
| 핵심 근거 사용 가능 여부 | 관련 보조 문헌으로 제한적 가능. 일반 SSL 전체를 대표하기보다는 추천 시스템 분야의 domain-specific SSL 문헌으로 사용 |

---

## 1. 한 문장 요약

이 논문은 추천 시스템에서 자기지도학습을 **user-item interaction, sequential behavior, graph structure, contrastive learning, masked reconstruction, generative SSL, adversarial SSL, recommendation augmentation, data sparsity, cold-start, ranking utility, robustness, fairness, privacy** 관점으로 정리하며, W05에서는 domain-specific SSL이 사용자 표현·추천 편향·fake interaction·graph poisoning·사용자 행동정보 프라이버시와 어떻게 연결되는지 설명하는 보조 survey 문헌이다.

---

## 2. 핵심 연구문제

> 추천 시스템의 SSL은 라벨 대신 클릭, 구매, 평점, 시청 이력, user-item graph, sequence, item content를 self-supervised signal로 사용한다. 따라서 추천 SSL에서는 pretraining corpus만이 아니라 interaction log, graph edge, augmentation rule, sequence masking, negative sampling이 모두 보안 공격면이 될 수 있다.

| 번호 | 연구질문 |
|---|---|
| RQ1 | 추천 시스템에서 SSL은 user-item interaction, sequence, graph, content feature를 어떻게 활용하는가? |
| RQ2 | Contrastive, generative, adversarial SSL은 추천 시나리오별로 어떻게 적용되는가? |
| RQ3 | User-item graph augmentation과 behavior sequence masking은 representation 학습에 어떤 역할을 하는가? |
| RQ4 | Fake interaction, poisoned behavior, graph manipulation, item metadata poisoning은 추천 SSL representation을 어떻게 왜곡할 수 있는가? |
| RQ5 | 현재 P02를 일반 SSL 지정 논문이 아니라 관련 보조 문헌으로 사용할 때 어떤 제한과 검증 메모를 남겨야 하는가? |

---

## 3. 논문의 핵심 기여

| 기여 | 설명 | W05 연결 |
|---|---|---|
| 추천 SSL taxonomy | interaction, sequence, graph, content 기반 추천 SSL을 체계화 | domain-specific SSL 사례 |
| Contrastive recommendation 정리 | 사용자·아이템의 서로 다른 view를 positive pair로 학습 | pair/graph poisoning 연결 |
| Generative recommendation 정리 | masked item, masked behavior, feature reconstruction 방식 설명 | masked reconstruction과 privacy 연결 |
| Graph SSL 정리 | user-item graph augmentation, edge/dropout, subgraph view 활용 | graph poisoning 공격면 정의 |
| 평가 지표 정리 | Recall@K, NDCG@K, ranking utility, representation quality를 구분 | 기말논문 실험 지표 |
| 보안 확장 가능성 | fake interaction, exposure manipulation, user privacy risk 분석에 활용 가능 | W05 P04/P05와 결합 |

---

## 4. 목차별 핵심 개괄

| 목차 | 핵심 내용 | 비전공자용 이해 |
|---|---|---|
| 1. Introduction | 추천 시스템에서 SSL이 필요한 이유와 데이터 희소성 문제를 설명한다. | 사용자가 남긴 행동만으로 취향을 더 잘 배우려는 방법이다. |
| 2. Recommendation Background | user, item, interaction, sequence, graph, ranking task를 정리한다. | 사용자와 상품 사이의 관계를 학습한다. |
| 3. Contrastive SSL | user/item의 여러 augmentation view를 비교해 표현을 학습한다. | 같은 사용자의 다른 관찰은 가깝게, 다른 사용자는 멀게 배운다. |
| 4. Generative SSL | 일부 interaction이나 item feature를 가리고 복원한다. | 사용자가 다음에 무엇을 클릭할지, 빠진 항목이 무엇인지 맞힌다. |
| 5. Graph SSL | user-item graph의 edge, node, subgraph augmentation을 사용한다. | 추천 관계망을 변형해도 의미가 유지되도록 학습한다. |
| 6. Sequential SSL | 사용자의 행동 순서를 mask/predict하여 sequence representation을 만든다. | 사용자의 다음 행동을 예측하면서 취향을 배운다. |
| 7. Applications | 일반 추천, sequential recommendation, social recommendation, graph recommendation 등에 적용된다. | 쇼핑, 영상, 뉴스, 음악 추천 등에 쓰인다. |
| 8. Challenges | 데이터 희소성, false negative, bias, privacy, robustness, scalability 문제가 남는다. | 추천이 조작되거나 개인정보가 노출될 수 있다. |

---

## 5. 핵심 이론 및 수식

> 아래 수식은 추천 SSL 원리와 W05 보안 평가를 설명하기 위한 표준화된 표현이다. GitHub 호환성을 위해 `\operatorname`은 사용하지 않고, 수식은 Markdown 표 밖의 LaTeX block math로 작성한다.

### 5.1 Masked Reconstruction Loss

추천 SSL에서는 사용자의 interaction sequence 또는 item feature 일부를 mask하고 복원하도록 학습할 수 있다.

$$
\mathcal{L}_{mask}=\sum_{i\in\mathcal{M}}\ell(\hat{x}_i,x_i)
$$

| 기호 | 의미 |
|---|---|
| $\mathcal{M}$ | mask 위치 집합 |
| $x_i$ | 원래 interaction 또는 item feature |
| $\hat{x}_i$ | 모델이 복원한 값 |
| $\ell$ | 복원 손실 |

### 보안적 의미

Masked reconstruction은 사용자 행동 패턴과 item 구조를 모델에 학습시킨다. 공격자가 interaction history나 item metadata를 조작하면 사용자 표현과 추천 결과가 왜곡될 수 있다.

---

### 5.2 User-Item Contrastive Loss

같은 사용자 또는 item의 다른 augmentation view를 positive pair로 두는 contrastive objective를 사용할 수 있다.

$$
\mathcal{L}_{rec}=-\log\frac{\exp(\mathrm{sim}(h_u^a,h_u^b)/\tau)}{\sum_{v\in\mathcal{B}}\exp(\mathrm{sim}(h_u^a,h_v^b)/\tau)}
$$

| 기호 | 의미 |
|---|---|
| $h_u^a,h_u^b$ | 사용자 $u$의 서로 다른 augmentation view 표현 |
| $h_v^b$ | 비교 대상 사용자 또는 item의 view 표현 |
| $\mathcal{B}$ | batch 내 비교 대상 집합 |
| $\mathrm{sim}$ | 유사도 함수 |
| $\tau$ | temperature |

### 보안적 의미

Graph augmentation이나 sequence augmentation이 공격자에 의해 조작되면 positive/negative 관계가 왜곡될 수 있다. 추천 결과가 특정 item으로 편향되거나 특정 사용자군에 불리하게 변할 수 있다.

---

### 5.3 Ranking Utility

추천 성능은 상위 $K$개 추천 목록의 관련성과 순서를 함께 평가한다.

$$
Recall_K=\frac{N_{hit}}{N_{rel}}
$$

$$
NDCG_K=\frac{DCG_K}{IDCG_K}
$$

$$
DCG_K=\sum_{i=1}^{K}\frac{2^{rel_i}-1}{\log_2(i+1)}
$$

| 기호 | 의미 |
|---|---|
| $N_{hit}$ | 상위 $K$개 추천 안에 포함된 관련 item 수 |
| $N_{rel}$ | 전체 관련 item 수 |
| $rel_i$ | $i$번째 추천 item의 relevance |
| $IDCG_K$ | 이상적인 ranking의 DCG |

### 보안적 의미

추천 SSL의 clean utility가 높더라도 특정 item을 과도하게 노출시키거나 특정 사용자군의 관련 item을 낮추면 보안·공정성 문제가 된다.

---

### 5.4 Representation Shift

오염 전후 user/item embedding 변화량을 측정한다.

$$
RepShift=\frac{1}{N}\sum_{i=1}^{N}\left\|h_{clean}(a_i)-h_{test}(a_i)\right\|_2
$$

| 기호 | 의미 |
|---|---|
| $a_i$ | 사용자 또는 item 평가 대상 |
| $h_{clean}$ | clean 추천 encoder |
| $h_{test}$ | 평가 대상 추천 encoder |

### 보안적 의미

Fake interaction과 graph poisoning은 ranking output이 바뀌기 전에 user/item representation을 먼저 이동시킬 수 있다.

---

### 5.5 Poison Impact

오염 전후 추천 utility 변화량을 측정한다.

$$
PoisonImpact=Utility_{clean}-Utility_{poison}
$$

### 보안적 의미

오염 후 추천 성능이 하락하거나 특정 target item의 exposure가 증가하면 추천 시스템 무결성이 훼손된 것이다.

---

### 5.6 Exposure Bias

특정 target item 또는 item group이 과도하게 노출되는 정도를 평가한다.

$$
ExposureBias=\frac{E_{target}}{E_{total}}
$$

| 기호 | 의미 |
|---|---|
| $E_{target}$ | target item 또는 target group의 노출량 |
| $E_{total}$ | 전체 추천 노출량 |

### 보안적 의미

추천 공격은 단순 accuracy 저하가 아니라 특정 상품·콘텐츠·집단의 노출 조작으로 나타날 수 있다.

---

### 5.7 Recommendation Security Score

추천 SSL은 ranking utility와 오염·편향·프라이버시 위험을 함께 평가해야 한다.

$$
RecSecurityScore=Utility_{rank}-\lambda_1PoisonImpact-\lambda_2ExposureBias-\lambda_3PrivacyRisk
$$

### 보안적 의미

추천 SSL에서는 정확도뿐 아니라 조작된 상호작용이 ranking, fairness, exposure, user privacy에 미치는 영향을 함께 평가해야 한다.

---

### 5.8 Recommendation SSL Risk

추천 SSL pipeline의 위험을 interaction, graph, augmentation, ranking, privacy 위험으로 요약한다.

$$
RecSSLRisk=InteractionRisk+GraphRisk+AugRisk+RankRisk+PrivacyRisk-AuditCoverage
$$

### 보안적 의미

추천 SSL 보안은 모델만 검사해서는 부족하다. user behavior log, graph edge, augmentation rule, ranking output, audit log를 함께 관리해야 한다.

---

## 6. AI 원리 70% 관점 분석

| 원리 항목 | 설명 | W05/P02에서의 의미 |
|---|---|---|
| Interaction SSL | 클릭, 구매, 평점, 시청 이력을 self-supervised signal로 사용 | user behavior representation 학습 |
| Sequential SSL | 사용자 행동 순서를 mask/predict하여 representation 학습 | session/order 정보 활용 |
| Graph SSL | user-item graph augmentation과 contrastive learning 사용 | graph poisoning 공격면 |
| Generative SSL | item 또는 behavior feature를 복원 | 민감 패턴 학습 위험 |
| Adversarial SSL | representation을 강건하게 만들기 위해 perturbation 사용 | robustness 연결 |
| Recommendation Transfer | SSL 표현이 downstream ranking이나 retrieval 성능에 영향 | clean/poison 분리 평가 필요 |
| Data Sparsity | 라벨·interaction 부족을 SSL signal로 보완 | cold-start 지원 |
| User Privacy | 행동 데이터가 개인 선호와 민감 속성을 반영 | privacy risk 평가 필요 |

---

## 7. 보안 이슈 30% 관점 분석

| 보안 항목 | 추천 SSL 관점 해석 | 대표 평가 지표 |
|---|---|---|
| 데이터 무결성 | fake interaction, bot behavior, item metadata poisoning이 representation을 왜곡 | PoisonImpact, RepShift |
| 기밀성 | 사용자 행동 데이터는 민감한 선호·위치·건강·정치 성향을 드러낼 수 있음 | PrivacyRisk, leakage test |
| 공정성 | 특정 item 또는 사용자군에 추천 노출이 편향될 수 있음 | ExposureBias, group utility |
| 가용성 | 추천 품질 저하는 서비스 신뢰도와 사용자 경험을 낮춤 | Recall_K, NDCG_K drop |
| 책임성 | interaction log, augmentation rule, model version, ranking output 기록 필요 | AuditCoverage |
| 공급망 | 사전학습된 추천 encoder와 graph snapshot 출처가 불명확하면 위험 | checkpoint lineage |

---

## 8. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 대상 | user-item interaction, behavior sequence, item metadata, user embedding, item embedding, graph structure, ranking output, audit log |
| 공격자 목표 | 특정 item 노출 증가, 경쟁 item 노출 감소, 사용자 표현 왜곡, 추천 품질 저하, 특정 group 차별적 ranking 유도 |
| 공격자 능력 | fake account, fake interaction, graph edge manipulation, item metadata 조작, behavior sequence 오염, bot traffic |
| 공격 경로 | interaction log 또는 graph edge → SSL augmentation/objective → representation → ranking output |
| 방어자 능력 | interaction provenance, graph anomaly detection, augmentation audit, ranking fairness check, privacy-preserving logging |
| 제외 범위 | 실제 플랫폼 조작, 개인정보 기반 추천 공격, 실사용자 데이터 사용, fake account 생성 절차 제공 |

---

## 9. 평가방법 및 지표

| 평가축 | 지표 | 의미 | W05/P02 활용 |
|---|---|---|---|
| Ranking utility | Recall_K, NDCG_K | 추천 성능 | clean utility |
| Representation | RepShift | 오염 전후 user/item embedding 변화 | poisoning 영향 |
| Data poisoning | PoisonImpact | fake interaction 후 성능 변화 | 데이터 오염 위험 |
| Exposure | ExposureBias | 특정 item/group 노출 편향 | 조작·공정성 위험 |
| Privacy | PrivacyRisk, leakage test | 사용자 행동 정보 노출 가능성 | 기밀성 평가 |
| Robustness | utility under perturbation | graph/sequence 조작 조건 성능 | 강건성 평가 |
| Audit | AuditCoverage | interaction provenance 기록 여부 | 책임성 |
| Lineage | checkpoint/data lineage | 모델·데이터 출처 | W14/W15 연결 |

---

## 10. 재현성 체크리스트

| 항목 | 기록해야 할 내용 |
|---|---|
| Bibliographic status | DOI, ACM CSUR 출판정보, 강의계획서 지정 논문과 로컬 PDF 차이, 로컬 PDF 상태 |
| Data | 공개 추천 데이터셋 또는 toy user-item matrix 사용, 실사용자 개인정보 제외 |
| SSL objective | contrastive, masked reconstruction, sequence prediction 중 선택 |
| Augmentation | edge dropout, node masking, sequence masking, feature masking 등 정책 명시 |
| Poison setting | fake interaction, edge perturbation 등 안전한 toy 조건만 사용 |
| Model | recommender backbone, encoder, graph snapshot, checkpoint hash |
| Evaluation | Recall_K, NDCG_K, RepShift, PoisonImpact, ExposureBias, PrivacyRisk 분리 |
| Evidence | data source, augmentation log, graph snapshot hash, ranking output, metric CSV/JSON, script commit |
| Limitation | 추천 시스템 특화 문헌이므로 일반 SSL survey 대체로 과장하지 않음 |
| GitHub math | `\operatorname` 사용 금지, `\mathrm{sim}`과 짧은 변수명 사용 |

---

## 11. 논문의 고유 기여

1. 추천 시스템 분야의 self-supervised learning을 체계화했다.
2. User-item graph, sequence, content signal을 SSL pretext task로 활용하는 방식을 정리했다.
3. W05에서 domain-specific SSL의 데이터 거버넌스·표현 오염·추천 편향 위험을 설명하는 보조 근거가 된다.
4. 일반 SSL 문헌과 달리 user behavior data의 민감성과 조작 가능성을 구체적으로 연결할 수 있다.
5. RAG ranking, retrieval system, recommender-style retrieval pipeline의 poisoning과 exposure bias 분석으로 확장할 수 있다.

---

## 12. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 지정 논문 동일성 확인 필요 | 강의계획서 지정 일반 SSL survey와 로컬 PDF가 다를 수 있다. | 관련 보조 문헌으로 명시하고 `paper_list.md` 메모 유지 |
| 도메인 제한 | 추천 시스템에 특화되어 image/text/video SSL 일반론을 완전히 대체하지 못한다. | P01/P03으로 일반 SSL과 비디오 SSL 보완 |
| 보안 직접성 부족 | 추천 공격·방어 전문 문헌은 아니다. | poisoning/backdoor 문헌 P04/P05와 결합 |
| 실제 데이터 민감성 | 사용자 행동 데이터 사용은 개인정보 위험이 있다. | toy/public data와 집계 지표 중심으로 제한 |
| Fairness 평가 복잡성 | 노출 편향과 group fairness는 데이터와 서비스 목표에 의존한다. | ExposureBias와 한계 병기 |
| 재현성 문제 | 추천 결과는 sampling, split, negative sampling, graph snapshot에 민감하다. | split, seed, graph snapshot hash 기록 |

---

## 13. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | SSL이 recommendation과 retrieval pipeline에도 적용되며 interaction poisoning 위험을 만든다는 문제의식 |
| 2장 관련연구 | 도메인 특화 SSL 사례로 추천 시스템 SSL 정리 |
| 3장 위협모형 | user-item graph, fake interaction, behavior poisoning, ranking manipulation 공격면 정의 |
| 4장 연구방법 | masked reconstruction, user-item contrastive loss, Recall_K, NDCG_K, RepShift, PoisonImpact, ExposureBias 지표 설계 |
| 5장 분석 | 추천 SSL pipeline과 interaction/graph poisoning risk matrix 제시 |
| 6장 보안적 함의 | 사용자 데이터 기밀성, 추천 편향, ranking manipulation, 책임성 해석 |
| 부록 | toy user-item matrix, augmentation rule, graph snapshot hash, ranking output, metric CSV 수록 |

---

## 14. 기말논문 연결 3문장

1. W05에서 기말논문에 반영할 개념: 추천 SSL은 user-item interaction과 graph 구조를 self-supervised signal로 사용하므로 fake interaction과 graph poisoning이 representation과 ranking을 동시에 왜곡할 수 있다.
2. W05에서 기말논문에 반영할 표·그림·실험: masked reconstruction, user-item contrastive loss, Recall_K, NDCG_K, RepShift, PoisonImpact, ExposureBias, RecSSLRisk 수식표와 recommendation SSL pipeline 도식을 반영한다.
3. W05가 W08/W14/W15와 연결되는 지점: RAG retrieval과 추천 시스템은 모두 ranking pipeline을 가지므로 interaction provenance, graph snapshot, ranking output, audit log를 evidence chain으로 남겨야 한다.

---

## 15. 최종 판단

P02는 W05의 관련 보조 문헌이다. 강의계획서 지정 일반 SSL survey와 동일 여부는 확인이 필요하지만, 현재 로컬 PDF는 추천 시스템 분야의 self-supervised learning을 체계화한 공식 ACM CSUR 논문이다. 따라서 기말논문에서는 P02를 **일반 SSL 대체 문헌이 아니라 recommendation/retrieval SSL, fake interaction, graph poisoning, exposure bias, ranking utility 평가의 보조 근거 문헌**으로 사용하는 것이 적절하다.

---

## 16. GitHub 수식 호환성 메모

이 파일에서는 GitHub 수식 렌더링 오류 방지를 위해 `\operatorname`을 사용하지 않는다.

| 피해야 할 표현 | 권장 표현 |
|---|---|
| `\operatorname{sim}` | `\mathrm{sim}` |
| `\operatorname{argmax}` | `\mathrm{argmax}` 또는 `\arg\max` |
| `N_{poisoned\ interactions}` | 짧은 변수명 사용 후 표에서 의미 설명 |
| `N_{target\ exposure}` | `E_{target}`처럼 짧은 변수명 사용 |
| 긴 영문 subscript | 짧은 변수명 사용 후 표에서 의미 설명 |

```bash
pandoc P02_summary.md -o P02_summary.docx
pandoc P02_summary.md -o P02_summary.pdf --pdf-engine=xelatex
```
