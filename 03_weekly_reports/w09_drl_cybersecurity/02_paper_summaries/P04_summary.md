# P04 Summary

## Cyber-security and reinforcement learning — A brief survey — Amrin Maria Khan Adawadkar, Nilima Kulkarni, Engineering Applications of Artificial Intelligence, 2022

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W09 DRL & Cybersecurity |
| 논문명 | Cyber-security and reinforcement learning — A brief survey |
| 저자 | Amrin Maria Khan Adawadkar, Nilima Kulkarni |
| 출판 정보 | Engineering Applications of Artificial Intelligence, 114, Article 105116, 2022 |
| DOI | https://doi.org/10.1016/j.engappai.2022.105116 |
| 검증 상태 | W09 `paper_list.md` 기준 DOI 확인. 강의계획서 저자명 표기 차이 메모 유지 |

---

## 1. 한 문장 요약

이 논문은 reinforcement learning을 사이버보안 문제에 적용하는 사례를 **intrusion response, adaptive defense, cyber-physical security, game-like attacker-defender interaction** 관점에서 짧게 정리하며, W09의 보안 응용 범위를 넓히는 survey 문헌이다.

---

## 2. 핵심 연구질문

| 번호 | 연구질문 |
|---|---|
| RQ1 | RL은 사이버 공격-방어 상호작용을 어떻게 모델링할 수 있는가? |
| RQ2 | Intrusion detection/response, access control, resource allocation에 RL을 적용할 때 어떤 장점과 위험이 있는가? |
| RQ3 | 방어 에이전트의 잘못된 action과 reward 설계 오류는 어떤 운영 위험을 만드는가? |

---

## 3. 핵심 수식

$$
\pi^*(s)=\arg\max_a Q^*(s,a)
$$

$$
Q^*(s,a)=\mathbb{E}\left[r+\gamma\max_{a'}Q^*(s',a')\mid s,a\right]
$$

**보안 해석:** 최적 정책은 reward 정의에 의존한다. reward가 실제 보안 목표를 반영하지 않으면 정책은 취약하거나 과잉 대응적일 수 있다.

---

## 4. 위협모형·평가지표

| 항목 | 내용 |
|---|---|
| 보호 자산 | 방어 정책, alert stream, 네트워크 서비스, 사용자 가용성 |
| 공격자 목표 | 방어 정책 예측, 상태 교란, 대응 비용 증가 |
| 지표 | response success, FPR, missed attack rate, cost, policy stability |
| 한계 | 실제 네트워크 방어 자동화는 simulation 검증과 human approval 필요 |

---

## 5. 기말논문 연결

P04는 RL-보안 응용의 폭을 보여주는 보조 문헌이다. 기말논문에서는 자동 대응이 항상 안전하지 않으므로 action approval, rollback, audit log가 필요하다는 논리로 연결한다.

---

## 6. 최종 판단

P04는 W09의 보안 응용 보조 문헌이다. P03과 함께 DRL cyber defense의 평가축을 구성한다.
