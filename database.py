import sqlalchemy
#from flask import Flask
#from flask_sqlalchemy import sqlalchemy
#from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.orm import declarative_base, sessionmaker


__all__ = [
    'create_viewed_users_table',
    'insert_viewed_user_data',
    'select_viewed_user'
]


Base = declarative_base()

class NoticedUsers(Base):
    __tablename__ = "viewed_users"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    vk_id = sqlalchemy.Column(sqlalchemy.Integer, unique=False)
    viewed_user_id = sqlalchemy.Column(sqlalchemy.Integer, unique=False)


DSN = "sqlite:///viewed_users.db"
engine = sqlalchemy.create_engine(DSN)
Session = sessionmaker(bind=engine)
session = Session()


def create_viewed_users_table():
    global engine
    Base.metadata.create_all(engine)


def insert_viewed_user_data(vk_id, viewed_user_id):
    viewed_user = NoticedUsers(vk_id=vk_id, viewed_user_id=viewed_user_id)
    session.add(viewed_user)
    session.commit()


def select_viewed_user(vk_id, viewed_user_id):
    result = session.query(NoticedUsers).filter(NoticedUsers.vk_id == vk_id, NoticedUsers.viewed_user_id == viewed_user_id).first()
    session.close()
    return result
