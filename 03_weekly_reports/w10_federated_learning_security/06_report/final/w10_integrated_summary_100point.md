# W10 100점형 통합 Summary

## Federated Learning Security

## 0. 문서 목적

이 문서는 W10 개별 논문 summary 5개를 기말논문 작성용 연구 노트로 통합한 100점형 요약본이다. Federated Learning의 aggregation, privacy, threats, backdoor, governance를 하나의 보안 평가체계로 묶는다.

---

## 1. 한 문장 통합 요약

W10은 FL을 **client update, aggregation, non-IID data, privacy leakage, poisoning, backdoor, secure aggregation, differential privacy, policy/audit**로 구성된 분산학습 보안 문제로 보고, clean accuracy뿐 아니라 ASR, leakage, utility drop, malicious client rate, update provenance를 함께 평가해야 함을 정리하는 주차다.

---

## 2. 문헌 5편 통합 매트릭스

| ID | 논문 | 핵심 역할 | 주요 지표 |
|---|---|---|---|
| P01 | FL Aggregation Survey | FL 기본 구조와 aggregation taxonomy | FedAvg, drift, communication cost |
| P02 | FL Security/Privacy Survey | 보안·프라이버시 위협 | leakage, utility drop |
| P03 | FL Threats Survey | 공격·방어 taxonomy | Byzantine rate, robust aggregation |
| P04 | Federation Strikes Back | privacy attacks·policy landscape | MI risk, privacy budget, compliance |
| P05 | FL Backdoor Survey | FL backdoor 공격·방어 | ASR, malicious client rate |

---

## 3. 핵심 수식 묶음

$$
w_{t+1}=\sum_{k=1}^{K}\frac{n_k}{n}w_{t+1}^{(k)}
$$

$$
ByzantineRate=\frac{K_{malicious}}{K_{total}}
$$

$$
ASR=\frac{1}{N}\sum_{i=1}^{N}\mathbf{1}[f_{w}(T(x_i))=y_t]
$$

$$
PrivacyRisk=w_1MI+w_2GI+w_3PI-w_4DefenseCoverage
$$

---

## 4. 통합 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | local data, client update, gradient, global model, aggregation log, client identity |
| 공격자 목표 | model poisoning, backdoor, gradient leakage, membership inference, property inference |
| 공격자 능력 | malicious client, local poisoning, update scaling, model replacement, repeated participation |
| 방어자 능력 | robust aggregation, secure aggregation, DP, update clipping, anomaly detection, client reputation |
| 제외 범위 | 실제 FL 시스템 공격, 개인정보 데이터 사용, 무단 client 참여 실험 |

---

## 5. 통합 평가 지표

| 평가축 | 대표 지표 | 해석 |
|---|---|---|
| Utility | clean accuracy, F1 | 정상 성능 |
| Robustness | ASR, accuracy drop | poisoning/backdoor 영향 |
| Privacy | MI advantage, gradient leakage, privacy budget | 개인정보 보호 |
| Aggregation Safety | malicious client rate, update norm, detection rate | 악성 update 대응 |
| Fairness | client-wise performance | non-IID 영향 |
| Cost | communication rounds, bandwidth | 운영 가능성 |
| Auditability | client id, round log, aggregation config | 사후 검증 가능성 |

---

## 6. 기말논문 연결 3문장

1. W10에서 기말논문에 반영할 개념: FL 보안은 데이터를 중앙에 모으지 않는다는 장점만으로 충분하지 않고, update·aggregation·client provenance가 새로운 공격면이 된다.
2. 반영할 표·그림·실험: FedAvg 수식, malicious client rate, FL backdoor ASR, privacy risk score, aggregation audit table을 반영한다.
3. W14 연결: FL의 client update와 aggregation log는 MLOps 공급망 감사와 유사하므로 model/data contribution provenance로 확장한다.

---

## 7. 최종 판단

W10은 분산 AI 학습과 협업형 데이터 기여 환경의 보안 평가 기준을 제공한다. RAG/LLM 환경에서도 문서·adapter·client update 기여자 추적과 승인 로그가 필요하다는 논리로 확장 가능하다.
