# W06 발표자 노트

## 1. 표지

오늘 발표는 확률생성모형, 특히 diffusion과 GAN의 원리를 정리하고, 이를 딥페이크 탐지 신뢰성 평가로 연결합니다. 핵심 메시지는 in-domain accuracy 하나로 detector를 신뢰하면 안 된다는 점입니다.

## 2. 왜 중요한가

Diffusion과 GAN은 고품질 합성미디어를 만들 수 있습니다. 문제는 생성 품질이 올라갈수록 탐지 모델이 기존 artifact에 의존하기 어려워진다는 것입니다. 따라서 포렌식 관점에서는 domain shift와 불확실성을 함께 봐야 합니다.

## 3. Diffusion 원리

Diffusion model은 forward process에서 노이즈를 추가하고 reverse process에서 denoising을 수행합니다. Score-based 관점은 데이터 분포의 gradient를 이용해 sample을 복원하는 방식으로 이해할 수 있습니다.

## 4. GAN 원리

GAN은 generator와 discriminator가 경쟁합니다. Discriminator가 real/fake를 구분한다는 점에서 detector와 비슷해 보이지만, 연구용 discriminator와 포렌식 detector는 목적과 검증 기준이 다릅니다.

## 5. 보안 이슈

딥페이크 보안에서 중요한 위험은 두 가지입니다. 첫째, 실제 조작물을 놓치는 false negative입니다. 둘째, 진짜 미디어를 가짜로 판단하는 false positive입니다. 둘 다 피해가 크기 때문에 분리해서 기록해야 합니다.

## 6. 논문 5편의 역할

P01-P03은 diffusion, video diffusion, GAN 원리를 맡고, P04-P05는 딥페이크 생성·탐지와 reliability를 맡습니다. 이 다섯 편을 연결하면 생성모형 평가와 탐지 신뢰성 평가를 분리할 수 있습니다.

다만 P02와 P03은 발표에서 주의해서 말해야 합니다. DOI는 확인했지만, P02는 강의계획서의 지정 저자·제목과 현재 로컬 PDF가 같은지 확인이 필요하고, P03은 강의계획서 저자명과 출판사 저자명이 다릅니다.

## 7. 위협모형

흐름은 synthetic media가 detector score로 들어가고, threshold decision을 거쳐 review workflow로 이어지는 구조입니다. 공격 절차를 재현하지 않고, score가 이동했을 때 판단이 어떻게 흔들리는지만 봅니다.

## 8. 평가 프로토콜

평가 지표는 accuracy, F1, FPR, FNR, AUROC, ECE, auto coverage, review rate입니다. 특히 review rate를 기록해야 자동판정이 얼마나 많은 샘플에 적용됐는지 설명할 수 있습니다.

## 9. Toy 실험

실험은 synthetic score 분포입니다. 기준 도메인에서는 real score 평균이 0.22, fake score 평균이 0.78입니다. 이동 도메인에서는 real 평균이 0.34로 올라가고 fake 평균이 0.61로 내려가 margin이 줄어듭니다.

## 10. 결과

In-domain accuracy와 F1은 1.000000입니다. 하지만 cross-domain에서는 accuracy가 0.816667, FNR이 0.200000으로 나빠집니다. 즉 정상 benchmark만 보면 위험을 놓칠 수 있습니다.

## 11. Review-band

0.40-0.60 score를 human review로 넘기면 review rate는 0.358333이고 auto coverage는 0.641667입니다. 자동판정 범위에서 FPR은 0.050000, FNR은 0.135135로 낮아집니다. 실제 방어 증명이 아니라 workflow 설계 예시입니다.

## 12. 기말논문 연결

기말논문에서는 딥페이크 탐지기의 cross-domain reliability 평가 프레임워크로 연결할 수 있습니다. 관련연구, 위협모형, 평가방법, 실험 장에 모두 반영 가능합니다.

## 13. 결론

마지막으로 네 가지를 강조합니다. 생성 품질과 탐지 신뢰성은 다르고, accuracy 단독 평가는 위험하며, FPR/FNR과 review routing을 함께 기록해야 하고, 수치는 실행 로그가 있을 때만 주장해야 합니다.

<!-- formula-visual-speaker-notes:start -->
## 수식·그래프·그림 발표자 노트

- 핵심 수식: Diffusion Forward Process와 Denoising Objective, GAN Min-Max와 FPR/FNR. 수식은 표준 정의식이며, 원문 위치나 formal guarantee가 확인되지 않은 부분은 확인 필요로 말한다.
- 기호 정의표는 청중이 식을 해석할 수 있도록 먼저 읽고, 이후 보안 지표와 연결한다.
- 그래프 설명: 그래프는 deepfake detector의 accuracy, F1, FPR, FNR, AUROC를 조건별로 비교한다. 탐지 문제에서는 false positive와 false negative의 보안 비용이 다르므로 accuracy만으로 결론을 내리지 않는다. source는 `metrics_summary.csv`이다.
- 다이어그램 설명: `generated-media detection pipeline`는 threat model 또는 평가 pipeline을 한 장으로 보여주는 보조 그림이다.
- 한계 고지: 생성 모델 수식은 표준 학습 목적 설명이며 deepfake 제작 절차를 안내하지 않는다.
<!-- formula-visual-speaker-notes:end -->
