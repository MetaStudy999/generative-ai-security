# P03 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 로컬 PDF 논문 제목 | A survey of Deep Neural Network watermarking techniques |
| 저자 | Yue Li, Hongxia Wang, Mauro Barni |
| 학술지 | Neurocomputing |
| 공식 출판정보 | Vol. 461, pp. 171-193, 2021 |
| DOI/URL | `10.1016/j.neucom.2021.07.051`, `https://linkinghub.elsevier.com/retrieve/pii/S092523122101095X`, `https://arxiv.org/abs/2103.09274` |
| 강의계획서 표기 | Feng Li et al., "Deep neural network watermarking: Techniques and challenges", Neurocomputing, 2021 |
| 검증 상태 | 로컬 PDF의 DOI/출판정보 확인 완료. 강의계획서 저자명·제목 차이는 사람 검토 필요. |

## 2. 필수 주의문

주의: W13의 P03은 강의계획서 지정 저자명·제목과 현재 로컬 PDF 기준 저자명·제목이 다르므로, 동일 논문 여부와 최종 DOI를 확인 필요 상태로 유지한다. 단, 현재 로컬 PDF 자체의 공식 DOI는 `10.1016/j.neucom.2021.07.051`로 확인됐다.

## 3. 한 문장 요약

이 논문은 DNN 워터마킹을 multimedia watermarking의 fidelity, robustness, capacity trade-off와 비교하면서 static/dynamic watermarking, white-box/black-box 검출, backdoor 기반 워터마킹의 가능성과 한계를 정리한다[3].

## 4. 연구문제

고비용 학습과 독점 데이터로 만들어진 DNN 모델의 지식재산을 어떻게 보호할 수 있는가가 핵심 질문이다. 기존 멀티미디어 워터마킹 개념을 DNN 모델의 weight, activation, trigger behavior에 어떻게 이식할 수 있는지도 다룬다.

## 5. 핵심 개념

| 개념 | 설명 | W13 연결 |
|---|---|---|
| Fidelity | 워터마크 삽입 후 모델 성능 유지 | utility accuracy 해석 |
| Robustness | fine-tuning, pruning, extraction 이후 검출 유지 | watermark detection 지표 |
| Capacity | 삽입 가능한 watermark payload 크기 | 본 toy 실험 범위 밖 |
| Static/Dynamic watermarking | weight 기반 또는 입력-출력 행동 기반 검출 | trigger-set toy 설계 |
| False positive | 무관 모델이 소유 모델처럼 판단되는 위험 | ownership claim 한계 |

## 6. W13 활용

W13 실험의 trigger-set ownership check는 실제 production watermarking scheme이 아니라 dynamic watermarking 아이디어를 단순화한 deterministic toy ownership signal이다. 따라서 detection rate와 false positive rate를 함께 기록해야 한다.

## 7. 한계와 검토 필요

2021년 survey라 LLM 시대의 watermarking과 model extraction defense는 추가 문헌이 필요하다. 강의계획서의 `Feng Li` 표기가 현재 확보본과 다르므로 최종 제출 전 확인해야 한다.
