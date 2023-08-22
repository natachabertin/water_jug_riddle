.PHONY: *

build:
	docker compose up --build -d

run:
	docker compose up -d

stop:
	docker compose stop

docker-rm-container:
	docker container rm -f fastapi-app

docker-bash:
	docker exec -it fastapi-app bash

test:
	pytest -v --cov=.

test-unit:
	pytest -v tests/unit --cov=.

test-int:
	pytest -v tests/integration

test-missing:
	pytest --cov=. --cov-report term-missing

test-cov80:
	pytest --cov=. --cov-fail-under=80

cli:
	python app/cli.py

precommit:
	pre-commit run --all-files --show-diff-on-failure
