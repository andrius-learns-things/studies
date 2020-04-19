from flask import Flask

app = Flask(__name__)


@app.route("/")
def get_root():
    return "Let's say this app returns very long text. This will be handy in testing how app looks in smaller resolutions."


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
