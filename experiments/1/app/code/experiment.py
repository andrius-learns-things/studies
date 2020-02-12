from providers.base import Provider


def run_the_experiment(provider: Provider):
    result = []
    result.append('TESTING {}'.format(provider.name))
    result.append('Total experiments made: {}'.format(provider.get_hit_count()))
    return result
