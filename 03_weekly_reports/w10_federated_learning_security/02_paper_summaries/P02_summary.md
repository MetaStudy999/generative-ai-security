# P02 Summary

## A survey on security and privacy of federated learning — Viraaji Mothukuri et al., Future Generation Computer Systems, 2021

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W10 Federated Learning Security |
| 논문명 | A survey on security and privacy of federated learning |
| 저자 | Viraaji Mothukuri et al. |
| 출판 정보 | Future Generation Computer Systems, 115, pp. 619–640, 2021 |
| DOI | https://doi.org/10.1016/j.future.2020.10.007 |
| 검증 상태 | W10 `paper_list.md` 기준 DOI 확인 |

---

## 1. 한 문장 요약

이 논문은 FL의 보안·프라이버시 위협을 **inference attack, poisoning, model update leakage, secure aggregation, differential privacy, access control, trust management** 관점에서 정리하는 W10의 핵심 보안 survey 문헌이다.

---

## 2. 핵심 연구질문

| 번호 | 연구질문 |
|---|---|
| RQ1 | FL은 데이터를 공유하지 않아도 어떤 privacy leakage가 발생하는가? |
| RQ2 | 악성 client는 update를 통해 global model을 어떻게 오염시킬 수 있는가? |
| RQ3 | Secure aggregation과 DP는 어떤 보호를 제공하고 어떤 trade-off를 만드는가? |
| RQ4 | FL 보안 평가는 utility, privacy, robustness, communication cost를 어떻게 함께 봐야 하는가? |

---

## 3. 핵심 수식

### 3.1 Update Leakage Risk

$$
Risk_{FL}=\alpha PoisonImpact+\beta LeakageRisk+\gamma ByzantineRate
$$

### 3.2 Privacy-Utility Trade-off

$$
UtilityDrop=Acc_{baseline}-Acc_{private}
$$

---

## 4. 위협모형·평가지표

| 항목 | 내용 |
|---|---|
| 보호 자산 | client data, gradient/update, client identity, global model |
| 공격자 목표 | membership inference, gradient leakage, model poisoning, backdoor |
| 방어 | secure aggregation, differential privacy, anomaly detection, robust aggregation |
| 지표 | clean accuracy, privacy leakage, ASR, utility drop, communication overhead |

---

## 5. 기말논문 연결

P02는 FL 보안·프라이버시의 직접 핵심 문헌이다. 기말논문에서는 분산 데이터 기여와 모델 업데이트를 감사 가능한 보안 자산으로 정의하는 근거로 사용한다.

---

## 6. 최종 판단

P02는 W10의 보안·프라이버시 기준 문헌이다. FL은 데이터가 중앙으로 모이지 않아도 update와 aggregation 단계에서 보안 위험이 남는다.
