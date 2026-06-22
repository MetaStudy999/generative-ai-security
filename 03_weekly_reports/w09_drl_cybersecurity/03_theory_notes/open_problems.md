# 한계와 오픈문제

## 1. 문헌 검증 한계

P01/P02는 로컬 PDF가 arXiv 버전을 포함하므로 최종 출판본과 세부 차이를 기말 제출 직전에 다시 대조한다. P03/P04/P05는 강의계획서 저자명과 DOI/PDF 저자명이 달라 동일 문헌 여부 또는 강의계획서 오기 여부를 확인해야 한다.

## 2. 방법론 한계

W09 실험은 tabular Q-learning toy environment이다. DRL의 neural policy, replay buffer, target network, actor-critic 안정성까지 검증한 것은 아니다. 따라서 수치는 “보상조작 효과를 설명하는 재현 가능한 예시”로만 해석한다.

## 3. 재현성 한계

현재 결과는 seed 42와 synthetic event generator에 의존한다. 다른 공격 비율, alert perturbation 비율, action cost를 쓰면 결과가 달라질 수 있다.

## 4. 기말 논문으로 남길 질문

| 번호 | 오픈문제 | 왜 어려운가 | 기말 논문 연결 가능성 |
|---:|---|---|---|
| 1 | 실제 운영 로그 없이 cyber-defense reward를 어떻게 설계할 것인가 | 개인정보·공격 재현 위험 때문에 공개 데이터가 제한적이다 | 높음 |
| 2 | reward manipulation과 일반 reward misspecification을 어떻게 구분할 것인가 | 공격과 설계 오류가 동일한 정책 실패로 나타날 수 있다 | 높음 |
| 3 | safety와 utility의 trade-off를 어떤 기준으로 설명할 것인가 | Robust reward는 안전 위반을 낮추지만 오탐 비용을 높일 수 있다 | 높음 |
| 4 | formal verification과 toy experiment를 어떻게 연결할 것인가 | 완전 검증은 확장성이 낮고 toy 실험은 일반화가 약하다 | 보통 |
