# P01 Summary

## Federated Learning Survey: A Multi-Level Taxonomy of Aggregation Techniques, Experimental Insights, and Future Frontiers — Meriem Arbaoui et al., ACM TIST, 2024

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W10 Federated Learning Security |
| 논문명 | Federated Learning Survey: A Multi-Level Taxonomy of Aggregation Techniques, Experimental Insights, and Future Frontiers |
| 저자 | Meriem Arbaoui et al. |
| 출판 정보 | ACM Transactions on Intelligent Systems and Technology, 15(6), pp. 1–69, 2024 |
| DOI | https://doi.org/10.1145/3678182 |
| 검증 상태 | W10 `paper_list.md` 기준 DOI 확인. 수업자료 ACM CSUR 표기와 공식 TIST 표기 차이 메모 유지 |

---

## 1. 한 문장 요약

이 논문은 federated learning을 **client-server architecture, local update, aggregation, non-IID data, communication efficiency, experimental taxonomy** 관점에서 정리하며, W10에서 안전한 aggregation과 감사 가능한 분산학습 평가의 기본 구조를 제공한다.

---

## 2. 핵심 연구질문

| 번호 | 연구질문 |
|---|---|
| RQ1 | FL은 중앙집중 학습과 비교해 어떤 데이터·통신·보안 구조를 갖는가? |
| RQ2 | FedAvg와 aggregation 기법은 client update를 어떻게 결합하는가? |
| RQ3 | non-IID client data는 성능과 공정성·보안 평가에 어떤 영향을 주는가? |
| RQ4 | aggregation 단계는 poisoning/backdoor 공격면이 되는가? |

---

## 3. 핵심 수식

### 3.1 Federated Averaging

$$
w_{t+1}=\sum_{k=1}^{K}\frac{n_k}{n}w_{t+1}^{(k)}
$$

| 기호 | 의미 |
|---|---|
| $w_{t+1}^{(k)}$ | client $k$의 local model update |
| $n_k$ | client $k$의 data size |
| $n$ | 전체 참여 데이터 수 |

### 보안 해석

악성 client update가 aggregation에 포함되면 global model이 오염될 수 있다. 따라서 update provenance, anomaly score, robust aggregation이 필요하다.

---

## 4. 위협모형·평가지표

| 항목 | 내용 |
|---|---|
| 보호 자산 | client data, local update, global model, aggregation log |
| 공격자 목표 | malicious update 삽입, model poisoning, backdoor, privacy leakage |
| 지표 | clean accuracy, client drift, update norm, aggregation robustness, communication cost |
| 재현성 | client split, non-IID setting, seed, client participation log 기록 |

---

## 5. 기말논문 연결

P01은 W10의 FL 기본 구조 문헌이다. 기말논문에서는 RAG/LLM 문서·모델 업데이트도 분산 데이터 기여 구조로 볼 수 있으므로 provenance와 aggregation audit 논리로 확장한다.

---

## 6. 최종 판단

P01은 FL 기본 taxonomy와 aggregation 평가의 핵심 배경 문헌이다. 보안 세부 위협은 P02~P05와 결합한다.
