# W02 Docker 보조 폴더

현재 실행 환경은 상위 폴더의 `Dockerfile`과 `docker-compose.yml`을 기준으로 한다. 추가 Docker 스크립트가 필요해지면 이 폴더에 보관한다.

## 현재 실행 명령

```bash
docker build -t w02-aisec .
docker run --rm -it -v $(pwd):/workspace w02-aisec bash
python src/run_experiment.py --config configs/config.yaml
```
