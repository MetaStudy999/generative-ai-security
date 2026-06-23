# P02 Summary

## Deep Reinforcement Learning for Autonomous Driving: A Survey — B. Ravi Kiran et al., IEEE TITS, 2022

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W09 DRL & Cybersecurity |
| 논문명 | Deep Reinforcement Learning for Autonomous Driving: A Survey |
| 저자 | B. Ravi Kiran et al. |
| 출판 정보 | IEEE Transactions on Intelligent Transportation Systems, 23(6), pp. 4909–4926, 2022 |
| DOI | https://doi.org/10.1109/TITS.2021.3054625 |
| 검증 상태 | W09 `paper_list.md` 기준 공식 DOI 확인. arXiv v2와 출판판 차이 메모 유지 |

---

## 1. 한 문장 요약

이 논문은 자율주행에서 DRL을 **perception, planning, control, reward design, simulation, safety, sample efficiency** 관점에서 정리하며, W09에서 사이버 방어 에이전트도 안전 제약과 시뮬레이션-현실 간극을 고려해야 함을 설명하는 응용 배경 문헌이다.

---

## 2. 핵심 연구질문

| 번호 | 연구질문 |
|---|---|
| RQ1 | 자율주행 DRL은 state/action/reward를 어떻게 설계하는가? |
| RQ2 | Safety constraint와 reward shaping은 실제 환경에서 왜 중요한가? |
| RQ3 | Simulation-to-real gap은 사이버 방어 에이전트 평가와 어떻게 유사한가? |
| RQ4 | 방어 자동화에서 잘못된 action의 비용을 어떻게 평가해야 하는가? |

---

## 3. 핵심 수식

### 3.1 Constrained Return

$$
J(\pi)=\mathbb{E}_{\pi}\left[\sum_t \gamma^t r_t\right], \qquad C(\pi)\leq c_{max}
$$

| 기호 | 의미 |
|---|---|
| $J(\pi)$ | 정책의 기대 보상 |
| $C(\pi)$ | 안전 위반 또는 비용 |
| $c_{max}$ | 허용 가능한 최대 위험 |

**보안 해석:** 사이버 방어에서도 reward만 높이는 정책이 정상 트래픽 차단, 서비스 중단, 과잉 대응을 만들 수 있다. 제약 조건이 필요하다.

---

## 4. 위협모형·평가지표

| 항목 | 내용 |
|---|---|
| 보호 자산 | 안전 정책, 자동 대응 action, 운영 서비스, 정상 사용자 흐름 |
| 공격자 목표 | state observation 교란, 방어 action 오도, reward hacking 유도 |
| 대표 지표 | cumulative reward, safety violation rate, response latency, false blocking rate |
| 재현성 | simulator version, scenario seed, reward/cost function, failure case 기록 |

---

## 5. 기말논문 연결

P02는 DRL 보안 자동화에서 안전 제약과 시뮬레이션 기반 검증의 필요성을 설명한다. RAG/LLM 보안 대응 자동화도 임의 action을 직접 실행하기보다 human approval과 cost constraint를 둬야 한다.

---

## 6. 최종 판단

P02는 자율주행 응용 문헌이지만, 안전 제약 DRL과 simulation-based evaluation 원칙을 사이버 방어에 전이하는 데 유용하다.
