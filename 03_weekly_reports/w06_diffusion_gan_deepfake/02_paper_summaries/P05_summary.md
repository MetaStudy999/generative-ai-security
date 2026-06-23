# P05 Summary

## Deepfake Detection: A Comprehensive Survey from the Reliability Perspective — Tianyi Wang et al., ACM Computing Surveys, 2025

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W06 확률생성모형(Diffusion/GAN) & 딥페이크 검출 |
| 논문명 | Deepfake Detection: A Comprehensive Survey from the Reliability Perspective |
| 저자 | Tianyi Wang et al. |
| 학술지 | ACM Computing Surveys |
| 권호/쪽 | Vol. 57, No. 3, pp. 1–35 |
| 연도 | online 2024 / print 2025 |
| DOI | https://doi.org/10.1145/3699710 |
| 보조 URL | https://arxiv.org/abs/2211.10881 |
| 로컬 PDF | `01_papers/pdf/05_Wang_et_al_2024_Deepfake_Detection_Reliability_Survey.pdf` |
| 검증 상태 | W06 `paper_list.md` 기준 DOI/URL 확인. 강의계획서 저자 축약/오기 가능성 메모 유지 |

---

## 1. 한 문장 요약

이 논문은 딥페이크 검출을 단순 이진분류가 아니라 **generalization, robustness, interpretability, calibration, fairness, open-set detection, reliability** 관점에서 재정의하고, W06에서 검출기의 실제 운영 신뢰성을 평가하는 핵심 기준을 제공한다.

---

## 2. 핵심 연구질문

| 번호 | 연구질문 |
|---|---|
| RQ1 | 딥페이크 검출기의 높은 in-domain 성능이 실제 환경 신뢰성을 보장하지 않는 이유는 무엇인가? |
| RQ2 | 생성기·데이터셋·압축·플랫폼 변화가 검출 일반화에 어떤 영향을 주는가? |
| RQ3 | Robustness, calibration, interpretability, fairness는 검출 reliability와 어떻게 연결되는가? |
| RQ4 | 실제 운영 검출 시스템은 threshold, human review, provenance evidence를 어떻게 기록해야 하는가? |

---

## 3. 핵심 수식

### 3.1 Reliability-Aware Detection Risk

$$
Risk_{det}=\alpha FN+\beta FP+\gamma ECE+\lambda Cost
$$

| 기호 | 의미 |
|---|---|
| $FN$ | fake를 real로 놓치는 미탐 |
| $FP$ | real을 fake로 오탐 |
| $ECE$ | Expected Calibration Error |
| $Cost$ | 검출 지연·검토 비용 |

### 3.2 Calibration Error

$$
ECE=\sum_{m=1}^{M}\frac{|B_m|}{n}\left|acc(B_m)-conf(B_m)\right|
$$

**보안 해석:** 검출 확률이 과신되면 운영자가 잘못된 판단을 내릴 수 있다. 딥페이크 검출은 맞고 틀림뿐 아니라 confidence calibration도 평가해야 한다.

---

## 4. Reliability 평가축

| 축 | 의미 |
|---|---|
| Generalization | 보지 못한 생성기·데이터셋에서 성능 유지 |
| Robustness | 압축·노이즈·크롭·재인코딩 후 성능 유지 |
| Interpretability | 검출 근거가 artifact나 의미 있는 단서인지 설명 가능 |
| Calibration | confidence가 실제 정확도와 일치하는지 |
| Fairness | 얼굴 속성·조명·품질·집단별 성능 편차 점검 |
| Open-set | 새로운 생성 방식 등장 시 unknown 처리 가능성 |

---

## 5. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 대상 | 검출기 신뢰성, 검출 로그, 실제 영상, 합성 영상, 사용자 권리 |
| 공격자 목표 | 검출 회피, 낮은 품질 변환으로 detector 무력화, false accusation 유도 |
| 공격자 능력 | 압축, blur, crop, noise, adversarial post-processing, 생성기 변경 |
| 방어자 능력 | cross-dataset test, calibration, human review, provenance 확인 |
| 제외 범위 | 실제 딥페이크 배포, 개인 영상 수집, 검출기 우회 절차 제공 |

---

## 6. 평가방법 및 지표

| 지표 | 의미 |
|---|---|
| AUC / F1 | 기본 검출 성능 |
| Cross-dataset AUC | 일반화 성능 |
| Robustness Drop | 변환 후 성능 하락 |
| ECE | calibration 품질 |
| FPR/FNR | 오탐·미탐 비용 |
| Subgroup Performance | 집단별 성능 편차 |
| Explanation Consistency | 설명 근거 안정성 |
| Provenance Coverage | 생성·편집·검토 로그 보존 정도 |

---

## 7. 재현성·기말논문 연결

| 항목 | 반영 내용 |
|---|---|
| 재현성 | 데이터셋 버전, 생성기, 압축 조건, threshold, detector checkpoint 기록 |
| 한계 | 실험실 성능을 소셜미디어·실제 수사·법적 판단 성능으로 과장하지 않음 |
| 기말논문 | 딥페이크 검출 reliability 평가표, calibration, human-in-the-loop 설계에 반영 |

---

## 8. 최종 판단

P05는 W06의 검출 신뢰성 핵심 문헌이다. P04가 딥페이크 생성·검출 taxonomy를 제공한다면 P05는 실제 운영 신뢰성, 일반화, calibration, robustness를 평가하는 기준을 제공한다.
