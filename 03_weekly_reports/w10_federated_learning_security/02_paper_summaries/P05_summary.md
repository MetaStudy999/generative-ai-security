# P05 Summary

## Backdoor attacks and defenses in federated learning: Survey, challenges and future research directions — Thuy Dung Nguyen et al., Engineering Applications of Artificial Intelligence, 2024

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W10 연합학습(FL) & FL 위협·방어·정책 |
| 논문명 | Backdoor attacks and defenses in federated learning: Survey, challenges and future research directions |
| 저자 | Thuy Dung Nguyen, Tuan Nguyen, Phi Le Nguyen, Hieu H. Pham, Khoa D. Doan, Kok-Seng Wong |
| 공식 출판 정보 | Engineering Applications of Artificial Intelligence, Vol. 127, Article 107166, 2024 |
| DOI | https://doi.org/10.1016/j.engappai.2023.107166 |
| 보조 URL | https://arxiv.org/abs/2303.02213 |
| 로컬 PDF | `01_papers/pdf/05_Nguyen_et_al_2024_FL_Backdoor_Attacks_Defenses.pdf` |
| 검증 상태 | W10 `paper_list.md` 기준 arXiv와 출판 DOI 확인. 출판본 DOI와 volume/article 정보 확인 완료 |
| PDF 확인 메모 | repo의 PDF 폴더에 해당 PDF blob이 존재함을 확인했다. 요약은 로컬 PDF 경로와 W10 `paper_list.md`의 공식 DOI 메타데이터 기준으로 보완했다. |
| 핵심 근거 사용 가능 여부 | 가능. W10에서 FL backdoor 공격·방어, malicious client, trigger behavior, model replacement, robust aggregation, anomaly detection, provenance audit를 설명하는 직접 핵심 문헌으로 사용 |

---

## 1. 한 문장 요약

이 논문은 federated learning 환경의 backdoor 공격과 방어를 **malicious client, local data poisoning, model poisoning, model replacement, trigger behavior, stealthiness, clean accuracy 유지, attack success rate, robust aggregation, anomaly detection, client reputation, defense challenge** 관점에서 체계화하며, W10에서 FL 보안 평가는 clean accuracy만으로 부족하고 **ASR·client provenance·trigger evaluation·aggregation audit**를 함께 봐야 함을 설명하는 핵심 backdoor survey 문헌이다.

---

## 2. 핵심 연구문제

> FL backdoor 공격은 일부 malicious client가 local update를 조작해 global model의 정상 성능은 유지하면서 특정 trigger 조건에서만 공격자 목표 행동을 하도록 만드는 문제다. 이러한 은닉 행동을 어떤 threat model과 metric으로 평가하고, robust aggregation·anomaly detection·client trust로 어떻게 완화할 것인가?

| 번호 | 연구질문 |
|---|---|
| RQ1 | FL backdoor는 중앙집중 backdoor와 비교해 client participation, aggregation, non-IID data, partial visibility 측면에서 어떤 차이가 있는가? |
| RQ2 | 악성 client update는 local data poisoning, model poisoning, scaling, model replacement 등을 통해 global model에 어떻게 은닉 trigger behavior를 삽입하는가? |
| RQ3 | Clean accuracy와 attack success rate를 분리해 평가해야 하는 이유는 무엇인가? |
| RQ4 | Robust aggregation, anomaly detection, update clipping, client reputation, validation set filtering은 어떤 방어 효과와 한계를 갖는가? |
| RQ5 | FL backdoor 실험에서 malicious client id, trigger pattern, target label, attack round, aggregation rule, client split, non-IID setting을 어떻게 기록해야 재현 가능한가? |

---

## 3. 논문의 핵심 기여

| 기여 | 설명 | W10 연결 |
|---|---|---|
| FL backdoor taxonomy | data poisoning, model poisoning, model replacement, trigger-based attack을 FL 환경에서 분류 | W10 backdoor 핵심 축 |
| FL 특수성 설명 | partial client participation, non-IID data, aggregation, client drift가 backdoor 평가를 어렵게 함 | W10 P01/P03과 연결 |
| 공격·방어 mapping | backdoor 공격 유형과 robust aggregation, anomaly detection, client reputation 등 방어를 연결 | threat-defense-metric matrix 근거 |
| Stealthiness 강조 | clean accuracy를 유지하면서 특정 trigger에서만 오작동하는 특성을 설명 | clean accuracy와 ASR 분리 필요 |
| Future challenges 제시 | 강건한 방어, realistic benchmark, adaptive attacker, privacy-preserving defense, provenance 문제 제시 | W14/W15 evidence chain 연결 |

---

## 4. 목차별 핵심 개괄

| 목차 | 핵심 내용 | 비전공자용 이해 |
|---|---|---|
| 1. Introduction | FL은 데이터 프라이버시 장점이 있지만, 일부 악성 client가 참여하면 global model에 backdoor를 심을 수 있다. | 여러 사람이 함께 모델을 만들 때, 일부 참여자가 몰래 “특정 신호가 오면 틀리게 답하라”는 습관을 넣을 수 있다. |
| 2. Federated Learning Background | FL의 server-client 구조, local training, aggregation, client participation, non-IID data 특성을 설명한다. | 각 client가 자기 데이터로 학습하고 update만 중앙 서버에 보내며, 서버는 이를 합쳐 global model을 만든다. |
| 3. Backdoor Attack Background | Backdoor는 정상 입력에서는 잘 작동하지만 trigger가 있는 입력에서 공격자 목표 출력으로 유도하는 공격이다. | 평소에는 멀쩡하지만 특정 표시가 붙으면 이상하게 동작하는 모델을 만드는 것이다. |
| 4. Backdoor Attacks in FL | Malicious client가 local data 또는 update를 조작해 aggregation을 통과하고 global model에 trigger behavior를 삽입하는 방법을 분류한다. | 악성 참여자가 보낸 학습 결과가 평균에 섞여 전체 모델의 숨은 습관이 된다. |
| 5. Defense Mechanisms | Robust aggregation, update clipping, anomaly detection, client reputation, validation-based detection, model inspection 등을 정리한다. | 너무 이상한 update를 걸러내거나, 참여자 신뢰도를 관리하거나, trigger 행동을 검사하는 방어가 필요하다. |
| 6. Evaluation Metrics | Clean accuracy, ASR, malicious client ratio, defense detection rate, FPR, utility drop, communication cost를 함께 봐야 한다. | 평소 성능이 좋아도 특정 trigger에서 공격 성공률이 높으면 안전하지 않다. |
| 7. Challenges | Non-IID와 악성 update 구분, adaptive attacker, stealthy backdoor, privacy-preserving defense와 audit 충돌, benchmark 부족이 문제다. | 정상 참여자도 데이터가 다르면 update가 이상해 보일 수 있어, 악성인지 정상 차이인지 구분이 어렵다. |
| 8. Future Research Directions | 현실적인 threat model, robust yet fair defense, client provenance, scalable auditing, privacy-compatible detection이 필요하다. | 앞으로는 단순히 평균을 잘 내는 것이 아니라 누가 어떤 update를 보냈는지 안전하게 감사해야 한다. |
| 9. Conclusion | FL backdoor 방어는 clean utility와 hidden trigger risk를 동시에 평가해야 하며, aggregation과 client provenance가 핵심이다. | FL 보안 평가는 “평소 정확도”와 “숨은 조건에서의 위험”을 분리해 봐야 한다. |

---

## 5. 핵심 이론 및 수식

> 아래 수식은 FL backdoor 공격·방어 평가를 W10 보고서에서 설명하기 위한 표준화된 표현이다. 실제 공격 절차 제공이 아니라 안전한 toy/synthetic evaluation과 문헌 기반 분석을 전제로 한다.

### 5.1 FL Backdoor Attack Success Rate

Backdoor trigger가 삽입된 입력이 target label 또는 target behavior로 유도된 비율이다.

$$
ASR_{bd}=\frac{1}{N}\sum_{i=1}^{N}\mathbf{1}[f_{w}(T(x_i))=y_t]
$$

| 기호 | 의미 |
|---|---|
| $T(x_i)$ | trigger가 적용된 입력 |
| $y_t$ | 공격자 목표 label 또는 target behavior |
| $f_w$ | global model |
| $N$ | trigger test sample 수 |

### 비전공자용 설명

평소에는 정상적으로 작동하는 모델이 특정 표시가 붙은 입력에서만 공격자가 원하는 답을 하는지 보는 지표다.

### 보안적 의미

Clean accuracy가 높아도 ASR이 높으면 backdoor가 성공한 것이다. 따라서 FL backdoor 평가에서는 clean accuracy와 ASR을 반드시 분리해야 한다.

---

### 5.2 Malicious Client Ratio

한 round 또는 전체 학습 과정에서 악성 client 비율을 측정한다.

$$
MalClientRate=\frac{K_{mal}}{K_{total}}
$$

| 기호 | 의미 |
|---|---|
| $K_{mal}$ | malicious client 수 |
| $K_{total}$ | 전체 참여 client 수 |

### 보안적 의미

악성 client가 적어도 update scaling이나 model replacement가 가능하면 global model에 큰 영향을 줄 수 있다. 실험에서는 malicious client 수와 참여 round를 반드시 기록해야 한다.

---

### 5.3 Clean-Backdoor Trade-off

Backdoor는 정상 성능을 유지하면서 hidden behavior를 심는 것이 특징이다.

$$
BackdoorRisk=\alpha ASR_{bd}-\beta Acc_{clean}+\gamma StealthScore
$$

| 기호 | 의미 |
|---|---|
| $ASR_{bd}$ | trigger 조건 공격 성공률 |
| $Acc_{clean}$ | 정상 test set 정확도 |
| $StealthScore$ | update 이상치가 탐지되지 않는 정도 또는 clean behavior 유지 정도 |

### 보안적 의미

공격자는 global model의 정상 성능을 떨어뜨리지 않으려 한다. 따라서 방어자는 정확도 하락만 보고 backdoor를 판단하면 안 된다.

---

### 5.4 Model Replacement Effect

악성 client update가 aggregation 후 global model을 공격자 목표 방향으로 강하게 끌어가는 위험을 표현할 수 있다.

$$
\Delta w_{global}=Agg(\Delta w_1,\ldots,\Delta w_{mal},\ldots,\Delta w_K)
$$

$$
Influence_{mal}=\frac{\|\Delta w_{mal}\|}{\sum_{k=1}^{K}\|\Delta w_k\|}
$$

### 보안적 의미

특정 client update의 norm이나 방향이 과도하게 크면 global update에 큰 영향을 줄 수 있다. Update clipping, norm monitoring, robust aggregation이 필요한 이유다.

---

### 5.5 Defense Detection Rate and False Positive Rate

방어가 악성 update를 얼마나 잘 탐지하고 정상 client를 얼마나 오탐하는지 평가한다.

$$
DetectionRate=\frac{TP_{malicious}}{TP_{malicious}+FN_{malicious}}
$$

$$
FPR=\frac{FP_{benign}}{FP_{benign}+TN_{benign}}
$$

### 보안적 의미

악성 client 탐지율이 높아도 정상 non-IID client를 많이 오탐하면 시스템 공정성과 성능이 악화된다. DetectionRate와 FPR은 함께 보고해야 한다.

---

### 5.6 Utility Drop under Defense

방어 적용 후 정상 성능 손실을 측정한다.

$$
UtilityDrop=Acc_{no\ defense}-Acc_{defense}
$$

### 보안적 의미

강한 방어는 ASR을 줄일 수 있지만 정상 정확도도 낮출 수 있다. 따라서 방어 평가는 ASR 감소와 utility drop을 함께 비교해야 한다.

---

### 5.7 Trigger Coverage and Provenance

Trigger test와 client provenance가 얼마나 충분히 기록되었는지 평가한다.

$$
AuditCoverage=\frac{N_{rounds\ with\ client\ update\ provenance}}{N_{total\ rounds}}
$$

### 보안적 의미

Backdoor 사고가 의심될 때 어느 client가 어느 round에서 어떤 update를 보냈는지 추적할 수 있어야 한다. Client ID는 privacy를 고려해 pseudonym으로 관리하되, update hash와 round log는 필요하다.

---

## 6. AI 원리 70% 관점 분석

| 원리 항목 | 설명 | W10/P05에서의 의미 |
|---|---|---|
| Federated Learning | 여러 client가 local update를 보내 global model 학습 | backdoor 삽입 경로 |
| Client Participation | round마다 일부 client만 참여 | 악성 client 참여 시점이 중요 |
| Aggregation | client update를 결합 | malicious update가 global model에 반영되는 지점 |
| Non-IID Data | client별 데이터 분포 차이 | 정상 drift와 backdoor update 구분 어려움 |
| Backdoor Learning | trigger와 target behavior를 은닉 학습 | clean accuracy와 ASR 분리 필요 |
| Model Replacement | 악성 update가 global model 방향을 강하게 조작 | update norm과 robust aggregation 평가 |
| Robust Aggregation | 악성 update 영향 완화 | 방어 핵심 축 |
| Anomaly Detection | update 이상치 탐지 | non-IID 오탐과 trade-off |

---

## 7. 보안 이슈 30% 관점 분석

| 보안 항목 | FL Backdoor 관점 해석 | 대표 평가 지표 |
|---|---|---|
| 기밀성 | client provenance와 update log가 민감정보를 포함할 수 있음 | log access control, pseudonymization |
| 무결성 | malicious client가 global model에 trigger behavior를 삽입 | ASR, PoisonImpact, Influence_mal |
| 가용성 | 과도한 방어가 정상 client를 배제해 학습 지연·성능 저하 유발 | FPR, dropout, UtilityDrop |
| 프라이버시 | backdoor 탐지를 위한 update 감사가 privacy와 충돌 가능 | privacy-auditability trade-off |
| 안전성 | clean accuracy가 좋아도 trigger 조건에서 위험 behavior 발생 가능 | ASR_bd, failure case |
| 책임성 | 악성 round/client/update를 추적하지 못하면 사고 원인 분석 불가 | AuditCoverage, update hash completeness |

---

## 8. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | global model, client update, aggregation process, client participation log, trigger test set, validation set, update hash, round log |
| 공격자 목표 | trigger 조건에서 target label 유도, clean 성능 유지, defense 우회, aggregation 조작, stealthy update 제출 |
| 공격자 능력 | malicious client 참여, local data poisoning, model update manipulation, update scaling, model replacement, trigger pattern 선택 |
| 공격 경로 | malicious local training → poisoned/model-replacement update → server aggregation → global model deployment → trigger input inference |
| 방어자 능력 | robust aggregation, update clipping, anomaly detection, client reputation, validation-based test, trigger scanning, update provenance logging |
| 제외 범위 | 실제 FL 서비스 공격, 실제 client 데이터 사용, 개인정보 기반 실험, 공격 코드 제공, 유해 trigger 생성 절차 제공 |

---

## 9. 평가방법 및 지표

| 평가축 | 지표 | 의미 | W10/P05 활용 |
|---|---|---|---|
| 정상 성능 | clean accuracy, loss, convergence round | 정상 test 성능 유지 | stealthiness 평가 |
| 공격 성공 | ASR_bd, target class error | trigger 조건 공격 성공 | backdoor 핵심 지표 |
| 공격자 조건 | MalClientRate, malicious client index, attack round | 공격 조건 명시 | 실험 재현성 |
| 악성 영향 | Influence_mal, update norm, cosine similarity | 악성 update의 global 영향 | model replacement 평가 |
| 방어 효과 | DetectionRate, FPR, ASR reduction | 악성 update 탐지·완화 | 방어 평가 |
| 유틸리티 비용 | UtilityDrop, convergence delay | 방어의 정상 성능 비용 | trade-off 평가 |
| 공정성 | per-client accuracy, non-IID FPR | 정상 non-IID client 오탐 여부 | fairness 평가 |
| 감사 가능성 | AuditCoverage, update provenance completeness | 사고 원인 추적 가능성 | W15 evidence chain |

---

## 10. 재현성 체크리스트

| 항목 | 기록해야 할 내용 |
|---|---|
| FL scenario | cross-device/cross-silo, client 수, participation rate, server trust assumption |
| Dataset split | IID/non-IID split, client별 data size, target class, trigger test set 구성 |
| Threat model | malicious client 수와 index, attacker knowledge, attack round, attack objective |
| Backdoor setting | trigger type/category, target label, poisoned sample ratio, model replacement 여부 |
| Aggregation | FedAvg/median/trimmed mean/Krum 등 aggregation rule과 parameter |
| Defense setting | clipping, anomaly detection, robust aggregation, client reputation, validation test 여부 |
| Evaluation | clean accuracy, ASR_bd, DetectionRate, FPR, UtilityDrop, Influence_mal, AuditCoverage |
| Logs | seed, round trace, client participation, update hash, malicious client pseudonym, failure case |
| 한계 | toy FL/backdoor 결과를 실제 의료·금융·모바일 FL 보안 보증으로 과장하지 않음 |

---

## 11. 논문의 고유 기여

1. FL backdoor 공격과 방어를 전문적으로 정리한 W10의 직접 핵심 문헌이다.
2. 중앙집중 backdoor와 달리 FL backdoor는 client participation, aggregation, non-IID, update visibility 문제와 결합된다는 점을 설명한다.
3. Clean accuracy와 ASR을 분리해 평가해야 함을 명확히 한다.
4. Robust aggregation과 anomaly detection 방어가 non-IID client drift와 privacy-auditability trade-off 때문에 제한될 수 있음을 보여준다.
5. 기말논문에서 malicious contribution, hidden behavior, update provenance audit 평가표를 만드는 직접 근거를 제공한다.

---

## 12. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| Stealthy attack 탐지 어려움 | clean accuracy가 유지되면 backdoor가 숨어 있을 수 있다. | ASR와 trigger test set 별도 평가 |
| Non-IID와 악성 update 구분 | 정상 client drift가 이상치처럼 보일 수 있다. | benign non-IID baseline과 malicious condition 분리 |
| Adaptive attacker | 공격자가 방어를 알고 update를 조정할 수 있다. | defense assumption과 adaptive risk 명시 |
| Defense trade-off | robust aggregation이 ASR을 낮춰도 utility와 fairness를 악화시킬 수 있다. | UtilityDrop, FPR, FairnessGap 병기 |
| Privacy-audit 충돌 | update를 자세히 감사하면 client privacy가 노출될 수 있다. | pseudonymized provenance와 접근통제 설계 |
| Benchmark 부족 | FL backdoor benchmark와 threat model이 논문마다 다르다. | threat-defense-metric matrix와 재현성 체크리스트 제안 |

---

## 13. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | 분산 참여형 AI 시스템은 hidden behavior와 malicious contribution을 별도로 평가해야 한다는 문제의식 |
| 2장 관련연구 | FL backdoor attacks and defenses survey를 핵심 관련연구로 정리 |
| 3장 위협모형 | malicious client, local update, trigger test set, aggregation process, global model 보호 자산 정의 |
| 4장 연구방법 | ASR_bd, MalClientRate, DetectionRate, FPR, UtilityDrop, AuditCoverage 지표 설계 |
| 5장 분석 | clean accuracy와 ASR 분리표, malicious client provenance audit workflow 제시 |
| 6장 보안적 함의 | robust aggregation, trigger evaluation, client trust, privacy-auditability trade-off 해석 |

---

## 14. 기말논문 연결 3문장

1. W10에서 기말논문에 반영할 개념: FL backdoor는 global model의 clean accuracy를 유지하면서 특정 trigger 조건에서만 공격자 목표 행동을 유도할 수 있으므로, FL 보안 평가는 accuracy와 ASR을 반드시 분리해야 한다.
2. W10에서 기말논문에 반영할 표·그림·실험: FL backdoor threat model, malicious client ratio, ASR_bd, DetectionRate/FPR, UtilityDrop, AuditCoverage를 포함한 hidden behavior 평가표를 반영한다.
3. W10이 LLM/RAG 보안 감사 프레임워크와 연결되는 지점: 분산 참여자가 모델 업데이트나 지식 그래프를 기여하는 구조에서는 hidden trigger, malicious contribution, update provenance, rollback log를 W14/W15 evidence chain에 포함해야 한다.

---

## 15. 최종 판단

P05는 W10의 backdoor 핵심 문헌이다. P01이 FL aggregation 구조를 제공하고 P02~P04가 보안·프라이버시 taxonomy와 정책축을 제공한다면, P05는 FL에서 가장 은밀한 무결성 위협인 backdoor를 집중적으로 다룬다. 따라서 W10 기말논문 연결에서는 P05를 **hidden behavior, ASR, malicious client, robust aggregation, client provenance audit 설계의 중심 근거 문헌**으로 사용하는 것이 적절하다.

---

## 16. 변환 호환성 메모

```bash
pandoc P05_summary.md -o P05_summary.docx
pandoc P05_summary.md -o P05_summary.pdf --pdf-engine=xelatex
```
