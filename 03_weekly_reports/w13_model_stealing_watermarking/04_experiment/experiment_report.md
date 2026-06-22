# 실험 보고서

## 1. 실험 목표

W13 실습은 모델 지식재산(IP)/모델 도난/모델 추출 위협의 보안 평가를 안전한 toy 환경에서 설계하는 것이다. 실제 시스템 침해나 실제 개인정보 사용은 제외한다.

## 2. 환경

| 항목 | 내용 |
|---|---|
| OS | Ubuntu 24.04 기준 |
| Container | Docker |
| Python | 3.x |
| Seed | 42 |
| 데이터 | 공개 데이터 또는 synthetic data |
| 결과 상태 | 실제 실행 전 |

## 3. 실행 절차

| 단계 | 설계 내용 | 결과 기록 |
|---|---|---|
| 공개 API가 아닌 toy classification model을 사용한다. | 설계 완료 | 실제 실행 결과는 실행 후 기록 |
| 원 모델과 substitute model의 출력 일치율을 비교하는 구조를 설계한다. | 설계 완료 | 실제 실행 결과는 실행 후 기록 |
| Query budget에 따른 substitute accuracy 변화를 기록할 수 있도록 설계한다. | 설계 완료 | 실제 실행 결과는 실행 후 기록 |
| 워터마킹은 실제 구현보다 검출 평가표 중심으로 작성한다. | 설계 완료 | 실제 실행 결과는 실행 후 기록 |
| 모델 소유권 검증 지표를 정리한다. | 설계 완료 | 실제 실행 결과는 실행 후 기록 |
| 결과는 실제 실행 전까지 빈칸으로 둔다. | 설계 완료 | 실제 실행 결과는 실행 후 기록 |

## 4. 결과

| 조건 | 주요 지표 | 결과 |
|---|---|---|
| Clean baseline | Accuracy/F1/Task score | 실행 전 |
| Security scenario | Attack impact/Risk score | 실행 전 |
| Defense/check | Robust score/Leakage score | 실행 전 |
| Reproducibility | Seed/config/log 확인 | 실행 전 |

## 5. 재현성 점검

- `configs/config.yaml`에 seed, 데이터, 실험 조건을 기록한다.
- Dockerfile 내부 uv sync와 pyproject.toml로 실행 환경을 고정한다.
- 결과값은 실제 실행 로그가 있을 때만 채운다.

## 6. 한계

본 실습은 학습 목적의 설계 초안이다. 실제 서비스, 실제 개인정보, 무단 공격 절차는 포함하지 않는다.
