# P02 Summary

## Deep Learning for Computer Vision: A Brief Review — Athanasios Voulodimos et al., Computational Intelligence and Neuroscience, 2018

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W03 컴퓨터비전 표현학습 & 비전 대적공격 |
| 논문명 | Deep Learning for Computer Vision: A Brief Review |
| 저자 | Athanasios Voulodimos, Nikolaos Doulamis, Anastasios Doulamis, Eftychios Protopapadakis |
| 학술지 | Computational Intelligence and Neuroscience |
| 권호/쪽 | 2018, Article ID 7068349, 13 pages |
| 연도 | 2018 |
| DOI | https://doi.org/10.1155/2018/7068349 |
| 논문 유형 | Brief Review / Computer Vision Deep Learning Survey |
| 로컬 PDF | `01_papers/pdf/02_Voulodimos_et_al_2018_Deep_Learning_Computer_Vision_Review.pdf` |
| 강의계획서 지정 논문과 일치 여부 | 일치. 강의계획서의 `Apostolos Voulodimos` 표기는 Crossref/PDF 기준 `Athanasios Voulodimos`로 정정 |
| 핵심 근거 사용 가능 여부 | 가능 |
| 검증 메모 | W03 `paper_list.md` 기준 Crossref/Hindawi URL 및 로컬 PDF 제목 일치 확인 |

---

## 1. 한 문장 요약

이 논문은 CNN, deep belief network, autoencoder 등 딥러닝 구조가 **classification, object detection, face recognition, action recognition, pose estimation** 등 컴퓨터비전 과제로 확장된 흐름을 요약하고, 비전 AI 보안 평가가 단일 accuracy가 아니라 task별 위험과 지표를 구분해야 함을 보여주는 리뷰 문헌이다.

---

## 2. 연구문제

> 딥러닝 구조는 컴퓨터비전의 주요 task에 어떻게 적용되어 왔으며, 각 task의 데이터 구조와 평가 지표는 비전 AI 보안 평가에 어떤 차이를 만드는가?

| 번호 | 연구질문 |
|---|---|
| RQ1 | CNN과 기타 deep model은 컴퓨터비전 task별로 어떤 역할을 하는가? |
| RQ2 | Classification, detection, recognition, action recognition, pose estimation은 평가 지표와 실패 비용이 어떻게 다른가? |
| RQ3 | 비전 모델의 적용 영역이 보안·안전·프라이버시 민감 영역으로 확장될 때 어떤 위험이 생기는가? |
| RQ4 | 보안 평가에서 task별 clean metric과 attack metric을 왜 분리해야 하는가? |

---

## 3. 핵심 이론 및 수식

### 3.1 Softmax Classifier

비전 분류 모델은 logit $z_k$를 class 확률 $p_k$로 변환한다.

$$
p_k=\frac{e^{z_k}}{\sum_{j=1}^{K} e^{z_j}}
$$

| 기호 | 의미 |
|---|---|
| $z_k$ | class $k$의 logit |
| $p_k$ | class $k$의 예측 확률 |
| $K$ | 전체 class 수 |

### 3.2 Cross-Entropy Loss

분류 학습은 보통 정답 분포 $y$와 예측 분포 $p$의 cross-entropy를 최소화한다.

$$
CE(y,p)=-\sum_{k=1}^{K}y_k\log p_k
$$

| 기호 | 의미 |
|---|---|
| $y_k$ | 정답 one-hot label |
| $p_k$ | 모델의 class 확률 |
| $CE$ | cross-entropy loss |

### 보안적 의미

Softmax confidence는 모델의 불확실성과 공격 성공 여부를 분석하는 단서가 될 수 있다. 대적 교란은 정답 class의 logit을 낮추거나 공격 target class의 logit을 높이는 방식으로 예측을 바꿀 수 있다. 따라서 비전 보안 평가에서는 accuracy뿐 아니라 confidence, calibration, margin, robust accuracy를 함께 봐야 한다.

---

## 4. AI 원리 관점 분석

| 항목 | 분석 |
|---|---|
| CNN | 이미지의 지역성과 계층적 패턴을 학습하는 대표 비전 구조다. |
| DBN/DBM | 초기 deep generative/unsupervised representation learning 계열을 설명한다. |
| Autoencoder | 입력 재구성과 representation learning에 사용된다. |
| Classification | class prediction 중심 task로 clean/robust accuracy 평가가 가능하다. |
| Detection | 객체 위치와 class를 함께 예측하므로 IoU, mAP, localization error가 중요하다. |
| Face Recognition | identity 관련 프라이버시·인증 보안 위험과 연결된다. |
| Action Recognition | 시간적 패턴과 영상 데이터가 포함되어 입력 공격면이 넓어진다. |
| Pose Estimation | keypoint/localization 오차가 안전 문제로 이어질 수 있다. |

---

## 5. 보안 이슈 관점 분석

P02는 직접적인 공격 논문은 아니지만 비전 AI가 적용되는 task별 보안 영향 범위를 넓혀준다.

| 보안 항목 | CV task 관점 해석 |
|---|---|
| 무결성 | 이미지 분류·탐지 결과가 조작되면 의사결정이 왜곡된다. |
| 기밀성 | 얼굴 인식과 감시 시스템은 개인정보·민감정보와 연결된다. |
| 안전성 | 객체탐지·pose estimation 실패는 자율주행·로봇 안전 문제로 이어질 수 있다. |
| 가용성 | 오탐·미탐이 많으면 관제·인증·자동화 시스템의 신뢰성이 낮아진다. |
| 책임성 | task별 데이터, 모델, metric, 실패 사례를 기록해야 한다. |

---

## 6. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 대상 | 이미지, 영상, 얼굴 데이터, pose/keypoint, detection output, class probability |
| 공격자 목표 | 오분류, 객체 미탐, 얼굴 인증 우회, 행동 인식 왜곡, pose 오차 유도 |
| 공격자 능력 | 이미지 노이즈, patch, 조명·각도 변화, 배경 조작, 영상 frame 변조 |
| 공격 경로 | 입력 이미지/영상 → feature extraction → task head → decision |
| 제외 범위 | 실제 감시·인증 시스템 공격, 무단 데이터 수집, 개인정보 재식별 |

---

## 7. 평가방법 및 지표

| Task | Clean 지표 | 보안 확장 지표 |
|---|---|---|
| Classification | accuracy, F1 | robust accuracy, ASR, confidence margin |
| Detection | mAP, IoU | adversarial mAP drop, missed detection rate |
| Face Recognition | verification accuracy, FAR/FRR | spoofing success, privacy leakage risk |
| Action Recognition | top-1/top-5 accuracy | temporal perturbation robustness |
| Pose Estimation | keypoint error, PCK | safety-critical keypoint failure rate |

---

## 8. 재현성 점검

| 항목 | 점검 |
|---|---|
| 데이터셋 | MNIST, CIFAR-10, COCO, ImageNet subset, face/action public datasets 가능 |
| 모델 | CNN baseline, pretrained CV model, task-specific head |
| 전처리 | resize, normalization, augmentation, crop policy 기록 필요 |
| 평가 | task별 metric과 attack condition metric 분리 필요 |
| 결과 파일 | clean metric, robust metric, confusion matrix, failure case 저장 |
| 재현 가능성 판단 | classification toy 실험은 가능. detection/face/action/pose 전체 재현은 비용과 데이터 제약이 큼 |

---

## 9. 논문의 고유 기여

1. 컴퓨터비전 딥러닝 응용의 주요 task를 짧게 정리한다.
2. CNN 중심 비전 모델이 다양한 task로 확장되는 흐름을 제공한다.
3. Task별 평가 지표가 다르므로 보안 평가도 task별로 달라져야 함을 설명하는 배경이 된다.
4. 얼굴 인식, 행동 인식, pose estimation 등 보안·안전 민감 응용을 기말논문 위협모형으로 연결할 수 있게 한다.

---

## 10. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 짧은 리뷰 | 깊은 수학적 분석이나 최신 모델까지 모두 다루지는 않는다. | P03/P04/P05 survey와 결합한다. |
| 보안 직접성 부족 | adversarial robustness가 중심 주제는 아니다. | P05의 robustness/safety survey를 핵심 보안 근거로 사용한다. |
| 최신 foundation vision 미반영 | CLIP, multimodal LLM, modern ViT는 제한적으로만 연결된다. | W07/W08 및 P03/P04와 연결한다. |
| task별 수치 전사 제한 | 원문 task별 세부 수치를 임의 전사하지 않는다. | 기말논문에서는 지표 구조 중심으로 사용한다. |

---

## 11. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | 비전 AI의 응용 확산과 보안 영향 범위 제시 |
| 2장 관련연구 | CV task와 딥러닝 구조 개요 |
| 3장 위협모형 | task별 보호 대상과 공격 목표 정의 |
| 4장 연구방법 | classification/detection/recognition별 지표 분리 |
| 6장 보안적 함의 | 안전성, 프라이버시, 책임성 관점 해석 |

---

## 12. 기말논문 연결 3문장

1. 이 주차에서 기말논문에 반영할 개념: 컴퓨터비전 보안 평가는 task별 출력 구조와 실패 비용을 고려해야 하며 classification accuracy 하나로 끝나지 않는다.
2. 이 주차에서 기말논문에 반영할 표·그림·실험: CV task별 보호 대상·공격 목표·평가지표 비교표를 반영한다.
3. 이 주차가 RAG 문서 오염/LLM 보안 감사 프레임워크와 연결되는 지점: 비전 task별 입력·출력·평가 분리는 멀티모달 LLM과 RAG 이미지/문서 입력 보안 평가로 확장된다.

---

## 13. 최종 판단

이 논문은 W03의 CV 응용 범위를 넓히는 배경 문헌이다. 대적공격의 핵심 근거는 P05이지만, P02는 task별 평가 지표와 보안 영향 차이를 정리하는 데 유용하다.

---

## 14. 변환 호환성 메모

```bash
pandoc P02_summary.md -o P02_summary.docx
pandoc P02_summary.md -o P02_summary.pdf --pdf-engine=xelatex
```
