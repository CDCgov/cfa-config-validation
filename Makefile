COMMANDS = build run push-to-registry login test

.PHONY: $(COMMANDS)

AZURE_CR_NAME := cfaprdconfigvalidation
IMAGE_NAME = '$(AZURE_CR_NAME).azurecr.io/config-validation-service:latest'

build:
	docker-compose build --no-cache

run:
	docker-compose up

login:
	az login

push-to-registry: build
	az acr login --name $(AZURE_CR_NAME)
	docker push $(IMAGE_NAME)

test:
	poetry run pytest
