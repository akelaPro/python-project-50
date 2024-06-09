install:	
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 gendiff

dell:
	pip uninstall hexlet-code

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

pytest:
	poetry run pytest

selfcheck:
  poetry check

check: selfcheck test lint


