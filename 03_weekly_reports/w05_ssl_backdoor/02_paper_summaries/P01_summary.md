# P01 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 정식 제목 | A Survey on Self-Supervised Learning: Algorithms, Applications, and Future Trends |
| 저자 | Jie Gui, Tuo Chen, Jing Zhang, Qiong Cao, Zhenan Sun, Hao Luo, Dacheng Tao |
| 출판 정보 | IEEE Transactions on Pattern Analysis and Machine Intelligence, 46(12), 9052-9071, 2024 |
| DOI/URL | `10.1109/TPAMI.2024.3415112`; arXiv `10.48550/arXiv.2301.05712`; https://arxiv.org/abs/2301.05712 |
| 로컬 PDF | `01_Gui_et_al_2024_Self_Supervised_Learning_Survey.pdf` |
| 검증 상태 | TPAMI DOI와 arXiv DOI 확인. 강의계획서의 `Yan Gui` 표기는 `Jie Gui`와 다른 표기이므로 확인 필요 |

## 2. 한 문장 요약

이 논문은 contrastive, generative, predictive 계열을 포함해 자기지도학습 알고리즘과 응용을 넓게 분류하며, W05에서 SSL/foundation model 원리 배경을 제공한다[1].

## 3. 핵심 연구문제

라벨 없이 생성되는 pretext task와 representation learning 구조가 어떻게 발전했으며, 다양한 응용 도메인에서 어떤 공통 원리와 한계를 갖는지 정리한다.

## 4. 핵심 기여

| 구분 | 내용 |
|---|---|
| Taxonomy | SSL 알고리즘을 contrastive, generative, predictive/context 기반 관점으로 정리한다 |
| 응용 범위 | 이미지, 비전, 텍스트 등 다양한 downstream task와 transfer 구조를 연결한다 |
| W05 연결 | pretraining representation이 downstream task로 전이되는 구조를 보안 자산으로 해석할 수 있게 한다 |

## 5. 보안 관점

P01은 직접적인 poisoning/backdoor 방어 논문은 아니다. 다만 self-supervised pretraining에서 데이터 수집, augmentation, positive/negative pair, corpus curation이 모델 표현을 결정하므로, 이 단계가 공격면이 될 수 있음을 설명하는 배경 문헌으로 활용한다.

### 5.1 핵심 수식 또는 알고리즘 설명

| 항목 | 내용 |
|---|---|
| 수식/알고리즘 이름 | InfoNCE 대조학습 손실 |
| 원문 위치 | 논문 세부 절/쪽/그림/알고리즘 번호 확인 필요. 로컬 DOI/URL 점검표로 문헌 대응만 확인. |
| 작성 형식 | Markdown + LaTeX math |
| 검산 도구 | 사용 안 함 |
| 수식 또는 절차 | 표준 정의식 / 원문 직접 인용 아님.<br>$$\mathcal{L}_{InfoNCE}=-\log\frac{\exp(sim(z,z^+)/\tau)}{\exp(sim(z,z^+)/\tau)+\sum_{j=1}^{K}\exp(sim(z,z_j^-)/\tau)}$$ |
| 기호·입력·출력 | \(z\): anchor 표현, \(z^+\): positive 표현, \(z_j^-\): negative 표현, \(\tau\): temperature |
| 직관적 의미 | InfoNCE 대조학습 손실는 자기지도학습·Backdoor 평가에서 핵심 원리나 평가 지표를 정량적으로 해석하기 위한 표준식이다. |
| 보안 관점 해석 | 자기지도학습·Backdoor 평가에서는 정상 성능과 보안 실패 조건을 분리해 보아야 한다. 이 항목은 공격·방어 원리 또는 운영 통제의 평가 기준을 명시하되, 실제 공격 절차나 무단 적용 단계는 포함하지 않는다. |
| 평가 지표와 연결 | linear probe accuracy, transfer performance, backdoor ASR |
| 한계와 가정 | 표준 정의식 / 원문 직접 인용 아님. 논문별 변형, 정확한 수식 번호, 실험 설정은 원문 PDF에서 확인 필요다. |
| 기말 논문 반영 여부 | 반영 |

## 6. 한계와 확인 필요

- 로컬 PDF는 arXiv v4 첫 페이지를 포함하며 TPAMI 최종판과 세부 편집 차이가 있을 수 있다.
- 강의계획서의 `Yan Gui` 표기가 출판사 기준 `Jie Gui`와 동일 인물 표기 오류인지 사람 검토가 필요하다.
- 본 보고서는 수식을 설명용으로 사용하며, 원문 수식·그림 번호 직접 인용은 최종 제출 전 원문 페이지 대조가 필요하다.

## 7. 기말 논문 활용

기말논문의 배경 이론과 관련연구 장에서 SSL pretraining, representation learning, transfer evaluation의 기본 taxonomy로 활용한다.
