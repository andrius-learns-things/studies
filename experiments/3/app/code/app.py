from flask import Flask


app = Flask(__name__)


@app.route("/")
def overview():
    output = "Minimal Flask app"
    return output


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
