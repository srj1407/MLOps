FROM python:3.12-slim

WORKDIR /app

# Install dependencies into the project's .venv from the locked uv configuration.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
COPY pyproject.toml uv.lock .python-version ./
RUN uv sync --locked --no-install-project

COPY . .

ENV PATH="/app/.venv/bin:$PATH" \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

EXPOSE 5000

CMD ["python", "app.py"]
