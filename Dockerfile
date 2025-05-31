## ----- Builder Stage ----- ## 

FROM python:3.13.4-slim-bookworm AS builder

RUN apt-get update && apt-get install --no-install-recommends -y \
        build-essential \
        wget && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install uv:
ADD https://astral.sh/uv/install.sh /install.sh
RUN chmod -R 655 /install.sh && /install.sh

# Set up the UV environment path correctly:
ENV PATH="/root/.local/bin:${PATH}"

# Install the Python package and it's dependencies:
WORKDIR /app
ADD . .
RUN uv sync --extra prod && uv pip install .


## ----- Production Stage ----- ##

FROM python:3.13.4-slim-bookworm AS production

ENV APP_USER=glendza

# Create a non-root user for the application:
RUN useradd --create-home ${APP_USER}

# Create necessary directories and set permissions:
RUN mkdir -p /app/db /app/static /app/media /app/logs && \
    chown -R "$APP_USER":"$APP_USER" /app/db /app/static /app/media /app/logs

WORKDIR /app

COPY --from=builder /app/.venv .venv

# Add the virtual environment to PATH so Python packages can be found:
ENV PATH="/app/.venv/bin:$PATH"

# Copy the entrypoint script:
COPY entrypoint.sh "/app/entrypoint.sh"
RUN chmod +x "/app/entrypoint.sh"

USER $APP_USER

ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["gunicorn", "glendza.web_app.wsgi:application", "--bind", ":8000", "--workers", "4", "--timeout", "300"]
