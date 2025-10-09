run:
	python App.py

test:
	pytest -v --maxfail=1 --disable-warnings

coverage:
	coverage run -m pytest
	coverage report -m
