# W05 평가방법

## 1. 평가 항목

| 평가 항목 | 지표 | 측정 방법 | 필요한 데이터 | 비고 |
|---|---|---|---|---|
| Clean Performance | clean accuracy | 정상 synthetic embedding을 nearest-centroid classifier로 평가 | synthetic 2D representation clusters | 기본 성능 |
| Poisoned Clean Performance | poisoned clean accuracy | poisoned training centroid로 clean test embedding 평가 | synthetic train/test split | clean 성능 유지 여부 |
| Backdoor Impact | attack success rate (ASR) | source-class test embedding에 trigger vector를 더한 뒤 target class 분류 비율 측정 | synthetic source test embeddings | 실제 공격 성능으로 일반화 금지 |
| Representation Change | mean representation shift | 원본 embedding과 trigger 적용 embedding 사이 거리 평균 | paired embedding | 표현공간 이동량 |
| Defense Check | ASR after defense, detection rate, clean FPR | consistency distance threshold로 trigger shift와 clean view shift를 분리 | paired-view consistency samples | toy 검증 |
| Reproducibility | seed/config/log completeness | seed, config, Docker, CSV/JSON/run_log 보존 여부 점검 | 실행 로그 | W05 toy 실행 완료 |
| Human Review | 검토 완료 여부 | DOI, 제목, 저자, 수치, 인용 대응을 사람이 재검토 | 체크리스트 | 제출 전 필수 |

## 2. W05 outputs 기준 수치

| 조건 | Clean Acc. | Poisoned Clean Acc. | ASR | ASR after defense | Mean Shift | Detection Rate | Clean FPR |
|---|---:|---:|---:|---:|---:|---:|---:|
| Clean representation baseline | 1.000000 |  |  |  |  |  |  |
| Poisoned/backdoor representation |  | 1.000000 | 1.000000 |  | 2.418677 |  |  |
| Consistency defense check |  |  |  | 0.000000 | 0.090597 | 1.000000 | 0.000000 |

근거 파일은 `04_experiment/outputs/metrics_summary.csv`, `04_experiment/outputs/results.json`, `04_experiment/outputs/run_log.md`다.

## 3. 실행 원칙

실험을 수행하지 않은 문서에는 정량값을 비워 두거나 미수행 상태로 표시한다. W05는 synthetic toy 실험을 실행했으므로 정량 수치는 outputs 파일에 기록된 값만 사용한다.

## 4. 한계 문장

이 결과는 synthetic 2D representation toy 실험의 평가 형식 검증용 수치이며, 실제 SSL 모델, foundation model, 상용 시스템의 poisoning/backdoor 보안 성능으로 일반화하지 않는다.
