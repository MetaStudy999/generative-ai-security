# P05 Summary

## Deep Reinforcement Learning Verification: A Survey — Matthew Landers, Afsaneh Doryab, ACM Computing Surveys, 2023

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W09 DRL & Cybersecurity |
| 논문명 | Deep Reinforcement Learning Verification: A Survey |
| 저자 | Matthew Landers, Afsaneh Doryab |
| 출판 정보 | ACM Computing Surveys, 55(14s), Article 330, pp. 1–31, 2023 |
| DOI | https://doi.org/10.1145/3596444 |
| 검증 상태 | W09 `paper_list.md` 기준 DOI 확인. 강의계획서 `H. Yan et al.` 동일성 확인 메모 유지 |

---

## 1. 한 문장 요약

이 논문은 DRL verification을 **policy verification, reachability, safety constraints, adversarial states, formal methods, testing, runtime monitoring** 관점에서 정리하며, W09에서 자동 방어 에이전트를 실제 운영 전 검증해야 하는 근거를 제공한다.

---

## 2. 핵심 연구질문

| 번호 | 연구질문 |
|---|---|
| RQ1 | DRL policy는 어떤 안전 명세와 제약 조건으로 검증할 수 있는가? |
| RQ2 | Testing, formal verification, runtime monitoring은 각각 어떤 장단점이 있는가? |
| RQ3 | 사이버 방어 에이전트의 action safety를 검증하지 않으면 어떤 위험이 생기는가? |
| RQ4 | W09 toy simulation 결과를 실제 방어 정책 보증으로 과장하지 않으려면 어떤 한계가 필요한가? |

---

## 3. 핵심 수식

### 3.1 Safety Property

$$
\forall s\in S_{safe}, \quad \pi(s)\notin A_{unsafe}
$$

### 3.2 Violation Rate

$$
ViolationRate=\frac{N_{unsafe\ actions}}{N_{episodes}}
$$

**보안 해석:** DRL 방어 정책은 reward가 높아도 위험 action을 선택하면 운영에 투입할 수 없다. 안전성은 별도 명세로 검증해야 한다.

---

## 4. 위협모형·평가지표

| 항목 | 내용 |
|---|---|
| 보호 자산 | DRL policy, 안전 제약, action space, 운영 서비스 |
| 공격자 목표 | policy가 unsafe action을 선택하도록 state 교란 |
| 지표 | violation rate, policy robustness, coverage, runtime alarm, false safe rate |
| 재현성 | safety specification, environment seed, counterexample trace 기록 |

---

## 5. 기말논문 연결

P05는 W09 자동 대응의 검증 근거다. RAG/LLM 보안 자동화에서도 차단·삭제·신고·도구 실행 같은 action은 안전 명세와 승인 절차가 필요하다.

---

## 6. 최종 판단

P05는 W09의 검증 핵심 문헌이다. DRL 기반 보안 대응은 성능보다 먼저 safety property와 violation rate를 관리해야 한다.
