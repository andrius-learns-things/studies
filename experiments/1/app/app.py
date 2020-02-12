from flask import Flask
from redis import Redis


REDIS_HOST = "redis"
REDIS_PORT = 6379


app = Flask(__name__)
redis = Redis(host=REDIS_HOST, port=REDIS_PORT)


@app.route('/')
def hello():
    redis.incr('hits')
    hits = int(redis.get('hits'))
    return 'Redis hit counter: {}'.format(str(hits))


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
