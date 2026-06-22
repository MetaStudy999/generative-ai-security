# 보안 이슈 30% 정리

## 1. 주요 보안 이슈

W10의 보안 이슈는 Gradient leakage, poisoning, backdoor, privacy attack이다. 이 부분은 전체 보고서의 30% 비중으로 두되, AI 원리를 실제 위협모형과 평가방법으로 전환하는 데 집중한다.

- Gradient leakage
- Membership inference in FL
- Poisoning attack
- Model poisoning
- Backdoor attack in FL
- Malicious client
- Byzantine client
- Secure aggregation
- Robust aggregation defense
- FL privacy policy landscape

## 2. CIA 관점 분석

| 관점 | 관련 위협 | 설명 |
|---|---|---|
| Confidentiality | Gradient leakage | 연합학습(FL) & FL 위협·방어·정책 환경에서 보호해야 할 자산과 실패 조건을 정의한다. |
| Integrity | Membership inference in FL | 연합학습(FL) & FL 위협·방어·정책 환경에서 보호해야 할 자산과 실패 조건을 정의한다. |
| Availability | Poisoning attack | 연합학습(FL) & FL 위협·방어·정책 환경에서 보호해야 할 자산과 실패 조건을 정의한다. |
| Privacy | Model poisoning | 연합학습(FL) & FL 위협·방어·정책 환경에서 보호해야 할 자산과 실패 조건을 정의한다. |
| Safety | Backdoor attack in FL | 연합학습(FL) & FL 위협·방어·정책 환경에서 보호해야 할 자산과 실패 조건을 정의한다. |
| Accountability | Malicious client | 연합학습(FL) & FL 위협·방어·정책 환경에서 보호해야 할 자산과 실패 조건을 정의한다. |

## 3. 공격-방어-평가 분류

| 구분 | 내용 |
|---|---|
| 공격 자산 | 데이터, 모델, 프롬프트/입력, 평가셋, 로그, 배포 파이프라인 중 주차 주제에 해당하는 자산 |
| 공격자 능력 | 입력 조작, 데이터 오염, 질의 반복, 업데이트 조작, 평가 누수 유도 등 |
| 방어 방법 | 데이터 검증, 강건성 평가, 접근 제어, 모니터링, 재현성 기록, human approval gate |
| 평가 지표 | Clean 성능, 공격 성공률, 강건 성능, 누수 점수, 재현성 로그, 운영 위험도 |

## 4. 기말 논문 연결

이 보안 이슈는 단독 공격 설명이 아니라, 연합학습(FL) 및 FL 위협/방어/정책의 생명주기에서 어느 단계가 취약한지 보여주는 사례로 사용한다.
