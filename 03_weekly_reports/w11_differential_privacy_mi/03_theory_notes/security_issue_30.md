# 보안 이슈 30% 정리

## 1. 주요 보안 이슈

W11의 보안 이슈는 Membership inference, privacy leakage, utility trade-off이다. 이 부분은 전체 보고서의 30% 비중으로 두되, AI 원리를 실제 위협모형과 평가방법으로 전환하는 데 집중한다.

- Membership inference attack
- Training data leakage
- Model memorization
- Overfitting과 privacy leakage의 관계
- Shadow model 기반 MI 공격 개념
- Confidence score 기반 MI 공격 개념
- DP 기반 방어
- Regularization, calibration, output restriction 방어
- DP 적용 시 accuracy 저하
- LLM/FL 환경에서 MI 방어 한계

## 2. CIA 관점 분석

| 관점 | 관련 위협 | 설명 |
|---|---|---|
| Confidentiality | Membership inference attack | 차등프라이버시(DP) & 멤버십 추론 공격·방어 환경에서 보호해야 할 자산과 실패 조건을 정의한다. |
| Integrity | Training data leakage | 차등프라이버시(DP) & 멤버십 추론 공격·방어 환경에서 보호해야 할 자산과 실패 조건을 정의한다. |
| Availability | Model memorization | 차등프라이버시(DP) & 멤버십 추론 공격·방어 환경에서 보호해야 할 자산과 실패 조건을 정의한다. |
| Privacy | Overfitting과 privacy leakage의 관계 | 차등프라이버시(DP) & 멤버십 추론 공격·방어 환경에서 보호해야 할 자산과 실패 조건을 정의한다. |
| Safety | Shadow model 기반 MI 공격 개념 | 차등프라이버시(DP) & 멤버십 추론 공격·방어 환경에서 보호해야 할 자산과 실패 조건을 정의한다. |
| Accountability | Confidence score 기반 MI 공격 개념 | 차등프라이버시(DP) & 멤버십 추론 공격·방어 환경에서 보호해야 할 자산과 실패 조건을 정의한다. |

## 3. 공격-방어-평가 분류

| 구분 | 내용 |
|---|---|
| 공격 자산 | 데이터, 모델, 프롬프트/입력, 평가셋, 로그, 배포 파이프라인 중 주차 주제에 해당하는 자산 |
| 공격자 능력 | 입력 조작, 데이터 오염, 질의 반복, 업데이트 조작, 평가 누수 유도 등 |
| 방어 방법 | 데이터 검증, 강건성 평가, 접근 제어, 모니터링, 재현성 기록, human approval gate |
| 평가 지표 | Clean 성능, 공격 성공률, 강건 성능, 누수 점수, 재현성 로그, 운영 위험도 |

## 4. 기말 논문 연결

이 보안 이슈는 단독 공격 설명이 아니라, 차등프라이버시(DP) 및 멤버십 추론 공격/방어의 생명주기에서 어느 단계가 취약한지 보여주는 사례로 사용한다.
