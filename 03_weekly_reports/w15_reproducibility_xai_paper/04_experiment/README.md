# W15 실습 폴더

이 폴더는 연구평가·재현성·설명가능성(XAI)·논문 구성 주차의 Docker 기반 실습 환경, 설정, 결과, 로그, 실습보고서를 관리한다.

## 구성

- `experiment_report.md`: 실습 목표, 평가 설계, 결과 기록 위치
- `Dockerfile`: 재현 가능한 Python 실행 환경
- `docker-compose.yml`: 로컬 컨테이너 실행 예시
- `pyproject.toml`: uv sync용 주차별 Python 프로젝트 메타데이터. 현재 감사 스크립트는 Python 표준 라이브러리만 사용하므로 dependencies는 빈 목록이다.
- `configs/config.yaml`: seed, 데이터, 보안 범위, 결과 기록 상태
- `src/run_experiment.py`: 로컬 재현성·제출 준비 감사 스크립트
- `outputs/`: 감사 실행 결과(`metrics_summary.csv`, `results.json`, `run_log.md`)

## 의존성 설치 원칙

WSL 호스트에는 uv를 설치하지 않는다. Dockerfile은 `python:3.11-slim` 기반에서 `COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/`로 uv를 포함하고, 컨테이너 내부에서 `uv sync`를 실행한다. 현재 `src/run_experiment.py`는 `argparse`, `csv`, `json`, `re`, `datetime`, `pathlib`만 사용하므로 별도 외부 패키지가 필요 없다.

## 원칙

실제 실행 전에는 결과값을 작성하지 않는다. 실행 후에는 `outputs/metrics_summary.csv`, `outputs/results.json`, `outputs/run_log.md`를 보존하고, 실험보고서·통합보고서·제출 체크리스트·AI 활용기록을 함께 갱신한다. DOI, URL, 원문 세부 수치, 실험 결과는 최종 검증 자료가 있을 때만 확정한다.

현재 W15는 모델 성능 실험이 아니라 로컬 재현성·제출 준비 감사로 실행 완료했다. 개인정보 사용, 실제 공격 수행, benchmark 성능 주장은 없다.

## 실행 예시

로컬 실행:

```bash
python3 src/run_experiment.py --config configs/config.yaml
```

Docker 실행은 repo root 전체를 `/workspace`로 마운트해야 한다. 감사 스크립트가 `04_final_paper/`도 함께 확인하기 때문이다.

```bash
docker build -t w15-reproducibility-xai-paper .
docker run --rm -v /home/ubuntu/generative-ai-security:/workspace -w /workspace/03_weekly_reports/w15_reproducibility_xai_paper/04_experiment w15-reproducibility-xai-paper python src/run_experiment.py --config configs/config.yaml
```
