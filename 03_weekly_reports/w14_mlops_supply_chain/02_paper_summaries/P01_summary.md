# 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 논문 제목 | A Multivocal Review of MLOps Practices, Challenges and Open Issues |
| 저자 | Beyza Eken, Samodha Pallewatta, Nguyen Khoi Tran, Ayse Tosun, Muhammad Ali Babar |
| 학술지/학회 | ACM Computing Surveys / arXiv version |
| 연도 | 2025 |
| DOI/URL | https://doi.org/10.1145/3747346 / https://arxiv.org/abs/2406.09737 |
| PDF 파일명 | 01_Eken_et_al_2025_MLOps_Practices_Multivocal_Review.pdf |
| 검증 상태 | 제목은 수업 검수보고서와 PDF 첫 페이지 기준으로 보정, ACM 최종본 세부 서지는 재대조 필요 |

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

## 6. 주요 결과

MLOps는 단순 자동화가 아니라 데이터 엔지니어링, ML 학습, 소프트웨어 배포, 운영 모니터링, 조직 협업을 결합한 socio-technical practice로 다뤄진다. 특히 pipeline complexity, production scale, artifact management, quality/security/governance가 운영형 ML 시스템의 반복 과제로 제시된다.

## 7. 보안 관점 분석

MLOps practices는 곧 통제항목이 된다. 데이터 버전관리, 모델 registry, config 고정, monitoring, rollback, 승인 절차가 약하면 데이터 오염, 모델 artifact 변조, 무단 업데이트, 로그 공백이 발생한다. 따라서 보안 평가는 모델 성능뿐 아니라 artifact traceability와 auditability를 함께 요구한다.

## 8. 한계와 오픈문제

Survey 문헌이므로 특정 보안 공격을 직접 재현하지는 않는다. 또한 grey literature를 포함하기 때문에 항목의 실무성은 높지만, 각 통제항목의 정량 효과는 별도 실험 또는 사례 분석으로 검증해야 한다.

## 9. 기말 논문에 반영할 부분

기말 논문에서는 P01을 MLOps 보안통제 프레임워크의 상위 taxonomy 근거로 사용한다. 특히 `data/model/config/log`를 함께 관리해야 한다는 논리를 W14 toy pipeline의 hash, audit coverage, artifact inventory 평가와 연결한다.
