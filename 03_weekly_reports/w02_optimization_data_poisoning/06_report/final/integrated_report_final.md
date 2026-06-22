# W02 대규모 최적화 & 데이터 오염 위협 통합보고서

## 0. 메타정보

| 항목 | 내용 |
|---|---|
| 주차 | W02 |
| 주제 | 대규모 최적화 & 데이터 오염 위협 |
| AI 원리 | 대규모 최적화, SGD, 일반화, 효율적 학습, 모델 압축/경량화 |
| 보안 이슈 | 데이터 오염, label-flipping, poisoning, backdoor |
| 문서 상태 | 제출용 최종 초안. 최종 제출 전 사람 검토 필요 |
| 실험 상태 | `04_experiment/outputs/`의 CSV/JSON/로그 존재 확인 |
| 주요 검토 필요 | P04 강의계획서 제목과 현재 로컬 PDF 동일 여부, ACM Article 번호, PDF 공개 저장소 보관 정책 |

## 1. 한 문장 요약

W02는 "학습은 데이터로 움직이고, 데이터가 오염되면 최적화 경로와 최종 모델의 신뢰성이 바뀐다"는 관점에서 대규모 최적화 원리와 poisoning/backdoor 평가 지표를 연결한다.

## 2. 학습 배경과 주차 목표

### 2.1 이번 주 주제의 위치

W02는 W01에서 정리한 ML 생명주기 보증과 위협모형을 학습 단계로 구체화하는 주차다. W01이 "ML 시스템을 어떻게 보안 평가 대상으로 볼 것인가"를 다루었다면, W02는 "학습 데이터와 라벨이 조작될 때 최적화 경로와 최종 모델 보안성이 어떻게 달라지는가"를 다룬다. 이후 W03 비전 대적공격, W05 self-supervised/backdoor, W10 연합학습 poisoning, W14 MLOps 공급망 보안과 직접 연결된다.

### 2.2 강의계획서상 학습목표

- 최적화-일반화의 병목을 정량적으로 이해한다.
- 효율화 기법의 정확도-비용 trade-off를 분석한다.
- poisoning/backdoor의 공격자 비용모형과 방어평가를 설계한다.

### 2.3 이번 주 핵심 질문

1. SGD와 mini-batch 학습은 왜 데이터 품질에 민감한가?
2. 데이터 오염은 학습 목적함수와 gradient 방향을 어떻게 바꾸는가?
3. Label-flipping과 backdoor는 어떤 점에서 다른 위협인가?
4. Clean accuracy가 높아도 ASR이 높으면 왜 보안적으로 실패인가?
5. W02의 toy 실험을 KCI 또는 SCI 논문 주제로 발전시키려면 어떤 연구문제가 적절한가?

## 3. AI 원리 70% 정리

대규모 머신러닝 학습은 전체 데이터의 손실을 최소화하는 최적화 문제로 볼 수 있으며, SGD와 mini-batch update는 확장 가능한 학습의 핵심 절차다[1]. 이 방식은 전체 gradient를 매번 계산하지 않아도 된다는 장점이 있지만, 샘플링 노이즈와 데이터 품질에 민감하다. 학습 데이터 일부가 조작되면 empirical risk와 gradient 추정이 달라지고, decision boundary가 의도하지 않은 방향으로 이동할 수 있다.

효율적 딥러닝은 정확도뿐 아니라 latency, memory, FLOPs, 비용을 함께 고려해야 한다[2]. 모델 압축, pruning, quantization, distillation, efficient architecture는 배포 가능성을 높이지만, 보안 평가에서는 방어 비용, 탐지 지연시간, 재학습 가능성, backdoor 잔존 여부도 함께 기록해야 한다.

**표 1. W02 핵심 개념과 보안 연결**

| 개념 | W02 의미 | 관련 문헌 | 보안 연결 |
|---|---|---|---|
| Large-scale optimization | 대규모 데이터에서 학습 가능한 최적화 절차 | [1] | 데이터 오염이 목적함수와 gradient를 바꿈 |
| Stochastic gradient | 일부 데이터로 gradient를 추정하는 학습 방식 | [1] | 오염 샘플이 업데이트 방향에 영향 |
| Generalization | 정상 test 성능을 설명하는 원리 | [1] | clean 성능과 공격 조건 성능을 분리해야 함 |
| Model efficiency | 정확도와 비용, 속도, 메모리를 함께 보는 관점 | [2] | 방어 비용과 배포 가능성 평가 |
| Compression/lightweighting | 모델 크기와 추론 비용 절감 | [2] | backdoor 제거/잔존 가능성 검토 |

## 4. 보안 이슈 30% 정리

Poisoning 공격은 학습 데이터나 라벨을 조작하여 모델 학습 결과를 왜곡하는 훈련 단계 공격이다[3]. Training data poisoning은 공격자 지식, 데이터 접근 범위, target 여부에 따라 threat model을 세분화해야 한다[4]. Label-flipping은 라벨을 다른 클래스로 바꾸는 비교적 단순한 poisoning이며, 전체 성능 저하나 특정 클래스 오류를 만들 수 있다.

Backdoor 공격은 clean accuracy가 높게 유지되더라도 trigger 조건에서 ASR이 높게 나타날 수 있으므로 별도 평가가 필요하다[5]. 따라서 W02에서 가장 중요한 지표 분리는 clean accuracy와 ASR이다. 정상 성능이 높아도 ASR이 높다면 보안적으로 실패한 모델일 수 있다.

**그림 1. 학습 데이터 오염 기반 ML 보안 평가 흐름**

```text
Clean Data / Poisoned Data
        |
        v
Training / Optimization
        |
        v
Model
        |
        +--> Clean Test Evaluation ----> Clean Accuracy, Macro F1
        |
        +--> Trigger Test Evaluation --> ASR
        |
        +--> Reproducibility Evidence -> seed, config, Docker, outputs
```

## 5. 논문 5편 요약

**표 2. 관련 문헌 5편 요약**

| ID | 논문 | 최종 서지 상태 | 핵심 기여 | W02 활용 |
|---|---|---|---|---|
| P01 | Optimization Methods for Large-Scale Machine Learning | SIAM Review, 60(2), 223-311, DOI `10.1137/16M1080173` | 대규모 최적화, SGD, noise reduction, second-order 방법 정리 | 데이터 오염이 목적함수와 gradient를 바꾼다는 원리 설명 |
| P02 | Efficient Deep Learning | ACM Computing Surveys, 55(12), 1-37, DOI `10.1145/3578938` | 모델 효율성, 압축, 비용-속도-품질 trade-off 정리 | 방어 비용과 배포 가능성을 평가표에 포함 |
| P03 | A Comprehensive Survey on Poisoning Attacks and Countermeasures in Machine Learning | ACM Computing Surveys, 55(8), 1-35, DOI `10.1145/3551636`; 저자명은 `Zhiyi Tian` | poisoning 공격과 대응책 taxonomy | 위협모형과 poisoning 평가 지표 근거 |
| P04 | Wild Patterns Reloaded | ACM Computing Surveys, 55(13s), 1-39, DOI `10.1145/3585385`; 강의계획서 제목과 동일 여부 확인 필요 | training data poisoning threat model과 방어 체계화 | 데이터 생명주기 기반 방어 체크리스트 |
| P05 | A survey of backdoor attacks and defences | Journal of Electronic Science and Technology, 23(3), Article 100326, DOI `10.1016/j.jnlest.2025.100326` | DNN부터 LLM까지 backdoor 공격/탐지/제거 정리 | clean accuracy와 ASR 동시 평가 근거 |

## 6. 논문 5편 비교표

| 논문 | 연구문제 | 핵심 방법 | 보안 위협 | 평가 지표 | 한계 | 내 논문 활용 |
|---|---|---|---|---|---|---|
| P01 | 대규모 ML에서 어떤 최적화 방법이 확장성과 수렴성을 보장하는가 | SGD, noise reduction, second-order method review | 직접 보안 공격은 아님 | 수렴성, 계산 비용, 일반화 | poisoning 지표 직접 제공 없음 | 학습 데이터 조작이 목적함수와 gradient에 미치는 영향 설명 |
| P02 | 모델을 더 작고 빠르고 효율적으로 만들려면 무엇을 고려해야 하는가 | 효율적 모델링, 압축, 시스템/하드웨어 survey | 효율화가 방어 비용과 검증 범위에 영향 | 정확도, latency, memory, FLOPs, cost | poisoning/backdoor 전용 문헌은 아님 | 방어 평가에 비용·속도·배포 가능성 추가 |
| P03 | poisoning 공격과 대응책을 어떻게 분류할 수 있는가 | 공격/방어 taxonomy | poisoning, backdoor, federated poisoning | accuracy drop, ASR, detection, robustness | 개별 실험 재현은 별도 필요 | W02 위협모형과 평가방법의 중심 근거 |
| P04 | training data poisoning 공격과 방어를 threat model 중심으로 어떻게 체계화할 수 있는가 | systematic survey, threat model 분석 | targeted/untargeted poisoning, clean-label, backdoor | clean accuracy, attack success, stealthiness, detection | 강의계획서 제목과 현재 로컬 PDF 제목 불일치 | 데이터 생명주기 기반 방어 체크리스트 |
| P05 | DNN부터 LLM까지 backdoor 공격과 방어는 어떻게 발전했는가 | backdoor attack/detection/removal/LLM survey | trigger 기반 조건부 오분류 | clean accuracy, ASR, trigger stealthiness, removal effect | LLM 환경 최신성 지속 갱신 필요 | clean accuracy-ASR 동시 평가 프레임 |

## 7. Research Track 분석

**표 3. W02 Research Track 요약**

| 항목 | 내용 |
|---|---|
| 연구문제 | 오염률과 공격 유형에 따라 clean accuracy, macro F1, ASR이 어떻게 변하는가 |
| 대상 시스템 | 지도학습 기반 분류 모델 |
| 보호 자산 | 학습 데이터, 라벨, 모델 파라미터, 검증셋, 예측 결과, 학습 로그 |
| 위협 | label-flipping poisoning, 안전한 toy backdoor trigger |
| 공격자 능력 | 일부 학습데이터 라벨 조작, 제한된 toy trigger 삽입 |
| 평가 지표 | clean accuracy, macro F1, ASR, stealthiness, reproducibility evidence |
| 재현성 | Docker, `pyproject.toml`, config, seed, outputs 로그 |
| 제외 범위 | 실제 개인정보, 실제 서비스, 무단 API, 운영 시스템 공격, 악성코드 실행 |

## 8. 실습 보고서

실습은 scikit-learn digits 데이터셋 기반으로 설계했다. 본 실습은 실제 공격 재현이 아니라 W02의 핵심인 데이터 오염 평가축을 안전하게 설명하기 위한 최소 toy protocol이다. 따라서 scikit-learn digits와 logistic regression을 사용하되, 평가 구조는 이후 딥러닝 모델과 대규모 모델에도 확장 가능하도록 clean accuracy, macro F1, ASR, reproducibility evidence로 분리하였다.

**표 4. W02 실습 설계**

| 단계 | 설계 내용 | 기록할 지표 | 안전 범위 |
|---|---|---|---|
| Clean baseline | 표준화 + Logistic Regression 학습 | accuracy, precision, recall, macro F1 | 공개 toy dataset |
| Label-flip 5/10/20% | 학습 라벨 일부를 다음 클래스로 변경 | accuracy drop, macro F1 | 교육용 시뮬레이션 |
| 안전한 toy backdoor 5% | 학습 샘플 일부에 단순 하단 픽셀 trigger 삽입 후 target label 부여 | clean accuracy, ASR | 실제 공격 절차로 일반화 금지 |
| 재현성 기록 | seed, config, Docker, outputs 저장 | CSV, JSON, run log | 로컬 실험 로그 |

**표 5. W02 실습 결과**

| 조건 | Poisoning Rate | N Poisoned | Clean Accuracy | Macro F1 | ASR | 근거 |
|---|---:|---:|---:|---:|---:|---|
| Clean baseline | 0% | 0 | 0.981481 | 0.981443 | 해당 없음 | `outputs/metrics_summary.csv` |
| Label-flip | 5% | 63 | 0.918519 | 0.918457 | 해당 없음 | `outputs/metrics_summary.csv` |
| Label-flip | 10% | 126 | 0.877778 | 0.877582 | 해당 없음 | `outputs/metrics_summary.csv` |
| Label-flip | 20% | 251 | 0.818519 | 0.818134 | 해당 없음 | `outputs/metrics_summary.csv` |
| Safe toy backdoor | 5% | 63 | 0.970370 | 0.970359 | 0.987654 | `outputs/metrics_summary.csv` |

해석은 제한적으로만 한다. Label-flip 조건은 오염률이 높아질수록 clean accuracy와 macro F1이 낮아지는 평가축을 보여준다. 안전한 toy backdoor 조건은 clean accuracy가 크게 유지되더라도 ASR이 높게 나올 수 있음을 설명하는 예시다. 이 결과는 실제 공격 성공률이나 실제 시스템 위험 수준으로 해석하지 않는다.

## 9. AI 도구 활용 기록

Codex를 사용해 폴더 상태 점검, 문헌 요약 보강, 이론노트 작성, 실험 코드 작성, Docker 실행 검증, 보고서 및 발표자료 작성을 수행했다. DOI/URL은 확인 가능한 근거가 있는 경우에만 기록했고, 정량값은 `outputs/` 파일 기준으로만 반영했다. 상세 기록은 `05_ai_worklog/`에 보존했다.

## 10. 토론 질문

1. Clean accuracy가 높고 ASR도 높은 모델은 어떤 의미에서 좋은 모델이 아닌가?
2. Label-flipping처럼 단순한 오염과 clean-label poisoning처럼 은닉적인 오염은 같은 지표로 평가할 수 있는가?
3. 모델 압축이나 pruning은 backdoor 방어에 도움이 되는가, 아니면 trigger를 더 숨길 수 있는가?
4. 제출 가능한 AI 보안 실습에서 실제 공격 재현과 안전한 toy simulation의 경계는 어디에 두어야 하는가?

## 11. 기말논문 연결

W02는 기말 논문의 관련연구, 위협모형, 평가방법, 보안적 함의 장에 직접 연결된다. 발전 가능한 주제는 "학습 데이터 오염과 backdoor 평가를 위한 다중지표 프레임워크"이다. 예상 기여는 오염률, clean accuracy, ASR, stealthiness, detection rate, efficiency cost, reproducibility evidence를 한 평가표에서 관리하는 것이다.

## 12. KCI 논문 형식 전환

### 12.1 KCI형 제목 후보

**표 6. KCI 논문 제목 후보**

| 번호 | 국문 제목 후보 | 영문 제목 후보 | 대상 시스템 | 보안 위협 | 연구방법 | 예상 기여 |
|---:|---|---|---|---|---|---|
| 1 | 학습 데이터 오염과 백도어 공격 평가를 위한 다중지표 프레임워크 연구 | A Multi-Metric Evaluation Framework for Training Data Poisoning and Backdoor Attacks | 지도학습 기반 분류 모델 | Label-flipping, Backdoor | 문헌분석 + toy 실험 | Clean accuracy와 ASR 분리 평가 |
| 2 | 데이터 오염률이 머신러닝 모델의 정상 성능과 공격 성공률에 미치는 영향 분석 | An Analysis of the Impact of Data Poisoning Rates on Clean Performance and Attack Success Rate in Machine Learning Models | 이미지 분류 모델 | 데이터 오염, Trigger backdoor | 오염률별 모의실험 | 오염률-성능 변화 분석 |
| 3 | AI 보안 평가에서 Clean Accuracy와 ASR 분리 기록의 필요성 연구 | A Study on the Need to Separately Report Clean Accuracy and Attack Success Rate in AI Security Evaluation | ML 보안 평가 시스템 | Backdoor, Poisoning | 평가 프로토콜 설계 | 다중지표 평가표 제안 |

### 12.2 추천 최종 제목

- 국문: 학습 데이터 오염과 백도어 공격 평가를 위한 다중지표 프레임워크 연구
- 영문: A Multi-Metric Evaluation Framework for Training Data Poisoning and Backdoor Attacks

### 12.3 국문초록 초안

본 연구는 학습 데이터 오염과 백도어 공격이 머신러닝 모델의 정상 성능과 공격 조건 성능에 미치는 영향을 분석하고, 이를 평가하기 위한 다중지표 프레임워크를 제안한다. 대규모 최적화와 효율적 딥러닝 문헌을 통해 학습 과정이 데이터 품질과 비용 제약에 민감하다는 점을 정리하고, poisoning 및 backdoor 관련 선행연구를 바탕으로 clean accuracy, macro F1, attack success rate, stealthiness, reproducibility evidence의 평가축을 도출한다. 또한 scikit-learn digits 공개 데이터셋을 활용한 안전한 toy experiment를 통해 label-flipping 오염률 변화와 toy backdoor 조건에서의 clean accuracy와 ASR 차이를 기록한다. 본 연구는 AI 보안 평가에서 정상 성능과 공격 성공률을 분리해 보고해야 함을 보이며, 학습 데이터 오염 위협에 대한 KCI형 모의투고 논문 주제로 확장될 수 있다.

### 12.4 영문초록 초안

This study analyzes how training data poisoning and backdoor attacks affect both clean performance and attack-condition performance of machine learning models. Based on studies on large-scale optimization, efficient deep learning, poisoning attacks, and backdoor defenses, this report derives a multi-metric evaluation framework consisting of clean accuracy, macro F1, attack success rate, stealthiness, and reproducibility evidence. A safe toy experiment using the public scikit-learn digits dataset is used to compare clean baseline performance, label-flipping poisoning at different rates, and a toy backdoor condition. The results illustrate the need to separately report clean accuracy and attack success rate in AI security evaluation. The proposed framework can be extended into a KCI-style research paper on training data poisoning and backdoor evaluation.

### 12.5 키워드

| 구분 | 키워드 |
|---|---|
| 국문 | 데이터 오염, 백도어 공격, 대규모 최적화, 머신러닝 보안, ASR, 재현성 |
| 영문 | Data Poisoning, Backdoor Attack, Large-Scale Optimization, Machine Learning Security, Attack Success Rate, Reproducibility |

### 12.6 연구문제

- RQ1. 데이터 오염률이 증가할 때 clean accuracy와 macro F1은 어떻게 변하는가?
- RQ2. Toy backdoor 조건에서 clean accuracy가 유지되더라도 ASR이 높게 나타날 수 있는가?
- RQ3. Poisoning/backdoor 평가에는 clean accuracy, macro F1, ASR, stealthiness, reproducibility evidence 중 어떤 지표 조합이 필요한가?

### 12.7 연구방법

- 문헌분석: 최적화, 효율적 딥러닝, poisoning, backdoor 관련 W02 논문 5편 비교
- 위협모형: 학습 데이터, 라벨, trigger, 모델 파라미터, 검증셋을 보호 자산으로 설정
- 모의실험: scikit-learn digits 데이터셋 기반 clean baseline, label-flip 5/10/20%, toy backdoor 5% 실험
- 평가방법: clean accuracy, macro F1, ASR, poisoning rate, n_poisoned, reproducibility evidence 기록
- 한계분석: toy dataset과 logistic regression의 외적 타당성 한계 명시

### 12.8 보안적 함의

- Integrity: 학습 데이터와 라벨 조작은 모델 결정경계를 바꾼다.
- Availability: 오염률 증가에 따라 정상 성능이 저하될 수 있다.
- Safety: backdoor는 특정 trigger 조건에서 목표 오분류를 유발할 수 있다.
- Accountability: 데이터 출처, 오염률, seed, config, 실행 로그가 보존되어야 한다.
- Reproducibility: 실험 수치는 outputs 파일과 보고서 수치가 일치해야 한다.

### 12.9 KCI 제출 가능성 점검표

| 점검 항목 | 상태 |
|---|---|
| 국문·영문 제목 후보 작성 | 완료 |
| 국문초록 초안 작성 | 완료 |
| 영문초록 초안 작성 | 완료 |
| 키워드 작성 | 완료 |
| 연구문제 작성 | 완료 |
| 연구방법 작성 | 완료 |
| 표 1개 이상 포함 | 완료 |
| 그림 1개 이상 포함 | 완료 |
| 국내 참고문헌 3편 이상 | 확인 필요 |
| 해외 참고문헌 5편 이상 | W02 기준 완료 |
| AI 활용 고지 | 완료 |
| 실험 outputs 파일 존재 | 완료 |

## 13. SCI 논문 형식 전환

### 13.1 SCI 제목 후보

A Multi-Metric Evaluation Framework for Training Data Poisoning and Backdoor Attacks: Separating Clean Performance, Attack Success Rate, and Reproducibility Evidence

### 13.2 Structured Abstract

#### Background

Training data poisoning and backdoor attacks threaten the integrity and reliability of machine learning models by manipulating the training process rather than only the inference-time inputs.

#### Problem

Many evaluations report clean accuracy without sufficiently separating poisoning impact, attack success rate, stealthiness, and reproducibility evidence. This makes it difficult to compare poisoning and backdoor risks across studies.

#### Method

This study synthesizes five representative studies on large-scale optimization, efficient deep learning, poisoning attacks, training data manipulation, and backdoor attacks. It also performs a safe toy experiment using the public scikit-learn digits dataset to compare clean baseline, label-flipping poisoning at multiple rates, and a toy backdoor condition.

#### Results

The W02 toy experiment records clean accuracy and macro F1 under label-flipping rates of 5%, 10%, and 20%, and separately reports ASR under a toy backdoor setting. These results should not be interpreted as real-world attack performance, but as an example of structured AI security reporting.

#### Contribution

The main contribution is a multi-metric evaluation structure that separates clean performance, poisoning impact, backdoor ASR, stealthiness, efficiency cost, and reproducibility evidence.

#### Implications

The framework can be extended to later topics such as self-supervised backdoors, federated learning poisoning, LLM backdoors, RAG data contamination, and MLOps supply-chain security.

### 13.3 Introduction 구성

- Training-stage attack과 inference-stage attack의 차이
- 대규모 최적화에서 데이터 품질이 중요한 이유
- Poisoning/backdoor 평가에서 clean accuracy 단독 보고의 한계
- ASR, stealthiness, reproducibility evidence의 필요성
- 본 연구의 contribution

### 13.4 Related Work 축

**표 7. SCI Related Work 축**

| 연구축 | 대표 논문 | 역할 |
|---|---|---|
| Large-scale optimization | Bottou et al. | 학습 목적함수와 SGD 기반 최적화 |
| Efficient deep learning | Menghani | 정확도-비용-속도 trade-off |
| Poisoning attacks | Tian et al. | poisoning taxonomy와 대응책 |
| Training data poisoning | Cina et al. 또는 현재 P04 | threat model과 systematic review |
| Backdoor attacks | Jin et al. | clean accuracy와 ASR 분리 평가 |

### 13.5 Threat Model

- Target system: supervised image classification model
- Protected assets: training data, labels, validation set, model parameters, predictions, logs
- Adversary knowledge: black-box, gray-box, white-box
- Adversary capability: label flipping, partial training data manipulation, toy trigger insertion
- Attack success condition: clean accuracy degradation or target-label prediction under trigger condition
- Excluded scope: real-world system compromise, unauthorized API query, personal data use, malware execution

### 13.6 Methodology

- Literature matrix construction
- Poisoning/backdoor threat model design
- Public toy dataset experiment
- Clean baseline evaluation
- Label-flip poisoning evaluation
- Toy backdoor ASR evaluation
- Reproducibility evidence collection

### 13.7 Experimental Setup

| Item | Description |
|---|---|
| Dataset | scikit-learn digits |
| Model | Logistic regression with standardization |
| Baseline | Clean baseline |
| Poisoning scenario | Label-flip 5%, 10%, 20% |
| Backdoor scenario | Toy pixel trigger, 5% poisoned training samples |
| Metrics | Clean accuracy, precision_macro, recall_macro, macro F1, ASR, n_poisoned |
| Environment | Ubuntu 24.04 / Docker / Python 3.11 |
| Seed | 42 |
| Output files | metrics_summary.csv, results.json, run_log.md |

### 13.8 Results

실험 결과는 표 5와 같다. 모든 수치는 `04_experiment/outputs/metrics_summary.csv`, `results.json`, `run_log.md` 기준으로 기록했다.

### 13.9 Discussion

- Label-flipping은 전체 성능 저하를 유발할 수 있다.
- Backdoor는 clean accuracy가 유지되어도 ASR이 높으면 보안적으로 실패다.
- Clean accuracy와 ASR은 반드시 분리해 보고해야 한다.
- Toy dataset 결과는 실제 대규모 모델이나 LLM backdoor를 대표하지 않는다.
- 재현성 증거는 seed, config, Docker, outputs 파일 보존으로 확보해야 한다.

### 13.10 Limitations and Threats to Validity

- Internal validity: logistic regression과 digits dataset이 deep neural network의 backdoor dynamics를 직접 대표하지 않는다.
- External validity: digits dataset은 실제 보안 데이터, foundation model, LLM fine-tuning, data supply chain을 대표하지 않는다.
- Construct validity: toy trigger ASR은 실제 공격 성공률이 아니라 평가축 설명용 지표다.
- Reproducibility: outputs 파일과 보고서 수치의 일치가 필요하다.
- Literature validity: P02/P04의 arXiv판과 최종 출판판 차이, P04 제목 불일치를 확인해야 한다.

### 13.11 Conclusion

W02는 데이터 오염과 backdoor 위협을 최적화 과정과 평가 지표 관점에서 연결한다. 핵심 결론은 clean accuracy, macro F1, ASR, stealthiness, efficiency cost, reproducibility evidence를 분리해 기록해야 한다는 것이다. 이 구조는 후속 주차의 backdoor, federated learning poisoning, LLM security, MLOps supply-chain risk로 확장될 수 있다.

## 14. 발표용 요약

- 핵심 메시지: 데이터 오염은 학습 목적함수와 gradient를 바꾸며, backdoor 평가는 clean accuracy와 ASR을 분리해야 한다.
- 발표 흐름: 최적화 원리 -> 데이터 오염 위협 -> 문헌 비교 -> 안전한 toy 실험 -> 기말논문 연결.
- 강조 수치: label-flip 20%에서 clean accuracy 0.818519, 안전한 toy backdoor 5%에서 clean accuracy 0.970370 및 ASR 0.987654.
- 한계 문장: 이 수치는 실제 공격 성능이 아니라 공개 toy 데이터셋에서 평가 지표 분리 방식을 설명하는 예시다.

## 15. 참고문헌 검증표

| 번호 | 문헌 | DOI/URL | 검증 상태 | 남은 확인 |
|---:|---|---|---|---|
| [1] | Bottou et al., "Optimization Methods for Large-Scale Machine Learning" | `https://doi.org/10.1137/16M1080173` | 확인 완료 | 없음 |
| [2] | Menghani, "Efficient Deep Learning" | `https://doi.org/10.1145/3578938`; `https://arxiv.org/abs/2106.08962` | 확인 완료 | ACM Article 번호 확인 필요 |
| [3] | Tian et al., "A Comprehensive Survey on Poisoning Attacks and Countermeasures in Machine Learning" | `https://doi.org/10.1145/3551636` | 확인 완료 | 강의계획서 저자명 오탈자 확인 |
| [4] | Cina et al., "Wild Patterns Reloaded" | `https://doi.org/10.1145/3585385`; `https://arxiv.org/abs/2205.01992` | DOI 확인 완료 / 지정 제목 동일 여부 확인 필요 | 강의계획서 P04 제목과 동일 여부 |
| [5] | Jin et al., "A survey of backdoor attacks and defences" | `https://doi.org/10.1016/j.jnlest.2025.100326` | 확인 완료 | 없음 |

## 16. 자기 점검표

| 점검 항목 | 상태 | 비고 |
|---|---|---|
| 1장 한 문장 요약 작성 | 완료 |  |
| 2장 학습 배경과 주차 목표 작성 | 완료 |  |
| AI 원리 70% 정리 | 완료 |  |
| 보안 이슈 30% 정리 | 완료 |  |
| 논문 5편 요약 | 완료 |  |
| 논문 5편 비교표 | 완료 |  |
| Research Track 5요소 작성 | 완료 | 연구문제, 위협모형, 평가방법, 재현성, 오픈문제 |
| P02 최종 출판판 검증 | 완료 | DOI `10.1145/3578938`; Article 번호 확인 필요 |
| P04 최종 출판판 검증 | 확인 필요 | DOI `10.1145/3585385`는 확인. 강의계획서 제목과 동일 여부 확인 필요 |
| 실험 outputs 파일 존재 확인 | 완료 | CSV/JSON/run log 존재 |
| 실험 결과와 보고서 수치 일치 | 완료 | outputs 기준 반영 |
| KCI 논문 형식 전환 작성 | 완료 |  |
| SCI 논문 형식 전환 작성 | 완료 |  |
| 본문 인용과 참고문헌 대응 | 완료 | [1]-[5] 대응 |
| 표·그림 번호 정리 | 완료 | 표 1-7, 그림 1 |
| AI 활용 고지 작성 | 완료 | `05_ai_worklog/ai_disclosure_draft.md` |
| PDF 저작권 위험 점검 | 완료 | PDF 5개 Git 추적 중. 삭제는 미수행 |
| 최종 사람이 검토할 항목 표시 | 완료 | P04, Article 번호, PDF 정책 |

## 참고문헌

[1] Leon Bottou, Frank E. Curtis, and Jorge Nocedal, "Optimization Methods for Large-Scale Machine Learning," SIAM Review, 60(2), 223-311, 2018. DOI: `10.1137/16M1080173`.

[2] Gaurav Menghani, "Efficient Deep Learning: A Survey on Making Deep Learning Models Smaller, Faster, and Better," ACM Computing Surveys, 55(12), 1-37, 2023. DOI: `10.1145/3578938`.

[3] Zhiyi Tian, Lei Cui, Jie Liang, and Shui Yu, "A Comprehensive Survey on Poisoning Attacks and Countermeasures in Machine Learning," ACM Computing Surveys, 55(8), 1-35, 2022/2023. DOI: `10.1145/3551636`.

[4] Antonio Emanuele Cina et al., "Wild Patterns Reloaded: A Survey of Machine Learning Security against Training Data Poisoning," ACM Computing Surveys, 55(13s), 1-39, 2023. DOI: `10.1145/3585385`. 강의계획서 P04 제목과 동일 여부 확인 필요.

[5] Ling-Xin Jin et al., "A survey of backdoor attacks and defences: From deep neural networks to large language models," Journal of Electronic Science and Technology, 23(3), Article 100326, 2025. DOI: `10.1016/j.jnlest.2025.100326`.
