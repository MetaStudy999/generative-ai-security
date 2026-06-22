# W03 실험 보고서

## 1. 실험 목표

W03 실습은 컴퓨터비전 표현학습 및 비전 대적공격의 평가 지표를 안전한 toy 환경에서 분리 기록하는 것이다. 본 실습은 실제 CNN/ViT 공격 재현이 아니라 W03의 핵심인 비전 대적공격 평가축을 안전하게 설명하기 위한 최소 toy protocol이다. 따라서 synthetic 8x8 막대 이미지와 nearest-centroid model을 사용하되, 평가 구조는 이후 CNN, ViT, 2D/3D 비전 모델에도 확장 가능하도록 clean accuracy, robust accuracy, ASR, robust drop, confusion matrix, reproducibility evidence로 분리하였다.

## 2. 안전 범위

| 구분 | 허용 | 제외 |
|---|---|---|
| 데이터 | synthetic 8x8 bar image | 실제 개인정보, 운영 서비스 이미지, 무단 수집 데이터 |
| 모델 | nearest-centroid classifier | 실제 운영 CNN/ViT 모델 공격 재현 |
| 공격 시나리오 | 중심점 방향 L-infinity perturbation toy 평가 | 실제 서비스 침해, 악용 가능한 공격 절차 |
| 방어 점검 | 2-level feature squeezing toy check | 실서비스 방어 효과 일반화 |
| 결과 기록 | 실행 로그가 있는 정량값, config 기반 재현 정보 | 실행하지 않은 수치, 출처 없는 성능 주장 |

## 3. 환경

| 항목 | 내용 |
|---|---|
| OS | Ubuntu 24.04 기준 |
| Container | Docker compose 또는 로컬 Python |
| Python | 3.11 |
| 의존성 | `pyyaml` only; 없으면 fallback parser 사용 |
| Dataset | `synthetic_8x8_bar_images` |
| Model | `nearest_centroid` |
| Seed | 42 |
| 결과 상태 | 실행 완료, 정량 결과 `outputs/` 기록 완료 |

## 4. condition 이름 대응

| 코드 condition | 보고서 표시명 | 설명 |
|---|---|---|
| `clean_baseline` | Clean baseline | 정상 입력 기준 성능 |
| `centroid_direction_linf` | Adversarial perturbation | 반대 클래스 중심점 방향 L-infinity toy perturbation |
| `adversarial_with_feature_squeeze` | Feature squeezing check | epsilon 0.30 perturbation 뒤 2-level feature squeezing 적용 |

## 5. 실행 소스

| 항목 | 내용 |
|---|---|
| 소스 파일 | `src/run_experiment.py` |
| 입력 설정 | `configs/config.yaml` |
| 출력 파일 | `outputs/metrics_summary.csv`, `outputs/results.json`, `outputs/run_log.md` |
| 예시 이미지 | `outputs/clean_example.pgm`, `outputs/adversarial_eps_0_30.pgm`, `outputs/feature_squeezed_eps_0_30.pgm` |
| 로컬 실행 명령 | `python3 src/run_experiment.py --config configs/config.yaml` |
| Docker 실행 명령 | `docker compose run --rm w03-computer-vision-adversarial python src/run_experiment.py --config configs/config.yaml` |

## 6. outputs 정합성 확인

`outputs/metrics_summary.csv`, `outputs/results.json`, `outputs/run_log.md`의 핵심 수치는 서로 일치한다. clean baseline의 ASR은 공격 조건이 아니므로 CSV에서는 빈칸, JSON에서는 `null`, 제출용 보고서에서는 `N/A` 또는 `해당 없음`으로 표시한다.

| 파일 | 존재 여부 | 비고 |
|---|---|---|
| `metrics_summary.csv` | 존재 | 조건별 accuracy, macro F1, ASR, robust drop 기록 |
| `results.json` | 존재 | metadata, rows, confusion matrix, PGM 예시 배열 기록 |
| `run_log.md` | 존재 | Markdown 실행 로그 |
| `clean_example.pgm` | 존재 | Netpbm 8x8 ASCII greymap |
| `adversarial_eps_0_30.pgm` | 존재 | Netpbm 8x8 ASCII greymap |
| `feature_squeezed_eps_0_30.pgm` | 존재 | Netpbm 8x8 ASCII greymap |

## 7. 결과 기록표

정량값은 실제 실행한 `outputs/metrics_summary.csv`, `outputs/results.json`, `outputs/run_log.md` 기준으로 기록했다.

| 조건 | Epsilon | Defense | N | Accuracy | Macro F1 | ASR | Robust Drop | Confusion Matrix |
|---|---:|---|---:|---:|---:|---:|---:|---|
| Clean baseline | 0.00 | none | 120 | 1.000000 | 1.000000 | N/A | 0.000000 | `[[60, 0], [0, 60]]` |
| Adversarial perturbation | 0.05 | none | 120 | 1.000000 | 1.000000 | 0.000000 | 0.000000 | `[[60, 0], [0, 60]]` |
| Adversarial perturbation | 0.15 | none | 120 | 1.000000 | 1.000000 | 0.000000 | 0.000000 | `[[60, 0], [0, 60]]` |
| Adversarial perturbation | 0.30 | none | 120 | 1.000000 | 1.000000 | 0.000000 | 0.000000 | `[[60, 0], [0, 60]]` |
| Adversarial perturbation | 0.45 | none | 120 | 0.000000 | 0.000000 | 1.000000 | 1.000000 | `[[0, 60], [60, 0]]` |
| Feature squeezing check | 0.30 | feature_squeeze_2_levels | 120 | 1.000000 | 1.000000 | 0.000000 | 0.000000 | `[[60, 0], [0, 60]]` |

## 8. 해석 기준

epsilon 0.05, 0.15, 0.30에서는 synthetic two-class toy 데이터의 결정 경계가 유지되어 accuracy와 macro F1이 1.000000으로 유지되었다. epsilon 0.45에서는 반대 클래스 중심점 방향 perturbation이 두 클래스의 toy decision boundary를 넘어 모든 샘플이 뒤집혔다. 이 결과는 실제 CNN/ViT, 2D/3D perception system, physical attack 성능을 의미하지 않는다.

## 9. 재현성 점검

- `configs/config.yaml`의 핵심 필드는 코드에서 validation 또는 실행 입력으로 반영된다.
- `pyproject.toml`은 실제 사용 의존성인 `pyyaml`만 남겨 과도한 패키지를 제거했다.
- `Dockerfile`은 `python:3.11-slim`과 uv 기반 환경을 사용한다.
- `docker-compose.yml`은 기본 command를 `bash`로 유지하되, README에 자동 실행 명령을 명시했다.
- 결과값은 CSV, JSON, Markdown 로그, PGM 예시 이미지로 보존된다.

## 10. 한계

Synthetic 8x8 bar image와 nearest-centroid model은 실제 CNN, ViT, 2D/3D 비전 모델을 대표하지 않는다. Centroid-direction perturbation은 FGSM/PGD 같은 표준 공격을 직접 구현한 것이 아니라 평가축 설명용 toy perturbation이다. 본 실습은 안전한 지표 기록 예시로만 사용한다.
