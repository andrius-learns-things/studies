from abc import ABC, abstractmethod
from time import time


class Experiment(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def run_the_experiment(self, provider):
        pass

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
