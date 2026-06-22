# AI 원리 70% 정리

## 1. 핵심 이론

W13의 AI 원리는 모델이 학습한 지식과 행동이 지식재산이 될 수 있다는 점에서 출발한다. 모델 도난은 넓게는 모델의 지식, 파라미터, 구조, 출력 행동을 무단으로 얻는 행위이고, 모델 추출은 특히 query-response 관찰을 이용해 대체 모델을 학습하거나 원 모델의 행동을 모방하는 절차를 뜻한다.

공개 API 기반 서비스에서는 사용자가 입력을 보내고 출력만 받는다. 그러나 출력 label, probability, embedding, text token이 반복적으로 모이면 공격자는 원 모델의 결정경계나 응답 패턴을 근사할 수 있다. 따라서 모델 IP 보호는 접근 제어만이 아니라 query budget, 출력 정보량, watermark/fingerprint, 이상 질의 탐지를 함께 설계해야 한다.

## 2. 핵심 개념표

| 개념 | 정의 | 직관적 설명 | 관련 논문 |
|---|---|---|---|
| Model IP | 학습 데이터, 파라미터, 구조, 하이퍼파라미터, 출력 행동에 반영된 경제적·기술적 가치 | 모델 자체가 연구·비용·데이터가 압축된 자산 | P01, P03 |
| Model Stealing | 모델 소유자의 허락 없이 모델 지식이나 행동을 획득하는 공격군 | 남의 모델을 베껴 쓰려는 시도 | P01 |
| Model Extraction | API 출력이나 응답 쌍으로 대체 모델을 학습하거나 원 모델 속성을 추정하는 절차 | 질문과 답을 많이 모아 비슷한 모델을 만드는 것 | P01, P04 |
| Query-response pairs | 입력과 원 모델 출력의 쌍 | substitute model의 학습 데이터 | P01, P04 |
| Model Fingerprinting | 모델 고유 행동 패턴을 이용해 소유권 또는 출처를 식별하는 방법 | 모델의 행동 지문 | P02, P03 |
| Model Watermarking | 모델 또는 생성물에 소유권 검증 신호를 삽입하는 방법 | 나중에 알아볼 수 있는 숨은 표식 | P02, P03, P04 |
| Robust Watermark | fine-tuning, pruning, editing, extraction 후에도 검출되는 워터마크 | 공격을 받아도 남는 표식 | P03, P04 |
| Adaptive Watermark | 출력 내용이나 공격 조건에 맞게 삽입·검출을 조정하는 워터마크 | 고정 규칙보다 유연한 표식 | P04 |
| Utility-Protection Trade-off | 워터마크/방어가 모델 품질을 떨어뜨릴 수 있는 상충관계 | 보호를 세게 하면 성능이 흔들릴 수 있음 | P02, P03, P04 |

## 3. 수식 또는 알고리즘

```text
1. 원 모델 f를 synthetic train data로 학습한다.
2. 소유권 검증용 trigger set W와 signature y_w를 정의한다.
3. 공격자 역할의 substitute model g는 query-response pairs (x, f(x))만 본다.
4. test set에서 fidelity = Pr[g(x) = f(x)]를 측정한다.
5. trigger set에서 watermark_detection = Pr[g(w) = y_w]를 측정한다.
6. 무관 clean model의 trigger 일치율을 false_positive proxy로 기록한다.
```

W13 실험에서 query budget 100, 500, 1000을 비교한 결과 extraction fidelity는 각각 0.864000, 0.920000, 0.902000이었다. 1-nearest-neighbor 기반 toy substitute라서 budget 증가가 항상 단조 개선을 보장하지는 않지만, query-response 정보만으로 victim behavior에 상당히 접근할 수 있음을 보여준다.

## 4. 초보자용 설명

모델 추출은 자판기 맛을 계속 보면서 비슷한 음료를 만드는 상황과 비슷하다. 내부 레시피를 보지 않아도 충분히 많은 입력과 출력을 모으면 비슷한 행동을 하는 대체 모델을 만들 수 있다. 워터마크는 “이 출력 패턴은 우리 모델에서 왔다”는 신호를 남기는 방법이지만, 오탐이 있으면 증거력이 약해진다.

## 5. 보안 연구와의 연결

모델 IP 보호 연구는 단순히 공격 성공률만 보지 않는다. W13에서는 extraction fidelity, substitute accuracy, watermark detection, false positive rate, utility accuracy를 함께 보고한다. 특히 false positive proxy가 0.600000으로 높게 측정되어, toy trigger-set만으로 강한 소유권 주장을 하기 어렵다는 한계도 함께 드러난다.
