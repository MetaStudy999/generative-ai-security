# W12 발표자 대본

## 1. 도입

오늘 발표는 신경망 검증, 정형방법, 대적방어, XAI, 강건성 trade-off를 하나로 묶어서 설명합니다. 핵심 질문은 모델이 테스트셋에서 잘 맞는다는 사실만으로 안전하다고 할 수 있는가입니다.

## 2. 문제 제기

Clean accuracy는 정상 조건의 평균 성능입니다. 하지만 보안 관점에서는 작은 입력 변화, 설명 조작, 검증 비용, 집단별 성능 차이까지 봐야 합니다. 그래서 W12는 성능 하나가 아니라 다중지표 평가표를 만드는 주차입니다.

## 3. 문헌 역할

P01은 신경망 검증에서 abstraction이 왜 필요한지 보여주고, P02는 대적공격과 방어 taxonomy를 제공합니다. P03은 XAI 설명 자체가 공격 대상이 될 수 있음을 보여줍니다. P04는 Lipschitz regularization과 강건성 보증을 연결하고, P05는 강건성·정확도·공정성의 삼각 trade-off를 정리합니다. 다만 로컬 PDF와 지정 논문 사이 불일치가 있어 최종 제출 전 공식 DOI와 원문 PDF 재확인이 필요합니다.

## 4. AI 원리

신경망 검증은 모델이 특정 입력 영역에서 명세를 만족하는지 확인하는 절차입니다. 경험적 평가는 테스트셋 평균 성능에 가깝고, 정형검증은 bound나 certificate처럼 보증 가능한 표현을 요구합니다. XAI는 설명을 제공하지만 설명이 불안정하면 검토 근거가 약해집니다.

## 5. 보안 이슈

대적 입력은 모델 예측을 바꾸는 integrity 문제입니다. Explanation manipulation은 사람이 보는 설명을 바꾸는 accountability 문제입니다. 검증 비용이 크면 검증이 생략될 수 있으므로 availability 문제도 생깁니다.

## 6. 실험 설명

실험은 실제 공격이 아니라 synthetic binary classification 기반 toy 평가입니다. `seed 42`로 toy logistic classifier를 학습하고, L-infinity epsilon 0.35 proxy로 perturbation 조건을 만들었습니다. 결과는 `outputs/run_log.md`에 남겼습니다.

## 7. 결과 해석

Clean model은 clean accuracy 0.818750이지만 robust accuracy는 0.543750입니다. Adversarial input 조건에서는 explanation stability와 certified rate가 더 낮아집니다. XAI stability check에서는 완화된 perturbation 조건에서 robust accuracy 0.696875와 explanation stability 0.976252를 보입니다. 기준 조건의 fairness gap은 0.039141, verification cost는 0.223524 ms입니다. 단, 이 값은 대규모 DNN 보증이 아니라 toy proxy입니다.

## 8. 기말논문 연결

기말논문에는 W12를 성능·강건성·설명안정성·공정성·재현성 통합 평가표로 연결할 수 있습니다. 특히 실행 로그와 보고서 수치를 일치시키는 절차가 연구윤리와 재현성 측면에서 중요합니다.

## 9. 마무리

W12의 결론은 정확도 중심 보고에서 보증 가능한 다중지표 보고로 넘어가야 한다는 것입니다.
