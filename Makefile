VERSION: 1.0
AUTHOR: NamND

build-docker-images:
	docker build -t sentiment-analysis/python:v2 .

project-setup:
	pip install -r requirements.txt

export:
	export FLASK_APP=app.py

run:
	flask run -p 5005

run-docker:
	docker-compose up