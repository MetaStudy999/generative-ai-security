# W03 Docker 보조 폴더

현재 실행 환경은 상위 폴더의 `Dockerfile`과 `docker-compose.yml`을 기준으로 한다. 추가 Docker 스크립트나 컨테이너 설정이 필요해지면 이 폴더에 보관한다.

## 현재 실행 명령

```bash
docker build -t w03-aisec .
docker run --rm -it -v $(pwd):/workspace w03-aisec bash
python src/run_experiment.py --config configs/config.yaml
```

로컬 점검은 `python3 src/run_experiment.py --config configs/config.yaml`로도 가능하며, 제출 수치는 `outputs/run_log.md`와 CSV/JSON 결과 파일을 기준으로 한다.
