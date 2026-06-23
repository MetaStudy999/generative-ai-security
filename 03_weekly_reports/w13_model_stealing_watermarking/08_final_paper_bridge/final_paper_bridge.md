# W13 기말논문 연결표

## 1. 추천 최종 주제

| 항목 | 내용 |
|---|---|
| 국문 제목 | 모델 추출 이후 소유권 검증을 위한 다중지표 평가 프레임워크 연구 |
| 영문 제목 | A Multi-Metric Evaluation Framework for Ownership Verification After Model Extraction |
| 대상 시스템 | 공개 API 또는 제한 인터페이스로 제공되는 ML/LLM/생성모형 서비스 |
| 핵심 위협 | model extraction, query abuse, watermark removal, false ownership claim |
| 핵심 기여 | query budget, extraction fidelity, substitute accuracy, watermark detection, false positive rate, utility accuracy, reproducibility evidence 통합 |

## 2. 이번 주차에서 얻은 연구 주제 후보

| 번호 | 주제 후보 | 대상 시스템 | 보안 위협 | 방법론 | 기여 가능성 |
|---:|---|---|---|---|---|
| 1 | 공개 API 기반 AI 모델의 모델 추출 위협모형과 방어 평가 연구 | ML/LLM API 서비스 | Model extraction, query abuse | 문헌분석 + synthetic toy evaluation | 높음 |
| 2 | 딥러닝 모델 워터마킹의 탐지율·위양성·품질저하 평가 기준 연구 | DNN/LLM 모델 | Watermark removal, forgery, false positive | 평가 프로토콜 설계 | 높음 |
| 3 | 생성형 AI 모델의 지식재산 보호를 위한 워터마킹·핑거프린팅 프레임워크 연구 | 생성모형/LLM | Model stealing, output misuse | 문헌분석 + 책임성 체크리스트 | 높음 |

## 3. 기말 논문에 반영할 내용

| 논문 장 | 반영 가능 내용 |
|---|---|
| 서론 | AI 모델의 경제적 가치와 지식재산 보호 필요성 |
| 관련연구 | model stealing, model extraction, DNN/LLM watermarking, fingerprinting |
| 연구문제 | query-response 정보만으로 모델 행동이 얼마나 모방되는가와 소유권 검증은 얼마나 신뢰할 수 있는가 |
| 연구방법 | synthetic toy model 기반 query budget 비교, trigger-set ownership check, false positive proxy |
| 분석/실험 | extraction fidelity 0.864000/0.920000/0.902000, watermark detection 0.700000/1.000000/1.000000 |
| 보안적 함의 | detection rate뿐 아니라 false positive 0.600000과 utility 0.868000을 함께 보고해야 함 |
| 연구윤리 | 실제 API 공격, 무단 대량 질의, 개인정보 사용 제외 |
| 결론 | 모델 IP 보호 평가에서 성능·소유권·위양성·재현성을 함께 기록하는 프레임워크 제안 |

## 4. KCI 전환 메모

KCI형 원고는 국문 문제의식과 실험 한계 설명이 중요하다. “모델 추출 이후 소유권 검증을 위한 다중지표 평가 프레임워크 연구”를 제목으로 두고, 국내 참고문헌 3편 이상과 AI 활용 고지, PDF 저작권 점검표를 보강해야 한다.

## 5. SCI 전환 메모

SCI형 원고는 structured abstract, threat model, methodology, threats to validity를 명확히 분리한다. P02/P05의 지정 논문 원문 확보 또는 대체 문헌 상태 표시가 해결되지 않으면 literature validity 위협으로 남긴다.

## 6. 후속 주차 연결 방식

W14의 MLOps/supply-chain 보안과 연결하면 모델 배포, API 로그, 질의 제한, 워터마크 검증 절차를 운영 통제 관점으로 확장할 수 있다. W15의 재현성/XAI 주제와 연결하면 DOI 검증, 대체 PDF 표시, AI 활용 고지, 실행 로그 보존을 연구윤리 장으로 묶을 수 있다.
