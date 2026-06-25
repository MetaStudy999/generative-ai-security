# P01 Summary

## Federated Learning Survey: A Multi-Level Taxonomy of Aggregation Techniques, Experimental Insights, and Future Frontiers — Meriem Arbaoui et al., ACM TIST, 2024

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W10 연합학습(FL) & FL 위협·방어·정책 |
| 논문명 | Federated Learning Survey: A Multi-Level Taxonomy of Aggregation Techniques, Experimental Insights, and Future Frontiers |
| 저자 | Meriem Arbaoui, Mohamed-el-Amine Brahmia, Abdellatif Rahmoun, Mourad Zghal |
| 공식 출판 정보 | ACM Transactions on Intelligent Systems and Technology, Vol. 15, No. 6, pp. 1–69, 2024 |
| DOI | https://doi.org/10.1145/3678182 |
| 로컬 PDF | `01_papers/pdf/01_Arbaoui_et_al_2024_FL_Aggregation_Taxonomy.pdf` |
| 검증 상태 | W10 `paper_list.md` 기준 공식 DOI 확인. 수업자료/프롬프트의 ACM Computing Surveys 57(2) 표기와 공식 DOI 메타데이터/TIST 표기 차이 메모 유지 |
| PDF 확인 메모 | repo의 PDF 폴더에 해당 PDF blob이 존재함을 확인했다. 요약은 로컬 PDF 경로와 W10 `paper_list.md`의 공식 DOI 메타데이터 기준으로 보완했다. |
| 핵심 근거 사용 가능 여부 | 가능. W10에서 Federated Learning 기본 구조, aggregation taxonomy, non-IID client drift, update provenance, aggregation audit를 설명하는 핵심 배경 문헌으로 사용 |

---

## 1. 한 문장 요약

이 논문은 federated learning을 **client-server architecture, local training, model update aggregation, FedAvg, multi-level aggregation taxonomy, client heterogeneity, non-IID data, communication efficiency, experimental insights, future frontier** 관점에서 정리하며, W10에서 FL 보안을 이해하기 위한 기본 구조와 **aggregation 단계가 model poisoning·backdoor·privacy leakage·auditability의 핵심 공격면**이 됨을 설명하는 핵심 문헌이다.

---

## 2. 핵심 연구문제

> Federated learning은 원본 데이터를 중앙 서버에 모으지 않고 여러 client의 local update를 aggregation해 global model을 학습한다. 이때 aggregation 기법, client heterogeneity, non-IID data, communication cost, update provenance는 성능과 보안성에 어떤 영향을 주는가?

| 번호 | 연구질문 |
|---|---|
| RQ1 | FL은 중앙집중 학습과 비교해 데이터 이동, client participation, server aggregation, privacy assumption 측면에서 어떤 구조적 차이를 갖는가? |
| RQ2 | FedAvg와 그 변형들은 client local update를 어떻게 결합하며, aggregation weight와 client data size는 global model에 어떤 영향을 주는가? |
| RQ3 | Non-IID client data, client drift, straggler, partial participation은 convergence, fairness, robustness를 어떻게 흔드는가? |
| RQ4 | Aggregation 단계는 malicious update, model poisoning, backdoor, free-riding, update manipulation의 공격면이 되는가? |
| RQ5 | FL 실험에서 client split, data heterogeneity, participation log, aggregation rule, communication budget을 어떻게 기록해야 재현성과 감사가 가능한가? |

---

## 3. 논문의 핵심 기여

| 기여 | 설명 | W10 연결 |
|---|---|---|
| Multi-level aggregation taxonomy | FL aggregation 기법을 여러 수준과 기준으로 분류 | W10 aggregation 평가의 기본 구조 |
| FedAvg 기반 구조 정리 | client local training과 server aggregation의 표준 흐름 설명 | FL 기본 수식과 실험 설계 연결 |
| Experimental insights 제공 | aggregation 기법의 성능, 통신 비용, client heterogeneity 영향을 비교 | 실험 재현성 체크리스트 근거 |
| Non-IID/client heterogeneity 분석 | client data 분포 차이와 client drift가 학습에 미치는 영향 논의 | 보안 평가에서 client drift와 poisoning 구분 필요 |
| Future frontiers 제시 | 효율성, scalability, personalization, robustness, privacy, deployment 과제 제시 | W10 P02~P05 보안·프라이버시 문헌 연결 |

---

## 4. 목차별 핵심 개괄

| 목차 | 핵심 내용 | 비전공자용 이해 |
|---|---|---|
| 1. Introduction | FL은 데이터를 중앙 서버로 보내지 않고 각 client가 local model을 학습한 뒤 update만 공유하는 분산학습 방식이다. 데이터 프라이버시와 통신 효율성이 장점이지만, aggregation과 heterogeneity 문제가 중요하다. | 병원·휴대폰·기관이 원본 데이터를 보내지 않고 각자 학습한 결과만 모아 공동 모델을 만드는 방식이다. |
| 2. Federated Learning Background | FL의 기본 구성요소인 server, client, local training, communication round, aggregation, global model update를 설명한다. | 각 참여자가 자기 데이터로 공부한 뒤 “공부 결과”만 중앙에 보내고, 중앙은 그 결과들을 평균 내 새 모델을 만든다. |
| 3. Aggregation Techniques | FedAvg를 중심으로 다양한 aggregation 전략과 변형을 분류한다. 가중 평균, client selection, update normalization, robust/efficient aggregation 등이 논의된다. | 여러 학생의 답안을 평균 낼 때, 누구의 답안을 얼마나 반영할지 정하는 규칙이 aggregation이다. |
| 4. Multi-Level Taxonomy | Aggregation을 client-level, server-level, data heterogeneity, communication, personalization, robustness 등 여러 관점에서 분류한다. | 단순 평균만 보는 것이 아니라 참여자 특성, 데이터 차이, 통신 비용, 보안성을 모두 고려해 평균 방식을 나눈다. |
| 5. Experimental Insights | 여러 aggregation 기법이 accuracy, convergence, communication cost, non-IID setting에서 어떻게 다른지 비교한다. | 같은 FL이라도 참여자 데이터가 다르면 모델 성능과 안정성이 달라진다. |
| 6. Challenges | Non-IID data, client drift, stragglers, scalability, privacy, security, fairness, personalization, deployment 문제가 남아 있다. | 각 참여자가 가진 데이터가 다르고 일부 참여자가 느리거나 악성일 수 있어 공동 학습이 어렵다. |
| 7. Future Frontiers | 더 robust하고 privacy-preserving하며 scalable한 aggregation, personalized FL, edge/IoT deployment, trustworthy FL이 미래 과제로 제시된다. | 앞으로는 평균을 잘 내는 것뿐 아니라 악성 참여자를 견디고, 개인정보를 보호하고, 개인별 맞춤 모델도 고려해야 한다. |
| 8. Conclusion | FL aggregation은 성능·통신·프라이버시·보안·공정성의 trade-off를 갖는 핵심 계층이며, 체계적 taxonomy와 재현성 있는 실험이 필요하다. | FL의 핵심은 데이터를 안 보내는 것이 아니라, 각자 보낸 update를 어떻게 안전하게 합칠 것인가다. |

---

## 5. 핵심 이론 및 수식

> 아래 수식은 FL aggregation과 W10 보안 평가를 설명하기 위한 표준화된 표현이다. 수식은 GitHub, MS Word, PDF 변환 호환성을 위해 Markdown 표 밖의 LaTeX block math로 작성한다.

### 5.1 Federated Learning Objective

FL은 여러 client의 local objective를 가중합해 global objective를 최소화한다.

$$
\min_{w} F(w)=\sum_{k=1}^{K}\frac{n_k}{n}F_k(w)
$$

| 기호 | 의미 |
|---|---|
| $K$ | client 수 |
| $n_k$ | client $k$의 데이터 수 |
| $n=\sum_k n_k$ | 전체 데이터 수 |
| $F_k(w)$ | client $k$의 local loss/objective |
| $w$ | global model parameter |

### 비전공자용 설명

전체 모델은 각 기관의 데이터에서 잘 작동해야 한다. 데이터가 많은 기관의 학습 결과를 조금 더 크게 반영하는 방식이다.

### 보안적 의미

데이터 수가 큰 client나 aggregation weight가 큰 client가 악성이면 global model에 더 큰 영향을 줄 수 있다. 따라서 client weight와 update provenance를 기록해야 한다.

---

### 5.2 Federated Averaging

FedAvg는 각 client가 local training을 수행한 뒤 server가 local model을 가중 평균한다.

$$
w_{t+1}=\sum_{k=1}^{K}\frac{n_k}{n}w_{t+1}^{(k)}
$$

| 기호 | 의미 |
|---|---|
| $w_{t+1}^{(k)}$ | round $t+1$에서 client $k$가 제출한 local model/update |
| $\frac{n_k}{n}$ | client $k$의 aggregation weight |
| $w_{t+1}$ | server가 만든 새 global model |

### 비전공자용 설명

각 참여자가 만든 모델을 데이터 수에 따라 평균 내서 하나의 모델로 합치는 것이다.

### 보안적 의미

악성 client update가 aggregation에 포함되면 global model이 오염될 수 있다. 따라서 update norm, anomaly score, client trust, robust aggregation이 필요하다. 기존 W10 P01에도 FedAvg와 악성 update 포함 위험이 핵심 수식으로 정리되어 있었다.

---

### 5.3 Local Update

각 client는 global model을 받아 자기 데이터로 local step을 수행한다.

$$
w_{t+1}^{(k)}=w_t-\eta\nabla F_k(w_t)
$$

| 기호 | 의미 |
|---|---|
| $w_t$ | 현재 global model |
| $\eta$ | learning rate |
| $\nabla F_k(w_t)$ | client $k$의 local gradient |

### 보안적 의미

Local gradient/update는 client 데이터 분포와 민감한 정보를 암시할 수 있다. 또한 malicious client는 gradient 방향을 조작해 model poisoning이나 backdoor를 유도할 수 있다.

---

### 5.4 Client Drift

Non-IID 환경에서는 client별 update 방향이 global objective와 다르게 흔들릴 수 있다.

$$
Drift_k=\left\|\nabla F_k(w)-\nabla F(w)\right\|_2
$$

| 기호 | 의미 |
|---|---|
| $Drift_k$ | client $k$의 local objective와 global objective 차이 |
| $\nabla F_k(w)$ | local gradient |
| $\nabla F(w)$ | global gradient |

### 비전공자용 설명

각 병원이나 휴대폰이 가진 데이터가 서로 너무 다르면, 각자가 원하는 모델 방향도 달라진다. 그래서 평균을 내도 모델이 흔들릴 수 있다.

### 보안적 의미

정상적인 non-IID client drift와 악성 poisoning update를 구분해야 한다. 단순히 update가 다르다고 모두 공격으로 보면 false positive가 생긴다.

---

### 5.5 Aggregation Robustness

악성 client가 일부 포함되어도 global model 성능이 유지되는지를 측정한다.

$$
RobustnessDrop=Acc_{clean\ clients}-Acc_{mixed\ clients}
$$

| 기호 | 의미 |
|---|---|
| $Acc_{clean\ clients}$ | 정상 client만 있을 때 정확도 |
| $Acc_{mixed\ clients}$ | 정상 client와 악성 client가 섞였을 때 정확도 |

### 보안적 의미

RobustnessDrop이 크면 aggregation rule이 malicious update에 취약하다는 뜻이다. W10 P03/P05의 poisoning/backdoor 평가와 직접 연결된다.

---

### 5.6 Communication Cost

FL은 여러 communication round를 수행하므로 통신 비용이 중요하다.

$$
CommCost=\sum_{t=1}^{T}\sum_{k\in C_t}Size(\Delta w_t^{(k)})
$$

| 기호 | 의미 |
|---|---|
| $T$ | communication round 수 |
| $C_t$ | round $t$에 참여한 client 집합 |
| $\Delta w_t^{(k)}$ | client $k$가 전송한 update |

### 보안적 의미

통신량을 줄이기 위해 update를 압축하거나 sparsify하면 성능과 보안 감시가 달라질 수 있다. update compression은 이상치 탐지와 provenance audit에도 영향을 준다.

---

### 5.7 Update Provenance Score

Aggregation audit를 위해 어떤 update가 어떤 client, round, configuration에서 왔는지 추적해야 한다.

$$
ProvenanceCoverage=\frac{N_{updates\ with\ complete\ metadata}}{N_{total\ updates}}
$$

### 보안적 의미

나중에 global model이 오염되었을 때 어떤 client update가 영향을 줬는지 추적할 수 있어야 한다. 따라서 round log, client ID pseudonym, update hash, aggregation rule을 기록해야 한다.

---

## 6. AI 원리 70% 관점 분석

| 원리 항목 | 설명 | W10/P01에서의 의미 |
|---|---|---|
| Federated Learning | 원본 데이터를 중앙으로 모으지 않고 local update만 공유 | 분산학습 기본 구조 |
| Client-Server Architecture | server가 global model을 배포하고 client가 local training 수행 | FL pipeline 구성 |
| Local Objective | client별 데이터에 대한 local loss | non-IID와 client drift 원인 |
| Aggregation | client update를 결합해 global model 생성 | FedAvg와 robust aggregation의 중심 |
| FedAvg | 데이터 수 가중 평균 기반 aggregation | W10 기본 수식 |
| Non-IID Data | client별 데이터 분포 차이 | 성능·공정성·보안 해석 필요 |
| Communication Efficiency | round, update size, client participation 관리 | edge/IoT 운영 비용 |
| Personalization | client별 특성에 맞춘 모델 조정 | global accuracy와 client fairness 균형 |

---

## 7. 보안 이슈 30% 관점 분석

| 보안 항목 | FL Aggregation 관점 해석 | 대표 평가 지표 |
|---|---|---|
| 기밀성 | local update와 gradient가 client data 정보를 암시할 수 있음 | leakage risk, gradient inversion risk |
| 무결성 | malicious update가 global model을 오염시킬 수 있음 | RobustnessDrop, malicious client rate |
| 가용성 | straggler, client dropout, 통신 실패가 학습을 지연시킴 | participation rate, timeout rate |
| 프라이버시 | 원본 데이터를 공유하지 않아도 update privacy leakage가 가능 | privacy leakage score, DP budget |
| 안전성 | 오염된 global model이 downstream decision을 잘못 만들 수 있음 | clean accuracy, backdoor ASR |
| 책임성 | 어떤 client update가 aggregation에 반영되었는지 추적 필요 | ProvenanceCoverage, aggregation audit completeness |

---

## 8. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | client data, local gradient/update, global model, aggregation rule, client participation log, update hash, round log |
| 공격자 목표 | malicious update 삽입, model poisoning, backdoor, free-riding, client drift 위장, privacy leakage 유도 |
| 공격자 능력 | 일부 client 제어, local data 조작, update scaling, model replacement, participation timing 조작, metadata 위조 |
| 공격 경로 | global model broadcast → local training/update → client submission → server aggregation → global model deployment |
| 방어자 능력 | robust aggregation, update clipping, anomaly detection, client trust, secure aggregation, DP, update provenance logging |
| 제외 범위 | 실제 FL 서비스 공격, 실제 client 데이터 사용, 개인정보 기반 gradient inversion 실험, 공격 코드 제공 |

---

## 9. 평가방법 및 지표

| 평가축 | 지표 | 의미 | W10/P01 활용 |
|---|---|---|---|
| 기본 성능 | clean accuracy, loss, convergence round | FL 모델 성능 | baseline aggregation 평가 |
| Heterogeneity | non-IID level, client drift, client fairness | client별 데이터 차이 영향 | non-IID 평가 |
| Aggregation robustness | RobustnessDrop, malicious client rate | 악성 client 혼입 시 성능 유지 | W10 P03/P05 연결 |
| Privacy | leakage risk, gradient inversion risk | update에서 데이터가 노출되는지 | W10 P02/P04 연결 |
| Communication | CommCost, round count, update size | 통신 비용 | edge/IoT 운영 평가 |
| Participation | participation rate, dropout rate, straggler ratio | client 참여 안정성 | 운영 재현성 |
| Provenance | ProvenanceCoverage, update hash completeness | update 추적 가능성 | W14/W15 evidence chain |
| Fairness | per-client accuracy, worst-client accuracy | client별 성능 편차 | 정책·공정성 평가 |

---

## 10. 재현성 체크리스트

| 항목 | 기록해야 할 내용 |
|---|---|
| Dataset split | client 수, client별 data size, IID/non-IID split 방법 |
| Client setting | participation rate, dropout, straggler, malicious client 여부 |
| Local training | local epoch, batch size, optimizer, learning rate, seed |
| Aggregation rule | FedAvg, weighted average, robust aggregation, clipping 여부 |
| Communication | round 수, update size, compression, communication budget |
| Security setting | malicious client rate, update anomaly rule, secure aggregation/DP 여부 |
| Evaluation | clean accuracy, client drift, RobustnessDrop, CommCost, ProvenanceCoverage |
| Logs | round log, client participation log, update hash, aggregation config |
| 한계 | toy FL 결과를 실제 cross-device/cross-silo FL 보안 보증으로 과장하지 않음 |

---

## 11. 논문의 고유 기여

1. Federated Learning aggregation 기법을 multi-level taxonomy로 체계화한다.
2. FedAvg를 비롯한 aggregation rule이 성능, 통신, non-IID, scalability에 미치는 영향을 정리한다.
3. FL 실험에서 client split, participation, aggregation rule, communication cost를 함께 기록해야 함을 보여준다.
4. W10 보안 관점에서 aggregation 단계가 model poisoning, backdoor, privacy leakage, auditability의 핵심 공격면임을 설명할 수 있는 근거를 제공한다.
5. W10 P02~P05의 FL 보안·프라이버시·backdoor 문헌을 이해하기 위한 기본 구조와 수식 언어를 제공한다.

---

## 12. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 직접 보안 전문 문헌은 아님 | aggregation taxonomy 문헌이며 공격·방어 전문 실험은 P02~P05가 더 직접적이다. | P02~P05와 결합해 보안 위협 분석 보완 |
| Non-IID와 악성 update 구분 어려움 | 정상 client drift와 poisoning update가 모두 outlier처럼 보일 수 있다. | drift와 malicious update를 분리해 평가 |
| Privacy 보장 과장 위험 | FL은 원본 데이터 미공유 구조지만 privacy를 자동 보장하지 않는다. | secure aggregation, DP, leakage risk 병기 |
| 재현성 복잡성 | client split, local epoch, participation, seed 차이가 결과를 크게 바꾼다. | config와 round log 필수화 |
| 운영 환경 차이 | cross-device와 cross-silo FL은 참여자 수, 통신, 신뢰 모델이 다르다. | scenario를 명확히 분리 |
| Aggregation audit 부족 | update metadata와 provenance가 없으면 사고 원인 추적이 어렵다. | update hash, participation log, aggregation config 기록 |

---

## 13. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | 분산 AI 학습은 데이터 미공유만으로 안전하지 않으며 aggregation 무결성과 update provenance가 중요하다는 문제의식 |
| 2장 관련연구 | FL aggregation taxonomy와 FedAvg 기본 구조 정리 |
| 3장 위협모형 | client data, local update, aggregation rule, global model, update log 보호 자산 정의 |
| 4장 연구방법 | FedAvg, RobustnessDrop, ClientDrift, CommCost, ProvenanceCoverage 지표 설계 |
| 5장 분석 | aggregation pipeline과 malicious update 공격면 mapping 표/그림 제시 |
| 6장 보안적 함의 | robust aggregation, secure aggregation, DP, audit log, update approval 필요성 해석 |

---

## 14. 기말논문 연결 3문장

1. W10에서 기말논문에 반영할 개념: Federated Learning은 원본 데이터를 중앙 서버에 모으지 않는 장점이 있지만, client update와 aggregation rule이 global model을 결정하므로 aggregation 무결성과 update provenance가 핵심 보안 자산이 된다.
2. W10에서 기말논문에 반영할 표·그림·실험: FedAvg 수식, FL client-server pipeline, non-IID/client drift 평가표, malicious update와 aggregation audit mapping을 반영한다.
3. W10이 LLM/RAG 보안 감사 프레임워크와 연결되는 지점: RAG 문서·모델 업데이트도 여러 참여자의 기여를 결합하는 구조로 볼 수 있으므로, contribution provenance, aggregation policy, update hash, rollback log를 W14/W15 evidence chain에 포함해야 한다.

---

## 15. 최종 판단

P01은 W10의 FL 기본 taxonomy와 aggregation 평가의 핵심 배경 문헌이다. 직접적인 보안 세부 위협은 P02~P05가 더 강하지만, P01은 FedAvg, aggregation rule, non-IID client drift, communication cost, update provenance를 설명하는 데 필수다. 따라서 W10 기말논문 연결에서는 P01을 **FL aggregation 구조, malicious update 공격면, update provenance audit 설계의 기본 근거 문헌**으로 사용하는 것이 적절하다.

---

## 16. 변환 호환성 메모

```bash
pandoc P01_summary.md -o P01_summary.docx
pandoc P01_summary.md -o P01_summary.pdf --pdf-engine=xelatex
```
