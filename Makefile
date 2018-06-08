start:
	export FLASK_APP=src/server.py
	export FLASK_ENV=development
	flask run

setup:
	git pull
	pip install -r requirements.txt