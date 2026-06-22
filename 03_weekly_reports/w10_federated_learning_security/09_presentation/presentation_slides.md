# W10 연합학습(FL) & FL 위협·방어·정책

---

## 1. 핵심 메시지

FL은 데이터를 중앙으로 모으지 않지만, update와 aggregation은 여전히 보안 평가 대상이다.

---

## 2. FL 원리

- Client: local data로 update 계산
- Server: update 수집과 global model 갱신
- Aggregation: FedAvg, coordinate median 등
- 핵심 trade-off: utility, privacy, robustness, communication cost

---

## 3. 위협모형

| 자산 | 위협 |
|---|---|
| local update | gradient leakage, membership inference |
| global model | poisoning, backdoor |
| aggregation result | malicious/byzantine client 영향 |
| training log | 재현성·책임성 근거 |

---

## 4. 논문 패킷 역할

P01은 aggregation taxonomy, P02/P03은 security/privacy taxonomy, P04는 privacy와 policy, P05는 backdoor와 ASR 평가를 담당한다.

---

## 5. Toy 실험 설계

- Synthetic binary classification
- 10 clients, client별 80 samples
- 25 FL rounds, seed 42
- 조건: Clean, poisoned 10%, poisoned 20%, robust aggregation 20%

---

## 6. 실험 결과

| 조건 | Accuracy | ASR |
|---|---:|---:|
| Clean FL | 0.960000 | 0.136076 |
| Poisoned FL 10% | 0.953333 | 0.297468 |
| Poisoned FL 20% | 0.950000 | 0.496835 |
| Robust aggregation 20% | 0.955000 | 0.237342 |

---

## 7. 해석

20% poisoned FedAvg는 clean accuracy를 크게 떨어뜨리지 않지만 ASR을 크게 올렸다.

Coordinate median은 ASR을 낮췄지만 완전히 제거하지는 못했다.

---

## 8. 기말논문 연결

W10는 utility, ASR, privacy leakage proxy, reproducibility를 함께 기록하는 AI 보안 평가표의 근거가 된다.

---

## 9. 결론

FL 보안 평가는 "데이터를 보내지 않는다"는 구조 설명을 넘어 update, aggregation, attack success, 로그 재현성을 함께 검토해야 한다.
