from flask import Flask
from providers.redis import RedisProvider
from providers.mongo import MongoProvider
from providers.in_memory import InMemoryProvider
from providers.postgres_direct import PostgresDirectProvider
from experiments.hit_count import HitCountExperiment
from experiments.single_entity import SingleEntityExperiment


app = Flask(__name__)

providers = [
    RedisProvider(),
    MongoProvider(),
    InMemoryProvider(),
    PostgresDirectProvider(),
]

experiments = [HitCountExperiment(), SingleEntityExperiment()]


@app.route("/")
def overview():

    all_results = []

    for provider in providers:

        all_results.append(" ")
        all_results.append(" ")

        all_results.append("TESTING {}".format(provider.name))

        for experiment in experiments:
            all_results.append("---")
            all_results.append("Experiment: {}".format(experiment.name))

            exp_results = experiment.run_the_experiment(provider)
            all_results.extend(exp_results)

    return "<br />".join(all_results)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
