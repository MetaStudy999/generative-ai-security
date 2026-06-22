# W14 MLOps/DevOps·데이터/모델 파이프라인·공급망 보안 통합보고서

## 0. 메타정보

| 항목 | 내용 |
|---|---|
| 주차 | W14 |
| 주제 | MLOps/DevOps·데이터/모델 파이프라인·공급망 보안 |
| AI 원리 | MLOps, DevOps, data/model pipeline, monitoring, drift, AIOps, edge deployment |
| 보안 이슈 | ML supply chain, data pipeline poisoning, model artifact tampering, deployment/update/logging attack surface |
| 문서 상태 | 최종본 |
| 실험 근거 | `04_experiment/outputs/run_log.md` |
| 작성일 | 2026-06-22 |

## 1. 한 문장 요약

W14는 ML 모델을 연구실 결과가 아니라 운영 파이프라인의 산출물로 보고, 데이터·모델·config·로그·모니터링을 함께 검증해야 AI 공급망 보안과 재현성을 설명할 수 있음을 정리한다.

## 2. AI 원리 70% 정리

MLOps는 ML, software engineering, data engineering, operations를 연결하는 생명주기 관리 방식이다. DevOps가 코드의 빌드와 배포 자동화에 초점을 둔다면, MLOps는 데이터와 모델이 계속 바뀐다는 특성 때문에 dataset version, feature pipeline, model registry, experiment tracking, drift monitoring, rollback, governance를 추가로 요구한다.

| 개념 | W14에서의 의미 |
|---|---|
| MLOps lifecycle | 데이터 준비, 학습, 검증, artifact 등록, 배포, monitoring, 재학습의 반복 구조 |
| Data/model pipeline | 데이터와 모델 산출물이 어떤 config, seed, code, 환경에서 만들어졌는지 추적하는 구조 |
| Monitoring/drift | 운영 입력과 출력 분포가 기준과 달라졌는지 감시하는 절차 |
| AIOps | 운영 telemetry를 이용해 incident detection, failure prediction, RCA, response를 보조하는 영역 |
| Edge deployment | AI가 cloud 밖 edge node/device로 확장될 때 artifact와 update 관리가 더 중요해지는 배포 형태 |

## 3. 보안 이슈 30% 정리

W14의 보안 이슈는 공격 절차 재현이 아니라 운영 파이프라인의 보호 자산과 통제항목 정의다. 핵심 위협은 데이터 파이프라인 오염, 모델 artifact 변조, 의존성 취약점, 무단 update, drift 미탐지, 로그 누락 또는 로그 노출이다.

| 관점 | 관련 위협 | 통제항목 |
|---|---|---|
| Confidentiality | log leakage, model artifact exposure | 로그 최소화, 접근통제 |
| Integrity | data poisoning, artifact tampering | dataset hash, model hash, approval gate |
| Availability | deployment failure, rollback failure | 배포 기록, rollback plan, incident log |
| Privacy | monitoring data leakage | telemetry masking, synthetic 실험 원칙 |
| Safety | unsafe model update, drift undetected | drift score, human review |
| Accountability | missing audit trail | audit coverage, artifact inventory |

## 4. 논문 5편 요약

| ID | 논문 | 핵심 역할 | DOI/URL 검증 상태 |
|---|---|---|---|
| P01 | A Multivocal Review of MLOps Practices, Challenges and Open Issues | MLOps practice, challenge, artifact/governance/security 항목 정리 | 부분 확인 |
| P02 | Challenges in Deploying Machine Learning: a Survey of Case Studies | 연구용 모델과 production deployment workflow의 격차 설명 | 확인 |
| P03 | A Systematic Survey on MLOps and AIOps: Taxonomy, Challenges, and Future Directions | monitoring, incident response, AIOps taxonomy 연결 | 부분 확인, 로컬 PDF 대체 |
| P04 | Deep Learning with Edge Computing: A Review | edge deployment의 latency, privacy, resource, update 제약 설명 | 부분 확인, 로컬 PDF 대체 |
| P05 | Deep Learning for Software Engineering: A Survey | AI-assisted software engineering과 DevOps/MLOps pipeline 연결 | 부분 확인, 로컬 PDF 대체 |

## 5. 논문 5편 비교

P01/P02는 MLOps와 deployment workflow의 큰 구조를 제공하고, P03은 운영 telemetry와 incident response, P04는 edge 배포 구조, P05는 개발 pipeline 내부의 AI 활용을 설명한다. 다섯 편을 합치면 W14의 핵심 결론은 `data/model/config/log/artifact`의 traceability 없이는 운영형 AI 시스템 보안을 주장하기 어렵다는 것이다.

## 6. Research Track

### 6.1 연구문제

RQ1. MLOps 파이프라인의 데이터 수집, 학습, 배포, 모니터링 단계에서 발생하는 보안 위협은 어떻게 분류할 수 있는가?

RQ2. 연구용 ML 실험과 운영용 ML 시스템 사이의 보안·재현성·평가 격차는 어떤 방식으로 줄일 수 있는가?

RQ3. ML 공급망 보안을 위해 어떤 로그, 메타데이터, 검증 절차, assurance case가 필요한가?

### 6.2 위협모형

대상 시스템은 MLOps 기반 ML 서비스 파이프라인이다. 보호 자산은 학습 데이터, feature pipeline, 학습 코드, config, seed, model artifact, registry, 배포 설정, 로그, 모니터링 데이터다. 공격자는 내부자, 외부 공격자, 공급망 공격자, 악성 패키지 제공자, 권한을 오남용하는 운영 참여자로 둔다.

### 6.3 평가방법

| 평가 항목 | 지표 | 이번 실행 결과 |
|---|---|---:|
| Baseline Utility | Accuracy / F1 | 0.925000 / 0.923077 |
| Pipeline Integrity | Dataset/model/config hash | dataset `sha256:b9e597bccdbde442`, model hash match true |
| Reproducibility | Re-run consistency | true |
| Drift Detection | Mean standardized feature shift | 0.307626 |
| Auditability | Audit coverage | 1.000000 |
| Supply Chain Risk | Inventory coverage | 1.000000 |

### 6.4 재현성

Dockerfile, pyproject.toml, config.yaml, seed 42, 실행 코드, run log, metrics CSV, results JSON을 함께 보존했다. 같은 config/seed 재실행에서 dataset/model hash가 일치해 re-run consistency는 true다.

### 6.5 한계와 오픈문제

실험은 local synthetic toy pipeline이다. 실제 registry, CI/CD, Kubernetes, package vulnerability scanner, production telemetry는 구현하지 않았다. P03/P04/P05는 대상 논문과 로컬 PDF가 달라 공식 원문 확보가 필요하다.

## 7. 실습 요약

W14 실습은 synthetic data를 생성해 toy logistic regression을 학습하고, dataset hash, config hash, model hash, drift score, audit coverage, artifact inventory를 저장했다. Drift score는 0.307626으로 threshold 0.25를 넘어 drift 감시 경보 조건을 만들었다. 이 수치는 공격 결과가 아니라 운영 감시 지표다.

## 8. AI 활용 기록 요약

Codex를 사용해 공통 지침 확인, W14 프롬프트 적용, 로컬 PDF 첫 페이지 대조, synthetic toy pipeline 코드 작성과 실행, 보고서·제출본·발표자료 작성을 수행했다. AI 산출물은 초안이며 최종 내용, 인용, 실험결과, 연구윤리 책임은 작성자에게 있다.

## 9. 토론 질문

1. AI BOM/ML artifact inventory에는 dataset, model, config, log 외에 어떤 항목이 반드시 들어가야 하는가?
2. Drift score가 threshold를 넘었을 때 자동 rollback과 human review 중 무엇을 우선해야 하는가?
3. 연구용 toy pipeline의 evidence를 실제 운영형 AI 시스템의 assurance case로 확장하려면 어떤 검증이 추가되어야 하는가?

## 10. 기말 논문 연결

W14는 기말 논문의 관련연구, 연구방법, 분석/실험, 보안적 함의 장에 반영할 수 있다. 특히 "운영형 AI 시스템 보안을 위한 최소 evidence set"으로 dataset hash, model hash, config hash, drift score, audit coverage, artifact inventory를 제안하는 근거가 된다.

## 11. 참고문헌 검증표

참고문헌 검증 상태는 `01_papers/doi_check.md`에서 관리한다. P02는 DOI가 로컬 PDF 첫 페이지와 수업자료에서 일치한다. P01은 제목을 수업 검수보고서와 PDF 첫 페이지 기준으로 보정했다. P03/P04/P05는 수업자료 DOI는 기록했지만 로컬 PDF가 대체문헌이므로 공식 원문 확보가 필요하다.

## 12. 자기 점검

| 항목 | 상태 |
|---|---|
| 논문 5편 요약 | 완료 |
| 비교표 | 완료 |
| AI 원리 70% | 완료 |
| 보안 이슈 30% | 완료 |
| Research Track | 완료 |
| 실험 실행 및 outputs 생성 | 완료 |
| 제출용 Markdown/HTML | 완료 |
| 발표 패키지 | 완료 |
| DOI 임의 생성 방지 | 완료, 수업자료 기준과 대체 PDF 상태 분리 |
| AI 활용 고지 | 완료 |
