# W12 예상 질문과 답변

## Q1. Clean accuracy가 높으면 robust accuracy도 높다고 볼 수 있나요?

아닙니다. W12 toy 실험에서도 clean model의 clean accuracy는 0.818750이지만 robust accuracy는 0.543750으로 낮아졌습니다. 정상 조건 성능과 perturbation 조건 성능은 분리해서 보고해야 합니다.

## Q2. Certified rate를 formal verification 결과로 말해도 되나요?

본 실습에서는 그렇게 말하면 안 됩니다. Certified rate는 synthetic binary classification 기반 toy logistic classifier에서 계산한 L-infinity bound proxy입니다. 실제 대규모 DNN의 formal verification은 별도 verifier, 명세, bound 방법, 검증 로그가 필요합니다.

## Q3. XAI stability가 높으면 설명을 신뢰해도 되나요?

높은 XAI stability는 긍정적인 신호지만 충분조건은 아닙니다. 설명 안정성은 예측 강건성, 공정성 영향, verification cost, 재현성 로그와 함께 봐야 합니다.

## Q4. Robust defense가 robust accuracy를 크게 개선하지 못한 이유는 무엇인가요?

본 실습의 방어는 단순한 대적 증강과 regularization proxy입니다. 강력한 adversarial training이나 verifier 기반 방어가 아니므로 개선 폭이 제한될 수 있습니다. 이 한계 자체가 toy 실험의 중요한 해석 포인트입니다.

## Q5. 이 실험을 실제 안전중요 시스템 평가로 확장할 수 있나요?

직접 확장할 수는 없습니다. 실제 시스템에서는 데이터 특성, 모델 구조, 위협모형, 검증 명세, 책임 소재가 모두 달라지므로 별도 승인된 평가 환경과 엄격한 안전 절차가 필요합니다.

## Q6. 참고문헌과 PDF는 그대로 제출해도 되나요?

아직 그대로 확정하면 안 됩니다. P01, P03, P04, P05는 로컬 PDF가 지정 논문과 다르거나 `SUBSTITUTE` 상태이고, P02도 원문 대조가 필요합니다. 공개 저장소에 학술 PDF를 포함하기 전 저작권과 공개 범위도 확인해야 합니다.

<!-- formula-visual-qna:start -->
## 수식·그래프·그림 보강 Q&A

### Q. 그래프 수치는 어디에서 온 것인가?

A. `04_experiment/outputs/metrics_summary.csv`의 기존 수치만 사용했다. CSV에 없는 값, 실행하지 않은 실험, 외부 논문 실험 수치는 추가하지 않았다.

### Q. 이 수식은 해당 논문의 원문 수식인가?

A. 발표 보강용 수식은 표준 정의식 또는 검증 가능한 평가식이다. 논문별 원문 절·쪽·그림 번호가 필요한 경우 최종 제출 전 사람 검토로 확인한다.

### Q. 다이어그램은 실험 결과인가?

A. 아니다. `verification-XAI robustness flow` 다이어그램은 AI-assisted conceptual diagram이며 threat model과 pipeline 설명을 위한 보조 그림이다.

### Q. 보안적으로 가장 조심해야 할 해석은 무엇인가?

A. `certified_rate`는 toy proxy 또는 제한 실험인지 formal verification인지 최종 원문 확인이 필요하다. 또한 모든 실습은 공개 데이터, synthetic/toy 데이터, 로컬 모의실험 범위로만 해석한다.
<!-- formula-visual-qna:end -->
