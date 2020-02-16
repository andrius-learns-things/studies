from flask import Flask
import pdb

app = Flask(__name__)


@app.route("/")
def index():
    test = "Welcome **** "
    pdb.set_trace()
    return test


if __name__ == "__main__":
    app.secret_key = "qwertyuiop1234567890!@#$%^&*()ZXCVBNM<>?ASDFGHJK"
    app.run()
