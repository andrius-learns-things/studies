from flask import Flask
from flask import jsonify
from flask_restplus import Api, Resource

flask_app = Flask(__name__)
app = Api(app=flask_app)

ns = app.namespace("random_strings", description="Random strings")


@ns.route("/")
class MainClass(Resource):
    def get(self):
        strings = ["AAA", "BBB", "CCC"]
        return jsonify(strings)


if __name__ == "__main__":
    flask_app.run(host="0.0.0.0", debug=True)
