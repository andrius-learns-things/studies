from .base import Experiment
from time import time

NUM = 10000


class TwoEntitiesJoinedExperiment(Experiment):
    @property
    def name(self):
        return "Two entities joined experiment"

    def run_the_experiment(self, provider):

        output = []

        self._experiment_init(provider, output)

        return output

    def _experiment_init(self, provider, output):
        def func():
            pass
            # provider.ensure_empty_person_structure()

        self._measure(output, "Init", func)

    def _measure(self, output, title, function):

        output.append("-")
        output.append("Measuring {}".format(title))

        start_time = time()
        function()
        end_time = time()

        elapsed_time = round(
            (end_time - start_time) * 1000
        )  # x1000 to get ms from secs

        output.append("Time: {}ms".format(elapsed_time))
