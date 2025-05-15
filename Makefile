install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
test:
	pytest -m pytest -vv --cov=hello test_*.py
format:
	black *.py
lint:
	pylint --disable=R,C --ignore-patterns=test_.*?.py *.py
container:
	docker run -rm -i hadolint/hadolint < Dockerfile
refactor: format lint

deploy:
#echo "deploying not implemented"

all: install lint test format deploy
	