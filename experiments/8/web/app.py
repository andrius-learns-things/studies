from flask import Flask


app = Flask(__name__)


@app.route("/")
def empty():
    return "Empty endpoint"


@app.route("/first-endpoint")
def first_endpoint():
    return "First endpoint"


@app.route("/second-endpoint")
def second_endpoint():
    return "Second endpoint"
