install:
	@poetry install

lint:
	@poetry run black .
	@poetry run isort .

format:
	@poetry run prospector .

sec:
	@pip-audit