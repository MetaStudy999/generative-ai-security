# 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 논문 제목 | A Multivocal Review of MLOps Practices, Challenges and Open Issues |
| 저자 | Beyza Eken, Samodha Pallewatta, Nguyen Khoi Tran, Ayse Tosun, Muhammad Ali Babar |
| 학술지/학회 | ACM Computing Surveys / arXiv version |
| 연도 | 2025 online, 2026 print |
| DOI/URL | https://doi.org/10.1145/3747346 / https://arxiv.org/abs/2406.09737 |
| PDF 파일명 | 01_Eken_et_al_2025_MLOps_Practices_Multivocal_Review.pdf |
| DOI 메타데이터 | Vol. 58, Issue 2, pp. 1-35, online 2025-09-08, print 2026-01-31 |
| 검증 상태 | DOI/arXiv/로컬 PDF는 Beyza Eken 제목으로 대응된다. 수업자료의 Bayram Eken 및 긴 제목 표기는 재확인 필요 |

## 2. 한 문장 요약

> 이 논문은 ML 모델을 연구실에서 운영환경으로 이전할 때 필요한 MLOps practices, adoption challenges, open issues를 multivocal literature review로 정리하며, MLOps 보안통제 프레임워크의 배경 축을 제공한다.

## 3. 연구문제

MLOps가 데이터 처리, 모델 학습, 배포, 모니터링, 재학습을 하나의 운영 생명주기로 묶을 때 어떤 실천항목과 난점이 반복되는가를 묻는다. W14 관점에서는 이 실천항목을 데이터/모델 artifact 관리, CI/CD, monitoring, governance, security control로 재해석하는 것이 핵심이다.

## 4. 핵심 개념

| 개념 | 설명 | 기말 논문 연결 |
|---|---|---|
| Multivocal Literature Review | 학술문헌과 grey literature를 함께 분석해 실무와 연구의 공통 개념을 추출 | 연구/운영 격차 설명 |
| MLOps lifecycle | 개발, 학습, 배포, 모니터링, 유지보수, 재학습의 반복 구조 | 위협모형의 단계 구분 |
| Artifact management | 데이터, 모델, config, 환경, 로그의 버전과 출처 관리 | 공급망 무결성 통제 |
| Governance/security | 품질, 보안, 책임성, 윤리 요구사항을 운영 프로세스에 포함 | assurance case 근거 |

## 5. 방법론

PDF 첫 페이지 기준으로 peer-reviewed 연구와 grey literature를 함께 분석하는 multivocal review다. 본 보고서에서는 로컬 PDF 제목과 수업자료 DOI를 대조했으며, 세부 분류표와 빈도 수치는 최종 원문 확인 대상으로 남긴다.

### 5.1 핵심 수식 또는 알고리즘 설명

이 논문은 수식 자체보다 분류체계, 평가 항목, 운영 절차가 핵심인 survey/review 성격이 강하다. 따라서 원문 기준으로 직접 반영할 핵심 수식은 제한적이다. 대신 본 요약에서는 다음 평가 지표 또는 알고리즘 절차를 개념 수준으로 정리한다.

| 항목 | 내용 |
|---|---|
| 핵심 절차/지표 | MLOps Lifecycle Control 절차 |
| 원문 위치 | 논문 세부 절/쪽/그림/알고리즘 번호 확인 필요. 로컬 DOI/URL 점검표로 문헌 대응만 확인. |
| 보안 관점 해석 | MLOps·Supply Chain 운영 보안 평가에서는 정상 성능과 보안 실패 조건을 분리해 보아야 한다. 이 항목은 공격·방어 원리 또는 운영 통제의 평가 기준을 명시하되, 실제 공격 절차나 무단 적용 단계는 포함하지 않는다. |
| 평가 지표와 연결 | artifact coverage, audit coverage, MTTR, rollback success |
| 기말 논문 반영 여부 | 반영 |
| 절차 요약 | 1. data/model/config/code artifact 식별<br>2. version, owner, hash, lineage 기록<br>3. CI/CD 승인과 배포 로그 연결<br>4. monitoring, drift, rollback evidence 유지 |
| 기호·입력·출력 | 입력: artifact와 운영 로그, 출력: 추적 가능한 lifecycle evidence |
| 직관적 의미 | MLOps Lifecycle Control 절차는 MLOps·Supply Chain 운영 보안 평가에서 수식보다 분류·운영·검증 흐름을 명시하는 데 초점을 둔다. |
| 한계와 가정 | survey/review 성격의 절차 요약이며, 원문 분류표의 세부 절·쪽 번호는 확인 필요다. |

## 5.1 서지 차이 메모

- 수업자료 표기: Bayram Eken et al., `A Multivocal Literature Review of MLOps Practices: Emerging Trends, Challenges, and Research Directions`.
- DOI/arXiv/로컬 PDF 기준: Beyza Eken et al., `A Multivocal Review of MLOps Practices, Challenges and Open Issues`.
- 주의: W14의 P01은 수업자료/프롬프트 표기와 로컬 PDF 기준 제목·저자명이 다르므로, DOI 10.1145/3747346의 공식 ACM 출판정보를 기준으로 최종 서지를 재확인해야 한다.

## 6. 주요 결과

MLOps는 단순 자동화가 아니라 데이터 엔지니어링, ML 학습, 소프트웨어 배포, 운영 모니터링, 조직 협업을 결합한 socio-technical practice로 다뤄진다. 특히 pipeline complexity, production scale, artifact management, quality/security/governance가 운영형 ML 시스템의 반복 과제로 제시된다.

## 7. 보안 관점 분석

MLOps practices는 곧 통제항목이 된다. 데이터 버전관리, 모델 registry, config 고정, monitoring, rollback, 승인 절차가 약하면 데이터 오염, 모델 artifact 변조, 무단 업데이트, 로그 공백이 발생한다. 따라서 보안 평가는 모델 성능뿐 아니라 artifact traceability와 auditability를 함께 요구한다.

## 8. 한계와 오픈문제

Survey 문헌이므로 특정 보안 공격을 직접 재현하지는 않는다. 또한 grey literature를 포함하기 때문에 항목의 실무성은 높지만, 각 통제항목의 정량 효과는 별도 실험 또는 사례 분석으로 검증해야 한다.

## 9. 기말 논문에 반영할 부분

기말 논문에서는 P01을 MLOps 보안통제 프레임워크의 상위 taxonomy 근거로 사용한다. 특히 `data/model/config/log`를 함께 관리해야 한다는 논리를 W14 toy pipeline의 hash, audit coverage, artifact inventory 평가와 연결한다.
