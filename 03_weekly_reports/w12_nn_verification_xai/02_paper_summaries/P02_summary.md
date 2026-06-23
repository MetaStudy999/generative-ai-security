# P02 Summary

## Adversarial Attacks and Defenses in Deep Learning: From a Perspective of Cybersecurity — Shuai Zhou et al., ACM Computing Surveys, 2022

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W12 Neural Network Verification & XAI Robustness |
| 논문명 | Adversarial Attacks and Defenses in Deep Learning: From a Perspective of Cybersecurity |
| 저자 | Shuai Zhou et al. |
| 출판 정보 | ACM Computing Surveys, 2022 |
| DOI | https://doi.org/10.1145/3547330 |
| 검증 상태 | W12 `paper_list.md` 기준 관련 논문 공식 DOI 확인. 로컬 PDF는 Ren et al. 2020 문헌으로 동일성 확인 메모 유지 |

---

## 1. 한 문장 요약

이 논문은 딥러닝의 adversarial attack과 defense를 **cybersecurity perspective, threat model, attack surface, defense taxonomy, robustness evaluation** 관점에서 정리하며, W12의 대적 강건성 평가 배경을 제공한다.

---

## 2. 핵심 연구질문

| 번호 | 연구질문 |
|---|---|
| RQ1 | 딥러닝 대적공격은 어떤 공격자 지식과 능력을 가정하는가? |
| RQ2 | 방어는 adversarial training, detection, preprocessing, certification으로 어떻게 나뉘는가? |
| RQ3 | Robust accuracy와 ASR을 어떻게 분리해 평가해야 하는가? |
| RQ4 | empirical defense가 형식 검증 없이 과장될 위험은 무엇인가? |

---

## 3. 핵심 수식

$$
\max_{\delta\in\Delta}\ell(f_\theta(x+\delta),y)
$$

$$
RobustAcc=\frac{1}{n}\sum_{i=1}^{n}\mathbf{1}[f_\theta(x_i^{adv})=y_i]
$$

---

## 4. 위협모형·평가지표

| 항목 | 내용 |
|---|---|
| 보호 자산 | model decision, input integrity, classifier confidence, safety output |
| 공격자 목표 | evasion, targeted misclassification, defense bypass |
| 지표 | robust accuracy, ASR, perturbation budget, transferability, defense cost |
| 재현성 | attack setting, epsilon, norm, model version, seed, defense config 기록 |

---

## 5. 기말논문 연결

P02는 W12의 adversarial robustness 문헌이다. 기말논문에서는 empirical robustness와 formal verification의 차이를 설명하는 연결 문헌으로 사용한다.

---

## 6. 최종 판단

P02는 관련 논문으로 사용하되, W12 지정 문헌/로컬 PDF 차이 메모를 유지한다.
