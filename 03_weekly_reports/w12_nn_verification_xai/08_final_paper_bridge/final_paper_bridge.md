# W12 기말논문 연결표

## 1. 이번 주차에서 얻은 연구 주제 후보

| 번호 | 주제 후보 | 대상 시스템 | 보안 위협 | 방법론 | 기여 가능성 |
|---:|---|---|---|---|---|
| 1 | 강건성·설명안정성·공정성·재현성을 함께 보고하는 AI 보안 평가 프레임워크 | AI/ML 평가 파이프라인 | 대적 입력, 설명 조작, 검증 누락 | 문헌분석, 체크리스트, toy 실험 | 높음 |
| 2 | XAI 기반 설명 결과의 대적공격 취약성 평가 연구 | XAI 설명 시스템 | explanation manipulation, saliency/attribution instability | synthetic perturbation 실험, 사례분석 | 높음 |
| 3 | 대규모 AI 모델의 위험기반 부분검증 프로토콜 연구 | 신경망 검증 파이프라인 | verification scalability failure | 프레임워크 설계, 비용 지표 | 높음 |
| 4 | Robustness-accuracy-fairness trade-off 보고 양식 연구 | AI 보안 연구 보고서 | 단일 지표 과신, 공정성 영향 은폐 | 평가표 설계, 재현성 로그 | 보통 |

## 2. 기말 논문에 반영할 내용

| 논문 장 | 반영 가능 내용 |
|---|---|
| 서론 | AI 모델 강건성과 설명가능성 검증의 필요성, 정확도 중심 보고의 한계 |
| 관련연구 | 신경망 검증, 대적방어, adversarial XAI, Lipschitz robustness, robustness-accuracy-fairness trade-off survey |
| 연구문제 | 강건성·정확도·공정성·설명안정성 통합 평가 |
| 연구방법 | 문헌분석, threat model, synthetic binary classification 기반 안전 toy 실험, 체크리스트 설계 |
| 분석/실험 | clean accuracy 0.818750, robust accuracy 0.543750, explanation stability 0.927782, certified rate 0.543750, fairness gap 0.039141, verification cost 0.223524를 기준 예시로 다중지표 보고 |
| 보안적 함의 | 무결성, 안전성, 책임성, 공정성, 재현성 관점 |
| 연구윤리 | AI 활용 고지, DOI/PDF 검증 상태 분리, 공개 PDF 저작권 위험 표시 |
| 결론 | 위험기반 AI 검증·XAI 보안 평가체계 제안 |

## 3. KCI 형식 연결

| 항목 | 초안 |
|---|---|
| 국문 제목 | 신경망 검증과 XAI 안정성을 고려한 AI 보안 다중지표 평가 프레임워크 |
| 연구목적 | AI 보안 평가에서 clean accuracy, robust accuracy, certified proxy, explanation stability, fairness gap, verification cost를 함께 보고하는 절차 제시 |
| 연구방법 | 국내외 선행연구 분석, 위협모형 정리, synthetic toy 실험, 재현성 체크리스트 |
| 기대효과 | 보안 평가 보고서에서 단일 성능 지표 과신을 줄이고 검증 한계와 연구윤리 고지를 강화 |

## 4. SCI 형식 연결

| Item | Draft |
|---|---|
| Title | A Multi-Metric Security Evaluation Framework for Neural Network Verification and XAI Stability |
| Research Question | How can AI security reports jointly represent robustness, explanation stability, fairness, verification cost, and reproducibility? |
| Method | Literature synthesis, threat modeling, synthetic toy experiment, reproducibility evidence |
| Contribution | A reporting framework that separates empirical robustness from certified robustness proxies and links XAI stability to AI security evaluation |
| Limitation | The current certified rate is a toy linear-bound proxy, not a formal certificate for large-scale DNNs |

## 5. 최종 주제 추천

가장 적합한 연결 주제는 "강건성·설명안정성·공정성·재현성을 함께 보고하는 AI 보안 평가 프레임워크"이다. W12의 문헌 비교와 toy 실험은 기말논문에서 보안 평가표와 재현성 절차를 설명하는 근거로 활용하기 좋다.

## 6. 반드시 남길 한계

- `certified_rate`는 toy logistic classifier의 선형 bound proxy이며 formal DNN verification certificate가 아니다.
- `adversarial_features()`는 실제 PGD/FGSM 공격 구현이 아니라 교육용 perturbation proxy다.
- P01~P05 DOI와 로컬 PDF에는 불일치가 있으므로 최종 원고에서 지정 논문처럼 단정 인용하지 않는다.
- public GitHub 저장소에 학술 PDF를 포함하기 전 저작권과 공개 범위를 사람이 확인해야 한다.
