# W12 논문 5편 비교표

| 논문 | 연구문제 | 핵심 방법 | 데이터/실험 | AI 원리 기여 | 보안 위협 연결 | 평가 지표 | 한계 | 내 논문 활용 |
|---|---|---|---|---|---|---|---|---|
| P01 | 신경망 검증에서 abstraction method는 어떤 역할을 하는가 | abstraction, reachability, bound propagation, formal specification survey | 지정 논문 원문 확인 필요, 현재 로컬 PDF는 Meng et al. 2022 관련 보조 문헌 | empirical evaluation과 formal verification 차이 설명 | 검증되지 않은 robust claim, scalability failure | certified robustness, verification cost, specification satisfaction | 관련 논문 PDF 상태, 강의 표기 매체와 공식 DOI 메타데이터 충돌 | verification pipeline과 formal-bound 개념 배경 |
| P02 | Deep learning 대적공격과 방어는 어떻게 분류되는가 | adversarial attack/defense taxonomy | 지정 논문과 로컬 Ren et al. 2020 PDF 동일 여부 확인 필요 | adversarial example, perturbation budget, robust training 개념 | prediction integrity attack, adaptive attack | clean accuracy, robust accuracy, ASR, defense success | 저자 Sen/Shuai, subtitle, 권호/DOI 대조 필요 | 공격·방어 평가축의 보안 근거 |
| P03 | XAI 설명은 대적 조작에 얼마나 취약한가 | adversarial XAI survey, explanation manipulation taxonomy | 지정 논문 원문 확인 필요, 현재 로컬 PDF는 Baniecki/Biecek 관련 보조 문헌 | feature attribution, saliency, explanation stability 개념 | misleading explanation, accountability failure | explanation stability, attribution similarity, explanation robustness | 관련 논문 PDF 상태, 공식 published title과 강의 표기 차이 | XAI stability와 accountability 지표 |
| P04 | Lipschitz regularization은 adversarial robustness를 어떻게 설명하는가 | Lipschitz bound, regularization, robustness survey | 지정 논문 원문 확인 필요, 현재 로컬 PDF는 Finlay et al. 관련 보조 문헌 | Lipschitz constant, margin, certified radius 개념 | perturbation amplification, robustness overclaim | robust accuracy, Lipschitz bound, certified rate | 관련 논문 PDF 상태, Inaki Pérez 지정 DOI 미확인 | toy certified rate proxy의 이론 배경 |
| P05 | Robustness, accuracy, fairness는 어떤 trade-off를 갖는가 | triangular trade-off analysis | 지정 논문 원문 확인 필요, 현재 로컬 PDF는 Singh et al. 관련 보조 문헌 | multi-objective evaluation 관점 | robustness 개선이 fairness/accuracy에 미치는 영향 | clean accuracy, robust accuracy, fairness gap | 관련 논문 PDF 상태, Chih-Hsiang Cheng 지정 DOI 미확인 | multi-metric 보안 평가표의 근거 |

## 종합 비교

1. P01은 신경망 검증과 abstraction 기반 formal method 문헌 축이다.
2. P02는 adversarial attack/defense taxonomy 문헌 축이다.
3. P03은 adversarial XAI와 explanation manipulation 문헌 축이다.
4. P04는 Lipschitz regularization과 certified robustness 문헌 축이다.
5. P05는 robustness-accuracy-fairness trade-off 문헌 축이다.

W12의 핵심 연결부는 clean accuracy, robust accuracy, explanation stability, certified rate, fairness gap, verification cost를 함께 보고하는 것이다. `certified rate`는 현재 toy 선형 모델의 bound proxy이며 실제 DNN formal verification certificate가 아니다. 또한 관련 논문 PDF는 지정 논문과 구분하여 관리해야 하며, DOI/URL과 원문 PDF가 최종 확인되기 전까지 지정 논문 원문처럼 인용하지 않는다.
