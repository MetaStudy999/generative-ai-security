# P03 Summary

## Deep Reinforcement Learning for Cyber Security — Thanh Thi Nguyen, Vijay Janapa Reddi, IEEE TNNLS, 2023

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W09 DRL & Cybersecurity |
| 논문명 | Deep Reinforcement Learning for Cyber Security |
| 저자 | Thanh Thi Nguyen, Vijay Janapa Reddi |
| 출판 정보 | IEEE TNNLS, 34(8), pp. 3779–3795, 2023 |
| DOI | https://doi.org/10.1109/TNNLS.2021.3121870 |
| 검증 상태 | W09 `paper_list.md` 기준 DOI 확인. 강의계획서 저자 표기 차이 메모 유지 |

---

## 1. 한 문장 요약

이 논문은 DRL을 사이버보안에 적용하는 연구를 **intrusion detection, malware analysis, cyber-physical defense, moving target defense, resource allocation, autonomous response** 관점에서 정리하고, W09의 핵심 보안 응용 문헌으로 사용된다.

---

## 2. 핵심 연구질문

| 번호 | 연구질문 |
|---|---|
| RQ1 | 사이버보안 문제는 어떤 state/action/reward 구조로 DRL에 매핑되는가? |
| RQ2 | 자동 방어 정책은 탐지율·오탐·대응 비용을 어떻게 함께 고려해야 하는가? |
| RQ3 | 공격자가 환경을 조작할 때 DRL policy는 어떤 취약성을 갖는가? |
| RQ4 | 안전한 DRL 사이버 실험은 어떤 toy/simulation 범위로 제한해야 하는가? |

---

## 3. 핵심 수식

### 3.1 Cyber Defense MDP

$$
\mathcal{M}=(\mathcal{S},\mathcal{A},P,R,\gamma)
$$

### 3.2 방어 보상 예시

$$
r_t=\alpha\cdot Detection_t-\beta\cdot FalseAlarm_t-\lambda\cdot ResponseCost_t
$$

**보안 해석:** 보상 함수는 방어자의 가치 판단을 코드화한다. 탐지만 높이고 비용을 무시하면 과잉 대응 정책이 생길 수 있다.

---

## 4. 위협모형·평가지표

| 항목 | 내용 |
|---|---|
| 보호 자산 | 네트워크 상태, IDS alert, 대응 정책, 로그, 서비스 가용성 |
| 공격자 목표 | 탐지 회피, 방어 action 유도, 상태 관측 오염, reward 조작 |
| 대표 지표 | detection rate, FPR, cumulative reward, response cost, policy robustness |
| 재현성 | simulator, state/action definition, reward function, episode trace 기록 |

---

## 5. 기말논문 연결

P03은 W09의 직접 보안 핵심 문헌이다. 기말논문에서는 AI 보안 대응을 단순 분류가 아니라 순차 의사결정·자동 대응·감사 가능한 policy evaluation 문제로 확장하는 근거로 사용한다.

---

## 6. 최종 판단

P03은 W09의 중심 문헌이다. DRL 기반 사이버 방어는 실제 시스템 직접 적용보다 simulation과 human-in-the-loop 평가로 제한하는 것이 안전하다.
