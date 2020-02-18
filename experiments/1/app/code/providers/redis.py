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
        if field == "first_name" and self.fn_index_exists:
            return self._search_persons_by_index(field, value)
        else:
            return self._search_persons_by_values(field, value)

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

        self.fn_index_exists = True

    # Single entity experiment - helpers

    def _search_persons_by_index(self, field, value):
        index_key = PERSON_FN_INDEX_KEY_FORMAT.format(value)
        index_val = self.redis.get(index_key)
        return loads(index_val) if index_val else []

    def _search_persons_by_values(self, field, value):

        results = []

        if len(self.all_person_ids) >= 10000:
            raise Exception("Too much")

        for p_id in self.all_person_ids:
            key = PERSON_VALUES_KEY_FORMAT.format(p_id)
            p = loads(self.redis.get(key))
            if p[field] == value:
                results.append(p)

        return results

    @property
    def all_person_ids(self):
        ids = self.redis.get("all_person_ids")
        return loads(ids) if ids else []

    @all_person_ids.setter
    def all_person_ids(self, ids):
        self.redis.set("all_person_ids", dumps(ids))

    @property
    def fn_index_exists(self):
        val = self.redis.get("fn_index_exists")
        return loads(val) if val else False

    @fn_index_exists.setter
    def fn_index_exists(self, value):
        self.redis.set("fn_index_exists", dumps(value))

    # Two entities experiment

    def ensure_empty_org_structures(self):
        pass

    def register_org(self, org, registration):
        pass

    def get_last_registered_orgs(self, subsystem):
        return []
