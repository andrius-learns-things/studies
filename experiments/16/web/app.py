from flask import Flask
import time


app = Flask(__name__)

LONG_STRING = (
    "__________".replace("_", "----------")
    .replace("-", "__________")
    .replace("_", "----------")
    .replace("-", "__________")
    .replace("_", "----------")
)
STRING_LENGTH_IN_MB = len(LONG_STRING) / 1000000


@app.route("/")
def empty():
    time.sleep(1)
    return "Empty endpoint"


@app.route("/use-and-release")
def use_and_release():
    _get_long_string()
    time.sleep(1)
    return "Endpoint, which uses and releases {}MB of memory.".format(
        STRING_LENGTH_IN_MB
    )


leaked = []


@app.route("/use-and-leak")
def use_and_leak():
    a = _get_long_string()
    time.sleep(1)
    leaked.append(a)
    return (
        "Endpoint, which uses and leaks {}B of memory. Leaked number of times: {}."
    ).format(STRING_LENGTH_IN_MB, len(leaked))


def _get_long_string():
    a = LONG_STRING + ""
    return a
