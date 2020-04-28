from flask import Flask

app = Flask(__name__)

ONE_KB_STRING = "__________".replace("_", "----------").replace("-", "__________")


@app.route("/")
def empty():
    return "Empty endpoint"


@app.route("/use-and-release-1kb")
def use_and_release_one_kb():
    a = ONE_KB_STRING + ""
    return "Endpoint, which uses and releases 1KB of memory. {}".format(len(a))


leaked = []


@app.route("/use-and-leak-1kb")
def use_and_leak_one_kb():
    a = ONE_KB_STRING + ""
    leaked.append(a)
    return "Endpoint, which uses and leaks 1KB of memory. Leaked: {}".format(
        len(leaked)
    )
