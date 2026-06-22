# 발표자 대본

## 1. 제목

오늘은 W13 모델 지식재산, 모델 도난, 모델 추출 위협을 다룹니다. 핵심은 모델 추출 위험을 fidelity로 보고, 소유권 검증은 detection만이 아니라 false positive와 함께 해석해야 한다는 점입니다.

## 2. 오늘의 질문

API 뒤에 모델이 숨겨져 있어도 출력은 계속 노출됩니다. 그래서 입력과 출력을 반복해서 모으면 모델 행동을 어느 정도 모방할 수 있습니다. 동시에 워터마크 검출률이 높다고 해서 바로 강한 증거가 되는지도 따져봐야 합니다.

## 3. 문헌 역할

P01은 모델 도난과 추출 taxonomy를 제공합니다. P03은 DNN 워터마킹의 trade-off를 설명합니다. P04는 ModelShield로 extraction 이후 소유권 검증을 다룹니다. P02와 P05는 로컬 PDF가 대체 문헌이라 보조 배경으로만 사용했습니다.

## 4. AI 원리

모델 IP는 파라미터만이 아니라 모델이 보이는 행동과 생성물 출처까지 포함합니다. 모델 추출은 query-response 정보를 모아 substitute model을 학습하는 과정입니다. 그래서 평가 지표로 victim과 substitute의 출력 일치율, 즉 fidelity를 둡니다.

## 5. 보안 이슈

모델 추출은 기밀성과 책임성을 흔듭니다. 워터마크는 소유권 검증을 돕지만 제거, 위조, 우연한 일치 가능성이 있습니다. 그래서 detection rate와 false positive rate를 같이 봐야 합니다.

## 6. Toy 실험 설계

실험은 실제 API가 아니라 synthetic binary classification입니다. victim은 toy logistic classifier이고 substitute는 query-response로 학습한 1NN classifier입니다. 워터마크는 20개 trigger-set signature로 단순화했습니다.

## 7. 실험 결과

query 100에서는 fidelity 0.864000, detection 0.700000입니다. query 500에서는 fidelity 0.920000, detection 1.000000입니다. query 1000에서는 fidelity 0.902000입니다. 1NN toy 구조라 단조 증가가 보장되지는 않습니다.

## 8. 해석

중요한 점은 false positive proxy가 0.600000으로 높다는 것입니다. 즉, detection이 높아도 오탐이 높으면 소유권 주장이 약합니다. 이 결과는 방어 성공 선언이 아니라 평가표에 FPR을 포함해야 한다는 근거입니다.

## 9. 기말논문 연결

기말논문으로는 모델 추출 이후 소유권 검증을 위한 다중지표 평가 프레임워크가 적절합니다. W14와 연결하면 API 로그와 운영 통제, W15와 연결하면 재현성·AI 활용 고지·문헌 검증으로 확장할 수 있습니다.

## 10. 결론

모델 IP 보호 평가는 공격 성공률 하나로 끝나지 않습니다. fidelity, detection, false positive, utility, 재현성을 함께 보고해야 합니다.
