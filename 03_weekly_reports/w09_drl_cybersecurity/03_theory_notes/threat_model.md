# 위협모형

| 항목 | 내용 |
|---|---|
| 대상 시스템 | DRL 기반 사이버 방어 에이전트 또는 자동 대응 시스템 |
| 보호 자산 | 상태 관측값, 보상함수, 정책, 보안 로그, 대응 action, 평가 결과 |
| 공격자 | 외부 공격자, 내부자, 로그/환경 조작자, 학습 파이프라인 참여자 |
| 공격자의 지식 | White-box, Gray-box, Black-box로 구분 |
| 공격자의 능력 | 상태 관측 조작, 보상 신호 왜곡, 환경 이벤트 조작, 로그 오염 |
| 공격 경로 | 보안 로그, alert stream, reward 계산 모듈, policy update, 자동 대응 action |
| 공격 성공 조건 | 높은 observed reward를 유지하면서 공격 이벤트 미대응, 정상 이벤트 과잉 격리, unsafe automated response가 발생함 |
| 방어자 가정 | seed/config/log 보존, synthetic 또는 공개 데이터 사용, human override 가능, 실제 공격 자동화 금지 |
| 방어/점검 | robust reward design, safety penalty, uncertain state escalation, perturbed-state evaluation |
| 제외 범위 | 실제 시스템 침해, 실제 네트워크 공격, 개인정보 사용, 무단 스캔, exploit 실행 |

## 연구문제 후보

RQ1. 사이버보안 환경에서 DRL 에이전트의 상태·행동·보상 설계는 방어 성능과 안전성에 어떤 영향을 미치는가?

RQ2. Reward manipulation은 DRL 기반 사이버 방어 에이전트의 정책을 어떻게 왜곡할 수 있는가?

RQ3. DRL 기반 자동 대응 시스템을 평가할 때 Detection F1, Safety Violation Rate, Policy Robustness를 어떻게 결합해야 하는가?

## Reward Manipulation과 Reward Misspecification

| 구분 | 정의 | W09 처리 |
|---|---|---|
| Reward manipulation | 공격자 또는 환경 조작자가 학습 보상 신호를 의도적으로 왜곡하는 경우 | manipulated reward 조건에서 true reward와 observed reward를 분리 기록 |
| Reward misspecification | 설계자가 실제 보안 목표를 보상함수에 잘못 반영한 설계 오류 | KCI/SCI 확장 주제의 한계와 후속 연구 항목으로 분리 |

이 위협모형은 실제 네트워크 침투 절차가 아니라 synthetic cyber-defense state/action/reward 기반 안전 toy 실험의 평가축을 설명하기 위한 것이다.
