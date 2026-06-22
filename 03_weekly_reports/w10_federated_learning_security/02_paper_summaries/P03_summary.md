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

## 6. 보안 관점 분석

P03은 공격-방어 taxonomy와 실험 설계 난점을 함께 정리한다. W10에서는 실제 공격 절차를 재현하지 않고, malicious client rate와 aggregation rule을 바꿀 때 clean utility와 ASR이 어떻게 달라지는지 평가표 형식만 검증한다.

## 7. 한계와 확인 필요

- P03 출판 DOI는 확인되었지만, 최종 제출 전 DOI landing page와 수업자료의 DOI 표기를 사람이 한 번 더 육안 확인하는 것이 좋다.
- W10 toy 실험은 실제 FL framework, secure aggregation, DP, gradient inversion, membership inference를 구현하지 않는다.

## 8. 기말 논문에 반영할 부분

P03은 공격-방어 taxonomy와 평가 프로토콜의 중심 문헌으로 반영한다. 특히 clean utility와 attack impact를 동시에 기록해야 한다는 근거로 사용한다.
