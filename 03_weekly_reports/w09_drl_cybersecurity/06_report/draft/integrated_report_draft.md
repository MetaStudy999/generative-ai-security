# W09 심층강화학습(DRL) & 사이버보안 적용·보상조작 통합보고서 초안

## 0. 메타정보

| 항목 | 내용 |
|---|---|
| 주차 | W09 |
| 주제 | 심층강화학습(DRL) & 사이버보안 적용·보상조작 |
| 작성일 | 2026-06-22 |
| 문서 상태 | 최종본 작성 전 초안 |
| 실험 상태 | synthetic toy cyber-defense 실험 실행 완료 |
| 실험 근거 | `04_experiment/outputs/run_log.md` |

## 1. 핵심 요약

W09는 DRL을 사이버 방어 자동화에 적용할 때 보상 설계와 보상조작이 정책 안전성을 어떻게 흔들 수 있는지 정리한다. tabular Q-learning toy 실험에서 manipulated reward 조건은 Average Reward 0.521167, Detection F1 0.617512, Safety Violation Rate 0.195000으로 기준 조건보다 악화되었다.

## 2. 구성

- AI 원리: MDP, Q-function, DQN, policy gradient, actor-critic, DRL verification
- 보안 이슈: DRL cyber defense, reward manipulation, reward hacking, state observation manipulation
- 문헌: DRL survey, autonomous driving safe RL, cyber-security DRL, RL cybersecurity survey, DRL verification survey
- 실험: synthetic state/action/reward 환경에서 normal/manipulated/robust reward 비교
- 기말논문 연결: DRL 기반 사이버 방어 에이전트의 보상조작 위협과 안전성 평가 프레임워크

## 3. 초안 점검

| 항목 | 상태 |
|---|---|
| 논문 5편 요약 | 완료 |
| DOI/URL 표 | 완료 / 확인 필요, P03/P04/P05 강의계획서 저자명 차이 최종 확인 필요 |
| AI 원리/보안 이슈 | 완료 |
| 실험 코드/결과 | 완료 |
| 제출용 보고서 | 완료 |
| 발표자료 | 완료 |
