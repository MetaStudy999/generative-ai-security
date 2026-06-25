# P02 Summary

## A survey on security and privacy of federated learning — Viraaji Mothukuri et al., Future Generation Computer Systems, 2021

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W10 연합학습(FL) & FL 위협·방어·정책 |
| 논문명 | A survey on security and privacy of federated learning |
| 저자 | Viraaji Mothukuri, Reza M. Parizi, Seyedamin Pouriyeh, Yan Huang, Ali Dehghantanha, Gautam Srivastava |
| 공식 출판 정보 | Future Generation Computer Systems, Vol. 115, pp. 619–640, 2021 |
| DOI | https://doi.org/10.1016/j.future.2020.10.007 |
| 로컬 PDF | `01_papers/pdf/02_Mothukuri_et_al_2021_FL_Security_Privacy_Survey.pdf` |
| 검증 상태 | W10 `paper_list.md` 기준 공식 DOI 확인. 100점형 summary 보완 완료 |
| PDF 확인 메모 | repo의 PDF 폴더에 해당 PDF blob이 존재함을 확인했다. 요약은 로컬 PDF 경로와 W10 `paper_list.md`의 공식 DOI 메타데이터 기준으로 보완했다. |
| 핵심 근거 사용 가능 여부 | 가능. W10에서 FL의 보안·프라이버시 위협, inference attack, poisoning, Byzantine client, secure aggregation, differential privacy, trust management를 설명하는 직접 핵심 문헌으로 사용 |

---

## 1. 한 문장 요약

이 논문은 federated learning의 보안·프라이버시 위협을 **client data privacy, gradient/update leakage, inference attack, poisoning attack, Byzantine client, model poisoning, backdoor, secure aggregation, differential privacy, encryption, access control, trust management, communication overhead** 관점에서 정리하며, W10에서 FL이 원본 데이터를 중앙에 모으지 않아도 update와 aggregation 단계에서 여전히 공격면이 남는다는 점을 설명하는 핵심 보안 survey 문헌이다.

---

## 2. 핵심 연구문제

> Federated learning은 원본 데이터가 client에 남아 있으므로 privacy-preserving 구조처럼 보이지만, model update, gradient, aggregation, client participation, communication channel에서 어떤 보안·프라이버시 위험이 발생하고 어떤 방어가 필요한가?

| 번호 | 연구질문 |
|---|---|
| RQ1 | FL은 raw data를 중앙 서버로 전송하지 않음에도 model update와 gradient를 통해 어떤 privacy leakage가 발생할 수 있는가? |
| RQ2 | 악성 client 또는 compromised server는 poisoning, model update manipulation, backdoor, Byzantine behavior를 통해 global model을 어떻게 오염시키는가? |
| RQ3 | Secure aggregation, homomorphic encryption, differential privacy, robust aggregation, anomaly detection은 각각 어떤 보호를 제공하고 어떤 비용을 만든다? |
| RQ4 | FL 보안 평가는 accuracy만이 아니라 privacy leakage, attack success rate, utility drop, communication overhead, computation cost를 어떻게 함께 봐야 하는가? |
| RQ5 | Cross-device FL과 cross-silo FL에서 신뢰 모델, client identity, access control, audit log는 어떻게 달라지는가? |

---

## 3. 논문의 핵심 기여

| 기여 | 설명 | W10 연결 |
|---|---|---|
| FL security/privacy taxonomy | FL의 주요 공격과 방어를 privacy attack, poisoning, communication, trust, cryptographic defense로 정리 | W10 보안·프라이버시 기준 문헌 |
| Privacy leakage 문제 제기 | 원본 데이터를 공유하지 않아도 gradient/update가 정보를 누출할 수 있음을 설명 | W11 MIA/DP와 연결 |
| Poisoning·Byzantine 위협 정리 | 악성 client update가 global model을 왜곡할 수 있음을 정리 | W10 P03/P05와 연결 |
| 방어기술 비교 | secure aggregation, DP, encryption, anomaly detection, robust aggregation의 trade-off 정리 | 방어 평가표 설계 |
| 운영 고려사항 제시 | communication overhead, computation cost, client trust, access control 필요성 강조 | W14 MLOps와 W15 evidence chain 연결 |

---

## 4. 목차별 핵심 개괄

| 목차 | 핵심 내용 | 비전공자용 이해 |
|---|---|---|
| 1. Introduction | FL은 분산된 client가 데이터를 공유하지 않고 공동 모델을 학습하는 방식이지만, 보안·프라이버시 문제가 여전히 남아 있다. | 데이터를 보내지 않는다고 자동으로 안전한 것은 아니다. 학습 결과를 주고받는 과정에서도 정보가 샐 수 있다. |
| 2. Federated Learning Background | FL의 server-client 구조, local training, aggregation, communication round, cross-device/cross-silo 유형을 설명한다. | 여러 기관이나 기기가 각자 학습하고 중앙 서버가 update를 모아 모델을 만든다. |
| 3. Security Threats | Model poisoning, data poisoning, Byzantine behavior, malicious update, communication attack 등을 정리한다. | 일부 참여자가 나쁜 학습 결과를 보내면 전체 모델이 망가질 수 있다. |
| 4. Privacy Threats | Gradient leakage, membership inference, model inversion, property inference, data reconstruction 위험을 다룬다. | 원본 데이터는 안 보내도 update를 보면 어떤 데이터로 학습했는지 추정될 수 있다. |
| 5. Defense Mechanisms | Secure aggregation, differential privacy, encryption, robust aggregation, anomaly detection, access control, trust management를 정리한다. | update를 암호화하거나, noise를 넣거나, 이상한 update를 걸러내는 방어가 필요하다. |
| 6. Trade-offs | 보안·프라이버시 방어는 accuracy, communication cost, computation cost, convergence speed에 영향을 준다. | 더 안전하게 만들수록 느려지거나 성능이 조금 떨어질 수 있다. |
| 7. Applications and Challenges | Healthcare, IoT, mobile, edge computing 등 민감 데이터 환경에서 FL이 유용하지만, trust, scalability, audit가 중요하다. | 병원·휴대폰·IoT처럼 데이터를 모으기 어려운 곳에 좋지만 관리가 복잡하다. |
| 8. Future Directions | Privacy-preserving FL, robust aggregation, secure communication, trust-aware FL, scalable defense가 미래 과제다. | 앞으로는 성능보다 “안전하고 감사 가능한 분산학습”이 중요하다. |
| 9. Conclusion | FL은 privacy-preserving potential이 있지만, update leakage와 malicious client 문제를 방어하지 않으면 안전하지 않다. | FL의 핵심은 데이터를 안 보내는 것뿐 아니라 update와 aggregation을 안전하게 관리하는 것이다. |

---

## 5. 핵심 이론 및 수식

> 아래 수식은 FL security/privacy 평가를 W10 보고서에서 설명하기 위한 표준화된 표현이다. 수식은 GitHub, MS Word, PDF 변환 호환성을 위해 Markdown 표 밖의 LaTeX block math로 작성한다.

### 5.1 Federated Security Risk

FL의 보안 위험은 poisoning impact, privacy leakage, Byzantine rate, communication exposure 등을 함께 고려할 수 있다.

$$
Risk_{FL}=\alpha PoisonImpact+\beta LeakageRisk+\gamma ByzantineRate+\delta CommExposure
$$

| 기호 | 의미 |
|---|---|
| $PoisonImpact$ | malicious update가 global model에 미치는 영향 |
| $LeakageRisk$ | gradient/update를 통한 privacy leakage 위험 |
| $ByzantineRate$ | 비정상 또는 악성 client 비율 |
| $CommExposure$ | 통신 과정에서 노출되는 정보 위험 |

### 비전공자용 설명

FL 위험은 하나가 아니다. 나쁜 참여자, 정보 유출, 통신 노출, 서버/클라이언트 신뢰 문제를 모두 합쳐 봐야 한다.

---

### 5.2 Update Leakage Risk

Client update가 client data 정보를 얼마나 암시하는지 평가한다.

$$
LeakageRisk=\frac{N_{sensitive\ attributes\ inferred}}{N_{inference\ attempts}}
$$

| 기호 | 의미 |
|---|---|
| $N_{sensitive\ attributes\ inferred}$ | 추론에 성공한 민감 속성 또는 membership 사례 수 |
| $N_{inference\ attempts}$ | privacy inference 시도 수 |

### 보안적 의미

FL은 원본 데이터를 보내지 않아도 update가 데이터의 흔적을 담을 수 있다. 따라서 gradient inversion, membership inference, property inference를 별도로 평가해야 한다.

---

### 5.3 Poison Impact

악성 update가 global model 성능을 얼마나 떨어뜨리는지 측정한다.

$$
PoisonImpact=Acc_{clean}-Acc_{poisoned}
$$

| 기호 | 의미 |
|---|---|
| $Acc_{clean}$ | 정상 client만 참여했을 때 global model 정확도 |
| $Acc_{poisoned}$ | malicious client 또는 poisoned update가 포함되었을 때 정확도 |

### 보안적 의미

PoisonImpact가 크면 global model이 악성 client update에 취약하다. 단, targeted backdoor의 경우 clean accuracy는 유지되면서 특정 trigger ASR만 높아질 수 있으므로 ASR도 함께 봐야 한다.

---

### 5.4 Byzantine Rate

전체 참여 client 중 비정상·악성 client 비율이다.

$$
ByzantineRate=\frac{K_{malicious}}{K_{total}}
$$

| 기호 | 의미 |
|---|---|
| $K_{malicious}$ | malicious 또는 Byzantine client 수 |
| $K_{total}$ | 전체 참여 client 수 |

### 비전공자용 설명

공동 학습에 참여한 기관이나 기기 중 몇 개가 이상하거나 악성인지를 보는 비율이다.

---

### 5.5 Privacy-Utility Trade-off

Differential privacy나 encryption 기반 방어는 privacy를 높이지만 utility를 낮출 수 있다.

$$
UtilityDrop=Acc_{baseline}-Acc_{private}
$$

| 기호 | 의미 |
|---|---|
| $Acc_{baseline}$ | privacy defense 없이 학습한 기준 정확도 |
| $Acc_{private}$ | DP, secure aggregation 등 privacy defense 적용 후 정확도 |

### 보안적 의미

방어를 적용하면 privacy leakage는 줄어들 수 있지만 모델 성능, convergence speed, communication cost가 나빠질 수 있다. 따라서 privacy와 utility를 함께 보고해야 한다.

---

### 5.6 Secure Aggregation Coverage

Secure aggregation이 얼마나 많은 update를 보호하는지 기록한다.

$$
SecureAggCoverage=\frac{N_{updates\ protected}}{N_{total\ updates}}
$$

### 보안적 의미

일부 update만 보호된다면 aggregation 전체가 안전하다고 말할 수 없다. round별 보호 범위와 실패 사례를 기록해야 한다.

---

### 5.7 Defense Cost

보안 방어는 통신·계산 비용을 증가시킬 수 있다.

$$
DefenseCost=CommOverhead+CompOverhead+LatencyIncrease
$$

### 보안적 의미

암호화, secure aggregation, DP, anomaly detection을 적용하면 안전성은 높아지지만 비용이 증가한다. 실제 운영에서는 overhead를 함께 평가해야 한다.

---

## 6. AI 원리 70% 관점 분석

| 원리 항목 | 설명 | W10/P02에서의 의미 |
|---|---|---|
| Federated Learning | 원본 데이터를 모으지 않고 local update로 global model 학습 | privacy-preserving potential의 출발점 |
| Local Update | client가 자기 데이터로 계산한 model update/gradient | privacy leakage와 poisoning의 핵심 매개체 |
| Aggregation | server가 client update를 결합 | malicious update가 global model에 반영되는 지점 |
| Non-IID Data | client별 데이터 분포 차이 | 정상 drift와 악성 update 구분의 어려움 |
| Secure Aggregation | server가 개별 update를 직접 보지 못하게 보호 | privacy 보호와 audit 어려움 trade-off |
| Differential Privacy | update에 noise를 넣어 개별 데이터 영향 제한 | privacy-utility trade-off 발생 |
| Robust Aggregation | 악성 update의 영향을 줄이는 aggregation | poisoning/Byzantine 방어 |
| Trust Management | client 신뢰도와 접근권한 관리 | cross-silo/cross-device 운영 보안 |

---

## 7. 보안 이슈 30% 관점 분석

| 보안 항목 | FL Security/Privacy 관점 해석 | 대표 평가 지표 |
|---|---|---|
| 기밀성 | gradient/update가 client data 정보를 누출할 수 있음 | LeakageRisk, membership inference success |
| 무결성 | malicious update, poisoning, Byzantine client가 global model을 오염 | PoisonImpact, ByzantineRate, ASR |
| 가용성 | 통신 실패, 악성 client, 과도한 방어 비용이 학습을 지연 | dropout rate, latency, DefenseCost |
| 프라이버시 | 원본 데이터 미공유만으로 충분하지 않으며 DP/secure aggregation 필요 | UtilityDrop, DP budget, SecureAggCoverage |
| 안전성 | 오염된 global model이 downstream task에서 위험한 판단을 만들 수 있음 | clean accuracy, backdoor ASR, failure case |
| 책임성 | 공격 또는 leakage 발생 시 어떤 update와 round가 원인인지 추적 필요 | update provenance, audit completeness |

---

## 8. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | client raw data, local gradient/update, client identity, global model, aggregation rule, communication channel, round log |
| 공격자 목표 | membership inference, gradient leakage, model inversion, property inference, model poisoning, backdoor, Byzantine disruption |
| 공격자 능력 | 일부 client 장악, update 조작, local data poisoning, communication observation, server/aggregator 관찰, metadata 조작 |
| 공격 경로 | client local training → update/gradient generation → communication → aggregation → global model update → downstream inference |
| 방어자 능력 | secure aggregation, DP, encryption, robust aggregation, anomaly detection, access control, trust management, audit log |
| 제외 범위 | 실제 client 데이터 사용, 개인정보 기반 gradient inversion 실험, 실제 FL 서비스 공격, 공격 코드 제공 |

---

## 9. 평가방법 및 지표

| 평가축 | 지표 | 의미 | W10/P02 활용 |
|---|---|---|---|
| 기본 성능 | clean accuracy, convergence round | FL 모델 성능 | baseline 평가 |
| 프라이버시 | LeakageRisk, MI success, UtilityDrop | update leakage와 privacy 방어 비용 | W11 연결 |
| 무결성 | PoisonImpact, ByzantineRate, backdoor ASR | malicious client 영향 | W10 P03/P05 연결 |
| 방어 효과 | SecureAggCoverage, robust aggregation success | 방어 적용 범위와 효과 | 방어 평가 |
| 비용 | DefenseCost, communication overhead, computation overhead | 운영 부담 | W14 MLOps 연결 |
| 신뢰관리 | client trust score, access-control violation | client 신뢰와 권한 | cross-silo FL 평가 |
| 감사 가능성 | update provenance, round trace completeness | 사고 원인 추적 가능성 | W15 evidence chain |
| 공정성 | per-client accuracy, worst-client accuracy | client별 성능 편차 | 정책 평가 |

---

## 10. 재현성 체크리스트

| 항목 | 기록해야 할 내용 |
|---|---|
| FL scenario | cross-device/cross-silo, client 수, server 신뢰 가정 |
| Dataset split | client별 data size, IID/non-IID split, 민감 속성 포함 여부 |
| Threat model | malicious client 수, server honest-but-curious 여부, attacker capability |
| Local training | local epoch, optimizer, learning rate, batch size, seed |
| Aggregation | FedAvg/robust aggregation/secure aggregation, clipping, anomaly rule |
| Privacy defense | DP noise, privacy budget, encryption/secure aggregation 적용 범위 |
| Evaluation | clean accuracy, LeakageRisk, PoisonImpact, ASR, UtilityDrop, DefenseCost |
| Logs | client participation, update hash, round trace, defense config, failure case |
| 한계 | toy FL 결과를 실제 의료·금융·모바일 FL 보안 보증으로 과장하지 않음 |

---

## 11. 논문의 고유 기여

1. FL이 privacy-preserving 구조로 보이지만 update와 aggregation 단계에서 여전히 공격면이 있음을 체계적으로 보여준다.
2. FL 보안과 프라이버시를 inference attack, poisoning, Byzantine client, secure aggregation, DP, trust management 관점으로 정리한다.
3. 방어기술의 효과뿐 아니라 utility drop, communication overhead, computation cost를 함께 평가해야 함을 강조한다.
4. W10 P01의 aggregation taxonomy를 실제 보안·프라이버시 위협으로 확장하는 중심 문헌이다.
5. W11의 differential privacy와 membership inference, W14의 MLOps audit, W15의 evidence chain과 연결된다.

---

## 12. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 방어 간 trade-off | DP, secure aggregation, robust aggregation은 각각 보호 범위와 비용이 다르다. | UtilityDrop, DefenseCost를 병기 |
| Privacy 보장 과장 위험 | FL이 raw data를 공유하지 않아도 gradient leakage가 가능하다. | privacy leakage 평가 별도 수행 |
| Secure aggregation의 감사 한계 | 개별 update를 숨기면 anomaly detection과 forensic audit가 어려워질 수 있다. | privacy와 auditability trade-off 명시 |
| Non-IID와 공격 구분 | 정상 client drift와 malicious update가 모두 이상치처럼 보일 수 있다. | drift baseline과 attack condition 분리 |
| 실제 운영 복잡성 | client dropout, unreliable network, device heterogeneity가 실험과 다르다. | participation log와 dropout rate 기록 |
| 표준 benchmark 부족 | 보안·프라이버시 방어를 통합 평가하는 표준이 제한적이다. | threat-defense-metric matrix 제안 |

---

## 13. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | FL은 데이터 미공유 구조만으로 안전하지 않으며 update leakage와 malicious client가 핵심 위험이라는 문제의식 |
| 2장 관련연구 | FL security/privacy survey로 핵심 선행연구 정리 |
| 3장 위협모형 | client data, local update, communication channel, aggregation rule, global model 보호 자산 정의 |
| 4장 연구방법 | LeakageRisk, PoisonImpact, ByzantineRate, UtilityDrop, SecureAggCoverage, DefenseCost 지표 설계 |
| 5장 분석 | FL threat-defense-metric matrix와 privacy-utility trade-off 표 제시 |
| 6장 보안적 함의 | secure aggregation, DP, robust aggregation, trust management, audit log 필요성 해석 |

---

## 14. 기말논문 연결 3문장

1. W10에서 기말논문에 반영할 개념: Federated Learning은 원본 데이터를 공유하지 않는 구조이지만, gradient/update와 aggregation 과정에서 privacy leakage, poisoning, Byzantine client 문제가 발생할 수 있다.
2. W10에서 기말논문에 반영할 표·그림·실험: FL security/privacy threat-defense-metric matrix, UtilityDrop 수식, secure aggregation과 DP의 trade-off 표를 반영한다.
3. W10이 LLM/RAG 보안 감사 프레임워크와 연결되는 지점: 분산 기여 기반 AI 시스템에서는 update provenance, privacy leakage, malicious contribution, defense cost를 W14/W15 evidence chain에 포함해야 한다.

---

## 15. 최종 판단

P02는 W10의 FL 보안·프라이버시 기준 문헌이다. P01이 aggregation 구조와 taxonomy를 제공한다면, P02는 그 구조에서 발생하는 privacy leakage, poisoning, Byzantine behavior, secure aggregation, DP, trust management 문제를 직접 다룬다. 따라서 W10 기말논문 연결에서는 P02를 **FL 보안·프라이버시 위협모형과 defense trade-off 평가의 중심 근거 문헌**으로 사용하는 것이 적절하다.

---

## 16. 변환 호환성 메모

```bash
pandoc P02_summary.md -o P02_summary.docx
pandoc P02_summary.md -o P02_summary.pdf --pdf-engine=xelatex
```
