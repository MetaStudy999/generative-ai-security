# P03 Summary

## Survey on federated learning threats: Concepts, taxonomy on attacks and defences, experimental study and challenges — Nuria Rodriguez-Barroso et al., Information Fusion, 2023

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W10 연합학습(FL) & FL 위협·방어·정책 |
| 논문명 | Survey on federated learning threats: Concepts, taxonomy on attacks and defences, experimental study and challenges |
| 저자 | Nuria Rodriguez-Barroso, Daniel Jimenez-Lopez, M. Victoria Luzon, Francisco Herrera, Eugenio Martinez-Camara |
| 공식 출판 정보 | Information Fusion, Vol. 90, pp. 148–173, 2023 |
| DOI | https://doi.org/10.1016/j.inffus.2022.09.011 |
| 보조 URL | https://arxiv.org/abs/2201.08135 |
| 로컬 PDF | `01_papers/pdf/03_Rodriguez_Barroso_et_al_2023_FL_Threats_Survey.pdf` |
| 검증 상태 | W10 `paper_list.md` 기준 arXiv와 출판 DOI 확인. 출판본 DOI와 volume/page 정보 확인 완료 |
| PDF 확인 메모 | repo의 PDF 폴더에 해당 PDF blob이 존재함을 확인했다. 요약은 로컬 PDF 경로와 W10 `paper_list.md`의 공식 DOI 메타데이터 기준으로 보완했다. |
| 핵심 근거 사용 가능 여부 | 가능. W10에서 FL 공격·방어 taxonomy, threat model, experimental challenge, malicious client 비율, robust aggregation 평가의 중심 문헌으로 사용 |

---

## 1. 한 문장 요약

이 논문은 federated learning의 위협을 **data poisoning, model poisoning, backdoor, Byzantine behavior, inference attack, communication threat, malicious client, server-side threat, robust aggregation, anomaly detection, privacy defense, experimental taxonomy** 관점에서 정리하고, 실제 실험 설계의 어려움인 **non-IID data, client sampling, malicious client ratio, aggregation rule, clean accuracy-ASR trade-off**를 함께 다루는 W10의 공격·방어 평가 핵심 문헌이다.

---

## 2. 핵심 연구문제

> Federated Learning은 원본 데이터를 공유하지 않는 분산학습 구조이지만, client update와 aggregation 과정에서 다양한 공격과 방어가 발생한다. 이러한 FL 위협을 공격 위치, 공격 목표, 공격자 능력, 방어 방식, 실험 조건에 따라 어떻게 분류하고 재현성 있게 평가할 것인가?

| 번호 | 연구질문 |
|---|---|
| RQ1 | FL 공격은 client-side, server-side, communication-side, aggregation-side에서 어떻게 분류되는가? |
| RQ2 | Data poisoning, model poisoning, Byzantine attack, backdoor attack, inference attack은 각각 어떤 보호 자산을 노리는가? |
| RQ3 | Robust aggregation, anomaly detection, secure aggregation, differential privacy는 어떤 공격에 효과적이고 어떤 trade-off를 만드는가? |
| RQ4 | Non-IID data, client sampling, local epoch, malicious client ratio, aggregation rule은 FL 공격·방어 평가 결과를 어떻게 바꾸는가? |
| RQ5 | FL threat 실험에서 clean accuracy, attack success rate, false positive, defense cost, client fairness, reproducibility evidence를 어떻게 함께 기록해야 하는가? |

---

## 3. 논문의 핵심 기여

| 기여 | 설명 | W10 연결 |
|---|---|---|
| FL threat taxonomy | 공격 위치, 공격 목표, 공격자 능력에 따라 FL 위협을 체계적으로 분류 | W10 위협모형 기본 구조 |
| 공격·방어 mapping | poisoning, inference, Byzantine, backdoor와 robust aggregation, DP, secure aggregation 등을 연결 | W10 P02/P05와 연결 |
| Experimental study 관점 | 단순 문헌 정리가 아니라 실험 설계의 변수와 한계를 강조 | 기말논문 방법론과 평가표 근거 |
| Non-IID와 client sampling 영향 | 정상 client drift와 악성 update 구분의 어려움을 제시 | malicious update 판별 평가 연결 |
| Challenge 정리 | 재현성, benchmark 부족, 현실적 공격자 모델, defense trade-off 문제 제시 | W14/W15 evidence chain 연결 |

---

## 4. 목차별 핵심 개괄

| 목차 | 핵심 내용 | 비전공자용 이해 |
|---|---|---|
| 1. Introduction | FL은 데이터를 공유하지 않는 장점이 있지만, 분산 참여자와 update aggregation 때문에 새로운 공격면이 생긴다. | 데이터를 보내지 않아도 “학습 결과”를 보내는 과정에서 공격과 유출이 생길 수 있다. |
| 2. Federated Learning Concepts | Server, client, local training, communication round, global aggregation, client participation, IID/non-IID 개념을 정리한다. | 여러 참여자가 각자 공부한 뒤 결과를 중앙에 보내고, 중앙이 평균을 내 새 교재를 만드는 구조다. |
| 3. Taxonomy on Attacks | Data poisoning, model poisoning, backdoor, Byzantine attack, inference attack, communication attack 등을 분류한다. | 일부 참여자가 나쁜 학습 결과를 보내거나, update를 보고 개인정보를 추정하는 공격이 가능하다. |
| 4. Taxonomy on Defences | Robust aggregation, anomaly detection, clipping, secure aggregation, differential privacy, trusted execution 등을 방어로 정리한다. | 이상한 update를 걸러내거나, update를 숨기거나, noise를 넣어 정보를 보호한다. |
| 5. Experimental Study | 공격·방어 실험에서 client 수, malicious client 비율, non-IID split, aggregation rule, metric 선택이 결과에 큰 영향을 준다. | 같은 공격이라도 참여자 수와 데이터 분포가 달라지면 결과가 완전히 달라질 수 있다. |
| 6. Challenges | 현실적인 공격자 모델, benchmark 표준화, 재현성, privacy-utility-robustness trade-off, scalability가 문제로 남는다. | 실험실에서 잘 막았다고 실제 FL 서비스에서도 안전하다고 말하기 어렵다. |
| 7. Conclusion | FL 위협은 공격·방어 taxonomy와 실험 조건을 함께 기록해야 올바르게 비교할 수 있다. | FL 보안 평가는 “무슨 공격을 막았는가”뿐 아니라 “어떤 조건에서 막았는가”가 중요하다. |

---

## 5. 핵심 이론 및 수식

> 아래 수식은 FL threats와 W10 보안 평가를 설명하기 위한 표준화된 표현이다. 수식은 GitHub, MS Word, PDF 변환 호환성을 위해 Markdown 표 밖의 LaTeX block math로 작성한다.

### 5.1 Byzantine Rate

전체 client 중 악성 또는 비정상 client의 비율이다.

$$
ByzantineRate=\frac{K_{malicious}}{K_{total}}
$$

| 기호 | 의미 |
|---|---|
| $K_{malicious}$ | 악성 client 수 |
| $K_{total}$ | 전체 client 수 |

### 비전공자용 설명

공동 학습에 참여하는 기관이나 기기 중 몇 개가 일부러 잘못된 update를 보내는지 보는 비율이다.

### 보안적 의미

ByzantineRate가 높아질수록 단순 평균 aggregation은 취약해진다. Robust aggregation 실험에서는 malicious client 비율을 반드시 기록해야 한다.

---

### 5.2 Robust Aggregation

Server는 client update 집합을 aggregation 함수로 결합한다.

$$
w_{t+1}=Agg\left(\{w_{t+1}^{(k)}\}_{k=1}^{K}\right)
$$

| 기호 | 의미 |
|---|---|
| $Agg$ | FedAvg, median, trimmed mean, Krum 등 aggregation 함수 |
| $w_{t+1}^{(k)}$ | client $k$의 local update 또는 local model |
| $w_{t+1}$ | 새 global model |

### 보안적 의미

Aggregation 함수가 단순 평균이면 악성 update가 global model에 큰 영향을 줄 수 있다. Robust aggregation은 outlier update의 영향력을 낮추지만, non-IID 정상 client를 공격자로 오탐할 위험도 있다.

---

### 5.3 Poisoning Impact

Poisoning이 global model의 정상 성능에 미치는 영향을 측정한다.

$$
PoisonImpact=Acc_{clean}-Acc_{poisoned}
$$

| 기호 | 의미 |
|---|---|
| $Acc_{clean}$ | 정상 client만 있을 때 정확도 |
| $Acc_{poisoned}$ | 악성 client/update가 포함되었을 때 정확도 |

### 보안적 의미

무차별 model poisoning은 clean accuracy를 낮춘다. 그러나 targeted backdoor는 clean accuracy를 유지하면서 특정 trigger에서만 오작동할 수 있으므로 ASR도 같이 봐야 한다.

---

### 5.4 Backdoor Attack Success Rate

Backdoor 공격 조건에서 target label이나 target behavior가 성공한 비율이다.

$$
ASR_{backdoor}=\frac{N_{trigger\ samples\ classified\ as\ target}}{N_{trigger\ samples}}
$$

### 보안적 의미

Clean accuracy가 높아도 ASR이 높으면 안전하지 않다. FL backdoor 평가는 clean utility와 targeted attack success를 분리해야 한다.

---

### 5.5 Inference Leakage Risk

Update 또는 model output을 통해 client data의 membership, property, sensitive attribute가 추론되는 위험이다.

$$
LeakageRisk=\frac{N_{successful\ inference}}{N_{inference\ attempts}}
$$

### 보안적 의미

FL은 raw data를 공유하지 않지만 update와 global model이 정보 누출 경로가 될 수 있다. W11 membership inference와 직접 연결된다.

---

### 5.6 Defense Detection Rate and False Positive Rate

방어가 악성 client를 얼마나 잘 탐지하고, 정상 client를 얼마나 오탐하는지 평가한다.

$$
DetectionRate=\frac{TP_{malicious}}{TP_{malicious}+FN_{malicious}}
$$

$$
FPR=\frac{FP_{benign}}{FP_{benign}+TN_{benign}}
$$

### 보안적 의미

악성 client 탐지율이 높아도 정상 non-IID client를 많이 오탐하면 FL 학습 참여 공정성과 성능이 떨어진다.

---

### 5.7 Client Fairness Gap

방어 적용 후 client별 성능 편차를 측정한다.

$$
FairnessGap=\max_k Acc_k-\min_k Acc_k
$$

### 보안적 의미

방어가 특정 client 집단의 성능을 크게 떨어뜨리면 정책·공정성 문제가 발생한다. Non-IID 환경에서는 fairness gap을 함께 봐야 한다.

---

## 6. AI 원리 70% 관점 분석

| 원리 항목 | 설명 | W10/P03에서의 의미 |
|---|---|---|
| FL architecture | server-client 구조와 update aggregation | 공격면 위치 정의 |
| Client participation | 일부 client만 round에 참여 | 공격 확률과 방어 난이도 변화 |
| Non-IID data | client별 데이터 분포 차이 | 정상 drift와 공격 update 구분 문제 |
| Aggregation rule | update 결합 방식 | robust aggregation의 핵심 |
| Poisoning | 학습 데이터 또는 model update 조작 | model utility와 integrity 훼손 |
| Backdoor | 특정 trigger에서만 target behavior 유도 | clean accuracy와 ASR 분리 필요 |
| Inference attack | update/model에서 client 정보 추론 | privacy leakage 평가 |
| Experimental protocol | 공격자 비율, split, seed, metric 기록 | 재현성 핵심 |

---

## 7. 보안 이슈 30% 관점 분석

| 보안 항목 | FL Threat Taxonomy 관점 해석 | 대표 평가 지표 |
|---|---|---|
| 기밀성 | update, gradient, model output이 client data 정보를 누출할 수 있음 | LeakageRisk, MI success |
| 무결성 | data/model poisoning과 Byzantine update가 global model을 오염 | PoisonImpact, ASR, ByzantineRate |
| 가용성 | 악성 client와 방어 오탐이 학습 지연·client 배제 문제를 유발 | dropout rate, FPR, round failure |
| 프라이버시 | raw data 미공유에도 membership/property inference 가능 | inference success, DP budget |
| 안전성 | backdoored global model이 downstream task에서 위험 behavior를 유발 | backdoor ASR, failure case |
| 책임성 | malicious client index, aggregation config, update hash가 없으면 원인 추적 불가 | audit completeness, provenance coverage |

---

## 8. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | local data, gradient/update, client identity, aggregation function, global model, client participation log, update hash |
| 공격자 목표 | accuracy drop, targeted ASR 증가, membership/property inference, aggregation poisoning, robust defense 우회 |
| 공격자 능력 | 일부 client 장악, local data poisoning, model update 조작, scaling, sign-flipping, backdoor trigger 삽입, communication 관찰 |
| 공격 경로 | local training → malicious update generation → client submission → aggregation → global model update → downstream inference |
| 방어자 능력 | robust aggregation, anomaly detection, clipping, client trust, secure aggregation, differential privacy, update provenance logging |
| 제외 범위 | 실제 client 데이터 사용, 개인정보 기반 inference 실험, 실제 FL 서비스 공격, 공격 코드 제공 |

---

## 9. 평가방법 및 지표

| 평가축 | 지표 | 의미 | W10/P03 활용 |
|---|---|---|---|
| 기본 성능 | clean accuracy, loss, convergence round | FL baseline 성능 | 정상 utility 평가 |
| 공격 영향 | PoisonImpact, ASR, target class error | 공격 성공 정도 | poisoning/backdoor 평가 |
| 공격자 조건 | ByzantineRate, malicious client index | 악성 client 조건 | 실험 재현성 |
| 방어 효과 | DetectionRate, FPR, robust aggregation success | 악성 update 탐지·완화 | 방어 평가 |
| 프라이버시 | LeakageRisk, inference success | update/model 정보 유출 | W11 연결 |
| Non-IID 영향 | client drift, per-client accuracy | 정상 heterogeneity 영향 | 오탐 구분 |
| 공정성 | FairnessGap, worst-client accuracy | client별 성능 편차 | 정책 평가 |
| 재현성 | client split, seed, aggregation config, round trace | 실험 반복 가능성 | W15 evidence chain |

---

## 10. 재현성 체크리스트

| 항목 | 기록해야 할 내용 |
|---|---|
| FL scenario | cross-device/cross-silo, client 수, server 신뢰 가정 |
| Dataset split | IID/non-IID split, class imbalance, client별 data size |
| Threat model | 공격 위치, 공격 목표, attacker knowledge, malicious client 수와 index |
| Attack setting | data poisoning/model poisoning/backdoor/inference 구분, 공격 round, target class |
| Defense setting | robust aggregation, anomaly detection, clipping, DP, secure aggregation 여부 |
| Aggregation config | FedAvg/median/trimmed mean/Krum 등 aggregation rule과 parameter |
| Evaluation | clean accuracy, ASR, PoisonImpact, DetectionRate, FPR, LeakageRisk, FairnessGap |
| Logs | seed, client participation, update hash, round trace, malicious client index, failure case |
| 한계 | toy FL 결과를 실제 의료·금융·모바일 FL 보안 보증으로 과장하지 않음 |

---

## 11. 논문의 고유 기여

1. FL threat를 공격 위치, 공격 목표, 공격자 능력, 방어 방식으로 체계화한다.
2. Data poisoning, model poisoning, backdoor, Byzantine attack, inference attack을 하나의 taxonomy로 연결한다.
3. Robust aggregation과 anomaly detection의 필요성과 한계를 experimental challenge 관점에서 설명한다.
4. Non-IID data와 malicious update를 구분해야 하는 평가 난점을 강조한다.
5. W10 기말논문에서 threat-defense-metric matrix와 malicious client 실험설계를 만드는 직접 근거를 제공한다.

---

## 12. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 실험 조건 민감성 | client split, non-IID level, malicious rate에 따라 결과가 달라진다. | 모든 config와 seed 기록 |
| Non-IID와 공격 구분 어려움 | 정상 client drift가 악성 update처럼 보일 수 있다. | benign non-IID baseline과 attack condition 분리 |
| 방어 trade-off | robust aggregation은 공격을 줄이지만 성능·공정성·통신비용에 영향 | clean utility와 fairness 병기 |
| Privacy와 audit 충돌 | secure aggregation은 privacy를 높이지만 개별 update 감사는 어렵게 한다. | privacy-auditability trade-off 명시 |
| Benchmark 부족 | FL threat benchmark가 일관되지 않아 논문 간 비교가 어렵다. | threat-defense-metric matrix 제안 |
| 실제 운영 전이 | toy/cross-silo 실험이 실제 cross-device 환경을 대표하지 못한다. | scenario scope 명확화 |

---

## 13. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | FL 보안은 raw data 미공유가 아니라 malicious client와 aggregation 신뢰성 문제라는 문제의식 |
| 2장 관련연구 | FL threat taxonomy와 attack/defense survey 정리 |
| 3장 위협모형 | local update, malicious client, aggregation function, global model, participation log 보호 자산 정의 |
| 4장 연구방법 | ByzantineRate, PoisonImpact, ASR, DetectionRate, FPR, FairnessGap 지표 설계 |
| 5장 분석 | FL attack-defense-metric matrix와 non-IID/악성 update 구분표 제시 |
| 6장 보안적 함의 | robust aggregation, secure aggregation, audit log, client trust, privacy-audit trade-off 해석 |

---

## 14. 기말논문 연결 3문장

1. W10에서 기말논문에 반영할 개념: FL 위협은 client-side와 server-side뿐 아니라 communication, aggregation, evaluation protocol 전반에서 발생하므로 공격 위치와 공격자 능력을 명확히 분리해야 한다.
2. W10에서 기말논문에 반영할 표·그림·실험: ByzantineRate, PoisonImpact, backdoor ASR, DetectionRate, FPR, FairnessGap을 포함한 FL threat-defense-metric matrix를 반영한다.
3. W10이 LLM/RAG 보안 감사 프레임워크와 연결되는 지점: 분산 참여자가 update나 지식 graph를 기여하는 구조에서는 malicious contribution, provenance, aggregation rule, audit log를 W14/W15 evidence chain에 포함해야 한다.

---

## 15. 최종 판단

P03은 W10에서 공격·방어 taxonomy와 experimental challenge를 제공하는 핵심 문헌이다. P01이 FL aggregation 구조를 제공하고 P02가 보안·프라이버시 전체 범주를 제공한다면, P03은 악성 client, poisoning, backdoor, Byzantine behavior, inference attack을 실험 조건과 지표로 연결한다. 따라서 W10 기말논문 연결에서는 P03을 **FL threat-defense-metric matrix, malicious client ratio, robust aggregation 평가의 중심 근거 문헌**으로 사용하는 것이 적절하다.

---

## 16. 변환 호환성 메모

```bash
pandoc P03_summary.md -o P03_summary.docx
pandoc P03_summary.md -o P03_summary.pdf --pdf-engine=xelatex
```
