# EnigmaAPI
Simple API to encode and decode text.

Technology stack:

- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Docker](https://www.docker.com/)
- [Travis CI](https://travis-ci.org/)
- [Heroku](https://www.heroku.com/)


## Base URL:

https://invulnerable-baguette-19588.herokuapp.com

## API Specification:
[Swagger](https://app.swaggerhub.com/apis/swdowiarz/EnigmaAPI/1.0.0)
 
 
## Deploy:

To deploy application:
1. Clone project repository to your local machine
2. Make sure you have Docker and Heroku CLI pre installed.
3. In your terminal go within project directory.
4. Run the following command: **_make docker_push_**. It will create docker image and push it to the docker hub.
5. Once the previous step is done run: make _**heroku_deploy**_ which will deploy docker to live servers on Heroku.