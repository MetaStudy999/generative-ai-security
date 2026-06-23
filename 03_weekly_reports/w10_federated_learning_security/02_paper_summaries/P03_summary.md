# P03 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 논문 제목 | Survey on federated learning threats: Concepts, taxonomy on attacks and defences, experimental study and challenges |
| 저자 | Nuria Rodriguez-Barroso, Daniel Jimenez-Lopez, M. Victoria Luzon, Francisco Herrera, Eugenio Martinez-Camara |
| 공식 출판 정보 | Information Fusion, 90, pp. 148-173, 2023 |
| DOI/URL | https://doi.org/10.1016/j.inffus.2022.09.011; https://arxiv.org/abs/2201.08135 |
| PDF 파일명 | 03_Rodriguez_Barroso_et_al_2023_FL_Threats_Survey.pdf |
| 검증 상태 | arXiv preprint와 Information Fusion 출판 DOI 확인 |

## 2. arXiv판과 출판판 차이 메모

- arXiv:2201.08135는 2022-01-20 제출본이다.
- arXiv 페이지의 journal reference와 related DOI가 Information Fusion 출판본 DOI 10.1016/j.inffus.2022.09.011로 연결된다.
- Crossref 기준 출판본은 2023년 Information Fusion volume 90, pp. 148-173이다.
- 제목과 저자 구성은 실질적으로 동일하나, 최종 참고문헌에는 출판본의 저자명 세부 표기와 DOI를 우선 사용한다.

## 3. 한 문장 요약

이 논문은 FL adversarial threat와 defense taxonomy를 정리하고 실험 연구를 포함해, 공격 유형별 방어 선택 기준과 남은 과제를 제시한다[3].

## 4. 연구문제

FL에서 adversarial attack과 defense를 어떤 taxonomy로 짝지을 것인가를 다룬다. W10 실험에서는 이 논문을 근거로 malicious client rate, defense type, clean utility, ASR을 분리해 기록한다.

## 5. 핵심 개념

| 개념 | 설명 | 기말 논문 연결 |
|---|---|---|
| Attack taxonomy | FL privacy/integrity attack을 분류하는 체계 | threat model |
| Defense taxonomy | 공격 범주에 대응하는 방어법 분류 | evaluation protocol |
| Model integrity | 악성 업데이트가 글로벌 모델을 왜곡하는 위험 | poisoning 실험 |
| Data privacy | 분산 구조에서도 local data 단서가 노출될 수 있는 위험 | leakage proxy |

### 5.1 핵심 수식 또는 알고리즘 설명

이 논문은 수식 자체보다 분류체계, 평가 항목, 운영 절차가 핵심인 survey/review 성격이 강하다. 따라서 원문 기준으로 직접 반영할 핵심 수식은 제한적이다. 대신 본 요약에서는 다음 평가 지표 또는 알고리즘 절차를 개념 수준으로 정리한다.

| 항목 | 내용 |
|---|---|
| 핵심 절차/지표 | Federated Threat Taxonomy 점검 절차 |
| 원문 위치 | 논문 세부 절/쪽/그림/알고리즘 번호 확인 필요. 로컬 DOI/URL 점검표로 문헌 대응만 확인. |
| 보안 관점 해석 | Federated Learning 보안 평가에서는 정상 성능과 보안 실패 조건을 분리해 보아야 한다. 이 항목은 공격·방어 원리 또는 운영 통제의 평가 기준을 명시하되, 실제 공격 절차나 무단 적용 단계는 포함하지 않는다. |
| 평가 지표와 연결 | attack surface coverage, robustness/privacy metric, communication overhead |
| 기말 논문 반영 여부 | 참고만 |
| 절차 요약 | 1. 공격 위치를 client, server, communication, aggregation으로 구분<br>2. 목표를 privacy leakage, poisoning, backdoor, availability로 구분<br>3. 방어를 secure aggregation, DP, robust aggregation, anomaly detection으로 매핑<br>4. utility와 privacy/robustness 비용을 함께 기록 |
| 기호·입력·출력 | 입력: FL 시스템 구성과 공격자 권한, 출력: 위협-방어-지표 매핑 |
| 직관적 의미 | Federated Threat Taxonomy 점검 절차는 Federated Learning 보안 평가에서 수식보다 분류·운영·검증 흐름을 명시하는 데 초점을 둔다. |
| 한계와 가정 | survey/review 성격의 절차 요약이며, 원문 분류표의 세부 절·쪽 번호는 확인 필요다. |

## 6. 보안 관점 분석

P03은 공격-방어 taxonomy와 실험 설계 난점을 함께 정리한다. W10에서는 실제 공격 절차를 재현하지 않고, malicious client rate와 aggregation rule을 바꿀 때 clean utility와 ASR이 어떻게 달라지는지 평가표 형식만 검증한다.

## 7. 한계와 확인 필요

- P03 출판 DOI는 확인되었지만, 최종 제출 전 DOI landing page와 수업자료의 DOI 표기를 사람이 한 번 더 육안 확인하는 것이 좋다.
- W10 toy 실험은 실제 FL framework, secure aggregation, DP, gradient inversion, membership inference를 구현하지 않는다.

## 8. 기말 논문에 반영할 부분

P03은 공격-방어 taxonomy와 평가 프로토콜의 중심 문헌으로 반영한다. 특히 clean utility와 attack impact를 동시에 기록해야 한다는 근거로 사용한다.
