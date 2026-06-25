# P01 Summary

## Deep Learning — Yann LeCun, Yoshua Bengio, Geoffrey Hinton, Nature, 2015

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W01 딥러닝 패러다임 & ML 보안 분류학 |
| 논문명 | Deep learning |
| 저자 | Yann LeCun, Yoshua Bengio, Geoffrey Hinton |
| 공식 출판 정보 | Nature, Vol. 521, pp. 436–444, 2015 |
| 발행일 | 2015-05-27 |
| DOI | https://doi.org/10.1038/nature14539 |
| 논문 유형 | Review Article |
| 로컬 PDF | `01_papers/pdf/01_LeCun_Bengio_Hinton_2015_Deep_Learning.pdf` |
| 검증 상태 | W01 `paper_list.md` 기준 공식 DOI와 Nature 출판정보 확인. 강의계획서 지정 논문과 일치 |
| PDF 확인 메모 | repo의 PDF 폴더에 P01 관련 PDF blob이 존재함을 확인했다. 요약은 로컬 PDF 경로와 W01 `paper_list.md`의 공식 DOI 메타데이터 기준으로 보완했다. |
| 핵심 근거 사용 가능 여부 | 가능. W01에서 딥러닝의 표현학습, 역전파, CNN/RNN, 분산표현, end-to-end learning, AI 보안 공격면의 이론적 배경 문헌으로 사용 |

---

## 1. 한 문장 요약

이 논문은 딥러닝을 **다층 신경망이 원시 데이터에서 계층적 표현을 자동 학습하고, 역전파와 경사 기반 최적화를 통해 이미지·음성·자연어·과학 데이터의 복잡한 패턴을 모델링하는 표현학습 패러다임**으로 정리하며, W01에서 AI 보안의 공격면인 **gradient, representation, decision boundary, confidence, training data dependency, distribution shift**를 이해하는 기술적 출발점을 제공한다.

---

## 2. 핵심 연구문제

> 왜 다층 신경망은 사람이 직접 설계한 특징공학보다 이미지, 음성, 자연어 같은 고차원 데이터에서 더 강력한 표현과 일반화 성능을 얻을 수 있는가? 그리고 이 표현학습 구조는 AI 보안에서 어떤 취약성과 방어 지표로 이어지는가?

| 번호 | 연구질문 |
|---|---|
| RQ1 | 딥러닝은 원시 입력에서 저수준 feature부터 고수준 semantic representation까지 어떻게 계층적으로 학습하는가? |
| RQ2 | 역전파와 경사하강법은 다층 신경망의 파라미터를 어떻게 효율적으로 조정하는가? |
| RQ3 | CNN, RNN, autoencoder, representation learning은 각각 어떤 데이터 구조와 문제에 적합한가? |
| RQ4 | 딥러닝의 미분가능성, 표현학습, confidence output은 adversarial attack, privacy attack, model extraction의 기술적 기반이 되는가? |
| RQ5 | AI 보안 기말논문에서 딥러닝 기본 원리를 위협모형, 평가 지표, 재현성 기록으로 어떻게 연결해야 하는가? |

---

## 3. 논문의 핵심 기여

| 기여 | 설명 | W01 연결 |
|---|---|---|
| 표현학습 패러다임 정리 | 사람이 수작업으로 feature를 만들지 않고 모델이 데이터에서 표현을 학습한다는 핵심 원리를 정리 | W01 AI 원리 70%의 중심 |
| 역전파의 핵심성 설명 | 다층 네트워크 학습을 가능하게 한 gradient-based optimization의 역할을 설명 | adversarial gradient 공격의 기반 |
| CNN/RNN 성공 사례 정리 | 이미지·음성·자연어에서 deep architecture가 성능을 높인 이유를 설명 | 보안 데이터 유형별 모델 선택 근거 |
| 계층적 representation 강조 | 저수준 신호에서 고수준 개념으로 이어지는 representation hierarchy를 설명 | feature embedding 공격·방어 분석 |
| AI 보안 연구의 원리 제공 | 논문 자체는 보안 논문이 아니지만 보안 공격과 방어를 이해하는 수학·구조적 기반 제공 | W01~W15 전 주차 기초 |

---

## 4. 목차별 핵심 개괄

| 목차 | 핵심 내용 | 비전공자용 이해 |
|---|---|---|
| 1. Introduction | 딥러닝은 여러 층을 통해 데이터를 점진적으로 추상화하여 복잡한 패턴을 학습한다. | AI가 스스로 중요한 특징을 찾아내는 방식이다. |
| 2. Representation Learning | 원시 입력을 적절한 표현으로 바꾸는 것이 학습 성능의 핵심이다. | 사진에서 선, 모양, 물체를 단계적으로 배우는 것과 같다. |
| 3. Backpropagation | 손실함수의 gradient를 각 층으로 전달해 파라미터를 갱신한다. | 틀린 정도를 계산하고 각 연결을 조금씩 고친다. |
| 4. Convolutional Networks | CNN은 지역성, 가중치 공유, 계층적 feature를 이용해 이미지와 시각 문제에서 강력하다. | 이미지의 작은 패턴을 모아 큰 물체를 인식한다. |
| 5. Recurrent Networks | RNN은 시간 순서와 문맥이 있는 음성·텍스트 데이터를 처리한다. | 문장의 앞뒤 순서를 기억하며 의미를 이해한다. |
| 6. Distributed Representations | 개념을 단일 feature가 아니라 여러 neuron의 조합으로 표현한다. | 단어 하나나 물체 하나도 여러 숫자의 조합으로 표현된다. |
| 7. Applications | 음성인식, 이미지인식, 자연어처리, 생물정보, 추천 등 다양한 분야에서 성과를 보였다. | 딥러닝이 여러 산업 분야에 확산된 이유를 보여준다. |
| 8. Future Directions | 더 나은 학습, 추론, 표현, memory, reasoning, unsupervised learning이 과제로 남아 있다. | AI가 더 적은 데이터로 더 잘 이해하고 추론하는 방향이다. |
| 보안 연결 | 딥러닝의 미분가능성·표현학습·confidence는 adversarial attack, privacy attack, extraction attack의 기반이 된다. | 강점이 동시에 공격면이 될 수 있다. |

---

## 5. 핵심 이론 및 수식

> 아래 수식은 딥러닝 기본 원리와 AI 보안 평가축을 연결하기 위해 표준화한 표현이다. 수식은 GitHub, MS Word, PDF 변환 호환성을 위해 Markdown 표 밖의 LaTeX block math로 작성한다.

### 5.1 경험위험최소화

딥러닝 모델의 기본 목적은 학습 데이터에서 평균 손실을 최소화하는 것이다.

$$
\min_{\theta}\hat{R}(\theta)=\frac{1}{n}\sum_{i=1}^{n}\ell(f_{\theta}(x_i),y_i)
$$

| 기호 | 의미 |
|---|---|
| $x_i$ | $i$번째 입력 데이터 |
| $y_i$ | 정답 레이블 |
| $f_\theta$ | 파라미터 $\theta$를 가진 모델 |
| $\ell$ | 손실함수 |
| $\hat{R}(\theta)$ | 경험위험 |

### 보안적 의미

평균 손실을 낮추는 모델이 공격 조건에서도 안전하다는 보장은 없다. AI 보안에서는 정상 평균 성능과 공격 조건 성능을 분리해 평가해야 한다.

---

### 5.2 경사하강법과 역전파

모델은 손실의 gradient를 따라 파라미터를 갱신한다.

$$
\theta_{t+1}=\theta_t-\eta\nabla_{\theta}\hat{R}(\theta_t)
$$

### 보안적 의미

역전파는 모델 학습을 가능하게 하지만, 입력에 대한 gradient는 adversarial example 생성과 취약성 분석의 기반이 된다.

---

### 5.3 입력 gradient 기반 교란

입력에 대한 손실 gradient는 모델 예측을 바꾸는 방향을 알려줄 수 있다.

$$
x^{adv}=x+\epsilon\cdot\operatorname{sign}\left(\nabla_x\ell(f_{\theta}(x),y)\right)
$$

### 보안적 의미

이 수식은 딥러닝의 미분가능성이 공격면이 될 수 있음을 보여준다. 방어에서는 같은 gradient 구조를 robust training과 sensitivity analysis에 활용한다.

---

### 5.4 계층적 표현학습

각 층은 이전 층의 표현을 비선형 변환하여 더 추상적인 표현을 만든다.

$$
h^{(l)}=\sigma\left(W^{(l)}h^{(l-1)}+b^{(l)}\right)
$$

| 기호 | 의미 |
|---|---|
| $h^{(l)}$ | $l$번째 층의 은닉 표현 |
| $W^{(l)}$ | 가중치 행렬 |
| $b^{(l)}$ | 편향 |
| $\sigma$ | 활성화 함수 |

### 보안적 의미

공격자는 내부 표현이 특정 트리거, shortcut, spurious feature에 민감한지 노린다. 방어자는 representation robustness와 feature stability를 측정해야 한다.

---

### 5.5 Softmax Confidence

분류 모델은 score를 확률처럼 보이는 confidence로 바꿀 수 있다.

$$
p(y=k|x)=\frac{\exp(z_k)}{\sum_j\exp(z_j)}
$$

### 보안적 의미

confidence score는 사용자에게 유용하지만 membership inference, model extraction, calibration failure의 공격면이 될 수 있다.

---

### 5.6 일반화 오차

학습 데이터 성능과 테스트 데이터 성능의 차이는 일반화 성능을 나타낸다.

$$
GenGap=R_{test}(\theta)-R_{train}(\theta)
$$

### 보안적 의미

일반화 gap이 크면 membership inference와 overfitting 기반 privacy attack의 위험이 증가할 수 있다.

---

### 5.7 표현 안정성

작은 입력 변화에 대해 내부 표현이 얼마나 안정적인지 평가할 수 있다.

$$
RepStability=1-\frac{\|h(x)-h(x')\|}{\|x-x'\|+\epsilon}
$$

### 보안적 의미

표현이 작은 교란에 크게 흔들리면 adversarial robustness가 낮을 수 있다. W12의 Lipschitz/XAI robustness와 연결된다.

---

### 5.8 딥러닝 보안 위험 점수

딥러닝 모델의 공격면을 요약하면 다음처럼 표현할 수 있다.

$$
DLRisk=\alpha GradExposure+\beta OverfitRisk+\gamma ConfidenceLeakage+\delta DriftRisk-\lambda MonitoringCoverage
$$

### 보안적 의미

좋은 딥러닝 시스템은 성능뿐 아니라 gradient 민감도, privacy leakage, drift, monitoring coverage를 함께 관리해야 한다.

---

## 6. AI 원리 70% 관점 분석

| 원리 항목 | 설명 | W01/P01에서의 의미 |
|---|---|---|
| 표현학습 | feature를 사람이 만들지 않고 모델이 학습 | 딥러닝 핵심 |
| 다층 구조 | 여러 은닉층으로 추상화 수준을 높임 | 계층적 representation |
| 역전파 | gradient를 이용해 파라미터 갱신 | 학습의 핵심 원리 |
| CNN | 지역성·가중치 공유 기반 시각 모델 | 이미지/영상 보안 연결 |
| RNN | 순차 데이터와 문맥 처리 | 텍스트/로그/시계열 보안 연결 |
| Distributed representation | 여러 neuron 조합으로 개념 표현 | embedding 기반 분석 |
| End-to-end learning | 입력부터 출력까지 하나의 목적함수로 학습 | 자동화된 feature learning |
| Generalization | 학습 데이터 밖 성능 | privacy/robustness와 연결 |

---

## 7. 보안 이슈 30% 관점 분석

| 보안 항목 | 딥러닝 원리와의 연결 | 대표 평가 지표 |
|---|---|---|
| 기밀성 | 학습 데이터와 모델 파라미터가 민감정보를 포함할 수 있음 | MI advantage, leakage rate |
| 무결성 | adversarial example, poisoning, backdoor가 모델 판단을 왜곡 | robust accuracy, ASR |
| 가용성 | 분포 이동, resource exhaustion, model drift가 서비스 품질 저하 | drift score, latency |
| 프라이버시 | overfitting과 confidence leakage가 membership/property inference로 이어짐 | GenGap, confidence gap |
| 안전성 | 고위험 영역에서 잘못된 예측이 실제 피해로 연결 | failure case rate |
| 책임성 | 모델 버전, 데이터, 학습 설정, 평가 로그가 있어야 감사 가능 | reproducibility coverage |

---

## 8. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | 모델 파라미터, 학습 데이터, 내부 표현, confidence score, decision boundary, 추론 결과, 학습·배포 파이프라인 |
| 공격자 목표 | 오분류 유도, 학습 데이터 정보 추론, 모델 추출, backdoor 삽입, confidence 기반 정보 수집 |
| 공격자 능력 | black-box query, gray-box confidence 관찰, white-box gradient 접근, 데이터 오염, 분포 이동 유발 |
| 공격 경로 | 입력/데이터/모델/출력 중 하나를 조작 또는 관찰 → representation/decision boundary 취약성 이용 → 잘못된 예측 또는 정보 노출 |
| 방어자 능력 | robust training, regularization, monitoring, calibration, DP, access control, model registry, XAI 검증 |
| 제외 범위 | 실제 시스템 공격 절차, 악성코드 작성, 데이터 오염 실행 방법, 권한 없는 모델 접근 지원 |

---

## 9. 평가방법 및 지표

| 평가축 | 지표 | 의미 | W01/P01 활용 |
|---|---|---|---|
| 기본 성능 | accuracy, loss, F1 | 정상 데이터 성능 | baseline |
| 일반화 | train-test gap, validation loss | overfitting 위험 | privacy와 연결 |
| 강건성 | robust accuracy, ASR, perturbation sensitivity | 공격 조건 성능 | W03/W12 연결 |
| 프라이버시 | membership advantage, confidence leakage | 학습 데이터 노출 위험 | W11 연결 |
| 표현 안정성 | RepStability, embedding drift | 내부 표현 신뢰성 | XAI/robustness 연결 |
| Calibration | ECE, confidence gap | confidence 신뢰성 | 안전한 추론 |
| 운영성 | drift score, monitoring coverage | 배포 후 안정성 | W14 연결 |
| 재현성 | seed, data version, model hash, config | 결과 재현 가능성 | W15 연결 |

---

## 10. 재현성 체크리스트

| 항목 | 기록해야 할 내용 |
|---|---|
| Bibliographic status | Nature DOI, 권호/쪽, 로컬 PDF 판본 상태 |
| Data | dataset name, version, split, preprocessing, label policy |
| Model | architecture, layer config, activation, parameter count |
| Training | optimizer, learning rate, batch size, epoch, seed, loss function |
| Evaluation | test set, metric, confidence calibration, robustness test |
| Security | adversarial setting, poisoning/backdoor 여부, privacy test 여부 |
| Environment | Python, framework, CUDA, dependency lock, hardware |
| Artifact | model checkpoint, model hash, training log, evaluation output |
| XAI | layer activation, attribution method, explanation config |
| 한계 | 정상 데이터 성능을 보안성·공정성·프라이버시 보장으로 과장하지 않음 |

---

## 11. 논문의 고유 기여

1. 딥러닝을 표현학습 중심 패러다임으로 대중적·학술적으로 체계화한 핵심 리뷰다.
2. CNN, RNN, representation learning, backpropagation의 원리를 하나의 흐름으로 설명한다.
3. W01의 AI 원리 70%를 구성하는 가장 기초적인 논문이다.
4. AI 보안 관점에서는 gradient, representation, confidence, generalization gap이 공격면이 될 수 있음을 이해하는 출발점이다.
5. W03 adversarial robustness, W05 backdoor, W11 privacy, W12 verification/XAI, W14 MLOps, W15 reproducibility로 이어지는 이론적 기반을 제공한다.

---

## 12. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 보안 논문은 아님 | 이 논문은 딥러닝 원리 리뷰이며 AI 보안 공격·방어를 직접 다루지는 않는다. | W03~W15 보안 문헌과 연결 |
| 최신 LLM 이전 문헌 | 2015년 논문이므로 transformer/LLM/RAG 최신 논의는 포함되지 않는다. | W04/W07/W08/W15 문헌으로 보완 |
| 평균 성능 중심 | 보안·프라이버시·공정성 지표는 직접 제시하지 않는다. | robust accuracy, privacy leakage, fairness metric 추가 |
| 설명가능성 제한 | 내부 표현의 의미 해석과 책임성은 제한적으로 다룬다. | W12/W15 XAI 문헌으로 보완 |
| 운영 관점 부족 | 배포·모니터링·MLOps 증거는 별도 주제다. | W14/W15와 연결 |
| 저작권 관리 | Nature PDF 원문을 공개 repo에 유지하면 권리 조건 검토가 필요하다. | DOI/서지/summary 중심 공개 검토 |

---

## 13. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | AI 보안 연구의 기반이 되는 딥러닝 표현학습과 gradient 기반 학습 원리 소개 |
| 2장 관련연구 | P01을 딥러닝 기본 원리와 표현학습 배경 문헌으로 정리 |
| 3장 위협모형 | 모델 파라미터, 내부 표현, confidence, decision boundary, 학습 데이터 보호 자산 정의 |
| 4장 연구방법 | 경험위험, gradient update, adversarial perturbation, representation stability 지표 설계 |
| 5장 분석 | 딥러닝 원리와 공격면 연결표 제시 |
| 6장 보안적 함의 | 딥러닝의 강점이 adversarial, privacy, extraction, drift 위험으로 전환되는 구조 해석 |
| 부록 | 수식 설명, 모델·데이터·평가 재현성 체크리스트 수록 |

---

## 14. 기말논문 연결 3문장

1. W01에서 기말논문에 반영할 개념: 딥러닝은 원시 데이터에서 계층적 표현을 학습하고 역전파로 파라미터를 최적화하는 구조이며, 이 미분가능성과 표현학습 구조가 AI 보안 공격면의 출발점이 된다.
2. W01에서 기말논문에 반영할 표·그림·실험: 경험위험최소화, gradient update, adversarial perturbation, representation stability, DLRisk 수식표와 딥러닝 원리-보안 공격면 연결표를 반영한다.
3. W01이 W15 최종 제출과 연결되는 지점: 딥러닝 모델을 평가할 때 정상 성능뿐 아니라 robustness, privacy leakage, calibration, drift, reproducibility evidence를 함께 기록해야 최종 논문의 신뢰성을 확보할 수 있다.

---

## 15. 최종 판단

P01은 W01의 중심 문헌이다. 이 논문은 보안 논문은 아니지만, AI 보안의 핵심 공격면인 gradient, representation, confidence, generalization gap, decision boundary를 이해하는 데 필수적인 이론적 기반을 제공한다. 따라서 기말논문에서는 P01을 **딥러닝 원리, 표현학습, 역전파, AI 보안 공격면의 기술적 배경 문헌**으로 사용하고, 실제 보안 공격·방어 평가는 W03~W15 문헌과 연결하는 것이 적절하다.

---

## 16. 변환 호환성 메모

```bash
pandoc P01_summary.md -o P01_summary.docx
pandoc P01_summary.md -o P01_summary.pdf --pdf-engine=xelatex
```
