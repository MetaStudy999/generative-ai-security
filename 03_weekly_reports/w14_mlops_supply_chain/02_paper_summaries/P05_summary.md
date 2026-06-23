# 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 수업자료 기준 제목 | Deep Learning for Software Engineering: A Survey |
| 수업자료 기준 저자 | Xiang Chen et al. |
| DOI 메타데이터 기준 제목 | A Survey on Deep Learning for Software Engineering |
| DOI 메타데이터 기준 저자 | Yanming Yang, Xin Xia, David Lo, John Grundy |
| 학술지/학회 | ACM Computing Surveys |
| 연도 | 2022 |
| DOI/URL | https://doi.org/10.1145/3505243 |
| DOI 메타데이터 | Vol. 54, Issue 10s, pp. 1-73, print 2022-01-31, online 2022-09-13 |
| 로컬 PDF 파일명 | 05_Yang_Xia_Lo_Grundy_2022_Deep_Learning_Software_Engineering.pdf |
| 로컬 PDF 제목 | A Survey on Deep Learning for Software Engineering |
| 로컬 PDF 저자 | Yanming Yang, Xin Xia, David Lo, John Grundy |
| 검증 상태 | DOI/로컬 PDF는 Yang/Xia/Lo/Grundy로 대응되나 수업자료의 Xiang Chen 표기와 다르므로 지정 논문 확인 필요 |

## 2. 한 문장 요약

> 대상 논문은 소프트웨어공학 문제에 딥러닝을 적용하는 연구 흐름을 정리하며, 로컬 대체 PDF는 DL model selection, optimization, SE task 적용, 남은 challenge를 survey로 정리한다.

## 3. 연구문제

딥러닝 모델이 bug detection, code search, defect prediction, testing, maintenance 등 소프트웨어공학 작업에 어떻게 적용되고, 어떤 모델 선택·최적화·평가 문제가 남는가를 다룬다. W14에서는 이를 MLOps/DevOps 파이프라인에서 AI가 소프트웨어 개발 자체에 들어올 때의 보안·재현성 요구로 연결한다.

## 4. 핵심 개념

| 개념 | 설명 | 기말 논문 연결 |
|---|---|---|
| DL for SE | 코드와 개발 산출물에 딥러닝을 적용하는 연구 흐름 | DevOps 자동화 배경 |
| Model selection | SE task별 입력 표현과 모델 구조 선택 | 평가 기준 |
| Optimization | DNN 성능을 좌우하는 학습·튜닝 요소 | 재현성 요구 |
| SE pipeline integration | 개발 도구, 테스트, 유지보수 workflow에 모델을 통합 | 공급망 공격면 |
| Evaluation gap | task score가 운영 안정성과 동일하지 않음 | MLOps 보안 평가 |

## 5. 방법론

로컬 PDF는 2006년 이후 DL for SE 연구를 survey하고, 관련 기술과 research topic을 분류한다. DOI 10.1145/3505243도 Yang/Xia/Lo/Grundy 논문으로 확인되었으나, 수업자료는 Xiang Chen et al.으로 되어 있어 지정 논문 표기 재확인이 필요하다. 본 보고서에서는 대상 논문과 로컬 PDF의 서지 차이를 명시하고, 세부 task taxonomy는 공식 원문 확보 후 최종 확정한다.

주의: W14의 P05는 수업자료의 Xiang Chen 표기와 DOI/로컬 PDF 기준 Yang/Xia/Lo/Grundy 계열 DL for software engineering 문헌이 불일치한다. 최종 제출 전 수업자료 지정 논문과 DOI 10.1145/3505243의 공식 출판정보를 재확인해야 한다.

## 6. 주요 결과

DL은 소프트웨어공학 도구의 성능을 높일 수 있지만, 모델 구조, 데이터 전처리, 최적화 방법, task definition에 따라 결과가 크게 달라진다. 이는 DevOps pipeline에 AI 모델을 넣을 때도 데이터·모델·config·실행환경을 함께 기록해야 함을 시사한다.

## 7. 보안 관점 분석

AI가 개발·테스트·운영 도구에 들어오면 software supply chain과 ML supply chain이 겹친다. 예를 들어 코드 추천, 결함 탐지, 테스트 생성 모델이 오염되거나 업데이트 검증 없이 배포되면 개발 pipeline 자체가 공격면이 된다.

## 8. 한계와 오픈문제

SE task 성능 지표만으로는 운영 보안성과 책임성을 판단하기 어렵다. 또한 현재 로컬 PDF와 대상 논문 서지가 다르므로 최종 인용 전 공식 원문 대조가 필요하다.

## 9. 기말 논문에 반영할 부분

P05는 MLOps 공급망 보안이 ML 모델만이 아니라 AI-assisted software engineering 도구까지 포함해야 함을 보여주는 배경으로 활용한다. W14의 artifact inventory와 audit log는 개발 자동화 모델에도 적용 가능한 최소 통제항목이다.
