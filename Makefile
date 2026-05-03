.PHONY: install install-dev run test lint format pre-commit clean

install:
	pip install -e .

install-dev:
	pip install -e ".[dev]"
	pre-commit install

run:
	python -m noctua

test:
	pytest tests/

lint:
	ruff check .

format:
	ruff format .

pre-commit:
	pre-commit run --all-files

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete