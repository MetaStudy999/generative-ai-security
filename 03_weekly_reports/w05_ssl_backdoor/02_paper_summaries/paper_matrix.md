# W05 논문 5편 비교표

| 논문 | 연구문제 | 핵심 방법 | 데이터/실험 | AI 원리 기여 | 보안 위협 연결 | 평가 지표 | 한계 | 내 논문 활용 |
|---|---|---|---|---|---|---|---|---|
| P01 | 자기지도학습 알고리즘과 응용은 어떻게 분류되는가 | contrastive, generative, predictive SSL taxonomy | 이미지, 텍스트, 그래프 등 응용 문헌 조사 | SSL 전체 지도와 representation learning 원리 | pretraining corpus와 augmentation 단계가 공격면이 될 수 있음 | representation quality, transfer performance, downstream accuracy | 보안 위협모형 직접 중심은 아님. 강의계획서 `Yan Gui` 표기 확인 필요 | SSL/파운데이션 모델 원리 배경 |
| P02 | SSL을 추천 시스템에 어떻게 적용할 수 있는가 또는 일반 SSL을 어떻게 종합할 수 있는가 | recommendation SSL 또는 general SSL survey, contrastive/generative/adversarial SSL | recommendation data 또는 일반 SSL 문헌 | domain-specific SSL 구조 이해 | 사용자-아이템 표현 오염, 추천 편향, 데이터 거버넌스 위험 | ranking metrics, representation quality, downstream utility | 강의계획서 지정 일반 SSL survey와 동일 여부 확인 필요 | SSL 응용 도메인과 데이터 거버넌스 연결 |
| P03 | 비디오 표현학습에서 자기지도학습은 어떻게 작동하는가 | temporal consistency, contrastive video learning, cross-modal video SSL survey | video representation 문헌 조사 | temporal representation과 pretraining-transfer 평가 | 영상 trigger, temporal backdoor, augmentation poisoning 가능성 | downstream action recognition, retrieval, representation quality | 직접 보안 문헌은 아님. 강의계획서 제목과 ACM 제목 차이 기록 필요 | 영상 SSL과 피지컬/비전 보안 확장 |
| P04 | poisoning 공격과 방어는 ML training lifecycle에서 어떻게 분류되는가 | poisoning attack/defense taxonomy, threat model survey | ML poisoning 문헌 조사 | 학습 데이터 조작이 최적화와 일반화를 흔드는 구조 | data poisoning, clean-label poisoning, backdoor, federated poisoning | clean accuracy, ASR, attack impact, detection rate | 강의계획서 제목/저자와 현재 정식 제목 차이 확인 필요 | W05 보안 위협모형 핵심 근거 |
| P05 | Backdoor 공격과 방어는 DNN부터 LLM까지 어떻게 발전했는가 | backdoor attack/detection/removal/defense survey | DNN, vision, NLP, LLM backdoor 문헌 | foundation model backdoor까지 확장 | trigger injection, stealthiness, ASR, model editing/LLM backdoor 위험 | clean accuracy, ASR, trigger stealthiness, defense success | 최신 LLM backdoor는 계속 갱신 필요. 강의계획서 `Z. Jin` 표기 확인 필요 | clean accuracy-ASR 분리 평가 핵심 근거 |

## 종합 비교

1. P01-P03은 SSL/표현학습 원리와 응용 문헌이다. P01은 일반 SSL taxonomy, P02는 현재 로컬 PDF 기준 추천 시스템 SSL, P03은 video SSL을 담당한다.
2. P04-P05는 poisoning/backdoor 보안 문헌이다. P04는 training-time poisoning taxonomy, P05는 DNN부터 LLM까지 backdoor taxonomy를 제공한다.
3. W05의 핵심 연결부는 `pretraining representation이 보안 자산이 된다`는 점이다.
4. SSL에서는 라벨이 없어도 augmentation, positive/negative pair, corpus curation, pretraining pipeline이 공격면이 된다.
5. clean accuracy, ASR, representation shift, detection rate, clean FPR은 서로 다른 실패 양상을 측정하므로 분리해야 한다.
6. W05 toy 실험은 실제 SSL/foundation model 실험이 아니라 표현공간 평가축 설명용이다.

## 최종 제출 전 검토 필요

| 항목 | 상태 |
|---|---|
| P01 IEEE TPAMI DOI | 확인: `10.1109/TPAMI.2024.3415112` |
| P02 지정 논문 동일 여부 | 확인 필요 |
| P03 Article 번호 | 확인 필요 |
| P04 강의계획서 제목/저자와 동일 여부 | 확인 필요 |
| P05 강의계획서 저자 표기 | 확인 필요 |
