import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.db.postgresql.models import Base
engine = create_engine(os.environ['POSTGRESQL_URL'])
session_maker = sessionmaker(bind=engine)


def init_postgresql():
    Base.metadata.create_all(engine)