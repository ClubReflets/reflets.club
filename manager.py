from flask_script import Manager
from sqlalchemy import exc
from src import app, db

manager = Manager(app)


@manager.command
def init():
    print('Initiating database...')
    db.reflect()
    db.drop_all()
    db.create_all()
    print('Init done.')


@manager.command
def seed():
    from src.models import User
    admin = User(email='reflets@etsmtl.net', password='123123')
    try:
        db.session.add(admin)
        db.session.commit()
        print('Seed done.')
    except exc.SQLAlchemyError as e:
        print(e)
        db.session.rollback()


if __name__ == "__main__":
    manager.run()