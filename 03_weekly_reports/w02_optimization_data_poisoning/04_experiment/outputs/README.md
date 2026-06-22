# W02 실험 출력 폴더

`src/run_experiment.py`를 Docker 환경에서 실행해 다음 파일을 생성했다.

| 파일 | 내용 |
|---|---|
| `metrics_summary.csv` | 조건별 accuracy, macro precision/recall/F1, ASR |
| `results.json` | 메타정보와 전체 결과 |
| `run_log.md` | 제출 보고서에 붙일 수 있는 실행 로그 |

호스트 Python에 `scikit-learn`이나 uv를 설치하지 않았고, Docker 실행 결과를 기준으로 정량값을 확정했다.
