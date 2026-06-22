# W09 제출용 보고서

## 표지

| 항목 | 내용 |
|---|---|
| 주차 | W09 |
| 보고서 제목 | 심층강화학습(DRL) & 사이버보안 적용·보상조작 |
| 과목 범위 | AI 보안 |
| 작성일 | 2026-06-22 |
| 문서 상태 | 제출용 통합본 |
| 관련 산출물 위치 | `03_weekly_reports/w09_drl_cybersecurity/` |
| 실험 근거 | `04_experiment/outputs/run_log.md` |

## 초록

본 보고서는 DRL의 MDP, Q-function, DQN, policy gradient, actor-critic, verification 개념을 정리하고, 이를 DRL 기반 사이버 방어 에이전트의 상태·행동·보상 설계 문제로 연결한다. 문헌 5편을 통해 DRL 원리, 안전중요 자동화, cyber-defense 적용, IDS/IPS 평가, DRL verification을 비교했다. 실습에서는 실제 네트워크나 공격 payload 없이 synthetic toy cyber-defense 환경에서 tabular Q-learning을 실행했다. Manipulated reward 조건은 Average Reward 0.521167, Detection F1 0.617512, Safety Violation Rate 0.195000으로 기준 조건보다 나빠졌으며, robust reward design은 Safety Violation Rate를 0.000000으로 낮췄다.

**키워드:** DRL, reinforcement learning, cyber defense, reward manipulation, reward hacking, safety violation, policy robustness

## 1. AI 원리 70%

강화학습은 agent가 state를 관측하고 action을 선택한 뒤 reward를 받아 policy를 개선하는 순차 의사결정이다. W09에서는 MDP와 Q-learning을 중심으로 상태·행동·보상 설계가 정책에 미치는 영향을 설명했다. DQN, policy gradient, actor-critic은 큰 상태공간과 복잡한 정책을 다루는 확장 방법이며, DRL verification은 높은 reward와 안전성을 분리해 보는 관점이다.

## 2. 보안 이슈 30%

| 관점 | 관련 위협 | W09 평가 연결 |
|---|---|---|
| Confidentiality | 보안 로그/상태 관측 노출 | 개인정보 미사용 |
| Integrity | reward manipulation, state poisoning | observed reward와 true reward 비교 |
| Availability | 정상 이벤트 과잉 격리 | Safety Violation Rate |
| Safety | 공격 이벤트 미대응 | Detection F1, violation rate |
| Accountability | 설명 불가능한 자동 대응 | config, seed, run log |

## 3. 문헌 요약

| ID | 문헌 | DOI/URL 상태 | 활용 |
|---|---|---|---|
| P01 | Arulkumaran et al., *A Brief Survey of Deep Reinforcement Learning* | DOI `10.1109/MSP.2017.2743240` | DRL 원리 |
| P02 | Kiran et al., *Deep Reinforcement Learning for Autonomous Driving* | DOI `10.1109/TITS.2021.3054625` | 안전중요 자동화 |
| P03 | Nguyen and Reddi, *Deep Reinforcement Learning for Cyber Security* | DOI `10.1109/TNNLS.2021.3121870` | cyber-defense 적용 |
| P04 | Adawadkar and Kulkarni, *Cyber-security and reinforcement learning* | DOI `10.1016/j.engappai.2022.105116` | IDS/IPS, IoT, IAM 평가 |
| P05 | Landers and Doryab, *Deep Reinforcement Learning Verification* | DOI `10.1145/3596444` | DRL verification |

## 4. Research Track

| 항목 | 내용 |
|---|---|
| 연구문제 | DRL 사이버 방어 에이전트의 보상조작은 방어 성능과 안전성에 어떤 영향을 미치는가 |
| 대상 시스템 | DRL 기반 사이버 방어 에이전트 |
| 보호 자산 | 상태 관측값, 보상함수, 정책, 보안 로그, 대응 action |
| 위협 | reward manipulation, state observation manipulation, unsafe automated response |
| 평가 지표 | Average Reward, Detection F1, Safety Violation Rate, Policy Robustness |
| 재현성 | seed 42, config, script, CSV/JSON/run log 보존 |
| 제외 범위 | 실제 시스템 침해, 실제 네트워크 공격, 개인정보, 무단 스캔, exploit 실행 |

## 5. 실습/실험 결과

| 조건 | Average Reward | Detection F1 | Safety Violation Rate | Policy Robustness | 해석 |
|---|---:|---:|---:|---:|---|
| Normal reward | 1.085250 | 0.840206 | 0.011667 | 0.838417 | 기준 조건 |
| Manipulated reward | 0.521167 | 0.617512 | 0.195000 | 0.325000 | 보상조작으로 true utility와 안전성 악화 |
| Robust reward design | 0.910833 | 0.780952 | 0.000000 | 0.709583 | 안전 위반 제거, 오탐 비용 증가 |

이 결과는 synthetic toy 실험의 평가 형식 검증용 수치다. 실제 IDS/IPS 제품, 실제 운영망, 실제 DRL neural policy 성능으로 일반화하지 않는다.

## 6. 발표자료 위치

| 파일 | 용도 |
|---|---|
| `09_presentation/presentation_report.md` | 발표용 보고서 |
| `09_presentation/presentation_slides.md` | 슬라이드 원본 |
| `09_presentation/presentation_slides.html` | 브라우저 발표용 슬라이드 |
| `09_presentation/speaker_notes.md` | 발표자 대본 |
| `09_presentation/qna.md` | 예상 질문과 답변 |
| `09_presentation/one_page_handout.md` | 1페이지 배포자료 |

## 7. 기말논문 연결

추천 주제는 “DRL 기반 사이버 방어 에이전트의 보상조작 위협과 안전성 평가 프레임워크”이다. W09의 기여 후보는 reward integrity 위협모형, Detection F1/Safety Violation/Policy Robustness 평가표, seed/config/output 기반 재현성 구조이다.

## 8. AI 활용 고지

Codex를 사용해 공통 지침 확인, 로컬 파일 점검, PDF 기반 서지 보정, synthetic toy 실험 코드 작성과 실행, 제출용 보고서 및 발표자료 작성을 수행했다. 정량값은 `04_experiment/outputs/run_log.md`, `metrics_summary.csv`, `results.json`과 일치하는 값만 사용했다. 상세 기록은 `05_ai_worklog/`에 있다.

## 9. 제출 전 점검표

| 점검 항목 | 상태 |
|---|---|
| 논문 요약 5편 | 완료 |
| 논문 비교표 | 완료 |
| AI 원리/보안 이슈 | 완료 |
| Research Track | 완료 |
| 실험 코드 | 완료 |
| 실험 결과 | 완료 |
| DOI/URL 검증표 | 완료 |
| AI 활용 고지 | 완료 |
| 발표자료 | 완료 |
