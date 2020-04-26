from flask import Flask

app = Flask(__name__)


@app.route("/")
def empty():
    return "Empty endpoint"


@app.route("/use-and-release-1kb")
def use_and_release_one_kb():
    return "Endpoint, which uses and releases 1KB of memory"
