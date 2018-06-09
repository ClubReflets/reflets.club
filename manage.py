from flask_script import Manager
from src import app, db

manager = Manager(app)


# Set the commands to be executed with manager
# Ex. python manage.py createdb
@manager.command
def create_db():
    db.reflect()
    db.drop_all()
    db.create_all()
