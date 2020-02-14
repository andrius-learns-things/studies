from .base import Experiment


class SingleEntityExperiment(Experiment):
    @property
    def name(self):
        return "Single entity experiment"

    def run_the_experiment(self, provider):
        return ["-"]
