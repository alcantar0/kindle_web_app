FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1
ENV POETRY_HOME="/opt/poetry"
ENV PATH="$POETRY_HOME/bin:$PATH"

WORKDIR /app

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl build-essential \
    && rm -rf /var/lib/apt/lists/*

# Instalar Poetry via curl
RUN curl -sSL https://install.python-poetry.org | python3 -

# Desabilitar virtualenvs dentro do container
RUN poetry config virtualenvs.create false

# Copiar apenas as config do Poetry primeiro (melhor cache)
COPY pyproject.toml poetry.lock* ./

# Instalar dependências
RUN poetry install --no-root --no-interaction --no-ansi

# Copiar o restante do projeto
COPY . .

EXPOSE 8080

# Start do Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]