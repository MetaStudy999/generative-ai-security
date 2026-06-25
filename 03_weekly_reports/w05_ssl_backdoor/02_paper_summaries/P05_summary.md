# P05 Summary

## A Survey of Backdoor Attacks and Defences: From Deep Neural Networks to Large Language Models — Ling-Xin Jin et al., Journal of Electronic Science and Technology, 2025

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W05 자기지도학습·파운데이션 모델 & Poisoning/Backdoor |
| 논문명 | A survey of backdoor attacks and defences: From deep neural networks to large language models |
| 저자 | Ling-Xin Jin, Wei Jiang, Xiang-Yu Wen, Mei-Yu Lin, Jin-Yu Zhan, Xing-Zhi Zhou, Maregu Assefa Habtie, Naoufel Werghi |
| 공식 출판 정보 | Journal of Electronic Science and Technology, Vol. 23, No. 3, Article 100326, 2025 |
| DOI | https://doi.org/10.1016/j.jnlest.2025.100326 |
| 로컬 PDF | `01_papers/pdf/05_Jin_et_al_2025_Backdoor_Attacks_and_Defences_Survey.pdf` |
| 검증 상태 | W05 `paper_list.md`와 `download_source.md` 기준 DOI, 제목, 저자, 학술지 확인. 강의계획서의 `Z. Jin et al.` 표기는 출판사 기준 첫 저자명과 달라 확인 메모 유지 |
| PDF 확인 메모 | repo의 PDF 폴더에 P05 관련 PDF blob이 존재함을 확인했다. 요약은 로컬 PDF 경로와 W05 `paper_list.md`, `download_source.md`의 공식 DOI 메타데이터 기준으로 보완했다. |
| 수식 호환성 | GitHub 수식 렌더링 오류 방지를 위해 `\operatorname`을 사용하지 않고, 긴 영문 subscript 대신 짧은 변수명과 표 설명을 사용했다. |
| 핵심 근거 사용 가능 여부 | 가능. W05에서 DNN-to-LLM backdoor taxonomy, trigger, target behavior, ASR, clean utility, detection/removal/mitigation, LLM fine-tuning/adapters/checkpoint supply-chain risk를 설명하는 핵심 보안 문헌으로 사용 |

---

## 1. 한 문장 요약

이 논문은 DNN부터 LLM까지 backdoor attack과 defence를 **trigger, target behavior, poisoned data, clean accuracy, attack success rate, stealthiness, detection, removal, mitigation, model supply chain, adapter/LoRA risk, prompt trigger, instruction-tuning backdoor** 관점에서 정리하며, W05에서는 정상 성능이 높아도 특정 trigger 조건에서만 악성 행동이 나타나는 **hidden behavior**를 clean utility와 ASR로 분리 평가해야 함을 보여주는 핵심 보안 survey 문헌이다.

---

## 2. 핵심 연구문제

> Backdoor 공격은 모델이 정상 입력에서는 정상적으로 동작하지만, 특정 trigger 조건에서는 공격자 목표 행동을 하도록 학습시키는 training-time 또는 supply-chain 위협이다. DNN에서는 이미지 patch, feature trigger, label manipulation이 중심이고, LLM에서는 fine-tuning data, instruction template, adapter, checkpoint, prompt pattern이 공격면이 될 수 있다.

| 번호 | 연구질문 |
|---|---|
| RQ1 | Backdoor trigger와 target behavior는 어떻게 정의되는가? |
| RQ2 | DNN backdoor와 LLM backdoor는 공격면과 방어면에서 어떻게 다른가? |
| RQ3 | Clean accuracy와 ASR을 분리해야 하는 이유는 무엇인가? |
| RQ4 | Detection, removal, mitigation은 어떤 지표로 평가해야 하는가? |
| RQ5 | SSL/foundation model pretraining, fine-tuning, adapter, RAG 문서, prompt template 단계에서 backdoor 위험은 어떻게 확대되는가? |

---

## 3. 논문의 핵심 기여

| 기여 | 설명 | W05 연결 |
|---|---|---|
| DNN-to-LLM backdoor taxonomy | 기존 DNN backdoor에서 LLM backdoor까지 공격면을 확장해 정리 | W05 P05 핵심 |
| Trigger 중심 위협모형 | trigger pattern, activation condition, target behavior를 분리 | 실험 설계 근거 |
| Clean/attack 성능 분리 | clean accuracy와 ASR을 별도 지표로 평가해야 함을 강조 | backdoor 평가 핵심 |
| 방어 방법 체계화 | detection, removal, mitigation, robust training, model inspection 정리 | 방어 평가 설계 |
| 공급망 관점 제공 | pretrained checkpoint, adapter, fine-tuning data, instruction data가 위험 경로가 될 수 있음 | W14/W15 evidence chain 연결 |
| LLM 보안 확장 | prompt trigger, instruction tuning, hidden behavior 위험을 LLM 환경으로 확장 | W07/W08 연결 |

---

## 4. 목차별 핵심 개괄

| 목차 | 핵심 내용 | 비전공자용 이해 |
|---|---|---|
| 1. Introduction | Backdoor는 정상 상황에서는 숨어 있다가 특정 조건에서만 작동하는 모델 위협이다. | 평소에는 멀쩡하지만 특정 표시가 있으면 잘못 행동하는 모델이다. |
| 2. Background | DNN, LLM, training-time attack, trigger, target label, poisoning 개념을 설명한다. | 모델이 학습될 때 몰래 조건부 행동을 넣는 구조다. |
| 3. Backdoor Attacks on DNNs | 이미지·음성·텍스트 모델에서 trigger 삽입과 target behavior를 정리한다. | 특정 패턴이 들어간 입력을 보면 틀리게 만들 수 있다. |
| 4. Backdoor Attacks on LLMs | instruction tuning, fine-tuning data, prompt trigger, adapter, model supply chain 위험을 다룬다. | LLM도 특정 문장·형식·adapter 때문에 숨은 행동을 할 수 있다. |
| 5. Detection | activation analysis, anomaly detection, trigger reverse search, spectral/representation analysis를 정리한다. | 모델 내부나 데이터에서 이상한 패턴을 찾는다. |
| 6. Removal and Mitigation | pruning, fine-tuning, unlearning, model editing, input filtering, robust training을 다룬다. | 숨은 행동을 제거하거나 작동하지 못하게 한다. |
| 7. Evaluation | clean accuracy, ASR, utility drop, ASR drop, FPR, trigger coverage를 함께 평가한다. | 정상 성능과 공격 조건 성능을 따로 봐야 한다. |
| 8. Challenges | adaptive trigger, stealthiness, transferability, LLM-scale 재현성, ethical risk가 남는다. | 공격은 숨기 쉬우며 대형 모델에서 검증이 어렵다. |

---

## 5. 핵심 이론 및 수식

> 아래 수식은 backdoor 공격과 방어 평가를 W05 보고서에서 설명하기 위한 표준화된 표현이다. GitHub 호환성을 위해 `\operatorname`은 사용하지 않고, 수식은 Markdown 표 밖의 LaTeX block math로 작성한다.

### 5.1 Backdoor Trigger Function

Backdoor는 정상 입력 $x$에 trigger 변환 $T$를 적용했을 때 목표 행동을 유도한다.

$$
\tilde{x}=T(x;\tau)
$$

| 기호 | 의미 |
|---|---|
| $x$ | 정상 입력 |
| $\tilde{x}$ | trigger가 포함된 입력 |
| $T$ | trigger 변환 함수 |
| $\tau$ | trigger pattern 또는 조건 |

### 보안적 의미

Trigger는 이미지 patch, 특정 token, 문장 구조, prompt template, adapter 조건처럼 다양한 형태가 될 수 있다. 따라서 방어자는 단일 trigger만이 아니라 여러 조건을 테스트해야 한다.

---

### 5.2 Backdoor Objective

정상 성능과 trigger 조건 목표 행동을 동시에 학습하는 형태로 표현할 수 있다.

$$
\min_{\theta}\left[\sum_{(x,y)\in D_c}\ell(f_{\theta}(x),y)+\lambda\sum_{x\in D_t}\ell(f_{\theta}(T(x;\tau)),y_t)\right]
$$

| 기호 | 의미 |
|---|---|
| $D_c$ | clean data |
| $D_t$ | trigger가 적용될 data |
| $y_t$ | target label 또는 target behavior |
| $\lambda$ | backdoor 항의 가중치 |
| $f_{\theta}$ | 학습 모델 |

### 보안적 의미

공격자는 정상 성능을 크게 해치지 않으면서 trigger 조건에서만 목표 행동을 유도하려 한다. 그래서 clean accuracy만 보면 공격이 숨겨질 수 있다.

---

### 5.3 Attack Success Rate

Trigger 조건에서 target behavior가 나타나는 비율이다.

$$
ASR=\frac{1}{N}\sum_{i=1}^{N}\mathbf{1}\left[f_{\theta}(T(x_i;\tau))=y_t\right]
$$

| 기호 | 의미 |
|---|---|
| $ASR$ | Attack Success Rate |
| $N$ | trigger 평가 입력 수 |
| $T(x_i;\tau)$ | trigger가 적용된 입력 |
| $y_t$ | target label 또는 target behavior |

### 보안적 의미

Clean accuracy가 높아도 ASR이 높으면 모델은 특정 조건에서 위험하다. Backdoor 평가에서는 clean 성능과 trigger 조건 성능을 반드시 분리해야 한다.

---

### 5.4 Utility Drop과 ASR Drop

방어 전후 정상 성능 저하와 공격 성공률 감소를 함께 본다.

$$
UtilityDrop=CleanAcc_{base}-CleanAcc_{def}
$$

$$
ASRDrop=ASR_{before}-ASR_{after}
$$

| 기호 | 의미 |
|---|---|
| $CleanAcc_{base}$ | 방어 전 기준 clean accuracy |
| $CleanAcc_{def}$ | 방어 후 clean accuracy |
| $ASR_{before}$ | 방어 전 attack success rate |
| $ASR_{after}$ | 방어 후 attack success rate |

### 보안적 의미

좋은 방어는 ASR을 낮추면서 clean utility를 크게 해치지 않아야 한다. 따라서 방어 평가는 ASRDrop과 UtilityDrop을 함께 봐야 한다.

---

### 5.5 Backdoor Detection Rate와 FPR

Backdoor sample 또는 backdoored model을 탐지하는 성능은 탐지율과 오탐률을 함께 본다.

$$
DetectionRate=\frac{TP_b}{TP_b+FN_b}
$$

$$
FPR=\frac{FP_c}{FP_c+TN_c}
$$

| 기호 | 의미 |
|---|---|
| $TP_b$ | backdoor를 backdoor로 탐지한 수 |
| $FN_b$ | backdoor를 놓친 수 |
| $FP_c$ | clean sample/model을 backdoor로 오탐한 수 |
| $TN_c$ | clean sample/model을 clean으로 판단한 수 |

### 보안적 의미

Backdoor detector가 정상 모델을 과도하게 오탐하면 운영 적용이 어렵다. DetectionRate와 FPR을 동시에 보고해야 한다.

---

### 5.6 Trigger Coverage

방어 평가가 여러 trigger 유형을 얼마나 포괄하는지 측정한다.

$$
TriggerCoverage=\frac{|Trig_{tested}|}{|Trig_{risk}|}
$$

| 기호 | 의미 |
|---|---|
| $Trig_{tested}$ | 실제 평가한 trigger 유형 집합 |
| $Trig_{risk}$ | threat model상 고려해야 할 trigger 유형 집합 |

### 보안적 의미

하나의 trigger에서 ASR이 낮아도 다른 trigger에서 실패할 수 있다. LLM에서는 phrase, format, role, instruction, adapter 조건까지 trigger 범위가 넓다.

---

### 5.7 Backdoor Defense Score

방어 품질은 ASR 감소, clean utility 유지, 오탐률을 함께 반영한다.

$$
DefenseScore=ASRDrop-\lambda_1UtilityDrop-\lambda_2FPR
$$

### 보안적 의미

ASR만 낮추는 방어는 충분하지 않다. 정상 성능과 오탐 부작용을 함께 관리해야 한다.

---

### 5.8 LLM Backdoor Risk

LLM 환경의 backdoor 위험을 fine-tuning data, adapter, checkpoint, prompt trigger, output risk로 요약한다.

$$
LLMBackdoorRisk=DataRisk+AdapterRisk+CheckpointRisk+PromptRisk+OutputRisk-AuditCoverage
$$

### 보안적 의미

LLM backdoor는 데이터뿐 아니라 adapter, LoRA, checkpoint, prompt template, RAG 문서에서도 발생할 수 있다. model card, checkpoint hash, fine-tuning data lineage, trigger test log가 필요하다.

---

## 6. AI 원리 70% 관점 분석

| 원리 항목 | 설명 | W05/P05에서의 의미 |
|---|---|---|
| Trigger Learning | 특정 pattern과 target behavior의 조건부 관계 학습 | hidden behavior 핵심 |
| Representation Shift | trigger가 내부 표현을 특정 방향으로 이동 | detection/analysis 근거 |
| Clean Utility | 정상 입력 성능은 유지될 수 있음 | clean accuracy만으로 부족 |
| DNN Backdoor | 이미지·음성·텍스트 trigger 기반 공격 | 전통적 backdoor 배경 |
| LLM Backdoor | instruction tuning, LoRA, adapter, prompt trigger가 공격면 | W07/W08 연결 |
| Detection | activation clustering, anomaly analysis, trigger search 등 | 방어 평가 |
| Removal | pruning, fine-tuning, unlearning, model editing | ASRDrop/UtilityDrop 필요 |
| Supply Chain | checkpoint, adapter, fine-tuning data lineage | W14/W15 연결 |

---

## 7. 보안 이슈 30% 관점 분석

| 보안 항목 | Backdoor 관점 해석 | 대표 평가 지표 |
|---|---|---|
| 무결성 | trigger 조건에서 모델 출력이 공격자 목표로 바뀜 | ASR, ASRDrop |
| 안전성 | 자율시스템, 보안관제, LLM agent에서 조건부 실패가 실제 피해로 이어질 수 있음 | high-risk trigger test |
| 기밀성 | LLM backdoor는 특정 prompt 조건에서 민감정보 유출을 유도할 수 있음 | leakage test |
| 가용성 | 과도한 방어가 clean utility를 떨어뜨릴 수 있음 | UtilityDrop |
| 공급망 보안 | pretrained model, checkpoint, adapter, fine-tuning data가 backdoor 경로가 됨 | checkpoint lineage, audit coverage |
| 책임성 | trigger test, data provenance, model version, defense log가 필요 | AuditCoverage |

---

## 8. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 대상 | pretraining data, fine-tuning data, checkpoint, adapter, LoRA, prompt template, trigger test set, output behavior |
| 공격자 목표 | trigger 조건에서 target label, target response, unsafe action, leakage behavior 유도 |
| 공격자 능력 | poisoned data 삽입, malicious checkpoint 제공, adapter 조작, prompt trigger 설계, fine-tuning corpus 오염 |
| 공격 경로 | data/checkpoint/adapter → training/fine-tuning → model behavior → trigger activation → unsafe output/action |
| 방어자 능력 | data lineage, checkpoint verification, trigger testing, activation analysis, model inspection, defense fine-tuning, human review |
| 제외 범위 | 실제 모델 backdoor 삽입, 무단 API 공격, 유해 trigger 배포, 공격 절차 상세화 |

---

## 9. 평가방법 및 지표

| 평가축 | 지표 | 의미 | W05/P05 활용 |
|---|---|---|---|
| 정상 성능 | Clean Accuracy | 정상 입력 성능 | utility 평가 |
| 공격 성공 | ASR | trigger 조건 목표 행동 발생률 | 핵심 backdoor 지표 |
| 방어 부작용 | UtilityDrop | 방어 후 clean 성능 저하 | 실용성 평가 |
| 탐지 성능 | DetectionRate | backdoor 샘플/모델 탐지율 | 탐지 평가 |
| 오탐 | FPR | 정상 모델/샘플 오탐률 | 운영 부작용 |
| 제거 효과 | ASRDrop | 방어 전후 ASR 감소량 | removal/mitigation 평가 |
| 검증 범위 | TriggerCoverage | 다양한 trigger 조건 평가 범위 | 검증 충분성 |
| 감사성 | AuditCoverage | 데이터·모델 출처와 검증 로그 | 공급망 감사 |

---

## 10. 재현성 체크리스트

| 항목 | 기록해야 할 내용 |
|---|---|
| Bibliographic status | DOI, Journal of Electronic Science and Technology 출판정보, 강의계획서 표기 차이, 로컬 PDF 상태 |
| Data | 공개 toy dataset 또는 synthetic trigger set 사용, 개인정보 제외 |
| Trigger | trigger 유형, 위치, pattern, target label/response, activation condition |
| Model | clean model, backdoor condition model, defended model, checkpoint hash |
| LLM setting | LLM backdoor 실험은 비용·윤리 위험이 크므로 문헌 기반 비교 중심으로 제한 |
| Evaluation | Clean Accuracy, ASR, DetectionRate, FPR, UtilityDrop, ASRDrop, TriggerCoverage |
| Defense | detection, removal, mitigation 방법과 threshold, fine-tuning setting |
| Evidence | trigger test set, model version, data lineage, defense log, metric CSV/JSON, limitation statement |
| Limitation | toy trigger 결과를 실제 LLM/foundation model 보안성으로 일반화하지 않음 |
| GitHub math | `\operatorname` 사용 금지, 긴 영문 subscript 대신 짧은 변수명과 표 설명 사용 |

---

## 11. 논문의 고유 기여

1. Backdoor 공격과 방어를 DNN에서 LLM까지 확장해 정리한다.
2. Clean accuracy와 ASR 분리 평가의 필요성을 명확히 한다.
3. Detection, removal, mitigation을 구분하고 각 단계의 평가 지표를 정리한다.
4. W05에서 foundation model/LLM backdoor 위험을 설명하는 핵심 문헌이다.
5. W07 LLM 보안, W08 RAG 문서 오염, W14 MLOps 공급망, W15 evidence chain으로 확장 가능한 hidden behavior 평가 프레임을 제공한다.

---

## 12. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 최신성 변동 | LLM backdoor 연구는 빠르게 변화한다. | 최종 제출 전 최신 문헌 추가 확인 |
| 재현 비용 | LLM backdoor 실험은 GPU·데이터·윤리 비용이 크다. | toy DNN 또는 문헌 기반 비교로 제한 |
| 악용 위험 | 공격 절차를 상세화하면 부적절하다. | 평가 지표와 방어 검증 중심으로 작성 |
| Trigger 일반화 | 특정 trigger 결과가 다른 모델에 일반화되지 않는다. | TriggerCoverage와 한계 명시 |
| 방어 부작용 | pruning/fine-tuning/removal이 clean utility를 떨어뜨릴 수 있다. | UtilityDrop 동시 보고 |
| 공급망 복잡성 | adapter, checkpoint, fine-tuning data provenance 확인이 어렵다. | checkpoint hash와 data lineage 기록 강화 |

---

## 13. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | 정상 성능이 높아도 hidden trigger behavior가 있을 수 있다는 문제의식 |
| 2장 관련연구 | DNN-to-LLM backdoor taxonomy 정리 |
| 3장 위협모형 | trigger, target behavior, checkpoint, adapter, fine-tuning data 공격면 정의 |
| 4장 연구방법 | trigger function, backdoor objective, ASR, DetectionRate, FPR, UtilityDrop, ASRDrop, TriggerCoverage 지표 설계 |
| 5장 분석 | clean utility와 hidden behavior를 분리한 backdoor evaluation matrix 제시 |
| 6장 보안적 함의 | 무결성, 안전성, 공급망, LLM adapter risk, 감사 가능성 해석 |
| 부록 | trigger test condition, model/checkpoint hash, defense log, metric CSV, limitation statement 수록 |

---

## 14. 기말논문 연결 3문장

1. W05에서 기말논문에 반영할 개념: Backdoor는 정상 입력에서는 utility를 유지하면서 trigger 조건에서만 공격자 목표 행동을 유도하는 hidden behavior 위험이다.
2. W05에서 기말논문에 반영할 표·그림·실험: trigger function, backdoor objective, ASR, DetectionRate/FPR, UtilityDrop/ASRDrop, LLMBackdoorRisk 수식표와 DNN-to-LLM backdoor 비교표를 반영한다.
3. W05가 W08/W14와 연결되는 지점: LLM fine-tuning data, adapter, RAG 문서, prompt template, checkpoint supply chain이 hidden behavior를 유발할 수 있으므로 P05의 backdoor 평가축을 RAG 문서 오염과 MLOps audit 구조로 확장한다.

---

## 15. 최종 판단

P05는 W05의 핵심 보안 문헌이다. Backdoor는 clean accuracy가 높아도 trigger 조건에서만 위험 행동이 나타나는 hidden behavior 문제이므로, SSL/foundation model 보안 평가에서 반드시 별도 지표로 다뤄야 한다. 따라서 기말논문에서는 P05를 **DNN-to-LLM backdoor taxonomy, trigger/target behavior, ASR, detection/removal/mitigation, adapter/checkpoint supply-chain risk, audit evidence의 중심 근거 문헌**으로 사용하는 것이 적절하다.

---

## 16. GitHub 수식 호환성 메모

이 파일에서는 GitHub 수식 렌더링 오류 방지를 위해 `\operatorname`을 사용하지 않는다.

| 피해야 할 표현 | 권장 표현 |
|---|---|
| `TP_{backdoor}` | `TP_b`처럼 짧은 변수명 사용 후 표에서 의미 설명 |
| `FN_{backdoor}` | `FN_b`처럼 짧은 변수명 사용 후 표에서 의미 설명 |
| `FP_{clean}` | `FP_c`처럼 짧은 변수명 사용 후 표에서 의미 설명 |
| `TN_{clean}` | `TN_c`처럼 짧은 변수명 사용 후 표에서 의미 설명 |
| 긴 영문 subscript | 짧은 변수명 사용 후 표에서 의미 설명 |

```bash
pandoc P05_summary.md -o P05_summary.docx
pandoc P05_summary.md -o P05_summary.pdf --pdf-engine=xelatex
```
