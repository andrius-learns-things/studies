from flask import Flask
from providers.redis import RedisProvider
from providers.mongo import MongoProvider
from providers.in_memory import InMemoryProvider
from providers.postgres_direct import PostgresDirectProvider
from experiment import run_the_experiment


app = Flask(__name__)
providers = [
    RedisProvider(),
    MongoProvider(),
    InMemoryProvider(),
    PostgresDirectProvider()
]


@app.route('/')
def overview():

    all_results = []

    for provider in providers:
        results = run_the_experiment(provider)

        all_results.append(" ")
        all_results.extend(results)

    return '<br />'.join(all_results)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
