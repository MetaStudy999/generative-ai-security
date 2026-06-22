# P02 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 강의계획서 표기 | H. Ren et al., "A Comprehensive Survey on Self-Supervised Learning", ACM Computing Surveys, 2025 |
| 현재 로컬 PDF 제목 | A Comprehensive Survey on Self-Supervised Learning for Recommendation |
| 저자 | Xubin Ren, Wei Wei, Lianghao Xia, Chao Huang |
| 출판 정보 | ACM Computing Surveys, 58(1), Article 22, 1-38, online 2025 |
| DOI/URL | `10.1145/3746280`; https://doi.org/10.1145/3746280 |
| 로컬 PDF | `02_Ren_et_al_2025_Self_Supervised_Learning_for_Recommendation.pdf` |
| 검증 상태 | DOI와 로컬 PDF 제목 확인. 강의계획서 지정 일반 SSL survey와 동일 여부 확인 필요 |

## 2. 주의 문구

주의: W05의 P02는 강의계획서 지정 일반 자기지도학습 종합 서베이와 동일 여부를 최종 확인해야 한다. 현재 로컬 PDF는 추천 시스템 분야의 Self-Supervised Learning survey로 범위가 좁으므로, 최종 제출 전 대체 문헌 사용 여부를 확인한다.

## 3. 한 문장 요약

현재 로컬 P02는 추천 시스템 맥락에서 contrastive, generative, adversarial SSL을 정리하는 도메인 특화 survey이며, W05에서는 사용자-아이템 표현과 데이터 거버넌스 위험을 설명하는 대체 또는 보조 문헌으로 쓰인다[2].

## 4. 핵심 연구문제

추천 시스템에서 데이터 희소성, 사용자-아이템 상호작용, 순차 추천, 그래프 구조를 활용해 어떻게 self-supervised signal을 만들고 추천 성능을 개선할 수 있는지 정리한다.

## 5. 핵심 기여

| 구분 | 내용 |
|---|---|
| Domain | 일반 SSL 전체가 아니라 recommender systems에 초점을 둔다 |
| 방법 축 | contrastive learning, generative learning, adversarial learning을 추천 시나리오별로 분류한다 |
| W05 연결 | 사용자-아이템 표현 오염, 추천 편향, 데이터 출처 관리, graph/user behavior augmentation 위험을 논의할 수 있다 |

## 6. 보안 관점

추천 시스템 SSL은 user-item graph, sequential behavior, item metadata, multimodal preference signal을 이용한다. 따라서 poisoned interaction, fake user behavior, graph augmentation 조작은 downstream ranking과 user representation을 왜곡할 수 있다. W05에서는 실제 추천 공격 절차가 아니라 데이터 거버넌스와 평가축 연결에만 활용한다.

## 7. 한계와 확인 필요

- 강의계획서 지정 제목에는 `for Recommendation`이 없으므로 현재 PDF를 지정 논문으로 확정하지 않는다.
- Crossref 검색에서 현재 DOI는 추천 SSL survey로 확인되었으나, 일반 SSL survey가 별도로 지정되었는지는 수업자료 원본 대조가 필요하다.
- 최종 제출 전 P02를 대체 문헌으로 유지할지, 지정 일반 SSL survey를 새로 확보할지 결정해야 한다.

## 8. 기말 논문 활용

기말논문에서 domain-specific SSL이 데이터 품질, 사용자 표현, 추천 편향, poisoned interaction 위험과 만나는 사례로 활용한다.
