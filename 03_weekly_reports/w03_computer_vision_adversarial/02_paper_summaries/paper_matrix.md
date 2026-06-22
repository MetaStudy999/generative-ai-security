# W03 논문 5편 비교표

| 논문 | 연구문제 | 핵심 방법 | 데이터/실험 | AI 원리 기여 | 보안 위협 연결 | 평가 지표 | 한계 | 내 논문 활용 |
|---|---|---|---|---|---|---|---|---|
| P01 | CNN/gradient 기반 학습은 문자인식 문제를 어떻게 해결하는가 | CNN, convolution, subsampling, gradient-based learning, GTN | 문자인식/OCR 계열 실험 | CNN의 역사적 원리와 inductive bias | gradient 기반 공격과 표현 취약성의 배경 | recognition accuracy 등 원문 세부 수치 확인 필요 | 최신 ViT·대적공격 직접 분석은 아님 | CNN 원리와 gradient 기반 취약성 배경 |
| P02 | 딥러닝은 컴퓨터비전 문제에 어떻게 적용되어 왔는가 | CNN, DBN/DBM, autoencoder, CV task review | CV 응용 문헌 조사 | CV task와 딥러닝 구조 분류 | 비전 모델 실패가 안전성 문제로 확장 | task별 성능 지표 원문 확인 필요 | 보안 위협모형은 제한적 | CV 응용과 보안 평가 연결 |
| P03 | Transformer는 멀티모달 학습에서 어떻게 쓰이는가 | multimodal transformer survey, self-attention, pretraining taxonomy | image-text/video/audio/3D 등 문헌 조사 | 이미지-텍스트 정합과 attention 구조 | 멀티모달 입력 조작, 정합 실패, prompt/image mismatch | retrieval/classification/generation 지표 원문 확인 필요 | 보안 분석은 직접 중심이 아님 | 멀티모달 AI 보안 평가 축 |
| P04 | Vision Transformer는 CNN과 어떻게 다른가 | ViT 구조, attention, patch embedding, vision task taxonomy | vision transformer 문헌 조사 | CNN 대비 inductive bias 차이 | patch/attention 기반 취약성 논의 가능 | accuracy, efficiency, robustness 지표 원문 확인 필요 | 대적공격 전문 문헌은 아님 | ViT와 CNN 비교 배경 |
| P05 | 2D/3D deep learning model은 대적공격에 얼마나 취약한가 | adversarial attack/defense/safety survey, threat model | 2D/3D vision 문헌 비교 | 2D/3D 모델 안전성 평가 | white-box, black-box, physical, 3D attack | robust accuracy, ASR, defense success, safety impact | 실험 재현은 별도 필요 | W03 보안 위협모형과 평가방법 핵심 근거 |

## 종합 비교

### 1. AI 원리 중심 문헌과 보안 평가 중심 문헌

P01-P04는 AI 원리와 표현학습 구조를 설명하는 데 강하다. P01은 CNN과 gradient-based learning의 역사적 출발점이고, P02는 CV task 전반의 딥러닝 적용을 정리한다. P03은 멀티모달 Transformer, P04는 Vision Transformer를 통해 CNN 이후 표현학습 구조를 확장한다. 반면 P05는 2D/3D 비전 모델의 adversarial robustness와 safety를 직접 다루는 보안 평가 중심 문헌이다.

### 2. CNN과 ViT의 inductive bias 차이

CNN은 지역 receptive field, weight sharing, translation equivariance처럼 이미지 격자 구조에 맞춘 inductive bias를 강하게 갖는다. ViT는 이미지를 patch token sequence로 바꾸고 self-attention으로 전역 관계를 학습하므로, 더 약한 구조 가정과 더 큰 데이터/사전학습 의존성을 갖는다. 따라서 같은 clean accuracy라도 취약성 원인과 평가 항목은 구조별로 다를 수 있다.

### 3. 멀티모달 학습의 보안 리스크

P03이 다루는 멀티모달 Transformer는 이미지, 텍스트, 비디오, 오디오 등 여러 modality를 함께 처리한다. 이 구조에서는 이미지 교란뿐 아니라 텍스트-이미지 정합 실패, modality mismatch, retrieval 오염, prompt/image mismatch가 보안 리스크가 될 수 있다. W03의 단일 이미지 toy 실험은 이 리스크를 직접 재현하지 않으므로 후속 주차 연결 항목으로 남긴다.

### 4. clean accuracy와 robust accuracy 분리 필요성

P01-P04가 설명하는 표현학습 구조는 정상 조건 성능을 높이는 배경이지만, P05가 보여주는 보안 평가는 공격 조건 성능을 별도로 묻는다. 따라서 제출 보고서에서는 clean accuracy, robust accuracy, ASR, robust drop, confusion matrix를 분리해 보고한다. W03 outputs 기준 clean baseline은 accuracy 1.000000이고, epsilon 0.45 toy perturbation은 accuracy 0.000000, ASR 1.000000으로 기록된다.

### 5. synthetic toy 실험의 한계

W03 실험은 synthetic 8x8 막대 이미지와 nearest-centroid model을 사용한다. epsilon 0.45 결과는 실제 CNN/ViT 공격 성공이 아니라 두 클래스 toy decision boundary를 넘어선 결과다. 따라서 이 실험은 성능 주장보다 평가 지표 분리, 산출물 보존, 재현성 근거 기록 방식을 설명하는 예시로만 사용한다.
