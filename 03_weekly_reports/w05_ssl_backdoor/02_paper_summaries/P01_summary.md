# P01 Summary

## A Survey on Self-Supervised Learning: Algorithms, Applications, and Future Trends — Jie Gui et al., IEEE TPAMI, 2024

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W05 자기지도학습·파운데이션 모델 & Poisoning/Backdoor |
| 논문명 | A Survey on Self-Supervised Learning: Algorithms, Applications, and Future Trends |
| 저자 | Jie Gui, Tuo Chen, Jing Zhang, Qiong Cao, Zhenan Sun, Hao Luo, Dacheng Tao |
| 공식 출판 정보 | IEEE Transactions on Pattern Analysis and Machine Intelligence, Vol. 46, No. 12, pp. 9052–9071, 2024 |
| DOI | https://doi.org/10.1109/TPAMI.2024.3415112 |
| 보조 URL | https://doi.org/10.48550/arXiv.2301.05712 |
| 로컬 PDF | `01_papers/pdf/01_Gui_et_al_2024_Self_Supervised_Learning_Survey.pdf` |
| 검증 상태 | W05 `paper_list.md` 기준 TPAMI DOI와 arXiv DOI 확인. 강의계획서의 `Yan Gui` 표기는 출판사 기준 `Jie Gui`와 달라 사람 최종 확인 메모 유지 |
| PDF 확인 메모 | repo의 PDF 폴더에 P01 관련 PDF blob이 존재함을 확인했다. 요약은 로컬 PDF 경로와 W05 `paper_list.md`의 공식 DOI/arXiv 메타데이터 기준으로 보완했다. |
| 수식 호환성 | GitHub 수식 렌더링 오류 방지를 위해 `\operatorname`을 사용하지 않고, `\mathrm{...}` 또는 짧은 변수명을 사용했다. 긴 영문 subscript는 표 설명으로 분리했다. |
| 핵심 근거 사용 가능 여부 | 가능. W05의 SSL 알고리즘 taxonomy, contrastive/generative/predictive learning, masked modeling, multimodal SSL, downstream transfer, poisoning/backdoor 공격면 설명의 핵심 배경 문헌으로 사용 |

---

## 1. 한 문장 요약

이 논문은 라벨 없이 표현을 학습하는 자기지도학습을 **contrastive learning, generative/masked modeling, predictive learning, clustering, bootstrapping, multimodal SSL, graph/video/audio/text SSL, pretraining-transfer, downstream adaptation, future trends** 관점에서 체계화하며, W05에서는 pretraining corpus·augmentation·positive/negative pair·masking policy·encoder checkpoint가 모두 보안 자산이자 poisoning/backdoor 공격면이 될 수 있음을 설명하는 핵심 배경 survey 문헌이다.

---

## 2. 핵심 연구문제

> SSL은 라벨을 직접 쓰지 않더라도, pretext task와 augmentation, masking, pair construction, corpus sampling을 통해 representation을 학습한다. 따라서 라벨이 없는 pretraining 단계에서도 데이터 오염, trigger 삽입, augmentation 조작, representation shift가 downstream 보안성에 영향을 줄 수 있다.

| 번호 | 연구질문 |
|---|---|
| RQ1 | SSL은 contrastive, generative, predictive, clustering, bootstrapping 계열로 어떻게 분류되는가? |
| RQ2 | Positive/negative pair, augmentation, masking, context prediction은 representation 학습에 어떤 역할을 하는가? |
| RQ3 | SSL pretraining representation은 downstream transfer, linear probe, fine-tuning으로 어떻게 평가되는가? |
| RQ4 | 라벨이 없는 pretraining 단계에서도 poisoning/backdoor 공격면이 생기는 이유는 무엇인가? |
| RQ5 | 기말논문에서 SSL 기반 encoder를 clean transfer performance와 attack-condition performance로 어떻게 분리 평가할 수 있는가? |

---

## 3. 논문의 핵심 기여

| 기여 | 설명 | W05 연결 |
|---|---|---|
| SSL taxonomy 정리 | contrastive, generative, predictive, clustering, multimodal SSL을 폭넓게 분류 | W05 AI 원리 70% 핵심 |
| Contrastive learning 설명 | positive/negative pair와 similarity objective를 이용한 representation learning 설명 | InfoNCE와 pair poisoning 연결 |
| Masked/generative learning 설명 | 입력 일부를 가리고 복원하는 방식으로 구조를 학습 | masked reconstruction과 corpus leakage 연결 |
| Transfer evaluation 정리 | linear probe, fine-tuning, retrieval, downstream task 평가 구조 제공 | clean/attack 분리 평가 근거 |
| Foundation model 연결 | 대규모 SSL pretraining이 foundation model의 기본 기술임을 설명 | W07/W08 LLM/RAG 보안과 연결 |
| 보안 확장 가능성 | 논문 자체는 보안 전문 survey는 아니지만 pretraining data와 representation이 보안 자산임을 설명 가능 | P04/P05 poisoning/backdoor와 결합 |

---

## 4. 목차별 핵심 개괄

| 목차 | 핵심 내용 | 비전공자용 이해 |
|---|---|---|
| 1. Introduction | SSL은 라벨 부족 문제를 완화하고 대규모 representation learning을 가능하게 한다. | 사람이 정답을 붙이지 않아도 AI가 데이터 구조를 배운다. |
| 2. Background | pretext task, representation, encoder, augmentation, downstream transfer 개념을 정리한다. | 먼저 스스로 공부하고 나중에 실제 과제를 푸는 구조다. |
| 3. Contrastive SSL | positive/negative pair와 similarity loss로 표현공간을 구성한다. | 같은 것은 가깝게, 다른 것은 멀게 배운다. |
| 4. Generative SSL | masked reconstruction, denoising, autoregressive prediction으로 입력 구조를 복원한다. | 가려진 부분을 맞히며 데이터의 패턴을 배운다. |
| 5. Predictive SSL | context, future frame, temporal order, rotation 등 pretext prediction을 사용한다. | 데이터의 다음 부분이나 숨은 관계를 예측한다. |
| 6. Multimodal SSL | 이미지-텍스트, 오디오-비디오, 비디오-텍스트 등 여러 modality의 정렬을 학습한다. | 서로 다른 데이터 형식을 같은 의미 공간에 맞춘다. |
| 7. Applications | vision, NLP, speech, graph, recommendation, medical, remote sensing 등 응용을 정리한다. | 여러 분야의 foundation model 기반이 된다. |
| 8. Challenges | false negative, augmentation bias, collapse, data quality, scaling, privacy, transfer 한계가 남는다. | 자동 학습도 데이터와 설계가 나쁘면 위험하다. |

---

## 5. 핵심 이론 및 수식

> 아래 수식은 SSL 원리와 W05 보안 평가를 설명하기 위한 표준화된 표현이다. GitHub 호환성을 위해 `\operatorname`은 사용하지 않고, 수식은 Markdown 표 밖의 LaTeX block math로 작성한다.

### 5.1 InfoNCE 대조학습 손실

Contrastive SSL은 anchor 표현 $z$와 positive 표현 $z^+$를 가깝게, negative 표현 $z_j^-$를 멀게 학습한다.

$$
\mathcal{L}_{NCE}=-\log\frac{\exp(\mathrm{sim}(z,z^+)/\tau)}{\exp(\mathrm{sim}(z,z^+)/\tau)+\sum_{j=1}^{K}\exp(\mathrm{sim}(z,z_j^-)/\tau)}
$$

| 기호 | 의미 |
|---|---|
| $z$ | anchor representation |
| $z^+$ | 같은 샘플 또는 관련 샘플에서 나온 positive representation |
| $z_j^-$ | negative representation |
| $\mathrm{sim}$ | 유사도 함수 |
| $\tau$ | temperature |

### 보안적 의미

공격자가 augmentation, positive pair, negative sampling, pretraining corpus를 조작하면 representation space가 왜곡될 수 있다. 라벨이 없어도 self-supervised objective 자체가 공격면이 된다.

---

### 5.2 Masked Reconstruction Objective

Generative SSL은 입력 일부를 가리고 원래 값을 복원하도록 학습할 수 있다.

$$
\mathcal{L}_{mask}=\sum_{i\in\mathcal{M}}\ell(\hat{x}_i,x_i)
$$

| 기호 | 의미 |
|---|---|
| $\mathcal{M}$ | mask 위치 집합 |
| $x_i$ | 원래 입력 조각 |
| $\hat{x}_i$ | 모델이 복원한 값 |
| $\ell$ | 복원 손실 |

### 보안적 의미

Masked reconstruction은 corpus의 통계적 패턴을 모델에 저장한다. 민감정보, 편향, 악성 패턴, trigger가 pretraining corpus에 포함되면 downstream behavior에 영향을 줄 수 있다.

---

### 5.3 Predictive SSL Objective

Predictive SSL은 context representation으로 미래 token, frame, patch 또는 latent state를 예측한다.

$$
\mathcal{L}_{pred}=\sum_{t=1}^{T}\ell(\hat{r}_{t+1},r_{t+1})
$$

| 기호 | 의미 |
|---|---|
| $r_{t+1}$ | 다음 시점 또는 다음 위치의 target representation |
| $\hat{r}_{t+1}$ | context에서 예측한 representation |
| $T$ | sequence length 또는 예측 step 수 |

### 보안적 의미

Video/text SSL에서 temporal order나 context prediction이 오염되면 downstream 판단이 특정 순서·패턴·trigger에 민감해질 수 있다.

---

### 5.4 Linear Probe와 Transfer 성능

SSL 표현은 보통 encoder를 고정하고 간단한 classifier를 붙여 평가한다.

$$
\hat{y}=g_{\phi}(h_{\theta}(x))
$$

| 기호 | 의미 |
|---|---|
| $h_{\theta}$ | self-supervised encoder |
| $g_{\phi}$ | downstream linear probe 또는 classifier |
| $\hat{y}$ | downstream 예측 |

### 보안적 의미

Clean transfer accuracy가 높더라도 특정 trigger, 특정 domain shift, 특정 class에서 ASR이 높으면 representation이 보안적으로 취약할 수 있다.

---

### 5.5 Representation Shift

Clean encoder와 오염된 encoder가 같은 입력에 대해 얼마나 다른 표현을 내는지 측정한다.

$$
RepShift=\frac{1}{N}\sum_{i=1}^{N}\left\|h_{clean}(x_i)-h_{test}(x_i)\right\|_2
$$

| 기호 | 의미 |
|---|---|
| $h_{clean}$ | 기준 clean encoder |
| $h_{test}$ | 평가 대상 encoder |
| $x_i$ | 평가 입력 |

### 보안적 의미

Poisoned pretraining이나 checkpoint 공급망 조작은 downstream classifier를 바꾸지 않아도 representation shift를 통해 성능 저하나 backdoor behavior를 만들 수 있다.

---

### 5.6 SSL Backdoor ASR

Trigger 조건에서 downstream target behavior가 나타나는 비율을 측정한다.

$$
ASR_{ssl}=\frac{N_{atk}}{N_{trig}}
$$

| 기호 | 의미 |
|---|---|
| $N_{trig}$ | trigger가 포함된 평가 입력 수 |
| $N_{atk}$ | 공격 목표 behavior가 발생한 사례 수 |

### 보안적 의미

SSL encoder는 라벨이 없는 pretraining에서 학습되지만, downstream fine-tuning 후 특정 trigger에 반응하는 hidden behavior가 나타날 수 있다.

---

### 5.7 Transfer Robustness

다른 downstream task로 전이했을 때 clean 성능과 robust 성능을 함께 본다.

$$
TransferRobustness=Acc_{clean}-ASR_{ssl}-\lambda RepShift
$$

### 보안적 의미

Foundation model은 여러 task로 전이되므로 한 task의 clean accuracy만으로 보안성을 판단하면 부족하다.

---

### 5.8 SSL Pipeline Risk

SSL 기반 시스템의 위험을 corpus, augmentation, objective, checkpoint, downstream 전이 위험으로 요약한다.

$$
SSLRisk=CorpusRisk+AugRisk+ObjectiveRisk+CheckpointRisk+TransferRisk-MonitoringCoverage
$$

### 보안적 의미

SSL 보안은 downstream classifier만 검사해서는 부족하다. pretraining corpus, augmentation rule, objective, checkpoint lineage, downstream transfer evidence를 함께 관리해야 한다.

---

## 6. AI 원리 70% 관점 분석

| 원리 항목 | 설명 | W05/P01에서의 의미 |
|---|---|---|
| Contrastive Learning | positive/negative pair를 이용해 표현공간을 구성 | InfoNCE와 pair poisoning 연결 |
| Generative SSL | masking, reconstruction, denoising으로 입력 구조를 학습 | corpus memorization과 leakage 위험 |
| Predictive SSL | context나 future token/frame을 예측 | temporal/text representation 학습 |
| Clustering/Bootstrapping | pseudo-label 또는 teacher-student 구조로 representation을 안정화 | collapse와 false positive 위험 |
| Augmentation | 같은 의미를 유지하는 변환을 positive signal로 사용 | augmentation policy가 공격면이 됨 |
| Transfer Learning | pretraining representation을 downstream task에 전이 | clean/attack 분리 평가 필요 |
| Foundation Model | 대규모 self-supervised pretraining은 foundation model의 핵심 기반 | W07/W08 LLM/RAG 보안 연결 |
| Multimodal SSL | 서로 다른 modality를 공통 표현공간에 정렬 | cross-modal poisoning과 privacy 연결 |

---

## 7. 보안 이슈 30% 관점 분석

| 보안 항목 | SSL 관점 해석 | 대표 평가 지표 |
|---|---|---|
| 데이터 무결성 | pretraining corpus와 augmentation pipeline이 오염되면 representation이 왜곡 | poison rate, RepShift |
| 모델 무결성 | downstream classifier가 정상이어도 encoder representation이 backdoor를 포함 가능 | ASR_ssl, trigger success |
| 기밀성 | self-supervised corpus가 민감정보를 포함하면 memorization/leakage 위험 | leakage test, nearest-neighbor |
| 가용성 | 오염 representation은 downstream 성능 저하와 task failure를 만들 수 있음 | clean accuracy drop |
| 프라이버시 | unlabeled corpus에도 개인정보·민감속성이 포함될 수 있음 | privacy leakage, MI signal |
| 책임성 | pretraining data, augmentation, seed, checkpoint 출처 기록 필요 | data lineage, model card |

---

## 8. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | pretraining corpus, augmentation rule, positive/negative pairs, mask policy, encoder, projection head, checkpoint, downstream task |
| 공격자 목표 | representation shift, downstream 성능 저하, trigger 조건 target behavior 유도, 특정 class/domain bias 삽입 |
| 공격자 능력 | corpus 오염, augmentation 조작, false positive/negative pair 삽입, mask policy 조작, checkpoint 공급망 조작 |
| 공격 경로 | corpus/augmentation → SSL objective → encoder representation → downstream model → output decision |
| 방어자 능력 | data lineage, augmentation audit, representation monitoring, trigger test, checkpoint verification, downstream robust evaluation |
| 제외 범위 | 실제 대규모 corpus 오염, 무단 모델 공격, 개인정보 포함 데이터 사용, 공격 trigger 제작 절차 제공 |

---

## 9. 평가방법 및 지표

| 평가축 | 지표 | 의미 | W05/P01 활용 |
|---|---|---|---|
| Clean transfer | Linear Probe Accuracy | encoder 표현의 downstream 분류 성능 | clean utility |
| Fine-tuning | Fine-tuning Accuracy | end-to-end downstream 성능 | 실사용 성능 |
| Retrieval | Retrieval Recall | 표현공간 검색 성능 | representation quality |
| Representation | RepShift | clean/test encoder 표현 차이 | poisoning 영향 평가 |
| Backdoor | ASR_ssl | trigger 조건 공격 성공률 | hidden behavior 평가 |
| Robustness | TransferRobustness | clean 성능·ASR·representation shift 통합 | foundation model 위험 평가 |
| Privacy | leakage test | corpus 민감정보 재현 가능성 | 기밀성 평가 |
| Audit | Data Lineage | pretraining data와 checkpoint 출처 기록 | 감사 가능성 |

---

## 10. 재현성 체크리스트

| 항목 | 기록해야 할 내용 |
|---|---|
| Bibliographic status | DOI, IEEE TPAMI 출판정보, arXiv 판본, 강의계획서 표기 차이, 로컬 PDF 상태 |
| Data | 공개 image/text/video toy corpus 사용, 개인정보·실제 민감 데이터 제외 |
| SSL objective | contrastive, masked reconstruction, predictive task 중 선택 |
| Augmentation | crop, mask, noise, temporal sampling, text corruption 등 policy 명시 |
| Model | encoder architecture, projection head, checkpoint hash, seed |
| Downstream | linear probe, fine-tuning classifier, task split, evaluation protocol |
| Security tests | RepShift, ASR_ssl, trigger-free clean accuracy, domain shift, privacy leakage |
| Evidence | config file, data source log, augmentation log, checkpoint hash, metric CSV/JSON, script commit |
| Limitation | 소규모 toy SSL 결과를 foundation model 보안성으로 일반화하지 않음 |
| GitHub math | `\operatorname` 사용 금지, `\mathrm{sim}`과 짧은 변수명 사용 |

---

## 11. 논문의 고유 기여

1. SSL 알고리즘과 응용을 폭넓은 taxonomy로 정리한다.
2. Contrastive/generative/predictive SSL의 공통 원리와 차이를 설명한다.
3. Pretraining representation과 downstream transfer 평가의 기본 구조를 제공한다.
4. W05에서 self-supervised pretraining 단계의 데이터 오염·backdoor 위험을 설명하는 배경 근거가 된다.
5. Foundation model, RAG embedding, multimodal representation 보안으로 확장할 수 있는 평가 프레임을 제공한다.

---

## 12. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 보안 직접성 부족 | poisoning/backdoor를 중심으로 다루는 논문은 아니다. | W05 P04/P05와 결합 |
| 대규모 재현 비용 | foundation-scale SSL 재현은 비용이 크다. | toy encoder/linear probe로 제한 |
| 저자명 검증 | 강의계획서의 `Yan Gui` 표기와 출판사 기준 `Jie Gui`가 다르다. | paper_list 검증 메모 유지 |
| 원문 수치 전사 제한 | survey 수치를 임의 전사하지 않는다. | 평가 프레임 중심으로 사용 |
| augmentation 일반화 | 특정 augmentation이 항상 의미 보존을 보장하지 않는다. | augmentation policy와 failure case 기록 |
| SSL 보안 평가 표준 부족 | SSL backdoor와 representation poisoning 지표가 연구마다 다를 수 있다. | RepShift, ASR_ssl, clean transfer를 분리 보고 |

---

## 13. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | foundation model과 SSL pretraining의 보안 중요성 제시 |
| 2장 관련연구 | SSL taxonomy, contrastive/generative/predictive learning 정리 |
| 3장 위협모형 | corpus, augmentation, pair construction, encoder, checkpoint, downstream transfer 공격면 정의 |
| 4장 연구방법 | InfoNCE, masked reconstruction, linear probe, RepShift, ASR_ssl, TransferRobustness 지표 설계 |
| 5장 분석 | SSL pipeline과 pretraining-stage attack surface matrix 제시 |
| 6장 보안적 함의 | 데이터 무결성, 모델 공급망, representation shift, downstream hidden behavior, 책임성 해석 |
| 부록 | data lineage, augmentation policy, checkpoint hash, linear probe config, metric CSV 수록 |

---

## 14. 기말논문 연결 3문장

1. W05에서 기말논문에 반영할 개념: SSL은 라벨 없이 representation을 학습하지만, pretraining corpus와 augmentation이 오염되면 downstream 모델 전체의 보안성이 흔들릴 수 있다.
2. W05에서 기말논문에 반영할 표·그림·실험: InfoNCE, masked reconstruction, predictive objective, linear probe, RepShift, ASR_ssl, SSLRisk 수식표와 SSL pipeline 도식을 반영한다.
3. W05가 W08/W14/W15와 연결되는 지점: RAG embedding과 LLM pretraining/fine-tuning도 self-supervised representation에 의존하므로 corpus/augmentation/checkpoint lineage를 evidence chain으로 남겨야 한다.

---

## 15. 최종 판단

P01은 W05의 AI 원리 핵심 문헌이다. 직접 보안 문헌은 아니지만 SSL pretraining representation이 왜 보안 자산이 되는지를 설명한다. 따라서 기말논문에서는 P01을 **SSL taxonomy, representation learning, pretraining corpus risk, augmentation attack surface, downstream transfer security, foundation model 보안의 배경 문헌**으로 사용하는 것이 적절하다.

---

## 16. GitHub 수식 호환성 메모

이 파일에서는 GitHub 수식 렌더링 오류 방지를 위해 `\operatorname`을 사용하지 않는다.

| 피해야 할 표현 | 권장 표현 |
|---|---|
| `\operatorname{sim}` | `\mathrm{sim}` |
| `\operatorname{argmax}` | `\mathrm{argmax}` 또는 `\arg\max` |
| `N_{trigger\ success}` | `N_{atk}`처럼 짧은 변수명 사용 후 표에서 의미 설명 |
| `N_{trigger\ inputs}` | `N_{trig}`처럼 짧은 변수명 사용 후 표에서 의미 설명 |
| 긴 영문 subscript | 짧은 변수명 사용 후 표에서 의미 설명 |

```bash
pandoc P01_summary.md -o P01_summary.docx
pandoc P01_summary.md -o P01_summary.pdf --pdf-engine=xelatex
```
