FROM python:3.11-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /workspace

ENV UV_PROJECT_ENVIRONMENT=/opt/venv
ENV PATH="/opt/venv/bin:${PATH}"

COPY pyproject.toml /workspace/pyproject.toml
RUN uv sync --no-dev

CMD ["bash"]
