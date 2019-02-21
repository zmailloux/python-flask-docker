CONTAINER_NAME=python-flask-docker
IMAGE_NAME=python-flask-docker
DOCKER_REPO=gcr.io/es-devops-d

.PHONY: build
build:
	docker build -t $(CONTAINER_NAME) .

tag-latest:
	@echo 'create tag latest'
	docker tag $(CONTAINER_NAME) $(DOCKER_REPO)/$(IMAGE_NAME):latest2

publish: tag-latest
	@echo 'publish latest to $(DOCKER_REPO)'
	docker push $(DOCKER_REPO)/$(IMAGE_NAME):latest2