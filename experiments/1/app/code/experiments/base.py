from abc import ABC, abstractmethod


class Experiment(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def run_the_experiment(self, provider):
        pass
