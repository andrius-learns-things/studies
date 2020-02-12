from providers.base import Provider


def run_the_experiment(provider: Provider):
    result = []
    result.append('Experiment for {}'.format(provider.name))
    result.append('Hit count {}'.format(provider.get_hit_count()))
    return result
