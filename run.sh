#!/bin/bash
. venv/bin/activate
pip install -r requirements.txt
export FLASK_APP=src/server.py
export FLASK_ENV=development
flask run