# P03 Summary

## Survey on federated learning threats: Concepts, taxonomy on attacks and defences, experimental study and challenges — Nuria Rodriguez-Barroso et al., Information Fusion, 2023

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W10 Federated Learning Security |
| 논문명 | Survey on federated learning threats: Concepts, taxonomy on attacks and defences, experimental study and challenges |
| 저자 | Nuria Rodriguez-Barroso et al. |
| 출판 정보 | Information Fusion, 90, pp. 148–173, 2023 |
| DOI | https://doi.org/10.1016/j.inffus.2022.09.011 |
| 검증 상태 | W10 `paper_list.md` 기준 DOI 및 arXiv 확인 |

---

## 1. 한 문장 요약

이 논문은 FL 위협을 **data poisoning, model poisoning, Byzantine attack, inference attack, backdoor, robust aggregation, defense taxonomy, experimental challenges** 관점에서 정리하고, W10의 공격·방어 평가 프로토콜 중심 문헌으로 사용된다.

---

## 2. 핵심 연구질문

| 번호 | 연구질문 |
|---|---|
| RQ1 | FL 공격은 client-side, server-side, communication-side에서 어떻게 분류되는가? |
| RQ2 | poisoning과 inference attack은 어떤 보호 자산을 노리는가? |
| RQ3 | robust aggregation은 악성 update를 어떻게 완화할 수 있는가? |
| RQ4 | non-IID 데이터와 client sampling은 방어 평가를 어떻게 어렵게 만드는가? |

---

## 3. 핵심 수식

### 3.1 Byzantine Ratio

$$
ByzantineRate=\frac{K_{malicious}}{K_{total}}
$$

### 3.2 Robust Aggregation 목적

$$
w_{t+1}=Agg\left(\{w_{t+1}^{(k)}\}_{k=1}^{K}\right)
$$

**보안 해석:** aggregation 함수가 단순 평균이면 악성 client update가 global model에 큰 영향을 줄 수 있다. 방어는 update norm, anomaly score, robust median/trimmed mean 등으로 확장된다.

---

## 4. 위협모형·평가지표

| 항목 | 내용 |
|---|---|
| 보호 자산 | local data, update, aggregation function, global model |
| 공격자 목표 | accuracy drop, target ASR 증가, privacy inference, aggregation poisoning |
| 지표 | clean accuracy, ASR, Byzantine rate, detection rate, FPR, client fairness |
| 재현성 | client split, IID/non-IID setting, malicious client index, aggregation config 기록 |

---

## 5. 기말논문 연결

P03은 W10의 위협 taxonomy와 실험 설계 기준 문헌이다. 기말논문에서는 분산 참여자가 있는 AI 시스템의 update provenance와 악성 참여자 비율 평가에 반영한다.

---

## 6. 최종 판단

P03은 W10에서 공격·방어 taxonomy와 experimental challenge를 제공하는 핵심 문헌이다.
