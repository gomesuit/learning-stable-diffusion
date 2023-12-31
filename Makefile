install:
	asdf plugin add python
	asdf install python $(cat .tool-versions)
	asdf exec pip install poetry

init:
	asdf exec poetry install

sample_1:
	asdf exec poetry run python sample.py

sample_2:
	asdf exec poetry run python sample_2.py