# W03 발표자 대본

## 발표 기준

| 항목 | 내용 |
|---|---|
| 주차 | W03 |
| 주제 | 컴퓨터비전 표현학습 & 비전 대적공격 |
| 권장 시간 | 8-10분 |
| 기준 슬라이드 | `presentation_slides.md`, `presentation_slides.html` |
| 수치 근거 | `04_experiment/outputs/run_log.md` |

## 표지. W03 컴퓨터비전 표현학습 & 비전 대적공격

예상 시간: 0:30

오늘 발표의 핵심은 비전 모델을 평가할 때 clean accuracy 하나만으로는 충분하지 않다는 점입니다. 정상 입력에서의 성능, 공격 조건에서의 성능, ASR, 그리고 결과를 다시 확인할 수 있는 실행 로그를 분리해서 봐야 합니다.

## 1. 왜 W03가 중요한가

예상 시간: 0:45

이미지 모델은 분류, 검색, 인식, 멀티모달 AI의 기반이 됩니다. 그런데 정상 테스트셋에서 잘 맞는 모델도 아주 작은 입력 변화에는 취약할 수 있습니다. 그래서 W03의 질문은 “모델이 이미지를 잘 본다”는 말이 보안적으로도 충분한가입니다. 발표에서는 좋은 표현학습과 안전한 모델 사이의 간격을 중심으로 설명하겠습니다.

## 2. 발표 로드맵

예상 시간: 0:30

발표는 여섯 부분으로 진행합니다. 먼저 컴퓨터비전 표현학습 원리를 보고, CNN과 ViT의 차이를 짚습니다. 그 다음 비전 대적공격의 위협모형을 정리하고, 논문 5편이 어떤 역할을 하는지 연결합니다. 마지막으로 toy 실험 결과와 기말논문 연결점을 설명합니다.

## 3. AI 원리 70%: CNN

예상 시간: 1:00

CNN은 지역 receptive field와 convolution을 통해 이미지의 공간적 특징을 학습합니다. 얕은 계층은 edge나 texture처럼 낮은 수준의 패턴을 잡고, 깊은 계층은 shape나 object-level 표현을 학습합니다. 보안 관점에서 중요한 점은 입력 픽셀의 작은 변화가 feature map과 decision boundary를 바꿀 수 있다는 것입니다.

## 4. AI 원리 70%: ViT와 멀티모달 표현

예상 시간: 1:00

ViT는 이미지를 patch token으로 나누어 attention으로 처리합니다. CNN과 inductive bias가 다르기 때문에 취약성도 다르게 나타날 수 있습니다. 또 멀티모달 모델에서는 이미지와 텍스트 표현공간이 정렬되므로, 입력 이미지 조작은 단순 분류 오류뿐 아니라 이미지-텍스트 정합 실패로도 이어질 수 있습니다.

## 5. 보안 이슈 30%

예상 시간: 1:00

비전 대적공격은 공격자의 지식과 접근 권한에 따라 white-box, black-box, transfer attack 등으로 나뉩니다. 정상 성능이 높더라도 공격 조건에서 robust accuracy가 낮아지거나 ASR이 높아질 수 있습니다. 그래서 보안 평가는 clean performance와 attack impact를 반드시 분리해야 합니다.

## 6. 논문 5편의 역할

예상 시간: 0:50

이번 주차의 문헌은 원리와 보안을 나누어 읽습니다. P01과 P02는 CNN과 컴퓨터비전 딥러닝의 원리 배경을 제공합니다. P03과 P04는 멀티모달 transformer와 Vision Transformer 관점에서 표현학습을 확장합니다. P05는 2D/3D adversarial robustness를 통해 보안 평가축을 제공합니다. 이 다섯 편을 연결해야 “성능 좋은 비전 모델”을 “보안적으로 평가 가능한 비전 모델”로 바꿔 볼 수 있습니다.

## 7. 위협모형

예상 시간: 0:55

이 슬라이드는 입력 이미지, 모델, 예측값, 평가 로그를 하나의 흐름으로 둡니다. 공격자는 입력 교란, 모델 접근, 목표 오분류, 결과 검증 누락 같은 경로를 이용할 수 있습니다. 방어자는 seed, config, log를 남기고, 실제 서비스 공격이 아닌 toy/synthetic 범위에서 안전하게 평가한다는 가정을 둡니다.

## 8. 평가 프로토콜

예상 시간: 0:55

평가는 정상 성능, 공격 영향, 강건 성능, 재현성, 사람 검토로 나누어 기록합니다. 특히 실험값은 CSV, JSON, run log로 남겨야 합니다. 단일 accuracy 표만 있으면 어떤 조건의 값인지 알기 어렵기 때문에, 조건별 평가표가 필요합니다.

## 9. Toy 실험 설계

예상 시간: 0:55

실험은 synthetic 8x8 vertical/horizontal bar image로 구성했습니다. 모델은 nearest-centroid classifier이고, 공격은 반대 클래스 중심점 방향의 L-infinity perturbation입니다. 방어 점검으로는 2-level feature squeezing을 사용했습니다. 이 실험은 실제 CNN/ViT 성능을 주장하기 위한 것이 아니라, 평가 지표와 로그 구조를 보여주기 위한 안전한 toy 실험입니다.

## 10. Toy 실험 결과

예상 시간: 1:10

정량값은 `04_experiment/outputs/run_log.md` 기준입니다. Clean baseline은 accuracy와 macro F1이 모두 1.000000입니다. Epsilon 0.30 perturbation에서는 accuracy 1.000000, ASR 0.000000으로 변화가 없었습니다. Epsilon 0.45에서는 accuracy와 macro F1이 0.000000이고 ASR이 1.000000입니다. Feature squeezing eps 0.30은 accuracy 1.000000, ASR 0.000000입니다.

## 11. 결과 해석과 한계

예상 시간: 0:55

Epsilon 0.45에서 모든 샘플이 오분류된 것은 이 toy 데이터에서 결정 경계를 넘어섰다는 뜻입니다. 하지만 이 결과를 실제 CNN, ViT, 2D/3D 비전 시스템 전체의 강건성으로 일반화하면 안 됩니다. 핵심은 수치 자체보다 clean 성능, 공격 영향, 재현성 근거를 분리해서 기록하는 방식입니다.

## 12. 기말논문 연결

예상 시간: 0:45

W03는 기말논문에서 관련연구, 위협모형, 평가방법, 분석/실험 장으로 이어질 수 있습니다. 특히 “AI 보안 평가 프레임워크”라는 contribution을 만들 때, 정상 성능과 공격 조건 성능, 재현성 근거를 분리하는 사례로 사용할 수 있습니다.

## 13. 결론

예상 시간: 0:40

결론은 네 가지입니다. 첫째, 비전 모델의 정상 성능은 보안성을 보장하지 않습니다. 둘째, 공격 조건 성능과 ASR을 따로 기록해야 합니다. 셋째, 실행 로그, config, seed, CSV/JSON 산출물이 있어야 수치를 주장할 수 있습니다. 넷째, W03는 기말논문의 재현성 중심 평가 프레임워크를 보강하는 사례입니다.

## 발표 마무리 멘트

질문에서는 toy 실험의 한계, 실제 CNN/ViT 확장 가능성, feature squeezing의 의미, 그리고 ASR을 accuracy와 분리하는 이유를 중심으로 답변하면 됩니다.

<!-- formula-visual-speaker-notes:start -->
## 수식·그래프·그림 발표자 노트

- 핵심 수식: Adversarial Perturbation Constraint, Robust Accuracy와 Robust Drop. 수식은 표준 정의식이며, 원문 위치나 formal guarantee가 확인되지 않은 부분은 확인 필요로 말한다.
- 기호 정의표는 청중이 식을 해석할 수 있도록 먼저 읽고, 이후 보안 지표와 연결한다.
- 그래프 설명: 그래프는 condition별 accuracy, attack_success_rate, robust_drop을 `metrics_summary.csv`에서 읽어 시각화한다. epsilon 또는 defense 조건별 변화는 robust accuracy를 clean accuracy와 분리해 보아야 함을 보여준다. 이미 존재하는 output 수치만 사용했다.
- 다이어그램 설명: `adversarial evaluation flow`는 threat model 또는 평가 pipeline을 한 장으로 보여주는 보조 그림이다.
- 한계 고지: 대적 교란은 toy evaluation 범위로 설명하며 실제 시스템 우회 절차로 쓰지 않는다.
<!-- formula-visual-speaker-notes:end -->
