# W14 논문 5편 비교표

| 논문 | 연구문제 | 핵심 방법 | 데이터/실험 | AI 원리 기여 | 보안 위협 연결 | 평가 지표 | 한계 | 내 논문 활용 |
|---|---|---|---|---|---|---|---|---|
| P01 | MLOps practices와 adoption challenge를 어떻게 통합적으로 정리할 것인가 | multivocal literature review, MLOps practice/challenge taxonomy | 학술문헌 + grey literature. 세부 taxonomy 원문 대조 필요 | MLOps lifecycle, experiment tracking, governance, reproducibility | artifact 관리 실패, governance gap, security control 부재 | lifecycle coverage, artifact coverage, governance maturity | 수업자료/프롬프트 제목 및 저자명과 DOI/로컬 PDF 제목 차이 확인 필요 | MLOps 보안통제 프레임워크의 상위 구조 |
| P02 | ML deployment workflow에서 반복되는 production challenge는 무엇인가 | case-study survey, deployment workflow analysis | published deployment case studies | 연구용 모델과 운영용 시스템의 차이 | data quality failure, integration failure, monitoring gap, rollback failure | deployment concern, workflow challenge, production readiness | 사례별 보안 통제 수준 정량 비교는 제한적 | 연구용/운영용 ML 격차 설명 |
| P03 | MLOps/AIOps taxonomy와 운영 자동화 task를 어떻게 구분할 것인가 | systematic survey, AIOps taxonomy, monitoring/incident response classification | 지정 원문 PDF 미확보. 로컬 PDF는 Cheng et al. cloud AIOps 대체문헌 | telemetry, anomaly detection, incident response, RCA | log leakage, anomaly detection failure, unsafe automated response | incident detection, failure prediction, RCA, TTD/TTR | 수업자료 제목과 DOI 메타데이터 제목 차이 및 로컬 PDF 대체 상태 | monitoring, incident response, auditability 근거 |
| P04 | Edge deployment에서 AI pipeline은 어떤 제약을 갖는가 | edge AI/deep learning with edge computing review | 지정 원문 PDF 미확보. 로컬 PDF는 Zhou et al. Edge Intelligence 대체문헌 | cloud-edge-device deployment, latency, resource constraints | distributed update tampering, edge artifact drift, telemetry gap | latency, bandwidth, privacy/locality, resource constraint | 대상 논문 공식 원문 PDF 재확인 필요 | edge 배포 환경의 공급망 통제 필요성 |
| P05 | Deep learning for software engineering이 DevOps/MLOps pipeline에 어떤 영향을 주는가 | DL for SE survey, AI-assisted software engineering taxonomy | DOI/로컬 PDF는 Yang/Xia/Lo/Grundy 논문. 수업자료의 Xiang Chen 표기 확인 필요 | code, test, defect prediction, SE automation | AI-assisted dev tool poisoning, software/ML supply-chain coupling | task performance, model selection, reproducibility, human review | 수업자료 지정 저자와 DOI/로컬 PDF 서지 차이 확인 필요 | AI 개발 자동화 도구의 감사·재현성 요구 |

## 종합 비교

### 1. 공통적으로 다루는 문제

다섯 편은 연구용 모델을 실제 소프트웨어와 운영환경에 연결할 때 생기는 격차를 서로 다른 층위에서 다룬다. P01은 MLOps lifecycle과 governance 구조 문헌이고, P02는 production deployment challenge 문헌이다. P03은 AIOps, monitoring, incident response 문헌이며, P04는 edge deployment와 분산 artifact/update 관리 문헌이다. P05는 software engineering pipeline 내부의 DL/AI 활용 문헌이다.

### 2. W14 핵심 연결부

W14의 핵심 연결부는 `data/model/config/log/artifact` traceability와 AI BOM/ML artifact inventory다. 모델 정확도만으로는 운영형 AI 보안성을 설명할 수 없으며, dataset hash, config hash, model hash, drift score, audit coverage, inventory coverage, re-run consistency를 함께 보고해야 한다.

### 3. SUBSTITUTE PDF 상태

P03/P04/P05는 대체 PDF 상태이므로 지정 논문처럼 인용하지 않는다. P03의 로컬 파일은 Cheng et al. AIOps cloud survey, P04의 로컬 파일은 Zhou et al. Edge Intelligence survey, P05의 로컬 파일은 Yang/Xia/Lo/Grundy DL for SE survey다. 최종 제출 전 수업자료 지정 논문과 DOI 메타데이터의 차이를 공식 출판 페이지에서 재확인해야 한다.

### 4. Toy 실험의 위치

W14 toy 실험은 실제 registry, CI/CD, Kubernetes, package scanner, production telemetry를 구현하지 않은 local synthetic pipeline이다. 따라서 drift score는 공격 성공률이 아니라 운영 감시 지표이고, audit coverage와 inventory coverage는 toy evidence coverage일 뿐 실제 기업 보안 보증이나 완전한 AI BOM이 아니다.
