# P02 Summary

## Adversarial Attacks and Defenses in Deep Learning: From a Perspective of Cybersecurity — Shuai Zhou et al., ACM Computing Surveys, 2022

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W12 신경망 검증(Neural Network Verification) & XAI Robustness |
| 공식 논문명 | Adversarial Attacks and Defenses in Deep Learning: From a Perspective of Cybersecurity |
| 공식 저자 | Shuai Zhou et al. |
| 공식 출판 정보 | ACM Computing Surveys, 2022 |
| DOI | https://doi.org/10.1145/3547330 |
| 로컬 PDF | `01_papers/pdf/02_Ren_et_al_2020_Adversarial_Attacks_Defenses_Deep_Learning.pdf` |
| 로컬 PDF 상태 | W12 `paper_list.md` 기준 로컬 PDF는 Kui Ren et al., `Adversarial Attacks and Defenses in Deep Learning`, Engineering 6, 2020, DOI `10.1016/j.eng.2019.12.012` 문헌이다. 공식 P02 DOI 논문과 동일 문헌으로 단정하지 않는다. |
| 검증 상태 | W12 `paper_list.md` 기준 관련 논문 공식 DOI 확인. 지정 논문명과 로컬 PDF 파일명·저자·매체·연도 차이 메모 유지 |
| PDF 확인 메모 | repo의 PDF 폴더에 P02 관련 PDF blob이 존재함을 확인했다. 다만 로컬 PDF는 공식 P02 지정 논문과 다르거나 보조 문헌이므로, summary는 공식 DOI 기준 P02를 중심으로 작성하고 로컬 PDF는 adversarial attack/defense 보완 문헌으로만 해석한다. |
| 핵심 근거 사용 가능 여부 | 가능. W12에서 adversarial attack/defense taxonomy, cybersecurity threat model, robust accuracy, ASR, empirical defense evaluation을 설명하는 관련 핵심 문헌으로 사용 |

---

## 1. 한 문장 요약

공식 P02 논문은 딥러닝 시스템의 adversarial attacks and defenses를 **cybersecurity perspective, adversary knowledge, attack surface, evasion attack, poisoning/backdoor 연결, targeted/untargeted misclassification, adversarial training, detection, preprocessing, robust evaluation, transferability, defense bypass, empirical robustness limitation** 관점에서 정리하며, W12에서 empirical adversarial robustness와 P01의 formal verification certificate를 구분해 설명하는 연결 문헌이다.

---

## 2. 핵심 연구문제

> 딥러닝 모델은 입력에 작은 교란이 추가될 때 오분류될 수 있으며, 공격자의 지식·접근권한·목표에 따라 공격과 방어의 평가 방식이 달라진다. 따라서 adversarial robustness 평가는 공격 조건, perturbation budget, norm, target 여부, defense configuration, formal guarantee 여부를 명확히 분리해 보고해야 한다.

| 번호 | 연구질문 |
|---|---|
| RQ1 | Adversarial attack은 white-box, black-box, gray-box, transfer-based 조건에서 각각 어떤 공격자 지식과 능력을 가정하는가? |
| RQ2 | Evasion, poisoning, backdoor, model extraction, defense bypass는 deep learning 보안 위협에서 어떻게 연결되는가? |
| RQ3 | Adversarial training, input preprocessing, detection, certified defense, model regularization은 어떤 방어 효과와 한계를 갖는가? |
| RQ4 | Robust accuracy, ASR, perturbation budget, transferability, defense cost를 어떻게 분리해 평가해야 empirical defense claim을 과장하지 않을 수 있는가? |
| RQ5 | 로컬 PDF가 공식 DOI 논문과 다를 때, 관련 PDF의 내용을 지정 논문처럼 인용하지 않고 어떻게 보완 문헌으로 관리해야 하는가? |

---

## 3. 논문의 핵심 기여

| 기여 | 설명 | W12 연결 |
|---|---|---|
| Cybersecurity 관점 taxonomy | adversarial attack과 defense를 공격자 지식, 공격면, 보안 목표 기준으로 정리 | W12 threat model 설계 |
| 공격·방어 mapping | evasion attack, poisoning/backdoor, transfer attack과 adversarial training, detection, preprocessing, certification을 연결 | P01 formal verification과 P04 Lipschitz robustness 연결 |
| Robustness 평가 강조 | clean accuracy와 robust accuracy, ASR, perturbation budget을 분리해야 함을 강조 | W12 평가방법 기준 |
| Defense limitation 정리 | 경험적 방어는 adaptive attacker와 defense bypass에 취약할 수 있음을 설명 | empirical claim 제한 문구 근거 |
| 로컬 PDF 관리 주의 | W12 P02는 공식 DOI와 로컬 PDF가 다르므로 인용 기준 분리가 필요 | 기말논문 참고문헌 검증표 근거 |

---

## 4. 목차별 핵심 개괄

| 목차 | 핵심 내용 | 비전공자용 이해 |
|---|---|---|
| 1. Introduction | 딥러닝은 이미지·음성·텍스트·보안 시스템에서 널리 쓰이지만, adversarial perturbation에 취약할 수 있다. | AI가 사람이 보기에는 거의 같은 입력을 다르게 판단할 수 있다. |
| 2. Cybersecurity Perspective | adversarial attack을 정보보안의 위협모형, 공격자 지식, 공격 목표, 공격면 관점으로 재해석한다. | 공격자가 무엇을 알고 무엇을 조작할 수 있는지 먼저 정해야 한다. |
| 3. Attack Taxonomy | white-box/black-box, targeted/untargeted, evasion/poisoning/backdoor, transfer attack 등을 분류한다. | 공격은 “운영 중 입력을 속이는 공격”과 “학습 때 모델을 오염시키는 공격” 등으로 나뉜다. |
| 4. Defense Taxonomy | adversarial training, input transformation, detection, gradient masking 방지, certified defense, model regularization 등을 정리한다. | 공격 예시로 훈련하거나, 입력을 정제하거나, 이상 입력을 탐지하거나, 수학적 보장을 시도한다. |
| 5. Evaluation Protocol | perturbation budget, norm, attack strength, adaptive attacker, transferability, robust accuracy, clean accuracy를 명확히 보고해야 한다. | 방어 성능은 어떤 조건에서 시험했는지가 중요하다. 약한 공격만 막았다고 강한 방어라고 말하면 안 된다. |
| 6. Limitations of Empirical Defenses | 경험적 방어는 특정 공격에만 강하고 adaptive attacker에 취약할 수 있다. | 한 공격을 막았다고 모든 공격을 막는 것은 아니다. |
| 7. Relation to Formal Verification | empirical robustness와 certified robustness는 다른 증거이며, formal verification은 특정 명세와 입력 범위에 대해서만 보장한다. | 테스트 통과와 수학적 증명은 다르다. |
| 8. Future Directions | scalable certified defense, realistic threat model, benchmark standardization, robust evaluation, deployment security가 과제로 남는다. | 실제 AI 보안에는 표준화된 공격·방어 평가와 검증 증거가 필요하다. |
| 로컬 관련 PDF 메모 | 로컬 PDF는 Ren et al. 2020 Engineering 논문이며, official P02와 동일 문헌으로 단정하지 않는다. | PDF가 있다고 해서 공식 지정 논문과 동일하게 인용하면 안 된다. |

---

## 5. 핵심 이론 및 수식

> 아래 수식은 adversarial robustness 평가와 W12 보안 보고서의 metric 설계를 설명하기 위한 표준화된 표현이다. 실제 공격 절차 제공이 아니라 평가 지표와 방어 검증 구조를 설명하기 위한 것이다.

### 5.1 Adversarial Objective

공격자는 허용된 perturbation 집합 $\Delta$ 안에서 loss를 증가시키는 입력 교란을 찾는 것으로 표현할 수 있다.

$$
\max_{\delta\in\Delta}\ell(f_\theta(x+\delta),y)
$$

| 기호 | 의미 |
|---|---|
| $x$ | 원본 입력 |
| $y$ | 정답 label |
| $\delta$ | adversarial perturbation |
| $\Delta$ | 허용 perturbation 집합 |
| $f_\theta$ | 딥러닝 모델 |

### 보안적 의미

공격 조건은 $\Delta$의 norm, epsilon, targeted 여부, white/black-box 여부에 따라 완전히 달라진다. 따라서 attack setting을 생략하면 robustness claim을 검증할 수 없다.

---

### 5.2 Perturbation Budget

Perturbation은 특정 norm과 budget으로 제한된다.

$$
\Delta=\{\delta:\|\delta\|_p\leq \epsilon\}
$$

| 기호 | 의미 |
|---|---|
| $p$ | $L_p$ norm 유형 |
| $\epsilon$ | perturbation budget |

### 보안적 의미

$L_\infty$, $L_2$, $L_1$ 등 norm 선택에 따라 평가 결과가 달라진다. 서로 다른 norm의 robust accuracy를 직접 비교하면 안 된다.

---

### 5.3 Robust Accuracy

Adversarial input에 대해 모델이 정답을 유지한 비율이다.

$$
RobustAcc=\frac{1}{n}\sum_{i=1}^{n}\mathbf{1}[f_\theta(x_i^{adv})=y_i]
$$

### 보안적 의미

Clean accuracy가 높아도 adversarial input에서 robust accuracy가 낮으면 공격에 취약하다. W12에서는 clean accuracy와 robust accuracy를 분리 보고한다.

---

### 5.4 Attack Success Rate

공격이 목표 오분류 또는 target label 유도에 성공한 비율이다.

$$
ASR=\frac{N_{successful\ attacks}}{N_{attempted\ attacks}}
$$

### 보안적 의미

방어 평가는 ASR 감소와 robust accuracy 증가를 함께 봐야 한다. 단, 공격 강도와 query budget도 함께 기록해야 한다.

---

### 5.5 Adversarial Training Objective

Adversarial training은 최악 perturbation에 대한 loss를 줄이도록 학습한다.

$$
\min_\theta \mathbb{E}_{(x,y)\sim D}\left[\max_{\delta\in\Delta}\ell(f_\theta(x+\delta),y)\right]
$$

### 보안적 의미

Adversarial training은 대표 방어지만 clean accuracy, training cost, 특정 공격 norm에 대한 overfitting 문제가 있을 수 있다.

---

### 5.6 Clean-Robust Trade-off

방어 적용 후 clean accuracy와 robust accuracy가 달라질 수 있다.

$$
Tradeoff_{CR}=Acc_{clean}-RobustAcc
$$

### 보안적 의미

방어가 robust accuracy를 높이더라도 clean accuracy를 크게 낮추면 실사용성이 떨어진다. P05의 robustness-accuracy-fairness trade-off와 연결된다.

---

### 5.7 Formal-Empirical Gap

경험적 공격 평가와 형식 검증 결과는 서로 다른 증거다.

$$
FormalEmpiricalGap=CertifiedRobustRate-EmpiricalRobustAcc
$$

### 보안적 의미

Empirical robust accuracy가 높아도 formal certificate가 없으면 모든 perturbation을 막는다는 뜻이 아니다. 반대로 certificate는 특정 input domain과 property 안에서만 의미가 있다.

---

## 6. AI 원리 70% 관점 분석

| 원리 항목 | 설명 | W12/P02에서의 의미 |
|---|---|---|
| Adversarial Example | 작은 입력 교란으로 모델 오분류 유도 | robust evaluation의 기본 대상 |
| Threat Model | white/black-box, targeted/untargeted, query budget | 공격 조건 명확화 |
| Perturbation Budget | 허용 교란 범위와 norm | robustness metric 조건 |
| Robust Accuracy | adversarial input에서 정답 유지율 | defense 성능 평가 |
| ASR | 공격 성공률 | 공격 효과 측정 |
| Adversarial Training | worst-case perturbation을 학습에 포함 | 대표 empirical defense |
| Defense Bypass | 특정 방어가 adaptive attack에 우회될 수 있음 | claim 제한 필요 |
| Formal vs Empirical | 실험적 방어와 증명 기반 방어 구분 | P01 verification 연결 |

---

## 7. 보안 이슈 30% 관점 분석

| 보안 항목 | Adversarial Robustness 관점 해석 | 대표 평가 지표 |
|---|---|---|
| 기밀성 | 모델 구조·gradient·confidence가 공격자 지식이 될 수 있음 | white/black-box scope |
| 무결성 | 입력이 미세하게 조작되어 모델 decision이 왜곡될 수 있음 | ASR, robust accuracy |
| 가용성 | 강한 방어가 inference latency와 training cost를 증가시킬 수 있음 | defense cost, latency |
| 프라이버시 | adversarial testing trace와 input sample이 민감 데이터를 포함할 수 있음 | trace anonymization |
| 안전성 | 자율주행·의료·보안 모델에서 오분류가 실제 피해로 연결될 수 있음 | safety violation, targeted ASR |
| 책임성 | attack setting과 defense config를 기록해야 재현 가능 | evaluation trace completeness |

---

## 8. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | model decision, input integrity, classifier confidence, safety output, defense configuration, evaluation log |
| 공격자 목표 | evasion, targeted misclassification, robust accuracy 저하, defense bypass, transfer attack 성공 |
| 공격자 능력 | input perturbation, model query, confidence 관찰, surrogate model 보유, white-box gradient 접근 가능성 |
| 공격 경로 | clean input → perturbation generation/evaluation → model inference → misclassification 또는 unsafe decision |
| 방어자 능력 | adversarial training, preprocessing, detection, certified defense, input validation, evaluation logging |
| 제외 범위 | 실제 시스템 공격, 구체적 adversarial example 생성 절차, 악용 코드, 무단 모델 질의 자동화 |

---

## 9. 평가방법 및 지표

| 평가축 | 지표 | 의미 | W12/P02 활용 |
|---|---|---|---|
| 정상 성능 | clean accuracy | 원본 입력 성능 | utility baseline |
| 공격 강건성 | robust accuracy, ASR | adversarial input 대응 | 핵심 robustness 평가 |
| 공격 조건 | norm, epsilon, targeted 여부, query budget | attack setting 명확화 | 재현성 필수 |
| 전이성 | transferability rate | surrogate attack 성공 여부 | black-box 위험 |
| 방어 비용 | training cost, inference latency, memory overhead | 방어 운영 비용 | 실무 적용성 |
| 방어 신뢰성 | adaptive attack performance, defense bypass rate | 방어 우회 가능성 | claim 제한 |
| 형식 검증 비교 | certified robust rate, FormalEmpiricalGap | empirical/formal 차이 | P01 연결 |
| 서지 정확성 | official DOI match, local PDF mismatch flag | 참고문헌 정확성 | 기말논문 검증표 |

---

## 10. 재현성 체크리스트

| 항목 | 기록해야 할 내용 |
|---|---|
| Bibliographic status | 공식 DOI 논문과 로컬 PDF 동일 여부, mismatch flag |
| Model | architecture, dataset, model hash, training config |
| Attack setting | white/black-box, targeted/untargeted, norm, epsilon, query budget |
| Defense setting | adversarial training, preprocessing, detection, certification 등 |
| Evaluation | clean accuracy, robust accuracy, ASR, transferability, defense cost |
| Randomness | seed, attack initialization, data split, model checkpoint |
| Adaptive setting | 방어를 아는 공격자 여부, defense bypass 평가 여부 |
| Formal comparison | certified result가 있는 경우 property, verifier, timeout 기록 |
| Logs | attack config, defense config, evaluation script, failure case |
| 한계 | empirical robustness 결과를 모든 공격과 모든 환경에 대한 보장으로 과장하지 않음 |

---

## 11. 논문의 고유 기여

1. Adversarial attack과 defense를 cybersecurity perspective에서 정리한다.
2. 공격자 지식, 공격 목표, 공격면, defense bypass를 threat model에 포함해야 함을 설명한다.
3. Clean accuracy, robust accuracy, ASR, perturbation budget을 분리해 평가해야 함을 강조한다.
4. W12 P01의 formal verification과 연결되어 empirical robustness와 certified robustness 차이를 설명하는 근거가 된다.
5. W12 P02는 로컬 PDF mismatch가 있으므로 참고문헌 검증표와 공식 DOI 우선 인용의 중요성을 보여주는 사례다.

---

## 12. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 로컬 PDF 불일치 | P02 로컬 PDF는 공식 DOI 논문과 다른 Ren et al. 2020 Engineering 문헌이다. | 공식 DOI 기준으로 인용하고 로컬 PDF는 보완 문헌으로 표시 |
| Empirical defense 한계 | 특정 공격에서 성능이 좋아도 adaptive attack에 취약할 수 있다. | adaptive threat model과 claim limitation 명시 |
| Perturbation norm 제한 | 특정 norm/epsilon 평가가 모든 실제 공격을 대표하지 않는다. | norm, epsilon, target 여부를 명확히 기록 |
| Defense cost | adversarial training은 계산비용과 clean accuracy 손실이 크다. | clean-robust trade-off와 cost 병기 |
| Formal guarantee 부족 | empirical robust accuracy는 수학적 보장이 아니다. | P01 certificate와 분리 보고 |
| Benchmark 차이 | dataset/model/attack setting 차이로 논문 간 비교가 어렵다. | attack-defense-metric matrix와 config log 필수화 |

---

## 13. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | AI 보안 평가는 clean accuracy가 아니라 adversarial setting에서 robust behavior를 봐야 한다는 문제의식 |
| 2장 관련연구 | 공식 P02 DOI 논문을 adversarial attacks/defenses cybersecurity survey로 정리하고, 로컬 PDF mismatch는 검증표에 기록 |
| 3장 위협모형 | input integrity, model decision, classifier confidence, defense config 보호 자산 정의 |
| 4장 연구방법 | robust accuracy, ASR, perturbation budget, transferability, defense cost, FormalEmpiricalGap 지표 설계 |
| 5장 분석 | adversarial threat model table과 empirical vs formal robustness 비교표 제시 |
| 6장 보안적 함의 | adaptive attack, defense bypass, certified defense 필요성, 참고문헌 검증 필요성 해석 |

---

## 14. 기말논문 연결 3문장

1. W12에서 기말논문에 반영할 개념: adversarial robustness 평가는 공격자의 지식, perturbation budget, norm, target 여부를 명확히 정의한 뒤 clean accuracy와 robust accuracy를 분리해 보고해야 한다.
2. W12에서 기말논문에 반영할 표·그림·실험: adversarial threat model 표, robust accuracy·ASR·transferability 평가표, empirical defense와 formal certificate 비교표, 공식 DOI/로컬 PDF mismatch 검증표를 반영한다.
3. W12가 LLM/RAG 보안 감사 프레임워크와 연결되는 지점: LLM/RAG 입력 교란·prompt perturbation·retrieval poisoning도 adversarial setting으로 볼 수 있으므로, threat model, evaluation config, failure case, evidence log를 W14/W15 evidence chain에 포함해야 한다.

---

## 15. 최종 판단

P02는 W12의 adversarial robustness 관련 핵심 문헌이다. 다만 W12 `paper_list.md` 기준 로컬 PDF는 공식 DOI 논문과 다른 Ren et al. 2020 Engineering 문헌으로 기록되어 있으므로, 기말논문 참고문헌에는 공식 DOI 논문인 Shuai Zhou et al.의 ACM Computing Surveys 논문을 우선 사용해야 한다. 로컬 PDF는 adversarial attack/defense 일반 배경을 보완하는 관련 문헌으로만 제한해 활용하는 것이 적절하다.

---

## 16. 변환 호환성 메모

```bash
pandoc P02_summary.md -o P02_summary.docx
pandoc P02_summary.md -o P02_summary.pdf --pdf-engine=xelatex
```
