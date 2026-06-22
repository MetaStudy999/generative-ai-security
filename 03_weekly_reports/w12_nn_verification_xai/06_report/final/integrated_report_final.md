# W12 신경망 검증·정형방법 & 대적방어·XAI·강건성 트레이드오프 통합보고서

## 0. 메타정보

| 항목 | 내용 |
|---|---|
| 주차 | W12 |
| 주제 | 신경망 검증·정형방법 & 대적방어·XAI·강건성 트레이드오프 |
| AI 원리 | Neural network verification, abstraction, formal methods, robustness proof |
| 보안 이슈 | 대적방어, XAI 공격면, robustness-accuracy-fairness trade-off |
| 작성일 | 2026-06-22 |
| 문서 상태 | 최종본 |
| 실험 근거 | `04_experiment/outputs/run_log.md` |

## 1. 한 문장 요약

W12는 신경망 검증과 정형방법을 AI 원리로 이해하고, 대적 강건성·XAI 설명 안정성·정확도·공정성 사이의 trade-off를 보안 평가 프로토콜로 연결하는 주차이다.

## 2. AI 원리 70% 정리

신경망 검증은 특정 입력 영역에서 모델 출력이 명세를 만족하는지 확인하려는 절차다. 경험적 평가는 테스트셋에서 평균 성능을 측정하지만, 정형검증은 입력 perturbation 집합, reachability, abstraction, bound propagation처럼 명세 기반 보증을 다룬다. Abstraction은 복잡한 신경망 계산을 더 단순한 영역이나 제약으로 근사해 검증 가능하게 만드는 방법이며, Lipschitz regularization은 입력 변화가 출력 변화로 증폭되는 정도를 제한하려는 학습 관점이다.

XAI는 모델 판단을 feature attribution, saliency map, rule, concept 등으로 설명하려는 접근이다. 설명이 안정적이지 않으면 모델의 신뢰성 검토도 흔들린다. 따라서 W12의 AI 원리는 "모델이 맞았는가"에서 끝나지 않고 "작은 입력 변화에도 예측과 설명이 일관적인가", "보증 가능한 범위는 어디까지인가"로 확장된다.

## 3. 보안 이슈 30% 정리

보안 이슈는 대적 입력이 모델 예측을 바꾸는 integrity 문제, 설명 조작이 검토자를 오도하는 accountability 문제, 검증 비용이 커져 실제 운영 검토가 실패하는 availability 문제로 나뉜다. Certified robustness와 empirical robustness는 구분해야 한다. 전자는 명세와 bound에 의존하고, 후자는 제한된 공격/테스트 조건에서 관측된 성능이다. Robustness, accuracy, fairness가 동시에 좋아지지 않을 수 있으므로 보고서에는 단일 지표가 아니라 다중 지표 표가 필요하다.

## 4. 논문 5편 요약

| ID | 논문 | 저자 | 연도 | 로컬 PDF/검증 상태 | 활용 |
|---|---|---|---|---|---|
| P01 | A Review of Abstraction Methods Toward Verifying Neural Networks | Boudardara et al. | 2024 | `SUBSTITUTE` PDF, 원문 대조 필요 | abstraction 기반 verification 분류 |
| P02 | Adversarial Attacks and Defenses in Deep Learning | Sen Zhou et al. | 2022 | 로컬 PDF 파일명과 프롬프트 논문명 대조 필요 | 공격·방어 taxonomy |
| P03 | Adversarial machine learning attacks against explainable artificial intelligence: A review | G. Vadillo et al. | 2025 | `SUBSTITUTE` PDF, 원문 대조 필요 | explanation manipulation과 XAI 공격면 |
| P04 | Adversarial Robustness of Neural Networks from Lipschitz Regularization: A Survey | Inaki Pérez et al. | 2024 | `SUBSTITUTE` PDF, 원문 대조 필요 | Lipschitz 기반 강건성 |
| P05 | The Triangular Trade-off between Robustness, Accuracy, and Fairness | Chih-Hsiang Cheng et al. | 2024 | `SUBSTITUTE` PDF, 원문 대조 필요 | robustness-accuracy-fairness trade-off |

## 5. 논문 5편 비교

P01은 검증 가능성, P02는 공격과 방어, P03은 설명 시스템의 공격면, P04는 Lipschitz 관점의 강건성, P05는 성능·강건성·공정성 사이의 trade-off를 담당한다. 다섯 편을 함께 읽으면 W12의 핵심은 "보증 가능한 AI"가 단일 기술이 아니라 모델 성능, 설명, 검증 비용, 사회적 영향까지 포함하는 평가 문제라는 점으로 정리된다.

## 6. Research Track

### 6.1 연구문제

RQ1. 신경망 검증 기법은 대규모 딥러닝 모델에서 어떤 확장성 한계를 갖는가?

RQ2. XAI 기반 설명 결과는 입력 perturbation 또는 대적 조작에 의해 얼마나 쉽게 왜곡될 수 있는가?

RQ3. Robustness, accuracy, fairness 간 trade-off를 보안 평가에서 어떻게 통합 지표로 보고해야 하는가?

### 6.2 위협모형

| 항목 | 내용 |
|---|---|
| 대상 시스템 | 딥러닝 분류 모델, XAI 기반 설명 시스템, 신경망 검증 파이프라인 |
| 보호 자산 | 모델 예측, 강건성 보증, 설명 결과, 공정성 지표, 안전 판단 |
| 공격자 | 입력 조작자, 설명 조작자, 평가 회피자 |
| 공격자의 지식 | White-box, Gray-box, Black-box |
| 공격 경로 | 입력 데이터, 설명 모듈, 검증 설정, 평가 프로토콜 |
| 공격 성공 조건 | 예측 또는 설명이 왜곡되지만 방어자가 탐지하지 못함 |
| 제외 범위 | 실제 안전중요 시스템 공격, 실제 운영 모델 침해 |

### 6.3 평가방법

| 평가 항목 | 지표 | W12 toy 실험 연결 |
|---|---|---|
| Clean performance | Clean Accuracy | 0.818750 기준 모델 |
| Robust performance | Robust Accuracy | 0.543750 기준 perturbation |
| Certified robustness | Certified Rate | 0.543750 선형 bound proxy |
| Explanation stability | Cosine similarity | 0.927782 기준 모델 |
| Fairness impact | Group accuracy gap | 0.039141 기준 모델 |
| Verification cost | Runtime ms | 0.184215 ms 기준 모델 |
| Reproducibility | Seed/config/output | seed 42, outputs 보존 |

### 6.4 재현성

실험은 `04_experiment/src/run_experiment.py`와 `04_experiment/configs/config.yaml`로 재실행할 수 있다. 결과는 `outputs/metrics_summary.csv`, `outputs/results.json`, `outputs/run_log.md`에 저장했다. 문헌 DOI와 원문 세부 수치는 임의 생성하지 않고 `01_papers/doi_check.md`에서 확인 필요 상태로 관리한다.

### 6.5 한계와 오픈문제

toy logistic classifier의 certified rate는 대규모 DNN formal verification이 아니다. XAI stability도 단순 feature attribution 기반 cosine similarity이므로 실제 saliency map 공격을 포괄하지 않는다. 향후 과제는 검증 비용이 큰 모델에서 risk-based partial verification을 어떻게 설계할지, 그리고 robust accuracy 개선이 fairness gap을 키우는 상황을 어떻게 보고할지이다.

## 7. 실습 요약

| 조건 | Clean Accuracy | Robust Accuracy | Explanation Stability | Certified Rate | Fairness Gap |
|---|---:|---:|---:|---:|---:|
| Clean model | 0.818750 | 0.543750 | 0.927782 | 0.543750 | 0.039141 |
| Adversarial input | 0.818750 | 0.543750 | 0.862321 | 0.340625 | 0.039141 |
| Robust defense | 0.815625 | 0.543750 | 0.927152 | 0.543750 | 0.044823 |
| XAI stability check | 0.815625 | 0.696875 | 0.976252 | 0.696875 | 0.044823 |

이 수치는 synthetic toy 환경의 교육용 결과다. 실제 안전중요 시스템의 보증이나 운영 모델 취약성으로 일반화하지 않는다.

## 8. AI 활용 기록 요약

Codex를 사용해 W12 폴더 상태 점검, 공통 지침 확인, toy 실험 코드 작성, 실행 결과 요약, 제출용·발표용 문서 구조화를 수행했다. 정량값은 실행 산출물과 일치하는 값만 반영했다.

## 9. 토론 질문

1. Empirical robustness가 충분히 높을 때도 formal robustness가 필요한 이유는 무엇인가?
2. XAI 설명이 안정적이지 않은 모델을 안전하다고 말할 수 있는가?
3. Robustness 개선이 accuracy나 fairness를 낮출 때 어떤 기준으로 모델을 선택해야 하는가?
4. 검증 비용이 큰 모델에서 전체 검증 대신 위험기반 부분검증을 허용할 수 있는가?

## 10. 기말 논문 연결

W12는 기말 논문의 관련연구, 위협모형, 평가방법, 보안적 함의에 연결된다. 특히 "성능·보안성·설명안정성·공정성·재현성 다중지표 평가표"를 만드는 근거 주차로 활용할 수 있다.

## 11. 참고문헌 검증표

참고문헌 DOI/URL은 `01_papers/doi_check.md`에서 확인한다. `SUBSTITUTE`가 포함된 로컬 PDF는 프롬프트 지정 논문과 대체 문헌의 일치 여부를 최종 제출 전 확인해야 한다.

## 12. 자기 점검

| 항목 | 상태 |
|---|---|
| 논문 5편 요약 | 완료, 원문 세부 대조 필요 |
| 비교표 | 완료 |
| AI 원리 70% | 완료 |
| 보안 이슈 30% | 완료 |
| Research Track | 완료 |
| 실험 코드와 outputs | 완료 |
| 제출용 보고서 | 완료 |
| 발표자료 | 완료 |
| DOI 임의 생성 방지 | 확인 필요 상태 유지 |
| AI 활용 고지 | 완료 |
