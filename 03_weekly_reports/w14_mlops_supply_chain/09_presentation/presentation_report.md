# W14 발표용 보고서

## 1. 발표 메타정보

| 항목 | 내용 |
|---|---|
| 주차 | W14 |
| 주제 | MLOps/DevOps·데이터/모델 파이프라인·공급망 보안 |
| 발표 시간 | 8-10분 |
| 핵심 메시지 | 운영형 AI 시스템 보안은 accuracy가 아니라 data/model/config/log/artifact evidence를 함께 요구한다. |
| 실험 근거 | `04_experiment/outputs/run_log.md` |

## 2. 한 문장 요약과 발표 흐름

W14는 ML 모델을 운영 파이프라인의 산출물로 보고, dataset hash, model hash, drift score, audit coverage, artifact inventory를 최소 evidence로 기록하는 방법을 정리한다.

발표 흐름은 `MLOps 원리 -> 공급망 보안 위협 -> 논문 5편 역할 -> toy pipeline 실험 -> 기말논문 연결` 순서로 진행한다.

## 3. 논문 5편의 발표 역할

| ID | 발표 역할 |
|---|---|
| P01 | MLOps practices와 challenge taxonomy의 큰 틀 |
| P02 | ML deployment workflow에서 연구/운영 격차 설명 |
| P03 | AIOps와 incident response, monitoring 연결 |
| P04 | edge deployment에서 artifact/update 관리가 어려워지는 이유 |
| P05 | AI-assisted software engineering이 DevOps/MLOps 공급망을 넓히는 지점 |

P03/P04/P05는 로컬 PDF가 대상 논문과 달라 공식 원문 확인이 필요하다는 점을 발표에서 명시한다.

## 4. AI 원리 70%와 보안 이슈 30%

| 구분 | 발표 포인트 |
|---|---|
| AI 원리 70% | MLOps lifecycle, data/model pipeline, monitoring, drift detection, AIOps, edge deployment |
| 보안 이슈 30% | data poisoning, artifact tampering, unsafe update, log leakage, drift 미탐지, audit gap |

핵심 설명은 "운영형 AI는 모델 파일 하나가 아니라 추적 가능한 생명주기"라는 점이다.

## 5. 실습/실험 실행 상태와 결과 근거

| 점검 항목 | 결과 | 의미 |
|---|---:|---|
| Baseline accuracy | 0.925000 | 정상 조건 기준 성능 |
| Baseline F1 | 0.923077 | 정상 조건 분류 균형 |
| Dataset hash | `sha256:b9e597bccdbde442` | 데이터 무결성 기준점 |
| Model hash match | true | 모델 artifact 변조 탐지 기준 |
| Re-run consistency | true | 동일 config/seed 재실행 가능성 |
| Drift score | 0.307626 | threshold 0.25 초과, 운영 감시 신호 |
| Audit coverage | 1.000000 | toy 필수 로그 필드 보존률 |
| Inventory coverage | 1.000000 | toy AI BOM/ML artifact inventory 최소 항목 충족률 |

Drift score 0.307626은 synthetic 기준 데이터와 drifted 데이터 사이의 평균 표준화 feature shift이며, 공격 성공률이나 실제 운영 장애 확률이 아니다. Audit coverage와 inventory coverage는 toy evidence coverage이므로 실제 기업 감사 완전성이나 완전한 AI BOM으로 해석하지 않는다.

## 6. 기말논문 연결 지점

W14는 기말논문에서 운영형 AI 시스템의 보안·재현성 보증을 위한 evidence set으로 연결된다. Dataset hash, model hash, config hash, drift score, audit coverage, artifact inventory를 최소 평가항목으로 사용할 수 있다.

## 7. 예상 질문과 답변

| 질문 | 답변 |
|---|---|
| Accuracy가 높으면 보안도 괜찮다고 볼 수 있는가? | 아니다. Accuracy는 모델 성능 기준선이고, 공급망 보안은 데이터·모델·config·로그가 추적 가능한지 별도로 봐야 한다. |
| Drift score 0.307626은 공격을 의미하는가? | 아니다. 입력 분포 변화 경보일 뿐이며, 공격인지 정상 환경 변화인지는 incident analysis가 필요하다. |
| Audit coverage 1.000000은 감사가 완전하다는 뜻인가? | 아니다. toy 필수 필드가 채워졌다는 뜻이며 로그 품질·진실성은 별도 검증이 필요하다. |
| Inventory coverage 1.000000은 완전한 AI BOM인가? | 아니다. dataset/model/config/run log 최소 항목만 다루며 SBOM, license, vulnerability scan은 운영 확장 항목이다. |
| P03/P04/P05는 왜 확인 필요인가? | 수업자료의 대상 논문 DOI와 로컬 PDF가 달라서 최종 인용 전 공식 원문 확보가 필요하다. |
| 이 toy 실험이 실제 MLOps 보안을 증명하는가? | 아니다. 실제 운영 보안성 증명이 아니라 evidence 구조의 최소 구현이다. |
