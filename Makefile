.PHONY: all setup build test quality-check docker-build docker-push

all: setup test quality-check docker-build docker-push

setup:
	@echo "Setting up environment..."
	pip install -r requirements.txt

build:
	@echo "Building Docker image..."
	docker build -t flask-app .

test:
	@echo "Running unit tests..."
	python -m unittest

quality-check:
	@echo "Checking code quality..."
	flake8 .

docker-build:
	@echo "Building Docker image..."
	docker build -t flask-app .

docker-push:
	@echo "Pushing Docker image to Docker Hub..."
	docker tag flask-app <your_dockerhub_username>/flask-app
	docker push <your_dockerhub_username>/flask-app
