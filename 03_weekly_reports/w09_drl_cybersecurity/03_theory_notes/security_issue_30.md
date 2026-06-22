# 보안 이슈 30% 정리

## 1. 주요 보안 이슈

W09의 보안 이슈는 DRL을 사이버 방어에 적용할 때의 보상조작과 안전한 자동 대응이다. DRL은 adaptive defense에 유망하지만, 방어 목표를 reward로 바꾸는 순간 공격면도 생긴다.

| 이슈 | 설명 | W09 연결 |
|---|---|---|
| DRL for cyber defense | IDS/IPS, IoT, CPS, SDN 방어를 순차 의사결정으로 모델링 | P03/P04 |
| Reward manipulation | 공격자 또는 잘못된 계측이 reward signal을 왜곡 | manipulated reward |
| Reward hacking | agent가 숫자 보상은 높이지만 실제 보안 목표를 어김 | observed reward와 true reward 차이 |
| State observation manipulation | alert, 로그, 센서 값을 낮추거나 높여 정책을 오도 | perturbed alert |
| False positive response | 정상 이벤트에 과잉 격리·차단 수행 | safety violation |
| False negative response | 공격 이벤트를 monitor로 방치 | safety violation |
| Verification difficulty | stochastic environment와 큰 상태공간 때문에 완전 보증이 어려움 | P05 |

## 2. CIA 관점 분석

| 관점 | 관련 위협 | 설명 |
|---|---|---|
| Confidentiality | 보안 로그/상태 관측 노출 | 에이전트의 state가 민감한 운영 정보를 포함할 수 있다. |
| Integrity | reward manipulation, state poisoning | 보상과 관측 무결성이 깨지면 정책이 잘못 학습된다. |
| Availability | 잘못된 자동 격리 또는 패치 | 정상 서비스를 차단하면 방어 시스템이 가용성을 해친다. |
| Privacy | 학습 로그와 이벤트 기록의 개인정보 포함 | 실제 개인정보는 W09 실험 범위에서 제외했다. |
| Safety | 위험 이벤트 미대응, 정상 이벤트 과잉 대응 | safety violation rate로 별도 측정한다. |
| Accountability | 설명 불가능한 자동 대응 | 정책·config·seed·run log를 보존해야 사후 검토가 가능하다. |

## 3. 공격-방어-평가 분류

| 구분 | 내용 |
|---|---|
| 공격 자산 | 상태 관측값, 보상함수, 정책, 학습 로그, 대응 action |
| 공격자 능력 | alert 조작, reward 신호 왜곡, 환경 이벤트 오염, 로그 변조 |
| 방어 방법 | reward clipping, safety penalty, human escalation, perturbation test, run log 보존 |
| 평가 지표 | Average Reward, Detection F1, Safety Violation Rate, Policy Robustness, Perturbed F1 |

## 4. 기말 논문 연결

기말 논문에서는 “높은 보상 = 안전한 방어”라는 가정을 비판하고, reward integrity와 policy safety를 분리해 평가하는 프레임워크로 발전시킨다.
