# 실습보고서 템플릿

## 1. 실습 목표

-

---

## 2. 실습 환경

| 항목 | 내용 |
|---|---|
| OS | Ubuntu 24.04 |
| 실행 방식 | Docker |
| Python | 3.11 (`python:3.11-slim`) |
| 패키지 관리자 | uv (Dockerfile 내부 포함) |
| 의존성 설치 | 컨테이너 내부 `uv sync` |
| Dataset | 확인 필요 |
| Seed | 확인 필요 |
| 결과 상태 | 설계만 완료 / 실행 완료 |
| GPU | Optional |

---

## 3. 프로젝트 구조

```text
experiment/
├── README.md
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
├── configs/
│   └── config.yaml
├── src/
├── outputs/
│   ├── metrics_summary.csv
│   ├── results.json
│   └── run_log.md
└── experiment_report.md
```

Dockerfile은 WSL 호스트에 uv를 설치하지 않고, 다음 방식으로 이미지 안에 uv를 포함한다.

```dockerfile
FROM python:3.11-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
RUN uv sync --no-dev
```

---

## 4. 실행 명령어

```bash
docker build -t aisec-experiment .
docker run --rm -it -v $(pwd):/workspace aisec-experiment bash
python src/run_experiment.py --config configs/config.yaml
```

---

## 5. 실험 설계

| 항목 | 내용 |
|---|---|
| Baseline |  |
| Attack/Threat Scenario |  |
| Defense/Check |  |
| Evaluation Metric |  |
| Dataset | 공개 데이터 / synthetic data / toy data |
| Seed |  |
| Safety Scope | 실제 개인정보, 운영 서비스, 무단 공격 절차 제외 |

---

## 6. 실험 결과

실행 전에는 결과값을 비워 두거나 `실행 전`으로 표시한다. 실행 후에는 `outputs/run_log.md` 기준으로 아래 표를 채우고, CSV/JSON 원본을 함께 보존한다.

| 조건 | 주요 지표 | 결과 | 근거 파일 |
|---|---|---|---|
| Clean baseline | Accuracy/F1/Task score | 실행 전 |  |
| Security scenario | ASR/Attack impact/Risk score | 실행 전 |  |
| Defense/check | Robust score/Leakage score | 실행 전 |  |
| Reproducibility | Seed/config/log 확인 | 실행 전 |  |

실행 완료 시 요약표:

| 조건 | Metric 1 | Metric 2 | Risk/ASR | 해석 |
|---|---:|---:|---:|---|
| Clean |  |  | 해당 없음 |  |
| Attack |  |  |  |  |
| Defense |  |  |  |  |

---

## 7. 오류와 해결

| 오류 | 원인 | 해결 |
| -- | -- | -- |
|    |    |    |

---

## 8. 논문과의 연결

*

---

## 9. 재현 가능성 점검

* [ ] Dockerfile 존재
* [ ] pyproject.toml 존재
* [ ] WSL 호스트에 uv 미설치
* [ ] Dockerfile 내부 uv 복사 명령 확인
* [ ] 컨테이너 내부 uv sync 실행
* [ ] config.yaml 존재
* [ ] seed 고정
* [ ] `outputs/results.json` 저장
* [ ] `outputs/metrics_summary.csv` 저장
* [ ] `outputs/run_log.md` 저장
* [ ] 실행 명령어 기록
* [ ] 실행 후 통합보고서, 제출 체크리스트, AI 활용기록 갱신
* [ ] 실행하지 않은 수치를 결과처럼 작성하지 않았음
