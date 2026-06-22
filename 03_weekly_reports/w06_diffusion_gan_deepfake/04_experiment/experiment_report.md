# 실험 보고서

## 1. 실험 목표

W06 실습은 diffusion/GAN 기반 합성미디어와 딥페이크 탐지의 신뢰성 평가를 안전한 toy 환경에서 확인하는 것이다. 실제 딥페이크 생성, 실제 개인정보 사용, 실제 서비스 질의는 제외하고 synthetic real/fake detector score 분포만 사용했다.

핵심 질문은 “in-domain에서는 잘 맞는 탐지기가 압축·후처리·미지 생성기와 같은 cross-domain 조건에서도 신뢰할 수 있는가”이다.

## 2. 환경

| 항목 | 내용 |
|---|---|
| OS | Ubuntu 24.04 기준 |
| Container | Docker 사용 가능, 호스트 `python3` 실행 검증 |
| Python | 3.11 계열 또는 호스트 `python3` |
| Seed | 42 |
| 데이터 | synthetic real/fake detector score distributions |
| 실행 명령 | `python3 src/run_experiment.py --config configs/config.yaml` |
| 결과 상태 | 실행 완료 |

## 3. 실행 절차

| 단계 | 설계 내용 | 결과 기록 |
|---|---|---|
| In-domain score 분포 생성 | real mean 0.22, fake mean 0.78, std 0.08 | 120개 synthetic sample |
| Cross-domain score 분포 생성 | real mean 0.34, fake mean 0.61, std 0.16 | 120개 synthetic sample |
| Threshold detector 적용 | score >= 0.50이면 synthetic/deepfake 판정 | FPR/FNR, F1, AUROC 기록 |
| Review-band triage 적용 | score 0.40-0.60은 자동판정 대신 human review | auto coverage와 review rate 기록 |
| 결과 근거 보존 | CSV, JSON, run log 생성 | `outputs/`에 저장 |

## 4. 결과

| 조건 | Accuracy | F1 | FPR | FNR | AUROC | ECE | Auto coverage | Review rate | 해석 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| In-domain detector baseline | 1.000000 | 1.000000 | 0.000000 | 0.000000 | 1.000000 | 0.216327 | 해당 없음 | 해당 없음 | 기준 도메인에서는 real/fake score 분리가 명확함 |
| Cross-domain reliability stress | 0.816667 | 0.813559 | 0.166667 | 0.200000 | 0.899722 | 0.147949 | 해당 없음 | 해당 없음 | score margin이 줄어 FPR/FNR trade-off가 나타남 |
| Review-band triage on shifted domain | 0.909091 | 0.901408 | 0.050000 | 0.135135 | 0.962162 | 0.174872 | 0.641667 | 0.358333 | 불확실 구간 35.8333%를 검토로 보내 자동판정 위험을 낮춤 |

정량값은 `outputs/run_log.md`, `outputs/metrics_summary.csv`, `outputs/results.json`과 일치한다.

## 5. 해석

In-domain accuracy가 1.000000이어도 cross-domain 조건에서는 accuracy가 0.816667로 떨어지고 FNR이 0.200000까지 증가했다. 이는 딥페이크 탐지에서 단일 benchmark 성능보다 transferability와 robustness를 분리해 기록해야 함을 보여준다.

Review-band triage는 모든 샘플을 자동 판정하지 않는다. 대신 0.40-0.60 불확실 구간을 human review로 보내 auto coverage를 0.641667로 낮추고, 자동판정 영역의 FPR을 0.050000, FNR을 0.135135로 낮췄다. 포렌식 맥락에서는 이처럼 자동 판정률과 검토율을 함께 보고해야 한다.

## 6. 재현성 점검

- `configs/config.yaml`에 seed, synthetic score 분포, threshold, review band를 기록했다.
- `src/run_experiment.py`는 CSV/JSON/run log를 모두 생성한다.
- 실행 산출물은 `outputs/metrics_summary.csv`, `outputs/results.json`, `outputs/run_log.md`에 보존했다.
- 실제 딥페이크 생성, 실제 개인정보, 무단 서비스 질의는 포함하지 않았다.

## 7. 한계

본 실습은 학습 목적의 synthetic toy 실험이다. 실제 딥페이크 데이터셋, 실제 detector, 법적 포렌식 증거능력으로 일반화하지 않는다. 수치는 평가 지표와 재현성 기록 구조를 설명하는 근거로만 사용한다.
