import psycopg2
from .base import Provider


SCHEMA = "public"


class PostgresDirectProvider(Provider):

    # Constructor

    def __init__(self):
        self.connection = psycopg2.connect(
            user="postgres",
            password="notverysecret",
            host="postgres",
            port="5432",
            database="postgres",
        )

    # Provider meta props

    @property
    def name(self):
        return "Postgres direct"

    # Hit count experiment

    def get_hit_count(self):

        table = "hits"

        definition = "(ID SERIAL PRIMARY KEY, " "MSG TEXT NOT NULL)"

        self._ensure_table_exists(SCHEMA, table, definition)

        insert_query = "INSERT INTO {}.{}(MSG) VALUES ('ANOTHER HIT');"
        insert_query = insert_query.format(SCHEMA, table)

        self._sql_command(insert_query)

        select_query = ("SELECT COUNT(*) FROM {}.{};").format(SCHEMA, table)

        return self._sql_select_scalar(select_query)

    # Single entity experiment

    def ensure_empty_person_structure(self):

        definition = (
            "(ID SERIAL PRIMARY KEY, "
            "PERSON_ID TEXT NOT NULL, "
            "FNAME TEXT NOT NULL, "
            "LNAME TEXT NOT NULL)"
        )

        self._ensure_table_exists(SCHEMA, "persons", definition)

        create_table_query = "DELETE FROM {}.{};".format(SCHEMA, "persons")
        self._sql_command(create_table_query)

        drop_index_query = "DROP INDEX IF EXISTS idx_persons_fname;"

        self._sql_command(drop_index_query)

    def register_person(self, person):
        insert_query = (
            "INSERT INTO {}.{}(PERSON_ID, FNAME, LNAME) " "VALUES ('{}', '{}', '{}');"
        )
        insert_query = insert_query.format(
            SCHEMA,
            "persons",
            person["person_id"],
            person["first_name"],
            person["last_name"],
        )

        self._sql_command(insert_query)

    def search_persons(self, field, value):

        fields_in_db = {
            "person_id": "PERSON_ID",
            "first_name": "FNAME",
            "last_name": "LNAME",
        }

        field_in_db = fields_in_db[field]

        select_query = ("SELECT * FROM {}.{} " "WHERE {}='{}';").format(
            SCHEMA, "persons", field_in_db, value
        )

        db_results = self._sql_select(select_query)

        results = [
            {"person_id": r[0], "first_name": r[1], "last_name": r[2]}
            for r in db_results
        ]
        return results

    def add_person_indexes(self):
        create_index_query = ("CREATE INDEX idx_persons_fname ON {}.{}({});").format(
            SCHEMA, "persons", "FNAME"
        )

        self._sql_command(create_index_query)

    # Single entity experiment - helpers

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

    def _sql_select(self, command):
        cursor = self.connection.cursor()
        cursor.execute(command)
        return cursor.fetchmany()

    def _sql_select_scalar(self, command):
        cursor = self.connection.cursor()
        cursor.execute(command)
        return cursor.fetchone()[0]

    def _sql_command(self, command):
        cursor = self.connection.cursor()
        cursor.execute(command)
        self.connection.commit()

    # Two entities experiment

    def ensure_empty_org_structures(self):
        pass

    def register_org(self, org, registration):
        pass

    def get_last_registered_orgs(self, subsystem):
        return []
