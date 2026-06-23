# 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 논문 제목 | Cyber-security and reinforcement learning -- A brief survey |
| 저자 | Amrin Maria Khan Adawadkar; Nilima Kulkarni |
| 학술지/학회 | Engineering Applications of Artificial Intelligence, Vol. 114, Article 105116 |
| 연도 | 2022 |
| DOI/URL | https://doi.org/10.1016/j.engappai.2022.105116 |
| PDF 파일명 | 04_Adawadkar_Kulkarni_2022_Cybersecurity_RL_Survey.pdf |
| 검증 상태 | 확인 필요: DOI/PDF 저자명은 `Amrin Maria Khan Adawadkar; Nilima Kulkarni`, 강의계획서 저자명은 `Aditya Adawadkar et al.` |

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

### 5.1 핵심 수식 또는 알고리즘 설명

| 항목 | 내용 |
|---|---|
| 수식/알고리즘 이름 | Policy Gradient Objective |
| 원문 위치 | 논문 세부 절/쪽/그림/알고리즘 번호 확인 필요. 로컬 DOI/URL 점검표로 문헌 대응만 확인. |
| 작성 형식 | Markdown + LaTeX math |
| 검산 도구 | 사용 안 함 |
| 수식 또는 절차 | 표준 정의식 / 원문 직접 인용 아님.<br>$$\nabla_\theta J(\theta)=\mathbb{E}_{\pi_\theta}\left[\nabla_\theta\log\pi_\theta(a\mid s)G_t\right]$$ |
| 기호·입력·출력 | \(\pi_\theta\): policy, \(G_t\): return estimate, \(a,s\): action/state |
| 직관적 의미 | Policy Gradient Objective는 DRL 사이버보안 평가에서 핵심 원리나 평가 지표를 정량적으로 해석하기 위한 표준식이다. |
| 보안 관점 해석 | DRL 사이버보안 평가에서는 정상 성능과 보안 실패 조건을 분리해 보아야 한다. 이 항목은 공격·방어 원리 또는 운영 통제의 평가 기준을 명시하되, 실제 공격 절차나 무단 적용 단계는 포함하지 않는다. |
| 평가 지표와 연결 | return, safe action rate, reward manipulation impact |
| 한계와 가정 | 표준 정의식 / 원문 직접 인용 아님. 논문별 변형, 정확한 수식 번호, 실험 설정은 원문 PDF에서 확인 필요다. |
| 기말 논문 반영 여부 | 반영 |

## 6. 주요 결과

RL 사이버보안 연구는 IDS와 IoT 자원 최적화에 상대적으로 많이 집중되어 있고, IAM은 문헌이 적다. 평가 기준이 표준화되어 있지 않아 detection rate, precision, accuracy 같은 공통 지표를 함께 기록해야 한다.

## 7. 보안 관점 분석

P04는 W09 실험의 Detection F1 지표를 정당화한다. 다만 자동 대응 정책은 단순 탐지 성능만으로 평가할 수 없으므로, Safety Violation Rate와 Policy Robustness를 함께 둬야 한다.

## 8. 한계와 오픈문제

Survey 범위가 RL 전반에 넓게 퍼져 있어 DRL verification이나 reward hacking을 깊게 다루지는 않는다. W09에서는 P03/P05와 결합해 보상조작과 검증 관점을 보완한다. 강의계획서의 `Aditya Adawadkar et al.` 표기와 DOI/PDF의 `Amrin Maria Khan Adawadkar; Nilima Kulkarni` 표기가 다르므로, 오기인지 대체 문헌인지는 확인 필요다.

## 9. 기말 논문에 반영할 부분

기말 논문의 관련연구 표에서 IDS/IPS, IoT, IAM 관점의 RL 보안 연구 공백과 평가 지표 표준화 필요성을 설명하는 근거로 사용한다.
