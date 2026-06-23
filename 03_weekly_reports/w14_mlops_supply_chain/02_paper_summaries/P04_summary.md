# 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 대상 논문 제목 | Deep Learning with Edge Computing: A Review |
| 대상 논문 저자 | Jiasi Chen, Xukan Ran |
| 학술지/학회 | Proceedings of the IEEE |
| 연도 | 2019 |
| DOI/URL | https://doi.org/10.1109/JPROC.2019.2921977 |
| DOI 메타데이터 | Vol. 107, Issue 8, pp. 1655-1674, 2019-08 |
| 로컬 PDF 파일명 | 04_RELATED_Zhou_et_al_2019_Edge_Intelligence_Survey.pdf |
| 로컬 PDF 제목 | Edge Intelligence: Paving the Last Mile of Artificial Intelligence with Edge Computing |
| 검증 상태 | DOI/권호/페이지 확인. 로컬 PDF는 Zhou et al. 관련 보조 문헌이므로 공식 원문 PDF 확보 필요 |

## 2. 한 문장 요약

> 대상 논문은 딥러닝과 edge computing의 결합을 다루며, 로컬 관련 논문 PDF는 edge intelligence가 latency, bandwidth, privacy, resource constraint 문제를 어떻게 재구성하는지 보여준다.

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

대상 논문은 deep learning과 edge computing review로 수업자료에 제시되어 있다. 로컬 관련 논문 PDF는 edge intelligence survey이며, 본 보고서에서는 edge deployment의 보안 함의를 도출하는 보조 근거로만 사용한다.

주의: W14의 P04는 지정 논문과 로컬 PDF가 표기 차이가 있다. 현재 로컬 PDF는 Zhou et al. Edge Intelligence 관련 보조 문헌이므로, 최종 제출 전 Jiasi Chen and Xukan Ran의 지정 논문 원문 PDF 또는 공식 출판 페이지를 확보해야 한다.

### 5.1 핵심 수식 또는 알고리즘 설명

| 항목 | 내용 |
|---|---|
| 수식/알고리즘 이름 | Edge Inference Latency-Cost Metric |
| 원문 위치 | 논문 세부 절/쪽/그림/알고리즘 번호 확인 필요. 로컬 DOI/URL 점검표로 문헌 대응만 확인. |
| 작성 형식 | Markdown + LaTeX math |
| 검산 도구 | 사용 안 함 |
| 수식 또는 절차 | 표준 정의식 / 원문 직접 인용 아님.<br>$$Cost=\alpha Latency+\beta Energy+\gamma ModelSize$$ |
| 기호·입력·출력 | Latency: 추론 지연, Energy: 에너지 사용, ModelSize: 모델 크기 |
| 직관적 의미 | Edge Inference Latency-Cost Metric는 MLOps·Supply Chain 운영 보안 평가에서 핵심 원리나 평가 지표를 정량적으로 해석하기 위한 표준식이다. |
| 보안 관점 해석 | MLOps·Supply Chain 운영 보안 평가에서는 정상 성능과 보안 실패 조건을 분리해 보아야 한다. 이 항목은 공격·방어 원리 또는 운영 통제의 평가 기준을 명시하되, 실제 공격 절차나 무단 적용 단계는 포함하지 않는다. |
| 평가 지표와 연결 | latency, energy, model size, security overhead |
| 한계와 가정 | 표준 정의식 / 원문 직접 인용 아님. 논문별 변형, 정확한 수식 번호, 실험 설정은 원문 PDF에서 확인 필요다. |
| 기말 논문 반영 여부 | 참고만 |

## 6. 주요 결과

Edge 환경은 낮은 지연, bandwidth 절감, 지역성 기반 프라이버시 이점을 제공하지만, 자원 제약과 heterogeneous device, 불안정한 연결, 분산 업데이트라는 운영 난점도 만든다. 이러한 난점은 MLOps pipeline이 중앙 서버 기준으로만 설계되면 놓치기 쉽다.

## 7. 보안 관점 분석

Edge 배포는 모델 artifact와 config가 여러 지점에 흩어지는 구조다. 이때 모델 업데이트 검증, device별 버전 추적, 로그 수집 범위, rollback 가능성, drift 감시가 핵심 통제항목이 된다. 중앙 cloud보다 공격면이 넓어질 수 있으므로 artifact inventory가 중요하다.

## 8. 한계와 오픈문제

현재 로컬 PDF는 대상 논문 직접 원문이 아니며, edge 보안 공격을 직접 재현하지 않는다. 기말 논문에서는 edge 환경을 예시로만 사용하고, 실제 device-level 공격 절차는 제외한다.

## 9. 기말 논문에 반영할 부분

P04는 MLOps 공급망 보안에서 deployment target이 cloud, on-premise, edge로 다양해질 때 artifact signing, version tracking, drift monitoring이 왜 필요한지 설명하는 근거로 반영한다.
