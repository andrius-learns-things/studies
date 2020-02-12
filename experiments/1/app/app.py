from flask import Flask
from redis import Redis
from pymongo import MongoClient


REDIS_HOST = "redis"
REDIS_PORT = 6379


MONGO_HOST = "mongo"


app = Flask(__name__)


redis = Redis(host=REDIS_HOST, port=REDIS_PORT)


client = MongoClient(
    MONGO_HOST,
    27017)
mongodb = client.hits_db


@app.route('/')
def hello():
    redis.incr('hits')
    hits_redis = int(redis.get('hits'))

    item_doc = {
        'hit': 'yes?'
    }
    mongodb.hits_db.insert_one(item_doc)

    items = [item for item in mongodb.hits_db.find()]

    hits_mongo = len(items)

    print('Contents: {}'.format([mongodb.hits_db.find()]))

    return 'Redis hit counter: {}, Mongo hit counter: {}'.format(
        str(hits_redis),
        str(hits_mongo)
    )


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
