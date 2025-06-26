# ======= Этап сборки =======
FROM python:3.12-slim AS builder

# Установка зависимостей для компиляции
RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*

# Создание виртуального окружения
RUN python -m venv /venv

# Копирование poetry.lock и pyproject.toml
WORKDIR /app
COPY pyproject.toml poetry.lock ./

# Установка Poetry
RUN pip install poetry

# Установка зависимостей
RUN . /venv/bin/activate && poetry install --no-dev

# Копирование исходников проекта
COPY src/ ./src

# ======= Этап финального образа =======
FROM python:3.12-slim

WORKDIR /app

# Копируем виртуальное окружение из билдер-этапа
COPY --from=builder /venv /venv

# Копируем исходники
COPY src/ ./src

# Настройка окружения
ENV PATH="/venv/bin:$PATH"
ENV PYTHONPATH=/app/src

# Открываем порт приложения
EXPOSE 8000

# Запуск приложения через Uvicorn
CMD ["uvicorn", "ooc.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
