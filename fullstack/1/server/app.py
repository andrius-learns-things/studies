from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def overview():
    return "Hello world from Flask backend endpoint"


@app.route("/api/items")
def get_items():
    result = [{"name": "A"}, {"name": "B"}]
    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
