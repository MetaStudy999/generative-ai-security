# 위협모형

## 1. 대상 시스템

W01의 대상은 딥러닝 또는 일반 ML 모델을 포함한 보안 응용 시스템이다. 단일 모델만 보지 않고 데이터 수집, 전처리, 학습, 검증, 배포, 추론, 모니터링으로 이어지는 생명주기 전체를 분석 단위로 둔다.

## 2. 보호 자산

| 자산 | 설명 | 대표 위협 |
|---|---|---|
| 학습 데이터 | 원본 데이터, 라벨, 전처리 결과 | poisoning, privacy leakage |
| 모델 파라미터 | 학습된 가중치와 구조 정보 | model extraction, inversion |
| 입력 데이터 | 추론 시 들어오는 샘플, 로그, 패킷, 이미지 | adversarial example, evasion |
| 출력 정보 | 클래스, confidence, embedding, 설명 결과 | membership inference, confidence leakage |
| 평가셋 | 성능 검증에 쓰이는 데이터와 라벨 | benchmark contamination, metric gaming |
| 운영 로그 | 학습·배포·추론 기록 | 사고 추적 실패, 재현성 훼손 |

## 3. 공격자 가정

| 구분 | 공격자 지식 | 공격자 능력 | 예시 |
|---|---|---|---|
| White-box | 모델 구조, 파라미터, 학습 절차를 안다. | gradient 계산, 내부 상태 분석 | 연구실 평가, 내부자 위협 |
| Gray-box | 일부 구조나 출력, 데이터 분포를 안다. | 반복 질의, 대체 모델 구성 | API 관찰 기반 공격 |
| Black-box | 입력과 출력만 관찰한다. | 질의 반복, 출력 비교 | 외부 서비스 사용자 |
| Data contributor | 학습 데이터 일부를 제공한다. | 라벨 조작, backdoor 삽입 | 공급망·데이터 수집 단계 |
| Evaluator/Operator | 평가 또는 운영 파이프라인에 접근한다. | 지표 왜곡, 로그 누락 | 내부 운영 리스크 |

## 4. 생명주기별 위협

| 단계 | 주요 위협 | 방어·점검 |
|---|---|---|
| 데이터 수집 | 오염 데이터, 편향, 개인정보 포함 | 출처 기록, 라벨 검수, 개인정보 제거 |
| 전처리 | feature leakage, 잘못된 정규화 | 파이프라인 버전 관리 |
| 모델 학습 | poisoning, backdoor, overfitting | seed/config 보존, validation split 점검 |
| 모델 검증 | 평가셋 오염, 단일 지표 의존 | clean/robust/privacy/reproducibility 지표 분리 |
| 배포 | 환경 차이, model extraction | 접근 제어, rate limit, 출력 최소화 |
| 추론 | evasion, adversarial example | 입력 검증, 모니터링, robust evaluation |
| 모니터링 | drift 미탐, 로그 누락 | drift detection, 감사 로그 |

## 5. 제외 범위

실제 서비스 침해, 실제 개인정보 사용, 무단 API 대량 질의, 실제 악성코드 실행, 공격 절차의 세부 재현은 제외한다. 실험은 공개 데이터 또는 synthetic data 기반의 안전한 toy evaluation으로 제한한다.

## 6. 평가 증거 요구사항

| 증거 | 목적 | W01 상태 |
|---|---|---|
| DOI/URL 검증표 | 참고문헌과 본문 인용 대응 확인 | 작성 완료, P04 확인 필요 |
| Seed/config | 실험 재현 조건 확인 | 작성 완료 |
| 실행 로그 | 정량값의 근거 보존 | outputs 파일 존재 확인 |
| AI 활용 고지 | 초안 작성 과정과 책임 범위 표시 | 작성 완료 |
| PDF 보관 상태 | 공개 저장소 저작권 위험 점검 | PDF 원문 Git 추적 중, 조치 필요 |

## 7. 연구문제 후보

RQ1. ML 생명주기 각 단계에서 보안 보증을 위해 최소한으로 남겨야 할 증거는 무엇인가?

RQ2. Clean performance, robust performance, privacy leakage, reproducibility를 함께 볼 때 어떤 지표 조합이 가장 설득력 있는가?

RQ3. Survey 기반 분류체계를 실제 toy 실험 또는 문헌 매트릭스로 연결할 때 어떤 한계가 생기는가?
