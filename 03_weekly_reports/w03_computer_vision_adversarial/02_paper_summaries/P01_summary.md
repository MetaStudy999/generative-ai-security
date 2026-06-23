# P01 Summary

## Gradient-Based Learning Applied to Document Recognition — Yann LeCun, Léon Bottou, Yoshua Bengio, Patrick Haffner, Proceedings of the IEEE, 1998

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W03 컴퓨터비전 표현학습 & 비전 대적공격 |
| 논문명 | Gradient-Based Learning Applied to Document Recognition |
| 저자 | Yann LeCun, Léon Bottou, Yoshua Bengio, Patrick Haffner |
| 학술지 | Proceedings of the IEEE |
| 권호/쪽 | Vol. 86, No. 11, pp. 2278–2324 |
| 연도 | 1998 |
| DOI | https://doi.org/10.1109/5.726791 |
| 논문 유형 | Classical Review / CNN and Document Recognition System Paper |
| 로컬 PDF | `01_papers/pdf/01_LeCun_et_al_1998_Gradient_Based_Learning_Document_Recognition.pdf` |
| 강의계획서 지정 논문과 일치 여부 | 일치 |
| 핵심 근거 사용 가능 여부 | 가능 |
| 검증 메모 | W03 `paper_list.md` 기준 Crossref/IEEE URL 및 로컬 PDF 제목 일치 확인 |

---

## 1. 한 문장 요약

이 논문은 문자인식과 문서인식 문제에서 CNN과 gradient-based learning을 결합하여 **지역 연결, weight sharing, subsampling, end-to-end 학습, Graph Transformer Network**가 픽셀 입력에서 계층적 표현을 직접 학습할 수 있음을 보여준 컴퓨터비전 딥러닝의 고전 핵심 문헌이다.

---

## 2. 연구문제

> 수작업 특징 추출과 분리된 분류기 대신, 입력 이미지에서 직접 계층적 특징을 학습하는 gradient 기반 신경망이 문자인식·문서인식 시스템을 얼마나 효과적으로 구성할 수 있는가?

| 번호 | 연구질문 |
|---|---|
| RQ1 | CNN은 문자인식에서 지역성, 공간 구조, 가중치 공유를 어떻게 활용하는가? |
| RQ2 | End-to-end gradient-based learning은 특징 추출기와 분류기를 어떻게 통합하는가? |
| RQ3 | Subsampling/pooling은 위치 변화와 왜곡에 대해 어떤 안정성을 제공하는가? |
| RQ4 | Gradient 기반 학습 구조는 현대 비전 대적공격의 어떤 이론적 출발점이 되는가? |
| RQ5 | 문서인식 pipeline의 모듈화와 전체 목적함수는 오늘날 AI 보안 평가에서 어떤 재현성 요구로 이어지는가? |

---

## 3. 핵심 이론 및 수식

> 작성 원칙: GitHub, MS Word, PDF 변환 호환성을 위해 수식은 표 안에 넣지 않고 별도 블록 수식으로 작성한다. 변수 설명은 Markdown 표로 분리한다.

### 3.1 2D Convolution

CNN의 기본 연산은 입력 특징맵의 국소 영역에 같은 kernel을 반복 적용하는 convolution이다.

$$
Y_{i,j,k}=b_k+\sum_{u,v,c}W_{u,v,c,k}X_{i+u,j+v,c}
$$

| 기호 | 의미 |
|---|---|
| $X$ | 입력 이미지 또는 입력 특징맵 |
| $Y$ | 출력 특징맵 |
| $W_{u,v,c,k}$ | 위치 $(u,v)$, 채널 $c$, 출력 채널 $k$의 convolution kernel |
| $b_k$ | 출력 채널 $k$의 bias |
| $i,j$ | 출력 공간 위치 |
| $c$ | 입력 채널 |

### 보안적 의미

Convolution은 이미지의 지역 패턴을 효율적으로 학습하지만, 같은 kernel이 전체 이미지에 반복 적용되므로 특정 국소 패턴이나 patch가 모델 예측에 과도한 영향을 줄 수 있다. 이는 adversarial patch, localized perturbation, physical sticker 공격을 해석하는 출발점이 된다.

---

### 3.2 Subsampling / Pooling

Pooling은 근처 영역의 정보를 요약하여 작은 위치 변화에 대한 완만한 불변성을 제공한다.

$$
Y_{i,j,k}=\operatorname{pool}\left(\{X_{a,b,k}:(a,b)\in \mathcal{N}(i,j)\}\right)
$$

| 기호 | 의미 |
|---|---|
| $\operatorname{pool}$ | max 또는 average pooling 연산 |
| $\mathcal{N}(i,j)$ | 출력 위치 $(i,j)$에 대응하는 입력 이웃 영역 |
| $k$ | 채널 인덱스 |

### 보안적 의미

Pooling은 작은 이동에 대한 안정성을 제공하지만, 모든 형태의 교란에 강건성을 보장하지는 않는다. 작은 $L_p$ 교란, patch 공격, 배경 변화, 이미지 변환 공격에서는 pooling만으로 robust performance를 보장할 수 없다.

---

### 3.3 Gradient-Based Learning

End-to-end 학습은 전체 목적함수의 gradient를 통해 각 층의 파라미터를 갱신한다.

$$
\theta_{t+1}=\theta_t-\eta_t\nabla_{\theta}\mathcal{L}(f_{\theta_t}(x),y)
$$

| 기호 | 의미 |
|---|---|
| $\theta_t$ | $t$번째 반복의 모델 파라미터 |
| $\eta_t$ | 학습률 |
| $\mathcal{L}$ | 학습 손실 |
| $f_{\theta_t}$ | 현재 파라미터의 모델 |

### 보안적 의미

Gradient는 학습의 핵심 도구이지만, 입력에 대한 gradient는 공격자가 모델 예측을 교란하는 방향을 추정하는 데에도 활용될 수 있다. 따라서 W03에서는 gradient-based learning을 대적공격의 기술적 배경으로 함께 해석한다.

---

## 4. AI 원리 관점 분석

| 항목 | 분석 |
|---|---|
| Local Receptive Field | 이미지의 국소 구조를 활용해 parameter 수를 줄이고 공간 패턴을 학습한다. |
| Weight Sharing | 같은 kernel을 전체 공간에 공유하여 translation equivariance를 제공한다. |
| Subsampling | 작은 위치 변화에 대한 표현 안정성을 높인다. |
| End-to-End Learning | 특징 추출과 분류를 하나의 목적함수 아래 학습한다. |
| Graph Transformer Network | 여러 인식 모듈을 전체 pipeline으로 결합해 문서 인식 문제를 처리한다. |
| Inductive Bias | CNN은 이미지의 지역성·공간성에 강한 구조 가정을 가진다. |

---

## 5. 보안 이슈 관점 분석

P01은 현대 adversarial attack 논문은 아니지만, 비전 모델의 공격면을 이해하는 기반을 제공한다.

| 보안 항목 | CNN/OCR 관점 해석 |
|---|---|
| 무결성 | 입력 이미지의 작은 교란이 분류 결과를 바꿀 수 있다. |
| 가용성 | 오탐·미탐이 누적되면 문서 자동처리 pipeline의 신뢰성이 낮아진다. |
| 안전성 | OCR, 번호판 인식, 문서 인증 등에서 오인식은 보안 사고로 이어질 수 있다. |
| 책임성 | 학습 데이터, 전처리, 모델 버전, 평가셋을 기록해야 결과 검증이 가능하다. |
| 물리 공격면 | 인쇄물, 스캔 품질, 왜곡, 노이즈, patch가 입력 공격면이 될 수 있다. |

---

## 6. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 대상 | 문서 이미지, 문자 라벨, OCR 모델, 전처리 pipeline, 인식 결과 |
| 공격자 목표 | 오인식 유도, 특정 문자/숫자 오분류, 문서 처리 오류 유발 |
| 공격자 능력 | 이미지 노이즈 추가, patch 삽입, 스캔 품질 조작, 입력 변환 유도 |
| 공격 경로 | 입력 이미지 → convolution feature → classifier → OCR 결과 |
| 제외 범위 | 실제 문서 위조, 운영 OCR 시스템 무단 공격, 악성코드 실행 |

---

## 7. 평가방법 및 지표

| 지표 | 의미 | W03/P01에서의 활용 |
|---|---|---|
| Recognition Accuracy | 문자/문서 인식 정확도 | 기본 clean performance |
| Error Rate | 오인식 비율 | OCR 실패 분석 |
| Clean Accuracy | 정상 입력 정확도 | baseline 성능 |
| Robust Accuracy | 교란 입력 정확도 | 대적 조건 성능 |
| Feature Stability | 입력 변화에 따른 내부 표현 변화 | 표현 안정성 평가 |
| Robust Drop | clean accuracy와 robust accuracy 차이 | 공격 영향 평가 |
| Reproducibility | 데이터, 전처리, seed, 모델 설정 기록 | 보고서 신뢰성 |

---

## 8. 재현성 점검

| 항목 | 점검 |
|---|---|
| 데이터셋 | MNIST, EMNIST, UCI digits, OCR toy dataset 사용 가능 |
| 모델 | CNN 또는 간단한 nearest-centroid/MLP baseline |
| 전처리 | resize, normalization, binarization, augmentation 기록 필요 |
| 공격 조건 | 안전한 toy perturbation, noise, shift, patch simulation만 사용 |
| 결과 파일 | clean accuracy, robust accuracy, confusion matrix, 실패 사례 저장 |
| 재현 가능성 판단 | 고전 OCR/CNN 원리는 공개 데이터로 재현 가능. 원문 전체 문서인식 시스템 재현은 구현 범위가 큼 |

---

## 9. 논문의 고유 기여

1. CNN이 문자인식에서 강력한 계층적 표현학습 구조가 될 수 있음을 보여주었다.
2. Convolution, weight sharing, subsampling, gradient-based learning을 실제 문서인식 pipeline과 연결했다.
3. End-to-end 학습이 수작업 특징공학을 대체할 수 있음을 제시했다.
4. 현대 컴퓨터비전 보안에서 입력 교란, patch, gradient 기반 공격을 해석하는 구조적 배경을 제공한다.

---

## 10. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 현대 adversarial attack 부재 | 1998년 고전 문헌이므로 FGSM/PGD/patch/physical attack을 직접 다루지 않는다. | P05의 robustness survey와 결합한다. |
| ViT/멀티모달 미반영 | CNN/OCR 중심이므로 ViT, multimodal transformer는 직접 다루지 않는다. | P03/P04와 연결한다. |
| 보안 지표 부재 | recognition accuracy 중심이며 robust accuracy, ASR은 별도 설계가 필요하다. | W03 평가표에서 clean/robust 분리 지표를 추가한다. |
| 원문 수치 전사 필요 | OCR 세부 실험 수치는 최종 원문 쪽수 대조가 필요하다. | 보고서에서는 수치 과장 없이 이론 배경으로 사용한다. |

---

## 11. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | 비전 AI 보안은 입력 이미지와 표현학습 구조에서 출발한다는 배경 제시 |
| 2장 관련연구 | CNN, convolution, pooling, end-to-end learning 이론 배경 |
| 3장 위협모형 | 이미지 입력, patch, noise, 전처리 pipeline 공격면 정의 |
| 4장 연구방법 | clean accuracy, robust accuracy, robust drop 기반 평가 설계 |
| 5장 실험/분석 | toy image perturbation 결과와 OCR/CNN 원리 연결 |
| 6장 보안적 함의 | 시각 모델의 무결성·안전성·책임성 해석 |

---

## 12. 기말논문 연결 3문장

1. 이 주차에서 기말논문에 반영할 개념: CNN은 이미지의 지역성과 공간 구조를 반영하는 표현학습 구조이며, 이 구조가 비전 AI 보안의 입력 공격면과 연결된다.
2. 이 주차에서 기말논문에 반영할 표·그림·실험: convolution 수식, CNN pipeline 도식, clean/robust accuracy 비교표, toy perturbation 결과를 반영한다.
3. 이 주차가 RAG 문서 오염/LLM 보안 감사 프레임워크와 연결되는 지점: 이미지·문서 인식 pipeline도 입력 전처리, feature extraction, 모델 추론, 결과 감사로 구성되므로 W14 MLOps 감사와 연결할 수 있다.

---

## 13. 최종 판단

이 논문은 W03의 AI 원리 핵심 문헌으로 사용한다. 현대 비전 대적공격의 직접 근거는 P05가 제공하지만, P01은 CNN의 inductive bias와 gradient-based learning을 설명하는 출발점이다.

---

## 14. 변환 호환성 메모

- GitHub Markdown, MS Word, PDF 변환 호환성을 위해 수식은 LaTeX 블록 수식으로 작성했다.
- 긴 수식은 Markdown 표 안에 넣지 않고 별도 문단으로 분리했다.
- 표에는 변수 설명과 해석만 배치했다.

```bash
pandoc P01_summary.md -o P01_summary.docx
pandoc P01_summary.md -o P01_summary.pdf --pdf-engine=xelatex
```
