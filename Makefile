setup:
	python3 -m venv venv
	. venv/bin/activate; pip install -r requirements.txt

# Run the Flask application.
run:
	FLASK_APP=app.py FLASK_ENV=development flask run

# Build the Docker image.
docker-build:
	docker build -t iris_model_app .

# Run the Docker container.
docker-run:
	docker run -p 4000:80 iris_model_app