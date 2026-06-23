# 발표자 대본

## 1. 제목

오늘은 W13 모델 지식재산, 모델 도난, 모델 추출 위협을 다룹니다. 핵심은 모델 추출 위험을 fidelity로 보고, 소유권 검증은 detection만이 아니라 false positive와 함께 해석해야 한다는 점입니다.

## 2. 오늘의 질문

API 뒤에 모델이 숨겨져 있어도 출력은 계속 노출됩니다. 그래서 입력과 출력을 반복해서 모으면 모델 행동을 어느 정도 모방할 수 있습니다. 동시에 워터마크 검출률이 높다고 해서 바로 강한 증거가 되는지도 따져봐야 합니다.

## 3. 문헌 역할과 검증 상태

P01은 모델 도난과 추출 taxonomy를 제공하며 DOI가 확인됐습니다. P03은 DNN 워터마킹 trade-off 문헌으로 DOI가 확인됐지만 강의계획서 표기 차이가 남아 있습니다. P04는 ModelShield로 extraction 이후 소유권 검증을 다루며 IEEE TIFS DOI가 확인됐습니다. P02와 P05는 로컬 PDF가 대체 문헌이라 보조 배경으로만 사용했습니다.

## 4. AI 원리

모델 IP는 파라미터만이 아니라 모델이 보이는 행동과 생성물 출처까지 포함합니다. 모델 추출은 query-response 정보를 모아 substitute model을 학습하는 과정입니다. 그래서 평가 지표로 victim과 substitute의 출력 일치율, 즉 fidelity를 둡니다.

## 5. 보안 이슈

모델 추출은 기밀성과 책임성을 흔듭니다. 워터마크는 소유권 검증을 돕지만 제거, 위조, 우연한 일치 가능성이 있습니다. 그래서 detection rate와 false positive rate를 같이 봐야 합니다.

## 6. Toy 실험 설계

실험은 실제 API가 아니라 synthetic binary classification입니다. victim은 toy logistic classifier이고 substitute는 query-response로 학습한 1NN classifier입니다. 워터마크는 20개 trigger-set signature로 단순화했습니다.

## 7. 실험 결과

query 100에서는 fidelity 0.864000, detection 0.700000입니다. query 500에서는 fidelity 0.920000, detection 1.000000입니다. query 1000에서는 fidelity 0.902000입니다. 1NN toy 구조라 단조 증가가 보장되지는 않습니다.

## 8. False Positive 해석

중요한 점은 false positive proxy가 0.600000으로 높다는 것입니다. 즉, detection이 높아도 오탐이 높으면 소유권 주장이 약합니다. 이 결과는 방어 성공 선언이 아니라 평가표에 FPR을 포함해야 한다는 근거입니다.

## 9. 기말논문 연결

기말논문으로는 모델 추출 이후 소유권 검증을 위한 다중지표 평가 프레임워크가 적절합니다. W14와 연결하면 API 로그와 운영 통제, W15와 연결하면 재현성·AI 활용 고지·문헌 검증으로 확장할 수 있습니다.

## 10. 결론

모델 IP 보호 평가는 공격 성공률 하나로 끝나지 않습니다. fidelity, detection, false positive, utility, 재현성을 함께 보고해야 합니다.

<!-- formula-visual-speaker-notes:start -->
## 수식·그래프·그림 발표자 노트

- 핵심 수식: Model Extraction Query Objective, Watermark Detection Rate, FPR/FNR, Utility Loss. 수식은 표준 정의식이며, 원문 위치나 formal guarantee가 확인되지 않은 부분은 확인 필요로 말한다.
- 기호 정의표는 청중이 식을 해석할 수 있도록 먼저 읽고, 이후 보안 지표와 연결한다.
- 그래프 설명: 그래프는 extraction_fidelity, substitute_accuracy, watermark_detection, false_positive_rate, utility_accuracy를 조건별로 비교한다. Watermark detection은 utility loss와 false positive risk를 함께 보아야 한다. 수치는 output CSV 그대로다.
- 다이어그램 설명: `model extraction and watermark audit flow`는 threat model 또는 평가 pipeline을 한 장으로 보여주는 보조 그림이다.
- 한계 고지: model extraction은 방어 평가 관점의 toy query objective로만 설명한다.
<!-- formula-visual-speaker-notes:end -->
