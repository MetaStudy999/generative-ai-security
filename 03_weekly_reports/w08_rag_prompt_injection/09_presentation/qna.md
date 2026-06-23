# 예상 질문과 답변

## Q1. 왜 실제 LLM이나 상용 API로 평가하지 않았나요?

이번 주차는 안전한 평가 프로토콜과 재현성 기록 구조를 완성하는 것이 목적입니다. 실제 공격 payload, live API, 실제 개인정보 없이도 ASR, source verification, tool misuse rate를 기록하는 구조를 검증할 수 있습니다.

## Q2. Source filter와 human approval 중 무엇이 더 중요한가요?

역할이 다릅니다. Source filter는 오염 문서가 context에 들어오는 것을 줄여 ASR을 0.575000에서 0.050000으로 낮췄습니다. Human approval은 고위험 action을 사람이 막아 tool misuse rate를 0.000000으로 낮췄지만 answer rate도 낮아졌습니다.

## Q3. GraphRAG에서는 무엇이 더 위험해지나요?

문서 본문뿐 아니라 node, edge, path, subgraph가 근거가 됩니다. 따라서 오염된 edge나 위조된 관계도 답변 근거로 들어올 수 있어 graph provenance가 필요합니다.

## Q4. P05 의료 논문은 왜 포함하나요?

Prompt injection이 단순한 답변 품질 문제가 아니라 safety-critical domain에서 위험한 권고와 책임 문제로 이어질 수 있음을 보여주기 위해 포함합니다.

## Q5. 이 실험 수치를 실제 시스템에 적용할 수 있나요?

아니요. W08 수치는 synthetic toy evaluator 결과입니다. 실제 시스템 적용 전에는 공개 benchmark, 복수 모델, 복수 seed, 사람 평가가 필요합니다.

<!-- formula-visual-qna:start -->
## 수식·그래프·그림 보강 Q&A

### Q. 그래프 수치는 어디에서 온 것인가?

A. `04_experiment/outputs/metrics_summary.csv`의 기존 수치만 사용했다. CSV에 없는 값, 실행하지 않은 실험, 외부 논문 실험 수치는 추가하지 않았다.

### Q. 이 수식은 해당 논문의 원문 수식인가?

A. 발표 보강용 수식은 표준 정의식 또는 검증 가능한 평가식이다. 논문별 원문 절·쪽·그림 번호가 필요한 경우 최종 제출 전 사람 검토로 확인한다.

### Q. 다이어그램은 실험 결과인가?

A. 아니다. `RAG pipeline threat model` 다이어그램은 AI-assisted conceptual diagram이며 threat model과 pipeline 설명을 위한 보조 그림이다.

### Q. 보안적으로 가장 조심해야 할 해석은 무엇인가?

A. prompt injection은 방어 평가 관점으로만 설명하고 실제 우회 절차는 제공하지 않는다. 또한 모든 실습은 공개 데이터, synthetic/toy 데이터, 로컬 모의실험 범위로만 해석한다.
<!-- formula-visual-qna:end -->
