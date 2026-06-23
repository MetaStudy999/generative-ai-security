# W01 발표자 노트

## 발표 개요

- 권장 시간: 8-10분
- 발표 톤: 원리 설명 70%, 보안 연결 30%
- 핵심 문장: “W01은 딥러닝을 정확도 모델이 아니라 보안 평가가 필요한 ML 시스템으로 보는 기준 주차입니다.”

## Slide 1. 제목

오늘 발표는 1주차 주제인 딥러닝 패러다임과 ML 보안 분류학입니다. 핵심은 딥러닝의 원리를 먼저 정리하고, 그 원리가 왜 보안 평가와 연결되는지 설명하는 것입니다. 단순히 모델 성능이 높다는 말로는 보안성을 설명하기 어렵기 때문에, clean performance, robust performance, privacy leakage, reproducibility를 분리해서 보겠습니다.

## Slide 2. 왜 W01이 기준 주차인가

1주차는 이후 주차를 읽기 위한 공통 언어를 만드는 단계입니다. poisoning, adversarial example, privacy attack 같은 주제는 서로 달라 보이지만, 모두 데이터와 모델, 평가 과정의 특정 지점을 공격한다는 공통점이 있습니다. 그래서 W01에서는 “모델이 잘 맞는다”는 성능 중심 질문을 “보안적으로 어떤 조건에서 믿을 수 있는가”라는 질문으로 바꿉니다.

## Slide 3. 발표 로드맵

발표는 여섯 부분으로 진행하겠습니다. 먼저 딥러닝 원리를 정리하고, 그 다음 보안 이슈를 CIA와 ML 생명주기 관점에서 연결합니다. 이어서 논문 5편이 각각 어떤 역할을 하는지 설명하고, 마지막으로 실습 결과와 기말논문 연결 가능성을 말씀드리겠습니다.

## Slide 4. 딥러닝 원리 70%

딥러닝의 핵심은 표현학습입니다. 모델이 사람이 설계한 특징만 쓰는 것이 아니라 원시 입력에서 과제에 유용한 표현을 직접 학습합니다. 역전파는 이 표현을 조정하는 기본 메커니즘이고, 일반화는 학습 데이터 밖에서도 성능이 유지되는지를 뜻합니다. 보안 관점에서는 이 내부 표현과 결정 경계가 공격의 대상이 됩니다.

## Slide 5. 보안 이슈 30%

ML 보안 이슈는 CIA와 accountability로 나눠볼 수 있습니다. Confidentiality는 membership inference나 model inversion처럼 데이터가 새는 문제와 연결됩니다. Integrity는 adversarial example이나 poisoning처럼 예측 결과가 조작되는 문제입니다. Availability는 침입탐지에서 오탐이 폭증하거나 미탐이 늘어나는 문제로 나타납니다. Accountability는 seed, config, 로그가 없어서 결과를 검증하지 못하는 문제입니다.

## Slide 6. 논문 5편의 역할

P01은 딥러닝의 기본 원리를 제공합니다. P02는 ML 생명주기 전체에서 어떤 보증 증거가 필요한지 보여줍니다. P03은 침입탐지에서 accuracy만으로는 부족하고 오탐과 미탐을 분리해야 한다는 점을 보여줍니다. P04는 대적 공격과 방어의 taxonomy를 제공합니다. P05는 프라이버시 공격과 leakage risk 평가축을 제공합니다. 이 다섯 편을 합치면 단일 accuracy가 아니라 위협가정과 평가 지표, 재현성 증거를 함께 기록해야 한다는 결론이 나옵니다.

## Slide 7. ML 생명주기 위협모형

ML 시스템은 데이터, 학습, 검증, 배포, 모니터링 단계로 이어집니다. 데이터 단계에서는 라벨 품질과 민감정보 노출이 문제가 되고, 학습 단계에서는 poisoning과 overfitting이 문제가 됩니다. 검증 단계에서는 robust 평가나 leakage 평가가 빠질 수 있고, 배포 단계에서는 evasion이나 model extraction이 생길 수 있습니다. 운영 단계에서는 drift와 incident log 관리가 중요합니다.

## Slide 8. 평가 프레임

W01에서 제안한 평가축은 네 가지입니다. 정상 조건 성능인 clean performance, 공격이나 교란 조건에서의 robust performance, 민감 정보 노출 가능성을 보는 privacy leakage, 그리고 같은 결과를 다시 만들 수 있는 reproducibility입니다. 이 중 하나만 높다고 해서 안전한 ML 시스템이라고 말하기 어렵습니다.

## Slide 9. 실습 설계

실습은 안전한 synthetic toy evaluation으로 제한했습니다. 실제 개인정보나 실제 서비스에 대한 질의는 하지 않았습니다. 표준 라이브러리만 사용해 작은 logistic regression을 구현했고, clean baseline, label-noise training, toy feature perturbation, privacy-safe audit을 비교했습니다.

## Slide 10. 실습 결과

clean baseline의 accuracy는 약 0.869였습니다. 라벨 노이즈를 넣은 경우 약 0.839로 내려갔고, feature perturbation 조건에서는 약 0.844가 나왔습니다. 여기서 중요한 점은 정상 조건 성능 하나만 보면 라벨 품질이나 입력 교란의 영향을 설명하지 못한다는 것입니다. 보안 평가는 조건별로 성능을 나누어 봐야 합니다.

## Slide 11. Privacy-safe audit

privacy-safe audit에서는 train accuracy와 test accuracy의 차이를 확인했습니다. 이번 synthetic data에서는 train-test gap이 -0.012로 낮은 과적합 신호로 기록됐습니다. 다만 이것은 실제 데이터 대상 membership inference 공격이 아닙니다. 개인정보 없이 과적합과 confidence를 점검하는 안전한 대체 실습으로 해석해야 합니다.

## Slide 12. 한계와 오픈 문제

한계는 분명합니다. synthetic toy evaluation은 실제 운영망의 공격 표면을 대표하지 않습니다. 하지만 W01의 목적은 실제 공격을 수행하는 것이 아니라, 앞으로의 주차에서 쓸 평가 프레임을 만드는 것입니다. 결론적으로 딥러닝 원리는 보안 취약성의 기술적 배경이고, ML 보안은 생명주기 전체에서 clean, robust, privacy, reproducibility를 분리해 평가해야 합니다. 이 흐름은 기말논문의 “ML 생명주기 기반 AI 보안 평가 프레임워크”로 발전시킬 수 있습니다.

## Slide 13. 결론과 기말논문 연결

마지막 결론입니다. W01의 핵심은 딥러닝 원리를 보안 취약성의 기술적 배경으로 이해하고, ML 보안을 생명주기 전체에서 평가해야 한다는 점입니다. 특히 clean performance, robust performance, privacy leakage, reproducibility를 분리해 기록해야 합니다. 이 정리는 기말논문의 “ML 생명주기 기반 AI 보안 평가 프레임워크”로 자연스럽게 이어집니다.

<!-- formula-visual-speaker-notes:start -->
## 수식·그래프·그림 발표자 노트

- 핵심 수식: Empirical Risk와 Generalization Gap, Robust Accuracy와 ASR. 수식은 표준 정의식이며, 원문 위치나 formal guarantee가 확인되지 않은 부분은 확인 필요로 말한다.
- 기호 정의표는 청중이 식을 해석할 수 있도록 먼저 읽고, 이후 보안 지표와 연결한다.
- 그래프 설명: 그래프는 `metrics_summary.csv`의 condition별 accuracy와 F1만 시각화한다. Clean baseline, label-noise training, toy feature perturbation 조건을 같은 축에 두어 정상 성능만으로 보안성을 단정하기 어렵다는 점을 보여준다. synthetic/toy 평가 결과이므로 실제 운영 시스템 보증으로 해석하지 않는다.
- 다이어그램 설명: `ML lifecycle threat model`는 threat model 또는 평가 pipeline을 한 장으로 보여주는 보조 그림이다.
- 한계 고지: 원문 논문별 절·쪽·그림 번호와 formal guarantee 여부는 확인 필요.
<!-- formula-visual-speaker-notes:end -->
