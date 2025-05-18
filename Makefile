install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
test:
	python -m pytest -vv --cov=CalCLI --cov=mylib test_*.py
format:
	black *.py mylib/*.py
lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py mylib/*.py
container:
	docker run -rm -i hadolint/hadolint < Dockerfile
refactor: format lint

deploy:
#echo "deploying not implemented"

all: install lint test format deploy
	