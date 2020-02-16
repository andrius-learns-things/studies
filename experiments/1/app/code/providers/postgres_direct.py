import psycopg2
from .base import Provider


class PostgresDirectProvider(Provider):
    def __init__(self):
        self.connection = psycopg2.connect(
            user="postgres",
            password="notverysecret",
            host="postgres",
            port="5432",
            database="postgres",
        )

    @property
    def name(self):
        return "Postgres direct"

    # Hit count experiment

    def get_hit_count(self):

        schema = "public"
        table = "hits"

        definition = "(ID SERIAL PRIMARY KEY, " "MSG TEXT NOT NULL)"

        self._ensure_table_exists(schema, table, definition)

        insert_query = "INSERT INTO {}.{}(MSG) VALUES ('ANOTHER HIT');"
        insert_query = insert_query.format(schema, table)

        self._sql_command(insert_query)

        select_query = ("SELECT COUNT(*) FROM {}.{};").format(schema, table)

        return self._sql_select_scalar(select_query)

    # Single entity experiment

    def ensure_empty_person_structure(self):
        pass

    def register_person(self, person):
        pass

    def search_persons(self, field, value):
        return []

    # Helpers

    def _ensure_table_exists(self, schema, table, definition):

        check_table_query = (
            "SELECT COUNT(*) FROM information_schema.tables "
            "WHERE table_schema = '{}' "
            "AND table_name = '{}';"
        ).format(schema, table)

        count = self._sql_select_scalar(check_table_query)

        if count == 0:

            create_table_query = ("CREATE TABLE {}.{} {};").format(
                schema, table, definition
            )

            self._sql_command(create_table_query)

    def _sql_select_scalar(self, command):
        cursor = self.connection.cursor()
        cursor.execute(command)
        return cursor.fetchone()[0]

    def _sql_command(self, command):
        cursor = self.connection.cursor()
        cursor.execute(command)
        self.connection.commit()
