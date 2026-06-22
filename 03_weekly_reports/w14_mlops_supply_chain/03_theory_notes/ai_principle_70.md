# AI 원리 70% 정리

## 1. 핵심 이론

W14의 AI 원리는 MLOps/DevOps, data/model pipeline, monitoring, drift detection, AIOps, edge deployment, software engineering for deep learning이다. 핵심은 모델 학습 알고리즘 하나가 아니라 `데이터 -> 학습 -> 검증 -> artifact 등록 -> 배포 -> 모니터링 -> 재학습/롤백`으로 이어지는 운영 생명주기다.

MLOps는 ML, software engineering, data engineering, operations를 연결한다. DevOps가 코드 빌드와 배포 자동화를 중심에 둔다면, MLOps는 데이터와 모델이 계속 변한다는 점 때문에 dataset version, feature pipeline, model registry, experiment tracking, drift monitoring, rollback, governance를 추가로 요구한다.

## 2. 핵심 개념표

| 개념 | 정의 | 직관적 설명 | 관련 논문 |
|---|---|---|---|
| MLOps | ML 모델을 반복 가능하고 관측 가능한 운영 시스템으로 만들기 위한 practice와 toolchain | 모델을 "파일"이 아니라 "운영 생명주기"로 관리 | P01 |
| DevOps | 소프트웨어 개발과 운영을 CI/CD, 자동화, 모니터링으로 연결하는 방식 | 코드를 빠르고 안정적으로 배포하는 운영 문화 | P01, P02 |
| ML Lifecycle | 데이터 준비, 학습, 검증, 배포, 모니터링, 재학습의 반복 구조 | 모델이 태어나고 바뀌고 감시되는 과정 | P01, P02 |
| Data Pipeline | 데이터 수집, 전처리, feature 생성, 품질 검증 흐름 | 모델의 입력 원천을 만드는 공정 | P01, P02 |
| Model Pipeline | 학습 코드, hyperparameter, seed, artifact, registry를 관리하는 흐름 | 모델 산출물이 만들어지는 공정 | P01 |
| Drift Monitoring | 운영 중 입력/출력/성능 분포가 변했는지 측정 | 모델이 낯선 환경을 만나고 있는지 보는 계기판 | P01, P03 |
| AIOps | 운영 telemetry에 AI를 적용해 이상탐지, 장애예측, 원인분석, 대응을 보조 | 로그와 metric을 이용한 운영 자동화 | P03 |
| Edge AI | edge device/node 가까이에서 학습 또는 추론을 수행하는 구조 | 데이터가 생기는 곳 근처에서 AI를 돌림 | P04 |
| DL for SE | 소프트웨어공학 task에 딥러닝을 적용하는 연구 영역 | 개발 도구 자체에 AI가 들어감 | P05 |

## 3. 수식 또는 알고리즘

W14 toy 실험에서는 운영 파이프라인의 최소 원리를 다음 절차로 구현했다.

```text
synthetic data 생성
-> dataset hash 계산
-> config hash 계산
-> toy logistic regression 학습
-> model artifact 저장 및 model hash 계산
-> 동일 seed/config 재실행 일관성 확인
-> drifted sample의 평균 표준화 이동량 계산
-> audit log와 artifact inventory 저장
```

Drift score는 feature별 평균 이동량을 기준 분포의 표준편차로 나눈 뒤 평균했다.

```text
drift_score = mean_j( abs(mean_current_j - mean_reference_j) / std_reference_j )
```

이번 실행에서는 drift score가 0.307626으로 threshold 0.25를 넘어 `drift_detected=true`가 되었다.

## 4. 초보자용 설명

연구실에서는 모델 accuracy만 적어도 실험이 끝난 것처럼 보일 수 있다. 운영환경에서는 다르다. 어떤 데이터로 학습했는지, config와 seed가 무엇인지, 모델 파일이 바뀌지 않았는지, 배포 뒤 입력 분포가 변했는지, 문제가 생겼을 때 로그로 추적할 수 있는지가 모두 필요하다.

## 5. 보안 연구와의 연결

MLOps 원리는 보안통제로 바로 바뀐다. 데이터 버전관리는 데이터 오염 탐지의 기준점이고, model hash는 artifact 변조 탐지의 기준점이며, drift monitoring은 운영 중 성능·안전성 변화를 감지하는 장치다. Audit coverage와 artifact inventory는 사고대응과 책임추적을 위한 최소 증거다.
