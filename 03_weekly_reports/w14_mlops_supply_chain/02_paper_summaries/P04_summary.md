# 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 대상 논문 제목 | Deep Learning with Edge Computing: A Review |
| 대상 논문 저자 | J. Chen et al. |
| 학술지/학회 | Proceedings of the IEEE |
| 연도 | 2019 |
| DOI/URL | https://doi.org/10.1109/JPROC.2019.2921977 |
| 로컬 PDF 파일명 | 04_SUBSTITUTE_Zhou_et_al_2019_Edge_Intelligence_Survey.pdf |
| 로컬 PDF 제목 | Edge Intelligence: Paving the Last Mile of Artificial Intelligence with Edge Computing |
| 검증 상태 | 대상 논문 DOI는 수업자료 기준, 로컬 PDF는 Zhou et al. 대체문헌이므로 공식 원문 확보 필요 |

## 2. 한 문장 요약

> 대상 논문은 딥러닝과 edge computing의 결합을 다루며, 로컬 대체 PDF는 edge intelligence가 latency, bandwidth, privacy, resource constraint 문제를 어떻게 재구성하는지 보여준다.

## 3. 연구문제

AI 추론과 학습을 중앙 cloud가 아니라 edge device 또는 edge node에 배치할 때 어떤 구조적 장점과 제약이 생기는가를 묻는다. W14에서는 이를 edge deployment pipeline과 모델 업데이트 공급망 보안 문제로 해석한다.

## 4. 핵심 개념

| 개념 | 설명 | 기말 논문 연결 |
|---|---|---|
| Edge AI / Edge intelligence | 데이터 발생 지점 가까이에서 AI 처리를 수행하는 구조 | 배포 환경 다양화 |
| Cloud-edge split | cloud와 edge의 계산·저장·추론 역할 분담 | 파이프라인 경계 설정 |
| Resource constraint | device의 계산, 메모리, 에너지 제한 | 모델 경량화와 운영 위험 |
| Privacy/locality | 데이터를 중앙으로 보내지 않는 이점과 한계 | 로그/모니터링 설계 |
| Model update | edge에 배포된 모델의 버전과 업데이트 관리 | 공급망 무결성 |

## 5. 방법론

대상 논문은 deep learning과 edge computing review로 수업자료에 제시되어 있다. 로컬 대체 PDF는 edge intelligence survey이며, 본 보고서에서는 edge deployment의 보안 함의를 도출하는 보조 근거로만 사용한다.

## 6. 주요 결과

Edge 환경은 낮은 지연, bandwidth 절감, 지역성 기반 프라이버시 이점을 제공하지만, 자원 제약과 heterogeneous device, 불안정한 연결, 분산 업데이트라는 운영 난점도 만든다. 이러한 난점은 MLOps pipeline이 중앙 서버 기준으로만 설계되면 놓치기 쉽다.

## 7. 보안 관점 분석

Edge 배포는 모델 artifact와 config가 여러 지점에 흩어지는 구조다. 이때 모델 업데이트 검증, device별 버전 추적, 로그 수집 범위, rollback 가능성, drift 감시가 핵심 통제항목이 된다. 중앙 cloud보다 공격면이 넓어질 수 있으므로 artifact inventory가 중요하다.

## 8. 한계와 오픈문제

현재 로컬 PDF는 대상 논문 직접 원문이 아니며, edge 보안 공격을 직접 재현하지 않는다. 기말 논문에서는 edge 환경을 예시로만 사용하고, 실제 device-level 공격 절차는 제외한다.

## 9. 기말 논문에 반영할 부분

P04는 MLOps 공급망 보안에서 deployment target이 cloud, on-premise, edge로 다양해질 때 artifact signing, version tracking, drift monitoring이 왜 필요한지 설명하는 근거로 반영한다.
