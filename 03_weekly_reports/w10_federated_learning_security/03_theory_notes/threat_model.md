# 위협모형

| 항목 | 내용 |
|---|---|
| 대상 시스템 | 연합학습 기반 분산 AI 학습 시스템 |
| 보호 자산 | 클라이언트 데이터, 로컬 모델 업데이트, 글로벌 모델, 집계 결과, 학습 로그 |
| 공격자 | 악성 클라이언트, 내부자, 서버 관찰자, 외부 질의자 |
| 공격자의 지식 | White-box, Gray-box, Black-box 조건을 구분 |
| 공격자의 능력 | 로컬 업데이트 조작, poisoned update 제출, backdoor trigger 삽입, gradient/update 관찰 |
| 공격 경로 | 클라이언트 업데이트, 서버 집계, 통신 채널, 글로벌 모델 배포, 사후 질의 |
| 공격 성공 조건 | global accuracy 저하, ASR 상승, client data 단서 추론, 방어 우회 |
| 방어자 가정 | client sampling, update validation, secure aggregation, robust aggregation, audit log 가능 |
| 제외 범위 | 실제 개인정보 데이터 사용, 실제 분산 시스템 침해, 무단 클라이언트 접속, 운영 FL 서비스 공격 |

## 연구문제 후보

RQ1. 연합학습 환경에서 malicious client 비율은 global model의 성능과 backdoor 공격 성공률에 어떤 영향을 미치는가?

RQ2. Secure aggregation과 robust aggregation은 gradient leakage, poisoning, backdoor 위험을 각각 어느 정도 완화할 수 있는가?

RQ3. FL 보안 평가에는 privacy leakage, robustness, utility, communication cost를 어떻게 결합해야 하는가?

## W10 toy threat model

본 주차 실험은 실제 FL 서비스가 아니라 synthetic binary classification 환경이다. 공격자는 10개 client 중 일부로만 모의하며, class 0 sample 일부에 toy trigger를 더하고 target class 1로 학습시키는 제한된 poisoned update만 사용한다. 이 설정은 악용 가능한 절차가 아니라 ASR, clean accuracy, aggregation type을 기록하기 위한 안전한 교육용 모의환경이다.
