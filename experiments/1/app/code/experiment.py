from providers.base import Provider


def run_the_experiment(provider: Provider):
    result = []
    result.append("TESTING {}".format(provider.name))
    msg = "Total experiments made: {}".format(provider.get_hit_count())
    result.append(msg)
    return result
