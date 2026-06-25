# P05 Summary

## Triangular Trade-off between Robustness, Accuracy, and Fairness in Deep Neural Networks: A Survey — Jingyang Li, Guoqiang Li, ACM Computing Surveys, 2025

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W12 신경망 검증(Neural Network Verification) & XAI Robustness |
| 공식 논문명 | Triangular Trade-off between Robustness, Accuracy, and Fairness in Deep Neural Networks: A Survey |
| 공식 저자 | Jingyang Li, Guoqiang Li |
| 공식 출판 정보 | ACM Computing Surveys, 2025 |
| DOI | https://doi.org/10.1145/3645088 |
| 로컬 PDF | `01_papers/pdf/05_RELATED_Singh_et_al_2021_Accuracy_Fairness_Robustness_Study.pdf` |
| 로컬 PDF 상태 | W12 `paper_list.md` 기준 로컬 PDF는 Moninder Singh et al., `An Empirical Study of Accuracy, Fairness, Explainability, Distributional Robustness, and Adversarial Robustness`, arXiv:2109.14653 관련 보조 문헌이다. 공식 P05 DOI 논문과 동일 문헌으로 단정하지 않는다. |
| 검증 상태 | W12 `paper_list.md` 기준 관련 논문 공식 DOI 확인. 강의자료의 `Chih-Hsiang Cheng et al.` 표기와 최종 반영표의 `Jingyang Li, Guoqiang Li` 표기 차이, 로컬 PDF 차이 메모 유지 |
| PDF 확인 메모 | repo의 PDF 폴더에 P05 관련 PDF blob이 존재함을 확인했다. 다만 로컬 PDF는 공식 P05 지정 논문과 다르거나 보조 문헌이므로, summary는 공식 DOI 기준 P05를 중심으로 작성하고 로컬 PDF는 accuracy/fairness/robustness empirical trade-off 보완 문헌으로만 해석한다. |
| 핵심 근거 사용 가능 여부 | 가능. W12에서 robustness, accuracy, fairness의 삼각 trade-off, subgroup risk, calibration, sociotechnical evaluation을 설명하는 핵심 관련 문헌으로 사용 |

---

## 1. 한 문장 요약

공식 P05 논문은 deep neural network의 보안·성능·공정성 평가를 **clean accuracy, adversarial robustness, certified/empirical robust accuracy, group fairness, subgroup error, calibration, robustness-fairness conflict, defense cost, sociotechnical risk** 관점에서 통합적으로 정리하며, W12에서 AI 보안 방어를 robust accuracy 하나로 판단하지 않고 **accuracy-robustness-fairness 삼각 trade-off**로 평가해야 함을 보여주는 핵심 관련 문헌이다.

---

## 2. 핵심 연구문제

> AI 보안 방어는 adversarial robustness를 높일 수 있지만, 동시에 clean accuracy를 낮추거나 특정 집단의 오류율과 calibration을 악화시킬 수 있다. 따라서 안전한 AI 보안 평가는 전체 평균 성능이 아니라 집단별 위험, 공정성, 강건성, 비용을 함께 고려해야 한다.

| 번호 | 연구질문 |
|---|---|
| RQ1 | Robustness를 높이는 방어가 clean accuracy, calibration, model capacity, subgroup performance에 어떤 비용을 만드는가? |
| RQ2 | 전체 robust accuracy가 높아져도 특정 subgroup의 FPR/FNR, robust error, calibration error가 악화될 수 있는가? |
| RQ3 | Fairness metric과 adversarial robustness metric은 어떤 조건에서 충돌하거나 상호 보완되는가? |
| RQ4 | AI 보안 보고서에서 clean accuracy, robust accuracy, fairness gap, subgroup risk, calibration, cost를 어떻게 함께 제시해야 하는가? |
| RQ5 | 로컬 PDF가 공식 DOI 논문과 다른 관련 문헌일 때, trade-off summary와 참고문헌 인용을 어떻게 분리 관리해야 하는가? |

---

## 3. 논문의 핵심 기여

| 기여 | 설명 | W12 연결 |
|---|---|---|
| 삼각 trade-off 체계화 | robustness, accuracy, fairness의 상호 긴장 관계를 survey 형태로 정리 | W12 사회기술적 평가축 |
| 평균 성능 한계 지적 | 전체 accuracy/robust accuracy만으로는 subgroup risk를 볼 수 없음을 강조 | subgroup evaluation 필요성 |
| 방어 부작용 분석 | adversarial training, robust optimization, regularization이 clean utility와 fairness에 미치는 영향 정리 | P02/P04 방어 평가 보완 |
| 공정성 지표 연결 | group fairness, FPR/FNR gap, equalized odds, calibration gap 등과 robustness를 연결 | 기말논문 metric 설계 |
| 로컬 PDF 관리 주의 | W12 P05는 공식 DOI와 로컬 PDF가 다르므로 인용 기준 분리가 필요 | 참고문헌 검증표 근거 |

---

## 4. 목차별 핵심 개괄

| 목차 | 핵심 내용 | 비전공자용 이해 |
|---|---|---|
| 1. Introduction | AI 모델의 평가는 accuracy만으로 충분하지 않으며, adversarial robustness와 fairness를 함께 고려해야 한다. | AI가 평균적으로 잘 맞혀도 특정 집단에 더 자주 틀리거나 공격에 더 약하면 안전하지 않다. |
| 2. Accuracy and Robustness | Clean accuracy와 robust accuracy의 차이, adversarial training의 효과와 비용을 정리한다. | 평소에는 잘 맞히는 모델이 공격 입력에서는 쉽게 틀릴 수 있다. |
| 3. Fairness in DNNs | Demographic parity, equalized odds, subgroup FPR/FNR, calibration 등 공정성 지표를 정리한다. | 전체 점수보다 집단별로 얼마나 공평하게 작동하는지가 중요하다. |
| 4. Robustness-Fairness Interaction | Robustness 방어가 특정 집단의 성능을 더 악화시키거나, fairness constraint가 robustness를 낮출 수 있음을 논의한다. | 보안을 강화했더니 일부 집단에서 더 많이 틀리는 일이 생길 수 있다. |
| 5. Triangular Trade-off | accuracy, robustness, fairness를 동시에 최적화하기 어렵고, metric 간 균형을 봐야 함을 설명한다. | 성능·보안·공정성을 모두 만점으로 만들기 어렵기 때문에 균형표가 필요하다. |
| 6. Evaluation Protocols | clean/robust accuracy, subgroup metrics, fairness gap, calibration, attack setting, defense cost를 함께 보고해야 한다. | 보안 논문도 집단별 성능표와 공격 조건표를 같이 내야 한다. |
| 7. Challenges | metric 충돌, benchmark 부족, sensitive attribute availability, deployment domain shift, governance 문제가 남아 있다. | 어떤 공정성 기준을 쓸지, 어떤 집단 정보를 쓸지부터 어렵다. |
| 8. Future Directions | multi-objective optimization, subgroup robustness, fair robust training, calibrated robustness, audit governance가 필요하다. | 앞으로는 “강한 AI”보다 “강하고 공정하며 검증 가능한 AI”가 중요하다. |
| 로컬 관련 PDF 메모 | 로컬 PDF는 Singh et al. 2021 empirical study로 보이며, official P05와 동일 문헌으로 단정하지 않는다. | PDF가 있다고 해서 공식 지정 논문과 동일하게 인용하면 안 된다. |

---

## 5. 핵심 이론 및 수식

> 아래 수식은 robustness-accuracy-fairness trade-off와 W12 사회기술적 보안 평가를 설명하기 위한 표준화된 표현이다. 수식은 GitHub, MS Word, PDF 변환 호환성을 위해 Markdown 표 밖의 LaTeX block math로 작성한다.

### 5.1 통합 Trade-off Score

보안 방어 평가에서 accuracy, robustness, fairness gap, cost를 함께 고려할 수 있다.

$$
Score=\alpha Acc_{clean}+\beta RobustAcc-\gamma FairnessGap-\lambda Cost
$$

| 기호 | 의미 |
|---|---|
| $Acc_{clean}$ | 원본 입력에서의 정확도 |
| $RobustAcc$ | adversarial input에서의 정확도 |
| $FairnessGap$ | 집단 간 성능 또는 오류율 격차 |
| $Cost$ | 학습·추론·감사 비용 |

### 보안적 의미

방어가 robust accuracy를 높여도 fairness gap이나 비용이 크게 증가하면 전체적으로 좋은 방어라고 보기 어렵다.

---

### 5.2 Fairness Gap

집단 A와 B의 성능 또는 오류율 차이를 측정한다.

$$
FairnessGap=|Metric_{groupA}-Metric_{groupB}|
$$

### 보안적 의미

특정 집단의 FPR, FNR, robust error가 더 높으면 보안 방어가 불공정한 피해를 만들 수 있다.

---

### 5.3 Subgroup Robustness Gap

집단별 robust accuracy 차이를 측정한다.

$$
RobustGap=\max_g RobustAcc_g-\min_g RobustAcc_g
$$

| 기호 | 의미 |
|---|---|
| $g$ | subgroup 또는 sensitive group |
| $RobustAcc_g$ | 집단 $g$의 robust accuracy |

### 보안적 의미

전체 robust accuracy가 높아도 특정 집단의 robust accuracy가 낮으면 공격에 취약한 집단이 존재한다.

---

### 5.4 Equalized Odds Gap

집단 간 FPR/FNR 차이를 함께 측정한다.

$$
EOGap=\max\left(|FPR_A-FPR_B|,\;|FNR_A-FNR_B|\right)
$$

### 보안적 의미

보안 시스템에서 FPR 차이는 정상 사용자를 더 많이 차단하는 문제를 만들고, FNR 차이는 특정 집단의 공격 또는 위험을 더 많이 놓치는 문제를 만든다.

---

### 5.5 Calibration Gap

집단별 calibration 품질 차이를 측정한다.

$$
CalibrationGap=|ECE_A-ECE_B|
$$

| 기호 | 의미 |
|---|---|
| $ECE$ | Expected Calibration Error |

### 보안적 의미

모델 confidence가 특정 집단에서 과신되거나 과소평가되면 human-in-the-loop 판단과 risk scoring이 왜곡될 수 있다.

---

### 5.6 Robustness-Accuracy Trade-off

방어 후 clean accuracy와 robust accuracy의 차이를 본다.

$$
CleanRobustGap=Acc_{clean}-RobustAcc
$$

### 보안적 의미

Adversarial robustness를 얻는 과정에서 정상 입력 성능이 얼마나 손상되는지 확인해야 한다.

---

### 5.7 Multi-objective Loss

accuracy, robustness, fairness를 함께 최적화하려는 학습 목표를 표현할 수 있다.

$$
\min_\theta \mathcal{L}_{task}(\theta)+\alpha \mathcal{L}_{robust}(\theta)+\beta \mathcal{L}_{fair}(\theta)
$$

### 보안적 의미

보안 방어는 단일 목적 최적화가 아니라 다목적 최적화 문제다. 각 항의 가중치는 정책적 판단을 포함한다.

---

## 6. AI 원리 70% 관점 분석

| 원리 항목 | 설명 | W12/P05에서의 의미 |
|---|---|---|
| Clean Accuracy | 정상 입력에서의 평균 성능 | utility baseline |
| Robust Accuracy | 공격 입력에서의 성능 | 보안 방어 효과 |
| Fairness Metric | 집단별 성능·오류율 차이 | 사회기술적 안전성 |
| Calibration | confidence와 실제 정답률 일치 | risk 판단 신뢰성 |
| Adversarial Training | robust accuracy 개선 방법 | fairness·accuracy 비용 가능 |
| Multi-objective Optimization | 여러 목표를 동시에 최적화 | trade-off 해석 |
| Subgroup Evaluation | 집단별 성능 분석 | 평균 성능의 한계 보완 |
| Governance Metric | 정책·책임성·감사 지표 | W15 evidence chain 연결 |

---

## 7. 보안 이슈 30% 관점 분석

| 보안 항목 | Trade-off 관점 해석 | 대표 평가 지표 |
|---|---|---|
| 기밀성 | subgroup attribute와 평가 로그가 민감정보일 수 있음 | sensitive attribute handling |
| 무결성 | 평균 성능만 제시하면 방어 효과가 왜곡될 수 있음 | subgroup audit, metric completeness |
| 가용성 | 강한 방어가 latency와 비용을 높이고 정상 사용성을 낮출 수 있음 | Cost, latency, clean accuracy |
| 프라이버시 | 공정성 평가를 위해 sensitive attribute를 사용할 때 privacy risk 발생 | privacy-aware fairness audit |
| 안전성 | 특정 집단이 공격이나 오류에 더 취약하면 사회적 피해 발생 | RobustGap, EOGap, subgroup FNR |
| 책임성 | accuracy·robustness·fairness·calibration을 함께 기록해야 감사 가능 | audit completeness, evidence log |

---

## 8. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | model decision, group-level performance, fairness metric, robustness claim, calibration, sensitive attribute handling, audit evidence |
| 공격자/위험 목표 | 특정 subgroup 취약성 악용, 평균 robust accuracy로 위험 은폐, fairness metric 누락, robustness overclaim |
| 공격자/위험 능력 | subgroup-specific perturbation, distribution shift 유발, benchmark cherry-picking, metric selection bias |
| 위험 경로 | defense training → average robust accuracy improvement → subgroup error 증가 또는 calibration 악화 → unfair/sunsafe deployment |
| 방어자 능력 | subgroup robustness evaluation, fairness audit, calibration check, multi-objective reporting, governance review |
| 제외 범위 | 실제 집단 대상 공격, 민감 속성 재식별, 차별적 운영 절차, 특정 개인·집단 피해 유도 |

---

## 9. 평가방법 및 지표

| 평가축 | 지표 | 의미 | W12/P05 활용 |
|---|---|---|---|
| 정상 성능 | clean accuracy, loss | 원본 입력 성능 | utility baseline |
| 강건성 | robust accuracy, ASR, certified radius | 공격 입력 방어 효과 | P02/P04 연결 |
| 집단 공정성 | FairnessGap, EOGap, subgroup FPR/FNR | 집단 간 성능·오류 차이 | 핵심 fairness 평가 |
| 집단 강건성 | RobustGap, subgroup robust accuracy | 집단별 공격 취약성 | subgroup risk |
| Calibration | ECE, CalibrationGap | confidence 신뢰성 | human-in-loop 위험 |
| 비용 | training cost, inference latency, audit cost | 방어 운영 비용 | MLOps 연결 |
| 보고 완전성 | metric completeness, group definition log | 평가 누락 방지 | W15 evidence chain |
| 서지 정확성 | official DOI match, local PDF mismatch flag | 참고문헌 정확성 | 기말논문 검증표 |

---

## 10. 재현성 체크리스트

| 항목 | 기록해야 할 내용 |
|---|---|
| Bibliographic status | 공식 DOI 논문과 로컬 PDF 동일 여부, mismatch flag |
| Dataset | train/test split, subgroup definition, sensitive attribute 처리 방식 |
| Model | architecture, model hash, training config |
| Attack/robustness setting | norm, epsilon, attack type, robust training 여부 |
| Fairness metric | demographic parity, equalized odds, FPR/FNR gap, subgroup accuracy 등 |
| Calibration | ECE, subgroup ECE, confidence binning 방식 |
| Evaluation | clean accuracy, robust accuracy, FairnessGap, RobustGap, EOGap, Cost |
| Governance | sensitive attribute access rule, privacy-preserving fairness audit 여부 |
| Logs | seed, config, metric script, subgroup report, failure case |
| 한계 | 평균 성능 결과를 모든 집단의 안전성과 공정성 보장으로 과장하지 않음 |

---

## 11. 논문의 고유 기여

1. Robustness, accuracy, fairness의 삼각 trade-off를 보안 평가의 핵심 문제로 체계화한다.
2. 평균 robust accuracy만으로는 subgroup risk와 fairness harm을 설명할 수 없음을 보여준다.
3. Adversarial defense의 부작용을 clean accuracy, fairness, calibration, cost 관점으로 확장한다.
4. W12 P01~P04의 formal/empirical robustness 논의를 사회기술적 평가축으로 마무리한다.
5. W12 P05는 로컬 PDF mismatch가 있으므로 참고문헌 검증표와 공식 DOI 우선 인용의 중요성을 보여주는 사례다.

---

## 12. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 로컬 PDF 불일치 | P05 로컬 PDF는 공식 DOI 논문과 다른 Singh et al. 2021 관련 empirical study다. | 공식 DOI 기준으로 인용하고 로컬 PDF는 보완 문헌으로 표시 |
| Metric 충돌 | fairness metric 간에도 서로 충돌할 수 있다. | 사용할 metric과 선택 이유 명시 |
| Sensitive attribute 문제 | fairness 평가에는 민감 속성이 필요할 수 있으나 privacy risk가 있다. | privacy-aware fairness audit로 제한 |
| 평균 성능 착시 | 전체 robust accuracy가 subgroup 취약성을 가릴 수 있다. | subgroup robust accuracy와 RobustGap 병기 |
| Domain shift | 배포 환경이 달라지면 fairness/robustness 관계도 달라진다. | distribution shift 한계 명시 |
| 정책 판단 개입 | trade-off 가중치는 기술적 값이 아니라 정책적 판단을 포함한다. | 가중치와 의사결정 근거를 명시 |

---

## 13. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | AI 보안 방어는 robust accuracy만으로 평가할 수 없고 accuracy·fairness·calibration을 함께 봐야 한다는 문제의식 |
| 2장 관련연구 | 공식 P05 DOI 논문을 robustness-accuracy-fairness trade-off survey로 정리하고, 로컬 PDF mismatch는 검증표에 기록 |
| 3장 위협모형 | subgroup performance, fairness metric, robustness claim, calibration, audit evidence 보호 자산 정의 |
| 4장 연구방법 | Score, FairnessGap, RobustGap, EOGap, CalibrationGap, CleanRobustGap 지표 설계 |
| 5장 분석 | robustness-accuracy-fairness triangular trade-off 그림과 subgroup risk table 제시 |
| 6장 보안적 함의 | 평균 성능 착시, subgroup 취약성, fairness governance, 참고문헌 검증 필요성 해석 |

---

## 14. 기말논문 연결 3문장

1. W12에서 기말논문에 반영할 개념: AI 보안 방어는 adversarial robustness를 높이더라도 clean accuracy, fairness, calibration을 악화시킬 수 있으므로 다목적 trade-off로 평가해야 한다.
2. W12에서 기말논문에 반영할 표·그림·실험: trade-off score, FairnessGap, RobustGap, EOGap, CalibrationGap 평가표와 robustness-accuracy-fairness 삼각 그림, 공식 DOI/로컬 PDF mismatch 검증표를 반영한다.
3. W12가 LLM/RAG 보안 감사 프레임워크와 연결되는 지점: RAG/LLM 안전장치도 전체 평균 성능뿐 아니라 사용자 집단별 실패율, 거절률, hallucination risk, citation reliability, audit evidence를 W14/W15 evidence chain에 포함해야 한다.

---

## 15. 최종 판단

P05는 W12의 사회기술적 평가축을 담당하는 핵심 관련 문헌이다. 다만 W12 `paper_list.md` 기준 로컬 PDF는 공식 DOI 논문과 다른 Singh et al. 2021 empirical study 관련 문헌으로 기록되어 있으므로, 기말논문 참고문헌에는 공식 DOI 논문인 Jingyang Li and Guoqiang Li의 ACM Computing Surveys 논문을 우선 사용해야 한다. 로컬 PDF는 accuracy/fairness/robustness empirical trade-off를 보완하는 관련 문헌으로만 제한해 활용하는 것이 적절하다.

---

## 16. 변환 호환성 메모

```bash
pandoc P05_summary.md -o P05_summary.docx
pandoc P05_summary.md -o P05_summary.pdf --pdf-engine=xelatex
```
