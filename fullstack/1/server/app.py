from flask import Flask, jsonify

app = Flask(__name__)


items = [{"name": "A"}, {"name": "B"}]


@app.route("/")
def overview():
    return "Hello world from Flask backend endpoint"


@app.route("/api/items", methods=["GET"])
def get_items():
    return jsonify(items)


@app.route("/api/items", methods=["POST"])
def add_item():
    items.append({"name": "New"})
    return jsonify(items)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
