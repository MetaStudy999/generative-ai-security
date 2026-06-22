# 핵심 용어

| 용어 | 정의 | W15 활용 |
|---|---|---|
| Evaluation | 모델 또는 시스템의 능력과 위험을 정해진 기준으로 측정하는 과정 | LLM/RAG 보안 평가 항목 설계 |
| Benchmark | 성능과 안전성을 비교하기 위해 쓰는 표준 데이터·과제 | contamination 점검 대상 |
| Benchmark contamination | 평가 데이터가 학습·튜닝·프롬프트 설계에 노출되는 현상 | 평가 무결성 위협 |
| Hidden test leakage | 비공개 평가셋의 정답·분포·패턴이 간접 노출되는 현상 | confidentiality/integrity 위협 |
| Reproducibility | 같은 조건에서 결과와 결론을 다시 검토할 수 있는 성질 | Docker/config/seed/log 보존 |
| Assurance evidence | 안전성 또는 신뢰성 주장을 뒷받침하는 검증 가능한 근거 | outputs와 제출 체크리스트 |
| XAI | 모델의 판단 근거를 사람이 이해할 수 있게 설명하는 연구 분야 | 설명 신뢰성과 공격면 분석 |
| Feature attribution | feature/token/pixel별 기여도를 표시하는 설명 방식 | 민감 feature 노출 점검 |
| Concept-based XAI | 사람이 이해 가능한 concept를 설명 단위로 사용하는 XAI | human review와 stability 평가 |
| Fidelity | 설명이 실제 모델 동작을 얼마나 잘 반영하는지 | explanation reliability |
| Stability | 작은 입력 변화에 설명이 얼마나 일관적인지 | explanation manipulation 탐지 |
| AI disclosure | AI 도구 사용 목적, 반영 위치, 검증 방법을 밝히는 고지 | 연구윤리와 책임성 |
| Reference verification | 제목, 저자, DOI/URL, 출판사, 로컬 PDF 일치 여부 확인 | 허위 인용 방지 |
