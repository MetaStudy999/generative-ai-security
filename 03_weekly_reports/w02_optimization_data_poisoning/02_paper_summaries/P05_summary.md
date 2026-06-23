# P05 Summary

## A Survey of Backdoor Attacks and Defences: From Deep Neural Networks to Large Language Models — Ling-Xin Jin et al., Journal of Electronic Science and Technology, 2025

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W02 대규모 최적화 & 데이터 오염 위협 |
| 논문명 | A survey of backdoor attacks and defences: From deep neural networks to large language models |
| 저자 | Ling-Xin Jin et al. |
| 학술지 | Journal of Electronic Science and Technology |
| 권호/쪽 | Vol. 23, Article 100326 |
| 연도 | 2025 |
| DOI | https://doi.org/10.1016/j.jnlest.2025.100326 |
| 논문 유형 | Survey / Backdoor Attacks and Defences Review |
| 로컬 PDF | `01_papers/pdf/05_Jin_et_al_2025_Backdoor_Attacks_and_Defences_Survey.pdf` |
| 강의계획서 지정 논문과 일치 여부 | 일치. 강의계획서의 `Z. Jin` 표기는 약식 표기로 추정 |
| 핵심 근거 사용 가능 여부 | 가능 |
| 검증 메모 | W02 `paper_list.md` 기준 DOI, 저자명, 학술지 확인 완료. 권호 표기는 최종 제출 양식에 맞춰 재확인 필요 |

---

## 1. 한 문장 요약

이 논문은 DNN부터 LLM까지 backdoor 공격과 방어를 **trigger, target behavior, clean accuracy, attack success rate, stealthiness, detection, removal, mitigation, LLM fine-tuning risk** 관점에서 정리하고, 정상 성능이 유지되더라도 특정 조건에서 공격자 목표 행동이 발생할 수 있음을 보여주는 핵심 survey 논문이다.

---

## 2. 연구문제

이 논문의 핵심 연구문제는 다음과 같이 정리할 수 있다.

> Backdoor 공격은 어떤 방식으로 모델 내부에 조건부 악성 행동을 삽입하며, 방어자는 정상 성능과 공격 조건 성능을 어떤 지표로 분리해 탐지·제거·완화해야 하는가?

### 세부 연구질문

| 번호 | 연구질문 |
|---|---|
| RQ1 | Backdoor 공격은 trigger, target label, poisoning data, training process 관점에서 어떻게 정의되는가? |
| RQ2 | Clean-label backdoor, dirty-label backdoor, physical trigger, semantic trigger는 어떤 차이가 있는가? |
| RQ3 | DNN backdoor와 LLM backdoor는 공격면과 방어 지표에서 어떻게 다른가? |
| RQ4 | Backdoor 방어는 탐지, 제거, 완화, 검증 단계로 어떻게 분류할 수 있는가? |
| RQ5 | Clean accuracy, ASR, stealthiness, trigger coverage, detection rate를 함께 보고해야 하는 이유는 무엇인가? |

---

## 3. 핵심 이론 및 수식

> 작성 원칙: GitHub, MS Word, PDF 변환 호환성을 위해 수식은 표 안에 넣지 않고 별도 블록 수식으로 작성한다. 변수 설명은 Markdown 표로 분리한다.

### 3.1 Backdoor Trigger 함수

Backdoor 공격은 정상 입력 $x$에 trigger 변환 $T(\cdot)$를 적용했을 때 모델이 공격자 목표 출력 $y^{target}$을 내도록 만드는 조건부 공격이다.

$$
x^{trigger} = T(x; \tau)
$$

| 기호 | 의미 |
|---|---|
| $x$ | 정상 입력 |
| $x^{trigger}$ | trigger가 삽입된 입력 |
| $T(\cdot)$ | trigger 삽입 함수 |
| $\tau$ | trigger 패턴 또는 조건 |

### 보안적 의미

Backdoor는 정상 입력에서는 모델이 정상적으로 동작하게 하면서, trigger 조건에서만 공격자 목표 행동을 유도한다. 따라서 단순 clean accuracy 검증만으로는 탐지하기 어렵다.

---

### 3.2 Backdoor 학습 목적

Backdoor 학습은 정상 데이터 성능과 trigger 데이터 목표 출력을 동시에 만족시키는 형태로 볼 수 있다.

$$
\min_{\theta}
\left[
\sum_{(x,y) \in D_{clean}} \ell(f_{\theta}(x), y)
+ \lambda \sum_{x \in D_{trigger}} \ell(f_{\theta}(T(x;\tau)), y^{target})
\right]
$$

| 기호 | 의미 |
|---|---|
| $D_{clean}$ | 정상 학습 데이터 |
| $D_{trigger}$ | trigger를 삽입할 데이터 집합 |
| $y^{target}$ | 공격자가 유도하려는 목표 출력 |
| $\lambda$ | 정상 학습 손실과 backdoor 손실의 상대 가중치 |

### 보안적 의미

이 목적함수는 backdoor 공격의 핵심을 보여준다. 공격자는 정상 데이터에서의 utility를 크게 해치지 않으면서 trigger 조건에서 목표 행동을 학습시키려 한다.

---

### 3.3 Attack Success Rate

Backdoor 공격의 핵심 지표는 trigger 입력에서 목표 행동이 발생한 비율이다.

$$
ASR = \frac{1}{N_{trigger}}
\sum_{j=1}^{N_{trigger}}
\mathbf{1}[f_{\theta}(x_j^{trigger}) = y^{target}]
$$

| 기호 | 의미 |
|---|---|
| $ASR$ | Attack Success Rate |
| $N_{trigger}$ | trigger 평가 입력 수 |
| $x_j^{trigger}$ | trigger가 포함된 $j$번째 입력 |
| $y^{target}$ | 공격 목표 출력 |
| $\mathbf{1}[\cdot]$ | 조건이 참이면 1, 거짓이면 0인 지시 함수 |

### 보안적 의미

ASR이 높고 clean accuracy도 높으면 공격은 은닉성이 높다. 따라서 backdoor 평가는 반드시 clean accuracy와 ASR을 분리해야 한다.

---

### 3.4 Backdoor Stealthiness

Backdoor의 은닉성은 정상 성능 유지와 탐지 회피 정도로 표현할 수 있다.

$$
UtilityDrop = CleanAcc_{baseline} - CleanAcc_{backdoored}
$$

$$
StealthRisk = ASR - UtilityDrop
$$

| 기호 | 의미 |
|---|---|
| $UtilityDrop$ | backdoor 모델의 정상 성능 저하량 |
| $CleanAcc_{baseline}$ | 정상 모델의 clean accuracy |
| $CleanAcc_{backdoored}$ | backdoor 모델의 clean accuracy |
| $StealthRisk$ | 공격 성공률과 낮은 성능 저하가 결합된 은닉 위험 점수 |

### 보안적 의미

$UtilityDrop$이 작고 $ASR$이 높으면 검증자는 모델을 정상으로 판단할 수 있다. 따라서 backdoor 방어는 정상 성능뿐 아니라 trigger coverage와 hidden behavior test를 포함해야 한다.

---

## 4. AI 원리 관점 분석

| 항목 | 분석 |
|---|---|
| 조건부 학습 | 모델은 trigger와 target label 사이의 조건부 관계를 학습한다. |
| Representation | trigger가 내부 activation 또는 feature representation을 특정 방향으로 이동시킬 수 있다. |
| Clean Accuracy | 정상 입력 성능은 높게 유지될 수 있으므로 단독 지표로 부족하다. |
| ASR | trigger 입력에서 공격자 목표가 달성되는지 평가한다. |
| Fine-tuning | LLM 환경에서는 instruction tuning, LoRA, PEFT 데이터가 backdoor 삽입 경로가 될 수 있다. |
| Detection | activation clustering, spectral signature, trigger reverse engineering 등이 사용될 수 있다. |
| Removal | pruning, fine-pruning, retraining, unlearning, model editing 등이 검토될 수 있다. |

---

## 5. 보안 이슈 관점 분석

P05는 W02에서 clean accuracy와 ASR의 차이를 가장 명확하게 설명하는 문헌이다. Backdoor는 모델의 정상 성능을 유지하면서 조건부 악성 행동을 숨기는 무결성 공격이다.

| 보안 항목 | Backdoor 관점 해석 |
|---|---|
| 기밀성 | LLM backdoor가 특정 prompt 조건에서 숨겨진 정보 노출을 유도할 수 있다. |
| 무결성 | Trigger 조건에서 모델 출력이 공격자 목표로 왜곡된다. |
| 가용성 | 특정 조건에서 서비스 오작동이나 거부가 발생할 수 있다. |
| 안전성 | 자율주행, 의료, 보안관제, LLM agent에서 조건부 실패가 실제 피해로 이어질 수 있다. |
| 책임성 | Trigger 조건, 학습 데이터, fine-tuning 이력, checkpoint 출처를 감사할 수 있어야 한다. |
| 운영 리스크 | 공개 모델, 외부 fine-tuning 데이터, adapter, plugin, RAG 문서가 backdoor 경로가 될 수 있다. |

---

## 6. 위협모형

### 6.1 보호 대상

| 보호 대상 | 설명 |
|---|---|
| 학습 데이터 | trigger가 삽입된 샘플, target label, fine-tuning data |
| 모델 파라미터 | backdoor 행동이 저장된 가중치 또는 adapter |
| 입력 인터페이스 | 이미지, 텍스트, prompt, instruction, tool call input |
| 출력 행동 | 분류 결과, 생성 텍스트, tool action, policy response |
| 검증 절차 | trigger test, hidden behavior test, activation analysis |
| 모델 공급망 | pretrained model, checkpoint, LoRA adapter, dataset package |

### 6.2 공격자 능력

| 공격자 유형 | 가능 행위 |
|---|---|
| Data poisoning attacker | trigger가 포함된 학습 데이터를 삽입한다. |
| Model supplier attacker | 이미 backdoor가 삽입된 pretrained model 또는 checkpoint를 제공한다. |
| Fine-tuning attacker | instruction data, LoRA adapter, PEFT 데이터에 backdoor를 삽입한다. |
| Prompt-trigger attacker | 특정 문구, 형식, semantic condition으로 LLM backdoor를 활성화한다. |
| Insider attacker | 검증 단계에서 trigger test를 누락하거나 로그를 삭제한다. |

### 6.3 공격 경로

```text
정상 또는 외부 데이터 수집
→ trigger와 target behavior 삽입
→ 모델 학습 또는 fine-tuning
→ clean validation 통과
→ 배포 후 trigger 조건 입력 발생
→ 목표 오분류 또는 악성 응답 발생
→ ASR 증가와 보안 실패 발생
```

---

## 7. 평가방법 및 지표

| 지표 | 의미 | W02/P05에서의 활용 |
|---|---|---|
| Clean Accuracy | 정상 입력에서의 정확도 | utility 유지 여부 평가 |
| ASR | trigger 입력에서 목표 행동 발생 비율 | backdoor 공격 핵심 지표 |
| Utility Drop | backdoor 적용 후 정상 성능 저하 | 은닉성 평가 |
| Trigger Coverage | 다양한 trigger 조건을 평가했는지 | 검증 충분성 평가 |
| Detection Rate | 방어가 backdoor를 탐지한 비율 | 탐지 성능 평가 |
| FPR | 정상 모델 또는 정상 샘플을 backdoor로 오탐한 비율 | 방어 부작용 평가 |
| Removal Effectiveness | 제거 후 ASR 감소량 | 방어 효과 평가 |
| Robustness after Removal | 제거 후 clean/robust 성능 유지 | 방어 후 utility 평가 |
| Auditability | 데이터·모델·adapter 출처 기록 여부 | 공급망 감사 가능성 평가 |

---

## 8. 재현성 점검

이 논문은 survey 문헌이므로 안전한 toy backdoor 평가 프로토콜로 핵심 지표를 재현하는 방식이 적절하다. 실제 시스템에 backdoor를 삽입하거나 무단 모델을 대상으로 실험하는 것은 범위에서 제외한다.

| 항목 | 점검 |
|---|---|
| 데이터셋 | MNIST, UCI digits, CIFAR-10 등 공개 toy dataset 사용 가능 |
| Trigger 설정 | 위치, 크기, 패턴, semantic condition, target label 기록 필요 |
| 오염률 | trigger 데이터 비율과 poison index 기록 필요 |
| 모델 | baseline model과 backdoored model을 분리 저장 |
| 평가 | clean accuracy, ASR, detection rate, FPR, utility drop 기록 |
| 방어 | pruning, retraining, input preprocessing, trigger scanning 조건 기록 |
| Seed/Config | seed, split, optimizer, epoch, trigger config 저장 필요 |
| 재현 가능성 판단 | toy/public data 기준 가능. LLM backdoor 일반화는 비용·윤리·모델 접근성 때문에 제한적 |

### W02 실습 연결

W02에서는 다음 최소 실험으로 P05의 핵심 평가 관점을 반영할 수 있다.

1. 공개 toy 데이터셋을 로딩한다.
2. trigger 위치와 target label을 기록한다.
3. clean model과 backdoor condition model을 구분한다.
4. 정상 테스트셋에서 clean accuracy를 계산한다.
5. trigger 테스트셋에서 ASR을 계산한다.
6. 방어 또는 탐지 절차가 있다면 detection rate와 FPR을 계산한다.
7. 결과를 실제 공격 절차가 아니라 안전한 보안 평가 예시로 제한해 해석한다.

---

## 9. 논문의 고유 기여

1. Backdoor 공격과 방어를 DNN부터 LLM까지 확장해 정리했다.
2. Clean accuracy와 ASR을 분리해야 backdoor 은닉성을 평가할 수 있음을 보여준다.
3. Trigger, target behavior, poisoning data, detection, removal, mitigation을 하나의 평가 프레임으로 연결한다.
4. LLM 환경에서 fine-tuning data, instruction data, adapter, prompt trigger가 새로운 공격면이 될 수 있음을 보여준다.
5. W02 기말논문에서 backdoor 평가표와 clean accuracy-ASR 분리의 핵심 근거로 사용할 수 있다.

---

## 10. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 최신성 변동 | LLM backdoor 연구는 빠르게 변하므로 2025년 이후 문헌 보강이 필요할 수 있다. | 최종 제출 전 최신 LLM backdoor 문헌 1~2편을 추가 확인한다. |
| 재현 비용 | LLM backdoor 실험은 모델·GPU·데이터 비용이 크다. | toy DNN 또는 공개 데이터 기반 최소 실험으로 제한한다. |
| 윤리적 위험 | backdoor 삽입 절차는 악용 가능성이 있다. | 공격 구현보다 평가 지표와 방어 체크리스트 중심으로 작성한다. |
| Trigger 일반화 | 특정 trigger 결과가 다른 모델·도메인에 일반화되지 않는다. | trigger coverage와 한계를 명시한다. |
| 방어 한계 | 하나의 방어가 모든 backdoor를 제거하지 못한다. | detection, removal, utility 유지 지표를 함께 보고한다. |

---

## 11. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | 정상 성능이 높아도 trigger 조건에서 악성 행동이 발생할 수 있다는 문제의식 제시 |
| 2장 관련연구 | Backdoor attack/defense taxonomy, DNN-to-LLM 확장 정리 |
| 3장 위협모형 | trigger, target behavior, model supplier, fine-tuning attacker 정의 |
| 4장 연구방법 | clean accuracy, ASR, utility drop, detection rate, FPR 기반 평가 설계 |
| 5장 실험/분석 | toy trigger 실험 또는 문헌 기반 backdoor 방어 비교표 제시 |
| 6장 보안적 함의 | 무결성, 안전성, 공급망 보안, 감사가능성 해석 |
| 7장 결론 | AI 보안은 정상 성능뿐 아니라 hidden behavior 검증을 포함해야 함을 제시 |

---

## 12. 기말논문 연결 3문장

1. 이 주차에서 기말논문에 반영할 개념: Backdoor 공격은 정상 입력에서는 clean accuracy를 유지하면서 trigger 조건에서 공격자 목표 행동을 유도하는 조건부 무결성 공격이다.
2. 이 주차에서 기말논문에 반영할 표·그림·실험: trigger 삽입 개념도, clean accuracy-ASR 비교표, utility drop/stealth risk 수식, detection-removal 평가표를 반영한다.
3. 이 주차가 RAG 문서 오염/LLM 보안 감사 프레임워크와 연결되는 지점: LLM fine-tuning 데이터, adapter, prompt trigger, RAG 문서 조건이 backdoor trigger처럼 작동할 수 있으므로 P05의 hidden behavior 평가를 W08/W14의 LLM 운영 감사로 확장한다.

---

## 13. 최종 판단

이 논문은 W02에서 backdoor 공격과 방어를 설명하는 핵심 문헌으로 사용한다. P03과 P04가 training data poisoning의 일반 taxonomy를 제공한다면, P05는 조건부 악성 행동과 ASR 평가를 명확히 한다. 기말논문에서는 P05를 통해 clean accuracy와 ASR을 분리하고, LLM/RAG 환경의 hidden behavior 감사로 확장하는 것이 적절하다.

---

## 14. 변환 호환성 메모

- GitHub Markdown, MS Word, PDF 변환 호환성을 위해 수식은 LaTeX 블록 수식으로 작성했다.
- 긴 수식은 Markdown 표 안에 넣지 않고 별도 문단으로 분리했다.
- 표에는 변수 설명과 해석만 배치했다.
- DOCX/PDF 변환 시에는 Pandoc 기준으로 다음 명령을 권장한다.

```bash
pandoc P05_summary.md -o P05_summary.docx
pandoc P05_summary.md -o P05_summary.pdf --pdf-engine=xelatex
```
