# P02 Summary

## Challenges in Deploying Machine Learning: A Survey of Case Studies — Andrei Paleyes, Raoul-Gabriel Urma, Neil D. Lawrence, ACM Computing Surveys, 2022/2023

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W14 MLOps & AI Supply Chain |
| 논문명 | Challenges in Deploying Machine Learning: A Survey of Case Studies |
| 저자 | Andrei Paleyes, Raoul-Gabriel Urma, Neil D. Lawrence |
| 공식 출판 정보 | ACM Computing Surveys, Vol. 55, Issue 6, pp. 1–29, online 2022-12-07, print 2023-07-31 |
| DOI | https://doi.org/10.1145/3533378 |
| 로컬 PDF | `01_papers/pdf/02_Paleyes_Urma_Lawrence_2022_ML_Deployment_Challenges.pdf` |
| 검증 상태 | W14 `paper_list.md` 기준 공식 DOI 확인. 로컬 PDF는 arXiv판이지만 제목·저자·DOI 주제가 대응됨 |
| PDF 확인 메모 | repo의 PDF 폴더에 P02 관련 PDF blob이 존재함을 확인했다. 요약은 로컬 PDF 경로와 W14 `paper_list.md`의 공식 DOI 메타데이터 기준으로 보완했다. |
| 핵심 근거 사용 가능 여부 | 가능. W14에서 ML deployment challenge, production data risk, drift, infrastructure mismatch, monitoring, feedback loop, rollback, incident response, human process gap을 설명하는 핵심 사례 survey 문헌으로 사용 |

---

## 1. 한 문장 요약

이 논문은 기계학습 모델을 연구실 성능표에서 실제 운영환경으로 옮길 때 발생하는 문제를 **data dependency, feature pipeline, training-serving skew, model drift, concept drift, infrastructure mismatch, monitoring gap, feedback loop, human-in-the-loop process, organizational ownership, deployment risk, incident response, rollback, reproducibility** 관점에서 사례 기반으로 정리하며, W14에서 AI 보안 프레임워크가 반드시 배포·운영·감시·복구 체계를 포함해야 함을 보여주는 핵심 문헌이다.

---

## 2. 핵심 연구문제

> ML 모델은 실험실에서는 높은 성능을 보이더라도 운영환경에서는 데이터 분포 변화, feature schema 불일치, 인프라 제약, 모니터링 부재, 피드백 루프, 조직 책임소재 부재 때문에 실패할 수 있다. 따라서 AI 보안은 공격·방어 알고리즘뿐 아니라 실제 배포 이후의 관측 가능성, 장애 대응, 롤백, 책임 있는 운영 체계를 포함해야 한다.

| 번호 | 연구질문 |
|---|---|
| RQ1 | ML 모델은 연구환경에서 production 환경으로 이동할 때 어떤 data, model, infrastructure, organization failure mode를 갖는가? |
| RQ2 | Training-serving skew, data drift, concept drift, feature quality degradation은 모델 신뢰성과 보안성에 어떤 영향을 주는가? |
| RQ3 | Production ML 시스템은 배포 후 무엇을 모니터링해야 하며, incident detection과 rollback에는 어떤 evidence가 필요한가? |
| RQ4 | 모델 배포 실패는 단순 기술 문제가 아니라 데이터 소유권, 운영 책임, 승인 절차, 사용자 피드백 관리 문제와 어떻게 연결되는가? |
| RQ5 | RAG/LLM 보안 프레임워크를 실제 서비스로 배포하려면 model endpoint, prompt/template, retrieval index, monitoring dashboard, rollback policy를 어떻게 설계해야 하는가? |

---

## 3. 논문의 핵심 기여

| 기여 | 설명 | W14 연결 |
|---|---|---|
| 배포 사례 중심 survey | 실제 ML 배포 사례를 통해 반복되는 실패 조건을 정리 | 실전 운영 리스크 근거 |
| 연구-운영 gap 설명 | notebook/prototype 성능과 production system 신뢰성의 차이를 강조 | W14 deployment risk 핵심 |
| 데이터 의존성 강조 | feature schema, data quality, drift, feedback loop가 모델 실패를 유발함을 정리 | AI supply chain의 data risk |
| 모니터링과 복구 강조 | 배포 후 metric, drift, alert, incident, rollback 체계 필요성 제시 | W14/W15 evidence chain |
| 조직·프로세스 문제 포함 | 역할·책임·협업·승인·운영 문화가 배포 성공에 중요함을 제시 | secure MLOps governance |

---

## 4. 목차별 핵심 개괄

| 목차 | 핵심 내용 | 비전공자용 이해 |
|---|---|---|
| 1. Introduction | ML 모델 배포는 단순히 학습된 모델 파일을 서버에 올리는 작업이 아니라 데이터·인프라·조직·운영을 결합하는 문제다. | 좋은 모델을 만들었다고 바로 서비스에 안전하게 쓸 수 있는 것은 아니다. |
| 2. Background | ML lifecycle, deployment, serving, monitoring, drift, feedback loop, MLOps 개념을 설명한다. | AI 모델은 배포 후에도 계속 관찰하고 관리해야 한다. |
| 3. Case Study Survey | 다양한 산업·연구 사례에서 ML 배포의 장애 요인과 패턴을 수집한다. | 실제 현장에서는 비슷한 문제가 반복된다. |
| 4. Data Challenges | 데이터 품질, schema 변화, missing values, feature drift, labeling 문제, training-serving skew를 다룬다. | 입력 데이터 형식이 조금만 바뀌어도 모델이 망가질 수 있다. |
| 5. Model and Infrastructure Challenges | 모델 serving, latency, scaling, dependency, environment mismatch, hardware/resource constraint를 정리한다. | 학습 때 잘 되던 모델도 서버 환경에서는 느리거나 불안정할 수 있다. |
| 6. Monitoring and Maintenance | drift detection, performance monitoring, alerting, retraining, rollback, incident response의 필요성을 설명한다. | 배포 후 성능이 나빠지는지 자동으로 감지해야 한다. |
| 7. Human and Organizational Factors | 개발자, 데이터 엔지니어, 운영자, 도메인 전문가 간 협업과 책임소재 문제가 중요하다. | AI 운영은 사람과 조직의 역할이 분명해야 한다. |
| 8. Lessons and Recommendations | 배포 전 검증, monitoring plan, data contract, model registry, rollback plan, documentation을 권장한다. | 배포 전에 “문제 생기면 어떻게 되돌릴지”를 정해 둬야 한다. |
| 9. Conclusion | ML 배포는 기술·데이터·조직이 결합된 시스템 문제이며, 지속적 운영 체계가 필요하다. | AI 보안은 운영 중 계속 관리되는 체계여야 한다. |

---

## 5. 핵심 이론 및 수식

> 아래 수식은 ML deployment risk와 운영 보안 평가 지표를 W14 보고서에서 설명하기 위한 표준화된 표현이다. 실제 논문의 정량식이라기보다 기말논문 운영 평가표 설계를 위한 지표다.

### 5.1 Deployment Risk

ML 배포 위험을 drift, data quality, infrastructure, monitoring gap으로 분해한다.

$$
DeploymentRisk=DriftRisk+DataQualityRisk+InfraRisk+MonitoringGap
$$

| 기호 | 의미 |
|---|---|
| $DriftRisk$ | 데이터/개념 분포 변화 위험 |
| $DataQualityRisk$ | 결측, schema break, feature 오류 위험 |
| $InfraRisk$ | serving, latency, scaling, dependency 위험 |
| $MonitoringGap$ | 운영 관측과 alert 부재 위험 |

### 보안적 의미

모델이 공격받지 않아도 운영 데이터와 환경이 바뀌면 보안·안전 실패가 발생한다.

---

### 5.2 Mean Time To Restore / Recovery

문제 발생 후 서비스 또는 모델을 안정 상태로 복구하는 데 걸린 시간이다.

$$
MTTR=t_{restore}-t_{incident}
$$

### 보안적 의미

AI 모델 장애와 보안 incident는 빠른 복구가 중요하다. rollback plan과 model registry가 없으면 MTTR이 증가한다.

---

### 5.3 Training-Serving Skew

학습 시 feature와 서비스 시 feature의 분포 또는 계산 차이다.

$$
Skew=Dist(P_{train}(X),P_{serve}(X))
$$

| 기호 | 의미 |
|---|---|
| $P_{train}(X)$ | 학습 시 입력/feature 분포 |
| $P_{serve}(X)$ | 운영 시 입력/feature 분포 |
| $Dist$ | KL divergence, PSI, Wasserstein distance 등 분포 차이 지표 |

### 보안적 의미

training-serving skew가 커지면 모델 성능이 저하되고, 공격자가 데이터 경로 차이를 악용할 가능성이 커진다.

---

### 5.4 Drift Detection Score

운영 데이터가 기준 데이터에서 얼마나 벗어났는지 측정한다.

$$
DriftScore=Dist(P_{baseline}(X),P_{current}(X))
$$

### 보안적 의미

DriftScore가 threshold를 넘으면 재평가, retraining, rollback 또는 human review가 필요하다.

---

### 5.5 Data Quality Error Rate

운영 입력 중 schema, missing value, range, type 오류가 있는 비율이다.

$$
DQErrorRate=\frac{N_{invalid\ records}}{N_{total\ records}}
$$

### 보안적 의미

데이터 품질 오류는 모델 성능 저하뿐 아니라 data poisoning, schema break, pipeline tampering 탐지 신호가 될 수 있다.

---

### 5.6 Rollback Success Rate

문제 모델에서 이전 안정 버전으로 복구에 성공한 비율이다.

$$
RollbackSuccess=\frac{N_{successful\ rollbacks}}{N_{rollback\ attempts}}
$$

### 보안적 의미

rollback은 AI 운영의 안전장치다. model registry와 deployment config provenance가 있어야 성공률이 높아진다.

---

### 5.7 Deployment Readiness Score

배포 전 readiness를 데이터·모델·인프라·모니터링·롤백 관점으로 평가한다.

$$
DeployReady=\alpha DataCheck+\beta ModelCheck+\gamma InfraCheck+\delta MonitorPlan+\eta RollbackPlan
$$

### 보안적 의미

배포 승인은 정확도 하나로 하지 말고 운영 준비도와 복구 계획까지 포함해야 한다.

---

## 6. AI 원리 70% 관점 분석

| 원리 항목 | 설명 | W14/P02에서의 의미 |
|---|---|---|
| ML Deployment | 모델을 production service로 전환 | W14 핵심 운영 문제 |
| Training-Serving Skew | 학습과 운영 feature 차이 | 성능·보안 실패 원인 |
| Data Drift | 입력 분포 변화 | monitoring 핵심 |
| Concept Drift | 입력-정답 관계 변화 | 재학습·검증 필요 |
| Feature Pipeline | 운영 feature 생성 경로 | schema break 위험 |
| Model Serving | API endpoint, latency, scaling | 인프라 운영성 |
| Monitoring | metric, drift, alert, incident 추적 | 배포 후 보안 관측 |
| Rollback | 안정 모델로 복구 | incident 대응 |

---

## 7. 보안 이슈 30% 관점 분석

| 보안 항목 | ML Deployment 관점 해석 | 대표 평가 지표 |
|---|---|---|
| 기밀성 | production data, feature store, endpoint log가 민감정보를 포함 | access log, retention policy |
| 무결성 | schema break, data contamination, misconfiguration이 모델 판단을 왜곡 | DQErrorRate, config hash |
| 가용성 | latency, scaling failure, rollback 실패가 서비스 장애로 연결 | MTTR, SLA, rollback success |
| 프라이버시 | 운영 로그와 feedback data가 개인정보를 축적할 수 있음 | privacy audit, log minimization |
| 안전성 | drift를 놓치면 잘못된 모델 판단이 장기간 유지 | DriftScore, alert delay |
| 책임성 | 배포 버전, feature version, alert, incident log가 있어야 감사 가능 | deployment evidence completeness |

---

## 8. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | production data, model endpoint, feature pipeline, feature schema, deployment config, monitoring dashboard, alert log, rollback artifact |
| 공격자/위험 목표 | drift 유발, schema break, data contamination, feature pipeline 조작, misconfiguration, monitoring 우회, feedback loop 악화 |
| 공격자/위험 능력 | 운영 입력 조작, 데이터 소스 변경, dependency/API 변경, 배포 설정 변경, 모니터링 threshold 우회, 내부자 실수 |
| 위험 경로 | feature/data 변경 → skew/drift 발생 → model endpoint 오판 → monitoring gap으로 탐지 지연 → incident 확대 |
| 방어자 능력 | data contract, schema validation, drift monitoring, canary deploy, rollback, incident response, human approval |
| 제외 범위 | 실제 운영 시스템 공격, 데이터 오염 절차, credential 탈취, 모니터링 우회 방법, 서비스 장애 유발 지원 |

---

## 9. 평가방법 및 지표

| 평가축 | 지표 | 의미 | W14/P02 활용 |
|---|---|---|---|
| 데이터 품질 | DQErrorRate, schema violation count | 운영 입력 안정성 | data risk 평가 |
| drift | DriftScore, skew distance, alert delay | 분포 변화 탐지 | monitoring 핵심 |
| 모델 성능 | online accuracy proxy, error rate, calibration | 운영 중 성능 | service quality |
| 인프라 | latency, throughput, availability | serving 안정성 | availability 평가 |
| incident 대응 | MTTR, incident count, rollback success | 복구 능력 | 운영 보안 평가 |
| 배포 준비도 | DeployReady, checklist completion | 사전 승인 조건 | governance |
| 재현성 | deployment version, feature version, model hash | 원인 분석 가능성 | W15 evidence chain |
| 사용자 영향 | false decision rate, escalation rate | downstream harm | safety 평가 |

---

## 10. 재현성 체크리스트

| 항목 | 기록해야 할 내용 |
|---|---|
| Bibliographic status | DOI 기준 서지, 로컬 PDF arXiv판 여부 |
| Model version | model ID, model hash, registry stage, baseline metric |
| Data/schema | data source, feature schema, schema version, data contract |
| Feature pipeline | feature code version, transformation config, dependency version |
| Deployment | endpoint version, rollout strategy, canary/A-B setting, config hash |
| Monitoring | drift metric, alert threshold, latency/error dashboard, owner |
| Incident response | rollback target, escalation rule, MTTR, incident template |
| Feedback loop | user feedback source, label update, retraining trigger |
| Evidence | deployment log, approval log, alert log, rollback log, postmortem |
| 한계 | 실험실 검증 결과를 production 안정성 보장으로 과장하지 않음 |

---

## 11. 논문의 고유 기여

1. ML 배포 실패를 단순 모델 성능 문제가 아니라 데이터·인프라·조직·운영의 시스템 문제로 정리한다.
2. Drift, training-serving skew, data quality, feedback loop가 실전 ML 보안과 신뢰성에 미치는 영향을 설명한다.
3. 모니터링, alerting, incident response, rollback의 필요성을 사례 기반으로 제시한다.
4. W14 P01의 MLOps practice를 실제 배포 실패 사례와 운영 요구사항으로 구체화한다.
5. RAG/LLM 서비스의 prompt, retrieval index, model endpoint, generated answer monitoring에도 직접 확장 가능하다.

---

## 12. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 사례 기반 일반화 한계 | case study survey는 도메인별 차이를 완전히 일반화하기 어렵다. | domain-specific risk table 작성 |
| 온라인 정답 부족 | production 환경에서는 즉시 ground truth가 없을 수 있다. | proxy metric과 delayed label 관리 |
| Drift 원인 불명확 | drift가 자연 변화인지 공격인지 구분이 어렵다. | drift + security event correlation 제안 |
| 모니터링 비용 | 모든 feature와 metric을 추적하면 비용과 noise가 증가한다. | critical metric 중심 alert 설계 |
| 조직 책임 문제 | 모델 개발자와 운영자 책임이 분리되면 incident 대응이 지연된다. | owner/approval/escalation matrix 작성 |
| RAG/LLM 확장 과제 | 전통 ML 배포 지표를 LLM/RAG에 그대로 적용하기 어렵다. | retrieval drift, prompt drift, hallucination monitoring 추가 |

---

## 13. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | AI 보안은 연구실 모델 평가가 아니라 production 배포 이후 drift·monitoring·rollback까지 포함해야 한다는 문제의식 |
| 2장 관련연구 | P02를 ML deployment challenge 핵심 사례 survey로 정리 |
| 3장 위협모형 | production data, feature pipeline, endpoint, monitoring dashboard, rollback artifact 보호 자산 정의 |
| 4장 연구방법 | DeploymentRisk, MTTR, DriftScore, DQErrorRate, RollbackSuccess, DeployReady 지표 설계 |
| 5장 분석 | ML deployment failure mode table과 monitoring/incident-response workflow 제시 |
| 6장 보안적 함의 | W01~W13의 공격·방어 지표를 production monitoring과 incident response로 연결 |

---

## 14. 기말논문 연결 3문장

1. W14에서 기말논문에 반영할 개념: ML deployment는 모델 파일 배포가 아니라 production data, feature pipeline, endpoint, monitoring, incident response, rollback이 결합된 운영 시스템 문제다.
2. W14에서 기말논문에 반영할 표·그림·실험: DeploymentRisk, MTTR, DriftScore, DQErrorRate, RollbackSuccess, DeployReady 수식표와 monitoring/rollback workflow를 반영한다.
3. W14가 W15 최종 논문과 연결되는 지점: W01~W13의 모든 공격·방어 실험 결과는 W14의 배포 버전, feature schema, monitoring threshold, alert log, rollback evidence와 연결되어야 최종 보고서의 재현성과 실무성이 확보된다.

---

## 15. 최종 판단

P02는 W14의 실전 배포 핵심 문헌이다. 좋은 모델보다 중요한 것은 운영 중 관측 가능하고, drift를 탐지할 수 있으며, 문제가 생기면 빠르게 rollback 가능한 모델이다. 따라서 기말논문에서는 P02를 **ML deployment risk, drift/monitoring, training-serving skew, incident response, rollback, production evidence chain의 중심 근거 문헌**으로 사용하는 것이 적절하다.

---

## 16. 변환 호환성 메모

```bash
pandoc P02_summary.md -o P02_summary.docx
pandoc P02_summary.md -o P02_summary.pdf --pdf-engine=xelatex
```
