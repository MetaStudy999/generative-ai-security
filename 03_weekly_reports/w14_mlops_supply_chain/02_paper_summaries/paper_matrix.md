# W14 논문 5편 비교표

| 논문 | 연구문제 | 핵심 방법 | 데이터/실험 | 보안 위협 | 평가 지표 | 한계 | 내 논문 활용 |
|---|---|---|---|---|---|---|---|
| P01 | MLOps practices와 adoption challenge를 어떻게 통합적으로 정리할 것인가 | Multivocal literature review | 학술문헌과 grey literature, 원문 세부 수치 재대조 필요 | artifact 관리 실패, governance/security 공백 | practice taxonomy, challenge taxonomy, lifecycle coverage | survey이므로 통제 효과 직접 검증은 아님 | MLOps 보안통제 프레임워크의 상위 구조 |
| P02 | ML deployment workflow에서 반복되는 production challenge는 무엇인가 | Case-study survey | published deployment case, 세부 사례 수치 재대조 필요 | 데이터 품질, 통합 실패, monitoring 부재 | workflow 단계별 challenge, deployment concern | 사례별 보안 통제 수준 비교는 제한적 | 연구용/운영용 ML 격차 설명 |
| P03 | MLOps/AIOps taxonomy와 운영 자동화 task를 어떻게 구분할 것인가 | Systematic survey / 로컬 대체 AIOps review | 대상 원문 PDF 미확보, 로컬 PDF는 cloud AIOps review | 로그 노출, 이상탐지 실패, 자동대응 오류 | incident detection, failure prediction, RCA, TTR/TTD | 로컬 PDF가 대체문헌 | monitoring, incident response, auditability 근거 |
| P04 | Edge deployment에서 AI pipeline은 어떤 제약을 갖는가 | Edge AI / edge computing review | 대상 원문 PDF 미확보, 로컬 PDF는 Edge Intelligence survey | 분산 모델 update, device별 artifact 변조, 로그 수집 공백 | latency, bandwidth, privacy/locality, resource constraint | 대상 논문 직접 원문 재확인 필요 | edge 배포 환경의 공급망 통제 필요성 |
| P05 | DL for SE가 DevOps/MLOps pipeline에 어떤 영향을 주는가 | DL for SE survey | 대상 원문 PDF 미확보, 로컬 PDF는 Yang/Xia/Lo/Grundy survey | AI-assisted 개발도구 오염, software/ML supply chain 결합 | task performance, model selection, optimization, reproducibility | 대상 논문과 로컬 PDF 서지 차이 | AI 개발 자동화 도구의 감사·재현성 요구 |

## 종합 비교

### 1. 공통적으로 다루는 문제

다섯 편은 연구용 모델을 실제 소프트웨어와 운영환경에 연결할 때 생기는 격차를 서로 다른 층위에서 다룬다. P01/P02는 MLOps와 deployment workflow를, P03은 운영 telemetry와 incident response를, P04는 edge deployment를, P05는 AI가 software engineering workflow에 들어오는 경우를 담당한다.

### 2. 논문 간 차이점

P01은 MLOps practice의 통합 구조, P02는 deployment case의 현실적 난점, P03은 AIOps 운영 감시, P04는 cloud-edge 배포 구조, P05는 개발 pipeline 내부의 AI 활용에 초점을 둔다. W14 보고서에서는 이 차이를 `data/model/config/log/artifact`의 traceability로 묶었다.

### 3. 아직 해결되지 않은 문제

P03, P04, P05는 로컬 PDF가 대상 논문의 직접 원문과 다르다. 최종 인용 전 공식 원문 확보가 필요하다. 또한 survey 문헌만으로는 보안 통제 효과를 정량 검증하기 어렵기 때문에 toy pipeline 실험을 통해 최소 지표를 보완했다.

### 4. 기말 논문 주제로 발전 가능한 연결부

기말 논문에서는 W14를 "운영형 AI 시스템의 보안·재현성 보증 프레임워크"의 근거 주차로 활용한다. 핵심 연결부는 artifact hash, config hash, dataset provenance, drift monitoring, audit coverage, AI BOM/ML artifact inventory다.
