from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from ..event_types import ADD_NEW_ITEM


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


class PostgresReadModel:

    # Constructor

    def __init__(self, event_store):
        self._event_store = event_store

    # Read model methods

    def get_items(self):
        engine = self._get_engine()
        self._ensure_updated(engine)

        Session = sessionmaker(bind=engine)
        session = Session()

        rows = session.query(Items).all()

        items = [{"name": r.name} for r in rows]

        return items

    # Helper methods

    def _get_engine(self):

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

    def _ensure_db_created(self, engine):

        has_tables = [
            engine.dialect.has_table(engine, TABLE_NAME_ITEMS),
            engine.dialect.has_table(engine, TABLE_NAME_INDEX),
        ]

        if not all(has_tables):
            Base.metadata.create_all(engine)

    def _get_index(self, engine):

        Session = sessionmaker(bind=engine)
        session = Session()

        indexes = session.query(Index).all()

        return indexes[0].index if indexes else 0

    def _ensure_updated(self, engine):

        self._ensure_db_created(engine)
        index = self._get_index(engine)

        new_events = self._event_store.get_events(index)

        event_handlers = self._get_event_handlers()

        for event in new_events:

            handler = event_handlers.get(event.type)

            if handler:
                handler(engine, event)

    def _get_event_handlers(self):
        return {ADD_NEW_ITEM: self._handle_add_new_item}

    def _handle_add_new_item(self, engine, event):
        Session = sessionmaker(bind=engine)
        session = Session()

        new_item = Items(name="New one")

        session.add(new_item)
        session.commit()
