# P03 요약: Multimodal Learning With Transformers: A Survey

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 논문 제목 | Multimodal Learning With Transformers: A Survey |
| 저자 | Peng Xu, Xiatian Zhu, David A. Clifton |
| 학술지 | *IEEE Transactions on Pattern Analysis and Machine Intelligence* |
| 권호/쪽 | 45(10), 12113-12132 |
| 연도 | 2023 |
| DOI/URL | https://doi.org/10.1109/TPAMI.2023.3275156 |
| PDF 파일명 | `03_Xu_et_al_2023_Multimodal_Learning_Transformers_Survey.pdf` |
| 검증 상태 | Crossref/IEEE URL 및 로컬 PDF 제목 일치 확인 |

## 2. 한 문장 요약

Transformer 기반 멀티모달 학습을 modality-agnostic token 처리, self-attention, cross-modal interaction, multimodal pretraining 관점에서 정리한 survey 문헌이다.

## 3. 연구문제

이미지, 텍스트, 비디오, 오디오, 3D/point cloud 등 서로 다른 modality를 Transformer 구조 안에서 어떻게 표현하고 정렬하며, 어떤 응용과 공통 과제가 있는지를 체계화한다.

## 4. 핵심 방법

| 요소 | 내용 | W03 연결 |
|---|---|---|
| Self-attention | modality별 token 사이 관계를 attention으로 모델링한다. | 이미지-텍스트 정합 |
| Multimodal pretraining | 여러 modality를 공동 표현공간에 학습한다. | multimodal robustness |
| Application taxonomy | image-text, video, audio, 3D 등 응용을 분류한다. | 공격면 확장 |
| Challenge taxonomy | fusion, alignment, missing modality, noise 등을 정리한다. | 보안 실패 조건 |

## 5. AI 원리 기여

P03은 W03를 단일 이미지 분류에서 멀티모달 비전 시스템으로 확장한다. Transformer는 CNN보다 modality-specific inductive bias가 약하고, token과 attention 구조를 통해 서로 다른 입력을 통합할 수 있다.

## 6. 보안 위협 연결

멀티모달 시스템에서는 이미지 교란뿐 아니라 텍스트-이미지 불일치, modality mismatch, prompt/image 조작, retrieval 오염, 평가셋 정합 실패가 보안 리스크가 될 수 있다. P03은 공격 논문은 아니지만 W07 멀티모달 LLM 보안으로 이어지는 연결 축이다.

## 7. 평가 지표와 한계

retrieval, classification, generation, grounding 등 task별 지표가 다르므로 clean accuracy와 robust accuracy 외에도 alignment quality, retrieval recall, generation quality 같은 지표가 필요할 수 있다. 단, P03 자체는 adversarial robustness 정량 평가를 직접 중심으로 하지 않는다.

## 8. 기말 논문 활용

멀티모달 AI 보안 평가에서 입력 modality별 보호 자산과 실패 조건을 나누는 관련연구 근거로 사용한다. W03의 toy 실험은 단일 이미지 분류에 한정되므로, P03은 후속 확장 방향을 제시하는 문헌으로 반영한다.
