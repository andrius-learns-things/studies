from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint


app = Flask(__name__)


swagger_url = "/swagger"
api_url = "/static/swagger.json"

blueprint = get_swaggerui_blueprint(
    swagger_url, api_url, config={"app_name": "Trivial API"}
)

app.register_blueprint(blueprint, url_prefix=swagger_url)


@app.route("/")
def overview():
    output = "Minimal Flask app"
    return output


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
