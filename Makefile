.PHONY: build run compose verify

build:
	docker build -t aisec-uv-cuda132 .

run:
	docker run --rm -it --gpus all -v "$$PWD":/workspace aisec-uv-cuda132

compose:
	docker compose run --rm aisec

verify:
	docker run --rm -it --gpus all -v "$$PWD":/workspace aisec-uv-cuda132 python scripts/verify_gpu.py
