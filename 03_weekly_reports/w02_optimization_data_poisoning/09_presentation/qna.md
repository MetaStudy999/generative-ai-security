# W02 예상 Q&A

## Q1. 왜 최적화 원리를 먼저 설명해야 하나?

Poisoning은 학습 데이터와 라벨을 조작해 손실함수와 gradient 추정을 바꾸는 공격이다. 최적화 원리를 이해해야 데이터 오염이 모델 전체에 영향을 주는 이유를 설명할 수 있다.

## Q2. Label-flipping과 backdoor는 무엇이 다른가?

Label-flipping은 라벨을 바꾸어 전체 성능이나 특정 클래스 성능을 저하시킬 수 있다. Backdoor는 정상 입력에서는 성능을 유지하면서 trigger가 있는 입력에서만 공격자 목표로 오분류되도록 만든다.

## Q3. Clean accuracy가 높으면 안전한 모델 아닌가?

아니다. Backdoor 모델은 정상 테스트셋에서는 높은 clean accuracy를 보일 수 있다. 따라서 trigger 조건의 ASR을 별도로 봐야 한다.

## Q4. 왜 실험 결과를 아직 숫자로 채우지 않았나?

호스트 Python에 `scikit-learn`이나 uv를 설치하지 않고 Docker에서 실행했다. 연구윤리상 실행하지 않은 수치를 임의로 적지 않고, 생성된 `outputs/run_log.md`를 기준으로 확정했다.

## Q5. 이 실습이 실제 공격을 의미하나?

아니다. 공개 digits 데이터셋에서 수행하는 교육용 toy evaluation이다. 실제 서비스, 개인정보, 무단 API, 운영 시스템 공격은 포함하지 않는다.

## Q6. 기말논문으로 가장 좋은 연결은 무엇인가?

“학습 데이터 오염과 backdoor 평가를 위한 다중지표 프레임워크”가 가장 자연스럽다. clean accuracy, ASR, stealthiness, detection rate, cost, reproducibility를 한 평가표로 통합할 수 있다.

<!-- formula-visual-qna:start -->
## 수식·그래프·그림 보강 Q&A

### Q. 그래프 수치는 어디에서 온 것인가?

A. `04_experiment/outputs/metrics_summary.csv`의 기존 수치만 사용했다. CSV에 없는 값, 실행하지 않은 실험, 외부 논문 실험 수치는 추가하지 않았다.

### Q. 이 수식은 해당 논문의 원문 수식인가?

A. 발표 보강용 수식은 표준 정의식 또는 검증 가능한 평가식이다. 논문별 원문 절·쪽·그림 번호가 필요한 경우 최종 제출 전 사람 검토로 확인한다.

### Q. 다이어그램은 실험 결과인가?

A. 아니다. `training-data poisoning evaluation flow` 다이어그램은 AI-assisted conceptual diagram이며 threat model과 pipeline 설명을 위한 보조 그림이다.

### Q. 보안적으로 가장 조심해야 할 해석은 무엇인가?

A. toy backdoor는 공개 toy 데이터 기반 안전 실습이며 실제 시스템 악용 절차로 일반화하지 않는다. 또한 모든 실습은 공개 데이터, synthetic/toy 데이터, 로컬 모의실험 범위로만 해석한다.
<!-- formula-visual-qna:end -->
