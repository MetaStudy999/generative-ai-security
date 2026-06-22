# W05 실험 보고서

## 1. 실험 목표

본 실습은 실제 SSL encoder 또는 파운데이션 모델 backdoor 공격 재현이 아니라 W05의 핵심인 표현공간 오염 평가축을 안전하게 설명하기 위한 최소 toy protocol이다. 따라서 synthetic 2차원 표현공간 클러스터와 nearest-centroid representation classifier를 사용하되, 평가 구조는 이후 SSL encoder, 비디오 표현학습, LLM/foundation model pretraining에도 확장 가능하도록 clean accuracy, poisoned clean accuracy, ASR, mean representation shift, detection rate, clean FPR, reproducibility evidence로 분리하였다.

## 2. 환경

| 항목 | 내용 |
|---|---|
| OS | Ubuntu 24.04 기준 |
| Container | Docker compose 실행 가능 구조 |
| Python | 3.11 계열 또는 호스트 `python3` |
| Seed | 42 |
| 데이터 | synthetic 2D representation clusters |
| 분류기 | nearest-centroid representation classifier |
| 결과 상태 | 실행 완료 |

## 3. 실행 명령

```bash
python3 src/run_experiment.py --config configs/config.yaml
```

Docker 사용 시:

```bash
docker compose run --rm w05-ssl-backdoor python3 src/run_experiment.py --config configs/config.yaml
```

## 4. 실험 설계

| 단계 | 설계 내용 | 결과 기록 |
|---|---|---|
| Clean representation baseline | clean synthetic embedding을 nearest-centroid classifier로 분류 | clean accuracy |
| Poisoned/backdoor representation | source embedding 일부에 trigger vector를 적용해 target label 학습 샘플로 추가 | poisoned clean accuracy, ASR, mean shift |
| Consistency defense check | paired-view distance threshold로 trigger shift를 플래그 | ASR after defense, detection rate, clean FPR |
| Reproducibility evidence | seed/config/script/output 보존 | CSV, JSON, run log |

## 5. 결과

| 조건 | Clean Acc. | Poisoned Clean Acc. | ASR | ASR after defense | Mean Shift | Detection Rate | Clean FPR |
|---|---:|---:|---:|---:|---:|---:|---:|
| Clean representation baseline | 1.000000 |  |  |  |  |  |  |
| Poisoned/backdoor representation |  | 1.000000 | 1.000000 |  | 2.418677 |  |  |
| Consistency defense check |  |  |  | 0.000000 | 0.090597 | 1.000000 | 0.000000 |

근거 파일:

- `outputs/metrics_summary.csv`
- `outputs/results.json`
- `outputs/run_log.md`

## 6. 결과 해석

Clean accuracy 1.000000은 toy cluster가 정상 조건에서 분리 가능하다는 뜻이다. ASR 1.000000은 source-class test embedding 16개가 trigger vector 적용 후 target centroid 쪽으로 분류된 toy 관찰값이다. Detection rate 1.000000과 clean FPR 0.000000은 paired-view distance threshold 조건에서 trigger shift가 모두 플래그되고 clean consistency noise는 플래그되지 않았다는 뜻이며, 실제 방어 성능 보증이 아니다.

## 7. 재현성 점검

- `configs/config.yaml`에 seed, 데이터, poison rate, trigger vector, defense threshold를 기록했다.
- `pyproject.toml` 의존성은 현재 코드가 사용하는 `pyyaml`만 남겼다.
- `docker compose build`와 `docker compose run --rm w05-ssl-backdoor python3 src/run_experiment.py --config configs/config.yaml` 실행을 확인했다.
- `docker-compose.yml`의 command는 `bash`이며, 자동 실행 명령은 README에 별도 명시했다.
- 정량값은 `outputs/run_log.md`, `outputs/metrics_summary.csv`, `outputs/results.json`과 일치한다.

## 8. 한계

이 결과는 synthetic 2D representation toy 실험의 평가 형식 검증용 수치이며, 실제 SSL 모델, foundation model, 상용 시스템의 poisoning/backdoor 보안 성능으로 일반화하지 않는다.
