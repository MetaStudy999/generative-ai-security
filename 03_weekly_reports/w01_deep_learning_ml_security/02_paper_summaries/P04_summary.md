# P04 Summary

## Adversarial Attacks and Defenses in Machine Learning-Powered Networks: A Contemporary Survey — Yulong Wang et al., arXiv, 2023

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W01 딥러닝 패러다임 & ML 보안 분류학 |
| 논문명 | Adversarial Attacks and Defenses in Machine Learning-Powered Networks: A Contemporary Survey |
| 저자 | Yulong Wang, Tong Sun, Shenghong Li, Xin Yuan, Wei Ni, Ekram Hossain, H. Vincent Poor |
| 학술지/출처 | arXiv preprint |
| arXiv ID | 2303.06302 |
| 연도 | 2023 |
| DOI/URL | https://doi.org/10.48550/arXiv.2303.06302 |
| 논문 유형 | Survey / Adversarial ML Review |
| 로컬 PDF | `01_papers/pdf/04_Wang_et_al_2023_Adversarial_Attacks_and_Defenses.pdf` |
| 강의계획서 지정 논문과 일치 여부 | 확인 필요. 강의계획서의 P04 지정 논문과 제목이 다르므로 현재 파일은 관련 논문 또는 대체 논문으로 관리한다. |
| 핵심 근거 사용 가능 여부 | 제한적 가능. 최종 제출 전 지정 논문 교체 여부 또는 대체 사용 사유를 명시해야 한다. |
| 검증 메모 | arXiv 제목·저자·초록 기준으로 확인. 최종 제출 시 강의계획서 지정 IEEE Communications Surveys & Tutorials 논문과 동일성 여부를 재확인한다. |

---

## 1. 한 문장 요약

이 논문은 ML-powered network와 DNN 기반 분류 모델을 대상으로 한 대적 공격과 방어를 **공격 원리, 공격자 지식 수준, 방어 메커니즘, 평가 한계, gradient masking, clean accuracy와 robust accuracy의 trade-off** 관점에서 분류한 최신 survey 논문이다.

---

## 2. 연구문제

이 논문의 핵심 연구문제는 다음과 같이 정리할 수 있다.

> ML 기반 네트워크 시스템에서 공격자는 어떤 방식으로 모델 입력과 추론 결과를 교란하며, 방어자는 어떤 조건과 지표로 실제 강건성이 향상되었는지를 검증해야 하는가?

### 세부 연구질문

| 번호 | 연구질문 |
|---|---|
| RQ1 | 대적 예제는 어떤 최적화 문제로 정의할 수 있는가? |
| RQ2 | white-box, gray-box, black-box 공격은 공격자 지식과 능력 측면에서 어떻게 구분되는가? |
| RQ3 | gradient-based, score-based, decision-based, search-based, physical-world attack은 어떤 원리로 작동하는가? |
| RQ4 | 방어 방법은 탐지, 입력 정제, adversarial training, regularization, certified defense로 어떻게 구분되는가? |
| RQ5 | 방어 성능 평가는 clean accuracy, robust accuracy, ASR, 계산 비용, transferability, gradient masking 여부를 어떻게 함께 고려해야 하는가? |

---

## 3. 핵심 이론 및 수식

> 작성 원칙: GitHub, MS Word, PDF 변환 호환성을 위해 수식은 표 안에 넣지 않고 별도 블록 수식으로 작성한다. 변수 설명은 Markdown 표로 분리한다.

### 3.1 대적 교란의 일반 목적함수

대적 공격은 원본 입력 $x$에 제한된 크기의 교란 $\delta$를 추가하여 모델의 손실을 증가시키거나 목표 오분류를 유도하는 문제로 볼 수 있다.

$$
\max_{\delta \in \mathcal{S}} \ell(f_{\theta}(x + \delta), y)
$$

| 기호 | 의미 |
|---|---|
| $x$ | 정상 입력 |
| $y$ | 정답 레이블 |
| $\delta$ | 공격자가 추가하는 입력 교란 |
| $\mathcal{S}$ | 허용 가능한 교란 집합. 예: $\lVert \delta \rVert_p \leq \epsilon$ |
| $f_{\theta}$ | 파라미터 $\theta$를 가진 ML/DNN 모델 |
| $\ell(\cdot)$ | 손실함수 |

### 보안적 의미

일반 ML 평가는 정상 입력 $x$에서 모델이 맞는지를 본다. 반면 대적 ML 평가는 공격자가 제한된 범위의 교란 $\delta$를 선택할 수 있을 때도 모델이 안정적인지를 본다. 따라서 높은 clean accuracy는 강건성을 보장하지 않는다.

---

### 3.2 강건 최적화 관점

방어 모델은 정상 손실뿐 아니라 최악의 교란 조건에서도 손실이 작아지도록 학습될 수 있다.

$$
\min_{\theta} \frac{1}{n}\sum_{i=1}^{n} \max_{\delta_i \in \mathcal{S}} \ell(f_{\theta}(x_i + \delta_i), y_i)
$$

| 기호 | 의미 |
|---|---|
| $n$ | 학습 샘플 수 |
| $x_i, y_i$ | $i$번째 입력과 정답 |
| $\delta_i$ | $i$번째 입력에 대한 허용 교란 |
| $\mathcal{S}$ | 위협모형이 허용하는 교란 범위 |
| $\theta$ | 학습 대상 모델 파라미터 |

### 보안적 의미

이 식은 adversarial training의 기본 아이디어를 나타낸다. 그러나 강건 학습은 계산 비용이 높고, clean accuracy가 낮아질 수 있으며, 특정 위협모형에만 강해지는 문제가 있다. 따라서 방어 성능은 공격 조건을 명시하지 않고는 해석할 수 없다.

---

### 3.3 Robust Accuracy와 Attack Success Rate

방어 성능은 정상 정확도와 공격 조건 정확도를 분리해서 평가해야 한다.

$$
RobustAcc = \frac{1}{n}\sum_{i=1}^{n} \mathbf{1}\left[f_{\theta}(x_i + \delta_i^{adv}) = y_i\right]
$$

$$
ASR = \frac{1}{n}\sum_{i=1}^{n} \mathbf{1}\left[f_{\theta}(x_i + \delta_i^{adv}) \neq y_i\right]
$$

| 기호 | 의미 |
|---|---|
| $RobustAcc$ | 공격 입력에서 모델이 정답을 유지한 비율 |
| $ASR$ | Attack Success Rate, 공격 성공률 |
| $\delta_i^{adv}$ | 공격 알고리즘으로 생성한 대적 교란 |
| $\mathbf{1}[\cdot]$ | 조건이 참이면 1, 거짓이면 0인 지시 함수 |

### 보안적 의미

$RobustAcc$와 $ASR$은 보완 관계에 있다. 단, multi-class targeted attack, untargeted attack, rejection option, 탐지 기반 방어가 포함되면 단순한 보완 관계가 깨질 수 있으므로 평가 프로토콜을 명확히 써야 한다.

---

### 3.4 Clean-Robust Trade-off

방어 적용 전후 성능은 다음과 같은 trade-off로 볼 수 있다.

$$
\Delta_{robust} = RobustAcc_{defense} - RobustAcc_{baseline}
$$

$$
\Delta_{clean} = CleanAcc_{defense} - CleanAcc_{baseline}
$$

| 기호 | 의미 |
|---|---|
| $\Delta_{robust}$ | 방어 적용 후 공격 조건 정확도 변화 |
| $\Delta_{clean}$ | 방어 적용 후 정상 조건 정확도 변화 |
| $CleanAcc$ | 정상 테스트 데이터 정확도 |
| $RobustAcc$ | 공격 입력에서의 정확도 |

### 보안적 의미

방어가 $RobustAcc$를 높이더라도 $CleanAcc$를 크게 낮추면 실제 운영에서 사용하기 어렵다. 따라서 방어 평가는 보안성만이 아니라 사용성, 지연시간, 비용, 유지보수성을 함께 고려해야 한다.

---

## 4. AI 원리 관점 분석

| 항목 | 분석 |
|---|---|
| 모델 구조 | DNN 기반 분류 모델은 고차원 입력을 내부 표현으로 변환하고 결정경계를 학습한다. |
| 추론 취약성 | 입력 공간의 작은 변화가 내부 표현과 결정경계를 넘어서면 오분류가 발생할 수 있다. |
| gradient 활용 | white-box 공격은 손실함수의 입력 기울기를 이용해 교란 방향을 계산한다. |
| black-box 추정 | score 또는 decision 결과만으로도 반복 질의를 통해 공격 입력을 탐색할 수 있다. |
| physical-world attack | 디지털 픽셀 교란뿐 아니라 카메라, 센서, 무선 네트워크, 물리 환경에서도 공격이 가능하다. |
| 방어 학습 | adversarial training, regularization, input transformation, detection 등이 사용된다. |
| 평가 문제 | 공격자 지식과 위협모형이 불명확하면 방어 성능을 비교할 수 없다. |

---

## 5. 보안 이슈 관점 분석

P04는 W01의 “보안 이슈 30%” 중 대적 머신러닝 축을 담당한다. 이 논문은 정상 데이터에서 높은 성능을 보이는 모델이 공격자가 만든 입력에서도 안전하다는 보장이 없음을 보여준다.

| 보안 항목 | 대적 ML에서의 의미 |
|---|---|
| 기밀성 | 모델 출력과 confidence가 반복 질의를 통해 공격자에게 정보를 제공할 수 있다. |
| 무결성 | 공격자가 입력을 조작하여 모델 판단을 원하는 방향으로 바꾼다. |
| 가용성 | 방어가 과도한 차단이나 지연을 만들면 서비스 운영성이 저하된다. |
| 안전성 | 자율주행, 의료, 네트워크 제어 등에서 오분류가 물리적 피해로 이어질 수 있다. |
| 책임성 | 공격 조건, 방어 설정, 실패 사례가 기록되지 않으면 사후 감사가 어렵다. |
| 운영 리스크 | 방어가 특정 공격에는 효과적이지만 adaptive attack이나 transfer attack에는 실패할 수 있다. |

---

## 6. 위협모형

### 6.1 보호 대상

| 보호 대상 | 설명 |
|---|---|
| 입력 데이터 | 이미지, 트래픽, 센서값, 네트워크 상태, 로그 |
| 모델 결정경계 | 정상 입력과 공격 입력을 구분하는 학습된 경계 |
| 추론 API | 모델 입력·출력, confidence, score, decision 응답 |
| 방어 모듈 | 입력 정제, 탐지기, robust classifier, rejection policy |
| 운영 시스템 | 네트워크 제어, IoT 시스템, 자율 시스템, 보안 탐지 시스템 |

### 6.2 공격자 능력

| 공격자 유형 | 가능 행위 |
|---|---|
| White-box attacker | 모델 구조, 파라미터, gradient, 손실함수에 접근한다. |
| Gray-box attacker | 모델 구조 일부, 학습 데이터 분포, confidence score 등 제한 정보를 가진다. |
| Black-box attacker | 입력과 출력 또는 decision 결과만 관찰하며 반복 질의한다. |
| Physical attacker | 센서·카메라·무선 환경 등 물리 환경의 입력을 조작한다. |
| Adaptive attacker | 방어 존재를 알고 우회 전략을 설계한다. |

### 6.3 공격 경로

```text
정상 모델 학습
→ 운영 환경에 모델 배포
→ 공격자가 모델 접근 수준을 파악
→ 허용 범위 내 입력 교란 또는 반복 질의 수행
→ 모델 오분류 또는 방어 우회 발생
→ 서비스 무결성·안전성 저하
```

---

## 7. 평가방법 및 지표

| 지표 | 의미 | W01/P04에서의 활용 |
|---|---|---|
| Clean Accuracy | 정상 입력에서의 정확도 | 기본 사용성 확인 |
| Robust Accuracy | 공격 입력에서의 정확도 | 방어 성능 핵심 지표 |
| Attack Success Rate, ASR | 공격 목표 달성 비율 | 공격 효과 측정 |
| Robust Drop | clean accuracy와 robust accuracy의 차이 | 공격에 따른 성능 저하 확인 |
| Perturbation Budget | 허용 교란 크기 | 위협모형의 강도 정의 |
| Query Budget | black-box 공격에서 허용 질의 횟수 | 현실적 공격 비용 평가 |
| Transferability | 한 모델에서 만든 공격이 다른 모델에도 통하는 정도 | gradient masking 여부 점검 |
| Latency | 방어 적용 후 추론 지연 | 운영 가능성 평가 |
| Compute Cost | 방어 학습·추론 비용 | 실제 적용 가능성 평가 |
| Failure Case Audit | 방어 실패 사례 기록 | 재현성과 사후 분석 |

---

## 8. 재현성 점검

이 논문은 survey 논문이므로 특정 실험 하나를 그대로 재현하기보다는, 공격-방어 평가 프로토콜을 재현 가능한 형태로 구성하는 것이 적절하다.

| 항목 | 점검 |
|---|---|
| 데이터셋 | MNIST, CIFAR-10, UCI digits, 네트워크 트래픽 데이터 등 공개 데이터셋 활용 가능 |
| 모델 | Logistic Regression, MLP, CNN 등 간단한 baseline부터 시작 |
| 공격 설정 | 위협모형, 교란 크기, 공격자 지식 수준, query budget 명시 필요 |
| 방어 설정 | adversarial training, input transformation, detection 등 적용 조건 기록 필요 |
| seed/config | 데이터 split, 모델 초기화, attack parameter, defense parameter 저장 필요 |
| 결과 파일 | clean accuracy, robust accuracy, ASR, runtime, 실패 사례를 CSV/JSON으로 저장 |
| 재현 가능성 판단 | 표준 데이터셋과 공개 공격 구현 사용 시 중간 이상. 실제 네트워크·물리 환경 일반화는 제한적 |

### W01 실습 연결

W01에서는 다음 최소 실험으로 P04의 핵심 평가 관점을 재현할 수 있다.

1. UCI digits 또는 MNIST 계열 데이터셋을 로딩한다.
2. baseline classifier를 학습한다.
3. 정상 테스트 정확도와 손실을 기록한다.
4. 제한된 크기의 입력 교란을 적용한 테스트셋을 만든다.
5. clean accuracy, robust accuracy, ASR, robust drop을 계산한다.
6. 방어 또는 간단한 입력 정제를 적용한 뒤 성능 변화를 비교한다.
7. 결과를 공격 조건, 교란 크기, 모델 설정과 함께 기록한다.

---

## 9. 논문의 고유 기여

1. ML-powered network 환경에서 대적 공격과 방어의 최신 연구 흐름을 공격 원리 기준으로 분류했다.
2. gradient-based 공격뿐 아니라 search-based, decision-based, drop-based, physical-world attack 등 다양한 공격 경로를 정리했다.
3. 방어 방법을 counter-attack detection과 robustness enhancement 관점으로 구분했다.
4. robust training, regularization, gradient masking, transferability, clean accuracy 저하 문제를 함께 논의했다.
5. 기말논문에서 사용할 수 있는 “정상 성능과 공격 조건 성능을 분리하여 보고해야 한다”는 평가 원칙을 제공한다.

---

## 10. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 지정 논문 동일성 확인 필요 | 현재 P04는 arXiv 관련 논문이며, 강의계획서 지정 IEEE CS&T 논문과 동일 여부가 불명확하다. | 최종 제출 전 지정 논문으로 교체하거나 관련 논문 사용 사유를 명시한다. |
| survey 기반 한계 | 특정 방어법의 실제 효과를 직접 검증하는 실험 논문이 아니다. | toy 실험 또는 공개 데이터셋 기반 최소 재현 실험을 추가한다. |
| 공격 조건 의존성 | 방어 성능은 교란 범위, 공격자 지식, query budget에 크게 좌우된다. | threat model 표를 먼저 제시하고 그 조건 안에서 결과를 해석한다. |
| gradient masking 위험 | 일부 방어는 실제 강건성을 높이지 않고 gradient만 숨길 수 있다. | transfer attack, black-box evaluation, adaptive attack 검토 항목을 추가한다. |
| 운영 환경 일반화 한계 | 네트워크·IoT·물리 환경에서는 디지털 벤치마크 성능이 그대로 유지되지 않을 수 있다. | latency, compute cost, failure case audit를 추가한다. |

---

## 11. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | ML 시스템은 정상 성능이 높아도 공격 조건에서 취약할 수 있다는 문제의식 제시 |
| 2장 관련연구 | 대적 공격과 방어 taxonomy, white/black-box threat model 정리 |
| 3장 위협모형 | 공격자 지식, 교란 범위, query budget, physical-world 조건 정의 |
| 4장 연구방법 | clean accuracy, robust accuracy, ASR, robust drop 기반 평가 설계 |
| 5장 실험/분석 | toy adversarial perturbation 또는 문헌 기반 공격-방어 비교표 제시 |
| 6장 보안적 함의 | 무결성, 안전성, 가용성, 운영 비용 관점에서 방어 trade-off 해석 |
| 7장 결론 | AI 보안 평가는 정상 성능·공격 성능·재현성·운영성을 함께 보고해야 함을 제시 |

---

## 12. 기말논문 연결 3문장

1. 이 주차에서 기말논문에 반영할 개념: 대적 ML은 정상 입력 성능과 공격 입력 성능이 다르다는 점을 보여주며, AI 보안 평가는 clean accuracy와 robust accuracy를 분리해야 한다.
2. 이 주차에서 기말논문에 반영할 표·그림·실험: 공격자 지식 수준 표, 공격-방어 taxonomy, clean/robust accuracy 비교표, ASR 계산표, defense trade-off 표를 반영한다.
3. 이 주차가 RAG 문서 오염/LLM 보안 감사 프레임워크와 연결되는 지점: RAG/LLM 보안에서도 공격자는 입력 문서나 프롬프트를 조작해 모델 출력을 교란하므로, P04의 threat model·ASR·robustness 평가 관점을 W08의 프롬프트 인젝션 평가로 확장한다.

---

## 13. 최종 판단

이 논문은 W01에서 대적 머신러닝의 평가 원칙을 제공하는 관련 핵심 문헌으로 사용한다. 다만 강의계획서 지정 P04와 동일한지 확인이 필요하므로, 최종 제출 전 문헌 검증표에서 “지정 논문”인지 “관련 대체 논문”인지 명확히 분리해야 한다. 기말논문에서는 P04를 통해 정상 성능 중심 평가의 한계를 지적하고, 공격자 지식·교란 범위·공격 성공률·방어 비용을 포함한 보안 평가 체계를 구성하는 것이 적절하다.

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
