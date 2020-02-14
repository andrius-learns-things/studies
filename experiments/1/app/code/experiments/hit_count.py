from .base import Experiment


class HitCountExperiment(Experiment):
    @property
    def name(self):
        return "Get hit count"

    def run_the_experiment(self, provider):
        return ["Hit count: {}".format(provider.get_hit_count())]
