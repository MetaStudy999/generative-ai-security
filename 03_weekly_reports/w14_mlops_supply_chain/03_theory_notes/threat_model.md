# 위협모형

| 항목 | 내용 |
|---|---|
| 대상 시스템 | MLOps 기반 ML 서비스 파이프라인 |
| 보호 자산 | 학습 데이터, feature pipeline, 학습 코드, config, seed, model artifact, model registry, 배포 설정, 로그, 모니터링 데이터 |
| 공격자 | 내부자, 외부 공격자, 공급망 공격자, 악성 패키지 제공자, 권한을 오남용하는 운영 참여자 |
| 공격자의 지식 | White-box, Gray-box, Black-box 조건을 구분하되 본 주차 실습은 공격 재현이 아니라 통제항목 점검에 한정 |
| 공격자의 능력 | 데이터 오염, 코드 변경, 의존성 조작, 모델 artifact 변조, 배포 설정 변경, 로그 삭제 또는 누락 유도 |
| 공격 경로 | 데이터 파이프라인, Git/CI, 학습 job, artifact registry, deployment manifest, serving endpoint, monitoring/logging 시스템 |
| 공격 성공 조건 | 오염된 모델 배포, hash 불일치 미탐지, drift 미탐지, rollback 불가, 감사 로그 부재, 서비스 장애 |
| 방어자 가정 | 버전관리, 접근통제, hash 검증, artifact inventory, audit log, drift monitoring, human approval gate를 적용할 수 있음 |
| 제외 범위 | 실제 운영 서비스 침해, 무단 시스템 접근, 실제 악성 패키지 배포, 실제 개인정보 사용, 공격 payload 제공 |

## 연구문제 후보

RQ1. MLOps 파이프라인의 데이터 수집, 학습, 배포, 모니터링 단계에서 발생하는 보안 위협은 어떻게 분류할 수 있는가?

RQ2. 연구용 ML 실험과 운영용 ML 시스템 사이의 보안·재현성·평가 격차는 어떤 방식으로 줄일 수 있는가?

RQ3. ML 공급망 보안을 위해 어떤 로그, 메타데이터, 검증 절차, assurance case가 필요한가?

## W14 toy 실험에서의 제한된 구현

| 통제항목 | 구현 방식 | 결과 |
|---|---|---|
| 데이터 무결성 | synthetic train/test/drift dataset hash 계산 | `sha256:b9e597bccdbde442` |
| 모델 무결성 | model artifact payload hash 계산 | model hash match true |
| 재현성 | 동일 config/seed 재실행 후 hash 비교 | re-run consistency true |
| Drift 감시 | 평균 표준화 feature shift 계산 | drift score 0.307626, threshold 0.25 초과 |
| 감사 가능성 | 필수 감사 필드 10개 기록 여부 점검 | audit coverage 1.000000, toy 필드 보존률 |
| Artifact inventory | dataset/model/config/run log 최소 항목 기록 | inventory coverage 1.000000, toy 최소 항목 충족률 |

## 안전 경계

이 위협모형은 교육용 보안 평가 설계다. 실제 시스템 침해 절차, 무단 접근 방법, 악성 패키지 배포 방법, 실제 개인정보 처리 절차는 포함하지 않는다.

Drift score 0.307626은 synthetic reference distribution과 drifted sample distribution 사이의 평균 표준화 feature shift이며, 실제 운영 장애 확률 또는 공격 성공률이 아니다. Audit coverage와 inventory coverage는 toy evidence coverage일 뿐 실제 기업 감사 완전성이나 완전한 AI BOM을 의미하지 않는다.
