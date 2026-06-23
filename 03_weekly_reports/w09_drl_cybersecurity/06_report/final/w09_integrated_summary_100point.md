# W09 100점형 통합 Summary

## DRL & Cybersecurity

## 0. 문서 목적

이 문서는 W09 개별 논문 summary 5개를 기말논문 작성용 연구 노트로 통합한 100점형 요약본이다. DRL 원리, 사이버보안 응용, 안전 제약, 검증 요구를 하나의 평가체계로 묶는다.

---

## 1. 한 문장 통합 요약

W09는 사이버 방어를 **state-action-reward 기반 순차 의사결정 문제**로 모델링하되, 자동 대응 정책은 cumulative reward뿐 아니라 detection rate, false action, response cost, safety violation, verification evidence를 함께 평가해야 함을 정리하는 주차다.

---

## 2. 문헌 5편 통합 매트릭스

| ID | 논문 | 핵심 역할 | 주요 지표 |
|---|---|---|---|
| P01 | DRL Brief Survey | DRL 기본 원리 | return, Q-value, policy objective |
| P02 | DRL Autonomous Driving | 안전 제약·simulation 평가 | constraint cost, safety violation |
| P03 | DRL for Cyber Security | 사이버보안 직접 응용 | detection rate, response cost |
| P04 | Cybersecurity and RL | RL 보안 응용 보조 survey | missed attack, false blocking |
| P05 | DRL Verification | policy 검증과 safety | violation rate, counterexample |

---

## 3. 핵심 수식 묶음

$$
G_t=\sum_{k=0}^{\infty}\gamma^k r_{t+k+1}
$$

$$
Q(s_t,a_t)\leftarrow Q(s_t,a_t)+\alpha\left[r_{t+1}+\gamma\max_{a'}Q(s_{t+1},a')-Q(s_t,a_t)\right]
$$

$$
r_t=\alpha\cdot Detection_t-\beta\cdot FalseAlarm_t-\lambda\cdot ResponseCost_t
$$

$$
ViolationRate=\frac{N_{unsafe\ actions}}{N_{episodes}}
$$

---

## 4. 통합 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | 네트워크 상태, IDS alert, 대응 정책, action log, 운영 서비스 |
| 공격자 목표 | state observation 교란, reward hacking, 방어 action 유도, 정책 우회 |
| 공격자 능력 | alert flooding, false signal, 환경 조작, 방어 정책 탐색 |
| 방어자 능력 | DRL policy, simulator, runtime monitor, human approval |
| 제외 범위 | 실제 네트워크 자동 차단 실험, 무단 공격, 악성코드 실행 |

---

## 5. 통합 평가 지표

| 평가축 | 대표 지표 | 해석 |
|---|---|---|
| Utility | cumulative reward | 정책 성능 |
| Detection | detection rate, missed attack rate | 공격 탐지 효과 |
| Cost | response cost, latency | 방어 비용 |
| Safety | violation rate, unsafe action count | 운영 안전성 |
| Robustness | adversarial state robustness | 상태 교란 저항성 |
| Reproducibility | seed, simulator, episode trace | 재현성과 감사 가능성 |

---

## 6. 기말논문 연결 3문장

1. W09에서 기말논문에 반영할 개념: AI 보안 자동대응은 단순 탐지 문제가 아니라 상태-행동-보상 기반 순차 의사결정 문제다.
2. 반영할 표·그림·실험: MDP 수식, cyber defense reward, safety property, violation rate, human approval workflow를 반영한다.
3. W14 연결: 운영 보안에서는 자동 action의 로그, 승인, rollback, safety verification이 MLOps 감사 대상으로 확장된다.

---

## 7. 최종 판단

W09는 자동화된 AI 보안 대응의 가능성과 위험을 동시에 보여준다. 실제 시스템에 직접 적용하기보다 synthetic/simulation 기반 평가와 human-in-the-loop 검증을 전제로 해야 한다.
