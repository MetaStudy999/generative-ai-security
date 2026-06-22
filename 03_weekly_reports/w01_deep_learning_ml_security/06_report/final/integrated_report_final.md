# W01 딥러닝 패러다임 & ML 보안 분류학 통합보고서

## 0. 메타정보

| 항목 | 내용 |
|---|---|
| 주차 | W01 |
| 주제 | 딥러닝 패러다임 & ML 보안 분류학 |
| AI 원리 | 딥러닝 패러다임, 표현학습, 역전파, 학습과 일반화 |
| 보안 이슈 | ML 생명주기 보증, 침입탐지, 대적 ML, 프라이버시 공격 |
| 문서 상태 | 최종본 |

## 1. 한 문장 요약

W01은 딥러닝을 “정확도를 내는 모델”이 아니라 데이터, 학습, 검증, 배포, 모니터링이 연결된 ML 시스템으로 보고, 이 시스템의 보안성을 clean performance, robust performance, privacy leakage, reproducibility evidence로 나누어 평가하는 기준 주차다.

## 2. AI 원리 70% 정리

딥러닝의 핵심은 다층 신경망이 원시 입력에서 계층적 표현을 학습한다는 점이다. P01은 표현학습, 역전파, CNN/RNN의 원리를 통해 모델이 복잡한 데이터 구조를 처리하는 방식을 설명한다. 이 원리는 보안 연구에서도 중요하다. 공격자가 모델 입력이나 데이터 분포를 조작할 때 실제로 흔드는 것은 모델의 내부 표현과 의사결정 경계이기 때문이다.

학습은 손실함수를 최소화하는 파라미터를 찾는 과정이며, 일반화는 학습 데이터 밖에서도 성능이 유지되는지를 뜻한다. 과적합은 단순 성능 저하 문제를 넘어 privacy leakage의 위험 신호가 될 수 있다. 따라서 W01에서는 경험위험, 일반화 격차, 대적 위험을 함께 정리했다.

### 2.1 핵심 수식 또는 알고리즘 쉬운 설명

아래 수식은 원문 수식의 직접 인용이 아니라, 각 논문의 핵심 개념을 보고서에서 설명하기 위한 대표 수식과 지표다. 최종 제출본에서 원문 수식으로 인용할 경우 논문 원문 쪽/절 번호를 추가 확인한다.

| ID | 핵심 수식/알고리즘 | 쉬운 설명 | 보안 평가 연결 |
|---|---|---|---|
| P01 | $h_l=\sigma(W_l h_{l-1}+b_l)$, $\theta \leftarrow \theta-\eta\nabla_\theta L$ | 딥러닝은 층마다 입력을 조금씩 바꾸어 표현을 만들고, 오차가 줄어드는 방향으로 가중치를 고친다. | 표현학습, 역전파, 대적 입력이 내부 표현을 흔드는 이유 |
| P02 | $EC=N_{checked}/N_{required}$ | ML 생명주기 보증은 필요한 증거 중 몇 개를 확인했는지로 관리할 수 있다. | 재현성·보증 evidence chain |
| P03 | $F1=2PR/(P+R)$ | 침입탐지는 정확도만 보면 오탐과 미탐을 놓치므로 precision과 recall을 같이 본다. | 탐지 성능과 보안 데이터 평가 |
| P04 | $\max_{\lVert\delta\rVert\le\epsilon} L(f_\theta(x+\delta),y)$ | 공격자는 사람이 보기엔 작은 변화 $\delta$로 모델 손실을 크게 만들려 한다. | adversarial robustness 평가 |
| P05 | $Adv=P(A=1\mid member)-P(A=1\mid nonmember)$ | 멤버십 공격은 학습에 들어간 데이터와 아닌 데이터를 얼마나 잘 구분하는지로 본다. | privacy leakage 평가축 |

## 3. 보안 이슈 30% 정리

보안 이슈는 ML 생명주기 관점에서 정리했다. P02는 데이터 관리, 모델 학습, 검증, 배포까지 이어지는 보증 증거의 필요성을 보여준다. P03은 침입탐지에서 accuracy만으로 보안성을 설명하기 어렵고 오탐과 미탐을 분리해야 함을 보여준다. P04는 adversarial example과 방어 검증의 한계를, P05는 membership inference와 model inversion 같은 privacy attack의 위험을 제시한다.

CIA 관점으로 보면 confidentiality는 privacy leakage, integrity는 adversarial example과 poisoning, availability는 오탐 폭증과 탐지 실패, accountability는 로그와 재현성 기록의 문제로 연결된다.

## 4. 논문 5편 요약

| ID | 논문 | 핵심 기여 | W01 활용 |
|---|---|---|---|
| P01 | Deep learning | 딥러닝의 표현학습과 역전파 원리 정리 | AI 원리의 배경 |
| P02 | Assuring the Machine Learning Lifecycle | ML 생명주기별 보증 요건과 방법 정리 | 위협모형과 재현성 프레임 |
| P03 | ML Methods for Cyber Security Intrusion Detection | 침입탐지 ML 방법과 평가 지표 분류 | 탐지 지표와 보안 데이터 한계 |
| P04 | Adversarial Attacks and Defenses in ML-Powered Networks | 대적 공격·방어 taxonomy와 방어 한계 정리 | robust 평가 기준 |
| P05 | Privacy Attacks in Machine Learning | privacy attack taxonomy와 threat model 정리 | leakage risk 평가축 |

## 5. 논문 5편 비교

P01은 원리 중심, P02는 생명주기 보증 중심, P03은 보안 탐지 응용 중심, P04는 무결성 공격 중심, P05는 기밀성 공격 중심이다. 다섯 편을 종합하면 W01의 결론은 분명하다. ML 보안 평가는 하나의 모델 성능표가 아니라 공격자 지식, 보호 자산, 방어 가정, 평가 지표, 재현성 증거를 함께 기록하는 구조여야 한다.

## 6. Research Track

### 6.1 연구문제

RQ1. ML 생명주기 각 단계에서 보안 보증을 위해 최소한으로 남겨야 할 증거는 무엇인가?

RQ2. Clean performance, robust performance, privacy leakage, reproducibility를 함께 볼 때 어떤 지표 조합이 보안 평가에 적합한가?

RQ3. Survey 기반 분류체계를 안전한 toy evaluation 또는 문헌 매트릭스로 연결할 때 어떤 한계가 생기는가?

### 6.2 위협모형

대상 시스템은 딥러닝 또는 일반 ML 모델을 포함한 보안 응용 시스템이다. 보호 자산은 학습 데이터, 모델 파라미터, 입력 데이터, 출력 정보, 평가셋, 운영 로그다. 공격자는 white-box, gray-box, black-box, data contributor, operator로 구분한다.

### 6.3 평가방법

평가 항목은 clean performance, detection quality, attack impact, robust performance, privacy/leakage, lifecycle assurance, human review로 둔다. 특히 clean accuracy와 robust accuracy를 분리하고, 프라이버시 위험은 별도 leakage risk로 기록한다.

### 6.4 재현성

재현성을 위해 DOI/URL 검증표, 로컬 PDF 목록, Dockerfile, pyproject.toml/uv sync, config, seed, 실행 소스, 결과 파일을 보존한다. W01 실습 결과는 `04_experiment/outputs/`에 `metrics_summary.csv`, `results.json`, `run_log.md`로 저장했다.

### 6.5 한계와 오픈문제

W01의 실험은 synthetic data 기반 toy evaluation이므로 실제 운영망 보안성을 직접 대표하지 않는다. Survey 문헌의 taxonomy를 실제 시스템 보안성으로 일반화하려면 데이터셋, 공격자 가정, 운영 환경 차이를 추가로 검토해야 한다.

## 7. 실습 요약

실습은 synthetic data 기반 safe toy evaluation으로 작성하고 실행했다. clean baseline, label-noise training, toy feature perturbation, privacy-safe audit, reproducibility check를 기록했다. 실제 개인정보, 실제 서비스 침해, 무단 API 질의, 악성코드 실행은 제외했다.

| 조건 | Accuracy | Precision | Recall | F1 | 메모 |
|---|---:|---:|---:|---:|---|
| Clean baseline | 0.869444 | 0.867403 | 0.872222 | 0.869806 | 정상 synthetic test split |
| Label-noise training | 0.838889 | 0.827957 | 0.855556 | 0.841530 | training label 126개 flip |
| Toy feature perturbation | 0.844444 | 0.848315 | 0.838889 | 0.843575 | Gaussian feature noise |

## 8. AI 활용 기록 요약

Codex를 사용해 W01 산출물의 구조화, 논문별 요약 보강, DOI/URL 검증표 정리, 실습 소스 작성, 통합보고서 문장화를 수행했다. 정량값은 `src/run_experiment.py` 실행으로 생성했고, 최종 제출 전 원문 세부 수치와 참고문헌 양식은 사람이 확인해야 한다.

## 9. 토론 질문

1. ML 보안 평가에서 clean accuracy와 robust accuracy 중 어느 쪽을 먼저 보고해야 하는가?
2. synthetic toy evaluation 결과를 실제 보안성 주장으로 과도하게 일반화하지 않으려면 어떤 표현이 필요한가?
3. 생명주기 보증 증거 중 최종 제출물에 반드시 포함해야 할 최소 항목은 무엇인가?

## 10. 기말 논문 연결

W01은 기말 논문의 상위 프레임을 제공한다. 핵심 주제 후보는 “ML 생명주기 기반 AI 보안 평가 프레임워크”이며, 각 후속 주차의 공격과 방어를 데이터 관리, 모델 학습, 검증, 배포·운영 단계에 매핑할 수 있다.

## 11. 참고문헌 검증표

참고문헌 DOI/URL은 `01_papers/doi_check.md`에 정리했다. P04는 arXiv DOI 기준으로 정리했고, P05는 ACM CSUR 관련 DOI를 함께 반영했다.

## 12. 자기 점검

| 항목 | 상태 |
|---|---|
| 논문 5편 요약 | 완료 |
| 논문 비교표 | 완료 |
| AI 원리 70% | 완료 |
| 보안 이슈 30% | 완료 |
| Research Track | 완료 |
| 실험 소스 및 실행 | 완료 |
| 정량 실험값 조작 방지 | 완료, 실행 로그 기반으로 기록 |
| DOI/URL 검증 | 완료, 확인 가능한 범위 반영 |
| AI 사용 고지 | 완료 |
