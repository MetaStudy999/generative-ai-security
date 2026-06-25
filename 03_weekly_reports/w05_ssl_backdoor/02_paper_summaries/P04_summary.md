# P04 Summary

## Threats to Training: A Survey of Poisoning Attacks and Defenses on Machine Learning Systems — Zhibo Wang, Jingjing Ma, Xue Wang, Jiahui Hu, Zhan Qin, Kui Ren, ACM Computing Surveys, 2022

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W05 자기지도학습·파운데이션 모델 & Poisoning/Backdoor |
| 강의계획서 표기 | Y. Wang et al., `A Survey of Poisoning Attacks and Defenses on Machine Learning` |
| 정식 제목 | Threats to Training: A Survey of Poisoning Attacks and Defenses on Machine Learning Systems |
| 저자 | Zhibo Wang, Jingjing Ma, Xue Wang, Jiahui Hu, Zhan Qin, Kui Ren |
| 공식 출판 정보 | ACM Computing Surveys, Vol. 55, No. 7, Article 134, pp. 1–36, 2022 |
| DOI | https://doi.org/10.1145/3538707 |
| 로컬 PDF | `01_papers/pdf/04_Wang_et_al_2022_Threats_to_Training_Poisoning_Survey.pdf` |
| 검증 상태 | W05 `paper_list.md`와 `download_source.md` 기준 DOI와 정식 제목 확인. 강의계획서의 `Y. Wang` 및 축약 제목과 동일 논문 여부는 최종 제출 전 확인 필요 |
| PDF 확인 메모 | repo의 PDF 폴더에 P04 관련 PDF blob이 존재함을 확인했다. 요약은 로컬 PDF 경로와 W05 `paper_list.md`, `download_source.md`의 공식 DOI 메타데이터 기준으로 보완했다. |
| 수식 호환성 | GitHub 수식 렌더링 오류 방지를 위해 `\operatorname`을 사용하지 않고, 긴 영문 subscript 대신 짧은 변수명과 표 설명을 사용했다. |
| 핵심 근거 사용 가능 여부 | 관련 보조 문헌으로 가능. W05에서 training-time poisoning, data poisoning, model poisoning, clean-label poisoning, defense detection, data sanitization, robust training, provenance audit의 핵심 보안 문헌으로 사용 |

---

## 1. 한 문장 요약

이 논문은 머신러닝 학습 단계의 poisoning 공격과 방어를 **data poisoning, label poisoning, feature poisoning, clean-label poisoning, targeted poisoning, availability poisoning, backdoor poisoning, model poisoning, federated/outsource learning threat, data sanitization, robust training, anomaly detection, provenance audit** 관점에서 체계화하며, W05에서는 SSL/foundation model의 pretraining corpus·augmentation·checkpoint·downstream data가 모두 학습 단계 공격면이 될 수 있음을 설명하는 핵심 보안 survey 문헌이다.

---

## 2. 핵심 연구문제

> Poisoning은 추론 단계 공격이 아니라 학습 과정 자체를 조작하는 공격이다. 공격자가 학습 데이터, 라벨, feature, augmentation, model update, checkpoint, federated client를 조작할 수 있으면 모델은 정상 성능을 유지하는 것처럼 보이면서도 특정 조건에서 실패하거나 전체 성능이 저하될 수 있다.

| 번호 | 연구질문 |
|---|---|
| RQ1 | Training-time poisoning은 data poisoning과 model poisoning으로 어떻게 구분되는가? |
| RQ2 | Availability attack, targeted attack, clean-label attack, backdoor attack은 공격 목표와 은닉성 측면에서 어떻게 다른가? |
| RQ3 | SSL pretraining corpus와 augmentation pipeline이 poisoning 공격면이 되는 이유는 무엇인가? |
| RQ4 | 방어는 data sanitization, robust training, anomaly detection, provenance monitoring으로 어떻게 구성되는가? |
| RQ5 | Clean accuracy, ASR, poison rate, detection rate, FPR, representation shift를 왜 함께 보고해야 하는가? |

---

## 3. 논문의 핵심 기여

| 기여 | 설명 | W05 연결 |
|---|---|---|
| Poisoning taxonomy | data poisoning, model poisoning, targeted/untargeted, clean-label/backdoor 공격을 분류 | W05 P04 핵심 |
| 학습 생명주기 관점 | 데이터 수집, 전처리, 학습, update, outsourcing, federated setting까지 확장 | foundation model supply chain 연결 |
| 방어 taxonomy | sanitization, robust training, outlier detection, provenance audit 등을 체계화 | 기말논문 방어 설계 |
| 평가 지표 강조 | poison rate, clean accuracy, ASR, detection rate, FPR을 분리 | 실험 지표 설계 |
| SSL 확장 가능성 | 라벨이 없는 pretraining에서도 corpus·augmentation·checkpoint 조작이 representation을 왜곡할 수 있음 | P01/P03와 결합 |
| RAG/LLM 연결성 | RAG corpus와 fine-tuning data도 training-time 자산으로 해석 가능 | W08/W14 연결 |

---

## 4. 목차별 핵심 개괄

| 목차 | 핵심 내용 | 비전공자용 이해 |
|---|---|---|
| 1. Introduction | 학습 과정에 오염이 들어가면 모델의 의사결정이 장기적으로 왜곡된다. | 모델이 처음 배울 때 잘못된 자료를 넣으면 나중에 계속 틀릴 수 있다. |
| 2. Threat Model | 공격자의 목표, 지식, 능력, 오염 위치, 학습 접근 범위를 정리한다. | 공격자가 무엇을 얼마나 조작할 수 있는지 정한다. |
| 3. Data Poisoning | 샘플, 라벨, feature, training set 일부를 조작하는 공격을 다룬다. | 학습 데이터 일부를 바꿔 모델을 속인다. |
| 4. Clean-label Poisoning | 라벨을 바꾸지 않고 입력 feature만 조작해 은닉성을 높인다. | 겉보기에는 정상 라벨이지만 내부 특징이 오염되어 있다. |
| 5. Backdoor Poisoning | trigger가 있을 때만 특정 behavior가 나오도록 학습한다. | 평소에는 정상, 특정 표시가 있을 때만 오작동한다. |
| 6. Model Poisoning | federated learning이나 outsourced training에서 update 또는 model을 조작한다. | 데이터가 아니라 모델 업데이트 자체를 조작한다. |
| 7. Defenses | data sanitization, robust training, anomaly detection, certified defense, provenance audit를 정리한다. | 이상 데이터를 제거하고 학습 과정을 기록한다. |
| 8. Challenges | adaptive attack, scalability, false positive, benchmark 표준화, supply-chain 문제가 남는다. | 공격과 방어가 계속 진화한다. |

---

## 5. 핵심 이론 및 수식

> 아래 수식은 poisoning 공격과 방어 평가를 W05 보고서에서 설명하기 위한 표준화된 표현이다. GitHub 호환성을 위해 `\operatorname`은 사용하지 않고, 수식은 Markdown 표 밖의 LaTeX block math로 작성한다.

### 5.1 Poisoned Training Objective

오염 데이터가 포함되면 학습 목적함수는 정상 데이터와 오염 데이터 손실을 함께 최소화한다.

$$
\min_{\theta}\left[\sum_{(x,y)\in D}\ell(f_{\theta}(x),y)+\lambda\sum_{(\tilde{x},\tilde{y})\in D_p}\ell(f_{\theta}(\tilde{x}),\tilde{y})\right]
$$

| 기호 | 의미 |
|---|---|
| $D$ | 정상 데이터 |
| $D_p$ | 오염 데이터 |
| $\lambda$ | 오염 항의 상대 가중치 |
| $f_{\theta}$ | 학습 모델 |
| $\ell$ | 손실함수 |

### 보안적 의미

공격자는 학습 목적함수에 오염 항을 삽입해 모델이 정상 성능은 유지하면서도 특정 조건에서 실패하도록 만들 수 있다.

---

### 5.2 Poison Rate

전체 학습 데이터 중 오염 데이터가 차지하는 비율이다.

$$
PoisonRate=\frac{|D_p|}{|D|+|D_p|}
$$

### 보안적 의미

낮은 poison rate에서도 높은 ASR이 나타나면 은닉성이 높은 공격이다. SSL 환경에서는 라벨이 없으므로 오염 여부가 더 늦게 발견될 수 있다.

---

### 5.3 Availability Attack Score

오염 후 정상 성능이 얼마나 떨어졌는지 측정한다.

$$
AccDrop=Acc_{clean}-Acc_{poison}
$$

| 기호 | 의미 |
|---|---|
| $Acc_{clean}$ | 정상 학습 조건의 성능 |
| $Acc_{poison}$ | 오염 학습 조건의 성능 |

### 보안적 의미

Availability poisoning은 특정 target만이 아니라 전체 모델 성능을 낮추는 공격이다. 성능 저하가 크면 서비스 가용성이 훼손된다.

---

### 5.4 Targeted Poisoning ASR

특정 target 조건에서 공격자가 원하는 behavior가 발생하는 비율이다.

$$
ASR_{poison}=\frac{N_{atk}}{N_{target}}
$$

| 기호 | 의미 |
|---|---|
| $N_{target}$ | target 또는 trigger 조건 평가 입력 수 |
| $N_{atk}$ | 공격 목표 behavior가 발생한 사례 수 |

### 보안적 의미

Clean accuracy가 유지되어도 ASR이 높으면 모델은 특정 조건에서 위험하다. Backdoor와 targeted poisoning 평가는 clean/attack 성능을 반드시 분리해야 한다.

---

### 5.5 Defense Detection Rate와 FPR

방어가 오염 샘플을 얼마나 잘 탐지하고 정상 샘플을 얼마나 적게 오탐하는지 평가한다.

$$
DetectionRate=\frac{TP_p}{TP_p+FN_p}
$$

$$
FPR=\frac{FP_c}{FP_c+TN_c}
$$

| 기호 | 의미 |
|---|---|
| $TP_p$ | 오염 샘플을 오염으로 탐지한 수 |
| $FN_p$ | 오염 샘플을 놓친 수 |
| $FP_c$ | 정상 샘플을 오염으로 오탐한 수 |
| $TN_c$ | 정상 샘플을 정상으로 판단한 수 |

### 보안적 의미

데이터 정제 방어는 오염 샘플을 잘 잡는 것뿐 아니라 정상 샘플을 과도하게 제거하지 않는 것도 중요하다.

---

### 5.6 Representation Shift

오염 학습 후 representation이 얼마나 달라졌는지 측정한다.

$$
RepShift=\frac{1}{N}\sum_{i=1}^{N}\left\|h_{clean}(x_i)-h_{poison}(x_i)\right\|_2
$$

### 보안적 의미

SSL과 foundation model에서는 downstream classifier보다 encoder representation이 먼저 오염될 수 있다. Representation shift는 poisoning의 중간 증거로 활용할 수 있다.

---

### 5.7 Defense Utility Score

방어 성능은 탐지율뿐 아니라 clean utility와 오탐 부작용을 함께 봐야 한다.

$$
DefenseUtility=DetectionRate-\lambda_1FPR-\lambda_2AccDrop
$$

### 보안적 의미

방어가 공격을 잘 잡더라도 정상 데이터를 대량 제거하거나 성능을 낮추면 실제 학습 파이프라인에 적용하기 어렵다.

---

### 5.8 Poisoning Pipeline Risk

학습 파이프라인의 poisoning 위험을 데이터, 라벨, feature, update, checkpoint, provenance 위험으로 요약한다.

$$
PoisoningRisk=DataRisk+LabelRisk+FeatureRisk+UpdateRisk+CheckpointRisk-ProvenanceCoverage
$$

### 보안적 의미

Poisoning 방어는 모델 학습 코드만 검사해서는 부족하다. data provenance, label source, augmentation, update log, checkpoint lineage를 함께 관리해야 한다.

---

## 6. AI 원리 70% 관점 분석

| 원리 항목 | 설명 | W05/P04에서의 의미 |
|---|---|---|
| Training-time Attack | 추론 단계가 아니라 학습 과정 자체를 공격 | poisoning의 핵심 정의 |
| Data Poisoning | 샘플, 라벨, feature, augmentation을 조작 | corpus 무결성 문제 |
| Model Poisoning | federated/outsource setting에서 update나 모델 조작 | 공급망·분산학습 위험 |
| Clean-label Poisoning | 라벨 변경 없이 입력 feature를 조작 | 은닉성 높은 공격 |
| Targeted Poisoning | 특정 target 조건에서만 실패 유도 | ASR 분리 평가 필요 |
| Availability Poisoning | 전체 성능 저하 유도 | 가용성 평가 |
| Robust Training | 오염에 덜 민감한 학습 시도 | 방어 방법 |
| Data Sanitization | 이상치·오염 샘플을 학습 전 제거 | FPR 관리 필요 |

---

## 7. 보안 이슈 30% 관점 분석

| 보안 항목 | Poisoning 관점 해석 | 대표 평가 지표 |
|---|---|---|
| 데이터 무결성 | corpus, label, feature, augmentation, model update가 보호 대상 | PoisonRate, provenance coverage |
| 모델 무결성 | 오염 학습은 decision boundary와 representation을 왜곡 | ASR_poison, RepShift |
| 가용성 | availability poisoning은 전체 성능을 저하시킴 | AccDrop |
| 안전성 | targeted poisoning은 특정 조건에서 위험한 의사결정 유도 | ASR_poison, high-risk case review |
| 기밀성 | data source와 poisoning audit log가 민감정보를 포함할 수 있음 | safe logging, access control |
| 책임성 | data provenance, training log, poison index, defense log가 필요 | audit completeness |

---

## 8. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 대상 | pretraining corpus, downstream dataset, label, feature, augmentation, model update, checkpoint, training log |
| 공격자 목표 | 성능 저하, 특정 target 오분류, trigger behavior, representation shift, downstream transfer failure |
| 공격자 능력 | 데이터 삽입, 라벨 조작, feature 조작, federated update 조작, checkpoint 공급, outsourced training 조작 |
| 공격 경로 | data/update/checkpoint → training objective → model representation → downstream output |
| 방어자 능력 | data lineage, sanitization, robust training, anomaly detection, checkpoint verification, training audit |
| 제외 범위 | 실제 데이터 공급망 공격, 무단 federated client 공격, 악성코드 실행, 공격 절차 상세화 |

---

## 9. 평가방법 및 지표

| 평가축 | 지표 | 의미 | W05/P04 활용 |
|---|---|---|---|
| 공격 강도 | PoisonRate | 오염 샘플 비율 | 공격 조건 기록 |
| 정상 성능 | Clean Accuracy | 정상 성능 | utility 유지 |
| 가용성 | AccDrop | 오염 후 성능 저하 | availability attack 평가 |
| 표적 공격 | ASR_poison | target/trigger 성공률 | integrity/backdoor 평가 |
| 방어 탐지 | DetectionRate | 오염 샘플 탐지율 | 방어 성능 |
| 방어 부작용 | FPR | 정상 샘플 오탐률 | sanitization 부작용 |
| 표현 변화 | RepShift | 오염 전후 표현 변화 | SSL poisoning 영향 |
| 감사성 | ProvenanceCoverage | 데이터 출처 기록 정도 | W14/W15 연결 |

---

## 10. 재현성 체크리스트

| 항목 | 기록해야 할 내용 |
|---|---|
| Bibliographic status | DOI, ACM CSUR 출판정보, 강의계획서 표기 차이, 로컬 PDF 상태 |
| Data | 공개 toy dataset 또는 SSL pretraining subset 사용, 개인정보 제외 |
| Poison setting | poison rate, poison index, target label, trigger 조건, random seed |
| Model | encoder, downstream classifier, checkpoint version, optimizer config |
| Defense | sanitization, robust training, detector threshold, checkpoint verification 조건 |
| Evaluation | clean accuracy, AccDrop, ASR_poison, DetectionRate, FPR, RepShift 분리 저장 |
| Evidence | data source, poison config, training log, defense log, metric CSV/JSON, script commit |
| Limitation | 실제 공격 절차가 아니라 안전한 toy/protocol 평가로 제한 |
| GitHub math | `\operatorname` 사용 금지, 긴 영문 subscript 대신 짧은 변수명과 표 설명 사용 |

---

## 11. 논문의 고유 기여

1. Training-time poisoning과 defense를 체계적으로 분류했다.
2. Data poisoning과 model poisoning을 구분해 학습 생명주기 위협면을 명확히 했다.
3. W05에서 SSL pretraining corpus와 foundation model supply chain의 보안 위험을 설명하는 핵심 근거가 된다.
4. 방어 평가에서 detection rate와 FPR을 함께 봐야 함을 시사한다.
5. W08 RAG corpus poisoning, W14 MLOps training pipeline, W15 evidence chain으로 확장 가능한 공통 위협모형을 제공한다.

---

## 12. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 표기 차이 | 강의계획서 제목/저자 표기와 정식 메타데이터가 다르다. | `paper_list.md` 검증 메모 유지 |
| SSL 특화 부족 | 일반 poisoning survey라 SSL 전용 실험은 제한적이다. | P01/P03과 연결 |
| 최신 LLM/RAG 확장 필요 | LLM instruction data, RAG corpus poisoning은 추가 문헌 필요 | W07/W08/W14로 확장 |
| 악용 위험 | 구체 공격 절차는 부적절하다. | 위협모형과 방어 평가 중심으로 제한 |
| 방어 오탐 문제 | data sanitization은 정상 샘플 제거로 성능 저하를 만들 수 있다. | DetectionRate와 FPR 동시 보고 |
| 공급망 복잡성 | checkpoint, outsourced training, federated update provenance 확인이 어렵다. | checkpoint hash와 training log 기록 강화 |

---

## 13. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | foundation model과 SSL/RAG pipeline에서 학습 데이터 무결성이 핵심 보안 문제라는 문제의식 |
| 2장 관련연구 | poisoning taxonomy와 defense taxonomy 정리 |
| 3장 위협모형 | data/model poisoning, label/feature 조작, federated/update 공격면 정의 |
| 4장 연구방법 | poisoned training objective, PoisonRate, AccDrop, ASR_poison, DetectionRate, FPR, RepShift 지표 설계 |
| 5장 분석 | SSL/foundation model pipeline의 poisoning risk matrix 제시 |
| 6장 보안적 함의 | 데이터 무결성, 모델 공급망, checkpoint provenance, 감사 가능성 해석 |
| 부록 | poison config, data lineage, checkpoint hash, defense log, metric CSV 수록 |

---

## 14. 기말논문 연결 3문장

1. W05에서 기말논문에 반영할 개념: SSL과 foundation model도 학습 데이터와 objective에 의존하므로 poisoning은 라벨 유무와 관계없이 representation을 왜곡할 수 있다.
2. W05에서 기말논문에 반영할 표·그림·실험: poisoned training objective, PoisonRate, AccDrop, ASR_poison, DetectionRate, FPR, RepShift 수식표와 SSL poisoning 위협모형 표를 반영한다.
3. W05가 W08/W14와 연결되는 지점: RAG corpus, embedding update, LLM fine-tuning data도 training-time 자산이므로 P04의 poisoning taxonomy를 RAG 문서 오염과 MLOps training audit 구조로 확장한다.

---

## 15. 최종 판단

P04는 W05의 핵심 보안 문헌이다. SSL 자체 문헌은 아니지만, 학습 데이터와 모델 update가 오염될 때 downstream representation과 decision boundary가 어떻게 왜곡될 수 있는지를 설명한다. 따라서 기말논문에서는 P04를 **training-time poisoning taxonomy, data/model poisoning, clean-label/backdoor 공격면, defense detection/FPR, data provenance audit의 중심 근거 문헌**으로 사용하는 것이 적절하다.

---

## 16. GitHub 수식 호환성 메모

이 파일에서는 GitHub 수식 렌더링 오류 방지를 위해 `\operatorname`을 사용하지 않는다.

| 피해야 할 표현 | 권장 표현 |
|---|---|
| `TP_{poison}` | `TP_p`처럼 짧은 변수명 사용 후 표에서 의미 설명 |
| `FN_{poison}` | `FN_p`처럼 짧은 변수명 사용 후 표에서 의미 설명 |
| `FP_{clean}` | `FP_c`처럼 짧은 변수명 사용 후 표에서 의미 설명 |
| `TN_{clean}` | `TN_c`처럼 짧은 변수명 사용 후 표에서 의미 설명 |
| 긴 영문 subscript | 짧은 변수명 사용 후 표에서 의미 설명 |

```bash
pandoc P04_summary.md -o P04_summary.docx
pandoc P04_summary.md -o P04_summary.pdf --pdf-engine=xelatex
```
