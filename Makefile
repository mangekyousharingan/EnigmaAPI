SERVICE_NAME=enigma
MY_DOCKER_NAME=$(SERVICE_NAME)
USERNAME=mangekyou
TAG=$(USERNAME)/$(MY_DOCKER_NAME)

.PHONY:
	test
.DEFAULT_GOAL := test

test:
	python -m pytest -v

docker_build:
	docker build -t $(MY_DOCKER_NAME) .

docker_run:
	docker run --name enigma_app -p 5000:5000 -d $(MY_DOCKER_NAME)

docker_push: docker_build
	@docker login --username $(USERNAME) --password $${DOCKER_PASSWORD};
	docker tag $(MY_DOCKER_NAME) $(TAG);
	docker push $(TAG);
	docker logout;
