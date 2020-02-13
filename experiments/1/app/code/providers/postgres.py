import psycopg2
from .base import Provider


class PostgresProvider(Provider):

    def __init__(self):
        self.connection = psycopg2.connect(
            user="postgres",
            password="notverysecret",
            host="postgres",
            port="5432",
            database="postgres"
        )

    @property
    def name(self):
        return "Postgres"

    def get_hit_count(self):

        schema = "public"
        table = "hits"

        definition = (
            "(ID SERIAL PRIMARY KEY, "
            "MSG TEXT NOT NULL)"
        )

        self._ensure_table_exists(schema, table, definition)

        insert_query = (
            "INSERT INTO {}.{}(MSG) "
            "VALUES ('ANOTHER HIT');"
        ).format(schema, table)

        self._exec(insert_query)

        select_query = (
            "SELECT COUNT(*) FROM {}.{};"
        ).format(schema, table)

        return self._exec(select_query)

    def _ensure_table_exists(self, schema, table, definition):

        check_table_query = (
            "SELECT EXISTS ( "
            "SELECT FROM information_schema.tables "
            "WHERE table_schema = '{}' "
            "AND table_name = '{}' "
            ");"
        ).format(schema, table)

        exists = self._exec(check_table_query)

        if not exists:

            create_table_query = (
                "CREATE TABLE {}.{} {};"
            ).format(schema, table, definition)

            self._exec(create_table_query)

    def _exec(self, command):
        cursor = self.connection.cursor()
        cursor.execute(command)
        return cursor.fetchone()
