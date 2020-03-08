from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


TABLE_NAME_ITEMS = "items"
TABLE_NAME_INDEX = "index"


Base = declarative_base()


class Items(Base):
    __tablename__ = TABLE_NAME_ITEMS

    id = Column(Integer, primary_key=True)
    name = Column(String)


class Index(Base):
    __tablename__ = TABLE_NAME_INDEX

    id = Column(Integer, primary_key=True)
    index = Column(Integer)


def get_engine():

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

    return create_engine(db_link, echo=True)


def ensure_db_created(engine):

    has_tables = [
        engine.dialect.has_table(engine, TABLE_NAME_ITEMS),
        engine.dialect.has_table(engine, TABLE_NAME_INDEX),
    ]

    if not all(has_tables):
        Base.metadata.create_all(engine)


def get_index(engine):

    Session = sessionmaker(bind=engine)
    session = Session()

    indexes = session.query(Index).all()

    return indexes[0].index if indexes else 0


def ensure_read_model_is_up_to_date():

    engine = get_engine()
    ensure_db_created(engine)
    index = get_index(engine)

    return index
