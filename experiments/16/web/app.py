from flask import Flask
import time


app = Flask(__name__)


@app.route("/")
def empty():
    time.sleep(1)
    return "Empty endpoint"


@app.route("/use-and-release")
def use_and_release():
    long_string, length = _get_long_string()
    time.sleep(1)
    return "Endpoint, which uses and releases {}MB of memory.".format(length)


leaked = []


@app.route("/use-and-leak")
def use_and_leak():
    long_string, length = _get_long_string()
    time.sleep(1)
    leaked.append(long_string)
    return (
        "Endpoint, which uses and leaks {}B of memory. Leaked number of times: {}."
    ).format(length, len(leaked))


def _get_long_string():
    long_string = (
        "__________".replace("_", "----------")
        .replace("-", "__________")
        .replace("_", "----------")
        .replace("-", "__________")
        .replace("_", "----------")
    )
    length = len(long_string) / 1000000
    return long_string, length
