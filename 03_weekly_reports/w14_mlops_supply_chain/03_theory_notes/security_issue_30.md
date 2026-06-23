# 보안 이슈 30% 정리

## 1. 주요 보안 이슈

W14의 보안 초점은 ML supply chain과 deployment/update/logging attack surface다. 모델 성능을 공격하는 절차를 재현하기보다, 운영형 ML 시스템에서 보호해야 할 자산과 통제항목을 식별한다.

- 데이터 파이프라인 오염: 학습 데이터, feature, label, split이 바뀌어도 추적하지 못하는 문제
- 모델 아티팩트 변조: registry 또는 배포 폴더의 모델 파일이 검증 없이 교체되는 문제
- Config/seed 누락: 같은 실험을 재실행할 수 없어 결과 검증이 불가능해지는 문제
- 의존성 패키지 취약점: 빌드 환경과 패키지 출처가 통제되지 않는 문제
- 모델 배포 취약점: 승인되지 않은 모델 update, rollback 실패, 배포 설정 오류
- 로그와 모니터링 데이터 노출: 운영 telemetry가 민감정보 또는 시스템 내부 상태를 노출하는 문제
- Drift detection 실패: 데이터 분포 변화나 환경 변화를 놓쳐 위험한 모델을 계속 사용하는 문제
- Assurance case 부재: 어떤 근거로 안전하고 재현 가능하다고 말하는지 설명하지 못하는 문제

## 2. CIA 관점 분석

| 관점 | 관련 위협 | 설명 |
|---|---|---|
| Confidentiality | Log leakage / model artifact exposure | 로그, monitoring data, model artifact가 내부 상태나 민감 단서를 노출할 수 있다. |
| Integrity | Data pipeline poisoning / model artifact tampering | 데이터, config, 모델 파일이 바뀌면 결과와 배포 모델의 신뢰성이 무너진다. |
| Availability | Deployment failure / pipeline disruption | 잘못된 update, rollback 실패, incident response 지연은 서비스 중단으로 이어진다. |
| Privacy | Monitoring data leakage | 운영 telemetry가 실제 사용자 입력이나 행동 패턴을 포함할 수 있다. |
| Safety | Unsafe model update / drift undetected | 입력 분포가 변했는데도 모델을 계속 사용하면 안전하지 않은 출력이 발생할 수 있다. |
| Accountability | Missing audit trail / weak assurance case | 사고 후 누가, 언제, 어떤 artifact를 배포했는지 설명할 수 없게 된다. |

## 3. 공격-방어-평가 분류

| 구분 | 내용 |
|---|---|
| 공격 자산 | 데이터셋, feature pipeline, 학습 코드, config, model artifact, registry, deployment manifest, logs |
| 공격자 능력 | 데이터 변경, 코드 변경, 의존성 조작, 모델 파일 교체, 로그 삭제, 승인 절차 우회 |
| 방어 방법 | hash 검증, artifact inventory, 접근통제, 승인 gate, monitoring, rollback, audit log, human review |
| 평가 지표 | dataset hash, model hash match, re-run consistency, drift score, audit coverage, inventory coverage |

## 4. W14 toy 실험의 보안 해석

이번 실행은 실제 공격 절차가 아니라 통제항목의 최소 구현이다. Dataset hash와 model hash는 무결성 기준점을 만들고, re-run consistency=true는 같은 seed/config로 결과를 다시 만들 수 있음을 보인다. Drift score 0.307626은 운영 입력 분포 변화 감시가 필요함을 보여주지만 공격 성공률이나 실제 운영 장애 확률이 아니다. Audit coverage 1.000000과 inventory coverage 1.000000은 toy 필수 필드 충족률이며 실제 기업 감사 완전성이나 완전한 AI BOM을 의미하지 않는다.

## 5. 기말 논문 연결

W14 보안 이슈는 기말 논문의 방법론 장에서 "운영형 AI 시스템 보안 평가표"로 발전시킨다. 평가표는 공격 절차보다 데이터·모델·config·로그의 provenance와 검증 가능성을 중심에 둔다.
