# P01 요약: Gradient-Based Learning Applied to Document Recognition

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 논문 제목 | Gradient-Based Learning Applied to Document Recognition |
| 저자 | Yann LeCun, Leon Bottou, Yoshua Bengio, Patrick Haffner |
| 학술지 | *Proceedings of the IEEE* |
| 권호/쪽 | 86(11), 2278-2324 |
| 연도 | 1998 |
| DOI/URL | https://doi.org/10.1109/5.726791 |
| PDF 파일명 | `01_LeCun_et_al_1998_Gradient_Based_Learning_Document_Recognition.pdf` |
| 검증 상태 | Crossref/IEEE URL 및 로컬 PDF 제목 일치 확인 |

## 2. 한 문장 요약

CNN과 gradient-based learning이 문자인식/OCR 문제에서 지역 연결, weight sharing, subsampling, end-to-end 학습을 통해 강력한 표현학습 구조가 될 수 있음을 보여준 고전 문헌이다.

## 3. 연구문제

핸드크래프트 특징 추출과 분리된 분류기 구조 대신, 픽셀 입력에서 직접 계층적 특징을 학습하는 gradient 기반 모델이 문자인식과 문서 인식 시스템을 얼마나 잘 해결할 수 있는지를 다룬다.

## 4. 핵심 방법

| 요소 | 내용 | W03 연결 |
|---|---|---|
| Convolution | 지역 receptive field와 weight sharing으로 이미지 구조를 반영한다. | CNN inductive bias |
| Subsampling/Pooling | 위치 변화에 대한 완만한 불변성을 만든다. | 시각 표현 안정성 |
| Gradient-based learning | 손실을 기준으로 전체 모델 파라미터를 조정한다. | gradient 기반 취약성 논의의 배경 |
| Graph Transformer Network | 여러 인식 모듈을 전체 목적함수 관점에서 연결한다. | end-to-end vision pipeline 평가 |

## 5. AI 원리 기여

P01은 W03의 AI 원리 축에서 CNN의 역사적 출발점이다. CNN은 이미지의 국소성과 공간 구조라는 inductive bias를 모델 구조에 넣기 때문에, 완전연결망보다 시각 패턴을 효율적으로 학습할 수 있다. 이 구조는 이후 이미지 분류, 객체탐지, OCR, 문서 인식, 의료 영상 등 많은 비전 응용의 기반이 되었다.

## 6. 보안 위협 연결

논문 자체는 현대적 adversarial attack 문헌이 아니지만, gradient 기반 학습과 이미지 표현 구조를 설명하기 때문에 gradient 기반 교란, decision boundary, feature representation 취약성을 이해하기 위한 배경 문헌으로 활용된다. 공격 절차나 실서비스 침해 방법은 본 보고서 범위에서 제외한다.

## 7. 평가 지표와 한계

원문은 문자인식/OCR 계열 실험을 포함하지만, W03 제출 초안에서는 원문 세부 실험 수치를 새로 전사하지 않았다. recognition accuracy 등 세부 수치는 최종 원문 쪽수 대조가 필요하다. 또한 이 논문은 CNN과 OCR 중심 고전 문헌이므로 ViT, 멀티모달 Transformer, 2D/3D adversarial robustness를 직접 분석하지 않는다.

## 8. 기말 논문 활용

CNN의 inductive bias와 gradient 기반 학습 원리를 설명하는 관련연구 배경으로 사용한다. W03 toy 실험에서는 nearest-centroid 모델을 쓰지만, clean accuracy와 robust accuracy를 분리해야 한다는 논리를 실제 CNN 평가로 확장할 때 P01을 출발점 문헌으로 연결할 수 있다.
