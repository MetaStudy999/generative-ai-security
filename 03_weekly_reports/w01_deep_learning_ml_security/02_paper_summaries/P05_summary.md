# P05 Summary

## A Survey of Privacy Attacks in Machine Learning — Maria Rigaki, Sebastian Garcia, ACM Computing Surveys, 2023

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W01 딥러닝 패러다임 & ML 보안 분류학 |
| 논문명 | A Survey of Privacy Attacks in Machine Learning |
| 저자 | Maria Rigaki, Sebastian Garcia |
| 학술지 | ACM Computing Surveys |
| 권호/쪽 | Vol. 56, No. 4, Article 101 |
| 연도 | 2023 |
| DOI | https://doi.org/10.1145/3624010 |
| 공개 원고 | https://arxiv.org/abs/2007.07646 |
| 논문 유형 | Survey / Privacy Attacks Review |
| 로컬 PDF | `01_papers/pdf/05_Rigaki_Garcia_2023_Survey_of_Privacy_Attacks_in_ML.pdf` |
| 강의계획서 지정 논문과 일치 여부 | 일치 |
| 핵심 근거 사용 가능 여부 | 가능 |
| 검증 메모 | DOI, arXiv 공개 원고, 로컬 PDF 목록 기준으로 확인. 최종 제출 시 ACM 공식 서지정보와 참고문헌 형식을 재확인한다. |

---

## 1. 한 문장 요약

이 논문은 ML 시스템에서 발생하는 프라이버시 공격을 **공격 대상 자산, 공격자 지식, 공격 인터페이스, 정보 누출 원인, 방어 전략** 기준으로 분류하고, 모델이 정상적으로 동작하더라도 학습 데이터·민감 속성·모델 정보가 유출될 수 있음을 체계화한 핵심 survey 논문이다.

---

## 2. 연구문제

이 논문의 핵심 연구문제는 다음과 같이 정리할 수 있다.

> ML 모델의 학습·추론·배포 과정에서 어떤 정보가 외부로 누출될 수 있으며, 공격자는 어떤 지식과 인터페이스를 이용해 학습 데이터, 민감 속성, 모델 정보를 추론하는가?

### 세부 연구질문

| 번호 | 연구질문 |
|---|---|
| RQ1 | ML 프라이버시 공격은 공격 대상에 따라 어떻게 분류되는가? |
| RQ2 | membership inference, model inversion, property inference는 각각 어떤 정보를 추론하는가? |
| RQ3 | 공격자의 지식 수준과 모델 접근 권한은 프라이버시 공격 성공 가능성에 어떤 영향을 주는가? |
| RQ4 | 모델의 overfitting, confidence score, 출력 인터페이스, 데이터 민감도는 정보 누출과 어떻게 연결되는가? |
| RQ5 | 기말논문에서 프라이버시 위험을 accuracy·robustness와 별도 축으로 어떻게 평가할 수 있는가? |

---

## 3. 핵심 이론 및 수식

> 작성 원칙: GitHub, MS Word, PDF 변환 호환성을 위해 수식은 표 안에 넣지 않고 별도 블록 수식으로 작성한다. 변수 설명은 Markdown 표로 분리한다.

### 3.1 Membership Inference Advantage

Membership inference는 특정 샘플 $z$가 학습 데이터에 포함되었는지 여부를 추론하는 공격이다. 공격 성공 정도는 학습 데이터에 포함된 샘플과 포함되지 않은 샘플을 구분하는 능력으로 표현할 수 있다.

$$
Adv_{MI} = \Pr[A(z)=1 \mid z \in D_{train}]
- \Pr[A(z)=1 \mid z \notin D_{train}]
$$

| 기호 | 의미 |
|---|---|
| $Adv_{MI}$ | membership inference advantage |
| $A$ | membership 여부를 판별하는 공격자 또는 평가기 |
| $z$ | 평가 대상 샘플 |
| $D_{train}$ | 모델 학습에 사용된 데이터셋 |
| $A(z)=1$ | 공격자가 $z$가 학습 데이터에 포함되었다고 판단한 사건 |

### 보안적 의미

$Adv_{MI}$가 클수록 공격자가 학습 데이터 포함 여부를 잘 구분한다는 뜻이다. 이는 모델이 특정 샘플에 대해 과도하게 확신하거나, 학습 데이터와 비학습 데이터에 서로 다른 출력 패턴을 보일 때 커질 수 있다. 따라서 프라이버시 평가는 모델 정확도와 별도로 membership leakage를 측정해야 한다.

---

### 3.2 Overfitting과 프라이버시 누출 위험

프라이버시 공격은 모델이 학습 데이터에 과도하게 적합될수록 쉬워질 수 있다. 단순화하면 일반화 격차를 다음과 같이 표현할 수 있다.

$$
Gap_{gen} = R_{test}(\theta) - R_{train}(\theta)
$$

| 기호 | 의미 |
|---|---|
| $Gap_{gen}$ | 일반화 격차 |
| $R_{train}(\theta)$ | 학습 데이터에서의 위험 또는 손실 |
| $R_{test}(\theta)$ | 테스트 데이터에서의 위험 또는 손실 |
| $\theta$ | 모델 파라미터 |

### 보안적 의미

일반화 격차가 크면 모델이 학습 데이터에 특화된 신호를 더 많이 보존할 수 있다. 이 경우 공격자는 confidence score, loss, decision boundary 근처의 응답 차이를 이용해 특정 샘플의 membership 여부를 추론할 가능성이 높아진다. 단, 일반화 격차만으로 모든 프라이버시 위험을 설명할 수는 없으므로 출력 인터페이스와 공격자 지식도 함께 고려해야 한다.

---

### 3.3 프라이버시-유틸리티 Trade-off

프라이버시 방어는 종종 모델 성능 또는 사용성을 낮춘다. 이를 간단히 다음과 같이 표현할 수 있다.

$$
\Delta_{privacy} = Risk_{privacy}^{baseline} - Risk_{privacy}^{defense}
$$

$$
\Delta_{utility} = Utility_{defense} - Utility_{baseline}
$$

| 기호 | 의미 |
|---|---|
| $\Delta_{privacy}$ | 방어 적용 후 프라이버시 위험 감소량 |
| $Risk_{privacy}^{baseline}$ | 방어 전 프라이버시 위험 |
| $Risk_{privacy}^{defense}$ | 방어 후 프라이버시 위험 |
| $\Delta_{utility}$ | 방어 적용 후 유틸리티 변화 |
| $Utility$ | accuracy, F1, 응답 품질, 서비스 유용성 등 |

### 보안적 의미

프라이버시 방어가 membership inference 위험을 낮추더라도 정확도, 응답 품질, 비용, 지연시간이 크게 악화되면 운영 적용이 어렵다. 따라서 방어 평가는 privacy risk와 utility를 동시에 보고해야 한다.

---

### 3.4 차등프라이버시의 기본 형태

차등프라이버시는 인접 데이터셋 $D$와 $D'$에 대해 알고리즘 출력 분포가 크게 달라지지 않도록 제한하는 프라이버시 보증이다.

$$
\Pr[M(D) \in S] \leq e^{\epsilon} \Pr[M(D') \in S] + \delta
$$

| 기호 | 의미 |
|---|---|
| $M$ | 무작위화된 학습 또는 분석 메커니즘 |
| $D, D'$ | 한 개 샘플만 다른 인접 데이터셋 |
| $S$ | 가능한 출력 사건 집합 |
| $\epsilon$ | 프라이버시 예산. 작을수록 강한 보호 |
| $\delta$ | 작은 실패 확률 허용항 |

### 보안적 의미

차등프라이버시는 membership inference 위험을 이론적으로 줄일 수 있는 대표적 방어지만, 실제 적용에서는 $\epsilon$ 설정, noise 크기, 데이터 전처리, 모델 성능 저하, 반복 질의에 따른 privacy budget 누적을 함께 설명해야 한다.

---

## 4. AI 원리 관점 분석

| 항목 | 분석 |
|---|---|
| 모델 학습 | 모델은 학습 데이터의 통계적 패턴을 파라미터와 결정경계에 반영한다. 이 과정에서 민감 정보가 간접적으로 보존될 수 있다. |
| 추론 인터페이스 | label만 제공하는지, confidence score를 제공하는지, embedding이나 gradient를 제공하는지에 따라 공격 가능성이 달라진다. |
| 일반화 | 과적합이 심하면 학습 데이터와 비학습 데이터에 대한 모델 응답 차이가 커져 membership inference 위험이 증가할 수 있다. |
| 출력 신호 | confidence, loss, entropy, rank, decision margin 등은 privacy leakage의 단서가 될 수 있다. |
| 모델 구조 | 복잡한 모델은 높은 성능을 보일 수 있지만, 학습 데이터의 특이 신호를 더 많이 보존할 가능성도 있다. |
| 방어 학습 | regularization, output restriction, confidence masking, differential privacy, auditing 등이 사용될 수 있다. |
| 평가 문제 | accuracy와 privacy risk는 서로 다른 지표이므로 별도로 측정해야 한다. |

---

## 5. 보안 이슈 관점 분석

P05는 W01의 CIA 관점 중 **기밀성**과 직접 연결된다. 대적 공격이 주로 모델 판단의 무결성을 위협한다면, 프라이버시 공격은 모델이 정상 응답을 하더라도 데이터가 새어 나갈 수 있음을 보여준다.

| 보안 항목 | 프라이버시 공격에서의 의미 |
|---|---|
| 기밀성 | 학습 데이터 포함 여부, 민감 속성, 원본 데이터 특징이 추론될 수 있다. |
| 무결성 | 공격자가 출력 인터페이스를 반복 질의하여 모델 행동을 체계적으로 분석할 수 있다. |
| 가용성 | 강한 방어가 과도한 noise나 응답 제한을 만들면 서비스 품질이 저하될 수 있다. |
| 프라이버시 | membership, attribute, property, inversion 계열 공격이 직접적인 프라이버시 위험이다. |
| 책임성 | 어떤 데이터가 사용되었고 어떤 출력이 제공되었는지 감사 가능해야 한다. |
| 운영 리스크 | API 응답 정책, 로그 보존, privacy budget 관리, 모델 업데이트 이력이 중요하다. |

---

## 6. 위협모형

### 6.1 보호 대상

| 보호 대상 | 설명 |
|---|---|
| 학습 데이터 | 개인정보, 민감 속성, 보안 로그, 의료·금융·행동 데이터 |
| 개별 샘플 membership | 특정 개인 또는 이벤트가 학습에 사용되었는지 여부 |
| 민감 속성 | 성별, 질병, 위치, 조직 속성, 공격 유형 등 직접 공개되지 않은 속성 |
| 집단 속성 | 학습 데이터셋 전체 또는 부분집합의 통계적 특성 |
| 모델 파라미터 | 학습 데이터의 통계적 신호가 반영된 가중치와 구조 |
| 출력 인터페이스 | label, confidence, probability vector, embedding, explanation, API log |

### 6.2 공격자 능력

| 공격자 유형 | 가능 행위 |
|---|---|
| Black-box attacker | 모델에 질의하고 label 또는 confidence score를 관찰한다. |
| Gray-box attacker | 모델 구조, 학습 데이터 분포, 일부 샘플, 출력 정책에 대한 제한 정보를 가진다. |
| White-box attacker | 모델 파라미터, gradient, architecture에 접근할 수 있다. |
| Auxiliary-data attacker | 외부 데이터셋이나 유사 분포 데이터를 이용해 공격 모델을 학습한다. |
| Insider attacker | 학습 로그, 데이터 처리 과정, 모델 버전, API 로그에 접근할 수 있다. |

### 6.3 공격 경로

```text
민감 데이터로 모델 학습
→ 모델이 데이터 패턴을 파라미터와 출력 분포에 반영
→ 공격자가 API 출력, confidence, loss, embedding, 로그를 관찰
→ membership/property/inversion 추론 수행
→ 학습 데이터 또는 민감 속성에 대한 정보 유출 발생
```

---

## 7. 평가방법 및 지표

| 지표 | 의미 | W01/P05에서의 활용 |
|---|---|---|
| MI Accuracy | membership 여부를 맞힌 비율 | membership inference 위험 평가 |
| MI Advantage | 학습 데이터와 비학습 데이터를 구분하는 공격 이득 | privacy leakage 정량화 |
| AUC | 공격자가 membership score로 구분하는 능력 | threshold 독립적 평가 |
| Precision/Recall | 공격 판정의 정확성과 누락 정도 | 공격 평가의 오탐·미탐 확인 |
| Reconstruction Error | model inversion 결과와 실제 민감 정보의 차이 | 복원 공격 평가 |
| Property Inference Accuracy | 학습 데이터 집단 속성 추론 정확도 | 집단 수준 정보 누출 평가 |
| Utility | 방어 후 모델 정확도, F1, 응답 품질 | 프라이버시-성능 trade-off 평가 |
| Privacy Budget | 차등프라이버시의 $\epsilon$, $\delta$ 값 | 이론적 보호 수준 기록 |
| Query Budget | 공격자가 허용받은 API 질의 횟수 | 현실적 공격 비용 평가 |

---

## 8. 재현성 점검

이 논문은 survey 논문이므로 특정 단일 실험을 그대로 재현하기보다는, privacy attack 평가 프로토콜을 toy/public data 환경에서 안전하게 재현하는 방식이 적절하다. 실제 민감정보를 사용하거나 공격 절차를 실서비스에 적용해서는 안 된다.

| 항목 | 점검 |
|---|---|
| 데이터셋 | MNIST, CIFAR-10, UCI Adult, toy tabular data 등 공개 데이터셋 사용 가능. 민감 데이터 사용 시 비식별·윤리 검토 필요 |
| 모델 | Logistic Regression, Random Forest, MLP 등 기본 모델로 최소 재현 가능 |
| 출력 인터페이스 | label-only, confidence score, probability vector 제공 여부를 명시해야 함 |
| 공격 설정 | 공격자 지식, auxiliary data, query budget, threshold 설정 기록 필요 |
| 방어 설정 | regularization, confidence masking, output restriction, differential privacy 적용 조건 기록 필요 |
| seed/config | split seed, model hyperparameter, defense parameter, privacy budget 기록 필요 |
| 결과 파일 | MI accuracy, MI advantage, AUC, utility, privacy-utility trade-off를 CSV/JSON으로 저장 |
| 재현 가능성 판단 | 공개 데이터 기반 toy 평가 가능. 실제 민감 데이터·운영 API 일반화는 제한적 |

### W01 실습 연결

W01에서는 다음 최소 실험으로 P05의 핵심 평가 관점을 안전하게 재현할 수 있다.

1. 공개 toy 데이터셋을 로딩한다.
2. train/test split을 고정하고 기본 분류기를 학습한다.
3. 학습 데이터와 비학습 데이터에 대한 confidence 또는 loss 차이를 비교한다.
4. membership inference risk를 정량화한다.
5. regularization 또는 출력 제한 후 utility와 privacy risk 변화를 비교한다.
6. 결과를 privacy risk, utility, query budget, defense setting과 함께 기록한다.

---

## 9. 논문의 고유 기여

1. ML 프라이버시 공격을 membership inference, model inversion, property inference 등 공격 목표별로 체계화했다.
2. 공격자 지식 수준과 모델 접근 인터페이스가 프라이버시 위험에 미치는 영향을 정리했다.
3. 모델이 정상적으로 동작해도 학습 데이터 또는 민감 속성이 유출될 수 있음을 보여준다.
4. differential privacy, regularization, output restriction, auditing 등 방어 전략을 비교할 수 있는 기준을 제공한다.
5. W01의 보안 평가를 accuracy·robustness 중심에서 privacy leakage까지 확장하는 근거를 제공한다.

---

## 10. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 단일 지표로 요약 어려움 | 프라이버시 위험은 데이터 민감도, 출력 인터페이스, 모델 구조, 공격자 지식에 따라 달라진다. | threat model 표와 privacy metric table을 함께 제시한다. |
| 방어 trade-off 복잡성 | DP, output restriction, regularization은 privacy risk를 낮출 수 있지만 utility를 감소시킬 수 있다. | privacy-utility trade-off 표를 작성한다. |
| 실제 데이터 사용 위험 | 실제 개인정보 데이터로 공격 실험을 수행하면 윤리·법적 문제가 발생할 수 있다. | toy/public data와 방어 중심 평가로 제한한다. |
| LLM/RAG 직접성 부족 | 전통 ML 중심의 privacy attack 논의가 많아 LLM prompt, embedding, RAG 문서 프라이버시는 별도 확장이 필요하다. | W07, W08, W11, W14 문헌과 연결한다. |
| 운영 감사 한계 | 모델 출력 정책과 API 로그가 없으면 사후 프라이버시 사고 분석이 어렵다. | audit log, access control, privacy budget 기록 구조를 기말논문에 반영한다. |

---

## 11. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | AI 모델이 정상적으로 동작해도 학습 데이터와 민감정보가 유출될 수 있다는 문제의식 제시 |
| 2장 관련연구 | membership inference, model inversion, property inference 등 privacy attack taxonomy 정리 |
| 3장 위협모형 | 공격자 지식, 출력 인터페이스, 보호 대상 데이터, query budget 정의 |
| 4장 연구방법 | MI advantage, AUC, utility, privacy budget 기반 평가 설계 |
| 5장 실험/분석 | toy/public data 기반 privacy risk와 utility trade-off 분석 |
| 6장 보안적 함의 | 기밀성, 프라이버시, 책임성, 감사가능성 관점에서 해석 |
| 7장 결론 | AI 보안 평가는 정확도·강건성·프라이버시 위험을 별도 축으로 동시에 보고해야 함을 제시 |

---

## 12. 기말논문 연결 3문장

1. 이 주차에서 기말논문에 반영할 개념: ML 프라이버시 공격은 모델이 정상적으로 응답해도 학습 데이터 포함 여부, 민감 속성, 집단 속성이 유출될 수 있음을 보여준다.
2. 이 주차에서 기말논문에 반영할 표·그림·실험: privacy attack taxonomy, 공격자 지식 수준 표, MI advantage 수식, privacy-utility trade-off 표를 반영한다.
3. 이 주차가 RAG 문서 오염/LLM 보안 감사 프레임워크와 연결되는 지점: RAG/LLM 환경에서도 프롬프트, 검색 문서, embedding, API 응답 로그가 민감정보 누출 경로가 될 수 있으므로 P05의 privacy threat model을 W07/W08/W14의 LLM 운영 보안 평가로 확장한다.

---

## 13. 최종 판단

이 논문은 W01에서 프라이버시 공격 축을 담당하는 핵심 문헌으로 사용한다. P03이 탐지 성능과 오탐·미탐 문제를 제공하고 P04가 대적 강건성 평가를 제공한다면, P05는 accuracy와 robustness로 설명되지 않는 데이터 기밀성 위험을 제공한다. 기말논문에서는 P05를 통해 AI 보안 평가축을 “성능, 강건성, 프라이버시, 재현성, 운영 감사”로 확장하는 것이 적절하다.

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
