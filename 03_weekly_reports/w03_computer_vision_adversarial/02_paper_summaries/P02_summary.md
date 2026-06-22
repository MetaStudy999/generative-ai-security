# P02 요약: Deep Learning for Computer Vision: A Brief Review

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 논문 제목 | Deep Learning for Computer Vision: A Brief Review |
| 저자 | Athanasios Voulodimos, Nikolaos Doulamis, Anastasios Doulamis, Eftychios Protopapadakis |
| 학술지 | *Computational Intelligence and Neuroscience* |
| 권호/쪽 | 2018, Article ID 7068349, 13 pages |
| 연도 | 2018 |
| DOI/URL | https://doi.org/10.1155/2018/7068349 |
| PDF 파일명 | `02_Voulodimos_et_al_2018_Deep_Learning_Computer_Vision_Review.pdf` |
| 검증 상태 | Crossref/Hindawi URL 및 로컬 PDF 제목 일치 확인 |

## 2. 한 문장 요약

컴퓨터비전에서 CNN, DBN/DBM, autoencoder 계열 딥러닝 방법이 classification, detection, face recognition, action recognition, pose estimation 등으로 확장된 흐름을 정리한 짧은 리뷰 문헌이다.

## 3. 연구문제

딥러닝 구조가 컴퓨터비전 문제에 어떻게 적용되어 왔고, 각 구조가 어떤 task와 데이터 조건에서 의미를 갖는지를 분류한다.

## 4. 핵심 방법

| 요소 | 내용 | W03 연결 |
|---|---|---|
| CNN review | convolution, pooling, fully connected layer의 역할을 설명한다. | 비전 표현학습 기본 구조 |
| CV task 정리 | detection, recognition, action/activity recognition, pose estimation 등을 정리한다. | 보안 영향 범위 |
| 모델 계열 비교 | CNN 외 DBN/DBM, autoencoder를 함께 다룬다. | 딥러닝 비전 구조의 확장 |
| 미래 과제 | 데이터, 계산, 설계 과제를 요약한다. | 평가 프로토콜 필요성 |

## 5. AI 원리 기여

P02는 W03의 AI 원리 축에서 “컴퓨터비전 문제 공간”을 넓혀 준다. P01이 CNN/OCR의 역사적 출발점이라면, P02는 비전 딥러닝이 여러 task로 확장되며 평가 지표가 task별로 달라진다는 점을 보여준다.

## 6. 보안 위협 연결

보안 논문은 아니지만, 비전 모델이 얼굴 인식, 행동 인식, 자세 추정 등 안전·프라이버시 민감 영역에 쓰인다는 점에서 입력 교란, 데이터셋 편향, 모델 실패가 보안·안전 문제로 확장될 수 있음을 설명하는 배경이 된다.

## 7. 평가 지표와 한계

task별 성능 지표는 원문과 각 응용 분야에 따라 다르므로 W03 초안에서는 새로운 정량값을 만들지 않는다. P02는 보안 위협모형이나 adversarial robustness를 직접 중심으로 다루지 않기 때문에 P05와 함께 읽어야 한다.

## 8. 기말 논문 활용

비전 AI 시스템의 적용 영역을 분류하고, 보안 평가가 classification accuracy 하나로 끝나지 않는다는 논리의 배경 문헌으로 사용한다. clean performance와 attack impact를 task별로 분리해 기록해야 한다는 평가표 설계에 반영한다.
