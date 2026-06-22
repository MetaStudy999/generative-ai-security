# W03 위협모형

## 1. 대상 시스템

W03의 대상 시스템은 이미지 분류 모델, Vision Transformer 기반 비전 모델, 멀티모달 비전 모델, 2D/3D perception 모델을 포함하는 컴퓨터비전 AI 시스템이다. 본 주차 실험은 이 전체 범위를 직접 재현하지 않고 synthetic toy setting으로 평가 지표 구조만 설명한다.

## 2. 보호 자산

| 자산 | 설명 | W03 평가 연결 |
|---|---|---|
| 이미지 입력 | 모델 추론에 들어가는 2D/3D 또는 멀티모달 입력 | perturbation, physical patch, modality mismatch |
| 학습된 표현 | feature map, patch token, multimodal embedding | 표현 교란, attention/feature 취약성 |
| 모델 파라미터 | CNN/ViT/nearest-centroid 등 모델 내부 상태 | white-box/gray-box 가정 |
| 예측 출력 | class label, score, retrieval/generation 결과 | 오분류, target misclassification |
| 평가셋 | clean/adversarial/defense check 데이터 | clean/robust 지표 분리 |
| 로그와 설정 | seed, config, Docker, outputs, confusion matrix | 재현성 증거 |

## 3. 공격자 가정

| 구분 | 내용 | 본 보고서 처리 |
|---|---|---|
| White-box | 모델 구조, 파라미터, gradient 등 내부 정보를 안다고 가정 | 개념 수준 설명만 포함 |
| Gray-box | 일부 구조나 학습 조건만 안다고 가정 | 후속 확장 항목 |
| Black-box | 내부 정보 없이 입력/출력 관측 또는 transfer를 활용 | 개념 수준 설명만 포함 |
| Physical-world | 카메라, LiDAR, 3D 입력 등 현실 환경 변형 가능성 | P05 기반 위험 설명, 실행 제외 |

## 4. 공격자 능력

- 이미지 입력에 제한된 perturbation을 추가할 수 있다.
- 다른 모델에서 만든 교란이 전이될 수 있다.
- 멀티모달 시스템에서는 이미지와 텍스트 또는 다른 modality의 정합을 흔들 수 있다.
- 3D/physical perception에서는 센서 입력, 객체 형태, 환경 조건이 안전성 문제로 이어질 수 있다.

실제 운영 서비스 침해, 무단 API 질의, 개인정보 이미지 사용, 악용 가능한 단계별 공격 절차는 제외한다.

## 5. 공격 성공 조건

| 성공 조건 | 지표 |
|---|---|
| 예측이 정답에서 오답으로 바뀜 | ASR, robust accuracy |
| 특정 목표 클래스로 오분류됨 | target ASR, confusion matrix |
| 정상 성능 대비 공격 조건 성능 하락 | robust drop |
| 안전 영향 발생 가능성 | safety impact, failure mode |
| 평가 재현 불가 | missing seed/config/log/output |

## 6. W03 toy 실험에 적용한 축소 위협모형

| 항목 | 내용 |
|---|---|
| Dataset | synthetic 8x8 막대 이미지 |
| Model | nearest-centroid classifier |
| Attack | `centroid_direction_linf` toy perturbation |
| Defense/check | `feature_squeeze_2_levels` |
| Success criterion | clean에서 맞던 샘플이 perturbation 후 오분류되는 비율 |
| Excluded | 실제 CNN/ViT 공격, 실제 이미지, 운영 서비스, 개인정보 |

epsilon 0.45 결과는 synthetic two-class toy decision boundary 전환이며 실제 CNN/ViT 공격 성공으로 해석하지 않는다.

## 7. 연구문제 후보

RQ1. 비전 모델의 clean accuracy와 robust accuracy는 어떤 조건에서 분리 보고해야 하는가?

RQ2. CNN, ViT, 멀티모달 비전 모델의 구조 차이는 보안 평가 항목에 어떤 영향을 주는가?

RQ3. Synthetic toy experiment는 비전 대적공격 평가 프레임워크를 설명하는 데 어떤 장점과 한계를 가지는가?
