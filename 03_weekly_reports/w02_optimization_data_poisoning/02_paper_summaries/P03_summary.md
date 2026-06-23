# P03 Summary

## A Comprehensive Survey on Poisoning Attacks and Countermeasures in Machine Learning — Zhiyi Tian, Lei Cui, Jie Liang, Shui Yu, ACM Computing Surveys, 2023

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W02 대규모 최적화 & 데이터 오염 위협 |
| 논문명 | A Comprehensive Survey on Poisoning Attacks and Countermeasures in Machine Learning |
| 저자 | Zhiyi Tian, Lei Cui, Jie Liang, Shui Yu |
| 학술지 | ACM Computing Surveys |
| 권호/쪽 | Vol. 55, No. 8, pp. 1–35 |
| 연도 | 2022/2023 |
| DOI | https://doi.org/10.1145/3551636 |
| 논문 유형 | Survey / Poisoning Attacks and Countermeasures Review |
| 로컬 PDF | `01_papers/pdf/03_Tian_Cui_Liang_Yu_2023_Comprehensive_Poisoning_Survey.pdf` |
| 강의계획서 지정 논문과 일치 여부 | 일치. 강의계획서의 `Zhipeng Tian` 표기는 출판 정보 기준 `Zhiyi Tian`으로 정리 |
| 핵심 근거 사용 가능 여부 | 가능 |
| 검증 메모 | W02 `paper_list.md` 기준 DOI와 저자명 확인 완료. 온라인 출판연도와 권호 표기는 제출 양식에 맞춰 최종 재확인 필요 |

---

## 1. 한 문장 요약

이 논문은 머신러닝 poisoning 공격을 **공격 목표, 공격자 지식, 오염 위치, 오염 방식, 대상 모델, 방어 전략**에 따라 체계적으로 분류하고, 학습 데이터 조작이 모델의 정확도·무결성·가용성·은닉성·재현성에 미치는 영향을 평가하기 위한 핵심 taxonomy를 제공하는 survey 논문이다.

---

## 2. 연구문제

이 논문의 핵심 연구문제는 다음과 같이 정리할 수 있다.

> 학습 단계에서 데이터 또는 라벨이 조작될 때, 공격자는 어떤 목표와 능력으로 모델 학습을 왜곡하며, 방어자는 어떤 지표와 절차로 poisoning 공격을 탐지·완화·평가해야 하는가?

### 세부 연구질문

| 번호 | 연구질문 |
|---|---|
| RQ1 | Poisoning attack은 공격 목표에 따라 availability attack과 integrity attack으로 어떻게 구분되는가? |
| RQ2 | 공격자의 지식 수준과 데이터 조작 권한은 공격 성공 가능성에 어떤 영향을 주는가? |
| RQ3 | Label-flipping, clean-label poisoning, feature poisoning, backdoor poisoning은 어떤 차이가 있는가? |
| RQ4 | Poisoning 방어는 데이터 정제, robust learning, anomaly detection, monitoring 관점에서 어떻게 분류되는가? |
| RQ5 | Clean accuracy, ASR, poison rate, stealthiness, detection rate를 함께 평가해야 하는 이유는 무엇인가? |

---

## 3. 핵심 이론 및 수식

> 작성 원칙: GitHub, MS Word, PDF 변환 호환성을 위해 수식은 표 안에 넣지 않고 별도 블록 수식으로 작성한다. 변수 설명은 Markdown 표로 분리한다.

### 3.1 Poisoned ERM 목적함수

Poisoning 공격은 학습 데이터셋에 오염 샘플을 섞어 모델이 오염된 경험위험을 최소화하도록 만든다.

$$
\min_{\theta}
\frac{1}{|D_{clean} \cup D_{poison}|}
\sum_{(x,y) \in D_{clean} \cup D_{poison}}
\ell(f_{\theta}(x), y)
$$

| 기호 | 의미 |
|---|---|
| $D_{clean}$ | 정상 학습 데이터셋 |
| $D_{poison}$ | 공격자가 삽입하거나 조작한 오염 데이터셋 |
| $f_{\theta}$ | 학습 대상 모델 |
| $\ell(\cdot)$ | 손실함수 |
| $\theta$ | 모델 파라미터 |

### 보안적 의미

Poisoning은 모델 입력을 추론 시점에만 바꾸는 것이 아니라 학습 목적함수 자체를 바꾼다. 따라서 최종 모델은 정상 검증 데이터에서 어느 정도 성능을 유지하더라도 특정 클래스, 특정 입력, 특정 트리거 조건에서 공격자 목표대로 동작할 수 있다.

---

### 3.2 Poison Rate

오염 강도는 전체 학습 데이터 중 오염 데이터의 비율로 표현할 수 있다.

$$
PoisonRate = \frac{|D_{poison}|}{|D_{clean} \cup D_{poison}|}
$$

| 기호 | 의미 |
|---|---|
| $PoisonRate$ | 학습 데이터 내 오염 샘플 비율 |
| $|D_{poison}|$ | 오염 샘플 수 |
| $|D_{clean} \cup D_{poison}|$ | 전체 학습 샘플 수 |

### 보안적 의미

Poison rate가 작아도 공격이 성공할 수 있다면 은닉성이 높다. 따라서 W02 실험에서는 오염률별 accuracy drop과 ASR을 함께 봐야 한다.

---

### 3.3 Poisoning 공격의 bilevel 구조

많은 poisoning 공격은 공격자가 오염 데이터를 선택하고, 학습자는 그 데이터로 모델을 학습하는 bilevel optimization 구조로 볼 수 있다.

$$
\max_{D_{poison} \in \mathcal{C}} \; \mathcal{A}(\theta^{*}, D_{test})
$$

$$
\text{subject to} \quad
\theta^{*} = \arg\min_{\theta}
\sum_{(x,y) \in D_{clean} \cup D_{poison}}
\ell(f_{\theta}(x), y)
$$

| 기호 | 의미 |
|---|---|
| $D_{poison}$ | 공격자가 선택한 오염 데이터 |
| $\mathcal{C}$ | 공격자의 제약 조건. 예: 오염률, 라벨 변경 가능 여부, 노이즈 크기 |
| $\mathcal{A}$ | 공격자의 목적함수. 예: 전체 성능 저하 또는 목표 오분류 |
| $\theta^{*}$ | 오염 데이터로 학습된 최종 모델 파라미터 |
| $D_{test}$ | 공격 효과를 평가할 테스트 데이터 |

### 보안적 의미

이 구조는 공격자와 학습자가 서로 다른 목적을 가진다는 점을 보여준다. 학습자는 손실을 줄이지만, 공격자는 학습 결과가 특정 보안 실패로 이어지도록 데이터를 조작한다.

---

### 3.4 Clean Accuracy와 ASR 분리

Poisoning/backdoor 계열 공격에서는 정상 입력 성능과 공격 조건 성능을 분리해야 한다.

$$
CleanAcc = \frac{1}{n}\sum_{i=1}^{n} \mathbf{1}[f_{\theta}(x_i)=y_i]
$$

$$
ASR = \frac{1}{m}\sum_{j=1}^{m} \mathbf{1}[f_{\theta}(x_j^{trigger})=y^{target}]
$$

| 기호 | 의미 |
|---|---|
| $CleanAcc$ | 정상 테스트셋 정확도 |
| $ASR$ | Attack Success Rate, 공격 성공률 |
| $x_j^{trigger}$ | 트리거 또는 공격 조건이 포함된 입력 |
| $y^{target}$ | 공격자가 유도하려는 목표 클래스 |

### 보안적 의미

Clean accuracy가 높아도 ASR이 높으면 보안적으로 실패한 모델이다. 따라서 poisoning 평가는 정상 성능 유지율과 공격 성공률을 동시에 보고해야 한다.

---

## 4. AI 원리 관점 분석

| 항목 | 분석 |
|---|---|
| 경험위험 | 학습 데이터 평균 손실을 최소화하는 구조이므로 데이터 오염에 직접 영향을 받는다. |
| Gradient | 오염 샘플은 gradient 방향을 왜곡해 결정경계를 이동시킬 수 있다. |
| Generalization | 오염 데이터에 의해 정상 일반화가 나빠지거나 특정 조건부 실패가 발생할 수 있다. |
| Label Noise | 단순 라벨 오류처럼 보이는 데이터가 공격 목적을 가질 수 있다. |
| Clean-label Poisoning | 라벨을 바꾸지 않아도 feature 조작만으로 학습 결과를 왜곡할 수 있다. |
| Backdoor Learning | 특정 trigger와 target label 사이의 조건부 관계를 모델이 학습한다. |
| Defense Learning | robust training, data sanitization, anomaly detection 등이 사용된다. |

---

## 5. 보안 이슈 관점 분석

P03은 W02의 중심 보안 문헌이다. 데이터 오염은 학습 단계 공격이므로 추론 단계 방어만으로는 충분하지 않다.

| 보안 항목 | Poisoning 관점 해석 |
|---|---|
| 기밀성 | 오염 데이터에 민감정보가 포함되거나 데이터 출처가 불명확하면 privacy risk가 증가한다. |
| 무결성 | 학습 데이터와 라벨의 무결성이 깨지면 모델 결정경계가 왜곡된다. |
| 가용성 | Availability poisoning은 전체 성능 저하를 유도해 서비스 신뢰성을 낮춘다. |
| 안전성 | 의료, 자율주행, 보안관제 등에서 특정 조건부 실패가 실제 피해로 이어질 수 있다. |
| 책임성 | 데이터 출처, 라벨 변경, 학습 로그가 없으면 사후 원인 추적이 어렵다. |
| 운영 리스크 | 데이터 파이프라인, 외부 데이터셋, crowd labeling, federated client가 공격면이 된다. |

---

## 6. 위협모형

### 6.1 보호 대상

| 보호 대상 | 설명 |
|---|---|
| 학습 데이터 | 입력 샘플, 라벨, 메타데이터, 데이터 출처 |
| 전처리 파이프라인 | 정규화, 증강, 필터링, feature extraction |
| 모델 학습 과정 | optimizer, batch sampling, loss function, checkpoint |
| 검증 데이터 | validation/test split, hidden test data |
| 방어 모듈 | data sanitization, anomaly detector, robust trainer |
| 운영 로그 | 데이터 버전, 라벨 이력, 학습 config, 결과 metric |

### 6.2 공격자 능력

| 공격자 유형 | 가능 행위 |
|---|---|
| Label-flip attacker | 일부 샘플의 라벨을 바꾼다. |
| Clean-label attacker | 라벨은 유지하면서 입력 feature를 조작한다. |
| Backdoor attacker | trigger와 target label의 조건부 관계를 삽입한다. |
| Federated attacker | 악성 client update를 통해 global model을 오염시킨다. |
| Data-supply attacker | 외부 데이터셋, 공개 크롤링 데이터, 라벨링 과정을 오염시킨다. |

### 6.3 공격 경로

```text
외부 또는 내부 데이터 수집
→ 공격자가 일부 데이터/라벨/feature/trigger 조작
→ 오염 데이터가 학습 파이프라인에 포함
→ 모델이 오염된 목적함수를 최소화
→ 정상 조건에서는 성능 유지 가능
→ 특정 조건에서 accuracy drop 또는 ASR 증가 발생
```

---

## 7. 평가방법 및 지표

| 지표 | 의미 | W02/P03에서의 활용 |
|---|---|---|
| Poison Rate | 전체 학습 데이터 중 오염 데이터 비율 | 공격 강도 정의 |
| Clean Accuracy | 정상 테스트셋 정확도 | 은닉성 확인 |
| Accuracy Drop | clean baseline 대비 성능 하락 | availability attack 평가 |
| ASR | trigger/target 조건 공격 성공률 | integrity/backdoor attack 평가 |
| Targeted Error | 특정 클래스 또는 샘플의 목표 오분류율 | targeted poisoning 평가 |
| Detection Rate | 오염 샘플 탐지율 | 방어 성능 평가 |
| False Positive Rate | 정상 샘플을 오염으로 잘못 탐지한 비율 | 데이터 정제 비용 평가 |
| Stealthiness | 오염 데이터가 정상처럼 보이는 정도 | 공격 은닉성 평가 |
| Reproducibility | 오염 설정과 결과 재현성 | seed, config, poison index 기록 필요 |

---

## 8. 재현성 점검

이 논문은 survey 문헌이므로 특정 단일 실험을 그대로 재현하기보다는, poisoning taxonomy를 기반으로 안전한 toy 실험 프로토콜을 구성하는 방식이 적절하다.

| 항목 | 점검 |
|---|---|
| 데이터셋 | MNIST, CIFAR-10, UCI digits, synthetic data 등 공개 데이터 사용 |
| 오염 방식 | label flip, feature noise, toy trigger 등 안전한 교육용 설정만 사용 |
| 공격 범위 | 실제 시스템·실사용 모델·무단 API 대상 실험은 제외 |
| Poison Index | 어떤 샘플이 오염되었는지 index 기록 필요 |
| Seed/Config | seed, poison rate, target label, trigger pattern, split 기록 필요 |
| 결과 파일 | clean accuracy, poisoned accuracy, ASR, detection rate, FPR 저장 |
| 재현 가능성 판단 | toy/public data 실험은 가능. 실제 데이터 공급망 공격 일반화는 제한적 |

### W02 실습 연결

W02에서는 다음 최소 실험으로 P03의 poisoning taxonomy를 재현할 수 있다.

1. 공개 toy 데이터셋을 로딩한다.
2. poisoning ratio를 정한다.
3. label flip 또는 단순 trigger 조건을 만든다.
4. clean model과 poisoned model을 같은 조건에서 학습한다.
5. clean accuracy, accuracy drop, ASR, detection rate를 계산한다.
6. 오염 샘플 index, seed, config, 결과 파일을 저장한다.
7. 실제 공격 절차가 아니라 평가 프레임워크 예시임을 명시한다.

---

## 9. 논문의 고유 기여

1. Poisoning 공격을 공격 목표, 공격자 지식, 오염 위치, 오염 방식, 대상 모델에 따라 체계화했다.
2. Availability attack과 integrity attack을 구분하여 평가 지표를 분리할 수 있게 했다.
3. Label-flipping, clean-label poisoning, backdoor, federated poisoning 등 다양한 공격면을 비교할 수 있는 taxonomy를 제공한다.
4. 방어 전략을 데이터 정제, robust learning, anomaly detection, monitoring 관점으로 연결할 수 있게 한다.
5. W02 기말논문에서 위협모형과 평가 프로토콜의 핵심 근거로 사용할 수 있다.

---

## 10. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| Survey 기반 한계 | 특정 실험 환경의 재현 코드와 단일 성능 결과를 제공하지 않는다. | toy/public data 기반 최소 재현 실험을 별도로 설계한다. |
| 최신 LLM/RAG 확장 필요 | Foundation model, instruction tuning, RAG corpus poisoning은 별도 최신 문헌이 필요하다. | W07, W08, W14와 연결한다. |
| 방어 일반화 어려움 | 특정 데이터셋에서 잘 되는 방어가 다른 도메인에서 실패할 수 있다. | 데이터셋·모델·공격 조건을 명확히 제한한다. |
| 공격-방어 적응성 | 방어가 알려지면 공격자가 우회 전략을 만들 수 있다. | adaptive threat model을 한계로 명시한다. |
| 윤리적 범위 관리 필요 | poisoning 절차는 악용 가능성이 있으므로 실사용 시스템 대상 재현은 부적절하다. | 공개 toy data와 방어 중심 평가로 제한한다. |

---

## 11. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | 데이터 오염은 학습 단계에서 AI 보안성을 훼손하는 핵심 위협이라는 문제의식 제시 |
| 2장 관련연구 | Poisoning taxonomy와 countermeasure 분류 정리 |
| 3장 위협모형 | 공격자 지식, 오염률, 오염 위치, 공격 목표 정의 |
| 4장 연구방법 | poison rate, clean accuracy, accuracy drop, ASR, detection rate 기반 평가 설계 |
| 5장 실험/분석 | label flip 또는 toy backdoor 조건의 결과표 제시 |
| 6장 보안적 함의 | 데이터 무결성, 모델 무결성, 책임성, 감사 가능성 해석 |
| 7장 결론 | AI 보안 연구는 추론 방어뿐 아니라 학습 데이터 보증을 포함해야 함을 제시 |

---

## 12. 기말논문 연결 3문장

1. 이 주차에서 기말논문에 반영할 개념: Poisoning 공격은 학습 데이터와 라벨의 무결성을 훼손하여 모델 학습 목적함수와 결정경계를 왜곡하는 학습 단계 공격이다.
2. 이 주차에서 기말논문에 반영할 표·그림·실험: poisoning taxonomy 표, poison rate 수식, clean accuracy-ASR 비교표, 오염률별 accuracy drop 그래프를 반영한다.
3. 이 주차가 RAG 문서 오염/LLM 보안 감사 프레임워크와 연결되는 지점: RAG 시스템의 검색 문서와 LLM fine-tuning 데이터도 학습·검색 파이프라인의 데이터 자산이므로, P03의 poisoning taxonomy를 W08의 문서 오염과 W14의 MLOps 데이터 검증으로 확장한다.

---

## 13. 최종 판단

이 논문은 W02의 핵심 보안 문헌으로 사용한다. P01이 최적화 원리를 제공하고 P02가 효율성·운영 비용 평가를 제공한다면, P03은 데이터 오염 공격의 taxonomy와 평가 프레임을 제공한다. 기말논문에서는 P03을 중심으로 poisoning threat model을 구성하고, P04와 P05를 통해 training-data poisoning과 backdoor 평가를 세분화하는 것이 적절하다.

---

## 14. 변환 호환성 메모

- GitHub Markdown, MS Word, PDF 변환 호환성을 위해 수식은 LaTeX 블록 수식으로 작성했다.
- 긴 수식은 Markdown 표 안에 넣지 않고 별도 문단으로 분리했다.
- 표에는 변수 설명과 해석만 배치했다.
- DOCX/PDF 변환 시에는 Pandoc 기준으로 다음 명령을 권장한다.

```bash
pandoc P03_summary.md -o P03_summary.docx
pandoc P03_summary.md -o P03_summary.pdf --pdf-engine=xelatex
```
