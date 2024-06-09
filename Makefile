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

setup:
	install build package-install
dell:
	pip uninstall hexlet-code

make check:
	poetry run pytest --cov=gendiff --cov-report xml


