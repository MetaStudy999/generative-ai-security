# W11 발표자 대본

## 발표 기준

| 항목 | 내용 |
|---|---|
| 주차 | W11 |
| 주제 | 차등프라이버시(DP) & 멤버십 추론 공격·방어 |
| 권장 시간 | 8-10분 |
| 기준 슬라이드 | `presentation_slides.md`, `presentation_slides.html` |
| 수치 근거 | `04_experiment/outputs/run_log.md` |

## 표지. 발표 제목

예상 시간: 0:30

오늘의 질문은 “DP를 적용했다는 말을 어떻게 검증할 것인가”입니다. 결론은 단순합니다. DP 보장은 선언이 아니라 accounting, utility, MI risk, leakage, 재현성 로그가 함께 있어야 해석 가능합니다.

## 1. 왜 중요한가

예상 시간: 0:50

모델이 학습한 데이터 원문이 노출되지 않아도, 어떤 레코드가 학습에 포함되었는지 알 수 있으면 privacy breach가 될 수 있습니다. 그래서 W11은 accuracy가 아니라 privacy leakage와 membership risk를 함께 봅니다.

## 2. 발표 로드맵

예상 시간: 0:30

먼저 DP와 DP-SGD 원리를 설명하고, membership inference 위협으로 연결합니다. 이후 문헌 5편, 위협모형, toy 실험, 기말논문 연결 순서로 가겠습니다.

## 3. AI 원리

예상 시간: 1:20

DP는 인접 데이터셋의 출력 분포 차이를 제한하는 정의입니다. 딥러닝에서는 clipping, noise injection, privacy accounting이 결합된 DP-SGD가 대표 구현입니다. 단순히 noise를 넣는 것과 정식 DP 보장은 다릅니다.

## 4. 보안 이슈

예상 시간: 1:00

membership inference는 confidence나 loss 같은 신호를 보고 sample의 학습 포함 여부를 추론하는 문제입니다. 본 발표에서는 실제 개인 대상 절차가 아니라 synthetic split 기반 지표로만 다룹니다.

## 5. 논문 5편의 역할

예상 시간: 1:00

P01은 DP misuse, P02는 DP-DL auditing, P03은 DP 적용 위치, P04는 MI taxonomy, P05는 MI defense와 trade-off를 담당합니다. P01, P02, P04, P05의 DOI는 확인했고, P03도 DOI가 Neurocomputing 논문으로 연결됨을 확인했습니다. 다만 P03/P05는 로컬 PDF가 대체 문헌이므로 원문 확보 전까지 지정 논문처럼 인용하지 않습니다.

## 6. 위협모형

예상 시간: 0:55

보호 자산은 membership information, confidence score, model output, evaluation log입니다. 실제 개인정보, 운영 모델/API 무단 질의, 실제 개인 대상 추론은 제외합니다.

## 7. 평가 프로토콜

예상 시간: 1:00

평가표는 utility, membership risk, leakage, reproducibility를 함께 둡니다. 이 네 가지를 함께 봐야 privacy claim을 연구 문장으로 책임 있게 쓸 수 있습니다.

## 8. 실험 설계

예상 시간: 1:00

표준 라이브러리 기반 synthetic binary classification입니다. Non-DP baseline과 DP-like noise low, medium, high를 비교합니다. 여기서 epsilon은 정식 accountant 값이 아니라 proxy입니다.

`noise_multiplier`도 formal DP-SGD accountant 값이 아니라 toy gradient noise scale입니다.

## 9. 결과

예상 시간: 1:10

Baseline accuracy는 0.956250이고 high noise accuracy는 0.950000입니다. Leakage score는 medium noise에서 0.011769로 가장 낮았습니다. 그러나 high noise에서 MI attack accuracy는 0.521875로 단조 개선되지 않았습니다.

## 10. 해석

예상 시간: 0:50

이 결과는 noise가 항상 privacy proxy를 단조롭게 개선하지 않는다는 점을 보여줍니다. 그래서 formal accounting과 반복 평가가 필요합니다.

## 11. 기말논문 연결

예상 시간: 0:45

기말논문에서는 privacy claim 다중지표 평가 프레임워크로 연결합니다. 관련연구, 위협모형, 평가방법, 보안적 함의 장에 직접 들어갑니다.

## 12. 결론

예상 시간: 0:30

DP는 구현 설정과 accounting까지 보고해야 합니다. MI 위험은 별도 보안 지표로 평가해야 합니다. 수치는 `outputs/` 로그가 있을 때만 주장합니다.
