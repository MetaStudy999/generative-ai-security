# P01 Summary

## A Multivocal Review of MLOps Practices, Challenges and Open Issues — Beyza Eken et al., ACM Computing Surveys, 2025/2026

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W14 MLOps & AI Supply Chain |
| 공식 논문명 | A Multivocal Review of MLOps Practices, Challenges and Open Issues |
| 공식 저자 | Beyza Eken, Samodha Pallewatta, Nguyen Tran, Ayse Tosun, Muhammad Ali Babar |
| 공식 출판 정보 | ACM Computing Surveys, Vol. 58, Issue 2, pp. 1–35, online 2025-09-08, print 2026-01-31 |
| DOI | https://doi.org/10.1145/3747346 |
| 보조 URL | arXiv `2406.09737` |
| 로컬 PDF | `01_papers/pdf/01_Eken_et_al_2025_MLOps_Practices_Multivocal_Review.pdf` |
| 검증 상태 | W14 `paper_list.md` 기준 DOI와 로컬 PDF/arXiv는 Beyza Eken 제목으로 일치한다. 단, 수업자료의 `Bayram Eken` 및 긴 제목 표기와 다르므로 차이 메모 유지 |
| PDF 확인 메모 | repo의 PDF 폴더에 P01 관련 PDF blob이 존재함을 확인했다. 요약은 로컬 PDF 경로와 W14 `paper_list.md`의 공식 DOI 메타데이터 기준으로 보완했다. |
| 핵심 근거 사용 가능 여부 | 가능. W14에서 MLOps lifecycle, data/model/pipeline governance, CI/CD/CT/CD, model registry, monitoring, drift, incident response, reproducibility, audit evidence, AI supply chain control의 기본 문헌으로 사용 |

---

## 1. 한 문장 요약

이 논문은 MLOps 실무와 연구 동향을 **data management, feature engineering, experiment tracking, model training, model registry, CI/CD/CT/CD, deployment, monitoring, drift detection, reproducibility, governance, collaboration, organizational maturity, security and compliance, lifecycle automation** 관점에서 다중문헌(multivocal) 방식으로 정리하며, W14에서 W01~W13의 AI 보안 공격·방어 논의를 실제 운영 가능한 **감사 가능한 AI 공급망 통제 체계**로 전환하는 핵심 배경 문헌이다.

---

## 2. 핵심 연구문제

> AI 보안은 논문 실험의 공격 성공률이나 방어 성능만으로 끝나지 않는다. 모델이 실제 서비스에 배포되려면 데이터, 코드, 모델, 환경, 실험, 승인, 배포, 모니터링, 롤백, 감사 로그가 생명주기 전체에서 연결되어야 한다. MLOps는 이 연결 구조를 제공하지만, 조직·도구·품질·보안·거버넌스 측면의 미해결 문제가 남아 있다.

| 번호 | 연구질문 |
|---|---|
| RQ1 | MLOps는 데이터 수집부터 모델 배포·모니터링·재학습까지 AI 생명주기를 어떤 단계로 구성하는가? |
| RQ2 | 모델 실험 결과를 운영 가능한 서비스로 전환할 때 재현성, 추적성, 모델 registry, 승인 절차, 배포 자동화는 왜 필요한가? |
| RQ3 | Data drift, concept drift, model degradation, security incident, rollback, audit log는 AI 보안 운영에서 어떤 역할을 하는가? |
| RQ4 | MLOps 실무에서 조직 협업, 도구 파편화, 환경 불일치, 책임 소재, compliance evidence 부족은 어떤 문제를 만드는가? |
| RQ5 | 기말논문에서 W01~W13의 공격·방어 지표를 W14/W15의 evidence chain으로 묶으려면 어떤 운영 통제 표를 설계해야 하는가? |

---

## 3. 논문의 핵심 기여

| 기여 | 설명 | W14 연결 |
|---|---|---|
| Multivocal review | 학술 문헌과 산업 실무 자료를 함께 검토해 MLOps practices와 challenges를 정리 | 실무형 AI 보안 운영 근거 |
| MLOps lifecycle 정리 | data, model, code, deployment, monitoring, governance 단계로 운영 생명주기를 체계화 | W14 핵심 구조 |
| Practice와 challenge 구분 | 자동화, registry, experiment tracking, monitoring, collaboration, reproducibility의 실무 이슈 정리 | 기말논문 통제 항목 설계 |
| Open issue 제시 | tool fragmentation, organization maturity, security/compliance, reproducibility gap, monitoring gap 등 미해결 문제 제시 | W15 재현성·감사 연결 |
| AI supply chain 연결 | 데이터·코드·모델·환경·배포 산출물의 provenance와 auditability 필요성 제시 | W14 AI 공급망 보안 프레임워크 |

---

## 4. 목차별 핵심 개괄

| 목차 | 핵심 내용 | 비전공자용 이해 |
|---|---|---|
| 1. Introduction | ML 시스템은 단순 모델 학습이 아니라 데이터·코드·모델·배포·운영이 연결된 복합 시스템이다. | AI 모델을 한 번 학습하는 것보다, 계속 안전하게 운영하는 것이 더 어렵다. |
| 2. MLOps Background | DevOps, DataOps, ModelOps, CI/CD, continuous training, monitoring, governance의 관계를 설명한다. | 소프트웨어 배포처럼 AI도 자동화와 추적 관리가 필요하다. |
| 3. Review Method | 학술 논문과 gray literature를 함께 분석해 실제 MLOps practice와 challenge를 수집한다. | 논문뿐 아니라 기업 실무 자료까지 같이 본다. |
| 4. MLOps Practices | versioning, experiment tracking, pipeline automation, model registry, deployment, monitoring, rollback, collaboration을 정리한다. | 누가 어떤 데이터와 코드로 어떤 모델을 만들고 배포했는지 기록한다. |
| 5. Challenges | 데이터 품질, 환경 재현성, 도구 파편화, drift, monitoring, governance, 조직 역할 분담 문제가 반복된다. | AI 운영이 실패하는 이유는 모델 성능만이 아니라 데이터·조직·운영 문제 때문이다. |
| 6. Security and Governance | 모델·데이터·파이프라인·배포 설정의 provenance와 audit evidence가 필요하다. | 공격을 막으려면 “무엇이 언제 어디서 바뀌었는지” 추적해야 한다. |
| 7. Open Issues | 표준화 부족, compliance evidence 부족, reproducibility gap, 책임소재 불명확, 운영 자동화 미성숙이 남아 있다. | AI 시스템을 믿으려면 표준화된 운영 증거가 필요하다. |
| 8. Future Directions | end-to-end automation, governance-by-design, monitoring maturity, secure MLOps, human-in-the-loop approval이 필요하다. | 앞으로는 AI 개발보다 안전한 운영 체계가 핵심이다. |
| 9. Conclusion | MLOps는 AI 실험을 운영 가능한 서비스와 감사 가능한 시스템으로 전환하는 핵심 프레임워크다. | AI 보안은 성능표가 아니라 운영 증거까지 포함해야 한다. |

---

## 5. 핵심 이론 및 수식

> 아래 수식은 MLOps 운영 위험과 AI 공급망 감사 지표를 W14 보고서에서 설명하기 위한 표준화된 표현이다. 실제 논문의 정량식이라기보다 기말논문 평가표 설계를 위한 운영 지표다.

### 5.1 MLOps Risk

AI 운영 위험을 데이터, 모델, 배포, 모니터링 공백으로 분해한다.

$$
MLOpsRisk=DataRisk+ModelRisk+DeploymentRisk+MonitoringGap
$$

| 기호 | 의미 |
|---|---|
| $DataRisk$ | 데이터 품질, drift, poisoning, leakage 위험 |
| $ModelRisk$ | 모델 취약성, 성능 저하, 검증 부족 위험 |
| $DeploymentRisk$ | 환경 불일치, 잘못된 설정, rollback 실패 위험 |
| $MonitoringGap$ | 운영 중 이상·drift·보안 이벤트 탐지 공백 |

### 보안적 의미

AI 보안은 모델 공격만이 아니라 데이터와 배포·운영 전 과정의 통제 실패까지 포함한다.

---

### 5.2 Audit Coverage

필수 통제 항목 중 실제 로그로 남은 항목의 비율이다.

$$
Coverage_{audit}=\frac{|Controls_{logged}|}{|Controls_{required}|}
$$

| 기호 | 의미 |
|---|---|
| $Controls_{logged}$ | 실제 evidence log가 남은 통제 항목 |
| $Controls_{required}$ | 정책상 필요한 통제 항목 |

### 보안적 의미

방어를 했다고 주장하려면 로그와 증거가 있어야 한다. audit coverage가 낮으면 사고 대응과 논문 재현성이 모두 약해진다.

---

### 5.3 Reproducibility Score

모델 재현에 필요한 산출물이 얼마나 기록되었는지 평가한다.

$$
ReproScore=\frac{|Artifacts_{available}|}{|Artifacts_{required}|}
$$

| 필수 artifact 예 | 설명 |
|---|---|
| data version | 데이터셋·전처리 버전 |
| code version | Git commit, branch, tag |
| model version | model registry ID, checksum |
| environment | Docker/conda/uv lock, CUDA, OS |
| training config | hyperparameter, seed, split |
| evaluation log | metric, test set, report |

### 보안적 의미

재현성이 낮은 모델은 감사·검증·사고 대응이 어렵다.

---

### 5.4 Drift Detection Delay

모델 성능 또는 데이터 분포 변화가 발생한 시점부터 탐지까지 걸린 시간이다.

$$
DriftDelay=t_{detected}-t_{occurred}
$$

### 보안적 의미

drift 탐지가 늦으면 잘못된 예측이 운영 환경에 오래 노출된다. 보안 관점에서는 incident detection delay와 유사하게 관리해야 한다.

---

### 5.5 Rollback Time

문제 모델을 이전 안정 버전으로 되돌리는 데 걸리는 시간이다.

$$
RollbackTime=t_{stable\ restored}-t_{incident\ confirmed}
$$

### 보안적 의미

AI 모델 배포 사고에서는 빠른 rollback이 가용성과 안전성을 지킨다. model registry와 deployment config가 없으면 rollback이 어렵다.

---

### 5.6 Pipeline Provenance Completeness

AI pipeline 단계별 provenance가 얼마나 연결되어 있는지 평가한다.

$$
ProvComplete=\frac{|Edges_{verified}|}{|Edges_{expected}|}
$$

| 기호 | 의미 |
|---|---|
| $Edges_{verified}$ | 데이터→코드→모델→배포→모니터링 사이 검증된 연결 |
| $Edges_{expected}$ | 전체 생명주기에서 기대되는 연결 |

### 보안적 의미

provenance가 끊기면 어떤 데이터와 코드가 운영 모델에 반영되었는지 추적할 수 없다. 이는 AI supply chain risk다.

---

### 5.7 Secure MLOps Readiness Score

MLOps 보안 준비도를 요약한다.

$$
SecureMLOpsScore=\alpha ReproScore+\beta Coverage_{audit}+\gamma ProvComplete-\lambda MLOpsRisk-\mu DriftDelay
$$

### 보안적 의미

안전한 AI 운영은 성능보다 evidence, provenance, monitoring, rollback 가능성의 조합으로 판단해야 한다.

---

## 6. AI 원리 70% 관점 분석

| 원리 항목 | 설명 | W14/P01에서의 의미 |
|---|---|---|
| MLOps Lifecycle | 데이터부터 배포·운영까지 ML 생명주기 관리 | W14 핵심 원리 |
| CI/CD/CT | code, deployment, training 자동화 | 운영 재현성·배포 안정성 |
| Experiment Tracking | 실험 설정·결과 기록 | 모델 검증 증거 |
| Model Registry | 모델 버전·상태·배포 이력 관리 | rollback과 ownership 추적 |
| Data/Feature Versioning | 데이터와 feature pipeline 추적 | poisoning·drift 감사 |
| Monitoring | 성능·drift·latency·오류 감시 | 운영 보안 탐지 |
| Governance | 승인·정책·책임소재 관리 | compliance evidence |
| Reproducibility | 모델 결과 재현 가능성 | W15 최종보고서 연결 |

---

## 7. 보안 이슈 30% 관점 분석

| 보안 항목 | MLOps 관점 해석 | 대표 평가 지표 |
|---|---|---|
| 기밀성 | 데이터셋, feature store, model artifact, registry 접근통제 필요 | access log, secret scanning |
| 무결성 | 데이터·코드·모델·배포 설정이 오염되면 전체 AI 결과가 훼손 | provenance, checksum, approval log |
| 가용성 | 배포 실패, drift, rollback 실패는 서비스 장애로 연결 | rollback time, MTTR, SLA |
| 프라이버시 | 학습 데이터와 monitoring log가 개인정보를 포함할 수 있음 | privacy audit, retention policy |
| 안전성 | 잘못된 모델이 운영에 남으면 downstream 피해 발생 | drift delay, incident severity |
| 책임성 | 모든 변경과 승인, 평가 결과가 evidence chain으로 남아야 함 | audit coverage, reproducibility score |

---

## 8. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | dataset, feature store, training code, pipeline config, model artifact, model registry, deployment config, monitoring log, approval log |
| 공격자 목표 | 데이터/모델 공급망 오염, 악성 모델 배포, registry 변조, monitoring 우회, rollback 방해, audit log 삭제 |
| 공격자 능력 | 내부자 권한, CI/CD 설정 변경, dependency 조작, artifact 교체, secret 탈취, log tampering |
| 공격 경로 | data/code 변경 → pipeline 실행 → model artifact 생성 → registry 등록 → deployment → monitoring gap 악용 |
| 방어자 능력 | versioning, access control, signed artifact, CI/CD policy, approval gate, drift monitoring, rollback, audit logging |
| 제외 범위 | 실제 시스템 침투, credential 탈취 절차, CI/CD 악용 코드 제공, 운영 서비스 공격 지원 |

---

## 9. 평가방법 및 지표

| 평가축 | 지표 | 의미 | W14/P01 활용 |
|---|---|---|---|
| 재현성 | ReproScore, artifact availability | 모델 재현 가능성 | W15 연결 |
| 감사성 | Coverage_audit, approval log completeness | 통제 증거 수준 | 기말논문 핵심 |
| 공급망 추적 | ProvComplete, model/data lineage | 데이터→모델→배포 추적 | AI supply chain |
| 운영 안정성 | DriftDelay, rollback time, MTTR | 사고 탐지·복구 능력 | MLOps 운영성 |
| 모델 품질 | deployment metric, monitoring metric | 운영 중 성능 유지 | service quality |
| 보안 통제 | access control, signed artifact, secret exposure | 악성 변경 방지 | secure MLOps |
| 조직 성숙도 | role clarity, approval process, ownership | 책임소재 | governance |
| 비용 | automation cost, monitoring overhead | 실무 적용성 | 운영 최적화 |

---

## 10. 재현성 체크리스트

| 항목 | 기록해야 할 내용 |
|---|---|
| Bibliographic status | DOI 기준 서지, 수업자료 표기 차이, 로컬 PDF 판본 상태 |
| Data version | dataset ID, split, preprocessing, feature version |
| Code version | Git commit, branch, dependency lock, script hash |
| Environment | OS, Python, CUDA, Dockerfile, uv/conda lock |
| Training config | hyperparameter, seed, model architecture, checkpoint |
| Evaluation | metric, test set, validation protocol, fairness/security metric |
| Registry | model ID, model hash, stage, approval status |
| Deployment | deployment target, config, rollout strategy, rollback plan |
| Monitoring | drift, latency, error, security event, alert threshold |
| Evidence | approval log, audit log, incident log, change request, report hash |

---

## 11. 논문의 고유 기여

1. MLOps를 학술·산업 실무 문헌 기반으로 폭넓게 정리한다.
2. 모델 개발과 운영 사이의 gap을 data/code/model/deployment/monitoring lifecycle로 설명한다.
3. AI 보안을 실험 성능이 아니라 운영 증거, 재현성, 모니터링, 승인 절차, rollback 가능성으로 확장한다.
4. W01~W13의 공격·방어 지표를 W14의 operational control과 W15의 reproducibility evidence chain으로 연결할 근거를 제공한다.
5. 기말논문에서 AI 보안 프레임워크를 실제 서비스 운영 프레임워크로 전환하는 중심 문헌으로 적합하다.

---

## 12. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 표기 차이 | 수업자료의 저자·제목 표기와 DOI 기준 서지에 차이가 있다. | DOI 기준으로 인용하고 차이 메모 유지 |
| 실무 자료 편향 | multivocal review는 산업 블로그·도구 문서의 편향이 있을 수 있다. | 학술 DOI와 공식 문서 중심으로 재검증 |
| 보안 통제 구체성 부족 | 일반 MLOps practice가 곧 secure MLOps는 아니다. | security control matrix를 별도 작성 |
| 조직 성숙도 차이 | 작은 팀과 대기업의 MLOps 적용 수준이 다르다. | maturity level을 구분 |
| 자동화 과신 | 자동화 pipeline도 악성 변경과 설정 오류에 취약하다. | approval gate와 signed artifact 포함 |
| 모니터링 공백 | drift와 보안 이벤트를 탐지하지 못하면 운영 중 위험이 누적된다. | drift/incident/rollback 지표 병기 |

---

## 13. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | AI 보안은 모델 성능이 아니라 생명주기 전체의 운영 증거와 공급망 통제까지 포함해야 한다는 문제의식 |
| 2장 관련연구 | P01을 MLOps practice/challenge/open issue 핵심 문헌으로 정리 |
| 3장 위협모형 | dataset, pipeline, model artifact, registry, deployment config, monitoring log 보호 자산 정의 |
| 4장 연구방법 | MLOpsRisk, Coverage_audit, ReproScore, DriftDelay, RollbackTime, ProvComplete 지표 설계 |
| 5장 분석 | secure MLOps lifecycle diagram과 AI supply chain control matrix 제시 |
| 6장 보안적 함의 | W01~W13 공격·방어 결과를 운영 통제, 승인, 모니터링, evidence chain으로 연결 |

---

## 14. 기말논문 연결 3문장

1. W14에서 기말논문에 반영할 개념: MLOps는 데이터·코드·모델·배포·모니터링·승인 로그를 연결해 AI 보안 주장을 운영 가능한 evidence chain으로 전환하는 생명주기 프레임워크다.
2. W14에서 기말논문에 반영할 표·그림·실험: MLOpsRisk, Coverage_audit, ReproScore, DriftDelay, RollbackTime, ProvComplete 수식표와 secure MLOps lifecycle diagram, AI supply chain control matrix를 반영한다.
3. W14가 W15 최종 논문과 연결되는 지점: W01~W13의 모든 공격·방어·평가 지표는 W14의 model registry, monitoring, approval, rollback, audit log에 연결되어야 최종 보고서에서 재현성과 책임성을 확보할 수 있다.

---

## 15. 최종 판단

P01은 W14의 MLOps 기본 문헌이다. AI 보안은 실험실 성능표로 끝나지 않고 데이터·코드·모델·배포·모니터링·승인·롤백 증거가 연결되어야 한다. 따라서 기말논문에서는 P01을 **secure MLOps lifecycle, AI supply chain governance, model registry/provenance, monitoring/rollback, audit evidence chain의 중심 근거 문헌**으로 사용하는 것이 적절하다.

---

## 16. 변환 호환성 메모

```bash
pandoc P01_summary.md -o P01_summary.docx
pandoc P01_summary.md -o P01_summary.pdf --pdf-engine=xelatex
```
