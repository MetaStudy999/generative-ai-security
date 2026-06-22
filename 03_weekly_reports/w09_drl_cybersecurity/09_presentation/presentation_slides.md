# W09 DRL & Cybersecurity

## 1. 핵심 메시지

DRL cyber-defense에서 reward가 흔들리면 높은 점수 뒤에 안전하지 않은 정책이 숨어 있을 수 있다.

---

## 2. 발표 질문

- DRL 에이전트는 무엇을 보고, 무엇을 선택하고, 무엇을 보상으로 받는가
- reward manipulation은 정책을 어떻게 왜곡하는가
- 안전한 자동 대응은 어떤 지표로 평가할 수 있는가

---

## 3. AI 원리 70%

| 개념 | 역할 |
|---|---|
| State | alert, 자산 중요도, 취약 여부 |
| Action | monitor, isolate, patch, escalate |
| Reward | 탐지 성공, 운영 비용, 안전 위반 |
| Policy | 상태별 대응 전략 |

---

## 4. 문헌의 역할

P01은 DRL 원리, P02는 안전중요 자동화, P03/P04는 cyber-defense 적용, P05는 DRL verification을 담당한다. P05는 강의계획서 저자명과 현재 PDF 저자명이 달라 확인 필요다.

---

## 5. 위협모형

```text
State observation -> Policy decision -> Automated response
          ^                 ^
          |                 |
   state manipulation   reward manipulation
```

보호 자산은 상태 관측값, 보상함수, 정책, 로그, 대응 action이다.

---

## 6. 실험 설계

- Synthetic toy cyber-defense state
- Tabular Q-learning
- Seed 42
- 조건: Normal reward, Manipulated reward, Robust reward design
- 지표: Average Reward, Detection F1, Safety Violation Rate, Policy Robustness

---

## 7. 실험 결과

| 조건 | Avg Reward | F1 | Safety Violation | Robustness |
|---|---:|---:|---:|---:|
| Normal | 1.085250 | 0.840206 | 0.011667 | 0.838417 |
| Manipulated | 0.521167 | 0.617512 | 0.195000 | 0.325000 |
| Robust | 0.910833 | 0.780952 | 0.000000 | 0.709583 |

---

## 8. 해석

- Manipulated reward는 observed reward와 true security objective를 분리시킨다.
- Robust reward는 safety violation을 0으로 낮췄지만 false positive 비용을 만든다.
- 따라서 F1 하나만으로 자동 대응 정책을 평가하기 어렵다.
- 이 수치는 toy protocol 결과이며 실제 IDS/IPS 성능이 아니다.

---

## 9. 기말논문 연결

DRL 기반 사이버 방어 에이전트의 보상조작 위협과 안전성 평가 프레임워크.

---

## 10. 결론

- Reward integrity를 보호해야 한다.
- Detection F1과 Safety Violation Rate를 함께 봐야 한다.
- 수치는 실행 로그와 CSV/JSON에 있을 때만 주장한다.
