# W12 발표용 보고서

## 1. 발표 메타정보

| 항목 | 내용 |
|---|---|
| 주차 | W12 |
| 주제 | 신경망 검증·정형방법 & 대적방어·XAI·강건성 트레이드오프 |
| 발표 시간 | 8-10분 |
| 핵심 메시지 | 안전한 AI 평가는 정확도 하나가 아니라 강건성, 설명 안정성, 공정성, 검증 비용, 재현성을 함께 보고해야 한다. |
| 실험 근거 | `../04_experiment/outputs/run_log.md` |
| 문서 상태 | 발표용 최종 초안. 최종 제출 확정 아님 |

## 2. 한 문장 요약과 발표 흐름

W12는 신경망 검증과 XAI를 "모델을 믿을 수 있는가"라는 하나의 질문으로 묶고, 이를 toy 실험의 다중지표 평가표로 보여준다.

발표 흐름은 문제 제기, 문헌 역할, AI 원리, 보안 이슈, toy 실험 결과, 기말논문 연결 순서로 구성한다.

## 3. 논문 5편의 발표 역할

| ID | 역할 |
|---|---|
| P01 | Abstraction 기반 신경망 검증의 배경. 로컬 PDF는 `SUBSTITUTE` |
| P02 | 대적공격과 방어의 taxonomy. DOI/원문 대조 필요 |
| P03 | XAI 설명 결과가 공격면이 될 수 있다는 근거. 로컬 PDF는 `SUBSTITUTE` |
| P04 | Lipschitz regularization과 robustness certificate 연결. 지정 DOI 확인 필요 |
| P05 | Robustness, accuracy, fairness trade-off 정리. 지정 DOI 확인 필요 |

## 4. AI 원리 70% 발표 설명

신경망 검증은 "테스트셋에서 잘 맞았다"보다 강한 질문을 던진다. 입력이 작은 범위에서 바뀌어도 모델 출력이 안전한가, 그 사실을 어떤 bound나 certificate로 말할 수 있는가가 핵심이다. XAI는 예측 이유를 설명하지만, 설명이 입력 변화에 쉽게 흔들리면 human review의 근거도 약해진다.

## 5. 보안 이슈 30% 발표 설명

대적 입력은 예측 무결성을 흔들고, explanation manipulation은 검토자 판단을 흔든다. 검증 비용이 커지면 실무에서는 검증 자체가 생략될 수 있다. 따라서 W12의 보안 이슈는 attack success 하나가 아니라 robust accuracy, explanation stability, certified rate, fairness gap, verification cost를 함께 보는 것이다.

## 6. 실습/실험 실행 상태와 결과 근거

| 조건 | Clean Accuracy | Robust Accuracy | Explanation Stability | Certified Rate | Fairness Gap | Cost ms |
|---|---:|---:|---:|---:|---:|---:|
| Clean model | 0.818750 | 0.543750 | 0.927782 | 0.543750 | 0.039141 | 0.223524 |
| Adversarial input | 0.818750 | 0.543750 | 0.862321 | 0.340625 | 0.039141 | 0.190324 |
| Robust defense | 0.815625 | 0.543750 | 0.927152 | 0.543750 | 0.044823 | 0.191790 |
| XAI stability check | 0.815625 | 0.696875 | 0.976252 | 0.696875 | 0.044823 | 0.193048 |

이 결과는 synthetic binary classification 기반 안전 toy 실험에서 얻은 교육용 수치다. Certified rate는 대규모 DNN 검증 결과가 아니라 toy 선형 모델의 bound proxy다.

## 7. 기말논문 연결 지점

W12는 기말논문의 평가 프레임워크 장에 직접 연결된다. 기여 후보는 "성능·강건성·설명안정성·공정성·재현성 통합 평가표"와 "실험 수치와 실행 로그를 분리하지 않는 보고 절차"이다.

## 8. 예상 질문과 답변

| 질문 | 답변 |
|---|---|
| 왜 clean accuracy만으로 부족한가? | perturbation 조건에서 robust accuracy가 낮아질 수 있기 때문에 안전성 판단에는 별도 지표가 필요하다. |
| certified rate를 그대로 보증으로 봐도 되는가? | 아니다. 본 실습은 선형 모델 bound proxy이며 실제 DNN formal verification과 구분해야 한다. |
| XAI stability가 높으면 모델이 안전한가? | 설명 안정성은 필요한 조건 중 하나일 뿐이며 예측 강건성, 공정성, 검증 비용과 함께 봐야 한다. |

## 9. 제출 전 주의

P01, P03, P04, P05는 로컬 PDF가 지정 논문과 다르거나 `SUBSTITUTE` 상태다. P02도 강의 표기와 공식 후보 DOI 사이 차이가 있어 최종 제출 전 공식 출판 페이지와 원문 PDF를 사람이 재확인해야 한다. 공개 저장소에 학술 PDF를 포함하기 전 저작권과 공개 범위를 별도로 점검한다.
