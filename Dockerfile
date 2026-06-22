FROM nvidia/cuda:13.2.1-cudnn-devel-ubuntu24.04

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ENV DEBIAN_FRONTEND=noninteractive
ENV UV_PROJECT_ENVIRONMENT=/opt/venv
ENV UV_PYTHON_INSTALL_DIR=/opt/uv-python
ENV UV_LINK_MODE=copy
ENV PATH="/opt/venv/bin:${PATH}"

ENV NVIDIA_VISIBLE_DEVICES=all
ENV NVIDIA_DRIVER_CAPABILITIES=compute,utility

WORKDIR /workspace

RUN apt-get update && apt-get install -y --no-install-recommends \
    bash \
    ca-certificates \
    curl \
    git \
    build-essential \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

RUN uv python install 3.11

COPY pyproject.toml uv.lock /workspace/
RUN uv sync --frozen --no-dev --python 3.11

COPY . /workspace

CMD ["bash"]
