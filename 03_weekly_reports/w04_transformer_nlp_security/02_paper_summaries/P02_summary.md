# P02 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 논문 제목 | A Practical Survey on Faster and Lighter Transformers |
| 저자 | Quentin Fournier, Gaetan Marceau Caron, Daniel Aloise |
| 출판 정보 | ACM Computing Surveys, Vol. 55, No. 14s, 2023, pp. 1-40 |
| DOI/URL | ACM DOI `10.1145/3586074`; https://arxiv.org/abs/2103.14636 |
| PDF 파일명 | 02_Fournier_et_al_2023_Faster_Lighter_Transformers_Survey.pdf |
| 검증 상태 | ACM CSUR 출판 DOI 확인. Article 번호는 Crossref/BibTeX 응답에 미제공되어 확인 필요 |

## 2. 한 문장 요약

P02는 Transformer를 실제 배포 환경에서 더 빠르고 가볍게 만들기 위한 pruning, quantization, distillation, efficient architecture, inference optimization 전략을 정리한 practical survey이다.

## 3. 연구문제

Transformer의 성능을 크게 훼손하지 않으면서 speedup, memory footprint, parameter count, inference latency를 어떻게 줄일 수 있는가를 다룬다.

## 4. 핵심 개념

| 개념 | 설명 | W04 연결 |
|---|---|---|
| Distillation | 큰 모델의 행동을 작은 모델에 이전한다. | 경량 보안 필터 배포 가능성 |
| Pruning | 중요도가 낮은 가중치·head·block을 제거한다. | 탐지기 비용 절감 |
| Quantization | 낮은 정밀도 표현으로 메모리와 계산량을 줄인다. | 온디바이스/저비용 방어 |
| Inference optimization | 캐싱, early exit, batch 최적화 등을 활용한다. | 실시간 프롬프트 검사 latency |

## 5. 방법론

문헌조사와 실용 분류를 결합한다. P01이 efficient attention 구조 자체에 초점을 둔다면, P02는 실제 시스템에서 어떤 효율화 수단을 선택할지에 더 가까운 survey이다.

## 6. 주요 결과

효율화 기법은 speed, memory, latency, parameter count를 개선할 수 있지만 utility degradation과 robustness 변화가 함께 발생할 수 있다. 보안 맥락에서는 방어 기능이 실제 운영 경로에 들어갈 수 있을 만큼 가벼운지가 중요하다.

## 7. 보안 관점 분석

프롬프트 마스킹, privacy-risk detector, 로그 감사 모듈은 비용이 크면 운영 시스템에서 제외되기 쉽다. P02는 방어 비용과 utility trade-off를 보고서의 평가축으로 넣는 근거가 된다.

## 8. 한계와 오픈문제

NLP 공격이나 프롬프트 프라이버시를 직접 다루는 문헌은 아니다. W04에서는 방어 시스템을 배포 가능한 비용으로 만들기 위한 보조 근거로 사용한다.

## 9. 기말 논문에 반영할 부분

프롬프트 민감정보 보호 평가체계에서 utility score와 latency/cost evidence를 함께 기록해야 한다는 논리로 연결한다.
