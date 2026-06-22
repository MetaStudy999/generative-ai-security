# W11 차등프라이버시(DP) & 멤버십 추론 공격·방어 통합보고서

## 0. 메타정보

| 항목 | 내용 |
|---|---|
| 주차 | W11 |
| 주제 | 차등프라이버시(DP) & 멤버십 추론 공격·방어 |
| AI 원리 | Differential Privacy, privacy budget, DP-SGD, privacy accounting |
| 보안 이슈 | Membership inference, privacy leakage, utility-privacy trade-off |
| 작성일 | 2026-06-22 |
| 문서 상태 | 제출용 최종본 |
| 실험 근거 | `04_experiment/outputs/run_log.md` |

## 1. 한 문장 요약

W11의 핵심은 DP 보장을 “적용했다”는 선언이 아니라 accuracy, MI attack accuracy, leakage, privacy budget/accounting, utility drop, 재현성 로그로 함께 검증해야 한다는 점이다.

## 2. AI 원리 70% 정리

DP는 인접 데이터셋의 출력 분포 차이를 제한해 특정 레코드의 포함 여부가 출력에서 드러나지 않도록 하는 privacy 원리다. 딥러닝에서는 DP-SGD가 대표 구현이며, gradient clipping과 noise injection을 통해 개별 sample이 update에 미치는 영향을 제한한다.

| 개념 | W11 해석 |
|---|---|
| Privacy budget | epsilon/delta로 표현되는 privacy loss 조건 |
| DP-SGD | clipping, noise, accountant가 함께 있어야 해석 가능 |
| Privacy accounting | 여러 step의 privacy loss를 누적 추적 |
| Utility-privacy trade-off | noise가 privacy risk를 낮출 수 있지만 성능과 안정성을 흔들 수 있음 |

P01은 DP misuse와 reporting 책임을, P02는 중앙집중형 DP-DL의 평가·감사 흐름을, P03은 deep learning/FL 환경에서 보호 대상과 적용 위치가 달라짐을 보여준다.

### 2.1 핵심 수식 또는 알고리즘 쉬운 설명

아래 수식은 원문 수식의 직접 인용이 아니라, 각 논문의 핵심 개념을 보고서에서 설명하기 위한 대표 수식과 지표다. 최종 제출본에서 원문 수식으로 인용할 경우 논문 원문 쪽/절 번호를 추가 확인한다.

| ID | 핵심 수식/알고리즘 | 쉬운 설명 | 보안 평가 연결 |
|---|---|---|---|
| P01 | $Pr[M(D)\in S]\le e^\epsilon Pr[M(D')\in S]+\delta$ | DP는 한 사람의 데이터가 들어가도 결과 분포가 크게 바뀌지 않게 제한한다. | privacy claim 검증 |
| P02 | $\bar g_i=g_i/\max(1,\lVert g_i\rVert_2/C)$, $\tilde g=\frac{1}{B}(\sum_i\bar g_i+\mathcal N(0,\sigma^2C^2I))$ | DP-SGD는 각 샘플 gradient를 자르고 노이즈를 더해 개인 영향력을 줄인다. | DP-SGD 원리 |
| P03 | $\epsilon_{total}\approx \sum_t \epsilon_t$ | 여러 학습 step에서 privacy loss가 누적되므로 accountant가 필요하다. | privacy accounting |
| P04 | $MIAdv=TPR-FPR$ | membership inference 공격은 member를 잘 맞히면서 non-member를 덜 오인할수록 강하다. | MI risk |
| P05 | $Tradeoff=(Utility,\ PrivacyRisk)$ | 방어는 하나의 점수가 아니라 성능과 privacy risk를 함께 보고해야 한다. | utility-privacy trade-off |

## 3. 보안 이슈 30% 정리

Membership inference는 특정 레코드가 학습 데이터였는지 추론하는 privacy attack이다. 보호 자산은 데이터 원문뿐 아니라 membership information, confidence score, loss 신호, 평가 로그까지 확장된다.

| 관점 | 관련 위협 | 평가 연결 |
|---|---|---|
| Confidentiality | membership inference, training data leakage | MI Attack Accuracy |
| Privacy | individual record exposure | Privacy Leakage Score |
| Integrity | 잘못된 DP claim, accountant 누락 | reference/config 검증 |
| Availability | 과도한 noise로 인한 utility 저하 | Accuracy, Utility Drop |
| Accountability | DOI/PDF 불일치, 실행 로그 부재 | `01_papers/`, `outputs/` |

## 4. 논문 5편 요약

| ID | 문헌 | 핵심 역할 | 검증 상태 |
|---|---|---|---|
| P01 | A Critical Review on the Use (and Misuse) of Differential Privacy in Machine Learning | DP misuse, epsilon 해석, reporting 책임 | arXiv 확인, ACM DOI 공식 확인 필요 |
| P02 | Recent Advances of Differential Privacy in Centralized Deep Learning | DP-DL auditing, privacy-utility 개선, application 분류 | arXiv 확인, ACM 최종본 대조 필요 |
| P03 | Differential Privacy in Deep Learning: A Literature Survey | deep learning DP 문헌축 | DOI 후보 확인, 로컬 PDF는 Fu et al. FL 대체 문헌 |
| P04 | Membership Inference Attacks on Machine Learning | MI attack/defense taxonomy | arXiv 확인, ACM DOI 공식 확인 필요 |
| P05 | Defenses to Membership Inference Attacks | MI defense taxonomy와 trade-off | DOI 후보 확인, 로컬 PDF는 Bai et al. FL-MIA 대체 문헌 |

## 5. 논문 5편 비교

P01/P02/P03은 DP 원리와 적용 위치를, P04/P05는 MI 공격과 방어 평가를 담당한다. 기말 논문에서는 이 둘을 분리하지 않고 “privacy claim 검증 프로토콜”로 묶는다.

| 비교축 | DP 문헌 | MI 문헌 | 통합 관점 |
|---|---|---|---|
| 보호 대상 | 개별 sample 영향 제한 | membership information 보호 | record-level privacy |
| 주요 지표 | epsilon/delta, accounting, utility | MI accuracy, confidence gap | utility + leakage 동시 보고 |
| 실패 조건 | 큰 epsilon, accountant 누락, 오용 | overfitting, confidence 노출 | 평가표와 로그 부재 |

## 6. Research Track

### 6.1 연구문제

RQ1. DP-like noise 또는 DP-SGD 설정 변화는 모델 accuracy와 membership inference risk 사이에 어떤 trade-off를 만드는가?

RQ2. MI 위험은 overfitting, confidence score, train/test 분포 차이에 따라 어떻게 달라지는가?

RQ3. AI 보안 연구에서 DP를 주장할 때 privacy accounting, utility, attack evaluation, reproducibility log를 어떤 최소 항목으로 보고해야 하는가?

### 6.2 위협모형

| 항목 | 내용 |
|---|---|
| 대상 시스템 | 개인정보가 포함될 수 있는 ML/DL 학습 시스템 |
| 보호 자산 | 학습 데이터 포함 여부, confidence score, model output, evaluation log |
| 공격자 | 외부 질의자, 모델 사용자, API 접근자, 내부 평가자 |
| 공격자의 지식 | black-box output 관찰부터 gray-box log 접근까지 구분 |
| 공격 경로 | 모델 API, 예측 확률, 학습 결과, 평가 로그 |
| 방어자 가정 | DP-SGD/DP-like noise, output restriction, calibration, accounting 가능 |
| 제외 범위 | 실제 개인정보, 실제 개인 대상 추론, 운영 모델/API 무단 질의 |

### 6.3 평가방법

| 평가 항목 | 지표 | 측정 방법 |
|---|---|---|
| Utility | Accuracy, Utility Drop | baseline 대비 test accuracy 비교 |
| Membership Risk | MI Attack Accuracy | synthetic member/non-member confidence threshold 비교 |
| Leakage | Privacy Leakage Score | mean member confidence와 non-member confidence 차이 |
| Privacy Budget | epsilon/delta 또는 epsilon proxy | accountant 또는 실습용 proxy 기록 |
| Reproducibility | seed/config/CSV/JSON/run log | `outputs/` 보존 |

### 6.4 재현성

| 항목 | 내용 |
|---|---|
| 실행 명령 | `python3 src/run_experiment.py --config configs/config.yaml` |
| Seed | 42 |
| 데이터 | synthetic binary classification, no personal data |
| 스크립트 | `04_experiment/src/run_experiment.py` |
| 산출물 | `metrics_summary.csv`, `results.json`, `run_log.md` |

### 6.5 한계와 오픈문제

- `epsilon_proxy`는 정식 privacy accountant 산출값이 아니다.
- P03/P05는 로컬 PDF가 지정 논문과 달라 원문 확보가 필요하다.
- toy 실험 결과는 실제 개인정보 보호 수준이나 실제 운영 모델의 MI 위험으로 일반화하지 않는다.
- 향후에는 DP-SGD 라이브러리와 formal accounting을 연결해야 한다.

## 7. 실습 요약

| 조건 | Accuracy | MI Attack Accuracy | Epsilon Proxy | Utility Drop | Privacy Leakage Score |
|---|---:|---:|---:|---:|---:|
| Non-DP baseline | 0.956250 | 0.515625 | 해당 없음 | 0.000000 | 0.014833 |
| DP-like noise low | 0.956250 | 0.515625 | 8.000000 | 0.000000 | 0.014494 |
| DP-like noise medium | 0.962500 | 0.512500 | 3.000000 | 0.000000 | 0.011769 |
| DP-like noise high | 0.950000 | 0.521875 | 1.000000 | 0.006250 | 0.016482 |

결과는 medium noise에서 leakage proxy가 가장 낮고 high noise에서 utility drop이 발생했다. high noise가 항상 MI risk를 낮춘 것은 아니므로, DP-like noise를 실제 DP 보장으로 오해하지 않아야 한다.

## 8. AI 활용 기록 요약

Codex를 사용해 로컬 파일 점검, W11 문헌/서지 정리, 실험 코드 작성, 실행 로그 생성, 제출용/발표용 문서 보완을 수행했다. 정량값은 `04_experiment/outputs/` 산출물과 일치하는 값만 반영했다.

## 9. 토론 질문

1. DP 보장을 주장할 때 epsilon만 제시하면 충분한가?
2. MI attack accuracy가 낮아도 confidence leakage가 남아 있다면 privacy risk를 어떻게 해석해야 하는가?
3. toy 실험과 실제 DP-SGD 실험 사이의 간극을 기말논문에서 어떻게 설명할 것인가?

## 10. 기말 논문 연결

| 논문 장 | 반영 가능 내용 |
|---|---|
| 서론 | AI 모델 학습에서 privacy protection과 utility trade-off의 필요성 |
| 관련연구 | DP misuse, DP-DL survey, MI attack/defense taxonomy |
| 연구문제 | DP claim 검증을 위한 다중지표 평가 |
| 연구방법 | synthetic toy 평가, threat model, reproducibility protocol |
| 분석/실험 | accuracy, MI attack accuracy, leakage score, utility drop |
| 보안적 함의 | privacy claim accountability와 원문/DOI 검증 |

## 11. 참고문헌 검증표

| ID | 상태 |
|---|---|
| P01 | arXiv 확인, ACM DOI 공식 확인 필요 |
| P02 | arXiv 확인, ACM 최종본/DOI 대조 필요 |
| P03 | DOI 후보 `10.1016/j.neucom.2024.127663`, 로컬 PDF 대체 상태 |
| P04 | arXiv 확인, ACM DOI 공식 확인 필요 |
| P05 | DOI 후보 `10.1145/3620667`, 로컬 PDF 대체 상태 |

상세 표는 `01_papers/doi_check.md`에 둔다.

## 12. 자기 점검

| 항목 | 상태 |
|---|---|
| 논문 5편 요약 | 완료 |
| 논문 비교표 | 완료 |
| AI 원리 70% | 완료 |
| 보안 이슈 30% | 완료 |
| Research Track | 완료 |
| 실험 코드/결과 | 완료 |
| 제출용 보고서 | 완료 |
| 발표자료 | 완료 |
| DOI/원문 확인 | 부분 완료, 최종 공식 대조 필요 |
