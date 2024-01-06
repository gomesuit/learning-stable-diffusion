install:
	mise install python@$(cat .tool-versions)
	pip install poetry

init:
	poetry install

sample_1:
	poetry run python sample.py

sample_2:
	poetry run python sample_2.py