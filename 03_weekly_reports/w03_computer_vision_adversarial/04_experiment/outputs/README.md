# W03 실험 출력 폴더

`src/run_experiment.py`를 실행해 다음 파일을 생성했다.

| 파일 | 내용 |
|---|---|
| `metrics_summary.csv` | 조건별 accuracy, macro precision/recall/F1, ASR, robust drop |
| `results.json` | 메타정보, 조건별 전체 결과, 예시 입력 배열 |
| `run_log.md` | 제출 보고서에 붙일 수 있는 실행 로그 |
| `clean_example.pgm` | synthetic clean 예시 이미지 |
| `adversarial_eps_0_30.pgm` | epsilon 0.30 toy adversarial 예시 이미지 |
| `feature_squeezed_eps_0_30.pgm` | feature squeezing 적용 예시 이미지 |

정량값은 이 폴더의 CSV/JSON/Markdown 로그가 서로 일치하는 경우에만 보고서에 확정값으로 반영한다.
