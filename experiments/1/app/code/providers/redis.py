from redis import Redis
from .base import Provider


class RedisProvider(Provider):
    def __init__(self):
        self.redis = Redis(host="redis", port=6379)

    @property
    def name(self):
        return "Redis"

    def get_hit_count(self):
        self.redis.incr("hits")
        return int(self.redis.get("hits"))
