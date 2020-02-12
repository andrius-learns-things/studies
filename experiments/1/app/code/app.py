from flask import Flask
from providers.redis import (
    get_hit_count as get_redis_hit_count
)
from providers.mongo import (
    get_hit_count as get_mongo_hit_count
)


app = Flask(__name__)


@app.route('/')
def overview():
    return ' | '.join([
        "Redis hit count: {}".format(get_redis_hit_count()),
        "Mongo hit count: {}".format(get_mongo_hit_count())
    ])


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
