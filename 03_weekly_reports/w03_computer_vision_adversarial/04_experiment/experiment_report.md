# W03 실험 보고서

## 1. 실험 목표

W03 실습은 컴퓨터비전 표현학습 및 비전 대적공격의 보안 평가를 안전한 toy 환경에서 확인하는 것이다. 실제 시스템 침해, 실제 개인정보 사용, 무단 공격 절차는 제외하고 synthetic 8x8 이미지와 단순 최근접 중심 분류기를 사용했다.

## 2. 안전 범위

| 구분 | 허용 | 제외 |
|---|---|---|
| 데이터 | synthetic 8x8 bar image | 실제 개인정보, 운영 서비스 이미지, 무단 수집 데이터 |
| 공격 시나리오 | 중심점 방향 L-infinity perturbation toy 평가 | 실제 서비스 침해, 악용 가능한 공격 절차 |
| 방어 점검 | 2-level feature squeezing toy check | 실서비스 방어 효과 일반화 |
| 결과 기록 | 실행 로그가 있는 정량값, config 기반 재현 정보 | 실행하지 않은 수치, 출처 없는 성능 주장 |

## 3. 환경

| 항목 | 내용 |
|---|---|
| OS | Ubuntu 24.04 기준 |
| Container | Docker |
| Python | 3.11 또는 로컬 `python3` |
| Dataset | `synthetic_8x8_bar_images` |
| Model | `nearest_centroid` |
| Seed | 42 |
| 결과 상태 | 실행 완료, 정량 결과 `outputs/` 기록 완료 |

## 4. 실행 절차

| 단계 | 설계 내용 | 기록 지표 | 현재 상태 |
|---|---|---|---|
| Clean baseline 학습 | synthetic vertical/horizontal bar 이미지 분류 | accuracy, macro F1, confusion matrix | 실행 완료 |
| Adversarial perturbation | 반대 클래스 중심점 방향으로 L-infinity 교란 | robust accuracy, ASR, robust drop | 실행 완료 |
| Clean/robust 비교 | epsilon별 성능 변화 확인 | accuracy, macro F1 | 실행 완료 |
| 공격 전후 이미지 예시 | clean/adversarial/feature-squeezed PGM 저장 | `*.pgm` | 실행 완료 |
| Defense/check | epsilon 0.30 입력에 2-level feature squeezing 적용 | defended accuracy, ASR | 실행 완료 |

## 5. 실행 소스

| 항목 | 내용 |
|---|---|
| 소스 파일 | `src/run_experiment.py` |
| 입력 설정 | `configs/config.yaml` |
| 출력 파일 | `outputs/metrics_summary.csv`, `outputs/results.json`, `outputs/run_log.md` |
| 예시 이미지 | `outputs/clean_example.pgm`, `outputs/adversarial_eps_0_30.pgm`, `outputs/feature_squeezed_eps_0_30.pgm` |
| 실행 명령 | `python3 src/run_experiment.py --config configs/config.yaml` |

## 6. 결과 기록표

정량값은 실제 실행한 `outputs/run_log.md` 기준으로 기록했다.

| 조건 | Epsilon | Defense | Accuracy | Macro F1 | ASR | Robust Drop | 해석 |
|---|---:|---|---:|---:|---:|---:|---|
| Clean baseline | 0.00 | none | 1.000000 | 1.000000 | 해당 없음 | 0.000000 | 기준 성능 |
| Adversarial perturbation | 0.05 | none | 1.000000 | 1.000000 | 0.000000 | 0.000000 | 작은 교란에서는 결정 경계 유지 |
| Adversarial perturbation | 0.15 | none | 1.000000 | 1.000000 | 0.000000 | 0.000000 | toy 데이터의 여유 마진 유지 |
| Adversarial perturbation | 0.30 | none | 1.000000 | 1.000000 | 0.000000 | 0.000000 | feature squeezing 점검 기준 epsilon |
| Adversarial perturbation | 0.45 | none | 0.000000 | 0.000000 | 1.000000 | 1.000000 | 반대 클래스 중심으로 넘어가 모든 샘플 오분류 |
| Feature squeezing check | 0.30 | 2-level | 1.000000 | 1.000000 | 0.000000 | 0.000000 | 작은 교란은 단순 양자화로 제거됨 |

## 7. 재현성 점검

- `configs/config.yaml`에 seed, 데이터, 실험 조건을 기록한다.
- Dockerfile 내부 uv sync와 pyproject.toml로 실행 환경을 고정한다.
- `src/run_experiment.py`는 로컬에 외부 패키지가 없어도 실행되도록 표준 라이브러리 fallback을 포함한다.
- 결과값은 실제 실행 로그 `outputs/run_log.md` 기준으로 확정했다.
- 코드 실행 시 CSV, JSON, Markdown 로그, PGM 예시 이미지가 동시에 생성된다.

## 8. 해석 기준

이 실험은 실제 이미지 모델 공격 성능을 주장하기 위한 것이 아니라, clean accuracy와 robust accuracy, ASR, 방어 점검 지표를 분리해서 기록하는 방법을 보여주는 최소 예시다. Epsilon 0.45에서 성능이 급락한 것은 synthetic 두 클래스의 중심점 경계를 넘어선 결과이며, 실제 CNN/ViT 모델의 강건성으로 일반화하지 않는다.

## 9. 한계

Synthetic 8x8 bar image와 nearest-centroid 모델은 실제 CNN, ViT, 2D/3D 비전 모델을 대표하지 않는다. 본 실습은 W03 보고서에서 비전 대적공격 평가 지표 구조를 설명하기 위한 안전한 toy 예시로만 사용한다.
