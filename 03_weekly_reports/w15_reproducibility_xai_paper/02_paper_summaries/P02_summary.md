# P02 Summary

## Assuring the Machine Learning Lifecycle: Desiderata, Methods, and Challenges — Rob Ashmore, Radu Calinescu, Colin Paterson, ACM Computing Surveys, 2021/2022

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W15 Reproducibility, XAI & Final Paper Bridge |
| 논문명 | Assuring the Machine Learning Lifecycle: Desiderata, Methods, and Challenges |
| 저자 | Rob Ashmore, Radu Calinescu, Colin Paterson |
| 공식 출판 정보 | ACM Computing Surveys, Vol. 54, Issue 5, Article 111, pp. 1–39, 2021/2022 |
| DOI | https://doi.org/10.1145/3453444 |
| 로컬 PDF | `01_papers/pdf/02_Ashmore_Calinescu_Paterson_2021_Assuring_ML_Lifecycle.pdf` |
| 검증 상태 | W15 `doi_check.md`와 `paper_list.md` 기준 공식 DOI 확인. 로컬 PDF는 White Rose accepted version으로 기록되어 있으므로 최종 인용은 ACM DOI 기준으로 정리 |
| PDF 확인 메모 | repo의 PDF 폴더에 P02 관련 PDF blob이 존재함을 확인했다. 요약은 로컬 PDF 경로와 W15 `doi_check.md` 및 `paper_list.md`의 공식 DOI 메타데이터 기준으로 보완했다. |
| 핵심 근거 사용 가능 여부 | 가능. W15에서 ML lifecycle assurance, data/model/deployment evidence, reproducibility, assurance case, requirements coverage, lifecycle risk, AI 활용 고지, 최종 논문 evidence chain의 중심 문헌으로 사용 |

---

## 1. 한 문장 요약

이 논문은 machine learning lifecycle의 assurance를 **requirements, data management, model learning, model verification, validation, explainability, robustness, safety, deployment, monitoring, change management, evidence chain, assurance case, lifecycle governance, uncertainty, reproducibility** 관점에서 정리하며, W15에서 최종 논문의 모든 주장과 실험 결과를 **문헌 근거·데이터 버전·코드·환경·설정·출력·검증 로그·AI 활용 고지**로 연결해야 한다는 기준을 제공하는 핵심 문헌이다.

---

## 2. 핵심 연구문제

> ML 시스템은 전통 소프트웨어와 달리 데이터 의존성, 통계적 불확실성, 분포 변화, 재학습, 모델 해석 가능성 부족, 운영 중 drift 때문에 assurance가 어렵다. 따라서 신뢰 가능한 ML 시스템을 만들려면 데이터 수집부터 배포 이후 모니터링까지 전 생명주기에 걸친 요구사항, 증거, 검증 방법, 한계, 책임소재를 연결해야 한다.

| 번호 | 연구질문 |
|---|---|
| RQ1 | ML lifecycle에서 assurance를 위해 어떤 desiderata, 즉 데이터·모델·검증·배포·운영 요구사항이 필요한가? |
| RQ2 | 데이터셋, 학습 코드, 모델 artifact, 검증 결과, 배포 로그는 어떻게 evidence chain으로 연결되어야 하는가? |
| RQ3 | ML 모델의 불확실성, drift, robustness, explainability, safety claim은 어떤 evidence 없이는 과장될 수 있는가? |
| RQ4 | 전통 소프트웨어 assurance 방법을 ML 시스템에 적용할 때 어떤 한계와 보완 방법이 필요한가? |
| RQ5 | 기말논문에서 AI 활용 고지, reference verification, 실험 로그, 재현성 표를 assurance case처럼 구성하려면 어떤 구조가 필요한가? |

---

## 3. 논문의 핵심 기여

| 기여 | 설명 | W15 연결 |
|---|---|---|
| ML lifecycle assurance 체계화 | 데이터, 학습, 검증, 배포, 운영 전 단계에서 assurance 요구사항을 정리 | W15 evidence chain 핵심 |
| Desiderata 제시 | 신뢰성, 안전성, 설명가능성, 강건성, 재현성, traceability 등 요구조건을 체계화 | 기말논문 평가 기준 |
| Evidence 중심 관점 | ML claim은 실험 결과만이 아니라 데이터·코드·모델·운영 증거와 함께 제시되어야 함 | 최종 제출 검증표 |
| 방법과 도전과제 비교 | verification, validation, testing, monitoring, assurance case, runtime evidence의 한계 제시 | W14/W15 연결 |
| 지속적 assurance 강조 | 배포 후 drift와 model update까지 assurance 범위에 포함 | MLOps와 최종논문 재현성 연결 |

---

## 4. 목차별 핵심 개괄

| 목차 | 핵심 내용 | 비전공자용 이해 |
|---|---|---|
| 1. Introduction | ML 시스템은 데이터 기반으로 학습되므로 전통 소프트웨어와 다른 assurance 문제가 있다. | AI는 코드만 검토해서 안전하다고 말하기 어렵다. 데이터와 학습 과정까지 봐야 한다. |
| 2. ML Lifecycle | 요구사항, 데이터 수집, 전처리, 학습, 검증, 배포, 모니터링, 업데이트 단계가 연결된다. | AI 모델의 출생부터 운영 후 관리까지 전체 과정을 추적해야 한다. |
| 3. Assurance Desiderata | safety, robustness, fairness, explainability, privacy, reliability, traceability, reproducibility 등 요구사항을 정리한다. | 믿을 수 있는 AI에는 여러 조건이 필요하다. |
| 4. Data Assurance | 데이터 품질, representativeness, bias, labeling, provenance, privacy를 검토해야 한다. | 잘못된 데이터로 학습하면 좋은 모델처럼 보여도 위험하다. |
| 5. Model Assurance | 학습 과정, architecture, hyperparameter, verification, validation, uncertainty, robustness를 기록한다. | 모델이 왜 그런 결과를 냈는지와 어떤 조건에서만 믿을 수 있는지 남겨야 한다. |
| 6. Deployment Assurance | 운영 환경, runtime monitoring, drift detection, incident response, update management가 필요하다. | 배포 후에도 모델이 계속 안전한지 봐야 한다. |
| 7. Assurance Cases | claim, argument, evidence 구조로 ML 시스템의 신뢰성 주장을 정리할 수 있다. | “안전하다”는 말에는 근거와 논리 구조가 따라야 한다. |
| 8. Challenges | 불확실성, distribution shift, black-box models, benchmark limitations, evidence gap, tool immaturity가 과제로 남는다. | AI는 환경이 바뀌면 성능과 안전성이 달라질 수 있다. |
| 9. Future Directions | lifecycle-wide evidence, automated assurance, trustworthy MLOps, continuous monitoring, governance가 필요하다. | 앞으로는 AI를 계속 검증하고 증거를 남기는 체계가 필요하다. |

---

## 5. 핵심 이론 및 수식

> 아래 수식은 ML lifecycle assurance와 W15 최종 논문의 evidence chain 설계를 설명하기 위한 표준화된 표현이다. 수식은 GitHub, MS Word, PDF 변환 호환성을 위해 Markdown 표 밖의 LaTeX block math로 작성한다.

### 5.1 Evidence Coverage

전체 요구사항 중 evidence로 뒷받침된 요구사항의 비율이다.

$$
Coverage_E=\frac{|R_{covered}|}{|R_{total}|}
$$

| 기호 | 의미 |
|---|---|
| $R_{covered}$ | 데이터·모델·검증·배포 증거가 연결된 요구사항 |
| $R_{total}$ | 전체 요구사항 |

### 보안적 의미

AI 보안 claim은 요구사항과 evidence가 연결되어야 한다. evidence coverage가 낮으면 주장이 과장될 수 있다.

---

### 5.2 Assurance Score

ML lifecycle의 주요 evidence를 가중합으로 요약한다.

$$
AssuranceScore=w_1DataEvidence+w_2ModelEvidence+w_3VerificationEvidence+w_4DeploymentEvidence
$$

| evidence | 의미 |
|---|---|
| $DataEvidence$ | 데이터 출처, 버전, 품질, bias, privacy 검토 |
| $ModelEvidence$ | 모델 구조, 학습 설정, checkpoint, model hash |
| $VerificationEvidence$ | test, validation, robustness, XAI, safety 평가 |
| $DeploymentEvidence$ | 배포 버전, monitoring, rollback, incident log |

### 보안적 의미

모델 성능만 좋다고 assurance가 충분한 것은 아니다. 데이터와 배포 evidence까지 있어야 한다.

---

### 5.3 Lifecycle Risk

ML lifecycle 전 단계의 위험을 합산한다.

$$
LifecycleRisk=DataRisk+TrainingRisk+VerificationRisk+DeploymentRisk+MonitoringRisk
$$

### 보안적 의미

한 단계라도 evidence gap이 크면 전체 ML 시스템 신뢰도가 낮아진다.

---

### 5.4 Traceability Completeness

요구사항, 데이터, 코드, 모델, 평가, 배포 사이의 연결이 얼마나 완전한지 측정한다.

$$
TraceComplete=\frac{|Links_{verified}|}{|Links_{required}|}
$$

| 연결 예 | 설명 |
|---|---|
| requirement ↔ metric | 요구사항을 어떤 지표로 검증했는지 |
| data ↔ model | 어떤 데이터로 어떤 모델을 학습했는지 |
| code ↔ artifact | 어떤 commit으로 어떤 artifact가 생성되었는지 |
| model ↔ evaluation | 어떤 모델 버전을 어떤 평가로 검증했는지 |
| deployment ↔ monitoring | 어떤 배포가 어떤 운영 로그와 연결되는지 |

---

### 5.5 Reproducibility Score

실험과 평가를 재현하는 데 필요한 artifact가 얼마나 확보되었는지 평가한다.

$$
ReproScore=\frac{|Artifacts_{available}|}{|Artifacts_{required}|}
$$

### 보안적 의미

재현성이 없으면 성능 주장, robustness 주장, XAI 해석, safety claim을 검증하기 어렵다.

---

### 5.6 Assurance Case Validity

claim, argument, evidence가 모두 연결된 비율이다.

$$
CaseValidity=\frac{|Claims_{supported}|}{|Claims_{total}|}
$$

### 보안적 의미

논문에서 주장하는 모든 항목은 근거 문헌, 실험 로그, 표, 수식, 한계 중 하나 이상과 연결되어야 한다.

---

### 5.7 AI Disclosure Completeness

AI 도구 사용 사실이 필요한 항목에 얼마나 명시되었는지 평가한다.

$$
AIDisclosure=\frac{|AIUse_{disclosed}|}{|AIUse_{actual}|}
$$

### 보안적 의미

생성형 AI를 요약, 번역, 코드, 그림, 표 작성에 사용했다면 최종 보고서에 사용 범위와 검토 방법을 기록해야 한다.

---

## 6. AI 원리 70% 관점 분석

| 원리 항목 | 설명 | W15/P02에서의 의미 |
|---|---|---|
| ML Lifecycle | 요구사항→데이터→학습→검증→배포→운영 | assurance 범위 |
| Data Evidence | 데이터 출처·품질·편향·프라이버시 근거 | 데이터 신뢰성 |
| Model Evidence | 모델 구조·학습 설정·checkpoint·hash | 모델 추적성 |
| Verification | 테스트, 검증, robustness, XAI, safety 평가 | 검증 근거 |
| Assurance Case | claim-argument-evidence 구조 | 논문 주장 구조화 |
| Traceability | 요구사항과 artifact 사이 연결 | 재현성·감사성 |
| Continuous Monitoring | 배포 후 drift·성능·안전 감시 | 운영 assurance |
| Governance | 승인, 책임, 문서화, AI 활용 고지 | 최종 제출 기준 |

---

## 7. 보안 이슈 30% 관점 분석

| 보안 항목 | ML Lifecycle Assurance 관점 해석 | 대표 평가 지표 |
|---|---|---|
| 기밀성 | 데이터, 모델, 로그, 평가 결과가 민감정보를 포함할 수 있음 | access log, PII scan, retention policy |
| 무결성 | 데이터 오염, 코드 변경, 모델 artifact 변조, 로그 변조가 claim을 훼손 | checksum, provenance, approval log |
| 가용성 | 배포 후 drift·incident·rollback 실패가 서비스 안정성을 낮춤 | monitoring coverage, MTTR |
| 프라이버시 | training data와 raw output이 개인정보를 노출할 수 있음 | privacy evidence, DP/MIA check |
| 안전성 | 검증되지 않은 모델 claim은 downstream harm으로 연결 | safety evidence, failure case log |
| 책임성 | claim, evidence, AI 사용 고지, reference verification이 연결되어야 감사 가능 | CaseValidity, AIDisclosure, ReproScore |

---

## 8. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | dataset, label, preprocessing code, training code, model artifact, verification evidence, deployment log, monitoring log, AI disclosure, final paper claim |
| 공격자/위험 목표 | evidence gap 은폐, 실험 재현 실패, 데이터/모델 provenance 누락, unverifiable claim, AI 사용 미고지, reference mismatch |
| 공격자/위험 능력 | cherry-picking, incomplete logging, hidden data preprocessing, undocumented model version, prompt/config 누락, PDF/DOI mismatch 방치 |
| 위험 경로 | 불완전한 데이터/코드/모델 기록 → 평가 결과 재현 불가 → claim 검증 실패 → 최종논문 신뢰도 하락 |
| 방어자 능력 | evidence chain, DOI verification, artifact hash, run log, config lock, AI disclosure, limitation table, review checklist |
| 제외 범위 | 실제 시스템 공격 절차, 데이터 변조 절차, 로그 삭제 방법, 허위 DOI 작성, AI 사용 은폐 지원 |

---

## 9. 평가방법 및 지표

| 평가축 | 지표 | 의미 | W15/P02 활용 |
|---|---|---|---|
| Evidence coverage | Coverage_E | 요구사항 근거 충족도 | 핵심 평가 |
| Assurance | AssuranceScore, CaseValidity | claim-argument-evidence 품질 | 최종논문 주장 검증 |
| Traceability | TraceComplete | 요구사항-데이터-모델-평가-배포 연결 | evidence chain |
| 재현성 | ReproScore | artifact 확보 수준 | W15 핵심 |
| Lifecycle risk | LifecycleRisk | 전 단계 위험 수준 | 보안 평가 |
| AI 활용 고지 | AIDisclosure | 생성형 AI 사용 투명성 | 제출 윤리 |
| 참고문헌 검증 | DOI match rate, reference mismatch count | 문헌 신뢰성 | 허위 인용 방지 |
| 운영 증거 | monitoring coverage, deployment log completeness | 배포 후 assurance | W14 연결 |

---

## 10. 재현성 체크리스트

| 항목 | 기록해야 할 내용 |
|---|---|
| Bibliographic status | DOI 기준 서지, accepted version 여부, 로컬 PDF 판본 상태 |
| Requirement | 연구문제, 평가 요구사항, 보안 요구사항, acceptance criterion |
| Data | dataset version, source, preprocessing, split, label policy, privacy check |
| Code | Git commit, dependency lock, script hash, Docker/uv/conda environment |
| Model | architecture, hyperparameter, seed, checkpoint, model hash |
| Evaluation | metric, test set, prompt, output, XAI result, safety/robustness result |
| Deployment | model registry, deployment config, monitoring log, rollback plan |
| Evidence | run log, result table, figure source, raw output, error case, limitation note |
| AI disclosure | 사용한 AI 도구, 사용 범위, 사람이 검토한 항목, 수정 내역 |
| Reference verification | DOI/URL, 공식 출판정보, 로컬 PDF 차이, 허위 인용 방지 메모 |

---

## 11. 논문의 고유 기여

1. ML lifecycle 전반에서 assurance가 필요한 항목을 desiderata, methods, challenges로 체계화한다.
2. 데이터·모델·검증·배포·운영 evidence가 연결되어야 신뢰 가능한 ML claim이 된다는 관점을 제공한다.
3. 전통 software assurance와 ML assurance의 차이를 설명하고, uncertainty와 drift를 포함한 지속적 assurance 필요성을 강조한다.
4. W15 최종논문에서 claim-argument-evidence 구조, reference verification, run log, AI disclosure를 결합하는 근거가 된다.
5. W01~W14의 개별 공격·방어·운영 지표를 하나의 재현성·감사 가능성 체계로 묶는 중심 문헌이다.

---

## 12. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| Accepted version | 로컬 PDF는 accepted version이므로 최종 인용은 DOI/ACM metadata 기준으로 유지해야 한다. | DOI 기준 서지 사용 |
| Assurance 범위 과대 | 모든 assurance를 완전 자동화하기 어렵다. | 핵심 claim 중심 evidence 우선순위 설정 |
| Evidence 비용 | 모든 로그와 artifact를 보존하면 비용과 관리 부담이 커진다. | 필수 evidence와 선택 evidence 구분 |
| Drift와 업데이트 | 배포 후 모델과 데이터가 바뀌면 기존 assurance가 약화된다. | continuous monitoring과 update log 반영 |
| XAI 한계 | 설명가능성 결과도 불완전하고 오해될 수 있다. | XAI evidence와 limitation 병기 |
| AI 사용 투명성 | 생성형 AI 활용 범위를 기록하지 않으면 연구 윤리와 재현성 문제가 생긴다. | AI disclosure table 추가 |

---

## 13. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | AI 보안 연구는 개별 성능 결과가 아니라 lifecycle-wide assurance와 evidence chain이 필요하다는 문제의식 |
| 2장 관련연구 | P02를 ML lifecycle assurance 핵심 문헌으로 정리 |
| 3장 위협모형 | dataset, model artifact, verification evidence, deployment log, final paper claim 보호 자산 정의 |
| 4장 연구방법 | Coverage_E, AssuranceScore, LifecycleRisk, TraceComplete, ReproScore, CaseValidity, AIDisclosure 지표 설계 |
| 5장 분석 | claim-argument-evidence table과 W01~W15 evidence chain matrix 제시 |
| 6장 보안적 함의 | 재현성 실패, 허위 인용, AI 활용 미고지, evidence gap, lifecycle drift의 위험 해석 |
| 부록 | reference verification, AI disclosure, run log, artifact table, limitation table 수록 |

---

## 14. 기말논문 연결 3문장

1. W15에서 기말논문에 반영할 개념: ML assurance는 데이터, 모델, 검증, 배포, 모니터링 evidence가 요구사항과 연결될 때 성립하며, 단순 성능 수치만으로는 신뢰 가능한 claim이 되기 어렵다.
2. W15에서 기말논문에 반영할 표·그림·실험: Coverage_E, AssuranceScore, LifecycleRisk, TraceComplete, ReproScore, CaseValidity, AIDisclosure 수식표와 claim-argument-evidence matrix를 반영한다.
3. W15 최종 제출과 연결되는 지점: 모든 논문 주장에는 DOI 검증, 실험 로그, 코드·데이터·모델 버전, prompt/config, raw output, AI 활용 고지, 한계 메모가 연결되어야 최종 보고서의 재현성과 신뢰성이 확보된다.

---

## 15. 최종 판단

P02는 W15의 evidence chain 핵심 문헌이다. 최종 기말논문에서 성능, 보안성, XAI, RAG 평가, MLOps 운영 통제를 주장하려면 각 주장마다 문헌 근거, 실험 로그, 설정값, artifact hash, raw output, reference verification, AI 활용 고지가 따라야 한다. 따라서 P02는 **ML lifecycle assurance, claim-argument-evidence 구조, 재현성 체크리스트, 최종 제출 검증표의 중심 근거 문헌**으로 사용하는 것이 적절하다.

---

## 16. 변환 호환성 메모

```bash
pandoc P02_summary.md -o P02_summary.docx
pandoc P02_summary.md -o P02_summary.pdf --pdf-engine=xelatex
```
