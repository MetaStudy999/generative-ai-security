# P05 Summary

## A Survey of Backdoor Attacks and Defences: From Deep Neural Networks to Large Language Models — Ling-Xin Jin et al., Journal of Electronic Science and Technology, 2025

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W05 자기지도학습·파운데이션 모델 & Poisoning/Backdoor |
| 논문명 | A survey of backdoor attacks and defences: From deep neural networks to large language models |
| 저자 | Ling-Xin Jin, Wei Jiang, Xiang-Yu Wen, Mei-Yu Lin, Jin-Yu Zhan, Xing-Zhi Zhou, Maregu Assefa Habtie, Naoufel Werghi |
| 학술지 | Journal of Electronic Science and Technology |
| 권호/쪽 | Vol. 23, No. 3, Article 100326 |
| 연도 | 2025 |
| DOI | https://doi.org/10.1016/j.jnlest.2025.100326 |
| 논문 유형 | Survey / Backdoor Attacks and Defences Review |
| 로컬 PDF | `01_papers/pdf/05_Jin_et_al_2025_Backdoor_Attacks_and_Defences_Survey.pdf` |
| 강의계획서 지정 논문과 일치 여부 | 제목은 일치. 강의계획서 `Z. Jin et al.` 표기는 출판사 기준 첫 저자명과 달라 확인 필요 |
| 핵심 근거 사용 가능 여부 | 가능 |
| 검증 메모 | W05 `paper_list.md` 기준 DOI, 제목, 저자, 학술지 확인 |

---

## 1. 한 문장 요약

이 논문은 DNN부터 LLM까지 backdoor attack, detection, removal, mitigation을 **trigger, target behavior, poisoning data, clean accuracy, attack success rate, stealthiness, defense success, LLM fine-tuning risk** 관점에서 정리하고, W05에서 clean performance와 hidden malicious behavior를 분리해야 함을 보여주는 핵심 보안 survey 논문이다.

---

## 2. 연구문제

> Backdoor 공격은 어떻게 모델에 조건부 악성 행동을 삽입하며, DNN과 LLM 환경에서 이를 어떤 지표와 절차로 탐지·제거·완화할 수 있는가?

| 번호 | 연구질문 |
|---|---|
| RQ1 | Backdoor trigger와 target behavior는 어떻게 정의되는가? |
| RQ2 | DNN backdoor와 LLM backdoor는 공격면과 방어면에서 어떻게 다른가? |
| RQ3 | Clean accuracy와 ASR을 분리해야 하는 이유는 무엇인가? |
| RQ4 | Detection, removal, mitigation은 어떤 지표로 평가해야 하는가? |
| RQ5 | SSL/foundation model pretraining과 fine-tuning 단계에서 backdoor 위험은 어떻게 확대되는가? |

---

## 3. 핵심 이론 및 수식

### 3.1 Backdoor Trigger Function

Backdoor는 정상 입력 $x$에 trigger 변환 $T(\cdot)$를 적용했을 때 목표 행동을 유도한다.

$$
\tilde{x}=T(x;\tau)
$$

| 기호 | 의미 |
|---|---|
| $x$ | 정상 입력 |
| $\tilde{x}$ | trigger가 포함된 입력 |
| $T$ | trigger 변환 함수 |
| $\tau$ | trigger pattern 또는 조건 |

---

### 3.2 Backdoor Objective

정상 성능과 trigger 조건 목표 행동을 동시에 학습하는 형태로 표현할 수 있다.

$$
\min_\theta
\left[
\sum_{(x,y)\in D_{clean}}\ell(f_\theta(x),y)
+\lambda\sum_{x\in D_{trigger}}\ell(f_\theta(T(x;\tau)),y_t)
\right]
$$

| 기호 | 의미 |
|---|---|
| $D_{clean}$ | 정상 데이터 |
| $D_{trigger}$ | trigger가 적용될 데이터 |
| $y_t$ | target label 또는 목표 행동 |
| $\lambda$ | backdoor 항의 가중치 |

### 보안적 의미

공격자는 정상 성능을 크게 해치지 않으면서 trigger 조건에서만 목표 행동을 유도하려 한다. 그래서 clean accuracy만 보면 공격이 숨겨질 수 있다.

---

### 3.3 Attack Success Rate

$$
ASR=\frac{1}{n}\sum_{i=1}^{n}\mathbf{1}\{f_\theta(T(x_i))=y_t\}
$$

| 기호 | 의미 |
|---|---|
| $ASR$ | Attack Success Rate |
| $T(x_i)$ | trigger 입력 |
| $y_t$ | target label 또는 실패 조건 |

---

### 3.4 Utility Drop과 Defense Success

$$
UtilityDrop=CleanAcc_{baseline}-CleanAcc_{defended}
$$

$$
ASRDrop=ASR_{before}-ASR_{after}
$$

| 기호 | 의미 |
|---|---|
| $UtilityDrop$ | 방어 후 정상 성능 저하 |
| $ASRDrop$ | 방어 후 공격 성공률 감소 |

### 보안적 의미

좋은 방어는 ASR을 낮추면서 clean utility를 크게 해치지 않아야 한다. 따라서 방어 평가는 detection rate, ASRDrop, utility drop을 함께 봐야 한다.

---

## 4. AI 원리 관점 분석

| 항목 | 분석 |
|---|---|
| Trigger Learning | 특정 pattern과 target behavior의 조건부 관계를 학습한다. |
| Representation Shift | trigger가 내부 표현을 특정 방향으로 이동시킬 수 있다. |
| Clean Utility | 정상 입력 성능은 유지될 수 있다. |
| LLM Backdoor | instruction tuning, LoRA, adapter, prompt trigger가 공격면이 된다. |
| Detection | activation clustering, spectral signature, trigger reverse engineering 등이 사용될 수 있다. |
| Removal | pruning, fine-tuning, unlearning, model editing 등이 검토된다. |

---

## 5. 보안 이슈 관점 분석

| 보안 항목 | Backdoor 관점 해석 |
|---|---|
| 무결성 | trigger 조건에서 모델 출력이 공격자 목표로 바뀐다. |
| 안전성 | 자율시스템, 보안관제, LLM agent에서 조건부 실패가 실제 피해로 이어질 수 있다. |
| 기밀성 | LLM backdoor는 특정 prompt 조건에서 민감정보 유출을 유도할 수 있다. |
| 공급망 보안 | pretrained model, checkpoint, adapter, fine-tuning data가 backdoor 경로가 될 수 있다. |
| 책임성 | trigger test, data provenance, model version, defense log가 필요하다. |

---

## 6. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 대상 | pretraining data, fine-tuning data, checkpoint, adapter, trigger test set, output behavior |
| 공격자 목표 | trigger 조건에서 target label/응답/action 유도 |
| 공격자 능력 | poisoned data 삽입, malicious checkpoint 제공, adapter 조작, prompt trigger 설계 |
| 공격 경로 | data/checkpoint/adapter → training/fine-tuning → model behavior → trigger activation |
| 제외 범위 | 실제 모델 backdoor 삽입, 무단 API 공격, 유해 trigger 배포 |

---

## 7. 평가방법 및 지표

| 지표 | 의미 | W05/P05에서의 활용 |
|---|---|---|
| Clean Accuracy | 정상 입력 성능 | utility 평가 |
| ASR | trigger 조건 목표 행동 발생률 | 핵심 backdoor 지표 |
| Utility Drop | 방어 후 clean 성능 저하 | 방어 부작용 |
| Detection Rate | backdoor 샘플/모델 탐지율 | 탐지 성능 |
| FPR | 정상 모델/샘플 오탐률 | 방어 부작용 |
| ASRDrop | 방어 전후 ASR 감소량 | 제거 효과 |
| Trigger Coverage | 다양한 trigger 조건 평가 범위 | 검증 충분성 |
| Auditability | 데이터·모델 출처와 검증 로그 | 공급망 감사 |

---

## 8. 재현성 점검

| 항목 | 점검 |
|---|---|
| 데이터 | 공개 toy dataset 또는 synthetic trigger set 사용 |
| trigger | 위치, 패턴, target label, activation condition 기록 |
| 모델 | clean model, backdoor condition model, defended model 분리 |
| 평가 | clean accuracy, ASR, detection rate, FPR, utility drop 저장 |
| LLM 범위 | LLM backdoor 실험은 비용·윤리 위험이 크므로 문헌 기반 비교 중심 |
| 한계 | toy trigger 결과를 실제 LLM/foundation model 보안성으로 일반화하지 않음 |

---

## 9. 논문의 고유 기여

1. Backdoor 공격과 방어를 DNN에서 LLM까지 확장해 정리한다.
2. Clean accuracy와 ASR 분리 평가의 필요성을 명확히 한다.
3. Detection, removal, mitigation 지표를 구분할 수 있게 한다.
4. W05에서 foundation model/LLM backdoor 위험을 설명하는 핵심 문헌이다.

---

## 10. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 최신성 변동 | LLM backdoor 연구는 빠르게 변화한다. | 최종 제출 전 최신 문헌 추가 확인 |
| 재현 비용 | LLM backdoor 실험은 GPU·데이터·윤리 비용이 크다. | toy DNN 또는 문헌 기반 비교로 제한 |
| 악용 위험 | 공격 절차를 상세화하면 부적절하다. | 평가 지표와 방어 검증 중심으로 작성 |
| Trigger 일반화 | 특정 trigger 결과가 다른 모델에 일반화되지 않는다. | trigger coverage와 한계를 명시 |

---

## 11. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | 정상 성능이 높아도 hidden trigger behavior가 있을 수 있다는 문제의식 |
| 2장 관련연구 | DNN-to-LLM backdoor taxonomy 정리 |
| 3장 위협모형 | trigger, target behavior, checkpoint, adapter 공격면 정의 |
| 4장 연구방법 | clean accuracy, ASR, detection rate, FPR, ASRDrop 평가 설계 |
| 6장 보안적 함의 | 무결성, 안전성, 공급망, 감사 가능성 해석 |

---

## 12. 기말논문 연결 3문장

1. 이 주차에서 기말논문에 반영할 개념: Backdoor는 정상 입력에서는 utility를 유지하면서 trigger 조건에서만 공격자 목표 행동을 유도하는 hidden behavior 위험이다.
2. 이 주차에서 기말논문에 반영할 표·그림·실험: trigger function, ASR 수식, utility drop/ASRDrop 수식, DNN-to-LLM backdoor 비교표를 반영한다.
3. 이 주차가 RAG 문서 오염/LLM 보안 감사 프레임워크와 연결되는 지점: LLM fine-tuning data, adapter, RAG 문서, prompt trigger가 hidden behavior를 유발할 수 있으므로 P05의 backdoor 평가축을 W08/W14로 확장한다.

---

## 13. 최종 판단

P05는 W05의 핵심 보안 문헌이다. SSL/foundation model이 pretraining·fine-tuning·adapter를 통해 확장될수록 backdoor 평가와 공급망 감사가 필수임을 보여준다.

---

## 14. 변환 호환성 메모

```bash
pandoc P05_summary.md -o P05_summary.docx
pandoc P05_summary.md -o P05_summary.pdf --pdf-engine=xelatex
```
