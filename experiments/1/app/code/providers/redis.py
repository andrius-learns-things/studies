from redis import Redis
from .base import Provider
from json import loads, dumps


class RedisProvider(Provider):
    def __init__(self):
        self.redis = Redis(host="redis", port=6379)

    @property
    def name(self):
        return "Redis"

    def get_hit_count(self):
        self.redis.incr("hits")
        return int(self.redis.get("hits"))

    def clear_persons(self):
        pass

    def register_person(self, person):
        self.redis.set(person["person_id"], dumps(person))

    def search_persons(self, field, value):

        results = []

        for key in self.redis.keys():
            p = loads(self.redis.get(key))
            if p[field] == value:
                results.append(p)

        return results
