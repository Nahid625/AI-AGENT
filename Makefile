.PHONY: verify lint format format-check test

verify: lint format-check test

lint:
	ruff check .

format:
	ruff format .

format-check:
	ruff format --check .

test:
	pytest
