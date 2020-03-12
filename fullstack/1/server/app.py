from flask import Flask, jsonify
from events.event_store.mongo import MongoEventStore
from events.event_types import ADD_NEW_ITEM
from events.readmodels.postgres import PostgresReadModel
from cache.redis import RedisCacheProvider


# App objects

app = Flask(__name__)
event_store = MongoEventStore()
read_model = PostgresReadModel(event_store)
cache = RedisCacheProvider()


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
    event_store.register_new_event(ADD_NEW_ITEM, {})
    items = read_model.get_items()
    return jsonify(items)


@app.route("/api/queued-items", methods=["POST"])
def add_item_to_queue():
    pass


@app.route("/api/add-tems-from-queue", methods=["POST"])
def add_item_from_quque():
    pass


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


# Entrypoint

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
