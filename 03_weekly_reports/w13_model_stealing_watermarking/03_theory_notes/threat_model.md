# 위협모형

| 항목 | 내용 |
|---|---|
| 대상 시스템 | 공개 API 또는 제한된 인터페이스로 제공되는 ML/LLM/생성모형 서비스 |
| 보호 자산 | 모델 파라미터, 모델 행동, 학습된 결정경계, 워터마크, fingerprint, 생성물 출처, API 로그 |
| 공격자 | 외부 질의자, 경쟁 서비스 운영자, 모델 추출 시도자, 워터마크 제거 시도자 |
| 공격자의 지식 | Black-box 또는 Gray-box. 본 실습은 로컬 synthetic black-box query-response만 가정 |
| 공격자의 능력 | 반복 질의, 입력-출력 쌍 수집, 대체 모델 학습, 워터마크 회피·희석 시도 |
| 공격 경로 | 공개 API, query-response 로그, 생성물, 배포 모델, imitation training data |
| 공격 성공 조건 | 원 모델과 유사한 성능/행동의 대체 모델을 얻거나, 소유권 워터마크를 제거·회피함 |
| 방어자 가정 | 질의 제한, 로그 감사, watermarking, fingerprinting, 이상 질의 탐지, 사후 소유권 검증 가능 |
| 제외 범위 | 실제 상용 API 대상 공격, 무단 대량 질의, 실제 모델 탈취, 개인정보 기반 평가 |

## 연구문제 후보

RQ1. 공개 API 기반 모델 서비스에서 query-response 정보만으로 모델 도난 위험을 어떻게 정량화할 수 있는가?

RQ2. 모델 워터마킹은 모델 추출 공격 이후에도 소유권 검증을 얼마나 안정적으로 수행할 수 있는가?

RQ3. 워터마킹 방어는 모델 품질, 탐지율, 위양성, 강건성 사이에서 어떤 trade-off를 만드는가?

## W13 실습 범위

본 실습은 실제 API가 아닌 synthetic toy classifier를 사용한다. 공격자는 `src/run_experiment.py`가 만든 query-response pairs만 보고 1-nearest-neighbor substitute model을 구성한다. 이 구조는 모델 추출의 위험을 이해하기 위한 축소 모형이며, 실제 서비스를 대상으로 한 절차나 운영 가능한 공격 지침이 아니다.
