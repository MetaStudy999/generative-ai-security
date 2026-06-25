# P03 Summary

## A Joint Study of the Challenges, Opportunities, and Roadmap of MLOps and AIOps: A Systematic Survey — Josu Diaz-de-Arcaya et al., ACM Computing Surveys, 2023/2024

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W14 MLOps & AI Supply Chain |
| 공식 논문명 | A Joint Study of the Challenges, Opportunities, and Roadmap of MLOps and AIOps: A Systematic Survey |
| 공식 저자 | Josu Diaz-de-Arcaya, Ana I. Torre-Bastida, Gorka Zarate, Raul Minon, Aitor Almeida |
| 공식 출판 정보 | ACM Computing Surveys, Vol. 56, Issue 4, pp. 1–30, online 2023-10-21, print 2024-04-30 |
| DOI | https://doi.org/10.1145/3625289 |
| 로컬 PDF | `01_papers/pdf/03_RELATED_Cheng_et_al_2023_AIOps_Cloud_Survey.pdf` |
| 로컬 PDF 상태 | W14 `paper_list.md` 기준 로컬 PDF는 Cheng et al., `AI for IT Operations (AIOps) on Cloud Platforms: Reviews, Opportunities and Challenges`, arXiv:2304.04661 관련 보조 문헌이다. 공식 P03 DOI 논문과 동일 문헌으로 단정하지 않는다. |
| 검증 상태 | W14 `paper_list.md` 기준 공식 DOI 확인. 수업자료의 `Daniel Diaz-de-Arcaya et al., A Systematic Survey on MLOps and AIOps: Taxonomy, Challenges, and Future Directions` 표기와 DOI 메타데이터·로컬 PDF 사이 차이 메모 유지 |
| PDF 확인 메모 | repo의 PDF 폴더에 P03 관련 PDF blob이 존재함을 확인했다. 다만 로컬 PDF는 공식 P03 지정 논문과 다른 AIOps/cloud 보조 문헌이므로, summary는 공식 DOI 기준 P03을 중심으로 작성하고 로컬 PDF는 AIOps cloud telemetry·incident automation 보완 문헌으로만 해석한다. |
| 핵심 근거 사용 가능 여부 | 가능. W14에서 MLOps와 AIOps의 접점, operational telemetry, monitoring, alert quality, incident response, automation governance, model lifecycle, cloud operation, audit evidence를 설명하는 핵심 문헌으로 사용 |

---

## 1. 한 문장 요약

이 논문은 MLOps와 AIOps를 **model lifecycle, operational telemetry, observability, anomaly detection, alert management, incident response, automation, cloud operation, model deployment, monitoring, drift, root-cause analysis, human approval, rollback, governance roadmap** 관점에서 함께 정리하며, W14에서 AI 보안 운영을 단순 MLOps 배포 관리가 아니라 **관제·탐지·대응·복구 자동화가 결합된 AI 운영 보안 체계**로 확장하는 핵심 bridge 문헌이다.

---

## 2. 핵심 연구문제

> MLOps는 모델 개발·배포·모니터링 생명주기를 관리하고, AIOps는 운영 로그·metric·trace·alert를 분석해 장애와 이상을 탐지·대응하는 체계다. AI 시스템이 실제 서비스에서 안전하게 운영되려면 이 둘을 분리하지 않고 model lifecycle evidence와 operational telemetry를 연결해야 한다.

| 번호 | 연구질문 |
|---|---|
| RQ1 | MLOps와 AIOps는 데이터, 모델, 배포, 운영 telemetry, incident log 측면에서 어떤 공통 자산과 통제 지점을 갖는가? |
| RQ2 | AI 시스템 장애·보안사고를 탐지하기 위해 어떤 metric, log, trace, alert, deployment event, model registry evidence가 필요한가? |
| RQ3 | 자동화된 anomaly detection과 incident response는 false alarm, alert fatigue, automation error, rollback failure를 어떻게 관리해야 하는가? |
| RQ4 | MLOps/AIOps 통합 체계에서 human approval, escalation, rollback, postmortem, audit log는 어떤 governance 역할을 하는가? |
| RQ5 | 기말논문에서 W01~W13의 공격·방어 지표를 W14의 운영 관제와 W15의 재현성 evidence chain에 어떻게 연결할 것인가? |

---

## 3. 논문의 핵심 기여

| 기여 | 설명 | W14 연결 |
|---|---|---|
| MLOps/AIOps bridge | 모델 생명주기 관리와 운영 관제 자동화를 하나의 roadmap으로 연결 | W14 P03 핵심 |
| Operational telemetry 강조 | metric, log, trace, alert, incident timeline을 AI 운영 증거로 해석 | monitoring·incident evidence 설계 |
| 자동화 위험 제시 | AIOps 자동화는 alert quality와 human approval 없이 오작동할 수 있음을 지적 | automation governance |
| Incident response 연결 | 탐지, 분류, root-cause analysis, 대응, rollback, postmortem을 운영 과정으로 정리 | W14/W15 evidence chain |
| Cloud AIOps 보완 | 로컬 관련 PDF의 cloud-platform AIOps 맥락을 보조적으로 활용 가능 | cloud telemetry와 edge/cloud 운영 연결 |

---

## 4. 목차별 핵심 개괄

| 목차 | 핵심 내용 | 비전공자용 이해 |
|---|---|---|
| 1. Introduction | ML 시스템은 배포 후에도 monitoring, incident response, automation이 필요하며, MLOps와 AIOps가 이를 함께 다룬다. | AI는 배포 후에도 계속 감시하고 문제가 생기면 자동·수동으로 대응해야 한다. |
| 2. MLOps Background | 데이터·코드·모델·배포·모니터링 생명주기, model registry, CI/CD/CT를 정리한다. | 모델 개발부터 운영까지 버전과 로그를 남기는 체계다. |
| 3. AIOps Background | 운영 metric, log, trace, alert, anomaly detection, root-cause analysis, incident automation을 정리한다. | 서버와 서비스 로그를 AI로 분석해 장애를 빨리 찾는 체계다. |
| 4. Joint Taxonomy | MLOps와 AIOps의 공통 영역을 data pipeline, deployment, monitoring, observability, automation, governance로 통합한다. | 모델 운영과 시스템 운영을 따로 보지 않고 한 장의 지도에 놓는다. |
| 5. Challenges | data quality, monitoring blind spot, alert fatigue, automation risk, tool fragmentation, role ambiguity가 문제로 제시된다. | 너무 많은 알람은 무시되고, 자동화가 잘못 작동하면 더 큰 장애가 될 수 있다. |
| 6. Opportunities | predictive maintenance, automated incident triage, drift detection, self-healing, model retraining governance가 기회로 제시된다. | 문제를 미리 예측하고, 원인을 찾고, 필요한 경우 복구까지 자동화할 수 있다. |
| 7. Roadmap | 관측성 확보, metric 표준화, human-in-the-loop approval, evidence log, governance-by-design이 필요하다. | 자동화 전에 무엇을 기록하고 누가 승인할지 정해야 한다. |
| 8. Future Directions | explainable AIOps, secure automation, trustworthy monitoring, cross-cloud operation, AI governance가 향후 과제다. | 관제 AI도 설명 가능하고 감사 가능해야 한다. |
| 로컬 관련 PDF 메모 | 로컬 PDF는 Cheng et al. AIOps cloud survey로, official P03과 동일 문헌으로 인용하지 않는다. | PDF가 있다고 해서 공식 지정 논문으로 인용하면 안 된다. |

---

## 5. 핵심 이론 및 수식

> 아래 수식은 MLOps/AIOps 운영 보안과 관제 자동화 평가를 W14 보고서에서 설명하기 위한 표준화된 표현이다. 실제 논문의 정량식이라기보다 기말논문 운영 평가표 설계를 위한 지표다.

### 5.1 OpsScore

운영 관제 품질은 탐지 범위, alert 품질, 복구 준비도, 자동화 위험을 함께 고려한다.

$$
OpsScore=DetectionCoverage+AlertQuality+RecoveryReadiness-AutomationRisk
$$

| 기호 | 의미 |
|---|---|
| $DetectionCoverage$ | 운영 metric/log/trace/alert가 위험을 얼마나 포착하는지 |
| $AlertQuality$ | alert의 precision, recall, actionable quality |
| $RecoveryReadiness$ | rollback, escalation, runbook 준비도 |
| $AutomationRisk$ | 잘못된 자동 대응, alert storm, feedback loop 위험 |

### 보안적 의미

운영 자동화는 탐지와 복구를 개선할 수 있지만, 품질 낮은 alert와 승인 없는 자동 대응은 새로운 위험이 된다.

---

### 5.2 Detection Coverage

필수 운영 이벤트 중 telemetry로 관측 가능한 비율이다.

$$
DetectionCoverage=\frac{|Events_{observable}|}{|Events_{critical}|}
$$

### 보안적 의미

관측되지 않는 이벤트는 탐지할 수 없다. AI 보안 운영에서는 모델 이벤트, 데이터 이벤트, 배포 이벤트, 사용자 이벤트를 모두 관측해야 한다.

---

### 5.3 Alert Precision and Recall

Alert 품질을 오탐과 미탐 관점으로 평가한다.

$$
AlertPrecision=\frac{TP}{TP+FP},\qquad AlertRecall=\frac{TP}{TP+FN}
$$

### 보안적 의미

precision이 낮으면 alert fatigue가 발생하고, recall이 낮으면 중요 incident를 놓친다.

---

### 5.4 Mean Time To Detect / Resolve

탐지와 복구 시간을 나눠 측정한다.

$$
MTTD=t_{detected}-t_{occurred}
$$

$$
MTTR=t_{resolved}-t_{detected}
$$

### 보안적 의미

AI 시스템 사고는 빠른 탐지와 빠른 복구가 모두 필요하다. MTTD와 MTTR은 별도 관리해야 한다.

---

### 5.5 Automation Risk

자동화된 대응의 실패 위험을 요약한다.

$$
AutomationRisk=\alpha FalseAction+\beta EscalationFailure+\gamma RollbackFailure+\delta AlertStorm
$$

### 보안적 의미

AIOps 자동화는 승인·검증·rollback gate 없이 운영되면 false action으로 서비스를 악화시킬 수 있다.

---

### 5.6 Incident Evidence Completeness

incident 대응 과정의 증거가 얼마나 완전한지 평가한다.

$$
IncidentEvidence=\frac{|Logs_{timeline}+Actions_{recorded}+Artifacts_{linked}|}{|Evidence_{required}|}
$$

### 보안적 의미

postmortem과 감사는 incident timeline, model version, data version, alert rule, operator action이 연결되어야 가능하다.

---

### 5.7 MLOps/AIOps Integration Score

모델 생명주기와 운영 관제가 얼마나 연결되어 있는지 평가한다.

$$
IntegrationScore=\frac{|Links_{model\text{-}ops}|}{|Links_{expected}|}
$$

| 연결 예 | 설명 |
|---|---|
| model registry ↔ deployment event | 어떤 모델이 언제 배포되었는지 |
| deployment event ↔ alert | 특정 배포 이후 어떤 alert가 발생했는지 |
| alert ↔ incident ticket | alert가 incident로 승격되었는지 |
| incident ↔ rollback | 어떤 모델 버전으로 복구했는지 |

---

## 6. AI 원리 70% 관점 분석

| 원리 항목 | 설명 | W14/P03에서의 의미 |
|---|---|---|
| MLOps | 모델 생명주기 관리 | 개발·배포·모니터링 연결 |
| AIOps | 운영 telemetry를 AI로 분석 | 장애·이상 탐지 자동화 |
| Observability | metric, log, trace 수집 | 탐지 가능성의 전제 |
| Incident Response | 탐지 후 분류·대응·복구 | 운영 보안 핵심 |
| Root-cause Analysis | 원인 추적 | postmortem과 재발 방지 |
| Alert Quality | actionable alert 품질 | alert fatigue 방지 |
| Human-in-the-loop | 자동화 승인·검증 | false action 통제 |
| Roadmap/Governance | 장기 운영 성숙도 | W15 evidence chain 연결 |

---

## 7. 보안 이슈 30% 관점 분석

| 보안 항목 | MLOps/AIOps 관점 해석 | 대표 평가 지표 |
|---|---|---|
| 기밀성 | telemetry와 incident log에 민감정보가 포함될 수 있음 | log masking, access control |
| 무결성 | log tampering과 metric poisoning은 잘못된 대응을 유도 | log integrity, signed telemetry |
| 가용성 | alert storm, automation error, rollback failure가 장애를 확대 | MTTR, rollback success |
| 프라이버시 | 운영 로그의 사용자 데이터와 모델 입력 보존 정책 필요 | retention policy, privacy audit |
| 안전성 | 탐지 지연과 잘못된 자동 대응은 downstream 피해로 연결 | MTTD, false action rate |
| 책임성 | alert rule, operator action, incident timeline이 감사 증거가 됨 | IncidentEvidence, audit completeness |

---

## 8. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | telemetry, metric, log, trace, alert pipeline, incident ticket, model registry, deployment event, rollback artifact, operator action log |
| 공격자/위험 목표 | log tampering, alert fatigue 유발, monitoring blind spot 악용, automation error 유도, incident timeline 삭제 |
| 공격자/위험 능력 | telemetry 조작, noisy alert 유발, threshold 회피, deployment event 은폐, 운영자 실수, 자동화 정책 오류 |
| 위험 경로 | 모델/데이터/배포 이벤트 발생 → telemetry 수집 실패 또는 alert 품질 저하 → incident 탐지 지연 → 자동 대응 오류 또는 rollback 실패 |
| 방어자 능력 | observability, signed log, alert tuning, incident runbook, approval gate, rollback, postmortem, audit evidence 보존 |
| 제외 범위 | 실제 운영 시스템 공격, 로그 변조 절차, credential 탈취, 모니터링 우회 방법, 서비스 장애 유발 지원 |

---

## 9. 평가방법 및 지표

| 평가축 | 지표 | 의미 | W14/P03 활용 |
|---|---|---|---|
| 관측성 | DetectionCoverage, metric/log/trace coverage | 위험 관측 범위 | AIOps 기본 |
| Alert 품질 | AlertPrecision, AlertRecall, false alarm rate | 알람 유용성 | alert fatigue 평가 |
| 탐지·복구 | MTTD, MTTR, incident count | 사고 대응 속도 | 운영 보안 |
| 자동화 위험 | AutomationRisk, false action rate | 자동 대응 부작용 | governance 필요성 |
| 증거 완전성 | IncidentEvidence, audit completeness | postmortem 가능성 | W15 연결 |
| 통합 수준 | IntegrationScore | MLOps와 AIOps 연결성 | W14 bridge 평가 |
| 운영 비용 | monitoring overhead, operator load | 실무 적용성 | MLOps maturity |
| 서지 정확성 | official DOI match, local PDF mismatch flag | 참고문헌 정확성 | reference audit |

---

## 10. 재현성 체크리스트

| 항목 | 기록해야 할 내용 |
|---|---|
| Bibliographic status | 공식 DOI 논문과 로컬 PDF 동일 여부, related flag |
| Telemetry source | metric, log, trace, model event, data event, deployment event |
| Alert rule | threshold, rule version, owner, severity, escalation policy |
| Model evidence | model registry ID, model hash, deployment version |
| Incident timeline | occurred, detected, acknowledged, resolved, postmortem timestamps |
| Operator action | 승인자, 자동/수동 조치, rollback 여부, action log |
| Root cause | data drift, model degradation, infra failure, security event 등 분류 |
| Metrics | AlertPrecision/Recall, MTTD, MTTR, false alarm rate, incident severity |
| Evidence log | ticket ID, dashboard snapshot, config hash, runbook version |
| 한계 | AIOps 자동화 결과를 사람 승인 없는 완전 자율 대응 보장으로 과장하지 않음 |

---

## 11. 논문의 고유 기여

1. MLOps와 AIOps를 분리된 주제가 아니라 AI 운영 생명주기와 관제 자동화의 결합 문제로 정리한다.
2. 운영 telemetry, alert, incident response, automation governance를 AI 보안 평가축으로 확장한다.
3. W14 P01의 MLOps lifecycle과 P02의 deployment challenge를 incident response와 observability 관점으로 연결한다.
4. W09의 DRL 자동 대응, W11 privacy monitoring, W13 watermark/provenance, W15 reproducibility를 하나의 evidence chain으로 묶는 bridge 역할을 한다.
5. 로컬 PDF가 official P03와 다른 AIOps cloud 보조 문헌이므로, 참고문헌 검증표와 related-paper 관리의 중요성을 보여준다.

---

## 12. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 로컬 PDF 불일치 | P03 로컬 PDF는 공식 DOI 논문이 아니라 Cheng et al. AIOps cloud survey다. | 공식 DOI/관련 PDF를 분리 표기 |
| Alert fatigue | 낮은 precision의 alert는 운영자가 무시하게 만든다. | AlertPrecision과 false alarm rate 병기 |
| 자동화 위험 | 잘못된 자동 조치가 장애를 확대할 수 있다. | approval gate와 rollback 조건 명시 |
| Telemetry 품질 | 로그 누락·변조·지연은 AIOps 판단을 왜곡한다. | log integrity와 coverage 평가 |
| 조직 책임 | incident owner와 escalation rule이 없으면 대응이 지연된다. | owner/escalation matrix 작성 |
| LLM/RAG 확장 | 전통 AIOps 지표만으로 hallucination, retrieval drift, prompt drift를 설명하기 어렵다. | LLM/RAG 전용 telemetry 추가 |

---

## 13. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | AI 보안 운영은 배포뿐 아니라 관측성, alert, incident response, 자동화 통제가 필요하다는 문제의식 |
| 2장 관련연구 | 공식 P03 DOI 논문을 MLOps/AIOps bridge survey로 정리하고 로컬 PDF mismatch는 검증표에 기록 |
| 3장 위협모형 | telemetry, alert pipeline, incident log, model registry, deployment event, rollback artifact 보호 자산 정의 |
| 4장 연구방법 | OpsScore, DetectionCoverage, AlertPrecision/Recall, MTTD, MTTR, AutomationRisk, IncidentEvidence 지표 설계 |
| 5장 분석 | MLOps/AIOps integration workflow와 incident evidence chain table 제시 |
| 6장 보안적 함의 | monitoring blind spot, alert fatigue, automation governance, rollback, postmortem evidence 필요성 해석 |

---

## 14. 기말논문 연결 3문장

1. W14에서 기말논문에 반영할 개념: MLOps/AIOps 통합은 model registry와 deployment event를 telemetry, alert, incident ticket, rollback evidence와 연결해 AI 보안 운영의 관측성과 대응성을 높이는 체계다.
2. W14에서 기말논문에 반영할 표·그림·실험: OpsScore, DetectionCoverage, AlertPrecision/Recall, MTTD, MTTR, AutomationRisk, IncidentEvidence 수식표와 MLOps/AIOps integration workflow를 반영한다.
3. W14가 W15 최종 논문과 연결되는 지점: W01~W13의 공격·방어 결과는 W14의 monitoring과 incident response 체계에 연결되어야 하며, W15에서는 이 연결이 evidence chain과 reproducibility table로 정리되어야 한다.

---

## 15. 최종 판단

P03은 W14의 MLOps/AIOps bridge 문헌이다. P01이 MLOps lifecycle을 제공하고 P02가 실제 ML deployment challenge를 제공한다면, P03은 이를 운영 관제, telemetry, alert, incident response, automation governance로 확장한다. 따라서 기말논문에서는 P03을 **AI 보안 운영 관제, MLOps/AIOps 통합, alert quality, incident evidence, automation approval, rollback governance의 중심 근거 문헌**으로 사용하는 것이 적절하다.

---

## 16. 변환 호환성 메모

```bash
pandoc P03_summary.md -o P03_summary.docx
pandoc P03_summary.md -o P03_summary.pdf --pdf-engine=xelatex
```
