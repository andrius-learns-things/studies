from flask import Flask, jsonify
from events.event_store.mongo import MongoEventStore
from events.event_types import ADD_NEW_ITEM
from events.readmodels.postgres import PostgresReadModel

app = Flask(__name__)

event_store = MongoEventStore()
read_model = PostgresReadModel(event_store)


items = [{"name": "A"}, {"name": "B"}]


@app.route("/")
def overview():
    return "Hello world from Flask backend endpoint"


@app.route("/api/items", methods=["GET"])
def get_items():

    read_model.update()
    return jsonify(items)


@app.route("/api/items", methods=["POST"])
def add_item():

    event_store.register_new_event(ADD_NEW_ITEM, {})
    read_model.update()

    items.append({"name": "New"})
    return jsonify(items)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
