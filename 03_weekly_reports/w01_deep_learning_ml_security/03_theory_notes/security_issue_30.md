# W01 보안 이슈 30% 정리

## 0. 문서 목적

이 문서는 W01의 보안 이슈 30%를 정리한다. 목표는 딥러닝 원리를 바로 공격 절차로 바꾸는 것이 아니라, **ML 시스템이 어떤 자산을 갖고, 어떤 방식으로 실패하며, 어떤 지표로 평가해야 하는지**를 분류하는 것이다.

---

## 1. 주요 보안 이슈

| 이슈 | 핵심 질문 | 관련 논문 | 대표 지표 |
|---|---|---|---|
| ML 생명주기 보증 | 데이터부터 배포까지 어떤 증거가 있어야 시스템을 신뢰할 수 있는가 | P02 | evidence coverage, traceability |
| 침입탐지와 ML | 보안 탐지 모델의 성능을 어떤 지표로 판단해야 하는가 | P03 | precision, recall, F1, FAR |
| 대적 머신러닝 | 공격자가 입력을 조작할 때 모델 예측은 얼마나 안정적인가 | P04 | ASR, robust accuracy, robustness gap |
| 프라이버시 공격 | 모델이 학습 데이터나 민감 속성을 누출하지 않는가 | P05 | MI advantage, leakage risk |
| 공격-방어-평가 체계 | 공격자 지식, 방어 가정, 평가 지표가 함께 명시됐는가 | P02-P05 | threat model completeness |
| 재현성·책임성 | 수치와 주장을 다시 확인할 증거가 남아 있는가 | P02 | seed, config, log, DOI |

---

## 2. CIA+PRA 관점 분석

W01에서는 전통적 CIA뿐 아니라 Privacy, Safety, Accountability를 함께 본다.

| 관점 | 관련 위협 | 설명 | 대표 지표 |
|---|---|---|---|
| Confidentiality | membership inference, model inversion, property inference | 모델이 정상 작동하더라도 학습 데이터나 민감 속성이 추론될 수 있다. | MI advantage, leakage rate |
| Integrity | adversarial example, poisoning, backdoor | 입력·데이터·학습 과정 조작으로 예측이 왜곡될 수 있다. | ASR, robust accuracy |
| Availability | 탐지 회피, 오탐 폭증, 모델 성능 붕괴 | 공격이 서비스 거부나 운영자 피로를 유발할 수 있다. | FAR, alert volume, MTTR |
| Privacy | 과적합, confidence leakage, shadow model attack | 개인정보 보호는 단순 접근제어가 아니라 모델 출력 설계와 연결된다. | privacy risk, utility drop |
| Safety | 안전 중요 시스템에서의 잘못된 판단 | ML 오류가 물리적·사회적 피해로 이어질 수 있다. | safety violation rate |
| Accountability | 로그 누락, 데이터 버전 미관리, 재현 불가 | 보안 사고 후 원인 분석과 책임 추적이 어려워진다. | evidence coverage, audit completeness |

---

## 3. 공격-방어-평가 분류

| 구분 | 내용 | W01 적용 |
|---|---|---|
| 공격 자산 | 데이터, 모델 파라미터, 입력, 출력, 평가셋, 로그, 배포 파이프라인 | 각 논문을 생명주기 단계에 매핑 |
| 공격자 지식 | White-box, gray-box, black-box | 공격 성공률 해석의 전제 조건으로 기록 |
| 공격자 능력 | 입력 조작, 데이터 오염, 질의 반복, 출력 관찰, 학습 과정 접근 | 악용 절차는 제외하고 위협모형 수준으로 기술 |
| 공격자 목표 | 오분류, 탐지 회피, 정보추출, 지표왜곡, 서비스 방해 | 지표별로 목표를 분리 |
| 방어 방법 | 데이터 검증, robust training, 출력 제한, DP, 모니터링, human review | 방어 효과와 비용을 함께 비교 |
| 평가 지표 | clean accuracy, F1, ASR, robust accuracy, leakage risk, reproducibility score | 통합보고서와 실험 설계에 반영 |
| 증거 요구 | DOI, config, seed, raw output, run log, human review | W15 evidence chain으로 연결 |

---

## 4. 생명주기 단계별 보안 이슈

| 단계 | 주요 위협 | 방어·점검 | 대표 지표 |
|---|---|---|---|
| 데이터 수집 | 데이터 오염, 편향, 개인정보 포함 | 출처 기록, 라벨 검수, 개인정보 제거 | data provenance, label error rate |
| 전처리 | feature leakage, 잘못된 정규화, split leakage | pipeline versioning, split audit | leakage check, config hash |
| 모델 학습 | poisoning, backdoor, overfitting | seed/config 보존, validation split, regularization | train/test gap, utility |
| 모델 검증 | 평가셋 오염, 단일 지표 의존 | clean/robust/privacy/reproducibility 지표 분리 | robust accuracy, MI advantage |
| 배포 | 환경 차이, model extraction, 출력 과다노출 | 접근 제어, rate limit, 출력 최소화 | query rate, output exposure |
| 추론 | evasion, adversarial example | 입력 검증, 모니터링, robust evaluation | ASR, detection rate |
| 모니터링 | drift 미탐, 로그 누락 | drift detection, 감사 로그, rollback | drift score, audit completeness |

---

## 5. 보안 이슈별 주의점

### 5.1 ML 생명주기 보증

보안 평가는 학습된 모델 파일만 검사해서 끝나지 않는다. 데이터 출처, 라벨링 방식, 전처리 코드, 학습 설정, 검증 데이터, 배포 환경, 모니터링 로그가 함께 보존되어야 한다.

### 5.2 침입탐지와 ML

침입탐지에서는 accuracy보다 false positive와 false negative의 비용이 중요하다. 탐지율이 높아도 오탐이 많으면 운영자가 경보를 무시하게 되고, 미탐이 많으면 실제 침해가 지나간다.

### 5.3 대적 머신러닝

방어 방법은 단일 공격에만 강한지, transfer attack이나 adaptive attack에도 버티는지 확인해야 한다. 방어가 gradient masking에 기대고 있으면 겉보기 성능만 좋아질 수 있다.

### 5.4 프라이버시 공격

프라이버시 위험은 모델이 틀릴 때만 생기지 않는다. 모델이 너무 잘 맞거나 confidence를 과도하게 노출할 때도 학습 데이터 포함 여부와 민감 속성이 추론될 수 있다.

### 5.5 재현성 실패

수치가 있어도 seed, config, data split, output log가 없으면 연구 주장으로서 약하다. W01 결과값은 실행 로그와 함께 보고해야 한다.

---

## 6. 기말논문 연결

기말논문에서는 W01의 보안 이슈를 “생명주기 기반 평가 항목”으로 확장한다. 각 주차 주제는 데이터 단계, 학습 단계, 검증 단계, 배포·운영 단계 중 어디에 위치하는지 표시하고, 성능·강건성·프라이버시·재현성을 함께 비교한다.

| 기말논문 장 | W01 보안 이슈 반영 |
|---|---|
| 2장 관련연구 | CIA+Privacy+Safety+Accountability 관점 정리 |
| 3장 위협모형 | 생명주기 단계별 보호 자산·공격자 목표 정의 |
| 4장 연구방법 | clean/robust/privacy/reproducibility 다중 지표 설계 |
| 5장 분석 | W01 toy 결과와 문헌 matrix를 분리해 해석 |
| 6장 보안적 함의 | 운영 로그, human review, 공개 저장소 PDF 위험, 책임성 논의 |
