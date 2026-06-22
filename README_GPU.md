# GPU 연구환경 안내

## 목적

이 환경은 `uv + Docker + NVIDIA GPU + CUDA 13.2 + Python 3.11` 기반의 재현 가능한 AI/ML 연구 실행환경을 제공한다. 기존 주차별 실험 폴더는 보존하고, GPU가 필요한 경우 루트 공통 환경을 사용하도록 구성했다.

## 구성 파일

- `Dockerfile`: `nvidia/cuda:13.2.1-cudnn-devel-ubuntu24.04` 기반 이미지
- `pyproject.toml`: Python 3.11 고정 및 공통 연구 의존성
- `uv.lock`: `uv lock --python 3.11`로 생성한 잠금 파일
- `docker-compose.yml`: `aisec` 서비스와 `gpus: all` 설정
- `.dockerignore`: Docker build context 제외 목록
- `scripts/verify_gpu.py`: 컨테이너 내부 GPU/PyTorch CUDA 검증 스크립트
- `Makefile`: build/run/compose/verify 명령 단축

## 호스트 전제조건

- NVIDIA Driver 설치
- NVIDIA Container Toolkit 설치
- Docker Engine 및 Docker Compose 설치
- `docker run --gpus all ...` 명령이 호스트에서 동작해야 함
- 현재 사용자가 Docker 데몬(`/var/run/docker.sock`)에 접근할 수 있어야 함

## 빌드

```bash
docker build -t aisec-uv-cuda132 .
```

또는:

```bash
make build
```

## 실행

```bash
docker run --rm -it --gpus all -v "$PWD":/workspace aisec-uv-cuda132
```

또는:

```bash
make run
```

## Docker Compose 실행

```bash
docker compose run --rm aisec
```

또는:

```bash
make compose
```

## 컨테이너 안에서 확인할 명령

```bash
python --version
nvidia-smi
python scripts/verify_gpu.py
```

## 한 번에 검증

```bash
docker run --rm -it --gpus all -v "$PWD":/workspace aisec-uv-cuda132 python scripts/verify_gpu.py
```

또는:

```bash
make verify
```

## PyTorch CUDA 13.2 설정

2026-06-22 KST 기준으로 공식 PyTorch wheel 인덱스 `https://download.pytorch.org/whl/cu132`에서 Python 3.11 Linux용 stable CUDA 13.2 wheel 항목을 확인했다. 따라서 nightly/test 인덱스가 아니라 stable `cu132` 인덱스를 사용한다.

현재 고정한 주요 패키지는 다음과 같다.

- `torch==2.12.1+cu132`
- `torchvision==0.27.1+cu132`

`torchaudio`는 같은 `cu132` 경로에서 CUDA 13.2 wheel을 확인하지 못했으므로 루트 공통 의존성에 포함하지 않았다. 오디오 실험에 `torchaudio`가 필요하면 공식 PyTorch 인덱스에서 CUDA 13.2 wheel 존재 여부를 다시 확인한 뒤 추가한다.

## 재현성 메모

- Python은 `requires-python = ">=3.11,<3.12"`로 고정한다.
- Dockerfile은 `uv python install 3.11` 후 `/opt/venv`에 가상환경을 만든다.
- `uv.lock`이 있으므로 Docker build에서는 `uv sync --frozen --no-dev --python 3.11`을 사용한다.
- lock 파일을 갱신할 때는 `uv lock --python 3.11`을 실행한 뒤 `docker build`로 다시 검증한다.

## 현재 환경에서 확인한 제한

이 작업을 수행한 Codex 실행 환경에서는 다음 제한이 있었다.

- `docker manifest inspect nvidia/cuda:13.2.1-cudnn-devel-ubuntu24.04`로 베이스 이미지 manifest는 확인했다.
- `uv.lock`은 임시 가상환경에 설치한 `uv 0.11.23`으로 생성했다.
- Docker 데몬 접근은 `/var/run/docker.sock` 권한 문제로 실패했다.
- 호스트 `nvidia-smi`는 `GPU access blocked by the operating system` 오류로 실패했다.

따라서 이 환경 안에서는 실제 `docker build`, `docker run --gpus all`, 컨테이너 내부 `nvidia-smi`, PyTorch CUDA tensor 연산까지는 완료했다고 기록하지 않는다. 위 전제조건을 만족하는 GPU 호스트에서 다시 검증해야 한다.

## 실패 시 대안

- Docker 데몬 권한 오류가 나면 현재 사용자를 Docker 그룹에 추가하거나 권한이 있는 계정에서 실행한다.
- `nvidia-smi`가 컨테이너 안에서 실패하면 NVIDIA Driver와 NVIDIA Container Toolkit 설치 상태를 먼저 확인한다.
- CUDA 13.2 wheel 또는 베이스 이미지가 특정 호스트에서 안정적으로 동작하지 않으면 CUDA 12.8 계열 PyTorch stable 환경으로 낮추는 방안을 우선 검토한다.
