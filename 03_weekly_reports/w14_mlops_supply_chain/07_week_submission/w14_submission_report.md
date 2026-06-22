# W14 제출용 보고서

## 1. 표지

| 항목 | 내용 |
|---|---|
| 주차 | W14 |
| 보고서 제목 | MLOps/DevOps·데이터/모델 파이프라인·공급망 보안 |
| 작성일 | 2026-06-22 |
| 문서 상태 | 제출용 통합본 |
| 최종 보고서 | `06_report/final/integrated_report_final.md` |
| 실험 근거 | `04_experiment/outputs/run_log.md` |
| 발표자료 | `09_presentation/` |

## 2. 초록과 키워드

본 보고서는 MLOps/DevOps, data/model pipeline, monitoring, drift detection을 AI 원리로 정리하고, ML supply chain, artifact tampering, logging/update attack surface를 보안 이슈로 분석한다. Synthetic toy MLOps pipeline 실험에서는 dataset hash, model hash, config hash, re-run consistency, drift score, audit coverage, artifact inventory를 산출했다. 실행 결과 baseline accuracy는 0.925000, F1은 0.923077, drift score는 0.307626, audit coverage와 inventory coverage는 각각 1.000000이었다.

키워드: MLOps, ML Supply Chain, Artifact Integrity, Drift Monitoring, Auditability, AI BOM

## 3. AI 원리 70%와 보안 이슈 30%

| 구분 | 핵심 내용 |
|---|---|
| AI 원리 70% | MLOps lifecycle, DevOps와 MLOps의 차이, data/model pipeline, model registry, monitoring, drift detection, AIOps, edge deployment |
| 보안 이슈 30% | data pipeline poisoning, model artifact tampering, dependency risk, unsafe update, log leakage, drift 미탐지, audit trail 부재 |

MLOps 보안 평가는 모델 성능만으로 충분하지 않다. 어떤 데이터와 config에서 모델이 만들어졌는지, 모델 artifact가 바뀌지 않았는지, 운영 입력 분포가 달라졌는지, 사고 후 추적 가능한 로그가 있는지를 함께 봐야 한다.

## 4. 논문 5편 요약과 DOI/URL 검증 상태

| ID | 논문 | 핵심 역할 | DOI/URL 상태 |
|---|---|---|---|
| P01 | A Multivocal Review of MLOps Practices, Challenges and Open Issues | MLOps practice와 challenge taxonomy | 부분 확인 |
| P02 | Challenges in Deploying Machine Learning: a Survey of Case Studies | production deployment workflow의 난점 | 확인 |
| P03 | A Systematic Survey on MLOps and AIOps: Taxonomy, Challenges, and Future Directions | AIOps와 monitoring/incident response | 부분 확인, 로컬 PDF 대체 |
| P04 | Deep Learning with Edge Computing: A Review | edge deployment의 운영 제약 | 부분 확인, 로컬 PDF 대체 |
| P05 | Deep Learning for Software Engineering: A Survey | AI-assisted software engineering과 pipeline 보안 | 부분 확인, 로컬 PDF 대체 |

P03/P04/P05는 수업자료 DOI를 기록했지만 로컬 PDF가 대체문헌이므로 최종 논문 인용 전 공식 원문 확인이 필요하다.

## 5. Research Track

| 항목 | 내용 |
|---|---|
| 연구문제 | MLOps 파이프라인에서 보안 위협을 어떻게 분류하고, 어떤 evidence로 재현성과 책임성을 보장할 것인가 |
| 대상 시스템 | MLOps 기반 ML 서비스 파이프라인 |
| 보호 자산 | 학습 데이터, feature pipeline, config, seed, model artifact, registry, 배포 설정, 로그, 모니터링 데이터 |
| 공격자 | 내부자, 외부 공격자, 공급망 공격자, 악성 패키지 제공자 |
| 평가 지표 | Accuracy, F1, dataset hash, model hash match, re-run consistency, drift score, audit coverage, inventory coverage |
| 재현성 | seed 42, config, run log, CSV, JSON, artifact inventory 보존 |
| 제외 범위 | 실제 개인정보, 실제 운영 서비스 침해, 무단 시스템 접근, 실제 악성 패키지 배포 |

## 6. 실습/실험 실행 상태와 결과표

실험은 실행 완료 상태이며, 모든 수치는 `04_experiment/outputs/run_log.md`와 일치한다.

| 점검 항목 | 측정 지표 | 결과 | 보안 의미 |
|---|---|---:|---|
| Baseline model | Accuracy | 0.925000 | 정상 조건 기준 성능 |
| Baseline model | F1 | 0.923077 | 정상 조건 분류 균형 |
| Data versioning | Dataset hash | `sha256:b9e597bccdbde442` | 데이터 무결성 기준점 |
| Model artifact verification | Model hash match | true | 모델 아티팩트 변조 탐지 기준 |
| Re-run consistency | Model/data hash match | true | 동일 config/seed 재실행 가능성 |
| Drift monitoring | Mean standardized feature shift | 0.307626 | 입력 분포 변화 감시 |
| Drifted model | Accuracy under drift | 0.925000 | 분포 변화 조건 성능 |
| Log audit | Audit coverage | 1.000000 | 책임추적 로그 완전성 |
| Artifact inventory | Inventory coverage | 1.000000 | AI BOM/ML artifact inventory 최소 항목 충족 |

## 7. 발표용 보고서 위치

발표자료는 `09_presentation/`에 있다. 최종 발표본은 `presentation_slides.html`이며, 발표 보고서, speaker notes, Q&A, one-page handout을 함께 작성했다.

## 8. 기말논문 연결

W14는 기말논문에서 운영형 AI 시스템의 보안·재현성 보증을 위한 evidence set으로 활용할 수 있다. Dataset hash, model hash, config hash, drift score, audit coverage, artifact inventory를 최소 지표로 제안한다.

## 9. AI 활용 고지

Codex를 사용해 공통 지침 확인, 로컬 PDF 메타데이터 대조, synthetic toy 실험 코드 작성과 실행, 보고서·제출본·발표자료 작성을 수행했다. 최종 내용, 인용, 실험결과, 연구윤리 책임은 작성자에게 있다.

## 10. 제출 전 점검

| 점검 항목 | 상태 |
|---|---|
| 실험 수치와 outputs 일치 | 완료 |
| 개인정보 사용 없음 | 완료 |
| 실제 서비스 공격 없음 | 완료 |
| DOI 임의 생성 없음 | 완료 |
| 대체 PDF 상태 표시 | 완료 |
| AI 활용 고지 포함 | 완료 |
| P03/P04/P05 공식 원문 확인 | 확인 필요 |
