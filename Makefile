# ======== Переменные =========
POETRY = poetry
PYTHON = poetry run python
UVICORN = poetry run uvicorn
PYTEST = poetry run pytest
BLACK = poetry run black
RUFF = poetry run ruff

# ======== Команды проекта ========

install:
	$(POETRY) install

run-server:
	PYTHONPATH=src $(UVICORN) ooc.api.main:app --reload --host 0.0.0.0 --port 8000

test:
	$(PYTEST)

simulate:
	PYTHONPATH=src poetry run python src/ooc/scripts/simulate_life.py

format:
	$(BLACK) src tests

lint:
	$(RUFF) src tests

update:
	$(POETRY) update

lock:
	$(POETRY) lock

# ======== Утилиты ========

clean-pyc:
	find . -name "*.pyc" -delete
	find . -name "*.pyo" -delete
	find . -name "__pycache__" -delete

clean:
	rm -rf dist build *.egg-info .pytest_cache .mypy_cache .ruff_cache

