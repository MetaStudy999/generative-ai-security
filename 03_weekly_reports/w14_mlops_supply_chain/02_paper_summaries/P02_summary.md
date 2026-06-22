# 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 논문 제목 | Challenges in Deploying Machine Learning: a Survey of Case Studies |
| 저자 | Andrei Paleyes, Raoul-Gabriel Urma, Neil D. Lawrence |
| 학술지/학회 | ACM Computing Surveys |
| 연도 | 2022 |
| DOI/URL | https://doi.org/10.1145/3533378 |
| PDF 파일명 | 02_Paleyes_Urma_Lawrence_2022_ML_Deployment_Challenges.pdf |
| 검증 상태 | DOI가 로컬 PDF 첫 페이지와 수업자료에서 일치 |

## 2. 한 문장 요약

> 이 논문은 ML 모델 배포 과정에서 실제 사례들이 겪는 workflow별 난점을 survey로 정리하며, 연구용 모델과 운영용 서비스 사이의 평가·운영 격차를 보여준다.

## 3. 연구문제

학술 연구에서 잘 동작한 ML 모델이 production workflow로 이동할 때 어떤 단계에서 실패하거나 병목을 만든다는 질문을 다룬다. W14에서는 이 질문을 보안 관점으로 확장해 배포 workflow의 각 단계가 어떤 공격면과 감사 요구사항을 갖는지 살핀다.

## 4. 핵심 개념

| 개념 | 설명 | 기말 논문 연결 |
|---|---|---|
| ML deployment workflow | 문제 정의, 데이터 준비, 학습, 검증, 통합, 배포, 모니터링의 흐름 | 평가 프로토콜 구조 |
| Production gap | 연구 환경의 성능과 운영 환경의 요구사항 사이 차이 | 연구 배경 |
| Case-study survey | 실제 배포 사례에서 반복되는 문제를 수집 | 운영 위험 근거 |
| Monitoring need | 배포 이후 입력/출력/성능 변화를 추적해야 함 | drift score와 audit log 연결 |

## 5. 방법론

논문은 published deployment case를 수집하고 ML deployment workflow 단계에 mapping한다. 본 요약은 PDF 첫 페이지와 수업자료 DOI를 대조한 뒤, 세부 사례별 통계는 원문 정밀 확인 대상으로 남겼다.

## 6. 주요 결과

배포 난점은 모델 학습 이후에만 생기지 않는다. 데이터 수집과 품질, 시스템 통합, 인프라, 운영 모니터링, 조직 협업 등 workflow 전반에서 반복된다. 따라서 ML 보안 평가도 모델 파일 하나가 아니라 pipeline 전체를 대상으로 해야 한다.

## 7. 보안 관점 분석

배포 workflow의 취약점은 공급망 보안 문제와 자연스럽게 이어진다. 데이터 준비 단계에서는 오염과 provenance 부재, 학습/평가 단계에서는 config와 seed 누락, 배포 단계에서는 artifact 변조와 rollback 실패, 운영 단계에서는 drift 미탐지와 로그 누락이 문제가 된다.

## 8. 한계와 오픈문제

Case-study survey는 현실성을 제공하지만 각 사례의 보안 통제 수준을 동일 지표로 비교하기 어렵다. 기말 논문에서는 이를 보완하기 위해 hash, drift score, audit coverage처럼 최소 공통 지표를 정의할 필요가 있다.

## 9. 기말 논문에 반영할 부분

P02는 연구용 ML 실험과 운영용 ML 시스템 사이의 보안·재현성 격차를 설명하는 배경 문헌으로 쓴다. W14 실습의 `re-run consistency`, `audit coverage`, `artifact inventory`가 그 격차를 줄이는 최소 기록이라는 논리를 뒷받침한다.
