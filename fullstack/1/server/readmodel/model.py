from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Items(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String)


class Index(Base):
    __tablename__ = "index"

    id = Column(Integer, primary_key=True)
    index = Column(Integer)


def setup_db():

    db_params = {
        "host": "postgres",
        "port": 5432,
        "database": "postgres",
        "user": "postgres",
        "password": "notverysecret",
    }

    db_link = "postgresql://{}:{}@{}:{}/{}".format(
        db_params["user"],
        db_params["password"],
        db_params["host"],
        db_params["port"],
        db_params["database"],
    )

    engine = create_engine(db_link, echo=True)

    Base.metadata.create_all(engine)
