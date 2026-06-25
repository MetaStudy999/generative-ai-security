# P01 Summary

## Gradient-Based Learning Applied to Document Recognition — Yann LeCun, Léon Bottou, Yoshua Bengio, Patrick Haffner, Proceedings of the IEEE, 1998

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W03 컴퓨터비전 표현학습 & 비전 대적공격 |
| 논문명 | Gradient-Based Learning Applied to Document Recognition |
| 저자 | Yann LeCun, Léon Bottou, Yoshua Bengio, Patrick Haffner |
| 공식 출판 정보 | Proceedings of the IEEE, Vol. 86, No. 11, pp. 2278–2324, 1998 |
| DOI | https://doi.org/10.1109/5.726791 |
| 논문 유형 | Classical Review / CNN and Document Recognition System Paper |
| 로컬 PDF | `01_papers/pdf/01_LeCun_et_al_1998_Gradient_Based_Learning_Document_Recognition.pdf` |
| 검증 상태 | W03 `paper_list.md` 기준 공식 DOI와 IEEE 출판정보 확인. 강의계획서 지정 논문과 일치 |
| PDF 확인 메모 | repo의 PDF 폴더에 P01 관련 PDF blob이 존재함을 확인했다. 요약은 로컬 PDF 경로와 W03 `paper_list.md`의 공식 DOI 메타데이터 기준으로 보완했다. |
| 수식 호환성 | GitHub 수식 렌더링 오류 방지를 위해 `\operatorname`을 사용하지 않고 `\mathrm{...}` 형태로 작성했다. |
| 핵심 근거 사용 가능 여부 | 가능. W03에서 CNN, convolution, weight sharing, subsampling/pooling, gradient-based learning, document recognition, OCR pipeline, vision adversarial attack surface의 핵심 배경 문헌으로 사용 |

---

## 1. 한 문장 요약

이 논문은 문자인식과 문서인식 문제에서 CNN과 gradient-based learning을 결합하여 **local receptive field, weight sharing, convolution, subsampling, end-to-end learning, Graph Transformer Network**가 픽셀 입력에서 계층적 표현을 직접 학습할 수 있음을 보여준 컴퓨터비전 딥러닝의 고전 문헌이며, W03에서는 현대 비전 대적공격을 이해하기 위한 **gradient, convolutional feature, spatial invariance, patch sensitivity, OCR pipeline risk**의 기술적 기반으로 사용한다.

---

## 2. 핵심 연구문제

> 수작업 특징 추출과 분리된 분류기 대신, 입력 이미지에서 직접 계층적 특징을 학습하는 gradient 기반 신경망이 문자인식·문서인식 시스템을 얼마나 효과적으로 구성할 수 있는가? 그리고 이 구조는 현대 비전 보안에서 어떤 공격면과 평가 지표로 이어지는가?

| 번호 | 연구질문 |
|---|---|
| RQ1 | CNN은 문자인식에서 지역성, 공간 구조, weight sharing을 어떻게 활용하는가? |
| RQ2 | End-to-end gradient-based learning은 feature extractor와 classifier를 어떻게 하나의 목적함수로 통합하는가? |
| RQ3 | Subsampling/pooling은 위치 변화와 작은 왜곡에 대해 어떤 형태의 안정성을 제공하는가? |
| RQ4 | Gradient 기반 학습 구조는 현대 vision adversarial attack, patch attack, physical perturbation의 어떤 이론적 출발점이 되는가? |
| RQ5 | 문서인식 pipeline의 모듈화와 전체 목적함수는 오늘날 AI 보안 평가에서 어떤 재현성·감사 가능성 요구로 이어지는가? |

---

## 3. 논문의 핵심 기여

| 기여 | 설명 | W03 연결 |
|---|---|---|
| CNN 기반 문자인식 정립 | Convolution, local receptive field, weight sharing, subsampling을 문자인식에 적용 | CV 표현학습의 고전 기반 |
| Gradient-based learning 강조 | 수작업 feature engineering 대신 gradient로 전체 모델을 학습 | adversarial gradient 분석의 기초 |
| End-to-end pipeline | 전처리, feature extraction, classification을 통합 학습하는 방향 제시 | MLOps/재현성 기록 필요 |
| Document recognition system | 단일 문자 인식에서 문서 전체 처리 pipeline으로 확장 | OCR 보안과 문서 자동처리 위험 |
| Graph Transformer Network | 여러 모듈을 연결한 구조에서 전체 목적함수 기반 학습 가능성 제시 | 복합 AI pipeline 평가와 연결 |

---

## 4. 목차별 핵심 개괄

| 목차 | 핵심 내용 | 비전공자용 이해 |
|---|---|---|
| 1. Introduction | 문자인식은 수작업 feature가 아니라 학습 가능한 feature hierarchy로 접근할 수 있다. | 사람이 특징을 정하지 않아도 모델이 글자 모양을 배운다. |
| 2. Gradient-based learning | 손실함수를 정의하고 gradient를 통해 모델 파라미터를 학습한다. | 틀린 정도를 계산해 모델을 조금씩 고친다. |
| 3. Convolutional networks | Local receptive field, weight sharing, convolution, subsampling으로 이미지 구조를 활용한다. | 작은 획과 모양을 찾아 글자 전체를 인식한다. |
| 4. LeNet 계열 모델 | 문자인식에 특화된 CNN 구조를 통해 픽셀 입력에서 class를 예측한다. | 손글씨 숫자나 문자를 CNN으로 분류한다. |
| 5. Document recognition | 단일 문자 인식뿐 아니라 문서 이미지, 문자 segmentation, sequence 처리까지 확장한다. | 글자 하나만 보는 것이 아니라 문서 전체 흐름도 본다. |
| 6. Graph Transformer Network | 여러 인식 모듈을 그래프처럼 연결하고 전체 목표에 맞게 조정한다. | 복잡한 문서 처리 과정을 하나의 시스템으로 묶는다. |
| 7. Applications | 은행 수표, 우편번호, OCR 등 실제 문서인식 응용을 다룬다. | 실생활 문서 자동처리의 초기 핵심 기술이다. |
| 보안 연결 | 입력 이미지, patch, 스캔 품질, 내부 feature, gradient가 공격면이 될 수 있다. | 비전 모델의 강점이 동시에 공격 지점이 된다. |

---

## 5. 핵심 이론 및 수식

> 수식은 GitHub Markdown/KaTeX 호환성을 우선한다. `\operatorname` 매크로는 사용하지 않고 `\mathrm{...}` 형태로 작성한다.

### 5.1 2D Convolution

CNN의 기본 연산은 입력 특징맵의 국소 영역에 같은 kernel을 반복 적용하는 convolution이다.

$$
Y_{i,j,k}=b_k+\sum_{u,v,c}W_{u,v,c,k}X_{i+u,j+v,c}
$$

| 기호 | 의미 |
|---|---|
| $X$ | 입력 이미지 또는 입력 특징맵 |
| $Y$ | 출력 특징맵 |
| $W_{u,v,c,k}$ | 위치 $(u,v)$, 입력 채널 $c$, 출력 채널 $k$의 convolution kernel |
| $b_k$ | 출력 채널 $k$의 bias |
| $i,j$ | 출력 공간 위치 |

### 보안적 의미

Convolution은 이미지의 지역 패턴을 효율적으로 학습하지만, 같은 kernel이 전체 이미지에 반복 적용되므로 특정 국소 패턴이나 patch가 모델 예측에 과도한 영향을 줄 수 있다. 이는 adversarial patch, localized perturbation, physical sticker 공격을 해석하는 출발점이 된다.

---

### 5.2 Subsampling / Pooling

Pooling은 근처 영역의 정보를 요약하여 작은 위치 변화에 대한 완만한 불변성을 제공한다.

$$
Y_{i,j,k}=\mathrm{pool}\left(\{X_{a,b,k}:(a,b)\in \mathcal{N}(i,j)\}\right)
$$

| 기호 | 의미 |
|---|---|
| $\mathrm{pool}$ | max pooling 또는 average pooling 연산 |
| $\mathcal{N}(i,j)$ | 출력 위치 $(i,j)$에 대응하는 입력 이웃 영역 |
| $k$ | 채널 인덱스 |

### 보안적 의미

Pooling은 작은 이동에 대한 안정성을 제공하지만, 모든 형태의 교란에 강건성을 보장하지는 않는다. 작은 $L_p$ 교란, patch 공격, 배경 변화, 이미지 변환 공격에서는 pooling만으로 robust performance를 보장할 수 없다.

---

### 5.3 Gradient-Based Learning

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

### 5.4 입력 Gradient 기반 교란

현대 vision adversarial attack은 입력에 대한 손실 gradient를 이용해 모델 예측을 바꾸는 방향을 찾는다.

$$
x^{adv}=x+\epsilon\cdot\mathrm{sign}\left(\nabla_x\mathcal{L}(f_{\theta}(x),y)\right)
$$

### 보안적 의미

W01에서 확인한 gradient 공격면이 W03의 비전 모델에서는 이미지 픽셀, patch, affine transform, 스캔 품질 조작으로 나타날 수 있다.

---

### 5.5 Clean Accuracy와 Robust Accuracy

정상 입력과 교란 입력에서의 성능을 분리해 측정한다.

$$
Acc_{clean}=\frac{N_{correct}(x)}{N_{total}}
$$

$$
Acc_{robust}=\frac{N_{correct}(x^{adv})}{N_{total}}
$$

### 보안적 의미

문자인식 시스템은 정상 데이터 성능이 높아도 교란·노이즈·스캔 품질 변화에 취약할 수 있다. 따라서 clean accuracy와 robust accuracy를 반드시 분리해야 한다.

---

### 5.6 Robust Drop

정상 성능 대비 공격 조건 성능 하락폭이다.

$$
RobustDrop=Acc_{clean}-Acc_{robust}
$$

### 보안적 의미

RobustDrop이 클수록 작은 교란이나 환경 변화가 모델 성능에 큰 영향을 준다는 뜻이다.

---

### 5.7 Feature Stability

입력 변화에 따른 내부 feature 변화량을 측정한다.

$$
FeatureStability=1-\frac{\|h(x)-h(x')\|}{\|x-x'\|+\epsilon}
$$

### 보안적 의미

문자 이미지가 조금 이동하거나 노이즈가 추가되었을 때 내부 표현이 크게 흔들리면 OCR 모델은 실제 운영에서 취약할 수 있다.

---

### 5.8 OCR Pipeline Risk

문서인식 pipeline의 보안 위험을 입력, 전처리, 모델, 후처리 위험으로 분해한다.

$$
OCRRisk=InputRisk+PreprocessRisk+ModelRisk+PostprocessRisk-MonitoringCoverage
$$

### 보안적 의미

문서인식 보안은 CNN 모델 하나만 보호하는 문제가 아니다. 스캔 품질, 이진화, segmentation, 모델 추론, 후처리 규칙, 로그 기록까지 포함해야 한다.

---

## 6. AI 원리 70% 관점 분석

| 원리 항목 | 설명 | W03/P01에서의 의미 |
|---|---|---|
| Local Receptive Field | 이미지의 국소 구조를 활용해 parameter 수를 줄임 | 문자 획·모양 학습 |
| Weight Sharing | 같은 kernel을 전체 공간에 공유 | translation equivariance |
| Convolution | 지역 패턴을 feature map으로 변환 | CNN 핵심 연산 |
| Subsampling/Pooling | 위치 변화에 대한 완만한 안정성 제공 | OCR distortion 대응 |
| End-to-End Learning | feature extraction과 classifier를 통합 학습 | 수작업 feature 대체 |
| Graph Transformer Network | 여러 인식 모듈을 전체 pipeline으로 연결 | 문서인식 시스템화 |
| Inductive Bias | 이미지의 지역성·공간성에 맞는 구조 가정 | CV 모델 설계 원리 |
| Gradient Optimization | 손실 gradient로 전체 모델 학습 | 대적 gradient 공격의 배경 |

---

## 7. 보안 이슈 30% 관점 분석

| 보안 항목 | CNN/OCR 관점 해석 | 대표 평가 지표 |
|---|---|---|
| 기밀성 | 문서 이미지와 OCR 결과가 개인정보·금융정보를 포함할 수 있음 | access log, redaction rate |
| 무결성 | 입력 이미지의 작은 교란이나 patch가 분류 결과를 바꿀 수 있음 | robust accuracy, ASR |
| 가용성 | 노이즈·스캔 품질 저하·segmentation 실패가 OCR 서비스를 저하시킴 | error rate, latency |
| 프라이버시 | OCR 로그와 confidence score가 민감문서 처리 흔적을 남김 | retention policy, leakage check |
| 안전성 | 번호판, 신분증, 수표, 문서 인증 오인식은 실제 피해로 연결 | false accept/reject rate |
| 책임성 | 데이터, 전처리, 모델 버전, 평가셋, 실패 사례를 기록해야 감사 가능 | reproducibility coverage |

---

## 8. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | 문서 이미지, 문자 라벨, OCR 모델, convolution feature, 전처리 pipeline, segmentation 결과, OCR 출력, confidence score |
| 공격자 목표 | 오인식 유도, 특정 문자/숫자 오분류, 문서 처리 오류 유발, 후처리 규칙 우회 |
| 공격자 능력 | 이미지 노이즈 추가, patch 삽입, 스캔 품질 조작, 회전/이동/크기 변환, 배경 패턴 삽입 |
| 공격 경로 | 입력 이미지 → 전처리/segmentation → convolution feature → classifier → OCR 결과 → 후처리 의사결정 |
| 방어자 능력 | 데이터 증강, robust training, input validation, preprocessing audit, 실패 사례 기록, monitoring, human review |
| 제외 범위 | 실제 문서 위조, 운영 OCR 시스템 무단 공격, 악성코드 작성, 개인정보 탈취 절차 |

---

## 9. 평가방법 및 지표

| 평가축 | 지표 | 의미 | W03/P01 활용 |
|---|---|---|---|
| 기본 인식 | recognition accuracy, character error rate | 정상 OCR 성능 | baseline |
| 오류 분석 | confusion matrix, top-k error | 어떤 문자가 자주 혼동되는지 | failure analysis |
| 강건성 | robust accuracy, RobustDrop, ASR | 교란 조건 성능 | adversarial CV 연결 |
| 위치 안정성 | shift/rotation/noise sensitivity | 입력 변환에 대한 안정성 | spatial robustness |
| 표현 안정성 | FeatureStability | 내부 feature 변화량 | representation security |
| 문서 pipeline | segmentation error, postprocess error | 전체 문서인식 실패 | system risk |
| 운영성 | latency, throughput, manual review rate | 실제 서비스 성능 | MLOps 연결 |
| 재현성 | data split, preprocessing, seed, model config | 결과 재현 가능성 | W15 연결 |

---

## 10. 재현성 체크리스트

| 항목 | 기록해야 할 내용 |
|---|---|
| Bibliographic status | DOI, IEEE 출판정보, 로컬 PDF 판본 상태 |
| Dataset | MNIST, EMNIST, UCI digits, OCR toy dataset, train/test split |
| Preprocessing | resize, normalization, binarization, deskewing, augmentation |
| Model | CNN architecture, kernel size, pooling, activation, parameter count |
| Training | optimizer, learning rate, epoch, batch size, seed, loss function |
| Attack/perturbation | noise, shift, rotation, blur, patch simulation, perturbation budget |
| Evaluation | clean accuracy, robust accuracy, confusion matrix, error examples |
| Pipeline | segmentation rule, postprocessing rule, manual review threshold |
| Environment | Python/framework version, dependency lock, hardware, run log |
| 한계 | 고전 OCR 결과를 현대 ViT/멀티모달 보안 성능으로 과장하지 않음 |

---

## 11. 논문의 고유 기여

1. CNN이 문자인식에서 강력한 계층적 표현학습 구조가 될 수 있음을 보여준 고전 문헌이다.
2. Convolution, weight sharing, subsampling, gradient-based learning을 실제 문서인식 pipeline과 연결했다.
3. End-to-end 학습이 수작업 특징공학을 대체할 수 있음을 제시했다.
4. 현대 컴퓨터비전 보안에서 입력 교란, patch, gradient 기반 공격을 해석하는 구조적 배경을 제공한다.
5. W03의 adversarial computer vision 논의를 W01의 딥러닝 원리, W12의 robustness/XAI, W14의 배포 운영, W15의 재현성 evidence와 연결한다.

---

## 12. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 현대 adversarial attack 부재 | 1998년 고전 문헌이므로 FGSM, PGD, physical patch attack을 직접 다루지 않는다. | W03 P05 robustness survey와 결합 |
| ViT/멀티모달 미반영 | CNN/OCR 중심이므로 ViT, multimodal transformer는 직접 다루지 않는다. | W03 P03/P04와 연결 |
| 보안 지표 부재 | recognition accuracy 중심이며 robust accuracy, ASR은 별도 설계가 필요하다. | clean/robust 분리 지표 추가 |
| 원문 수치 전사 주의 | OCR 세부 실험 수치는 최종 원문 대조가 필요하다. | 수치 과장 없이 구조와 방법 중심 활용 |
| 운영 환경 차이 | 고전 OCR 시스템과 최신 cloud/edge vision system은 다르다. | W14 MLOps/edge 문헌과 연결 |
| 저작권 관리 | PDF 원문을 public repo에 유지하면 권리 조건 검토가 필요하다. | DOI/서지/summary 중심 공개 검토 |

---

## 13. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | 컴퓨터비전 보안의 기반인 CNN, convolution, gradient-based learning 소개 |
| 2장 관련연구 | P01을 CNN/OCR 및 비전 표현학습의 고전 문헌으로 정리 |
| 3장 위협모형 | 문서 이미지, convolution feature, OCR output, confidence score, preprocessing pipeline 보호 자산 정의 |
| 4장 연구방법 | convolution, pooling, gradient update, robust accuracy, FeatureStability, OCRRisk 지표 설계 |
| 5장 분석 | CNN 구조와 adversarial attack surface 연결표 제시 |
| 6장 보안적 함의 | localized perturbation, patch attack, physical-world OCR risk, pipeline reproducibility 해석 |
| 부록 | preprocessing, model config, perturbation 조건, failure case, 수식 설명 수록 |

---

## 14. 기말논문 연결 3문장

1. W03에서 기말논문에 반영할 개념: CNN은 local receptive field와 weight sharing으로 이미지의 계층적 표현을 학습하지만, 같은 구조가 localized perturbation과 adversarial patch에 민감한 공격면이 될 수 있다.
2. W03에서 기말논문에 반영할 표·그림·실험: convolution, pooling, gradient update, 입력 gradient 교란, clean/robust accuracy, FeatureStability, OCRRisk 수식표와 CNN 공격면 연결표를 반영한다.
3. W03이 W15 최종 제출과 연결되는 지점: 비전 모델 평가 결과는 data split, preprocessing, model config, perturbation setting, clean/robust score, failure example을 evidence chain으로 남겨야 재현성과 신뢰성을 확보할 수 있다.

---

## 15. 최종 판단

P01은 W03의 컴퓨터비전 표현학습 핵심 문헌이다. 이 논문은 현대 adversarial attack 논문은 아니지만, CNN과 gradient-based learning이 왜 강력한지, 동시에 왜 입력 교란·patch·스캔 품질 변화에 취약한 공격면을 만들 수 있는지 이해하는 데 필수적이다. 따라서 기말논문에서는 P01을 **CNN/OCR 원리, convolutional feature, gradient-based learning, 비전 대적공격의 기술적 배경 문헌**으로 사용하고, 실제 공격·방어 평가는 W03 P05와 W12 robustness/XAI 문헌으로 보완하는 것이 적절하다.

---

## 16. GitHub 수식 호환성 메모

이 파일에서는 GitHub 수식 렌더링 오류 방지를 위해 `\operatorname`을 사용하지 않는다.

| 피해야 할 표현 | 권장 표현 |
|---|---|
| `\operatorname{pool}` | `\mathrm{pool}` |
| `\operatorname{sign}` | `\mathrm{sign}` |
| `\operatorname{argmax}` | `\mathrm{argmax}` 또는 `\arg\max` |

```bash
pandoc P01_summary.md -o P01_summary.docx
pandoc P01_summary.md -o P01_summary.pdf --pdf-engine=xelatex
```
