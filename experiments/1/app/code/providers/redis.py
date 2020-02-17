from redis import Redis
from .base import Provider
from json import loads, dumps


PERSON_VALUES_KEY_FORMAT = "P_{}"
PERSON_FN_INDEX_KEY_FORMAT = "PI_{}"


class RedisProvider(Provider):

    # Constructor

    def __init__(self):
        self.redis = Redis(host="redis", port=6379)

    # Provider meta props

    @property
    def name(self):
        return "Redis"

    # Hit count experiment

    def get_hit_count(self):
        self.redis.incr("hits")
        return int(self.redis.get("hits"))

    # Single entity experiment

    def ensure_empty_person_structure(self):
        self.redis.flushdb()

    def register_person(self, person):
        self.all_person_ids = self.all_person_ids + [person["person_id"]]
        self.redis.set(
            PERSON_VALUES_KEY_FORMAT.format(person["person_id"]), dumps(person)
        )

    def search_persons(self, field, value):

        results = []

        for p_id in self.all_person_ids:
            key = PERSON_VALUES_KEY_FORMAT.format(p_id)
            p = loads(self.redis.get(key))
            if p[field] == value:
                results.append(p)

        return results

    def add_person_indexes(self):

        for p_id in self.all_person_ids:
            key = PERSON_VALUES_KEY_FORMAT.format(p_id)
            p = loads(self.redis.get(key))

            first_name = p["first_name"]

            index_key = PERSON_FN_INDEX_KEY_FORMAT.format(first_name)
            index_val = self.redis.get(index_key)
            index_val = loads(index_val) if index_val else []

            index_val.append(p)

            self.redis.set(index_key, dumps(index_val))

    # Single entity experiment - helpers

    @property
    def all_person_ids(self):
        ids = self.redis.get("all_person_ids")
        return loads(ids) if ids else []

    @all_person_ids.setter
    def all_person_ids(self, ids):
        self.redis.set("all_person_ids", dumps(ids))
