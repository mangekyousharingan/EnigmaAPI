SERVICE_NAME=enigma
HEROKU_APP_NAME=invulnerable-baguette-19588
MY_DOCKER_NAME=$(SERVICE_NAME)
USERNAME=mangekyou
TAG=$(USERNAME)/$(MY_DOCKER_NAME)

.PHONY:
	test
.DEFAULT_GOAL := test

test:
	python -m pytest -v

lint:
	flake8 --ignore=E501,E999 common test

docker_build:
	docker build -t $(MY_DOCKER_NAME) .

docker_run:
	docker run --name enigma_app -p 5000:5000 -d $(MY_DOCKER_NAME)

docker_push: docker_build
	@docker login --username $(USERNAME) --password $${DOCKER_PASSWORD};
	docker tag $(MY_DOCKER_NAME) $(TAG);
	docker push $(TAG);
	docker logout;

heroku_deploy:
	wget -qO- https://toolbelt.heroku.com/install-ubuntu.sh | sh
	heroku plugins:install @heroku-cli/plugin-container-registry
	docker login --username _ --password=$${HEROKU_API_KEY} registry.heroku.com
	heroku container:push web --app $(HEROKU_APP_NAME)
	heroku container:release web --app $(HEROKU_APP_NAME)
