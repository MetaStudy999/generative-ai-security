# P05 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 논문 제목 | Backdoor attacks and defenses in federated learning: Survey, challenges and future research directions |
| 저자 | Thuy Dung Nguyen, Tuan Nguyen, Phi Le Nguyen, Hieu H. Pham, Khoa D. Doan, Kok-Seng Wong |
| 공식 출판 정보 | Engineering Applications of Artificial Intelligence, 127, Article 107166, 2024 |
| DOI/URL | https://doi.org/10.1016/j.engappai.2023.107166; https://arxiv.org/abs/2303.02213 |
| PDF 파일명 | 05_Nguyen_et_al_2024_FL_Backdoor_Attacks_Defenses.pdf |
| 검증 상태 | arXiv preprint와 EAAI 출판 DOI 확인 |

## 2. arXiv판과 출판판 차이 메모

- arXiv:2303.02213은 2023-03-03 제출본이다.
- Crossref 기준 출판본은 2024년 Engineering Applications of Artificial Intelligence volume 127, Article 107166이다.
- 제목과 저자 구성은 실질적으로 동일하며, 최종 참고문헌에는 DOI 10.1016/j.engappai.2023.107166을 우선 사용한다.

## 3. 한 문장 요약

이 논문은 FL backdoor attack과 defense 연구를 survey하며, 악성 클라이언트 업데이트가 글로벌 모델의 특정 입력 행동을 바꿀 수 있는 위험과 방어 과제를 정리한다[5].

## 4. 연구문제

FL에서 backdoor가 왜 중앙집중 학습보다 검증하기 어려운지, 방어는 clean accuracy와 ASR을 어떻게 동시에 평가해야 하는지 다룬다. W10 toy 실험의 ASR 지표는 이 문헌을 직접 반영한다.

## 5. 핵심 개념

| 개념 | 설명 | 기말 논문 연결 |
|---|---|---|
| Backdoor attack | 특정 trigger 입력에서 목표 오동작을 유도하는 공격 | ASR 지표 |
| Malicious client | poisoned update를 제출하는 FL 참여자 | 악성 비율 실험 |
| Stealthiness | clean 성능을 크게 떨어뜨리지 않으면서 backdoor를 유지하는 특성 | clean accuracy와 ASR 동시 해석 |
| Backdoor defense | robust aggregation, update inspection 등 | coordinate median 비교 |

### 5.1 핵심 수식 또는 알고리즘 설명

| 항목 | 내용 |
|---|---|
| 수식/알고리즘 이름 | FL Backdoor Aggregation Risk |
| 원문 위치 | 논문 세부 절/쪽/그림/알고리즘 번호 확인 필요. 로컬 DOI/URL 점검표로 문헌 대응만 확인. |
| 작성 형식 | Markdown + LaTeX math |
| 검산 도구 | 사용 안 함 |
| 수식 또는 절차 | 표준 정의식 / 원문 직접 인용 아님.<br>$$w_{t+1}=\frac{1}{K}\left(\sum_{k\in H}w_k+\sum_{k\in A}w_k\right)$$ |
| 기호·입력·출력 | \(H\): honest clients, \(A\): adversarial clients, \(w_k\): client update 또는 local model |
| 직관적 의미 | FL Backdoor Aggregation Risk는 Federated Learning 보안 평가에서 핵심 원리나 평가 지표를 정량적으로 해석하기 위한 표준식이다. |
| 보안 관점 해석 | Federated Learning 보안 평가에서는 정상 성능과 보안 실패 조건을 분리해 보아야 한다. 이 항목은 공격·방어 원리 또는 운영 통제의 평가 기준을 명시하되, 실제 공격 절차나 무단 적용 단계는 포함하지 않는다. |
| 평가 지표와 연결 | ASR, clean accuracy, client fraction, robust aggregation success |
| 한계와 가정 | 표준 정의식 / 원문 직접 인용 아님. 논문별 변형, 정확한 수식 번호, 실험 설정은 원문 PDF에서 확인 필요다. |
| 기말 논문 반영 여부 | 반영 |

## 6. 보안 관점 분석

P05는 backdoor 평가에서 clean accuracy와 ASR을 분리해야 한다는 근거를 제공한다. W10 실험에서 20% poisoned FedAvg는 clean accuracy 0.950000을 유지하면서 ASR 0.496835를 보였고, coordinate median은 같은 20% 조건에서 ASR을 0.237342로 낮췄다. 단, 이 수치는 synthetic toy protocol 결과이며 실제 FL 제품 공격 성공률이 아니다.

## 7. 한계와 확인 필요

- P05 출판 DOI는 확인되었지만, 최종 제출 전 DOI landing page와 수업자료의 DOI 표기를 사람이 한 번 더 육안 확인하는 것이 좋다.
- W10은 실제 backdoor payload나 실제 FL 서비스 공격 절차를 포함하지 않는다.

## 8. 기말 논문에 반영할 부분

P05는 backdoor threat model과 ASR 평가 지표를 기말 논문의 방법론 장에 연결한다. 방어 비교에서는 clean accuracy만이 아니라 ASR 감소를 함께 기록해야 한다는 근거로 사용한다.
