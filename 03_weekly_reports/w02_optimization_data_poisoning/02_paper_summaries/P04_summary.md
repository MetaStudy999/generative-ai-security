# P04 Summary

## Wild Patterns Reloaded: A Survey of Machine Learning Security against Training Data Poisoning — Antonio Emanuele Cina et al., ACM Computing Surveys, 2023

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W02 대규모 최적화 & 데이터 오염 위협 |
| 현재 로컬 논문명 | Wild Patterns Reloaded: A Survey of Machine Learning Security against Training Data Poisoning |
| 강의계획서 지정 제목 | Training Data Poisoning Attacks and Defenses: A Systematic Review |
| 저자 | Antonio Emanuele Cina, Kathrin Grosse, Ambra Demontis, Sebastiano Vascon, Werner Zellinger, Bernhard A. Moser, Alina Oprea, Battista Biggio, Marcello Pelillo, Fabio Roli |
| 학술지 | ACM Computing Surveys |
| 권호/쪽 | Vol. 55, No. 13s, pp. 1–39 |
| 연도 | 2023 |
| DOI | https://doi.org/10.1145/3585385 |
| 공개 원고 | https://arxiv.org/abs/2205.01992 |
| 논문 유형 | Survey / Training Data Poisoning Review |
| 로컬 PDF | `01_papers/pdf/04_Cina_et_al_2023_Wild_Patterns_Reloaded_Poisoning_Survey.pdf` |
| 강의계획서 지정 논문과 일치 여부 | 제목 차이로 확인 필요. 현재 repo에서는 관련 논문 또는 판본 확인 필요 문헌으로 관리 |
| 핵심 근거 사용 가능 여부 | 제한적 가능. 최종 제출 전 지정 제목과 동일 논문인지 재확인 필요 |
| 검증 메모 | W02 `paper_list.md` 기준 DOI 확인 완료. 단, 강의계획서 지정 제목과 현재 로컬 PDF 제목의 차이를 최종 제출 전 사람이 확인해야 한다. |

---

## 1. 한 문장 요약

이 논문은 훈련 데이터 poisoning 공격과 방어를 **공격 목표, 공격자 지식, 오염 데이터 생성 방식, 데이터 provenance, 방어 관측 가능성, 평가 지표, 데이터 생명주기 보안** 관점에서 체계화하고, 학습 데이터 무결성이 ML 보안의 핵심 전제임을 보여주는 survey 논문이다.

---

## 2. 연구문제

이 논문의 핵심 연구문제는 다음과 같이 정리할 수 있다.

> 훈련 데이터가 공격자에 의해 부분적으로 조작될 수 있는 환경에서, poisoning 공격은 어떤 조건과 목표로 모델을 왜곡하며, 방어자는 데이터·학습·검증 단계에서 어떤 증거와 지표로 공격을 탐지하고 완화해야 하는가?

### 세부 연구질문

| 번호 | 연구질문 |
|---|---|
| RQ1 | Training data poisoning은 공격 목표와 공격자 능력에 따라 어떻게 분류되는가? |
| RQ2 | Untargeted poisoning, targeted poisoning, clean-label poisoning, backdoor poisoning은 어떤 평가 지표가 필요한가? |
| RQ3 | 데이터 수집·라벨링·전처리·학습 단계 중 어느 위치에서 방어 증거를 수집해야 하는가? |
| RQ4 | 방어 방법은 데이터 정제, robust learning, model inspection, monitoring으로 어떻게 분류되는가? |
| RQ5 | Clean accuracy, ASR, stealthiness, detection rate, false positive rate를 함께 보고해야 하는 이유는 무엇인가? |

---

## 3. 핵심 이론 및 수식

> 작성 원칙: GitHub, MS Word, PDF 변환 호환성을 위해 수식은 표 안에 넣지 않고 별도 블록 수식으로 작성한다. 변수 설명은 Markdown 표로 분리한다.

### 3.1 Poison Rate

Training data poisoning의 기본 강도는 전체 학습 데이터 중 오염 샘플 비율로 표현할 수 있다.

$$
PoisonRate = \frac{|D_{poison}|}{|D_{clean} \cup D_{poison}|}
$$

| 기호 | 의미 |
|---|---|
| $D_{poison}$ | 오염 데이터셋 |
| $D_{clean}$ | 정상 데이터셋 |
| $PoisonRate$ | 학습 데이터 내 오염 비율 |

### 보안적 의미

Poison rate가 낮으면서 ASR이 높고 clean accuracy가 유지된다면 공격은 은닉성이 높다. 따라서 단순 성능 저하만 보는 방식으로는 backdoor나 targeted poisoning을 놓칠 수 있다.

---

### 3.2 Targeted Poisoning Objective

Targeted poisoning은 전체 성능 저하보다 특정 입력 또는 특정 클래스의 목표 오분류를 유도한다.

$$
\max_{D_{poison} \in \mathcal{C}} \; \Pr[f_{\theta^*}(x^{target}) = y^{adv}]
$$

$$
\theta^* = \arg\min_{\theta}
\sum_{(x,y) \in D_{clean} \cup D_{poison}}
\ell(f_{\theta}(x), y)
$$

| 기호 | 의미 |
|---|---|
| $x^{target}$ | 공격자가 오분류시키려는 목표 입력 또는 조건 |
| $y^{adv}$ | 공격자가 유도하려는 목표 레이블 |
| $D_{poison}$ | 공격자가 삽입하는 오염 데이터 |
| $\mathcal{C}$ | 공격 제약. 예: 오염률, 라벨 변경 가능 여부, 노이즈 범위 |
| $\theta^*$ | 오염 데이터로 학습된 모델 파라미터 |

### 보안적 의미

이 구조는 훈련 데이터 poisoning이 bilevel 문제임을 보여준다. 방어자는 학습 후 모델만 보는 것이 아니라 데이터 provenance와 학습 과정 증거를 함께 확인해야 한다.

---

### 3.3 Stealthiness와 Utility 유지

Poisoning 공격의 은닉성은 정상 성능 유지 정도와 오염 데이터 탐지 난이도로 볼 수 있다.

$$
StealthScore = CleanAcc_{poisoned} - CleanAcc_{baseline}
$$

$$
DefenseFPR = \frac{FP_{clean}}{FP_{clean}+TN_{clean}}
$$

| 기호 | 의미 |
|---|---|
| $StealthScore$ | 오염 모델과 정상 모델의 clean accuracy 차이 |
| $CleanAcc_{poisoned}$ | 오염 모델의 정상 테스트 정확도 |
| $CleanAcc_{baseline}$ | 정상 모델의 정상 테스트 정확도 |
| $DefenseFPR$ | 정상 샘플을 오염으로 잘못 탐지한 비율 |
| $FP_{clean}$ | 정상 샘플을 오염으로 잘못 탐지한 수 |
| $TN_{clean}$ | 정상 샘플을 정상으로 올바르게 판단한 수 |

### 보안적 의미

방어가 오염 데이터를 잘 탐지하더라도 정상 데이터를 과도하게 제거하면 학습 성능과 운영성이 저하된다. 따라서 detection rate와 FPR을 함께 봐야 한다.

---

### 3.4 Clean Accuracy와 ASR

Backdoor 또는 targeted poisoning 평가에서는 정상 성능과 공격 성공률을 분리한다.

$$
CleanAcc = \frac{1}{n}\sum_{i=1}^{n} \mathbf{1}[f_{\theta}(x_i)=y_i]
$$

$$
ASR = \frac{1}{m}\sum_{j=1}^{m} \mathbf{1}[f_{\theta}(x_j^{trigger})=y^{target}]
$$

### 보안적 의미

정상 정확도만 높고 ASR을 측정하지 않으면 “숨은 실패 조건”을 놓친다. 따라서 W02 보고서에서는 clean accuracy, ASR, stealthiness, detection rate, FPR을 동시에 기록해야 한다.

---

## 4. AI 원리 관점 분석

| 항목 | 분석 |
|---|---|
| 데이터 중심 학습 | 모델은 학습 데이터 분포와 라벨을 기준으로 결정경계를 학습하므로 데이터 무결성이 핵심이다. |
| Bilevel Optimization | 공격자는 오염 데이터를 고르고, 학습자는 그 데이터로 모델을 학습하는 이중 구조가 된다. |
| Clean-label Poisoning | 라벨을 바꾸지 않아도 feature와 representation을 조작해 목표 오분류를 유도할 수 있다. |
| Backdoor Learning | trigger와 target label의 조건부 상관을 모델 내부에 학습시킨다. |
| Detection Difficulty | 오염 데이터가 정상 분포에 가까울수록 탐지가 어려워진다. |
| Defense Placement | 방어는 데이터 수집, 전처리, 학습, 검증, 배포 후 모니터링 단계에 배치될 수 있다. |

---

## 5. 보안 이슈 관점 분석

P04는 W02에서 데이터 생명주기 기반 poisoning 방어를 정리하는 문헌이다. 공격 실행 절차보다 중요한 것은 **위협모형, 관측 가능성, 방어 위치, 평가 지표**를 명확히 하는 것이다.

| 보안 항목 | Training Data Poisoning 관점 해석 |
|---|---|
| 데이터 무결성 | 학습 데이터와 라벨의 출처, 변경 이력, 검증 절차가 핵심 보안 자산이다. |
| 모델 무결성 | 오염된 데이터는 모델 결정경계와 내부 표현을 바꾼다. |
| 은닉성 | 정상 성능이 유지되면 공격이 배포 전 검증을 통과할 수 있다. |
| 방어 관측성 | 방어자가 데이터, gradient, activation, output 중 무엇을 볼 수 있는지 명시해야 한다. |
| 책임성 | 데이터 provenance, 라벨링 이력, 학습 로그가 없으면 사후 감사가 어렵다. |
| 운영 리스크 | 공개 데이터셋, 크롤링 데이터, 외주 라벨링, federated client가 공격면이 된다. |

---

## 6. 위협모형

### 6.1 보호 대상

| 보호 대상 | 설명 |
|---|---|
| 원천 데이터 | 수집된 원본 데이터와 메타데이터 |
| 라벨 | 사람 또는 자동화 시스템이 부여한 정답 정보 |
| 전처리 결과 | feature, embedding, augmentation 결과 |
| 학습 파이프라인 | dataset loader, sampler, optimizer, loss function |
| 검증 절차 | validation set, trigger test, outlier detector |
| provenance evidence | 데이터 출처, 변경 이력, 승인 로그 |

### 6.2 공격자 능력

| 공격자 유형 | 가능 행위 |
|---|---|
| Untargeted attacker | 전체 모델 성능 저하를 목표로 데이터 일부를 오염시킨다. |
| Targeted attacker | 특정 입력 또는 클래스의 목표 오분류를 유도한다. |
| Clean-label attacker | 라벨 변경 없이 feature만 조작한다. |
| Backdoor attacker | trigger 조건에서만 목표 행동이 발생하도록 학습 데이터를 구성한다. |
| Data pipeline attacker | 데이터 수집·라벨링·증강·저장 과정 중 하나를 조작한다. |

### 6.3 공격 경로

```text
데이터 수집
→ 라벨링/전처리/증강
→ 공격자가 일부 데이터 또는 라벨을 오염
→ 학습 파이프라인에 오염 데이터 포함
→ 모델이 정상 성능은 유지하되 특정 조건에서 실패
→ 배포 후 trigger 또는 target 조건에서 보안 사고 발생
```

---

## 7. 평가방법 및 지표

| 지표 | 의미 | W02/P04에서의 활용 |
|---|---|---|
| Poison Rate | 학습 데이터 내 오염 비율 | 공격 강도 정의 |
| Clean Accuracy | 정상 입력 정확도 | 공격 은닉성 확인 |
| Accuracy Drop | baseline 대비 성능 저하 | availability poisoning 평가 |
| ASR | trigger/target 조건 공격 성공률 | backdoor/targeted poisoning 평가 |
| Targeted Success Rate | 특정 목표 오분류 성공률 | targeted attack 평가 |
| Detection Rate | 방어가 오염 샘플을 탐지한 비율 | 데이터 정제 성능 평가 |
| FPR | 정상 샘플을 오염으로 오탐한 비율 | 방어의 부작용 평가 |
| Stealthiness | 정상 성능 유지와 탐지 회피 정도 | 은닉 공격 평가 |
| Provenance Coverage | 데이터 출처와 변경 이력의 기록 정도 | 감사 가능성 평가 |

---

## 8. 재현성 점검

이 논문은 survey 문헌이므로 안전한 toy protocol로 taxonomy와 평가 지표를 재현하는 방식이 적절하다. 실제 시스템 공격이나 무단 데이터 오염은 범위에서 제외한다.

| 항목 | 점검 |
|---|---|
| 데이터셋 | 공개 toy dataset 또는 UCI/MNIST/CIFAR 계열 데이터 사용 |
| 오염 설정 | poison rate, target label, trigger pattern, clean-label 여부 기록 |
| 방어 설정 | data filtering, anomaly detection, retraining, trigger scanning 조건 기록 |
| 관측 가능성 | 방어자가 데이터, 라벨, gradient, activation, output 중 무엇을 보는지 명시 |
| Seed/Config | seed, split, batch order, optimizer, hyperparameter 기록 |
| 결과 파일 | clean accuracy, ASR, detection rate, FPR, provenance checklist 저장 |
| 재현 가능성 판단 | toy/public data 기준 재현 가능. 실제 데이터 공급망과 LLM/RAG 일반화는 제한적 |

### W02 실습 연결

W02에서는 다음 최소 실험으로 P04의 평가 관점을 반영할 수 있다.

1. clean dataset과 poisoned dataset을 분리해 저장한다.
2. poison rate와 poison index를 명시한다.
3. clean-label 여부, target class, trigger pattern을 기록한다.
4. clean model과 poisoned model을 동일 config로 학습한다.
5. clean accuracy, ASR, detection rate, FPR을 계산한다.
6. 데이터 provenance checklist를 작성한다.
7. 결과를 실제 공격 효과가 아니라 안전한 평가 프로토콜 예시로 해석한다.

---

## 9. 논문의 고유 기여

1. Training data poisoning을 공격자 목표, 지식, 능력, 데이터 조작 방식 기준으로 체계화했다.
2. 공격과 방어를 데이터 생명주기 관점으로 정리해 provenance와 감사 가능성의 중요성을 보여준다.
3. Clean-label poisoning과 backdoor처럼 탐지가 어려운 공격을 구분해 평가할 수 있는 프레임을 제공한다.
4. 방어를 데이터 정제, robust learning, 검증, 모니터링 위치로 분해할 수 있게 한다.
5. W02 기말논문에서 clean accuracy, ASR, stealthiness, detection rate를 동시에 보는 다중지표 평가 근거를 제공한다.

---

## 10. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 판본 확인 필요 | 강의계획서 지정 제목과 현재 로컬 PDF 제목이 다르다. | 최종 제출 전 지정 논문과 동일 여부를 재확인하고, 필요 시 관련 논문으로 명시한다. |
| Survey 기반 한계 | 특정 모델·데이터셋에서 방어 안정성을 직접 입증하지 않는다. | toy/public data 기반 최소 실험을 별도 수행한다. |
| 도메인 일반화 한계 | Vision 중심 연구가 tabular, log, LLM, RAG 데이터로 그대로 일반화되지 않는다. | W08 RAG 문서 오염, W14 MLOps 데이터 검증으로 확장한다. |
| Adaptive attacker 한계 | 방어가 알려지면 공격자가 우회할 수 있다. | adaptive threat model을 한계로 명시한다. |
| 방어 비용 문제 | 데이터 정제와 trigger scanning은 비용이 클 수 있다. | P02의 효율성 지표와 결합한다. |

---

## 11. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | 데이터 생명주기 보안과 학습 데이터 무결성의 중요성 제시 |
| 2장 관련연구 | Training data poisoning taxonomy와 defense taxonomy 정리 |
| 3장 위협모형 | 공격자 목표, 지식, 능력, 오염 위치, 관측 가능성 정의 |
| 4장 연구방법 | poison rate, ASR, stealthiness, detection rate, FPR 기반 평가 설계 |
| 5장 실험/분석 | clean vs poisoned model, 방어 전후 지표 비교표 제시 |
| 6장 보안적 함의 | 데이터 무결성, 책임성, provenance, 감사 가능성 해석 |
| 7장 결론 | AI 보안은 모델 방어뿐 아니라 데이터 공급망 보증을 포함해야 함을 제시 |

---

## 12. 기말논문 연결 3문장

1. 이 주차에서 기말논문에 반영할 개념: Training data poisoning은 데이터 출처, 라벨, 전처리, 학습 파이프라인의 무결성을 훼손해 모델의 정상 성능과 공격 조건 성능을 분리시키는 학습 단계 공격이다.
2. 이 주차에서 기말논문에 반영할 표·그림·실험: 데이터 생명주기 위협모형, poison rate 수식, clean accuracy-ASR-stealthiness-detection rate 평가표, provenance checklist를 반영한다.
3. 이 주차가 RAG 문서 오염/LLM 보안 감사 프레임워크와 연결되는 지점: RAG 검색 문서와 LLM fine-tuning corpus도 training data pipeline의 일부로 볼 수 있으므로, P04의 데이터 provenance와 poisoning defense taxonomy를 W08/W14에 연결한다.

---

## 13. 최종 판단

이 논문은 W02에서 training data poisoning과 방어 taxonomy를 정리하는 핵심 관련 문헌으로 사용한다. 다만 강의계획서 지정 제목과 로컬 PDF 제목 차이가 있으므로 최종 제출 전 문헌 검증표에서 “지정 논문”인지 “관련 대체 논문”인지 명확히 표시해야 한다. 기말논문에서는 데이터 생명주기 보안, provenance evidence, clean accuracy-ASR 분리 평가의 근거로 활용하는 것이 적절하다.

---

## 14. 변환 호환성 메모

- GitHub Markdown, MS Word, PDF 변환 호환성을 위해 수식은 LaTeX 블록 수식으로 작성했다.
- 긴 수식은 Markdown 표 안에 넣지 않고 별도 문단으로 분리했다.
- 표에는 변수 설명과 해석만 배치했다.
- DOCX/PDF 변환 시에는 Pandoc 기준으로 다음 명령을 권장한다.

```bash
pandoc P04_summary.md -o P04_summary.docx
pandoc P04_summary.md -o P04_summary.pdf --pdf-engine=xelatex
```
