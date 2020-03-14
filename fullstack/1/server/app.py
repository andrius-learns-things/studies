from flask import Flask, jsonify
from events.event_store.mongo import MongoEventStore
from events.event_types import ADD_NEW_ITEM
from events.readmodels.postgres import PostgresReadModel
from cache.redis import RedisCacheProvider
from mq.rabbitmq import RabbitMQProvider
from worker import add_item_async


# App objects

app = Flask(__name__)
event_store = MongoEventStore()
read_model = PostgresReadModel(event_store)
cache = RedisCacheProvider()
queue = RabbitMQProvider()


# API endpoints


@app.route("/")
def overview():
    return "Hello world from Flask backend endpoint"


@app.route("/api/items", methods=["GET"])
def get_items():
    items = read_model.get_items()
    return jsonify(items)


@app.route("/api/items", methods=["POST"])
def add_item():
    event_store.register_new_event(ADD_NEW_ITEM, {"name": "Item"})
    items = read_model.get_items()
    return jsonify(items)


@app.route("/api/queued-items", methods=["POST"])
def add_item_to_queue():
    queue.post("Item in the queue")
    return jsonify(None)


@app.route("/api/add-items-from-queue", methods=["POST"])
def add_items_from_queue():

    items_in_queue = queue.get_all()

    for item in items_in_queue:
        event_store.register_new_event(ADD_NEW_ITEM, {"name": "Item added from queue"})

    items = read_model.get_items()
    return jsonify(items)


@app.route("/api/items-from-cache", methods=["GET"])
def get_items_from_cache():

    # Constants
    ITEM_CACHE_DURATION_IN_SEC = 10
    ITEM_CACHE_KEY = "items"

    items = cache.get(ITEM_CACHE_KEY)
    if not items:
        items = read_model.get_items()
        cache.set(ITEM_CACHE_KEY, items, ITEM_CACHE_DURATION_IN_SEC)
    return jsonify(items)


@app.route("/api/add-item-after-delay", methods=["POST"])
def add_item_after_delay():
    add_item_async.apply_async(countdown=10)
    return jsonify(None)


# Entrypoint

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
