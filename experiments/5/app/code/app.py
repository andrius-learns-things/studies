from flask import Flask
from flask import jsonify
from graphql import schema

app = Flask(__name__)


@app.route("/")
def get_root():

    query_string = "{ hello }"
    result = schema.execute(query_string)
    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
