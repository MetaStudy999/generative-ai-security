# 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 수업자료 기준 제목 | A Systematic Survey on MLOps and AIOps: Taxonomy, Challenges, and Future Directions |
| 수업자료 기준 저자 | Daniel Diaz-de-Arcaya et al. |
| DOI 메타데이터 기준 제목 | A Joint Study of the Challenges, Opportunities, and Roadmap of MLOps and AIOps: A Systematic Survey |
| DOI 메타데이터 기준 저자 | Josu Diaz-de-Arcaya, Ana I. Torre-Bastida, Gorka Zarate, Raul Minon, Aitor Almeida |
| 학술지/학회 | ACM Computing Surveys |
| 연도 | 2023 online, 2024 print |
| DOI/URL | https://doi.org/10.1145/3625289 |
| DOI 메타데이터 | Vol. 56, Issue 4, pp. 1-30, online 2023-10-21, print 2024-04-30 |
| 로컬 PDF 파일명 | 03_SUBSTITUTE_Cheng_et_al_2023_AIOps_Cloud_Survey.pdf |
| 로컬 PDF 제목 | AI for IT Operations (AIOps) on Cloud Platforms: Reviews, Opportunities and Challenges |
| 검증 상태 | DOI 메타데이터와 수업자료 제목/저자 표기가 다르며, 로컬 PDF는 Cheng et al. 대체문헌이므로 공식 원문 확보 필요 |

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

대상 논문은 수업자료 기준 MLOps/AIOps systematic survey다. DOI 10.1145/3625289의 메타데이터 제목은 수업자료 제목과 다르므로 최종 인용 전 공식 ACM 페이지를 재확인한다. 로컬 PDF는 cloud AIOps review로, 본 보고서에서는 로컬 PDF 첫 페이지의 task taxonomy를 운영 모니터링 보조 근거로만 사용한다. 대상 논문의 세부 taxonomy는 공식 원문 확보 후 재확인한다.

주의: W14의 P03은 지정 논문과 로컬 PDF가 불일치한다. 현재 로컬 PDF는 Cheng et al. AIOps 관련 대체문헌이므로, 최종 제출 전 Daniel/Josu Diaz-de-Arcaya et al.의 지정 논문 원문 PDF 또는 공식 출판 페이지를 확보해야 한다.

### 5.1 핵심 수식 또는 알고리즘 설명

| 항목 | 내용 |
|---|---|
| 수식/알고리즘 이름 | KL Divergence Drift Metric |
| 원문 위치 | 논문 세부 절/쪽/그림/알고리즘 번호 확인 필요. 로컬 DOI/URL 점검표로 문헌 대응만 확인. |
| 작성 형식 | Markdown + LaTeX math |
| 검산 도구 | 사용 안 함 |
| 수식 또는 절차 | 표준 정의식 / 원문 직접 인용 아님.<br>$$D_{KL}(P\Vert Q)=\sum_x P(x)\log\frac{P(x)}{Q(x)}$$ |
| 기호·입력·출력 | \(P\): 기준 분포, \(Q\): 현재 또는 운영 분포 |
| 직관적 의미 | KL Divergence Drift Metric는 MLOps·Supply Chain 운영 보안 평가에서 핵심 원리나 평가 지표를 정량적으로 해석하기 위한 표준식이다. |
| 보안 관점 해석 | MLOps·Supply Chain 운영 보안 평가에서는 정상 성능과 보안 실패 조건을 분리해 보아야 한다. 이 항목은 공격·방어 원리 또는 운영 통제의 평가 기준을 명시하되, 실제 공격 절차나 무단 적용 단계는 포함하지 않는다. |
| 평가 지표와 연결 | drift score, alert precision, retraining trigger, MTTR |
| 한계와 가정 | 표준 정의식 / 원문 직접 인용 아님. 논문별 변형, 정확한 수식 번호, 실험 설정은 원문 PDF에서 확인 필요다. |
| 기말 논문 반영 여부 | 반영 |

## 6. 주요 결과

AIOps 관점에서는 post-release 운영이 observe, detect, engage, act 흐름으로 분해된다. 각 단계는 TTO, TTD, TTT, TTR 같은 시간 지표와 precision/recall 같은 탐지 지표를 갖는다. 이는 MLOps 보안에서도 drift detection, incident response, rollback 기록을 분리해 평가해야 함을 시사한다.

## 7. 보안 관점 분석

운영 telemetry는 방어자에게 필요한 관측 자산이지만 동시에 민감 정보와 시스템 상태가 노출되는 위험 자산이다. 로그가 부족하면 공격이나 drift를 놓치고, 로그가 과도하거나 보호되지 않으면 기밀성과 프라이버시 문제가 생긴다. 따라서 W14 평가에서는 audit coverage와 로그 범위를 함께 다룬다.

## 8. 한계와 오픈문제

현재 로컬 PDF는 대상 논문의 직접 원문이 아니므로 P03의 최종 인용은 공식 PDF 확보 뒤 확정해야 한다. 또한 AIOps 자동 대응은 잘못 설계되면 잘못된 rollback이나 scale action으로 availability를 해칠 수 있다.

## 9. 기말 논문에 반영할 부분

P03는 MLOps 보안 프레임워크에서 monitoring, incident response, auditability를 분리하는 근거로 사용한다. W14 toy 실험의 drift score와 audit coverage를 운영형 AI 시스템 평가 지표로 연결한다.
