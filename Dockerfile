FROM ghcr.io/astral-sh/uv:0.13.0-python3.14-trixie-slim

RUN groupadd --system --gid 999 app \
    && useradd --system --gid 999 --uid 999 --create-home app

WORKDIR /app

ENV PATH="/app/.venv/bin:$PATH" \
    PORT=8080 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy

COPY pyproject.toml uv.lock README.md ./
COPY src ./src

RUN uv sync --locked --no-dev --no-editable

USER app

EXPOSE 8080

CMD ["sh", "-c", "uvicorn legalization_consulting.main:app --host 0.0.0.0 --port ${PORT} --proxy-headers --forwarded-allow-ips=*"]
