# W05 발표자 노트

## 1. 표지

오늘 발표는 자기지도학습과 파운데이션 모델, 그리고 poisoning/backdoor 보안을 연결합니다. 핵심 메시지는 표현학습 기반 모델의 보안 평가는 clean 성능 하나로 설명할 수 없다는 점입니다.

## 2. 왜 중요한가

Foundation model은 대규모 pretraining 표현을 여러 task에 재사용합니다. 그래서 pretraining 데이터가 오염되거나 trigger가 표현공간을 특정 방향으로 이동시키면 downstream task까지 영향을 받을 수 있습니다.

## 3. Self-Supervised Learning 원리

자기지도학습은 사람이 직접 붙인 라벨 없이 데이터 자체에서 학습 신호를 만듭니다. 목표는 downstream task에 잘 전이되는 representation을 만드는 것입니다. 이 representation이 바로 W05의 보호 자산입니다.

## 4. 주요 방법

Contrastive learning은 positive pair와 negative pair의 거리를 이용합니다. Masked modeling은 입력 일부를 가리고 복원합니다. Predictive learning은 문맥이나 미래 상태를 예측합니다. 세 방법 모두 데이터 구성과 augmentation 품질에 민감합니다.

## 5. 보안 이슈

Poisoning은 학습 데이터나 pretraining corpus를 오염시키는 공격입니다. Backdoor는 평소에는 정상처럼 보이다가 trigger가 들어오면 target behavior를 유도합니다. 핵심 지표는 clean 성능과 ASR을 분리해 보는 것입니다.

## 6. 논문 5편의 역할

P01-P03은 자기지도학습과 video/recommendation 도메인의 표현학습 원리를 맡고, P04-P05는 poisoning과 backdoor의 공격·방어 taxonomy를 맡습니다. 원리 문헌과 보안 문헌을 연결해야 연구문제가 선명해집니다.

## 7. 위협모형

흐름은 pretraining data에서 SSL objective를 거쳐 embedding space와 downstream classifier로 이어집니다. 공격자는 poisoned sample이나 trigger를 넣고, 방어자는 데이터 검수, consistency check, 실행 로그 보존으로 대응합니다.

## 8. 평가 프로토콜

평가 지표는 clean accuracy, poisoned clean accuracy, ASR, mean shift, detection rate, clean FPR로 나눕니다. 이 구분이 있어야 정상 입력에서는 잘 동작하지만 trigger 조건에서는 실패하는 상황을 설명할 수 있습니다.

## 9. Toy 실험

실험은 실제 데이터나 실제 모델 공격이 아닙니다. synthetic 2D representation cluster를 만들고 nearest-centroid classifier로 clean 조건과 trigger 조건을 비교했습니다. 실행 결과는 outputs 폴더의 CSV, JSON, run_log에 있습니다.

## 10. 결과

Clean baseline accuracy는 1.000000입니다. Poisoned/backdoor 조건에서도 clean accuracy는 1.000000이지만, trigger 후 source embedding이 target centroid로 분류되어 ASR이 1.000000입니다. Consistency defense 후 ASR은 0.000000입니다.

## 11. 한계

이 결과는 toy 실험입니다. 실제 SSL 모델이나 foundation model의 보안 성능으로 일반화하면 안 됩니다. 발표에서 중요한 것은 수치 자체보다 지표 분리와 로그 근거를 갖춘 평가 구조입니다.

## 12. 기말논문 연결

기말논문에서는 표현학습 기반 AI 시스템의 poisoning/backdoor 평가 프레임워크로 연결할 수 있습니다. 관련연구, 위협모형, 평가방법, 분석/실험 장에 모두 반영 가능합니다.

## 13. 결론

마지막으로 네 가지를 강조합니다. 표현공간은 보호 자산이고, backdoor 평가는 clean 성능과 trigger 조건을 분리해야 하며, representation shift는 중요한 평가축이고, 수치는 실행 근거가 있을 때만 주장해야 합니다.
