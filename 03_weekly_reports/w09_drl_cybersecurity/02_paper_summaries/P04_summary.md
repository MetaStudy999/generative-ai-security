# 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 논문 제목 | Cyber-security and reinforcement learning - A brief survey |
| 저자 | Amrin Maria Khan Adawadkar; Nilima Kulkarni |
| 학술지/학회 | Engineering Applications of Artificial Intelligence |
| 연도 | 2022 |
| DOI/URL | https://doi.org/10.1016/j.engappai.2022.105116 |
| PDF 파일명 | 04_Adawadkar_Kulkarni_2022_Cybersecurity_RL_Survey.pdf |
| 검증 상태 | 로컬 PDF 확인, DOI 확인 |

## 2. 한 문장 요약

> 이 논문은 IDS/IPS, IoT, IAM 영역에서 reinforcement learning을 활용한 사이버보안 연구를 정리하며, 표준 평가 기준과 데이터셋 부족이 DRL 보안 연구의 큰 한계임을 보여준다.

## 3. 연구문제

RL이 침입탐지·침입방지·IoT·IAM 문제에 어떻게 적용되어 왔으며, 어떤 데이터셋과 평가 지표로 비교할 수 있는지가 핵심 질문이다.

## 4. 핵심 개념

| 개념 | 설명 | W09 연결 |
|---|---|---|
| IDS/IPS | 공격 이벤트를 탐지하거나 차단하는 보안 시스템이다. | cyber-defense 대상 |
| IoT | 이동성과 자원 제약으로 상태공간과 공격면이 복잡하다. | synthetic state 설계 |
| IAM | 접근 제어와 인증에 RL을 적용할 수 있지만 연구가 적다. | 자동 대응 범위 |
| Evaluation criteria | detection rate, precision, accuracy 등이 비교 지표로 쓰인다. | Detection F1, FPR/FNR |

## 5. 방법론

2010-2021년 문헌을 대상으로 RL 기반 IDS/IPS, IoT, IAM 연구를 survey하고, 데이터셋과 알고리즘, 평가 지표를 정리한다.

## 6. 주요 결과

RL 사이버보안 연구는 IDS와 IoT 자원 최적화에 상대적으로 많이 집중되어 있고, IAM은 문헌이 적다. 평가 기준이 표준화되어 있지 않아 detection rate, precision, accuracy 같은 공통 지표를 함께 기록해야 한다.

## 7. 보안 관점 분석

P04는 W09 실험의 Detection F1 지표를 정당화한다. 다만 자동 대응 정책은 단순 탐지 성능만으로 평가할 수 없으므로, Safety Violation Rate와 Policy Robustness를 함께 둬야 한다.

## 8. 한계와 오픈문제

Survey 범위가 RL 전반에 넓게 퍼져 있어 DRL verification이나 reward hacking을 깊게 다루지는 않는다. W09에서는 P03/P05와 결합해 보상조작과 검증 관점을 보완한다.

## 9. 기말 논문에 반영할 부분

기말 논문의 관련연구 표에서 IDS/IPS, IoT, IAM 관점의 RL 보안 연구 공백과 평가 지표 표준화 필요성을 설명하는 근거로 사용한다.
