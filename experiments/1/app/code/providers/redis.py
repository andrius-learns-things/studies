from redis import Redis


redis = Redis(host="redis", port=6379)


def get_hit_count():
    redis.incr('hits')
    return int(redis.get('hits'))
