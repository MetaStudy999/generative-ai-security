# W02 대규모 최적화 & 데이터 오염 위협 통합보고서

## 0. 메타정보

| 항목 | 내용 |
|---|---|
| 주차 | W02 |
| 주제 | 대규모 최적화 & 데이터 오염 위협 |
| AI 원리 | 대규모 최적화, SGD, 일반화, 효율적 학습, 모델 압축/경량화 |
| 보안 이슈 | 데이터 오염, label-flipping, poisoning, backdoor |
| 문서 상태 | 제출용 최종본 |
| 실험 상태 | Docker 실행 완료, 정량 결과 `04_experiment/outputs/` 기록 완료 |

## 1. 한 문장 요약

W02는 “학습은 데이터로 움직이고, 데이터가 오염되면 최적화 경로와 최종 모델의 신뢰성이 바뀐다”는 관점에서 대규모 최적화 원리와 poisoning/backdoor 평가 지표를 연결한다.

## 2. AI 원리 70% 정리

대규모 머신러닝은 많은 데이터와 고차원 파라미터에서 손실함수를 최소화하는 문제다. 전체 데이터의 gradient를 매번 계산하는 방식은 비용이 크기 때문에 실제 학습에서는 stochastic gradient descent와 mini-batch update가 널리 사용된다. 이 방식은 확장성이 높지만 샘플링 노이즈와 데이터 품질에 민감하다.

이 점이 데이터 오염 위협과 직접 연결된다. 학습 데이터 일부가 조작되면 empirical risk와 gradient 추정이 달라지고, 모델의 decision boundary가 공격자에게 유리한 방향으로 이동할 수 있다. 따라서 poisoning은 테스트 시점 공격이 아니라 학습 목적함수를 바꾸는 훈련 단계 공격으로 이해해야 한다.

효율적 딥러닝은 모델을 작고 빠르게 만들기 위한 압축, pruning, quantization, distillation, efficient architecture, efficient training을 포함한다. 효율화는 배포 가능성을 높이지만, 보안 평가에서는 방어 비용, 탐지 지연시간, 재학습 가능성, backdoor 잔존 여부도 함께 기록해야 한다.

| 개념 | W02 의미 | 관련 문헌 |
|---|---|---|
| Large-scale optimization | 대규모 데이터에서 학습 가능한 최적화 절차 | P01 |
| Stochastic gradient | 일부 데이터로 gradient를 추정하는 확장 가능한 학습 방식 | P01 |
| Generalization | 정상 test 성능과 공격 조건 성능을 구분해야 하는 이유 | P01 |
| Model efficiency | 정확도와 비용, 속도, 메모리를 함께 보는 관점 | P02 |
| Compression/lightweighting | 방어 비용과 backdoor 제거 가능성에 영향을 주는 효율화 기법 | P02 |

### 2.1 핵심 수식 또는 알고리즘 쉬운 설명

아래 수식은 원문 수식의 직접 인용이 아니라, 각 논문의 핵심 개념을 보고서에서 설명하기 위한 대표 수식과 지표다. 최종 제출본에서 원문 수식으로 인용할 경우 논문 원문 쪽/절 번호를 추가 확인한다.

| ID | 핵심 수식/알고리즘 | 쉬운 설명 | 보안 평가 연결 |
|---|---|---|---|
| P01 | $\min_\theta \frac{1}{n}\sum_i L(f_\theta(x_i),y_i)$, $\theta_{t+1}=\theta_t-\eta\nabla L_B(\theta_t)$ | 학습은 평균 손실을 줄이는 일이고, SGD는 일부 샘플 묶음으로 업데이트 방향을 추정한다. | 데이터 오염이 gradient를 바꾸는 원리 |
| P02 | $CR=Size_{base}/Size_{compressed}$ | 경량화는 모델 크기나 비용을 줄이지만 보안 탐지 능력도 함께 확인해야 한다. | 효율성-보안 trade-off |
| P03 | $\max_{D_p} L_{val}(\theta^*(D\cup D_p))$ | poisoning은 오염 데이터 $D_p$를 넣어 학습된 모델이 검증에서 실패하게 만드는 훈련 단계 공격이다. | poisoning threat model |
| P04 | $Impact=Perf_{clean}-Perf_{poisoned}$ | 데이터 오염의 피해는 정상 학습 대비 성능이 얼마나 떨어졌는지로 먼저 볼 수 있다. | accuracy drop, provenance |
| P05 | $ASR=N_{target}/N_{trigger}$ | backdoor는 정상 성능이 좋아도 trigger 입력에서 목표 오분류가 많으면 실패다. | clean accuracy와 ASR 분리 |

## 3. 보안 이슈 30% 정리

데이터 오염 공격은 학습 데이터나 라벨을 조작해 모델 학습 결과를 바꾸는 공격이다. Label-flipping은 라벨을 다른 클래스로 바꾸는 비교적 단순한 poisoning이며, 전체 성능 저하나 특정 클래스 오류를 만들 수 있다. Backdoor는 정상 입력에서는 모델이 잘 동작하지만 특정 trigger가 포함된 입력에서는 공격자 목표로 오분류되도록 만드는 조건부 무결성 공격이다.

W02에서 가장 중요한 지표 분리는 clean accuracy와 ASR이다. Clean accuracy는 정상 테스트셋에서의 성능이고, ASR은 trigger 입력에서 공격자 목표 예측이 발생한 비율이다. 정상 성능이 높아도 ASR이 높다면 보안적으로 실패한 모델일 수 있다.

| 보안 속성 | W02 위협 | 평가 지표 |
|---|---|---|
| Integrity | label-flipping, backdoor | accuracy drop, ASR |
| Availability | 모델 전체 성능 저하 | clean accuracy, macro F1 |
| Safety | trigger 조건부 오분류 | ASR, target error |
| Accountability | 오염 출처 추적 실패 | provenance, 로그, config |
| Reproducibility | 보안 주장 검증 불가 | seed, Docker, 실행 로그 |

## 4. 논문 5편 요약

| ID | 논문 | 핵심 기여 | W02 활용 |
|---|---|---|---|
| P01 | Optimization Methods for Large-Scale Machine Learning | 대규모 최적화, SGD, noise reduction, second-order 방법 정리 | 데이터 오염이 목적함수와 gradient를 바꾼다는 원리 설명 |
| P02 | Efficient Deep Learning | 모델 효율성, 압축, 비용-속도-품질 trade-off 정리 | 방어 비용과 배포 가능성을 평가표에 포함 |
| P03 | A Comprehensive Survey on Poisoning Attacks and Countermeasures in Machine Learning | poisoning 공격과 대응책 taxonomy | 위협모형과 poisoning 평가 지표 근거 |
| P04 | Wild Patterns Reloaded | training data poisoning threat model과 방어 체계화 | 데이터 생명주기 기반 방어 체크리스트 |
| P05 | A survey of backdoor attacks and defences | DNN부터 LLM까지 backdoor 공격/탐지/제거 정리 | clean accuracy와 ASR 동시 평가 근거 |

## 5. 논문 5편 비교

P01-P02는 AI 원리와 운영 제약을 제공하고, P03-P05는 학습 데이터 오염과 backdoor 위협을 제공한다. W02의 핵심은 두 영역을 분리해서 읽지 않는 것이다. 최적화는 데이터로부터 업데이트 방향을 얻고, poisoning은 바로 그 데이터와 라벨을 조작한다. 효율화는 모델을 운영 가능하게 하지만 방어 비용과 탐지 가능성에 영향을 준다.

## 6. Research Track

### 6.1 연구문제

RQ1. 데이터 오염률이 증가할 때 clean accuracy와 macro F1은 어떻게 변하는가?

RQ2. Backdoor 조건에서 clean accuracy를 유지하면서 ASR이 높아질 수 있는가?

RQ3. Poisoning/backdoor 방어평가에는 clean accuracy, ASR, stealthiness, detection rate, cost 중 어떤 지표 조합이 필요한가?

### 6.2 위협모형

| 항목 | 내용 |
|---|---|
| 대상 시스템 | 지도학습 기반 분류 모델 |
| 보호 자산 | 학습 데이터, 라벨, 모델 파라미터, 검증셋, 예측 결과, 학습 로그 |
| 공격자 | 데이터 제공자, 악의적 라벨러, 내부 데이터 파이프라인 접근자 |
| 공격자의 지식 | black-box, gray-box, white-box |
| 공격자의 능력 | 일부 학습데이터 라벨 조작, trigger 삽입, 오염 데이터 업로드 |
| 공격 성공 조건 | clean accuracy 저하 또는 trigger 조건부 목표 오분류 |
| 방어자 가정 | 데이터 검증, 실험 로그 보존, clean/trigger 평가셋 구성 가능 |
| 제외 범위 | 실제 운영 시스템 침해, 개인정보 사용, 무단 API 질의 |

### 6.3 평가방법

| 평가 항목 | 지표 | 측정 방법 |
|---|---|---|
| Clean performance | accuracy, macro F1 | 정상 테스트셋 평가 |
| Poisoning impact | accuracy drop | 오염률별 모델 재학습 후 비교 |
| Backdoor effect | ASR | trigger 테스트셋의 목표 라벨 예측률 |
| Stealthiness | clean accuracy 유지율 | clean 성능과 ASR 동시 비교 |
| Reproducibility | seed, config, logs | Docker와 출력 파일 보존 |
| Efficiency | train time, model size, inference cost | 실행 로그와 모델/환경 정보 기록 |

### 6.4 재현성

실험 폴더에는 `Dockerfile`, `pyproject.toml`, `configs/config.yaml`, `src/run_experiment.py`를 배치했다. Docker에서 실행해 `outputs/metrics_summary.csv`, `outputs/results.json`, `outputs/run_log.md`를 생성했고, 호스트 Python에는 `scikit-learn`이나 uv를 설치하지 않았다.

### 6.5 한계와 오픈문제

Digits toy dataset은 실제 대규모 모델의 데이터 파이프라인을 대표하지 않는다. Label-flipping은 이해하기 쉽지만 clean-label poisoning의 은닉성을 충분히 설명하지 못한다. Backdoor trigger도 안전한 toy 패턴으로 제한했으므로 실제 공격 성능으로 일반화할 수 없다. LLM backdoor와 데이터 공급망 poisoning은 최신 문헌 보강이 필요하다.

## 7. 실습 요약

실습은 scikit-learn digits 데이터셋 기반으로 설계했다. Clean baseline은 표준화와 logistic regression을 사용한다. Label-flip 조건은 학습 라벨의 5%, 10%, 20%를 다음 클래스로 바꾼 뒤 성능 변화를 비교한다. Toy backdoor 조건은 학습 샘플 일부에 하단 픽셀 trigger를 넣고 target label을 부여한 뒤, 정상 테스트셋 성능과 trigger 테스트셋 ASR을 분리해 측정한다.

| 조건 | Poisoning Rate | Clean Accuracy | Macro F1 | ASR | 상태 |
|---|---:|---:|---:|---:|---|
| Clean baseline | 0% | 0.981481 | 0.981443 | 해당 없음 | 실행 완료 |
| Label-flip | 5% | 0.918519 | 0.918457 | 해당 없음 | 실행 완료 |
| Label-flip | 10% | 0.877778 | 0.877582 | 해당 없음 | 실행 완료 |
| Label-flip | 20% | 0.818519 | 0.818134 | 해당 없음 | 실행 완료 |
| Toy backdoor | 5% | 0.970370 | 0.970359 | 0.987654 | 실행 완료 |

## 8. AI 활용 기록 요약

Codex를 사용해 폴더 상태 점검, 문헌 요약 보강, 이론노트 작성, 실험 코드 작성, Docker 실행 검증, 보고서 및 발표자료 작성을 수행했다. DOI/URL은 확인 가능한 근거가 있는 경우에만 기록했고, 정량값은 Docker 실행 로그 기준으로만 반영했다. 상세 기록은 `05_ai_worklog/`에 보존했다.

## 9. 토론 질문

1. Clean accuracy가 높고 ASR도 높은 모델은 어떤 의미에서 “좋은 모델”이 아닌가?
2. Label-flipping처럼 단순한 오염과 clean-label poisoning처럼 은닉적인 오염은 같은 지표로 평가할 수 있는가?
3. 모델 압축이나 pruning은 backdoor 방어에 도움이 되는가, 아니면 trigger를 더 숨길 수 있는가?
4. 제출 가능한 AI 보안 실습에서 실제 공격 재현과 안전한 toy simulation의 경계는 어디에 두어야 하는가?

## 10. 기말 논문 연결

W02는 기말 논문의 관련연구, 위협모형, 평가방법, 보안적 함의 장에 직접 연결된다. 발전 가능한 주제는 “학습 데이터 오염과 backdoor 평가를 위한 다중지표 프레임워크”이다. 예상 기여는 오염률, clean accuracy, ASR, stealthiness, detection rate, efficiency cost, reproducibility evidence를 한 평가표에서 관리하는 것이다.

## 11. 참고문헌 검증표

| ID | 검증 상태 | 비고 |
|---|---|---|
| P01 | DOI 기록 | `10.1137/16M1080173` |
| P02 | arXiv URL 기록 | ACM DOI 최종 확인 권장 |
| P03 | DOI 확인 | `10.1145/3551636` |
| P04 | arXiv URL 기록 | 로컬 PDF 제목 우선 |
| P05 | DOI 확인 | `10.1016/j.jnlest.2025.100326` |

## 12. 자기 점검

| 항목 | 상태 |
|---|---|
| 논문 5편 요약 | 완료 |
| 논문 비교표 | 완료 |
| AI 원리 70% | 완료 |
| 보안 이슈 30% | 완료 |
| Research Track | 완료 |
| Docker 실습 코드 | 완료 |
| 실험 정량 결과 | 완료 |
| AI 활용 고지 | 완료 |
| 발표자료 | 완료 |
