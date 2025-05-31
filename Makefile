.PHONY:  lint docker-run docker-build sync mm migrate sm smu su cs cc format

include .env
export $(shell sed 's/=.*//' .env)

DOCKER_DEV_TAG = glendza

lint:
	@ruff check --fix

format:
	@ruff check  --select I --fix && ruff format

cc:
	@find . -name \*.pyc -delete

docker-run:
	@docker run --network host --env-file .env ${DOCKER_DEV_TAG}:latest

docker-build:
	@docker build -t ${DOCKER_DEV_TAG}:latest .

sync:
	@uv sync \
		--extra dev \
		--extra prod

# Django management commands:
mm:
	@gmanage makemigrations

migrate:
	@gmanage migrate

sm:
	@gmanage showmigrations

smu:
	@gmanage showmigrations | grep '\[ \]\|^[a-z]' | grep '[  ]' -B 1 || true

su:
	@gmanage createsuperuser

cs:
	@gmanage collectstatic
