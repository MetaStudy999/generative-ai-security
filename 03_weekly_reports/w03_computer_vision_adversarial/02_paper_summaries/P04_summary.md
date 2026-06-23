# P04 요약: Transformers in Vision: A Survey

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 논문 제목 | Transformers in Vision: A Survey |
| 저자 | Salman Khan, Muzammal Naseer, Munawar Hayat, Syed Waqas Zamir, Fahad Shahbaz Khan, Mubarak Shah |
| 학술지 | *ACM Computing Surveys* |
| 권호/쪽 | 54(10s), 1-41 |
| 연도 | 2022 |
| DOI/URL | https://doi.org/10.1145/3505244 |
| PDF 파일명 | `04_Khan_et_al_2022_Transformers_in_Vision_Survey.pdf` |
| 검증 상태 | Crossref/ACM URL 및 로컬 PDF 제목 일치 확인 |

## 2. 한 문장 요약

Vision Transformer와 다양한 vision transformer 변형을 self-attention, patch/token representation, pretraining, vision task 적용 관점에서 정리한 survey 문헌이다.

## 3. 연구문제

NLP에서 성공한 Transformer가 이미지 인식, 탐지, 분할, 생성, 비디오, 3D vision 등 컴퓨터비전 문제에 어떻게 적용되며, CNN과 어떤 inductive bias 차이를 갖는지 다룬다.

## 4. 핵심 방법

| 요소 | 내용 | W03 연결 |
|---|---|---|
| Patch embedding | 이미지를 patch token sequence로 변환한다. | ViT 기본 구조 |
| Self-attention | 장거리 의존성과 전역 관계를 모델링한다. | CNN 대비 구조 차이 |
| Pretraining/fine-tuning | 대규모 데이터에서 표현을 학습하고 task에 맞춘다. | 평가 데이터와 재현성 |
| Vision task taxonomy | classification, detection, segmentation, generation, 3D 등을 정리한다. | 보안 평가 범위 |

## 5. AI 원리 기여

P04는 CNN과 ViT의 inductive bias 차이를 설명하는 핵심 문헌이다. CNN은 지역성과 translation equivariance를 구조적으로 강하게 반영하는 반면, ViT는 patch token과 attention을 통해 더 약한 구조 가정으로 전역 관계를 학습한다.

### 5.1 핵심 수식 또는 알고리즘 설명

| 항목 | 내용 |
|---|---|
| 수식/알고리즘 이름 | Vision Transformer Patch Embedding |
| 원문 위치 | 논문 세부 절/쪽/그림/알고리즘 번호 확인 필요. 로컬 DOI/URL 점검표로 문헌 대응만 확인. |
| 작성 형식 | Markdown + LaTeX math |
| 검산 도구 | 사용 안 함 |
| 수식 또는 절차 | 표준 정의식 / 원문 직접 인용 아님.<br>$$Z_0=[x_{cls};x_p^1E;x_p^2E;\cdots;x_p^NE]+E_{pos}$$ |
| 기호·입력·출력 | \(x_p^i\): image patch, \(E\): patch embedding, \(E_{pos}\): positional embedding |
| 직관적 의미 | Vision Transformer Patch Embedding는 컴퓨터비전·대적공격 평가에서 핵심 원리나 평가 지표를 정량적으로 해석하기 위한 표준식이다. |
| 보안 관점 해석 | 컴퓨터비전·대적공격 평가에서는 정상 성능과 보안 실패 조건을 분리해 보아야 한다. 이 항목은 공격·방어 원리 또는 운영 통제의 평가 기준을 명시하되, 실제 공격 절차나 무단 적용 단계는 포함하지 않는다. |
| 평가 지표와 연결 | clean/robust accuracy, patch corruption robustness, attention stability |
| 한계와 가정 | 표준 정의식 / 원문 직접 인용 아님. 논문별 변형, 정확한 수식 번호, 실험 설정은 원문 PDF에서 확인 필요다. |
| 기말 논문 반영 여부 | 반영 |

## 6. 보안 위협 연결

ViT의 patch/token 구조와 attention은 CNN과 다른 취약성 분석이 필요하다. patch-level perturbation, attention 교란, pretraining data 문제, transferability는 W03 보안 평가에서 별도 항목으로 분리할 수 있다. 단, P04는 대적공격 전문 survey가 아니므로 P05와 함께 사용한다.

## 7. 평가 지표와 한계

accuracy, efficiency, robustness, transferability 등 다양한 지표가 관련되지만, W03 초안에서는 원문 수치를 임의 전사하지 않는다. survey 문헌이므로 특정 모델의 보안 성능을 확정하는 근거로 과장하지 않는다.

## 8. 기말 논문 활용

CNN 기반 평가와 ViT 기반 평가의 차이를 관련연구와 평가 프로토콜에 반영한다. 특히 같은 clean accuracy라도 구조별 취약성 원인이 다를 수 있으므로 clean/robust/ASR 분리 기록의 필요성을 뒷받침한다.
