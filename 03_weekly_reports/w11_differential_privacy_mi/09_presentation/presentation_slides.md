# W11 차등프라이버시(DP) & 멤버십 추론 공격·방어

## 발표 핵심

DP 보장은 선언이 아니라 accounting, utility, MI risk, leakage, 재현성 로그로 검증해야 한다.

---

# 1. 왜 중요한가

- 학습 데이터 포함 여부 자체가 민감정보가 될 수 있다.
- DP를 적용했다고 해도 accountant와 평가 로그가 없으면 보장 해석이 어렵다.
- Accuracy만 보면 privacy leakage를 놓친다.

---

# 2. 발표 로드맵

1. AI 원리
2. 보안 이슈
3. 논문 5편의 역할
4. 위협모형과 평가방법
5. synthetic toy 실험
6. 기말논문 연결

---

# 3. AI 원리 70%

- Differential Privacy: 인접 데이터셋의 출력 분포 차이 제한
- DP-SGD: gradient clipping + noise injection + privacy accounting
- Privacy budget: epsilon/delta와 utility의 trade-off

---

# 4. 보안 이슈 30%

| 위협 | 공격자 가정 | 대표 지표 |
|---|---|---|
| Membership inference | confidence/loss 관찰 | MI Attack Accuracy |
| Privacy leakage | member/non-member 신호 차이 | Leakage Score |
| DP misuse | accountant 누락 | Reference/config check |

---

# 5. 논문 5편의 역할

| ID | 중심 역할 | 발표 활용 |
|---|---|---|
| P01 | DP misuse | reporting 책임 |
| P02 | DP-DL survey | auditing/evaluation |
| P03 | DP 적용 위치 | DL/FL 연결 |
| P04 | MI taxonomy | 위협모형 |
| P05 | MI defense | trade-off |

---

# 6. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | membership information, confidence score, output, log |
| 공격자 | 외부 질의자, 모델 사용자, 내부 평가자 |
| 공격 경로 | API output, confidence, evaluation log |
| 제외 범위 | 실제 개인정보, 실제 개인 대상 추론, 무단 API |

---

# 7. 평가 프로토콜

| 평가 항목 | 지표 | 기록 방법 |
|---|---|---|
| Utility | Accuracy, Utility Drop | CSV/JSON/log |
| Membership risk | MI Attack Accuracy | synthetic split |
| Leakage | Privacy Leakage Score | confidence gap |
| Reproducibility | seed, config, outputs | run log |

---

# 8. 실험 설계

- Synthetic binary classification
- Toy logistic regression
- Non-DP baseline vs DP-like noise low/medium/high
- `epsilon_proxy`는 정식 DP accountant 값이 아님

---

# 9. 결과

| 조건 | Accuracy | MI Acc. | Eps. proxy | Leakage |
|---|---:|---:|---:|---:|
| Non-DP | 0.956250 | 0.515625 | 해당 없음 | 0.014833 |
| Low | 0.956250 | 0.515625 | 8.000000 | 0.014494 |
| Medium | 0.962500 | 0.512500 | 3.000000 | 0.011769 |
| High | 0.950000 | 0.521875 | 1.000000 | 0.016482 |

---

# 10. 해석

- Medium noise에서 leakage proxy가 가장 낮았다.
- High noise는 utility drop이 생겼지만 MI risk가 단조롭게 낮아지지는 않았다.
- DP claim은 accountant와 반복 평가 없이는 확정할 수 없다.

---

# 11. 기말논문 연결

| 기말논문 장 | 연결 내용 |
|---|---|
| 관련연구 | DP misuse, DP-DL, MI survey |
| 위협모형 | membership information 보호 |
| 평가방법 | utility + MI risk + leakage + logs |
| 보안적 함의 | privacy claim accountability |

---

# 12. 결론

- DP는 구현 설정과 accounting까지 함께 보고해야 한다.
- MI 위험은 별도 보안 지표로 평가해야 한다.
- 수치는 `outputs/` 로그가 있을 때만 주장한다.
