# W01 제출용 단일 보고서

## 딥러닝 패러다임 & ML 보안 분류학

## 0. 메타정보

| 항목 | 내용 |
|---|---|
| 주차 | W01 |
| 보고서 제목 | 딥러닝 패러다임 & ML 보안 분류학 |
| 과목 범위 | AI 보안 |
| 작성자 | 박영세 |
| 학번 | 26200122 |
| 작성일 | 2026-06-26 |
| 문서 상태 | 주차별 단일 제출용 보고서 |
| 원본 관리 파일 | `03_weekly_reports/w01_deep_learning_ml_security/07_week_submission/w01_submission_report.md` |
| Word/PDF 제출본 권장 위치 | `03_weekly_reports/w01_deep_learning_ml_security/07_week_submission/exports/` |
| 관련 산출물 위치 | `03_weekly_reports/w01_deep_learning_ml_security/` |
| 안전 범위 | 실제 개인정보, 운영망 데이터, 무단 API 질의, 악성코드 실행 제외 |
| 제출 전 주의 | P04는 강의계획서 지정 IEEE COMST 논문과 동일 여부를 최종 확인해야 함 |

---

## 초록

본 보고서는 W01 주차의 딥러닝 원리와 ML 보안 분류학을 하나의 제출용 보고서로 통합한다. 딥러닝은 원시 입력에서 계층적 표현을 학습하고, 손실함수의 gradient를 이용해 파라미터를 갱신함으로써 높은 예측 성능을 달성한다. 그러나 이러한 구조는 입력 교란, 학습 데이터 오염, 침입탐지 오탐·미탐, 프라이버시 누출, 재현성 실패와 같은 보안 문제와 직접 연결된다. 본 보고서는 W01 논문 5편을 바탕으로 AI 보안 평가를 clean performance, robust performance, privacy leakage, reproducibility evidence의 네 축으로 정리하고, synthetic toy evaluation 결과를 통해 정상 성능, 라벨 노이즈, 입력 교란, 과적합 신호를 분리 기록하였다. 실험은 실제 개인정보나 운영 서비스를 사용하지 않으며, 결과는 실제 공격 성공이 아니라 보안 평가 보고 구조의 예시로 한정한다.

**키워드:** 딥러닝, ML 보안, 생명주기 보증, 침입탐지, 대적 공격, 프라이버시 공격, 재현성

---

## 1. 한 문장 요약

W01은 딥러닝을 “정확도를 내는 모델”이 아니라 데이터, 학습, 검증, 배포, 모니터링 전 단계에서 검증해야 하는 **ML 생명주기 기반 보안 시스템**으로 재정의하는 기준 주차다.

---

## 2. 학습 배경과 주차 목표

### 2.1 이번 주 주제의 위치

W01은 전체 AI 보안 세미나의 기준 프레임을 세우는 주차다. 이후 W02 데이터 오염, W03 비전 대적공격, W07 LLM 보안, W08 RAG 프롬프트 인젝션, W11 차등프라이버시, W14 MLOps 공급망 보안은 모두 W01에서 정리한 ML 생명주기, 위협모형, 평가방법, 재현성 기준 위에서 해석된다.

### 2.2 강의계획서상 학습목표

- 딥러닝 핵심 구성요소를 공통 언어로 정리한다.
- ML lifecycle assurance desiderata를 정의한다.
- 침입탐지, 대적 공격, 프라이버시 공격을 ML 보안 분류학으로 연결한다.
- 주차별 논문 요약을 기말논문의 연구문제, 위협모형, 평가방법, 재현성 구조로 확장한다.

### 2.3 이번 주 핵심 질문

1. 딥러닝은 왜 단순 모델이 아니라 생명주기 시스템으로 평가해야 하는가?
2. clean accuracy만으로 ML 보안성을 설명할 수 없는 이유는 무엇인가?
3. 대적 공격, 프라이버시 공격, 침입탐지 오류는 어떤 평가축으로 분리해야 하는가?
4. W01의 문헌과 실습을 기말 KCI 논문 주제로 발전시키려면 어떤 연구문제가 적절한가?

---

## 3. 논문 5편의 서술형 종합 요약

### 3.1 P01. Deep learning

P01은 딥러닝의 기본 원리를 설명하는 핵심 문헌이다. 딥러닝은 원시 입력을 여러 층의 비선형 변환을 거쳐 점점 더 추상적인 표현으로 바꾸는 방식으로 학습한다. 이미지에서는 낮은 층이 edge나 texture를 학습하고, 높은 층은 object나 semantic pattern을 학습한다. 텍스트와 음성에서도 낮은 수준의 신호가 점차 의미 있는 representation으로 변환된다.

딥러닝이 중요한 이유는 사람이 직접 feature를 설계하지 않아도 모델이 데이터에서 표현을 학습할 수 있기 때문이다. 그러나 보안 관점에서는 이 장점이 동시에 취약점이 된다. 모델 내부 표현이 사람이 직접 해석하기 어렵기 때문에, 작은 입력 교란이 예측을 바꾸거나, 학습 데이터의 편향과 민감 정보가 모델 내부에 반영될 수 있다.

### 3.2 P02. Assuring the Machine Learning Lifecycle

P02는 ML 시스템을 단순 모델이 아니라 생명주기 전체에서 보증해야 한다고 설명한다. ML 시스템은 데이터 수집, 데이터 전처리, 모델 학습, 검증, 배포, 운영 모니터링을 거친다. 각 단계에는 서로 다른 위험이 존재한다. 데이터 수집 단계에서는 데이터 품질과 편향 문제가 발생하고, 학습 단계에서는 과적합과 poisoning 위험이 있으며, 배포 이후에는 drift, 입력 분포 변화, 운영 로그 누락 문제가 발생할 수 있다.

이 논문은 AI 보안 평가를 “모델 정확도”에서 “증거 기반 생명주기 보증”으로 확장한다. 보안성을 주장하려면 데이터 출처, 학습 설정, 모델 버전, seed, 평가 지표, 로그, human review 기록이 남아 있어야 한다.

### 3.3 P03. A Survey of Data Mining and Machine Learning Methods for Cyber Security Intrusion Detection

P03은 ML이 사이버보안 침입탐지에 어떻게 적용되는지 정리한다. 침입탐지는 네트워크 트래픽, 시스템 로그, 사용자 행동 데이터에서 정상과 이상을 구분하는 문제다. 이때 ML 모델은 classification, clustering, anomaly detection, ensemble learning 등 다양한 방식으로 사용된다.

보안 관점에서 침입탐지는 단순히 accuracy가 높다고 좋은 시스템이 아니다. 정상 트래픽을 공격으로 잘못 판단하면 false positive가 증가하고, 실제 공격을 놓치면 false negative가 발생한다. 운영 환경에서는 오탐이 많으면 보안 담당자의 피로도가 증가하고, 미탐이 많으면 실제 침해 사고로 이어질 수 있다.

### 3.4 P04. Adversarial Attacks and Defenses in Machine Learning-Powered Networks: A Contemporary Survey

P04는 대적공격과 방어를 정리하는 관련 문헌이다. 대적공격은 입력에 작고 의도적인 교란을 추가해 모델의 예측을 바꾸는 공격이다. 이미지 분류에서는 사람이 보기에는 거의 같은 이미지라도 모델은 다른 class로 잘못 분류할 수 있다. 네트워크 환경에서는 traffic feature나 protocol behavior가 조작되어 탐지기를 우회할 수 있다.

이 논문은 W01에서 clean accuracy와 robust accuracy를 분리해야 한다는 점을 보여준다. 모델이 정상 입력에서는 높은 정확도를 보이더라도, 공격자가 만든 교란 입력에서 성능이 급격히 떨어지면 안전한 모델이라고 할 수 없다.

주의: 현재 W01의 P04는 강의계획서 지정 IEEE Communications Surveys & Tutorials 논문과 동일 여부를 최종 확인해야 한다. 제출 전 지정 논문으로 교체할지, 현재 arXiv 관련 논문을 주차 주제 보강 문헌으로 사용할지 결정해야 한다.

### 3.5 P05. A Survey of Privacy Attacks in Machine Learning

P05는 ML 프라이버시 공격을 체계화한다. 대표적인 공격에는 membership inference, model inversion, property inference, model extraction 등이 있다. Membership inference는 특정 데이터가 학습 데이터에 포함되었는지 추론하는 공격이고, model inversion은 모델 출력이나 confidence를 통해 입력의 민감 속성을 추정하는 공격이다.

프라이버시 공격이 중요한 이유는 모델이 높은 성능을 보이더라도 학습 데이터에 대한 정보를 과도하게 기억하거나 노출할 수 있기 때문이다. 특히 train-test gap이 크거나 confidence score가 과도하게 뚜렷한 경우, 공격자는 이를 이용해 학습 데이터 포함 여부를 추론할 수 있다.

---

## 4. 논문 간 연결 관계

W01 논문 5편은 다음 흐름으로 연결된다.

```text
딥러닝 기본 원리
→ ML 생명주기 보증
→ 침입탐지 응용
→ 대적공격과 강건성 평가
→ 프라이버시 공격과 정보 누출 평가
```

P01은 딥러닝이 어떻게 표현을 학습하는지 설명한다. P02는 그 모델을 실제 시스템으로 운영할 때 생명주기 전체를 보증해야 함을 제시한다. P03은 딥러닝과 ML이 침입탐지라는 보안 응용에서 어떻게 쓰이는지 보여준다. P04는 이러한 ML 모델이 공격자 입력에 의해 어떻게 조작될 수 있는지 설명하고, P05는 모델이 학습 데이터와 민감 정보를 노출할 수 있음을 보여준다.

따라서 W01의 핵심 결론은 명확하다. AI 보안 평가는 모델 정확도 하나로 끝나지 않는다. **성능, 강건성, 프라이버시, 재현성**을 분리해 측정하고, 이 결과를 ML 생명주기 증거로 남겨야 한다.

---

## 5. AI 원리 70% 정리

딥러닝은 원시 입력에서 계층적 표현을 학습하는 방식으로 발전해 왔다. LeCun, Bengio, Hinton의 논문은 표현학습, 역전파, CNN/RNN 계열 모델의 기본 원리를 정리한다. 보안 관점에서 이 원리는 중요하다. 공격자가 모델 입력이나 데이터 분포를 조작할 때 실제로 영향을 받는 것은 모델의 내부 표현과 decision boundary이기 때문이다.

학습은 손실함수를 최소화하는 파라미터를 찾는 과정이며, 일반화는 학습 데이터 밖에서도 성능이 유지되는지를 의미한다. 과적합은 일반적인 성능 저하 문제에 그치지 않고 membership inference와 같은 privacy leakage 위험의 배경이 될 수 있다.

### 5.1 핵심 수식

딥러닝 학습은 손실함수 최소화 문제로 표현할 수 있다.

$$
L(\theta)=\frac{1}{N}\sum_{i=1}^{N}\ell(f_{\theta}(x_i),y_i)
$$

| 기호 | 의미 |
|---|---|
| $\theta$ | 모델 파라미터 |
| $f_{\theta}$ | 학습 모델 |
| $\ell$ | 손실함수 |
| $N$ | 학습 샘플 수 |

파라미터는 gradient를 이용해 갱신된다.

$$
\theta_{t+1}=\theta_t-\eta\nabla_{\theta}L(\theta_t)
$$

| 기호 | 의미 |
|---|---|
| $\eta$ | learning rate |
| $\nabla_{\theta}L$ | 파라미터에 대한 손실함수 gradient |

정상 성능과 공격 조건 성능은 분리해 평가해야 한다.

$$
RobustAcc=\frac{N_{rob}}{N_{test}}
$$

| 기호 | 의미 |
|---|---|
| $N_{test}$ | 전체 평가 샘플 수 |
| $N_{rob}$ | 교란 조건에서도 정답을 맞힌 샘플 수 |

과적합에 따른 프라이버시 위험 신호는 train-test gap으로 점검할 수 있다.

$$
GenGap=Acc_{train}-Acc_{test}
$$

### 5.2 핵심 개념과 보안 연결

| 핵심 개념 | 의미 | 보안 연결 |
|---|---|---|
| 표현학습 | 원시 입력에서 유용한 특징을 모델이 직접 학습 | 대적 입력이 내부 표현을 왜곡할 수 있음 |
| 역전파 | gradient를 이용한 파라미터 갱신 | gradient 기반 공격의 기술적 배경 |
| 일반화 | 새 데이터에서도 성능이 유지되는 성질 | clean 성능과 robust 성능의 분리 필요 |
| 과적합 | 학습 데이터에 과도하게 맞는 상태 | privacy leakage와 membership inference 위험 신호 |
| 생명주기 증거 | 데이터, 설정, 실행 로그, 검토 기록 | 보안 주장의 재현성 검토 조건 |

---

## 6. 보안 이슈 30% 정리

ML 시스템 보증은 데이터 수집, 학습, 검증, 배포 전 단계의 증거 관리 문제로 볼 수 있다. 침입탐지에서는 정확도뿐 아니라 오탐과 미탐을 분리해 평가해야 한다. 대적 공격 연구는 clean accuracy와 robust accuracy를 분리해 보고해야 함을 보여준다. 프라이버시 공격 연구는 모델 출력이 학습 데이터 포함 여부나 민감 속성을 노출할 수 있음을 지적한다.

| 보안 속성 | ML 보안 문제 | 대표 위협 | W01 평가 관점 |
|---|---|---|---|
| Confidentiality | 학습 데이터와 민감 정보 노출 | membership inference, model inversion | privacy leakage |
| Integrity | 예측 결과 조작 | adversarial example, poisoning | robust performance |
| Availability | 탐지 실패 또는 오탐 폭증 | IDS 미탐, 오탐 비용 증가 | false positive/false negative |
| Accountability | 결과 재현과 책임 추적 실패 | seed, config, 로그 누락 | reproducibility evidence |

---

## 7. Research Track 분석

### 7.1 연구문제

- RQ1. ML 생명주기 각 단계에서 AI 보안 평가를 위해 필요한 최소 증거는 무엇인가?
- RQ2. clean performance, robust performance, privacy leakage, reproducibility evidence를 통합한 평가 체크리스트는 어떻게 구성할 수 있는가?
- RQ3. synthetic toy evaluation은 실제 AI 보안 평가 프레임워크를 설명하는 데 어떤 장점과 한계를 가지는가?

### 7.2 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | 학습 데이터, 평가 데이터, 모델 파라미터, 입력 데이터, 출력 confidence, 운영 로그 |
| 공격자 목표 | 모델 오분류 유도, 침입탐지 우회, 학습 데이터 포함 여부 추론, 민감 정보 추정 |
| 공격자 지식 | white-box, gray-box, black-box |
| 공격자 능력 | 입력 조작, 반복 질의, 출력 관찰, 일부 데이터 기여 |
| 공격 경로 | 데이터 수집 → 학습 → 검증 → 배포 → 모니터링 |
| 방어자 능력 | robust evaluation, privacy audit, data provenance, logging, human review |
| 제외 범위 | 실제 운영망 공격, 개인정보 사용, 무단 API 반복 질의, 악성코드 실행 |

### 7.3 평가축

| 평가축 | 질문 | 대표 지표 또는 증거 |
|---|---|---|
| Clean performance | 정상 조건에서 잘 맞는가 | accuracy, precision, recall, F1 |
| Robust performance | 교란 조건에서도 유지되는가 | robust accuracy, performance drop |
| Privacy leakage | 데이터 포함 여부나 민감 정보가 새는가 | train-test gap, confidence signal |
| Reproducibility evidence | 같은 결과를 다시 만들 수 있는가 | seed, config, code, logs, DOI/URL 검증 |

### 7.4 재현성

재현성을 위해 DOI/URL 검증표, 로컬 PDF 목록, Dockerfile, `pyproject.toml`, config, seed, 실행 소스, 결과 파일을 보존한다. W01 실습 결과는 `04_experiment/outputs/`에 저장된 것으로 보고서에 기록한다.

---

## 8. 실습 보고서 및 그래프 수치 검증

실습은 안전한 synthetic toy evaluation, 즉 실제 개인정보와 운영 서비스를 쓰지 않는 synthetic 기반 안전 모의실험으로 제한하였다. 본 실습은 딥러닝 성능 재현이 아니라 W01의 핵심인 ML 보안 평가축을 안전하게 설명하기 위한 최소 toy protocol이다. 따라서 로지스틱 회귀를 사용하되, 평가 구조는 이후 딥러닝 모델에도 동일하게 확장 가능하도록 clean performance, perturbation impact, privacy-safe audit, reproducibility evidence로 분리하였다.

### 8.1 실습 설계

| 항목 | 내용 |
|---|---|
| 데이터 | synthetic binary classification data |
| 모델 | toy logistic regression |
| 조건 1 | clean baseline |
| 조건 2 | label-noise training |
| 조건 3 | toy feature perturbation |
| 조건 4 | privacy-safe overfitting/confidence audit |
| Seed | 42 |
| 결과 위치 | `04_experiment/outputs/` |

### 8.2 실습 결과 수치

| 조건 | Accuracy | Precision | Recall | F1 | 보안 해석 |
|---|---:|---:|---:|---:|---|
| Clean baseline | 0.869444 | 0.867403 | 0.872222 | 0.869806 | 정상 synthetic test split 기준 |
| Label-noise training | 0.838889 | 0.827957 | 0.855556 | 0.841530 | training label 126개 flip 후 성능 저하 |
| Toy feature perturbation | 0.844444 | 0.848315 | 0.838889 | 0.843575 | Gaussian feature noise 조건에서 성능 저하 |

Privacy-safe audit 결과 train accuracy는 0.857143, test accuracy는 0.869444, train-test gap은 -0.012301로 나타났고 risk label은 `low_overfitting_signal`로 기록되었다. 이 결과는 synthetic data의 과적합 신호 점검이며, 실제 데이터 대상 membership inference 공격 결과로 해석하지 않는다.

### 8.3 그래프 수치 검증

현재 제출 보고서의 그래프는 `assets/w01_metric_chart.png`를 참조한다. 그래프의 원천은 `04_experiment/outputs/metrics_summary.csv`로 표시되어 있으며, 확인 가능한 SVG 그래프에는 accuracy와 F1 두 series가 표시되어 있다. 따라서 그래프 해석은 accuracy와 F1 비교로 제한한다. Precision과 recall은 표에는 포함하지만 현재 그래프 series에는 포함하지 않는다.

| 조건 | 그래프 Accuracy | 표 Accuracy | 그래프 F1 | 표 F1 | 확인 결과 |
|---|---:|---:|---:|---:|---|
| Clean baseline | 0.869444 | 0.869444 | 0.869806 | 0.869806 | 일치 |
| Label-noise training | 0.838889 | 0.838889 | 0.841530 | 0.841530 | 일치 |
| Toy feature perturbation | 0.844444 | 0.844444 | 0.843575 | 0.843575 | 일치 |

<!-- submission-metric-chart:start -->
**그림 1. W01 metrics summary chart**

![W01 metrics summary chart](assets/w01_metric_chart.png)

출처: `04_experiment/outputs/metrics_summary.csv`. 이 그래프는 공개 toy/synthetic 산출물 기반이며 실제 공격 성능이나 운영 환경 성능으로 일반화하지 않는다. 현재 그래프는 accuracy와 F1만 시각화한다.
<!-- submission-metric-chart:end -->

---

## 9. 기말논문 연결

W01은 기말 논문의 상위 프레임을 제공한다. 발전 가능한 주제는 “ML 생명주기 기반 AI 보안 평가 프레임워크 연구”이다. 이후 주차의 poisoning, adversarial example, LLM security, RAG prompt injection, federated learning, differential privacy, MLOps supply chain 이슈를 데이터 관리, 모델 학습, 검증, 배포·운영 단계에 매핑할 수 있다.

| 기말논문 장 | W01 반영 내용 |
|---|---|
| 1장 서론 | 정확도 중심 AI 평가의 한계와 AI 보안 평가 필요성 |
| 2장 관련연구 | 딥러닝, ML 생명주기, 침입탐지, 대적공격, 프라이버시 공격 |
| 3장 위협모형 | 데이터, 모델, 입력, 출력, 로그를 보호 자산으로 정의 |
| 4장 연구방법 | clean, robust, privacy, reproducibility 평가축 설계 |
| 5장 분석 | synthetic toy evaluation 결과와 평가 체크리스트 |
| 6장 결론 | AI 보안 평가는 생명주기 증거와 함께 관리되어야 함 |

---

## 10. AI 도구 활용 기록

AI 도구는 문헌 요약, 코드 점검, 문장 구조화, 그래프 생성 보조에 사용하였다. 모든 DOI/URL, 실험 수치, 본문 인용, 결론은 작성자가 outputs 파일과 로컬 참고문헌 검증표를 대조하여 검증한다.

| 항목 | 내용 |
|---|---|
| 사용 도구명 | Codex, ChatGPT 계열 도구 |
| 사용 목적 | 문헌 요약 정리, 보고서 구조화, 안전한 toy/synthetic 실험 결과 표기 점검, 그래프 생성 보조, 제출 전 체크리스트 정리 |
| AI 산출물 반영 위치 | `07_week_submission/w01_submission_report.md`, `07_week_submission/assets/w01_metric_chart.png`, `05_ai_worklog/ai_disclosure_draft.md` |
| 본인 수정 내용 | 주차별 문헌 상태 확인, 실험 수치와 outputs 대조, 안전 범위와 한계 문장 확인, 최종 제출 전 미확정 문헌 분리 |
| 사실관계 검증 방법 | `01_papers/paper_list.md`, `01_papers/doi_check.md`, `05_references/doi_index.md`, 강의계획서 문헌표 대조 |
| 실험결과 검증 방법 | `04_experiment/outputs/metrics_summary.csv`, `results.json`, `run_log.md`의 수치와 보고서 표기 대조 |
| 최종 책임 확인 | AI 산출물은 초안 보조이며 최종 제출자는 원고 내용, 인용, 실험결과, 연구윤리 책임을 확인한다. |

---

## 11. 제출 전 자기 점검표

| 점검 항목 | 상태 | 비고 |
|---|---|---|
| 메타정보 작성 | 완료 | 작성일 2026-06-26 반영 |
| 초록 및 키워드 작성 | 완료 |  |
| AI 원리 70% 정리 | 완료 | 핵심 수식 추가 |
| 보안 이슈 30% 정리 | 완료 |  |
| 논문 5편 서술형 요약 | 완료 |  |
| 논문 간 연결 관계 작성 | 완료 |  |
| Research Track 5요소 작성 | 완료 | 연구문제, 위협모형, 평가방법, 재현성, 한계 |
| 실험 outputs 파일 존재 확인 | 완료 | 실험 보고서 기준 세 파일 존재로 기록 |
| 실험 결과와 보고서 수치 일치 | 완료 | 실험 보고서 수치 기준 반영 |
| 그래프 수치 확인 | 완료 | accuracy/F1 series 기준 표와 일치 |
| P04 논문 지정 여부 검증 | 확인 필요 | arXiv P04와 강의계획서 IEEE 논문 동일 여부 미확정 |
| AI 활용 고지 작성 | 완료 |  |
| DOCX/PDF 제출본 생성 | 필요 | `07_week_submission/exports/` 권장 |
| 최종 사람이 검토할 항목 표시 | 완료 | P04, 참고문헌, Word/PDF 렌더링 |

---

## 12. 참고문헌 검증표

| 번호 | 참고문헌 | DOI/URL | 검증 상태 | 비고 |
|---:|---|---|---|---|
| [1] | Yann LeCun, Yoshua Bengio, Geoffrey Hinton, “Deep learning,” Nature, 2015 | https://doi.org/10.1038/nature14539 | 확인 | Nature 페이지와 로컬 PDF 제목 확인 |
| [2] | Rob Ashmore, Radu Calinescu, Colin Paterson, “Assuring the Machine Learning Lifecycle,” ACM CSUR, 2021 | https://doi.org/10.1145/3453444 | 부분 확인 | 로컬 accepted version DOI 확인, 출판사 랜딩 재확인 필요 |
| [3] | Anna L. Buczak, Erhan Guven, “A Survey of Data Mining and Machine Learning Methods for Cyber Security Intrusion Detection,” IEEE COMST, 2016 | https://doi.org/10.1109/COMST.2015.2494502 | 확인 | 로컬 PDF 메타데이터와 첫 페이지 DOI 확인 |
| [4] | Yulong Wang et al., “Adversarial Attacks and Defenses in Machine Learning-Powered Networks: A Contemporary Survey,” arXiv, 2023 | https://doi.org/10.48550/arXiv.2303.06302 | arXiv 확인, 강의계획서 지정 논문 동일 여부 확인 필요 | IEEE COMST 25(4) 2245-2298 정보와 동일 여부 미확정 |
| [5] | Maria Rigaki, Sebastian Garcia, “A Survey of Privacy Attacks in Machine Learning,” ACM CSUR, 2023 | https://doi.org/10.1145/3624010 | 부분 확인 | 로컬 arXiv v3/ACM 양식 PDF 확인, 출판사 랜딩 재확인 필요 |

---

## 13. 부록 A. KCI 논문 형식 전환 아이디어

### A.1 제목 후보

| 번호 | 국문 제목 후보 | 영문 제목 후보 | 대상 시스템 | 보안 위협 | 연구방법 | 예상 기여 |
|---:|---|---|---|---|---|---|
| 1 | ML 생명주기 기반 AI 보안 평가 프레임워크 연구 | A Study on an AI Security Evaluation Framework Based on the ML Lifecycle | ML/딥러닝 시스템 | 보안 평가 누락, 재현성 실패 | 문헌분석 + 체크리스트 | 생명주기 기반 평가 프레임 |
| 2 | 인공지능 보안 평가를 위한 성능·강건성·프라이버시·재현성 통합 체크리스트 연구 | An Integrated Checklist for AI Security Evaluation: Performance, Robustness, Privacy, and Reproducibility | AI 보안 시스템 | 대적 공격, 프라이버시 누출 | 문헌 매트릭스 + toy evaluation | 통합 평가 체크리스트 |
| 3 | 딥러닝 기반 보안 시스템의 생명주기 보증과 평가 지표 연구 | Lifecycle Assurance and Evaluation Metrics for Deep Learning-Based Security Systems | 딥러닝 보안 응용 | 데이터·모델·운영 리스크 | 위협모형 + 평가 프로토콜 | 보안 평가 지표 체계 |

추천 최종 제목은 “ML 생명주기 기반 AI 보안 평가 프레임워크 연구”이다. 국문초록은 딥러닝 기반 AI 시스템의 보안성을 단일 정확도가 아니라 ML 생명주기 관점에서 평가하는 프레임워크를 제안한다는 내용으로 구성한다.

### A.2 연구문제

- RQ1. ML 생명주기 각 단계에서 AI 보안 평가를 위해 필요한 최소 증거는 무엇인가?
- RQ2. clean performance, robust performance, privacy leakage, reproducibility evidence를 통합한 평가 체크리스트는 어떻게 구성할 수 있는가?
- RQ3. synthetic toy evaluation은 실제 AI 보안 평가 프레임워크를 설명하는 데 어떤 장점과 한계를 가지는가?

---

## 14. 부록 B. SCI 논문 형식 전환 아이디어

SCI 제목 후보는 “A Lifecycle-Based Evaluation Framework for AI Security: Integrating Clean Performance, Robustness, Privacy Leakage, and Reproducibility Evidence”이다.

Structured abstract는 Background, Problem, Method, Results, Contribution, Implications로 구성한다. 결과 문장은 W01 toy evaluation이 label noise와 feature perturbation 조건에서 clean baseline 대비 성능 저하를 보였다는 수준으로 제한하며, 실제 운영망 보안성으로 일반화하지 않는다.

| 연구축 | 대표 논문 | 역할 |
|---|---|---|
| Deep learning principles | LeCun et al. | 모델·표현학습 원리 |
| ML lifecycle assurance | Ashmore et al. | 생명주기 보증 |
| ML for intrusion detection | Buczak and Guven | 보안 탐지 평가 |
| Adversarial ML | Wang et al. | 강건성 평가. 강의계획서 지정 논문 동일 여부 확인 필요 |
| Privacy attacks | Rigaki and Garcia | 프라이버시 누출 평가 |

---

## 15. 부록 C. 제출 파일 위치와 변환 권장

| 파일 | 설명 |
|---|---|
| `07_week_submission/w01_submission_report.md` | 본 제출용 보고서 원본 |
| `07_week_submission/assets/w01_metric_chart.png` | 제출 보고서 그래프 |
| `04_experiment/experiment_report.md` | 실험 근거 보고서 |
| `04_experiment/outputs/` | 실험 결과 근거 파일 위치 |
| `05_ai_worklog/ai_disclosure_draft.md` | AI 활용 고지 근거 |

Word 제출본은 다음 위치에 생성해 관리한다.

```text
03_weekly_reports/w01_deep_learning_ml_security/07_week_submission/exports/w01_submission_report.docx
```

PDF 제출본은 Word에서 최종 육안 검수 후 다음 위치에 저장한다.

```text
03_weekly_reports/w01_deep_learning_ml_security/07_week_submission/exports/w01_submission_report.pdf
```

수식은 GitHub와 Word 변환을 모두 고려하여 Markdown 표 안에 넣지 않고, `$$...$$` block math로 유지한다.
