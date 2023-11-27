run:
	@poetry run env $(shell grep -v ^\# .env | xargs) python main.py
