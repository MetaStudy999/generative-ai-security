# 실험 보고서

## 1. 실험 목표

W14 실습은 MLOps/DevOps·데이터/모델 파이프라인·공급망 보안의 최소 통제항목을 synthetic MLOps toy pipeline 기반 안전 실험에서 확인하는 것이다. 실제 운영 서비스, 실제 개인정보, 무단 접근, 실제 악성 패키지 배포는 포함하지 않는다.

Toy logistic regression을 사용한 이유는 모델 성능 경쟁이 아니라 evidence set 구조를 안전하고 재현 가능하게 검증하기 위해서다. 즉, dataset hash, config hash, model hash, drift score, audit coverage, inventory coverage, re-run consistency가 함께 남는지 확인하는 것이 핵심이다.

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
docker compose run --rm w14-mlops-supply-chain python3 src/run_experiment.py --config configs/config.yaml
```

`docker-compose.yml`의 기본 command는 `bash`이므로, 실험 자동 실행은 위 명령처럼 명시적으로 지정한다.

2026-06-23 재검증에서 `docker compose build`와 `docker compose run --rm w14-mlops-supply-chain python3 src/run_experiment.py --config configs/config.yaml` 명령이 모두 성공했다.

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
| Log audit | Audit coverage | 1.000000 | toy 필수 로그 필드 보존률 |
| Artifact inventory | Inventory coverage | 1.000000 | toy AI BOM/ML artifact inventory 최소 항목 충족률 |

### 5.1 Drift score 해석 보완

본 실험의 drift score는 synthetic 기준 데이터와 drifted 데이터의 평균 표준화 feature shift이다. 이 값은 실제 운영 장애나 공격 성공률을 의미하지 않는다. 다만 drift score가 threshold 0.25를 초과하면 운영형 AI 시스템에서 human review, rollback 검토, 추가 데이터 검증, model performance 재평가가 필요하다는 감시 신호로 해석한다.

### 5.2 MLOps Evidence Set 해석

| Evidence 항목 | 의미 | 보안 연결 | 한계 |
|---|---|---|---|
| Dataset hash | 데이터 버전의 무결성 기준점 | 데이터 오염·변조 탐지 | 데이터 품질 자체를 보장하지는 않음 |
| Config hash | 실험·학습 설정의 재현성 기준점 | 설정 변조 탐지 | 외부 의존성 버전까지 포함 필요 |
| Model hash | 모델 artifact 변경 탐지 | 모델 변조 탐지 | 모델 행동 의미를 설명하지는 않음 |
| Drift score | 운영 입력 분포 변화 감시 | drift 미탐지 방지 | 원인 분석·대응 결정은 별도 필요 |
| Audit coverage | 필수 로그 필드 보존률 | 책임추적성 | 로그 품질·진실성을 보장하지는 않음 |
| Inventory coverage | AI BOM/ML artifact inventory 최소 항목 충족률 | 공급망 가시성 | SBOM, license, vulnerability scan 확장 필요 |

### 5.3 AI BOM / ML Artifact Inventory 확장 항목

| 범주 | 필수 항목 | W14 toy 실험 반영 | 운영 확장 필요 |
|---|---|---|---|
| Dataset | dataset name, version, hash, source, license, personal data flag | 일부 반영 | data card, lineage, consent, retention |
| Feature pipeline | feature code version, transformation hash | 미반영 | feature store lineage |
| Training code | git commit, source hash, environment | 일부 반영 필요 | signed build, branch protection |
| Config | config hash, hyperparameters, seed | 반영 | config approval workflow |
| Model artifact | model hash, model type, metric, registry path | 반영 | model card, signature, registry ACL |
| Dependency | package list, container image digest | 미반영 | SBOM, vulnerability scan |
| Deployment | deployment version, endpoint, rollout policy | 미반영 | canary, rollback, approval gate |
| Monitoring | drift score, threshold, telemetry schema | 일부 반영 | alerting, incident response |
| Audit | run log, audit log, approval record | 일부 반영 | immutable log, access log |

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
- `experiment.results_recorded`와 `experiment.notes`는 실행 분기용이 아니라 기록용 필드이며, `results.json`의 config 블록에 보존된다.
- `status`는 실행 상태 기록용 metadata로 `results.json`과 `run_log.md`에 남는다.
- `src/run_experiment.py`는 synthetic data만 생성하며 외부 네트워크나 실제 개인정보를 사용하지 않는다.
- 결과값은 `outputs/run_log.md`, `metrics_summary.csv`, `results.json`과 보고서 표가 일치해야 한다.
- audit required fields 10개는 `audit_log.jsonl`에 모두 기록되어 toy audit coverage 1.000000으로 계산되었다.
- `pyproject.toml`은 현재 코드에서 실제 필요한 `pyyaml`만 남겼다. YAML parser가 없을 때도 내장 단순 parser로 실행 가능하다.

## 8. 한계

본 실습은 MLOps 보안통제의 최소 evidence 구조를 보여주는 toy pipeline이다. 실제 model registry, CI/CD, package vulnerability scanner, Kubernetes deployment, production telemetry는 구현하지 않았다. Drift score는 입력 분포 변화 경보이며, 원인 분석이나 자동 대응은 별도 절차가 필요하다.

이 결과는 synthetic MLOps toy pipeline 기반 평가 형식 검증용 수치이며, 실제 model registry, CI/CD, Kubernetes, package vulnerability scanner, production telemetry, 실제 기업 공급망 보안 수준으로 일반화하지 않는다.
