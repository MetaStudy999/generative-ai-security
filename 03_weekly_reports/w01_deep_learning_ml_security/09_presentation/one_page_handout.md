# W01 발표 1페이지 요약

## 주제

딥러닝 패러다임 & ML 보안 분류학

## 핵심 주장

딥러닝 모델은 단순한 정확도 모델이 아니라 데이터, 학습, 검증, 배포, 모니터링이 연결된 ML 시스템이다. 따라서 보안성은 clean performance, robust performance, privacy leakage, reproducibility evidence를 분리해 평가해야 한다.

## 논문 5편의 역할

| 논문 | 역할 |
|---|---|
| P01 Deep learning | 표현학습, 역전파, 일반화 원리 |
| P02 Assuring the ML Lifecycle | ML 생명주기 보증과 재현성 증거 |
| P03 ML for Cyber Security IDS | 오탐, 미탐, 보안 탐지 지표 |
| P04 Adversarial Attacks and Defenses | 대적 공격과 robust 평가 |
| P05 Privacy Attacks in ML | membership inference, model inversion, leakage risk |

## 평가 프레임

| 평가축 | 질문 |
|---|---|
| Clean performance | 정상 조건에서 잘 맞는가 |
| Robust performance | 공격 또는 교란 조건에서도 유지되는가 |
| Privacy leakage | 데이터 포함 여부나 민감 정보가 새는가 |
| Reproducibility | 같은 결과를 다시 만들 수 있는가 |

## 실습 결과

| 조건 | Accuracy | F1 |
|---|---:|---:|
| Clean baseline | 0.869444 | 0.869806 |
| Label-noise training | 0.838889 | 0.841530 |
| Toy feature perturbation | 0.844444 | 0.843575 |

## 해석

정상 조건의 accuracy만으로는 라벨 품질 저하, 입력 교란, privacy risk를 설명할 수 없다. W01 실습은 실제 공격 실험이 아니라 synthetic data 기반의 안전한 평가축 예시다.

## 기말논문 연결

기말논문 후보 주제는 “ML 생명주기 기반 AI 보안 평가 프레임워크”이다. W01은 이후 주차의 공격과 방어를 데이터 관리, 학습, 검증, 배포·운영 단계에 매핑하는 기준을 제공한다.

<!-- formula-visual-handout:start -->
## 수식·그래프·그림 보강 요약

| 항목 | 반영 내용 |
|---|---|
| 핵심 수식 | Empirical Risk와 Generalization Gap, Robust Accuracy와 ASR |
| 그래프 | `assets/charts/w01_metrics_chart.png` (`metrics_summary.csv` 기반) |
| 다이어그램 | `assets/diagrams/w01_pipeline_diagram.svg` (ML lifecycle threat model) |
| 기호 정의 | 통합보고서와 발표 슬라이드의 수식 블록에 포함 |
| 주의사항 | 원문 논문별 절·쪽·그림 번호와 formal guarantee 여부는 확인 필요. |
<!-- formula-visual-handout:end -->
