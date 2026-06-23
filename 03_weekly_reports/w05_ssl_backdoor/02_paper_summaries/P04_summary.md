# P04 Summary

## Threats to Training: A Survey of Poisoning Attacks and Defenses on Machine Learning Systems — Zhibo Wang et al., ACM Computing Surveys, 2022

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W05 자기지도학습·파운데이션 모델 & Poisoning/Backdoor |
| 강의계획서 표기 | Y. Wang et al., "A Survey of Poisoning Attacks and Defenses on Machine Learning" |
| 정식 제목 | Threats to Training: A Survey of Poisoning Attacks and Defenses on Machine Learning Systems |
| 저자 | Zhibo Wang, Jingjing Ma, Xue Wang, Jiahui Hu, Zhan Qin, Kui Ren |
| 학술지 | ACM Computing Surveys |
| 권호/쪽 | Vol. 55, No. 7, Article 134, pp. 1–36 |
| 연도 | 2022 |
| DOI | https://doi.org/10.1145/3538707 |
| 논문 유형 | Survey / Poisoning Attacks and Defenses Review |
| 로컬 PDF | `01_papers/pdf/04_Wang_et_al_2022_Threats_to_Training_Poisoning_Survey.pdf` |
| 강의계획서 지정 논문과 일치 여부 | 제목·저자 표기 차이로 관련 논문 확인 필요. 주제와 DOI 기준 보조 문헌으로 사용 가능 |
| 핵심 근거 사용 가능 여부 | 관련 보조 문헌으로 가능 |
| 검증 메모 | W05 `paper_list.md` 기준 DOI와 정식 제목 확인. 최종 제출 전 강의계획서 표기와 동일 논문 여부 확인 필요 |

---

## 1. 한 문장 요약

이 논문은 머신러닝 학습 단계의 poisoning 공격과 방어를 **data poisoning, model poisoning, clean-label poisoning, federated/outsourcing threat, sanitization, robust training, detection, reproducibility** 관점에서 체계화하고, W05에서 SSL/foundation model의 pretraining pipeline도 학습 단계 공격면이 될 수 있음을 설명하는 핵심 보안 survey 문헌이다.

---

## 2. 연구문제

> 학습 데이터, 라벨, 모델 업데이트, 외부 학습 서비스가 공격자에 의해 조작될 수 있을 때, poisoning 공격은 어떤 방식으로 모델을 왜곡하며 방어자는 어떤 지표와 증거로 이를 탐지·완화해야 하는가?

| 번호 | 연구질문 |
|---|---|
| RQ1 | Training-time poisoning은 data poisoning과 model poisoning으로 어떻게 구분되는가? |
| RQ2 | Availability attack, targeted attack, clean-label attack, backdoor attack은 어떤 목표 차이가 있는가? |
| RQ3 | SSL pretraining corpus와 augmentation pipeline이 poisoning 공격면이 되는 이유는 무엇인가? |
| RQ4 | 방어는 data sanitization, robust training, anomaly detection, monitoring으로 어떻게 구성되는가? |
| RQ5 | Clean accuracy, ASR, poison rate, detection rate, FPR을 왜 함께 보고해야 하는가? |

---

## 3. 핵심 이론 및 수식

### 3.1 Poisoned Training Objective

오염 데이터가 포함되면 학습 목적함수는 정상 데이터와 오염 데이터 손실을 함께 최소화한다.

$$
\min_\theta\left[
\sum_{(x,y)\in D}\ell(f_\theta(x),y)
+\lambda\sum_{(\tilde{x},\tilde{y})\in D_p}\ell(f_\theta(\tilde{x}),\tilde{y})
\right]
$$

| 기호 | 의미 |
|---|---|
| $D$ | 정상 데이터 |
| $D_p$ | 오염 데이터 |
| $\lambda$ | 오염 항의 상대 가중치 |
| $f_\theta$ | 학습 모델 |
| $\ell$ | 손실함수 |

### 보안적 의미

공격자는 학습 목적함수에 오염 항을 삽입해 모델이 정상 성능은 유지하면서도 특정 조건에서 실패하도록 만들 수 있다.

---

### 3.2 Poison Rate

$$
PoisonRate=\frac{|D_p|}{|D|+|D_p|}
$$

| 기호 | 의미 |
|---|---|
| $D_p$ | 오염 데이터셋 |
| $D$ | 정상 데이터셋 |

### 보안적 의미

낮은 poison rate에서도 높은 ASR이 나타나면 은닉성이 높은 공격이다. SSL 환경에서는 라벨이 없으므로 오염 여부가 더 늦게 발견될 수 있다.

---

### 3.3 Defense Detection Rate와 FPR

$$
DetectionRate=\frac{TP_{poison}}{TP_{poison}+FN_{poison}}
$$

$$
FPR=\frac{FP_{clean}}{FP_{clean}+TN_{clean}}
$$

| 기호 | 의미 |
|---|---|
| $TP_{poison}$ | 오염 샘플을 오염으로 탐지한 수 |
| $FN_{poison}$ | 오염 샘플을 놓친 수 |
| $FP_{clean}$ | 정상 샘플을 오염으로 오탐한 수 |
| $TN_{clean}$ | 정상 샘플을 정상으로 판단한 수 |

### 보안적 의미

데이터 정제 방어는 오염 샘플을 잘 잡는 것뿐 아니라 정상 샘플을 과도하게 제거하지 않는 것도 중요하다.

---

## 4. AI 원리 관점 분석

| 항목 | 분석 |
|---|---|
| Training-time Attack | 추론 단계가 아니라 학습 과정 자체를 공격한다. |
| Data Poisoning | 샘플, 라벨, feature, augmentation을 조작한다. |
| Model Poisoning | federated/outsource setting에서 업데이트나 모델을 조작한다. |
| Clean-label Poisoning | 라벨 변경 없이 입력 feature를 조작한다. |
| Robust Training | 오염에 덜 민감한 학습을 시도한다. |
| Data Sanitization | 이상치·오염 샘플을 학습 전 제거한다. |

---

## 5. 보안 이슈 관점 분석

| 보안 항목 | Poisoning 관점 해석 |
|---|---|
| 데이터 무결성 | corpus, label, augmentation, model update가 보호 대상이다. |
| 모델 무결성 | 오염 학습은 decision boundary와 representation을 왜곡한다. |
| 가용성 | availability poisoning은 전체 성능을 저하시킨다. |
| 안전성 | targeted poisoning은 특정 조건에서 위험한 의사결정을 유도한다. |
| 책임성 | data provenance, training log, poison index, defense log가 필요하다. |

---

## 6. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 대상 | pretraining corpus, downstream dataset, label, augmentation, model update, checkpoint |
| 공격자 목표 | 성능 저하, 특정 target 오분류, trigger behavior, representation shift |
| 공격자 능력 | 데이터 삽입, 라벨 조작, feature 조작, federated update 조작, checkpoint 공급 |
| 공격 경로 | data/update → training objective → model representation → downstream output |
| 제외 범위 | 실제 데이터 공급망 공격, 무단 federated client 공격, 악성코드 실행 |

---

## 7. 평가방법 및 지표

| 지표 | 의미 | W05/P04에서의 활용 |
|---|---|---|
| Poison Rate | 오염 샘플 비율 | 공격 강도 |
| Clean Accuracy | 정상 성능 | utility 유지 |
| Accuracy Drop | 성능 저하 | availability attack 평가 |
| ASR | target/trigger 성공률 | integrity/backdoor 평가 |
| Detection Rate | 오염 샘플 탐지율 | 방어 성능 |
| FPR | 정상 샘플 오탐률 | 방어 부작용 |
| Representation Shift | 오염 전후 표현 변화 | SSL poisoning 영향 |
| Provenance Coverage | 데이터 출처 기록 정도 | 감사 가능성 |

---

## 8. 재현성 점검

| 항목 | 점검 |
|---|---|
| 데이터 | 공개 toy dataset 또는 SSL pretraining subset 사용 |
| 오염 설정 | poison rate, poison index, target label, trigger pattern 기록 |
| 모델 | encoder, downstream classifier, checkpoint version 기록 |
| 방어 | sanitization, robust training, detector 조건 기록 |
| 평가 | clean accuracy, ASR, detection rate, FPR, representation shift 저장 |
| 한계 | 실제 공격 절차가 아니라 안전한 toy/protocol 평가로 제한 |

---

## 9. 논문의 고유 기여

1. Training-time poisoning과 defense를 체계적으로 분류했다.
2. Data poisoning과 model poisoning을 구분해 학습 생명주기 위협면을 명확히 했다.
3. W05에서 SSL pretraining corpus와 foundation model supply chain의 보안 위험을 설명하는 핵심 근거가 된다.
4. 방어 평가에서 detection rate와 FPR을 함께 봐야 함을 시사한다.

---

## 10. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 표기 차이 | 강의계획서 제목/저자 표기와 정식 메타데이터가 다르다. | paper_list에 검증 메모 유지 |
| SSL 특화 부족 | 일반 poisoning survey라 SSL 전용 실험은 제한적이다. | P01/P03과 연결한다. |
| 최신 LLM/RAG 확장 필요 | LLM instruction data, RAG corpus poisoning은 추가 문헌 필요 | W07/W08/W14로 확장 |
| 악용 위험 | 구체 공격 절차는 부적절하다. | 위협모형과 방어 평가 중심으로 제한 |

---

## 11. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 2장 관련연구 | poisoning taxonomy와 defense taxonomy |
| 3장 위협모형 | data/model poisoning, federated/update 공격면 정의 |
| 4장 연구방법 | poison rate, ASR, detection rate, FPR 평가 설계 |
| 5장 분석 | SSL/foundation model pipeline의 poisoning 위험 비교표 |
| 6장 보안적 함의 | 데이터 무결성, 공급망, 감사 가능성 해석 |

---

## 12. 기말논문 연결 3문장

1. 이 주차에서 기말논문에 반영할 개념: SSL과 foundation model도 학습 데이터와 objective에 의존하므로 poisoning은 라벨 유무와 관계없이 representation을 왜곡할 수 있다.
2. 이 주차에서 기말논문에 반영할 표·그림·실험: poisoned training objective, poison rate, detection rate/FPR 수식, SSL poisoning 위협모형 표를 반영한다.
3. 이 주차가 RAG 문서 오염/LLM 보안 감사 프레임워크와 연결되는 지점: RAG corpus, embedding update, LLM fine-tuning data도 training-time 자산이므로 P04의 poisoning taxonomy를 W08/W14로 확장한다.

---

## 13. 최종 판단

P04는 W05의 핵심 보안 문헌이다. SSL 자체 문헌이 아니더라도 학습 단계 오염과 방어 taxonomy를 제공하므로 P01/P03의 SSL 원리와 결합해 사용한다.

---

## 14. 변환 호환성 메모

```bash
pandoc P04_summary.md -o P04_summary.docx
pandoc P04_summary.md -o P04_summary.pdf --pdf-engine=xelatex
```
