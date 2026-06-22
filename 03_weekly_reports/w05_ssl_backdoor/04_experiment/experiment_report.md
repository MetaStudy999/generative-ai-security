# 실험 보고서

## 1. 실험 목표

W05 실습은 자기지도학습/파운데이션 모델 및 Poisoning/Backdoor의 보안 평가를 안전한 toy 환경에서 설계하는 것이다. 실제 시스템 침해나 실제 개인정보 사용은 제외한다.

## 2. 환경

| 항목 | 내용 |
|---|---|
| OS | Ubuntu 24.04 기준 |
| Container | Docker |
| Python | 3.11 계열 또는 호스트 `python3` |
| Seed | 42 |
| 데이터 | synthetic 2D representation clusters |
| 결과 상태 | 실행 완료 |

## 3. 실행 절차

| 단계 | 설계 내용 | 결과 기록 |
|---|---|---|
| Clean representation baseline 구성 | 완료 | clean synthetic embedding nearest-centroid accuracy 1.000000 |
| 간단한 feature extraction 또는 embedding 생성 | 완료 | source/target 2차원 synthetic 표현공간 생성 |
| 오염 전후 feature distribution 비교 | 완료 | poisoned clean accuracy 1.000000, 평균 trigger shift 2.418677 |
| Backdoor trigger가 표현공간에 미치는 영향 설명 | 완료 | triggered source embedding ASR 1.000000 |
| Consistency 방어 점검 | 완료 | detection rate 1.000000, clean FPR 0.000000 |
| 결과 근거 보존 | 완료 | `outputs/run_log.md`, `metrics_summary.csv`, `results.json` |

## 4. 결과

| 조건 | 주요 지표 | 결과 |
|---|---|---|
| Clean baseline | Clean accuracy | 1.000000 |
| Security scenario | Attack success rate | 1.000000 |
| Security scenario | Mean representation shift | 2.418677 |
| Defense/check | ASR after defense | 0.000000 |
| Defense/check | Trigger detection rate / clean FPR | 1.000000 / 0.000000 |
| Reproducibility | Seed/config/log 확인 | 완료 |

## 5. 재현성 점검

- `configs/config.yaml`에 seed, 데이터, poison rate, trigger vector, defense threshold를 기록했다.
- Dockerfile 내부 uv sync와 pyproject.toml로 컨테이너 실행 환경을 고정했다.
- 호스트 검증은 `python3 src/run_experiment.py --config configs/config.yaml`로 수행했다.
- 정량값은 `outputs/run_log.md`, `outputs/metrics_summary.csv`, `outputs/results.json`과 일치한다.

## 6. 한계

본 실습은 학습 목적의 synthetic toy 실험이다. 실제 SSL 모델, foundation model, 실제 서비스, 실제 개인정보, 무단 공격 절차는 포함하지 않는다. 따라서 수치는 보안 성능 일반화가 아니라 평가 지표와 재현성 기록 구조를 설명하는 근거로만 사용한다.
