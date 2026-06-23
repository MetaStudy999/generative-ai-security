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

### 5.1 핵심 수식 또는 알고리즘 설명

| 항목 | 내용 |
|---|---|
| 수식/알고리즘 이름 | Watermark Utility Loss |
| 원문 위치 | 논문 세부 절/쪽/그림/알고리즘 번호 확인 필요. 로컬 DOI/URL 점검표로 문헌 대응만 확인. |
| 작성 형식 | Markdown + LaTeX math |
| 검산 도구 | 사용 안 함 |
| 수식 또는 절차 | 표준 정의식 / 원문 직접 인용 아님.<br>$$UtilityLoss=Acc_{clean}-Acc_{wm}$$ |
| 기호·입력·출력 | \(Acc_{clean}\): 기준 모델 정확도, \(Acc_{wm}\): 워터마크 삽입 후 정확도 |
| 직관적 의미 | Watermark Utility Loss는 Model Stealing·Watermarking 평가에서 핵심 원리나 평가 지표를 정량적으로 해석하기 위한 표준식이다. |
| 보안 관점 해석 | Model Stealing·Watermarking 평가에서는 정상 성능과 보안 실패 조건을 분리해 보아야 한다. 이 항목은 공격·방어 원리 또는 운영 통제의 평가 기준을 명시하되, 실제 공격 절차나 무단 적용 단계는 포함하지 않는다. |
| 평가 지표와 연결 | utility loss, TPR/FPR, robustness under transformation |
| 한계와 가정 | 표준 정의식 / 원문 직접 인용 아님. 논문별 변형, 정확한 수식 번호, 실험 설정은 원문 PDF에서 확인 필요다. |
| 기말 논문 반영 여부 | 반영 |

## 6. W13 활용

W13 실험의 trigger-set ownership check는 실제 production watermarking scheme이 아니라 dynamic watermarking 아이디어를 단순화한 deterministic toy ownership signal이다. 따라서 detection rate와 false positive rate를 함께 기록해야 한다.

## 7. 한계와 검토 필요

2021년 survey라 LLM 시대의 watermarking과 model extraction defense는 추가 문헌이 필요하다. 강의계획서의 `Feng Li` 표기가 현재 확보본과 다르므로 최종 제출 전 확인해야 한다.
