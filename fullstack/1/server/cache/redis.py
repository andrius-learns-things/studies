from redis import Redis
from .base import BaseCacheProvider
from json import loads, dumps


class RedisCacheProvider(BaseCacheProvider):

    # Constructor

    def __init__(self):
        self.redis = Redis(host="redis", port=6379)

    # Cacher methods

    def get(self, key):
        value = self.redis.get(key)
        return loads(value) if value else None

    def set(self, key, value, expire_in_seconds=None):
        self.redis.set(key, dumps(value), ex=expire_in_seconds)
