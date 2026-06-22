# 실험 보고서

## 1. 실험 목표

W14 실습은 MLOps/DevOps·데이터/모델 파이프라인·공급망 보안의 최소 통제항목을 안전한 synthetic toy 환경에서 확인하는 것이다. 실제 운영 서비스, 실제 개인정보, 무단 접근, 실제 악성 패키지 배포는 포함하지 않는다.

## 2. 환경

| 항목 | 내용 |
|---|---|
| OS | Ubuntu 24.04 기준 |
| Container | Dockerfile 제공, 로컬 실행은 Python 3.11 호환 코드 |
| Python | 3.11 기준 |
| Seed | 42 |
| 데이터 | synthetic_mlops_binary_classification |
| Train/Test sample | 320 / 160 |
| Feature 수 | 5 |
| 모델 | toy logistic regression |
| Drift shift | 0.60 |
| Drift threshold | 0.25 |
| 결과 상태 | 실행 완료 |

## 3. 실행 절차

```bash
python3 03_weekly_reports/w14_mlops_supply_chain/04_experiment/src/run_experiment.py --config 03_weekly_reports/w14_mlops_supply_chain/04_experiment/configs/config.yaml
```

Docker 사용 시에는 `04_experiment/`에서 다음 절차를 따른다.

```bash
docker build -t w14-aisec .
docker run --rm -it -v "$(pwd):/workspace" w14-aisec bash
python src/run_experiment.py --config configs/config.yaml
```

## 4. 실험 설계

| 단계 | 설계 내용 | 결과 기록 |
|---|---|---|
| Synthetic ML pipeline | 외부 데이터 없이 train/test/drift sample 생성 | `results.json` metadata |
| 데이터 버전관리 | train/test/drift dataset을 canonical JSON으로 변환 후 SHA-256 계산 | `dataset_sha256` |
| 모델 학습 | toy logistic regression 학습 | baseline accuracy/F1 |
| 모델 아티팩트 검증 | model payload를 저장하고 SHA-256 계산 | `model_artifact.json`, `model_sha256` |
| 재현 실행 | 같은 config/seed로 재실행 후 dataset/model hash 비교 | re-run consistency |
| Drift monitoring | 기준 test와 drifted sample의 평균 표준화 feature shift 계산 | drift score |
| AI BOM 초안 | dataset, model, config, run log inventory 작성 | `artifact_inventory.json` |
| 감사 로그 | 필수 감사 필드 10개 보존 여부 점검 | audit coverage |

## 5. 결과

| 점검 항목 | 측정 지표 | 결과 | 보안 의미 |
|---|---|---:|---|
| Baseline model | Accuracy | 0.925000 | 정상 조건 기준 성능 |
| Baseline model | F1 | 0.923077 | 정상 조건 분류 균형 |
| Data versioning | Dataset hash | `sha256:b9e597bccdbde442` | 데이터 무결성 기준점 |
| Model artifact verification | Model hash match | true | 모델 아티팩트 변조 탐지 기준 |
| Re-run consistency | Model/data hash match | true | 동일 config/seed 재실행 가능성 |
| Drift monitoring | Mean standardized feature shift | 0.307626 | 입력 분포 변화 감시 |
| Drifted model | Accuracy under drift | 0.925000 | 분포 변화 조건 성능 |
| Log audit | Audit coverage | 1.000000 | 책임추적 로그 완전성 |
| Artifact inventory | Inventory coverage | 1.000000 | AI BOM/ML artifact inventory 최소 항목 충족 |

## 6. 결과 파일

| 파일 | 내용 |
|---|---|
| `outputs/run_log.md` | 사람이 읽는 실행 로그와 결과표 |
| `outputs/metrics_summary.csv` | 조건별/점검항목별 정량 지표 |
| `outputs/results.json` | config, hash, metrics, artifact inventory |
| `outputs/model_artifact.json` | toy model payload와 metadata |
| `outputs/artifact_inventory.json` | dataset, model, config, run log inventory |
| `outputs/audit_log.jsonl` | 감사 필드 기록 |

## 7. 재현성 점검

- `configs/config.yaml`에 seed, 데이터 크기, drift shift, threshold, 실행 상태를 기록했다.
- `src/run_experiment.py`는 synthetic data만 생성하며 외부 네트워크나 실제 개인정보를 사용하지 않는다.
- 결과값은 `outputs/run_log.md`, `metrics_summary.csv`, `results.json`과 보고서 표가 일치해야 한다.

## 8. 한계

본 실습은 MLOps 보안통제의 최소 evidence 구조를 보여주는 toy pipeline이다. 실제 model registry, CI/CD, package vulnerability scanner, Kubernetes deployment, production telemetry는 구현하지 않았다. Drift score는 입력 분포 변화 경보이며, 원인 분석이나 자동 대응은 별도 절차가 필요하다.
