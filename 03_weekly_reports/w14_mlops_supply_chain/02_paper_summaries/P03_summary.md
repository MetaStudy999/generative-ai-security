# 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 대상 논문 제목 | A Systematic Survey on MLOps and AIOps: Taxonomy, Challenges, and Future Directions |
| 대상 논문 저자 | Daniel Diaz-de-Arcaya et al. |
| 학술지/학회 | ACM Computing Surveys |
| 연도 | 2023 |
| DOI/URL | https://doi.org/10.1145/3625289 |
| 로컬 PDF 파일명 | 03_SUBSTITUTE_Cheng_et_al_2023_AIOps_Cloud_Survey.pdf |
| 로컬 PDF 제목 | AI for IT Operations (AIOps) on Cloud Platforms: Reviews, Opportunities and Challenges |
| 검증 상태 | 대상 논문 DOI는 수업자료 기준, 로컬 PDF는 Cheng et al. 대체문헌이므로 공식 원문 확보 필요 |

## 2. 한 문장 요약

> 대상 논문은 MLOps와 AIOps의 taxonomy와 challenge를 정리하는 문헌이며, 로컬 대체 PDF는 cloud AIOps의 incident detection, failure prediction, root cause analysis, automated actions를 정리해 운영 모니터링 관점의 보조 근거를 제공한다.

## 3. 연구문제

MLOps/AIOps는 운영 데이터를 이용해 시스템 상태를 관찰하고, 이상을 탐지하며, 원인을 찾고, 대응을 자동화할 수 있는가를 묻는다. W14에서는 이 질문을 ML 공급망 보안의 monitoring·incident response·audit trail과 연결한다.

## 4. 핵심 개념

| 개념 | 설명 | 기말 논문 연결 |
|---|---|---|
| AIOps | IT 운영 데이터에 AI/ML을 적용해 관찰, 탐지, 분석, 대응을 보조 | 운영 감시 계층 |
| Telemetry data | metrics, logs, traces, events 등 운영 관측 데이터 | audit coverage |
| Incident detection | 장애나 이상 상태를 조기에 식별 | drift/incident trigger |
| Root cause analysis | 장애 원인과 관련 이벤트를 좁히는 분석 | 사고대응 절차 |
| Automated actions | rollback, scale-out 등 대응 자동화 | 안전한 update gate |

## 5. 방법론

대상 논문은 수업자료 기준 MLOps/AIOps systematic survey다. 로컬 PDF는 cloud AIOps review로, 본 보고서에서는 로컬 PDF 첫 페이지의 task taxonomy를 운영 모니터링 보조 근거로만 사용한다. 대상 논문의 세부 taxonomy는 공식 원문 확보 후 재확인한다.

## 6. 주요 결과

AIOps 관점에서는 post-release 운영이 observe, detect, engage, act 흐름으로 분해된다. 각 단계는 TTO, TTD, TTT, TTR 같은 시간 지표와 precision/recall 같은 탐지 지표를 갖는다. 이는 MLOps 보안에서도 drift detection, incident response, rollback 기록을 분리해 평가해야 함을 시사한다.

## 7. 보안 관점 분석

운영 telemetry는 방어자에게 필요한 관측 자산이지만 동시에 민감 정보와 시스템 상태가 노출되는 위험 자산이다. 로그가 부족하면 공격이나 drift를 놓치고, 로그가 과도하거나 보호되지 않으면 기밀성과 프라이버시 문제가 생긴다. 따라서 W14 평가에서는 audit coverage와 로그 범위를 함께 다룬다.

## 8. 한계와 오픈문제

현재 로컬 PDF는 대상 논문의 직접 원문이 아니므로 P03의 최종 인용은 공식 PDF 확보 뒤 확정해야 한다. 또한 AIOps 자동 대응은 잘못 설계되면 잘못된 rollback이나 scale action으로 availability를 해칠 수 있다.

## 9. 기말 논문에 반영할 부분

P03는 MLOps 보안 프레임워크에서 monitoring, incident response, auditability를 분리하는 근거로 사용한다. W14 toy 실험의 drift score와 audit coverage를 운영형 AI 시스템 평가 지표로 연결한다.
