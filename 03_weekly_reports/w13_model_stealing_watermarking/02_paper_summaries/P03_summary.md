# P03 Summary

## A Survey of Deep Neural Network Watermarking Techniques — Yue Li, Hongxia Wang, Mauro Barni, Neurocomputing, 2021

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W13 Model Stealing & Watermarking |
| 논문명 | A survey of Deep Neural Network watermarking techniques |
| 저자 | Yue Li, Hongxia Wang, Mauro Barni |
| 공식 출판 정보 | Neurocomputing, Vol. 461, pp. 171–193, 2021 |
| DOI | https://doi.org/10.1016/j.neucom.2021.07.051 |
| 보조 URL | arXiv `2103.09274` |
| 로컬 PDF | `01_papers/pdf/03_Li_Wang_Barni_2021_DNN_Watermarking_Survey.pdf` |
| 검증 상태 | W13 `paper_list.md`와 `download_source.md` 기준 로컬 PDF 공식 DOI 확인 완료. 강의계획서의 `Feng Li et al., Deep neural network watermarking: Techniques and challenges` 표기와 실제 공식 저자·제목 차이 메모 유지 |
| PDF 확인 메모 | repo의 PDF 폴더에 P03 관련 PDF blob이 존재함을 확인했다. 요약은 로컬 PDF 경로, download source 기록, W13 `paper_list.md`의 공식 DOI 메타데이터 기준으로 보완했다. |
| 핵심 근거 사용 가능 여부 | 가능. W13에서 DNN watermarking, ownership verification, trigger set, watermark key, white-box/black-box watermark, robustness, fidelity, capacity, false ownership claim 평가의 핵심 문헌으로 사용 |

---

## 1. 한 문장 요약

이 논문은 deep neural network watermarking 기술을 **white-box watermark, black-box trigger-set watermark, parameter/activation watermark, ownership verification, watermark key, trigger set, verification threshold, fidelity, robustness, capacity, security, false positive/false negative, fine-tuning·pruning·distillation·model extraction 공격 내성** 관점에서 체계적으로 정리하며, W13에서 model stealing 이후 소유권을 증명하고 도난 모델을 식별하는 핵심 방어 문헌이다.

---

## 2. 핵심 연구문제

> DNN 모델은 학습 데이터, 연산 비용, 설계 노하우가 축적된 고가의 IP 자산이다. 모델이 복제·추출·재배포될 때 소유자는 해당 모델이 자신의 모델임을 어떻게 증명하고, 공격자가 fine-tuning, pruning, compression, distillation, model extraction으로 watermark를 제거하거나 약화시키는 상황을 어떻게 평가해야 하는가?

| 번호 | 연구질문 |
|---|---|
| RQ1 | DNN watermark는 모델 내부 parameter/activation에 삽입되는가, 아니면 특정 trigger input에 대한 black-box behavior로 삽입되는가? |
| RQ2 | Watermark verification은 model ownership proof, stolen model detection, false ownership claim 방지에 어떻게 활용되는가? |
| RQ3 | Fine-tuning, pruning, compression, distillation, model extraction, watermark overwriting 이후에도 watermark가 유지되는가? |
| RQ4 | 좋은 watermark는 fidelity, robustness, capacity, security, efficiency, stealthiness 사이에서 어떤 trade-off를 가져야 하는가? |
| RQ5 | 기말논문에서 watermark 검증 결과를 법적 소유권 확정이 아니라 기술적 evidence chain으로 어떻게 제한해 표현해야 하는가? |

---

## 3. 논문의 핵심 기여

| 기여 | 설명 | W13 연결 |
|---|---|---|
| DNN watermark taxonomy | white-box, black-box, trigger-set, parameter-based, activation-based watermarking 분류 | W13 P03 핵심 분류 |
| Ownership verification 구조화 | watermark key, trigger set, verification threshold, score 기반 소유권 검증 구조 설명 | model stealing 대응 근거 |
| 공격 내성 평가 | pruning, fine-tuning, distillation, extraction, overwriting에 대한 watermark robustness 논의 | P01 model stealing과 연결 |
| 평가 지표 정리 | fidelity, robustness, capacity, security, FPR/FNR, verification accuracy 정리 | W13 metric 설계 |
| 실무 한계 제시 | watermark가 utility를 낮추거나 오탐·미탐·key leakage·false claim 위험을 만들 수 있음을 제시 | W15 evidence chain 연결 |

---

## 4. 목차별 핵심 개괄

| 목차 | 핵심 내용 | 비전공자용 이해 |
|---|---|---|
| 1. Introduction | DNN 모델은 복제와 재배포가 가능하므로, 소유권 보호와 도난 모델 식별을 위한 watermarking이 필요하다. | AI 모델에도 보이지 않는 소유권 표식을 넣을 수 있다. |
| 2. Background | DNN 구조, model IP, model stealing, watermark, ownership verification의 기본 개념을 설명한다. | 모델이 훔쳐졌을 때 “이 모델이 내 것”임을 증명하려는 기술이다. |
| 3. Watermark Taxonomy | White-box watermark, black-box watermark, trigger set, parameter regularization, activation pattern 기반 기법을 분류한다. | 모델 내부를 볼 수 있어야 검증되는 방식과 API 답변만으로 검증되는 방식이 있다. |
| 4. Embedding Methods | 학습 과정에 watermark loss를 추가하거나 trigger sample을 넣어 특정 응답을 만들게 한다. | 특수 질문을 던졌을 때 소유자만 아는 답을 하게 만드는 방식이다. |
| 5. Verification Methods | watermark key, trigger set, response pattern, parameter signature, threshold로 소유권을 검증한다. | 비밀 열쇠와 검증 문제를 이용해 모델 소유권을 확인한다. |
| 6. Attacks on Watermarks | fine-tuning, pruning, model compression, distillation, model extraction, watermark overwriting 등이 watermark를 약화시킨다. | 훔친 사람이 모델을 조금 고치면 표식이 사라질 수 있다. |
| 7. Evaluation Criteria | fidelity, robustness, capacity, security, efficiency, false positive/false negative를 함께 평가한다. | 표식이 잘 남아야 하지만 모델 성능을 망치면 안 된다. |
| 8. Open Challenges | adaptive attacker, watermark removal, key management, legal evidence, benchmark 부족, deepfake/LLM 확장이 과제로 남는다. | 기술적으로 표식을 찾는 것과 법적으로 소유권을 증명하는 것은 다르다. |
| 9. Conclusion | DNN watermarking은 model stealing에 대응하는 중요한 기술이지만, 보장 범위와 검증 조건을 명확히 기록해야 한다. | 워터마크는 강력한 증거가 될 수 있지만 절대적 보장은 아니다. |

---

## 5. 핵심 이론 및 수식

> 아래 수식은 DNN watermarking 검증과 W13 model ownership 평가를 설명하기 위한 표준화된 표현이다. 실제 공격·우회 절차가 아니라 방어·검증·감사 지표 중심으로 정리한다.

### 5.1 Watermark Verification Function

Watermarked model $f_w$와 secret key 또는 trigger set $K$를 이용해 watermark 존재 여부를 판정한다.

$$
Verify(f_w,K)=\mathbf{1}[Score(f_w,K)>\tau]
$$

| 기호 | 의미 |
|---|---|
| $f_w$ | watermark가 삽입된 모델 |
| $K$ | watermark key 또는 trigger set |
| $Score$ | 검증 점수 |
| $\tau$ | 판정 threshold |

### 보안적 의미

threshold를 어떻게 정하느냐에 따라 FPR/FNR이 바뀐다. 소유권 주장은 score, threshold, key 관리, 검증 로그를 함께 제시해야 한다.

---

### 5.2 Trigger-set Verification Accuracy

trigger set에 대해 기대한 watermark response가 나오는 비율이다.

$$
Acc_{wm}=\frac{1}{|T|}\sum_{(x_t,y_t)\in T}\mathbf{1}[f_w(x_t)=y_t]
$$

| 기호 | 의미 |
|---|---|
| $T$ | watermark trigger set |
| $x_t$ | trigger input |
| $y_t$ | 소유자가 기대하는 trigger label 또는 response |

### 보안적 의미

Black-box watermark에서는 trigger-set accuracy가 ownership verification의 핵심 지표가 된다. 단, 일반 task accuracy와 분리 보고해야 한다.

---

### 5.3 Watermark Robustness

공격 또는 모델 변형 후 watermark가 유지되는 정도다.

$$
Robustness_{wm}=\frac{N_{verified\ after\ attack}}{N_{verified\ before\ attack}}
$$

### 보안적 의미

fine-tuning, pruning, compression, distillation 후에도 verification이 유지되어야 실전 방어 가치가 있다.

---

### 5.4 Fidelity Loss

워터마크 삽입으로 task 성능이 얼마나 손상되었는지 측정한다.

$$
FidelityLoss=Acc_{clean}-Acc_{watermarked}
$$

### 보안적 의미

watermark가 강하더라도 정상 task 성능을 크게 낮추면 실무 적용성이 떨어진다.

---

### 5.5 Watermark Capacity

모델에 삽입 가능한 watermark 정보량 또는 trigger 수를 나타낸다.

$$
Capacity_{wm}=\frac{|M_{embedded}|}{Size(f_w)}
$$

| 기호 | 의미 |
|---|---|
| $|M_{embedded}|$ | 삽입된 watermark message 또는 trigger 정보량 |
| $Size(f_w)$ | 모델 크기 또는 parameter 수 |

### 보안적 의미

capacity가 커도 stealthiness와 fidelity가 낮아질 수 있다. 적정 용량과 검증 안정성의 균형이 필요하다.

---

### 5.6 False Positive / False Negative Risk

소유권 검증에서 오탐과 미탐을 구분한다.

$$
FPR=\frac{FP}{FP+TN},\qquad FNR=\frac{FN}{FN+TP}
$$

### 보안적 의미

FPR이 높으면 무관한 모델을 내 모델이라고 잘못 주장할 수 있고, FNR이 높으면 실제 도난 모델을 놓칠 수 있다.

---

### 5.7 Ownership Evidence Score

기술적 소유권 증거를 요약하는 지표다.

$$
EvidenceScore=\alpha Acc_{wm}+\beta Robustness_{wm}-\gamma FPR-\lambda FidelityLoss
$$

### 보안적 의미

좋은 watermark evidence는 검증 정확도와 공격 내성이 높고, 오탐과 성능 손실이 낮아야 한다. 법적 주장에는 추가 증거와 로그가 필요하다.

---

## 6. AI 원리 70% 관점 분석

| 원리 항목 | 설명 | W13/P03에서의 의미 |
|---|---|---|
| DNN Watermarking | 모델에 소유권 표식 삽입 | 핵심 방어 기술 |
| White-box Watermark | parameter/activation 접근으로 검증 | 내부 검증 방식 |
| Black-box Watermark | API query와 trigger response로 검증 | 실서비스 검증 방식 |
| Trigger Set | 소유자만 아는 검증 입력 집합 | ownership key 역할 |
| Watermark Key | 검증에 필요한 비밀 정보 | key management 필요 |
| Robustness | 모델 변형 후 watermark 유지 | 실전 방어력 |
| Fidelity | watermark 후 task 성능 보존 | utility 조건 |
| Capacity/Security | 삽입 정보량과 위조·제거 내성 | watermark 품질 기준 |

---

## 7. 보안 이슈 30% 관점 분석

| 보안 항목 | DNN Watermarking 관점 해석 | 대표 평가 지표 |
|---|---|---|
| 기밀성 | watermark key, trigger set, verification threshold가 노출되면 우회·위조 가능 | key leakage risk |
| 무결성 | 모델 소유권 증거가 위조되거나 제거될 수 있음 | FPR/FNR, verification score |
| 가용성 | watermark 삽입이 모델 성능이나 inference cost를 악화시킬 수 있음 | FidelityLoss, latency |
| 프라이버시 | trigger set이 training data 또는 민감 sample을 포함하면 위험 | trigger privacy check |
| 안전성 | stolen model을 식별하지 못하면 악성 재배포와 책임 회피가 가능 | verification success, audit evidence |
| 책임성 | key, trigger hash, model hash, verification log를 보존해야 분쟁 대응 가능 | evidence chain completeness |

---

## 8. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | model ownership, model weights, trigger set, watermark key, verification threshold, model hash, audit log |
| 공격자 목표 | watermark 제거, ownership 부인, false ownership claim, watermark overwriting, model extraction 후 재배포 |
| 공격자 능력 | fine-tuning, pruning, compression, distillation, model extraction, trigger probing, stolen model 재학습 |
| 공격 경로 | watermarked model 획득/추출 → 모델 변형 또는 재학습 → watermark score 감소 → 소유권 부인 또는 재배포 |
| 방어자 능력 | robust watermark embedding, trigger secrecy, key management, black/white-box verification, model fingerprinting, audit logging |
| 제외 범위 | 실제 모델 워터마크 제거 절차, 타사 모델 소유권 허위 주장, watermark key 탈취, 공격 코드 제공 |

---

## 9. 평가방법 및 지표

| 평가축 | 지표 | 의미 | W13/P03 활용 |
|---|---|---|---|
| 소유권 검증 | Acc_wm, Verify score, threshold pass rate | watermark 존재 검증 | 핵심 평가 |
| 오탐·미탐 | FPR, FNR | false claim과 missed theft 위험 | 법적·운영 리스크 |
| 강건성 | Robustness_wm under pruning/fine-tuning/distillation | 변형 후 watermark 유지 | 공격 내성 |
| 모델 성능 | clean accuracy, FidelityLoss | watermark 삽입 후 task utility | 실무 적용성 |
| 용량 | Capacity_wm, trigger set size | 삽입 가능한 정보량 | watermark 설계 |
| 은닉성 | stealthiness, anomaly of trigger behavior | watermark 탐지·제거 난이도 | 보안성 |
| 비용 | embedding cost, verification latency | 운영 비용 | MLOps 연결 |
| 재현성 | trigger hash, key ID, model hash, verifier version | 감사 가능성 | W15 evidence chain |

---

## 10. 재현성 체크리스트

| 항목 | 기록해야 할 내용 |
|---|---|
| Bibliographic status | 공식 DOI 논문과 로컬 PDF 동일 여부, 강의자료 표기 차이 |
| Model | architecture, dataset, model hash, training config |
| Watermark type | white-box/black-box, parameter/activation/trigger-set 방식 |
| Key/trigger | key ID, trigger set hash, trigger size, threshold, key management 방식 |
| Verification | verifier version, Score function, threshold, Acc_wm, FPR/FNR |
| Attack/robustness | fine-tuning, pruning, distillation, extraction, compression 조건 |
| Utility | clean accuracy, watermarked accuracy, FidelityLoss |
| Logs | model checkpoint, verification log, evidence hash, seed, config |
| Legal/evidence note | watermark 검증은 기술적 증거이며 법적 소유권 확정은 별도 판단 필요 |
| 한계 | watermark 유지 결과를 모든 모델 변형과 모든 공격에 대한 절대 보장으로 과장하지 않음 |

---

## 11. 논문의 고유 기여

1. DNN watermarking 기술을 white-box와 black-box 관점에서 체계적으로 정리한다.
2. Model stealing 이후 소유권 검증과 도난 모델 식별을 위한 기술적 근거를 제공한다.
3. Fidelity, robustness, capacity, security, efficiency, FPR/FNR을 함께 고려해야 함을 강조한다.
4. Watermark가 fine-tuning, pruning, distillation, extraction에 의해 약화될 수 있음을 위협모형에 포함한다.
5. W13 기말논문에서 model ownership evidence chain과 watermark verification table을 설계하는 핵심 근거가 된다.

---

## 12. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 강의자료 표기 차이 | W13 paper_list 기준 공식 DOI와 강의계획서 저자명·제목 표기에 차이가 있다. | 공식 DOI/로컬 PDF 기준으로 인용하고 차이 메모 유지 |
| Watermark 제거 가능성 | fine-tuning, pruning, distillation으로 watermark가 약화될 수 있다. | Robustness_wm 조건별 평가표 제시 |
| 오탐·미탐 위험 | threshold 설정이 false ownership claim 또는 missed theft로 이어질 수 있다. | FPR/FNR과 confidence interval 병기 |
| 성능 손실 | watermark가 task accuracy와 latency를 낮출 수 있다. | FidelityLoss와 cost 기록 |
| Key management | trigger set이나 key가 노출되면 위조·제거 가능 | trigger hash와 접근통제 메모 |
| 법적 증거 한계 | 기술적 watermark 검증만으로 법적 소유권이 자동 확정되지는 않는다. | evidence chain과 법적 판단을 분리 |

---

## 13. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | AI 모델은 model stealing 이후 소유권 검증이 필요한 IP 자산이라는 문제의식 |
| 2장 관련연구 | 공식 P03 DOI 논문을 DNN watermarking survey 핵심 문헌으로 정리 |
| 3장 위협모형 | model ownership, watermark key, trigger set, verification threshold, model hash 보호 자산 정의 |
| 4장 연구방법 | Verify function, Acc_wm, Robustness_wm, FidelityLoss, FPR/FNR, EvidenceScore 지표 설계 |
| 5장 분석 | DNN watermarking taxonomy와 ownership evidence chain table 제시 |
| 6장 보안적 함의 | model stealing 대응, false ownership claim, watermark removal, key management, legal evidence 한계 해석 |

---

## 14. 기말논문 연결 3문장

1. W13에서 기말논문에 반영할 개념: DNN watermarking은 모델 내부 또는 black-box trigger behavior에 소유권 표식을 삽입하고, 검증 시 watermark key와 threshold를 통해 model ownership evidence를 생성하는 기술이다.
2. W13에서 기말논문에 반영할 표·그림·실험: white-box/black-box watermark taxonomy, Verify function, Acc_wm·Robustness_wm·FPR/FNR·FidelityLoss 평가표, key/trigger evidence chain을 반영한다.
3. W13이 LLM/RAG 보안 감사 프레임워크와 연결되는 지점: RAG/LLM 서비스에서도 모델뿐 아니라 prompt template, embedding index, generated answer, citation provenance에 ownership/fingerprint evidence를 설계하고 W14/W15 evidence chain과 연결해야 한다.

---

## 15. 최종 판단

P03은 W13의 DNN watermarking 핵심 문헌이다. P01이 model stealing 공격 배경을 제공하고 P02가 LLM watermark/fingerprint를 다룬다면, P03은 DNN 모델 자체의 소유권 검증과 도난 모델 식별을 위한 고전적 핵심 기준을 제공한다. 따라서 기말논문에서는 P03을 **DNN watermarking taxonomy, ownership verification, trigger set/key management, robustness·fidelity·FPR/FNR 평가의 중심 근거 문헌**으로 사용하는 것이 적절하다.

---

## 16. 변환 호환성 메모

```bash
pandoc P03_summary.md -o P03_summary.docx
pandoc P03_summary.md -o P03_summary.pdf --pdf-engine=xelatex
```
